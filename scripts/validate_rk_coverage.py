"""Validate that every NOSS CoCU Related Knowledge item has a supporting KP file.

Usage:
    uv run python scripts/validate_rk_coverage.py bev aesthetic it
    uv run python scripts/validate_rk_coverage.py all

Exit codes:
    0  - 100% coverage (all RK items found in KP files)
    1  - partial coverage or missing NOSS extract
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))

from scripts.rk_parser import RKItem, parse_noss_extract  # noqa: E402

ROOT = Path(__file__).parents[1]

SUBJECTS: dict[str, str] = {
    "bev": "bev-diagnostic-rectification",
    "aesthetic": "aesthetic-services",
    "it": "it-computer-system",
}

# Match section headings that contain RK codes (e.g. "### 1.1" or "## K3")
_RK_HEADING = re.compile(r"^#{1,5}\s+(\d+\.\d+)\b|^#{1,5}\s+(K\d+)\b", re.MULTILINE)


def _cu_from_dirname(name: str) -> str:
    m = re.search(r"C(\d+)", name, re.IGNORECASE)
    return f"C{int(m.group(1)):02d}" if m else name


def scan_kp_files(subject_dir: Path) -> dict[str, list[tuple[Path, set[str]]]]:
    """Return {cu_code: [(kp_path, {rk_codes_found_in_content})]} for all KP files."""
    result: dict[str, list[tuple[Path, set[str]]]] = {}
    for cu_dir in sorted(subject_dir.iterdir()):
        if not cu_dir.is_dir() or cu_dir.name.startswith("_"):
            continue
        cu_code = _cu_from_dirname(cu_dir.name)
        kp_files = sorted(cu_dir.glob("KP-*.md"))
        entries: list[tuple[Path, set[str]]] = []
        for kp in kp_files:
            content = kp.read_text(encoding="utf-8")
            codes = {m.group(1) or m.group(2) for m in _RK_HEADING.finditer(content)}
            entries.append((kp, codes))
        if entries:
            result.setdefault(cu_code, []).extend(entries)
    return result


def build_coverage_report(
    rk_items: list[RKItem],
    kp_index: dict[str, list[tuple[Path, set[str]]]],
) -> dict[str, list[object]]:
    """Compare RK items to KP file content, return covered/orphaned/undocumented."""
    covered: list[dict[str, str]] = []
    orphaned: list[dict[str, str]] = []
    undocumented: list[str] = []

    rk_by_cu: dict[str, list[RKItem]] = {}
    for item in rk_items:
        rk_by_cu.setdefault(item.cu, []).append(item)

    for cu, items in rk_by_cu.items():
        kp_list = kp_index.get(cu, [])
        all_codes: set[str] = {c for _, codes in kp_list for c in codes}
        for item in items:
            if item.code in all_codes:
                try:
                    kp_str = str(next(p for p, codes in kp_list if item.code in codes).relative_to(ROOT))
                except (StopIteration, ValueError):
                    kp_str = "?"
                covered.append({"cu": cu, "code": item.code, "file": kp_str})
            else:
                orphaned.append({"cu": cu, "code": item.code, "description": item.description})

    all_noss_codes = {item.code for item in rk_items}
    for _cu, kp_list in kp_index.items():
        for kp_path, codes in kp_list:
            for c in sorted(codes - all_noss_codes):
                try:
                    label = str(kp_path.relative_to(ROOT))
                except ValueError:
                    label = str(kp_path)
                undocumented.append(f"{label} -> {c}")

    return {"covered": covered, "orphaned": orphaned, "undocumented": undocumented}


def _print_report(subject: str, report: dict[str, list[object]]) -> None:
    covered = report["covered"]
    orphaned = report["orphaned"]
    undocumented = report["undocumented"]
    total = len(covered) + len(orphaned)
    pct = f"{100 * len(covered) // total}%" if total else "N/A"
    print(f"\n=== {subject.upper()} RK Coverage: {len(covered)}/{total} ({pct}) ===")
    for item in covered:
        assert isinstance(item, dict)
        print(f"  [OK]      {item['cu']} {item['code']} -> {item['file']}")
    for item in orphaned:
        assert isinstance(item, dict)
        print(f"  [MISSING] {item['cu']} {item['code']}: {item['description'][:60]}", file=sys.stderr)
    for entry in undocumented:
        print(f"  [UNDOC]   {entry}", file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate NOSS RK coverage against KP files.")
    parser.add_argument("subjects", nargs="+", metavar="SUBJECT",
                        help="Subjects to validate: bev aesthetic it all")
    args = parser.parse_args()

    subject_keys = list(SUBJECTS.keys()) if "all" in args.subjects else args.subjects
    invalid = [s for s in subject_keys if s not in SUBJECTS]
    if invalid:
        print(f"Unknown subjects: {invalid}. Valid: {list(SUBJECTS)}", file=sys.stderr)
        return 2

    has_gap = False
    for subj in subject_keys:
        subject_dir = ROOT / SUBJECTS[subj]
        noss_file = subject_dir / "00-noss-extract.md"
        if not noss_file.exists():
            print(f"[WARN] No NOSS extract for {subj}: {noss_file}", file=sys.stderr)
            has_gap = True
            continue
        rk_items = parse_noss_extract(noss_file, subj)
        kp_index = scan_kp_files(subject_dir)
        report = build_coverage_report(rk_items, kp_index)
        _print_report(subj, report)
        if report["orphaned"]:
            has_gap = True

    return 1 if has_gap else 0


if __name__ == "__main__":
    sys.exit(main())
