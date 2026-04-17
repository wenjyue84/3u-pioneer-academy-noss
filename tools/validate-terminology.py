#!/usr/bin/env python3
"""
validate-terminology.py — TCM Terminology Consistency Checker

Reads the TCM terminology index and scans WIM documents for corrupted
variants of canonical terms — specifically, terms with separators or
punctuation inserted between characters (e.g., 足三里 → 足三-里).

Usage:
    python tools/validate-terminology.py <index_file> <scan_dir> --output <out_file>

Exit code: 0 always (deviations written to --output file).
Test: [ ! -s term-deviations.txt ]  — passes when output file is empty.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Separator characters that could be erroneously inserted within a term
_SEP = r'[\s\-–—·•/\\|,，、:：;；\*_`~\u200b\u00a0]'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def contains_chinese(s: str) -> bool:
    """Return True if string contains any CJK ideograph."""
    return any(0x4E00 <= ord(c) <= 0x9FFF or 0x3400 <= ord(c) <= 0x4DBF for c in s)


def build_separator_regex(term: str) -> re.Pattern[str]:
    """Build regex matching a term's characters with optional separators between them.

    E.g. "足三里" → regex matching 足[sep]+三[sep]+里 (at least one separator somewhere).
    """
    chars = [re.escape(c) for c in term]
    # Each adjacent pair separated by optional separator(s)
    pattern = f'{_SEP}*'.join(chars)
    return re.compile(pattern)


# ---------------------------------------------------------------------------
# Index parsing
# ---------------------------------------------------------------------------

def load_terminology_index(index_path: Path) -> list[str]:
    """
    Parse the terminology index markdown table and return all canonical
    Chinese terms (first pipe-delimited column, length >= 3).
    """
    terms: list[str] = []
    with open(index_path, encoding="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped.startswith("|"):
                continue
            if re.fullmatch(r"[|\s\-:]+", stripped):
                continue
            cols = [c.strip() for c in stripped.split("|")]
            if len(cols) < 3:
                continue
            term = cols[1]
            if len(term) >= 3 and contains_chinese(term):
                terms.append(term)
    return terms


# ---------------------------------------------------------------------------
# Deviation detection — separator-insertion approach
# ---------------------------------------------------------------------------

def find_deviations_in_file(
    filepath: Path,
    canonical_terms: list[str],
    term_regexes: list[tuple[str, re.Pattern[str]]],
) -> list[tuple[int, str, str]]:
    """
    Scan a file for corrupted term variants (separator chars inserted
    between canonical characters).  Only flags matches that differ from
    the exact canonical form (i.e. contain at least one separator).

    Returns list of (line_number, canonical_term, deviation_found).
    """
    deviations: list[tuple[int, str, str]] = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return deviations

    for term, regex in term_regexes:
        for match in regex.finditer(content):
            found = match.group()
            if found == term:
                continue  # exact match — no deviation
            line_no = content[: match.start()].count("\n") + 1
            deviations.append((line_no, term, found))

    return deviations


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Check TCM terminology consistency in WIM documents."
    )
    parser.add_argument("index_file", help="Path to tcm-terminology-index.md")
    parser.add_argument("scan_dir", help="Directory to scan for .md files")
    parser.add_argument("--output", default="term-deviations.txt", help="Output file")
    args = parser.parse_args(argv)

    index_path = Path(args.index_file)
    scan_dir = Path(args.scan_dir)
    output_path = Path(args.output)

    if not index_path.exists():
        print(f"ERROR: index file not found: {index_path}", file=sys.stderr)
        sys.exit(1)
    if not scan_dir.is_dir():
        print(f"ERROR: scan directory not found: {scan_dir}", file=sys.stderr)
        sys.exit(1)

    canonical_terms = load_terminology_index(index_path)
    if not canonical_terms:
        print("WARNING: no terms loaded from index.", file=sys.stderr)

    # Pre-compile separator-insertion regexes for each term
    term_regexes = [(t, build_separator_regex(t)) for t in canonical_terms]

    # Scan KP, KK, PM, PA, KA files only
    target_pattern = re.compile(r"^(KP|KK|PM|PA|KA)", re.IGNORECASE)
    md_files = sorted(
        f for f in scan_dir.rglob("*.md") if target_pattern.match(f.name)
    )

    all_deviations: list[tuple[Path, int, str, str]] = []
    for md_file in md_files:
        for line_no, canonical, found in find_deviations_in_file(
            md_file, canonical_terms, term_regexes
        ):
            all_deviations.append((md_file, line_no, canonical, found))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as out:
        for md_file, line_no, canonical, found in all_deviations:
            out.write(
                f"{md_file}:{line_no}: DEVIATION — "
                f"found '{found}', expected canonical '{canonical}'\n"
            )

    if all_deviations:
        print(
            f"Found {len(all_deviations)} terminology deviation(s). "
            f"See {output_path}",
            file=sys.stderr,
        )
    else:
        print(f"OK — {len(md_files)} files checked, 0 deviations found.")


if __name__ == "__main__":
    main()
