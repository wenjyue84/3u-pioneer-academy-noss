"""Validate 30/70 Knowledge/Performance training hours distribution across all CUs.

Usage:
    uv run python scripts/validate_training_distribution.py all_subjects
    uv run python scripts/validate_training_distribution.py bev aesthetic it tuinalogy

Exit codes:
    0  - all CUs compliant (25-35% knowledge allocation)
    1  - one or more CUs non-compliant or hours missing
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).parents[1]

SUBJECTS: dict[str, str] = {
    "bev": "bev-diagnostic-rectification",
    "aesthetic": "aesthetic-services",
    "it": "it-computer-system",
    "tuinalogy": "tuinalogy-services",
}

# Compliance band: flag if knowledge % outside [25%, 35%]
KNOWLEDGE_MIN = 25.0
KNOWLEDGE_MAX = 35.0
KNOWLEDGE_TARGET = 30.0


@dataclass
class CUDistribution:
    subject: str
    cu: str
    theory_hours: float
    practical_hours: float
    source_teori: Path
    source_amali: Path
    warnings: list[str] = field(default_factory=list)

    @property
    def total_hours(self) -> float:
        return self.theory_hours + self.practical_hours

    @property
    def knowledge_pct(self) -> float:
        if self.total_hours == 0:
            return 0.0
        return self.theory_hours / self.total_hours * 100

    @property
    def performance_pct(self) -> float:
        return 100.0 - self.knowledge_pct

    @property
    def compliant(self) -> bool:
        if self.total_hours == 0:
            return False
        return KNOWLEDGE_MIN <= self.knowledge_pct <= KNOWLEDGE_MAX


# ---------------------------------------------------------------------------
# Duration parsers — ordered from most specific to most generic
# ---------------------------------------------------------------------------

_PATTERNS_THEORY = [
    # IT: | **Jumlah Jam Teori / Theory Hours** | 90 hours (30% …) |
    re.compile(r"Jumlah\s+Jam\s+Teori[^|]*\|\s*(\d+(?:\.\d+)?)\s*hours?", re.IGNORECASE),
    # Aesthetic table: | Tempoh Teori / Theory Duration | 8 hours |
    re.compile(r"Tempoh\s+Teori[^|]*\|\s*(\d+(?:\.\d+)?)\s*hours?", re.IGNORECASE),
    # Aesthetic inline bold: **Theory Duration:** 8 hours (colon may be inside bold)
    re.compile(r"Theory\s+Duration[*:]{0,3}\s*(\d+(?:\.\d+)?)\s*hours?", re.IGNORECASE),
    # BEV: ## Total Theory Session Duration: approximately 370 minutes (6 hours 10 minutes)
    re.compile(
        r"Total\s+Theory\s+Session\s+Duration[^(]*\(\s*(\d+(?:\.\d+)?)\s*hours?",
        re.IGNORECASE,
    ),
    # BEV compact: ## Total: approximately 195 minutes (3 hours 15 minutes)
    re.compile(r"^#{1,4}\s+Total[^(]*\(\s*(\d+(?:\.\d+)?)\s*hours?", re.IGNORECASE | re.MULTILINE),
    # BEV minutes-only: ## Total: approximately 195 minutes
    re.compile(r"^#{1,4}\s+Total[^(]*?(\d+)\s+minutes\s*$", re.IGNORECASE | re.MULTILINE),
    # Tuinalogy Chinese: **时数：** 72 小时
    re.compile(r"\*{1,2}时数[：:]\*{0,2}\s*(\d+(?:\.\d+)?)\s*小时", re.IGNORECASE),
]

_PATTERNS_PRACTICAL = [
    # IT
    re.compile(r"Jumlah\s+Jam\s+Amali[^|]*\|\s*(\d+(?:\.\d+)?)\s*hours?", re.IGNORECASE),
    # Aesthetic table
    re.compile(r"Tempoh\s+Amali[^|]*\|\s*(\d+(?:\.\d+)?)\s*hours?", re.IGNORECASE),
    # Aesthetic inline bold: **Practical Duration:** 24 hours
    re.compile(r"Practical\s+Duration[*:]{0,3}\s*(\d+(?:\.\d+)?)\s*hours?", re.IGNORECASE),
    # BEV with named label
    re.compile(
        r"Total\s+Practical\s+Session\s+Duration[^(]*\(\s*(\d+(?:\.\d+)?)\s*hours?",
        re.IGNORECASE,
    ),
    # BEV compact
    re.compile(r"^#{1,4}\s+Total[^(]*\(\s*(\d+(?:\.\d+)?)\s*hours?", re.IGNORECASE | re.MULTILINE),
    # BEV minutes-only
    re.compile(r"^#{1,4}\s+Total[^(]*?(\d+)\s+minutes\s*$", re.IGNORECASE | re.MULTILINE),
    # Tuinalogy Chinese
    re.compile(r"\*{1,2}时数[：:]\*{0,2}\s*(\d+(?:\.\d+)?)\s*小时", re.IGNORECASE),
]


def _extract_hours(content: str, patterns: list[re.Pattern[str]]) -> float | None:
    """Return the first numeric match (in hours) from the content."""
    for pat in patterns:
        m = pat.search(content)
        if m:
            value = float(m.group(1))
            # If matched a minutes-only pattern (last two patterns), convert
            if "minutes" in pat.pattern and "hours" not in pat.pattern:
                value = round(value / 60, 4)
            return value
    return None


def parse_duration_from_file(path: Path, is_practical: bool = False) -> float | None:
    """Parse theory or practical duration (hours) from a PM lesson plan file."""
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return None
    patterns = _PATTERNS_PRACTICAL if is_practical else _PATTERNS_THEORY
    return _extract_hours(content, patterns)


# ---------------------------------------------------------------------------
# Subject scanner
# ---------------------------------------------------------------------------


def _cu_sort_key(name: str) -> tuple[str, int]:
    m = re.search(r"([A-Z]+)(\d+)", name, re.IGNORECASE)
    if m:
        return (m.group(1).upper(), int(m.group(2)))
    return (name, 0)


def scan_subject(subject_key: str) -> list[CUDistribution]:
    """Scan all CU folders in a subject and return distribution data."""
    folder_name = SUBJECTS.get(subject_key)
    if not folder_name:
        return []
    subject_dir = ROOT / folder_name
    if not subject_dir.exists():
        return []

    results: list[CUDistribution] = []
    cu_dirs = sorted(
        [d for d in subject_dir.iterdir() if d.is_dir() and not d.name.startswith("_")],
        key=lambda d: _cu_sort_key(d.name),
    )

    for cu_dir in cu_dirs:
        teori_path = cu_dir / "PM-teori.md"
        amali_path = cu_dir / "PM-amali.md"

        if not teori_path.exists() and not amali_path.exists():
            continue

        warns: list[str] = []
        theory_hrs = 0.0
        practical_hrs = 0.0

        if teori_path.exists():
            val = parse_duration_from_file(teori_path, is_practical=False)
            if val is None:
                warns.append("theory hours not found in PM-teori.md")
            else:
                theory_hrs = val
        else:
            warns.append("PM-teori.md missing")

        if amali_path.exists():
            val = parse_duration_from_file(amali_path, is_practical=True)
            if val is None:
                warns.append("practical hours not found in PM-amali.md")
            else:
                practical_hrs = val
        else:
            warns.append("PM-amali.md missing")

        results.append(
            CUDistribution(
                subject=subject_key,
                cu=cu_dir.name,
                theory_hours=theory_hrs,
                practical_hours=practical_hrs,
                source_teori=teori_path,
                source_amali=amali_path,
                warnings=warns,
            )
        )

    return results


# ---------------------------------------------------------------------------
# Report generator
# ---------------------------------------------------------------------------


def compute_compliance(distributions: list[CUDistribution]) -> dict[str, object]:
    """Return summary stats and compliance flags."""
    total_theory = sum(d.theory_hours for d in distributions)
    total_practical = sum(d.practical_hours for d in distributions)
    total_all = total_theory + total_practical
    cumulative_pct = (total_theory / total_all * 100) if total_all > 0 else 0.0

    non_compliant = [d for d in distributions if not d.compliant]
    return {
        "total_theory": total_theory,
        "total_practical": total_practical,
        "total_hours": total_all,
        "cumulative_knowledge_pct": round(cumulative_pct, 1),
        "non_compliant_cus": non_compliant,
        "compliant_count": len(distributions) - len(non_compliant),
        "total_count": len(distributions),
    }


def generate_report(distributions: list[CUDistribution], verbose: bool = True) -> bool:
    """Print the compliance report; return True if all CUs compliant."""
    if not distributions:
        print("  No CU data found.")
        return True

    by_subject: dict[str, list[CUDistribution]] = {}
    for d in distributions:
        by_subject.setdefault(d.subject, []).append(d)

    all_compliant = True

    for subj, cus in by_subject.items():
        summary = compute_compliance(cus)
        status_icon = "✓" if summary["cumulative_knowledge_pct"] >= KNOWLEDGE_MIN and summary["cumulative_knowledge_pct"] <= KNOWLEDGE_MAX else "✗"  # type: ignore[operator]
        print(f"\n{'='*60}")
        print(f"Subject: {SUBJECTS.get(subj, subj)}")
        print(f"{'='*60}")

        for d in cus:
            if d.total_hours == 0:
                row_icon = "?"
                all_compliant = False
            elif d.compliant:
                row_icon = "✓"
            else:
                row_icon = "✗"
                all_compliant = False

            print(
                f"  [{row_icon}] {d.cu:6s}  "
                f"Theory: {d.theory_hours:6.1f}h  "
                f"Practical: {d.practical_hours:6.1f}h  "
                f"K%: {d.knowledge_pct:5.1f}%  "
                f"P%: {d.performance_pct:5.1f}%"
            )
            for w in d.warnings:
                print(f"         WARNING: {w}")

        cumulative_pct = summary["cumulative_knowledge_pct"]
        print(
            f"\n  [{status_icon}] Cumulative — "
            f"Theory: {summary['total_theory']:.1f}h  "
            f"Practical: {summary['total_practical']:.1f}h  "
            f"K%: {cumulative_pct}%  "
            f"(target: {KNOWLEDGE_TARGET}%, range: {KNOWLEDGE_MIN}-{KNOWLEDGE_MAX}%)"
        )
        print(
            f"  Compliant CUs: {summary['compliant_count']}/{summary['total_count']}"
        )

    return all_compliant


# ---------------------------------------------------------------------------
# .spiral/monitor integration
# ---------------------------------------------------------------------------

MONITOR_STATE_PATH = ROOT / ".spiral" / "_monitor_state.json"


def update_monitor_kp_ratio(distributions: list[CUDistribution]) -> None:
    """Append K/P ratio health-check entry to .spiral/_monitor_state.json."""
    import json

    if not MONITOR_STATE_PATH.exists():
        return

    state: dict[str, object] = {}
    try:
        state = json.loads(MONITOR_STATE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        pass

    from datetime import datetime, timezone

    total_theory = sum(d.theory_hours for d in distributions)
    total_practical = sum(d.practical_hours for d in distributions)
    total_all = total_theory + total_practical
    cumulative_pct = round((total_theory / total_all * 100) if total_all > 0 else 0.0, 1)
    non_compliant = [f"{d.subject}/{d.cu}" for d in distributions if not d.compliant]

    state["kp_ratio_health"] = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cumulative_knowledge_pct": cumulative_pct,
        "target_pct": KNOWLEDGE_TARGET,
        "compliant_range": [KNOWLEDGE_MIN, KNOWLEDGE_MAX],
        "non_compliant_cus": non_compliant,
        "status": "ok" if not non_compliant else "drift",
    }

    try:
        MONITOR_STATE_PATH.write_text(
            json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8"
        )
    except OSError:
        pass


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate 30/70 K/P training hours distribution"
    )
    parser.add_argument(
        "subjects",
        nargs="+",
        help="Subject keys (bev, aesthetic, it, tuinalogy) or 'all_subjects'",
    )
    parser.add_argument("--no-monitor", action="store_true", help="Skip .spiral/monitor update")
    args = parser.parse_args(argv)

    keys = list(SUBJECTS.keys()) if "all_subjects" in args.subjects else args.subjects
    unknown = [k for k in keys if k not in SUBJECTS]
    if unknown:
        print(f"ERROR: Unknown subjects: {', '.join(unknown)}", file=sys.stderr)
        print(f"Valid subjects: {', '.join(SUBJECTS.keys())}", file=sys.stderr)
        return 1

    all_distributions: list[CUDistribution] = []
    for key in keys:
        all_distributions.extend(scan_subject(key))

    compliant = generate_report(all_distributions)

    if not args.no_monitor:
        update_monitor_kp_ratio(all_distributions)

    if not compliant:
        print("\nWARNING: One or more CUs have K/P distribution drift.", file=sys.stderr)
        return 1

    print("\nAll CUs comply with 30/70 K/P distribution requirement.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
