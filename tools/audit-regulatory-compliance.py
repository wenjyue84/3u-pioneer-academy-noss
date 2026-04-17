#!/usr/bin/env python3
"""
audit-regulatory-compliance.py — Malaysian T&CM Regulatory Compliance Audit Tool.

Scans Tuinalogy WIM documents against Malaysian regulatory frameworks:
  - T&CM Act 2013 (registration, scope of practice, consent)
  - OSHA 1994 (workplace safety, ergonomics, infection control)
  - PDPA 2010 (patient data, confidentiality)
  - MOH Code of Ethics 2007 (professional conduct)

Usage:
    python tools/audit-regulatory-compliance.py <directory>
    python tools/audit-regulatory-compliance.py tuinalogy-services/ --output compliance-gaps-report.csv
    python tools/audit-regulatory-compliance.py tuinalogy-services/ --regulation "T&CM Act 2013"

Output CSV columns:
    Regulation | Section | Required Coverage | Files Addressing | Status | Recommendation
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Matrix parser
# ---------------------------------------------------------------------------

def parse_compliance_matrix(matrix_path: Path) -> list[dict[str, str]]:
    """Parse regulatory-compliance-matrix.md into a list of rule dicts.

    Each rule dict has keys: regulation, section, keywords (list[str]),
    required_coverage, verification_points.
    """
    rules: list[dict[str, str]] = []
    text = matrix_path.read_text(encoding="utf-8")

    current_reg = ""
    current_sec = ""
    current_keywords: list[str] = []
    current_coverage = ""
    current_vpoints = ""

    def _flush() -> None:
        if current_reg and current_sec:
            rules.append(
                {
                    "regulation": current_reg,
                    "section": current_sec,
                    "keywords": current_keywords[:],
                    "required_coverage": current_coverage,
                    "verification_points": current_vpoints,
                }
            )

    for line in text.splitlines():
        stripped = line.strip()
        reg_m = re.match(r"^#{3,4}\s+REG:\s+(.+)$", stripped)
        sec_m = re.match(r"^#{4,5}\s+SEC:\s+(.+)$", stripped)
        kw_m = re.match(r"^\*\*Keywords:\*\*\s+(.+)$", stripped)
        cov_m = re.match(r"^\*\*Required Coverage:\*\*\s+(.+)$", stripped)
        vp_m = re.match(r"^\*\*Verification Points:\*\*\s+(.+)$", stripped)

        if reg_m:
            _flush()
            current_reg = reg_m.group(1).strip()
            current_sec = ""
            current_keywords = []
            current_coverage = ""
            current_vpoints = ""
        elif sec_m:
            _flush()
            current_sec = sec_m.group(1).strip()
            current_keywords = []
            current_coverage = ""
            current_vpoints = ""
        elif kw_m:
            current_keywords = [k.strip() for k in kw_m.group(1).split(",") if k.strip()]
        elif cov_m:
            current_coverage = cov_m.group(1).strip()
        elif vp_m:
            current_vpoints = vp_m.group(1).strip()

    _flush()
    return rules


# ---------------------------------------------------------------------------
# Document scanner
# ---------------------------------------------------------------------------

def scan_documents(directory: Path) -> dict[str, str]:
    """Return {relative_path: content} for all .md files under directory."""
    docs: dict[str, str] = {}
    for md_file in sorted(directory.rglob("*.md")):
        try:
            docs[str(md_file.relative_to(directory))] = md_file.read_text(
                encoding="utf-8"
            )
        except (OSError, UnicodeDecodeError):
            pass
    return docs


def files_matching_keywords(docs: dict[str, str], keywords: list[str]) -> list[str]:
    """Return list of doc paths that contain at least one keyword (whole-word, case-insensitive)."""
    matched: list[str] = []
    patterns = [re.compile(r"\b" + re.escape(kw) + r"\b", re.IGNORECASE) for kw in keywords]
    for path, content in docs.items():
        if any(p.search(content) for p in patterns):
            matched.append(path)
    return matched


# ---------------------------------------------------------------------------
# Report generator
# ---------------------------------------------------------------------------

def generate_report(
    rules: list[dict[str, str]],
    docs: dict[str, str],
    regulation_filter: str | None,
) -> list[dict[str, str]]:
    """Evaluate each rule against docs; return rows for CSV output."""
    rows: list[dict[str, str]] = []
    for rule in rules:
        if regulation_filter and rule["regulation"].lower() != regulation_filter.lower():
            continue

        matched = files_matching_keywords(docs, rule["keywords"])
        status = "Compliant" if matched else "Gap"
        files_str = "; ".join(matched) if matched else ""

        if status == "Gap":
            recommendation = (
                f"Add coverage for '{rule['section']}' in relevant KP/KK/PM documents. "
                f"Verification points: {rule['verification_points']}."
            )
        else:
            recommendation = (
                f"Coverage confirmed in {len(matched)} file(s). "
                "Verify depth of coverage in periodic review."
            )

        rows.append(
            {
                "Regulation": rule["regulation"],
                "Section": rule["section"],
                "Required Coverage": rule["required_coverage"],
                "Files Addressing": files_str,
                "Status": status,
                "Recommendation": recommendation,
            }
        )
    return rows


def write_csv(rows: list[dict[str, str]], output_path: Path) -> None:
    """Write compliance rows to CSV."""
    fieldnames = [
        "Regulation",
        "Section",
        "Required Coverage",
        "Files Addressing",
        "Status",
        "Recommendation",
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: list[dict[str, str]]) -> None:
    """Print a compact terminal summary."""
    total = len(rows)
    gaps = sum(1 for r in rows if r["Status"] == "Gap")
    compliant = total - gaps
    print(f"\n{'='*60}")
    print(f"COMPLIANCE AUDIT SUMMARY")
    print(f"{'='*60}")
    print(f"  Total rules checked : {total}")
    print(f"  Compliant           : {compliant}")
    print(f"  Gaps (Critical)     : {gaps}")
    print(f"{'='*60}")
    if gaps:
        print("\nGAPS IDENTIFIED:")
        for r in rows:
            if r["Status"] == "Gap":
                print(f"  [{r['Regulation']}] {r['Section']}")
    print()


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Malaysian T&CM Regulatory Compliance Audit Tool for Tuinalogy WIM."
    )
    parser.add_argument(
        "directory",
        help="Root directory containing Tuinalogy .md documents (e.g. tuinalogy-services/)",
    )
    parser.add_argument(
        "--matrix",
        default=None,
        help="Path to regulatory-compliance-matrix.md (default: <directory>/_reference/regulatory-compliance-matrix.md)",
    )
    parser.add_argument(
        "--regulation",
        default=None,
        help="Filter audit to a single regulation name (e.g. 'T&CM Act 2013')",
    )
    parser.add_argument(
        "--output",
        default="compliance-gaps-report.csv",
        help="Output CSV file path (default: compliance-gaps-report.csv)",
    )
    args = parser.parse_args(argv)

    directory = Path(args.directory)
    if not directory.is_dir():
        print(f"ERROR: Directory not found: {directory}", file=sys.stderr)
        return 1

    matrix_path = (
        Path(args.matrix)
        if args.matrix
        else directory / "_reference" / "regulatory-compliance-matrix.md"
    )
    if not matrix_path.is_file():
        print(f"ERROR: Compliance matrix not found: {matrix_path}", file=sys.stderr)
        return 1

    rules = parse_compliance_matrix(matrix_path)
    if not rules:
        print("ERROR: No rules parsed from compliance matrix.", file=sys.stderr)
        return 1

    docs = scan_documents(directory)
    rows = generate_report(rules, docs, args.regulation)
    output_path = Path(args.output)
    write_csv(rows, output_path)

    print_summary(rows)
    print(f"Report written to: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
