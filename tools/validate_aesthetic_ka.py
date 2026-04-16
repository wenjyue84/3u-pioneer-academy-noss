#!/usr/bin/env python3
"""Validate Aesthetic Services Knowledge Assessment (KA) markdown files."""
from __future__ import annotations

import argparse
import glob as glob_module
import re
import sys
from pathlib import Path


def find_ka_files(patterns: list[str]) -> list[str]:
    """Expand glob patterns; fall back to C0[1-4]/KA.md if nothing matches."""
    files: list[str] = []
    for pattern in patterns:
        matched = glob_module.glob(pattern)
        if matched:
            files.extend(matched)
        else:
            # Derive parent dir from pattern (e.g. aesthetic-services/CU-*/KA.md)
            p = Path(pattern)
            if len(p.parts) >= 3:
                parent = p.parents[1]
            else:
                parent = Path("aesthetic-services")
            fallback = str(parent / "C0[1-4]" / "KA.md")
            files.extend(glob_module.glob(fallback))
    return sorted(set(files))


def validate_file(
    path: str, min_questions: int, validate_bilingual: bool
) -> tuple[bool, list[str]]:
    """Return (passed, errors) for a single KA.md file."""
    errors: list[str] = []
    try:
        content = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return False, [f"File not found: {path}"]

    en_count = len(re.findall(r"\*\*EN:\*\*", content))
    bm_count = len(re.findall(r"\*\*BM:\*\*", content))

    if en_count < min_questions:
        errors.append(
            f"Bilingual questions: {en_count} found, minimum {min_questions} required"
        )
    if validate_bilingual and en_count != bm_count:
        errors.append(
            f"Bilingual mismatch: {en_count} EN: vs {bm_count} BM: markers"
        )
    return len(errors) == 0, errors


def validate_glossary(ka_path: str) -> list[str]:
    """Warn if key glossary terms are absent from the KA file."""
    p = Path(ka_path)
    glossary_path = p.parents[1] / "_docs" / "aesthetic-glossary.md"
    if not glossary_path.exists():
        return ["Glossary not found; skipping term validation"]

    glossary = glossary_path.read_text(encoding="utf-8")
    content = p.read_text(encoding="utf-8").lower()

    terms = re.findall(r"\|\s*([A-Za-z][A-Za-z ()]+?)\s*\|", glossary)
    skip = {"english term", "istilah bahasa malaysia"}
    missing = [
        t.strip() for t in terms[:12]
        if t.strip() and t.strip().lower() not in skip and t.strip().lower() not in content
    ]
    return [f"Terms absent from KA: {', '.join(missing)}"] if missing else []


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Aesthetic KA files")
    parser.add_argument("files", nargs="+", help="KA.md paths or glob patterns")
    parser.add_argument("--min-questions", type=int, default=5)
    parser.add_argument("--validate-bilingual", action="store_true")
    args = parser.parse_args()

    ka_files = find_ka_files(args.files)
    if not ka_files:
        print("WARNING: No KA files found. Validation skipped.")
        sys.exit(0)

    all_passed = True
    for path in ka_files:
        passed, errors = validate_file(path, args.min_questions, args.validate_bilingual)
        print(f"[{'PASS' if passed else 'FAIL'}] {path}")
        for err in errors:
            print(f"  ERROR: {err}")
            all_passed = False
        for warn in validate_glossary(path):
            print(f"  WARN:  {warn}")

    if not all_passed:
        sys.exit(1)
    print(f"\nAll {len(ka_files)} KA files passed validation.")


if __name__ == "__main__":
    main()
