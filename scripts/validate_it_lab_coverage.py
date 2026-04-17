"""IT-020 Hands-On Lab Activity Coverage Validator.

Reports lab coverage % by level and lists unmapped KPs with suggestions.

Usage:
    uv run python scripts/validate_it_lab_coverage.py [--root PATH] [--json]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
MAPPING_FILE = "it-computer-system/lab-activity-mapping.json"


def analyze_kp_lab_map(
    root: Path,
) -> dict[str, dict[str, object]]:
    """Return per-level stats: total, mapped, unmapped KP list."""
    data = json.loads(
        (root / MAPPING_FILE).read_text(encoding="utf-8"),
    )
    results: dict[str, dict[str, object]] = {}
    suggestions = data.get("_unmapped_suggestions", {})
    for level in ("L3", "L4", "L5"):
        cus = data.get(level, {})
        total = 0
        mapped = 0
        unmapped: list[dict[str, str]] = []
        for cu_id, labs in sorted(cus.items()):
            for i, lab in enumerate(labs):
                kp_num = i + 1
                kp_id = f"{level}-{cu_id}-KP{kp_num:02d}"
                total += 1
                if lab is not None:
                    mapped += 1
                else:
                    sug = suggestions.get(kp_id, "TBD")
                    unmapped.append({"kp": kp_id, "suggestion": sug})
        pct = (mapped / total * 100) if total else 0
        results[level] = {
            "total": total, "mapped": mapped,
            "pct": round(pct, 1), "unmapped": unmapped,
        }
    return results


def report_coverage_gaps(root: Path) -> str:
    """Return formatted coverage report string."""
    stats = analyze_kp_lab_map(root)
    lines = ["IT-020 LAB ACTIVITY COVERAGE REPORT", "=" * 40]
    total_all = 0
    mapped_all = 0
    all_unmapped: list[dict[str, str]] = []
    for level in ("L3", "L4", "L5"):
        s = stats[level]
        lines.append(
            f"\n{level}: {s['mapped']}/{s['total']} KPs mapped ({s['pct']}%)",
        )
        total_all += int(str(s["total"]))
        mapped_all += int(str(s["mapped"]))
        for u in s["unmapped"]:  # type: ignore[union-attr]
            all_unmapped.append(u)  # type: ignore[arg-type]
    pct_all = round(mapped_all / total_all * 100, 1) if total_all else 0
    lines.append(f"\nOVERALL: {mapped_all}/{total_all} ({pct_all}%)")
    lines.append(f"UNMAPPED KPs: {len(all_unmapped)}")
    if all_unmapped:
        lines.append("\nSuggested lab activities for unmapped KPs:")
        for u in all_unmapped:
            lines.append(f"  {u['kp']}: {u['suggestion']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="IT-020 lab coverage")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.json:
        print(json.dumps(analyze_kp_lab_map(args.root), indent=2))
    else:
        print(report_coverage_gaps(args.root))


if __name__ == "__main__":
    main()
