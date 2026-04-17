"""Coverage validator for NOSS-to-WIM cross-reference matrix.

Usage:
    uv run python _tools/coverage_validator.py --subject BEV --output report.txt
    uv run python _tools/coverage_validator.py --subject all --output report.txt
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

MATRIX_PATH = Path(__file__).parent.parent / "_data" / "coverage_matrix.json"
SUBJECT_KEY_MAP = {
    "bev": "BEV",
    "aesthetic": "Aesthetic",
    "it": "IT",
}


def check_coverage(subject_key: str, subject_data: dict, project_root: Path) -> dict:
    """Check file existence for one subject and return gap report."""
    folder = project_root / subject_data["folder"]
    gaps: list[dict] = []
    covered: list[dict] = []

    for cu_id, cu_data in subject_data["CUs"].items():
        # Check work activities → KK files
        for wa in cu_data.get("work_activities", []):
            kk_path = folder / wa["kk_file"]
            entry = {
                "type": "work_activity",
                "noss_code": wa["noss_code"],
                "title": wa["title"],
                "expected_file": wa["kk_file"],
                "cu": cu_id,
            }
            if kk_path.exists():
                entry["status"] = "covered"
                covered.append(entry)
            else:
                entry["status"] = "missing"
                gaps.append(entry)

        # Check related knowledge → KP files
        for rk in cu_data.get("related_knowledge", []):
            kp_path = folder / rk["kp_file"]
            entry = {
                "type": "related_knowledge",
                "noss_code": rk["noss_code"],
                "title": rk["title"],
                "expected_file": rk["kp_file"],
                "cu": cu_id,
            }
            if kp_path.exists():
                entry["status"] = "covered"
                covered.append(entry)
            else:
                entry["status"] = "missing"
                gaps.append(entry)

        # Check assessments → KA/PA files
        for assess_type, assess_file in cu_data.get("assessments", {}).items():
            assess_path = folder / assess_file
            entry = {
                "type": f"assessment_{assess_type}",
                "noss_code": f"{subject_data['noss_code']}-{cu_id}-{assess_type}",
                "title": f"{assess_type} Assessment",
                "expected_file": assess_file,
                "cu": cu_id,
            }
            if assess_path.exists():
                entry["status"] = "covered"
                covered.append(entry)
            else:
                entry["status"] = "missing"
                gaps.append(entry)

    total = len(covered) + len(gaps)
    coverage_pct = (len(covered) / total * 100) if total > 0 else 100.0

    return {
        "subject": subject_key,
        "noss_code": subject_data["noss_code"],
        "folder": subject_data["folder"],
        "total_documents": total,
        "covered": len(covered),
        "not_covered": len(gaps),
        "coverage_pct": round(coverage_pct, 1),
        "gaps": gaps,
    }


def format_report(results: list[dict]) -> str:
    """Format gap analysis as human-readable text."""
    lines = ["=" * 60, "NOSS-to-WIM Coverage Gap Analysis Report", "=" * 60, ""]

    any_gaps = False
    for result in results:
        lines.append(f"Subject: {result['subject']} ({result['noss_code']})")
        lines.append(f"Folder:  {result['folder']}")
        lines.append(
            f"Coverage: {result['covered']}/{result['total_documents']} "
            f"({result['coverage_pct']}%)"
        )

        if result["gaps"]:
            any_gaps = True
            lines.append(f"\nNot Covered ({len(result['gaps'])} items):")
            for gap in result["gaps"]:
                lines.append(
                    f"  [{gap['cu']}] {gap['noss_code']} — "
                    f"{gap['title']} → MISSING: {gap['expected_file']}"
                )
        else:
            lines.append("  All documents covered.")

        lines.append("")

    lines.append("=" * 60)
    status = "GAPS FOUND — action required" if any_gaps else "PASS — full coverage"
    lines.append(f"Overall Status: {status}")
    lines.append("=" * 60)
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate NOSS-to-WIM coverage matrix"
    )
    parser.add_argument(
        "--subject",
        required=True,
        choices=["BEV", "Aesthetic", "IT", "all"],
        help="Subject to validate (case-insensitive) or 'all'",
    )
    parser.add_argument("--output", help="Output file path for gap report (text)")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).parent.parent),
        help="Project root directory",
    )
    args = parser.parse_args()

    matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))
    project_root = Path(args.root)

    subject_arg = args.subject.lower()
    if subject_arg == "all":
        subjects_to_check = list(matrix.keys())
    else:
        key = SUBJECT_KEY_MAP.get(subject_arg, args.subject)
        if key not in matrix:
            print(f"ERROR: Subject '{args.subject}' not found in matrix.", file=sys.stderr)
            sys.exit(2)
        subjects_to_check = [key]

    results = [
        check_coverage(key, matrix[key], project_root) for key in subjects_to_check
    ]

    report_text = format_report(results)

    if args.output:
        Path(args.output).write_text(report_text, encoding="utf-8")
        print(f"Report written to: {args.output}")
    else:
        print(report_text)

    total_gaps = sum(r["not_covered"] for r in results)
    if total_gaps > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
