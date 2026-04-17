"""rubric-standardizer.py — Validate and reformat PA rubric tables (US-041).

Usage:
    uv run python _tools/rubric-standardizer.py [--report]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Column header aliases mapped to canonical names
_ALIASES: dict[str, str] = {
    # Competency Dimension
    "competency dimension": "dimension",
    "criteria": "dimension",
    "评分项": "dimension",
    "kriteria": "dimension",
    "dimension": "dimension",
    "criterion": "dimension",
    # Level Descriptor
    "level descriptor": "descriptor",
    "descriptor": "descriptor",
    "description": "descriptor",
    "满分": "descriptor",
    "standard": "descriptor",
    "level": "descriptor",
    # Score
    "score": "score",
    "marks": "score",
    "评分": "score",
    "markah": "score",
    "points": "score",
    "max": "score",
    # Evidence
    "evidence": "evidence",
    "evidence required": "evidence",
    "observable": "evidence",
    "proof": "evidence",
    "证据": "evidence",
}

_REQUIRED = {"dimension", "descriptor", "score", "evidence"}


def _parse_table_headers(header_row: str) -> list[str]:
    """Return canonical column names from a markdown table header row."""
    cells = [c.strip().lower() for c in header_row.strip().strip("|").split("|")]
    return [_ALIASES.get(c, c) for c in cells if c]


def _table_blocks(text: str) -> list[list[str]]:
    """Extract all markdown table blocks (list of row strings) from text."""
    tables: list[list[str]] = []
    current: list[str] = []
    for line in text.splitlines():
        if re.match(r"^\s*\|", line):
            current.append(line)
        else:
            if len(current) >= 2:
                tables.append(current)
            current = []
    if len(current) >= 2:
        tables.append(current)
    return tables


def _is_separator(row: str) -> bool:
    return bool(re.match(r"^\s*\|[\s|:-]+\|\s*$", row))


def _data_rows(block: list[str]) -> list[str]:
    """Return data rows (skip header + separator rows)."""
    rows = [r for r in block if not _is_separator(r)]
    return rows[1:] if rows else []


def validate_rubric_format(path: Path) -> dict[str, object]:
    """Validate a PA file against the standard rubric format.

    Returns a dict with keys:
        file (str), compliant (bool), issues (list[str]),
        rubric_table_count (int), compliant_tables (int)
    """
    text = path.read_text(encoding="utf-8")
    tables = _table_blocks(text)

    if not tables:
        return {
            "file": str(path.relative_to(ROOT)),
            "compliant": False,
            "issues": ["No markdown table found in PA file"],
            "rubric_table_count": 0,
            "compliant_tables": 0,
        }

    issues: list[str] = []
    compliant_count = 0

    for i, block in enumerate(tables, 1):
        if not block:
            continue
        headers = _parse_table_headers(block[0])
        canonical = set(headers)
        missing = _REQUIRED - canonical
        data = _data_rows(block)

        if missing:
            issues.append(f"Table {i}: missing columns {sorted(missing)}")
            continue
        if len(data) < 2:
            issues.append(f"Table {i}: fewer than 2 data rows ({len(data)} found)")
            continue
        compliant_count += 1

    return {
        "file": str(path.relative_to(ROOT)),
        "compliant": compliant_count > 0,
        "issues": issues,
        "rubric_table_count": len(tables),
        "compliant_tables": compliant_count,
    }


def reformat_rubric(path: Path) -> str:
    """Return file text with a standard-format rubric appended if none exists.

    Only adds a placeholder rubric; does not modify existing content.
    """
    result = validate_rubric_format(path)
    if result["compliant"]:
        return path.read_text(encoding="utf-8")

    placeholder = (
        "\n\n---\n\n"
        "## Standard Rubric (Auto-generated placeholder — please fill in)\n\n"
        "| Competency Dimension | Level Descriptor | Score | Evidence |\n"
        "|----------------------|------------------|-------|----------|\n"
        "| *(criterion 1)* | *(description of competent performance)* | 0 | *(observable proof)* |\n"
        "| *(criterion 2)* | *(description of competent performance)* | 0 | *(observable proof)* |\n"
    )
    return path.read_text(encoding="utf-8") + placeholder


def generate_compliance_report(root: Path = ROOT) -> dict[str, object]:
    """Scan all PA*.md files and return a compliance report."""
    pa_files = sorted(root.glob("**/PA*.md"))
    results = [validate_rubric_format(p) for p in pa_files]

    total = len(results)
    compliant = sum(1 for r in results if r["compliant"])
    pct = round(100 * compliant / total, 1) if total else 0.0

    non_compliant = [r for r in results if not r["compliant"]]

    return {
        "total_files": total,
        "compliant_files": compliant,
        "compliance_pct": pct,
        "non_compliant": non_compliant,
        "all_results": results,
    }


def _print_report(report: dict[str, object]) -> None:
    print(f"\n=== PA Rubric Compliance Report ===")
    print(f"Files scanned : {report['total_files']}")
    print(f"Compliant     : {report['compliant_files']}")
    print(f"Compliance %  : {report['compliance_pct']}%")

    non_compliant = report["non_compliant"]  # type: ignore[index]
    if non_compliant:
        print(f"\nNon-compliant files ({len(non_compliant)}):")
        for r in non_compliant:
            print(f"  {r['file']}")
            for issue in r["issues"]:  # type: ignore[union-attr]
                print(f"    - {issue}")
    else:
        print("\nAll PA files are compliant.")


if __name__ == "__main__":
    report = generate_compliance_report()
    _print_report(report)
    sys.exit(0 if report["compliance_pct"] == 100.0 else 1)
