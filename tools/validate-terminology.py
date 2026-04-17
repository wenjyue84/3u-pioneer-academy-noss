#!/usr/bin/env python3
"""
validate-terminology.py — TCM Terminology Consistency Checker

Reads the TCM terminology index and scans WIM documents for near-miss
character variants of canonical terms (Levenshtein distance == 1).

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


# ---------------------------------------------------------------------------
# Levenshtein distance (pure Python, no third-party deps)
# ---------------------------------------------------------------------------

def levenshtein_distance(s1: str, s2: str) -> int:
    """Compute edit distance between two strings."""
    m, n = len(s1), len(s2)
    if m < n:
        s1, s2, m, n = s2, s1, n, m
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            curr[j] = min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + cost)
        prev = curr
    return prev[n]


# ---------------------------------------------------------------------------
# Index parsing
# ---------------------------------------------------------------------------

def is_chinese_char(c: str) -> bool:
    """Return True if c is a CJK unified ideograph."""
    cp = ord(c)
    return (
        0x4E00 <= cp <= 0x9FFF
        or 0x3400 <= cp <= 0x4DBF
        or 0x20000 <= cp <= 0x2A6DF
    )


def contains_chinese(s: str) -> bool:
    return any(is_chinese_char(c) for c in s)


def load_terminology_index(index_path: Path) -> list[str]:
    """
    Parse the terminology index markdown table and return all canonical
    Chinese terms (first pipe-delimited column, length >= 3).
    """
    terms: list[str] = []
    in_table = False
    with open(index_path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            # Detect markdown table rows (start and end with |)
            stripped = line.strip()
            if not stripped.startswith("|"):
                in_table = False
                continue
            in_table = True
            # Skip header separator rows like |---|---|
            if re.fullmatch(r"[|\s\-:]+", stripped):
                continue
            cols = [c.strip() for c in stripped.split("|")]
            # cols[0] is empty (before first |), cols[1] is first cell
            if len(cols) < 3:
                continue
            term = cols[1]
            if len(term) >= 3 and contains_chinese(term):
                terms.append(term)
    return terms


# ---------------------------------------------------------------------------
# Deviation detection
# ---------------------------------------------------------------------------

def extract_chinese_windows(text: str, lengths: list[int]) -> list[tuple[int, str]]:
    """
    Extract all substrings of the given lengths that contain at least
    one Chinese character.  Returns list of (position, substring).
    """
    results: list[tuple[int, str]] = []
    for length in set(lengths):
        for i in range(len(text) - length + 1):
            window = text[i : i + length]
            if contains_chinese(window):
                results.append((i, window))
    return results


def find_deviations_in_file(
    filepath: Path,
    canonical_terms: list[str],
    canonical_set: set[str],
) -> list[tuple[int, str, str]]:
    """
    Scan a single file for near-miss variants of canonical terms.

    Returns a list of (line_number, canonical_term, deviation_found).
    """
    deviations: list[tuple[int, str, str]] = []
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return deviations

    lines = content.split("\n")
    # Window lengths to check: len(term) ± 1 for each canonical term
    window_lengths: set[int] = set()
    for term in canonical_terms:
        L = len(term)
        if L - 1 >= 3:
            window_lengths.add(L - 1)
        window_lengths.add(L)
        window_lengths.add(L + 1)

    for line_no, line in enumerate(lines, start=1):
        if not contains_chinese(line):
            continue
        windows = extract_chinese_windows(line, list(window_lengths))
        for _pos, window in windows:
            if window in canonical_set:
                continue  # exact match — OK
            for term in canonical_terms:
                if abs(len(window) - len(term)) > 1:
                    continue
                dist = levenshtein_distance(window, term)
                if dist == 1:
                    deviations.append((line_no, term, window))
                    break  # report once per window
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
    canonical_set = set(canonical_terms)

    # Scan KP, KK, PM, PA, KA files
    target_pattern = re.compile(r"^(KP|KK|PM|PA|KA)", re.IGNORECASE)
    md_files = [
        f
        for f in scan_dir.rglob("*.md")
        if target_pattern.match(f.name)
    ]
    md_files.sort()

    all_deviations: list[tuple[Path, int, str, str]] = []
    for md_file in md_files:
        file_devs = find_deviations_in_file(md_file, canonical_terms, canonical_set)
        for line_no, canonical, found in file_devs:
            all_deviations.append((md_file, line_no, canonical, found))

    # Write output
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
        print(
            f"OK — {len(md_files)} files checked, 0 deviations found."
        )


if __name__ == "__main__":
    main()
