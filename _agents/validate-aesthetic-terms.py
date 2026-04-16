#!/usr/bin/env python3
"""validate-aesthetic-terms.py — Aesthetic Services terminology consistency validator.

Scans KP documents for EN/BM term usage and checks against the glossary.
Exits 0 if all terms are used consistently; exits 1 if inconsistencies are found.

Usage:
    python _agents/validate-aesthetic-terms.py \
        --check aesthetic-services/C*/KP*.md \
        --glossary aesthetic-services/00-aesthetic-terminology.md \
        --output inconsistencies.csv
"""

import argparse
import csv
import re
import sys
from pathlib import Path


def load_glossary(glossary_path: str) -> dict[str, str]:
    """Parse glossary table rows into {EN_lower: BM_canonical} mapping."""
    pairs: dict[str, str] = {}
    path = Path(glossary_path)
    content = path.read_text(encoding="utf-8")
    # Match table rows: | EN Term | BM Term | ... |
    row_pattern = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", re.MULTILINE)
    for match in row_pattern.finditer(content):
        en_raw = match.group(1).strip()
        bm_raw = match.group(2).strip()
        # Skip header rows and separator rows
        if en_raw.startswith("-") or en_raw.lower() in (
            "english term (en)",
            "(use this in en text)",
        ):
            continue
        if bm_raw.startswith("-") or not bm_raw or bm_raw.lower() in (
            "bahasa malaysia (bm)",
            "(use this in bm text)",
        ):
            continue
        # Normalise: strip bold markers, parenthetical notes, extra whitespace
        en_clean = re.sub(r"\*\*|\*|`", "", en_raw).split("(")[0].strip().lower()
        bm_clean = re.sub(r"\*\*|\*|`", "", bm_raw).split("(")[0].strip()
        if en_clean and bm_clean:
            pairs[en_clean] = bm_clean
    return pairs


def extract_terms_from_file(
    filepath: str, glossary: dict[str, str]
) -> list[dict[str, str]]:
    """Find glossary EN terms in a KP file and record the BM translation used nearby."""
    findings: list[dict[str, str]] = []
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")

    for en_term, canonical_bm in glossary.items():
        # Skip very short terms (< 5 chars) to avoid false positives
        if len(en_term) < 5:
            continue
        # Escape for regex use; allow word-boundary matching (case-insensitive)
        pattern = re.compile(
            r"(?i)\b" + re.escape(en_term) + r"\b[^.]{0,80}"
        )
        for m in pattern.finditer(content):
            context = m.group(0)
            # Look for an inline BM translation: (*...*) or (*...) immediately after term
            inline_bm_match = re.search(r"\(\*([^)]+)\*?\)", context)
            bm_found = inline_bm_match.group(1).strip() if inline_bm_match else ""
            if bm_found:
                findings.append(
                    {
                        "file": str(filepath),
                        "en_term": en_term,
                        "canonical_bm": canonical_bm,
                        "bm_used": bm_found,
                        "consistent": "YES"
                        if bm_found.lower() == canonical_bm.lower()
                        else "NO",
                        "context": context[:100].replace("\n", " "),
                    }
                )
    return findings


def check_consistency(
    kp_files: list[str], glossary: dict[str, str]
) -> list[dict[str, str]]:
    """Aggregate findings across all KP files; return inconsistency rows only."""
    all_findings: list[dict[str, str]] = []
    for filepath in kp_files:
        findings = extract_terms_from_file(filepath, glossary)
        all_findings.extend(findings)

    # Group by en_term — detect terms with multiple different BM translations
    term_translations: dict[str, set[str]] = {}
    for row in all_findings:
        key = row["en_term"]
        bm = row["bm_used"]
        term_translations.setdefault(key, set()).add(bm)

    # Build inconsistency report: terms with >1 translation OR non-canonical translation
    inconsistencies: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for row in all_findings:
        en = row["en_term"]
        bm_used = row["bm_used"]
        canonical = row["canonical_bm"]
        is_inconsistent = (
            bm_used.lower() != canonical.lower()
            or len(term_translations.get(en, set())) > 1
        )
        if is_inconsistent:
            key = (row["file"], en, bm_used)
            if key not in seen:
                seen.add(key)
                inconsistencies.append(
                    {
                        "file": row["file"],
                        "en_term": en,
                        "canonical_bm": canonical,
                        "bm_used": bm_used,
                        "all_translations_found": "; ".join(
                            sorted(term_translations.get(en, set()))
                        ),
                        "context": row["context"],
                    }
                )
    return inconsistencies


def generate_csv_report(
    inconsistencies: list[dict[str, str]], output_path: str
) -> None:
    """Write inconsistencies to CSV file."""
    fieldnames = [
        "file",
        "en_term",
        "canonical_bm",
        "bm_used",
        "all_translations_found",
        "context",
    ]
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inconsistencies)


def resolve_glob_patterns(patterns: list[str]) -> list[str]:
    """Expand glob patterns to file paths."""
    import glob

    resolved: list[str] = []
    for pattern in patterns:
        matched = glob.glob(pattern, recursive=True)
        if matched:
            resolved.extend(matched)
        elif Path(pattern).exists():
            resolved.append(pattern)
    return sorted(set(resolved))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate EN/BM terminology consistency in Aesthetic KP documents."
    )
    parser.add_argument(
        "--check",
        nargs="+",
        required=True,
        metavar="GLOB",
        help="KP file paths or glob patterns to scan (e.g. aesthetic-services/C*/KP*.md)",
    )
    parser.add_argument(
        "--glossary",
        required=True,
        metavar="FILE",
        help="Path to 00-aesthetic-terminology.md",
    )
    parser.add_argument(
        "--output",
        default="inconsistencies.csv",
        metavar="FILE",
        help="Output CSV file path (default: inconsistencies.csv)",
    )
    args = parser.parse_args()

    # Load glossary
    glossary = load_glossary(args.glossary)
    print(f"Loaded {len(glossary)} EN/BM term pairs from glossary.")

    # Resolve file patterns
    kp_files = resolve_glob_patterns(args.check)
    if not kp_files:
        print("ERROR: No KP files found matching the given patterns.", file=sys.stderr)
        sys.exit(1)
    print(f"Scanning {len(kp_files)} KP file(s)...")

    # Check consistency
    inconsistencies = check_consistency(kp_files, glossary)

    # Generate report
    generate_csv_report(inconsistencies, args.output)

    if inconsistencies:
        print(
            f"\nFAIL — {len(inconsistencies)} terminology inconsistency/ies found."
        )
        print(f"Report written to: {args.output}")
        print("\nSummary of inconsistencies:")
        printed_terms: set[str] = set()
        for row in inconsistencies:
            if row["en_term"] not in printed_terms:
                printed_terms.add(row["en_term"])
                print(
                    f"  [{row['en_term']}] canonical='{row['canonical_bm']}' "
                    f"| found: {row['all_translations_found']}"
                )
        sys.exit(1)
    else:
        print(
            f"\nPASS — All terminology usage is consistent with the glossary."
        )
        print(f"Report written to: {args.output}")
        sys.exit(0)


if __name__ == "__main__":
    main()
