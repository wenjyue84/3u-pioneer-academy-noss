#!/usr/bin/env python3
"""
apply-pregnancy-warnings.py — Backfill pregnancy contraindication warnings to KP/KK files.

Scans all KP-*.md and KK-*.md files under the given directory for references to
the 5 forbidden acupoints (LI-4, SP-6, GB-21, BL-32, BL-33) and inserts a
warning callout block if one is not already present.

Idempotent: safe to run multiple times.

Usage:
    python tools/apply-pregnancy-warnings.py [directory]
    python tools/apply-pregnancy-warnings.py tuinalogy-services/
"""
from __future__ import annotations

import os
import re
import sys


FORBIDDEN_POINTS: list[tuple[str, str, str]] = [
    (r"\bLI-?4\b|合谷", "LI-4", "合谷/Hegu"),
    (r"\bSP-?6\b|三阴交", "SP-6", "三阴交/Sanyinjiao"),
    (r"\bGB-?21\b|肩井", "GB-21", "肩井/Jianjing"),
    (r"\bBL-?32\b|次髎", "BL-32", "次髎/Ciliao"),
    (r"\bBL-?33\b|中髎", "BL-33", "中髎/Zhongliao"),
]

WARNING_MARKER = "⚠️ **Pregnancy Contraindication**"


def build_warning_block(found_points: list[tuple[str, str]]) -> str:
    """Build a blockquote warning block listing all found forbidden points."""
    if len(found_points) == 1:
        code, name = found_points[0]
        point_str = f"{code} ({name})"
    else:
        parts = [f"{code} ({name})" for code, name in found_points]
        point_str = ", ".join(parts)

    lines = [
        "",
        f"> ⚠️ **Pregnancy Contraindication** — {point_str} mentioned in this document"
        " are forbidden during pregnancy at all trimesters per T&CM Act 2013 Section 28."
        " Do NOT apply to pregnant clients. See `_reference/pregnancy-safety-reference.md`.",
        "",
    ]
    return "\n".join(lines)


def find_insertion_point(lines: list[str]) -> int:
    """Return the line index AFTER the metadata header block (after first '---' separator)."""
    found_first_separator = False
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "---":
            if not found_first_separator:
                found_first_separator = True
            else:
                # Second separator — insert after it
                return i + 1
    # Fallback: insert after first separator
    for i, line in enumerate(lines):
        if line.strip() == "---":
            return i + 1
    # No separator found — insert after first heading
    for i, line in enumerate(lines):
        if line.startswith("#"):
            return i + 1
    return 1


def process_file(path: str) -> bool:
    """Process one file. Returns True if file was modified."""
    with open(path, encoding="utf-8") as fh:
        content = fh.read()

    # Check which forbidden points are in this file
    found_points: list[tuple[str, str]] = []
    for pattern, code, name in FORBIDDEN_POINTS:
        if re.search(pattern, content):
            found_points.append((code, name))

    if not found_points:
        return False

    # Already has the warning marker — skip
    if WARNING_MARKER in content:
        return False

    lines = content.splitlines(keepends=True)
    insert_at = find_insertion_point(lines)
    warning = build_warning_block(found_points)
    warning_lines = [ln + "\n" for ln in warning.split("\n")]

    lines[insert_at:insert_at] = warning_lines

    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(lines)

    return True


def main() -> None:
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "tuinalogy-services"

    modified: list[str] = []
    skipped: list[str] = []

    for dirpath, _, files in os.walk(root_dir):
        for fname in sorted(files):
            if fname.endswith(".md") and fname.startswith(("KP-", "KK-")):
                full_path = os.path.join(dirpath, fname)
                if process_file(full_path):
                    modified.append(full_path)
                    print(f"  [UPDATED] {full_path}")
                else:
                    skipped.append(full_path)

    print(f"\nDone. Updated {len(modified)} file(s), skipped {len(skipped)} file(s).")


if __name__ == "__main__":
    main()
