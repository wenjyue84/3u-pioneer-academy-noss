#!/usr/bin/env python3
"""
check-pregnancy-safety.py — Validate pregnancy contraindication warnings in KP/KK documents.

Scans all KP-*.md and KK-*.md files under the given directory for references to
forbidden acupoints (LI-4, SP-6, GB-21, BL-32, BL-33). Any file that references
a forbidden point but lacks the ⚠️ **Pregnancy Contraindication** warning callout
is reported as a violation.

Usage:
    python tools/check-pregnancy-safety.py <directory> [--format csv|text]
    python tools/check-pregnancy-safety.py tuinalogy-services/ --format csv

Exit code: 0 if no violations, 1 if violations found.

CSV output format:
    file,violations,points
    path/to/file.md,0,
    path/to/bad.md,1,LI-4;GB-21
    ...
    TOTAL,<violation_count>,
"""
from __future__ import annotations

import argparse
import os
import re
import sys


FORBIDDEN_POINTS: list[tuple[str, str]] = [
    (r"\bLI-?4\b|合谷", "LI-4"),
    (r"\bSP-?6\b|三阴交", "SP-6"),
    (r"\bGB-?21\b|肩井", "GB-21"),
    (r"\bBL-?32\b|次髎", "BL-32"),
    (r"\bBL-?33\b|中髎", "BL-33"),
]

WARNING_MARKER = "⚠️ **Pregnancy Contraindication**"


def check_file(path: str) -> tuple[list[str], bool]:
    """Return (list of forbidden point codes found, has_warning)."""
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    found = [code for pattern, code in FORBIDDEN_POINTS if re.search(pattern, content)]
    has_warning = WARNING_MARKER in content
    return found, has_warning


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check KP/KK documents for pregnancy contraindication warnings."
    )
    parser.add_argument("directory", nargs="?", default="tuinalogy-services")
    parser.add_argument(
        "--format",
        choices=["csv", "text"],
        default="text",
        help="Output format (default: text)",
    )
    args = parser.parse_args()

    rows: list[tuple[str, int, str]] = []  # (file, violation_count, points_str)
    total_violations = 0

    for dirpath, _, files in os.walk(args.directory):
        for fname in sorted(files):
            if fname.endswith(".md") and fname.startswith(("KP-", "KK-", "PA")):
                full_path = os.path.join(dirpath, fname)
                found_points, has_warning = check_file(full_path)

                if not found_points:
                    continue  # File doesn't mention forbidden points — skip

                violation = 0 if has_warning else 1
                total_violations += violation
                rows.append((full_path, violation, ";".join(found_points)))

    if args.format == "csv":
        print("file,violations,points")
        for file_path, viol, points in rows:
            print(f"{file_path},{viol},{points}")
        print(f"TOTAL,{total_violations},")
    else:
        if rows:
            for file_path, viol, points in rows:
                status = "OK" if viol == 0 else "MISSING WARNING"
                print(f"  [{status}] {file_path} — points: {points}")
        else:
            print("  No KP/KK files reference forbidden acupoints.")

        print(f"\nTotal violations: {total_violations}")
        if total_violations > 0:
            print(
                "Run: python tools/apply-pregnancy-warnings.py <directory> to fix violations."
            )

    sys.exit(0 if total_violations == 0 else 1)


if __name__ == "__main__":
    main()
