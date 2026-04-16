#!/usr/bin/env python3
"""Validate IT Level 3 Knowledge Assessment (KA) markdown files."""
from __future__ import annotations

import argparse
import glob as glob_module
import re
import sys
from pathlib import Path

_Q_HEADER = re.compile(r"^### Q(\d+)", re.MULTILINE)
_Q_TYPE = re.compile(r"\*\*Type:\*\*\s*(MCQ|Short Answer|Scenario)")
_Q_DIFF = re.compile(r"\*\*Difficulty:\*\*\s*(L[123])")
_Q_MARKS = re.compile(r"\*\*Marks:\*\*\s*(\d+)")
_Q_LO = re.compile(r"\*\*LO Ref:\*\*")
_Q_RUBRIC = re.compile(r"\*\*Rubric:\*\*")
_K_ITEM = re.compile(r"^-\s*(K\d+):", re.MULTILINE)


def find_ka_files(patterns: list[str]) -> list[str]:
    """Expand glob patterns; fall back to L3-C0[2-4]/KA.md if nothing matches."""
    files: list[str] = []
    for pattern in patterns:
        matched = glob_module.glob(pattern)
        if matched:
            files.extend(matched)
        else:
            p = Path(pattern)
            parent = p.parents[1] if len(p.parts) >= 3 else Path("it-computer-system")
            fallback = str(parent / "L3-C0[2-4]" / "KA.md")
            files.extend(glob_module.glob(fallback))
    return sorted(set(files))


def parse_questions(content: str) -> list[dict[str, str]]:
    """Split content into per-question blocks and extract metadata."""
    parts = _Q_HEADER.split(content)
    questions: list[dict[str, str]] = []
    # parts = [preamble, q_num1, q_body1, q_num2, q_body2, ...]
    for i in range(1, len(parts), 2):
        body = parts[i + 1] if i + 1 < len(parts) else ""
        q: dict[str, str] = {}
        m = _Q_TYPE.search(body)
        if m:
            q["type"] = m.group(1)
        m = _Q_DIFF.search(body)
        if m:
            q["difficulty"] = m.group(1)
        m = _Q_MARKS.search(body)
        if m:
            q["marks"] = m.group(1)
        q["has_lo_ref"] = str(bool(_Q_LO.search(body)))
        q["has_rubric"] = str(bool(_Q_RUBRIC.search(body)))
        questions.append(q)
    return questions


def validate_file(path: str, min_questions: int) -> tuple[bool, list[str]]:
    """Return (passed, errors) for one KA.md file."""
    errors: list[str] = []
    try:
        content = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return False, [f"File not found: {path}"]

    questions = parse_questions(content)
    n = len(questions)
    if n < min_questions:
        errors.append(f"Questions: {n} found, minimum {min_questions} required")

    for i, q in enumerate(questions, 1):
        if "type" not in q:
            errors.append(f"Q{i}: missing **Type:**")
        if "difficulty" not in q:
            errors.append(f"Q{i}: missing **Difficulty:**")
        if "marks" not in q:
            errors.append(f"Q{i}: missing **Marks:**")
        if q.get("has_lo_ref") != "True":
            errors.append(f"Q{i}: missing **LO Ref:**")
        if q.get("has_rubric") != "True":
            errors.append(f"Q{i}: missing **Rubric:**")

    if n >= min_questions:
        types = [q.get("type", "") for q in questions]
        if not any(t == "MCQ" for t in types):
            errors.append("No MCQ questions found (need ~40%)")
        if not any(t == "Short Answer" for t in types):
            errors.append("No Short Answer questions found (need ~40%)")
        if not any(t == "Scenario" for t in types):
            errors.append("No Scenario questions found (need ~20%)")

    return len(errors) == 0, errors


def validate_noss_coverage(noss_path: str, mapping_path: str) -> list[str]:
    """Check all NOSS K-items appear in the YAML mapping with coverage."""
    errors: list[str] = []
    np_ = Path(noss_path)
    mp_ = Path(mapping_path)
    if not np_.exists():
        return [f"NOSS extract not found: {noss_path}"]
    if not mp_.exists():
        return [f"Mapping file not found: {mapping_path}"]

    k_items = _K_ITEM.findall(np_.read_text(encoding="utf-8"))

    mapped: set[str] = set()
    for line in mp_.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, _, val = line.partition(":")
        if val.strip():
            mapped.add(key.strip().split(".")[-1])

    for k in k_items:
        if k not in mapped:
            errors.append(f"NOSS item {k} has no question coverage in {mapping_path}")
    return errors


def main() -> None:
    """Entry point."""
    parser = argparse.ArgumentParser(description="Validate IT Level 3 KA files")
    parser.add_argument("files", nargs="+", help="KA.md paths or glob patterns")
    parser.add_argument("--min-questions", type=int, default=4)
    parser.add_argument("--validate-against-noss", action="store_true")
    args = parser.parse_args()

    ka_files = find_ka_files(args.files)
    if not ka_files:
        print("WARNING: No KA files found. Validation skipped.")
        sys.exit(0)

    all_passed = True
    for path in ka_files:
        passed, errors = validate_file(path, args.min_questions)
        print(f"[{'PASS' if passed else 'FAIL'}] {path}")
        for err in errors:
            print(f"  ERROR: {err}")
            all_passed = False

    if args.validate_against_noss:
        noss_errors = validate_noss_coverage(
            "it-computer-system/00-noss-extract.md",
            "tools/it_noss_mapping.yaml",
        )
        for err in noss_errors:
            print(f"  NOSS ERROR: {err}")
            all_passed = False

    if not all_passed:
        sys.exit(1)
    print(f"\nAll {len(ka_files)} IT KA files passed validation.")


if __name__ == "__main__":
    main()
