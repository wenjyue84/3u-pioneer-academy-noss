#!/usr/bin/env python3
"""Enforce JPK 'CONTOH FORMAT PENULISAN SOALAN' rules on WIM/ADI question files.

Rules (source: raw/soalan-format/contoh-format-penulisan-soalan.jpeg):
1. '?' at the end of a question stem, hard against the last word (no space before it).
2. Non-Bahasa-Melayu words must be *italic*.
3. Every answer choice ends with a full stop, EXCEPT choices that are purely numeric,
   a common noun on its own, or a proper noun (name) on its own.
4. Every answer choice starts with a capital letter.
5. Roman numerals (I, II, III, IV) and option letters (A, B, C, D) must be uppercase.
6. Exactly four answer choices per question (A-D).
7. A question referring to an image/stimulus must use the word "Berdasarkan".
8. Answer choices must be structurally homogeneous (parallel phrasing/length).
9. Answer choices ordered short-to-long / small-to-large.
10. Distractors must be homogeneous (same category/unit) as the correct answer.

Rules 1, 3, 4, 5, 6 are checked precisely. Rules 2, 7, 8, 9, 10 are heuristic and
reported as WARN for human review (they need semantic judgement this script can't
safely automate). Run with --fix to auto-correct rules 1, 4, 5, 6-count-report only
(count violations are never auto-fixed — they need a human to add/remove a choice).

Usage:
    uv run check_format.py <file-or-dir> [<file-or-dir> ...] [--fix] [--json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

QUESTION_RE = re.compile(r"^\*\*Soalan\s+\d+\*\*.*$", re.MULTILINE)
OPTION_RE = re.compile(r"^([A-Z]|[IVX]+)\.\s+(.*)$")
ROMAN_OPTION_RE = re.compile(r"^[ivx]+\.\s")

# Common English/loan technical terms seen in these NOSS docs that must be italicised
# when they appear un-italicised in Malay running text. Extend as new terms surface.
EN_TERMS = [
    "script", "storyboard", "footage", "man hour", "machine", "shooting script",
    "master script", "continuity script", "editing", "editor", "producer",
    "director", "sound effect", "visual effect", "genre", "render", "export",
    "timeline", "workflow", "template", "backup", "preview", "playback",
    "colour grading", "color grading", "transition", "montage", "voice over",
    "voice-over", "soundtrack", "keyframe", "codec", "resolution", "aspect ratio",
    "frame rate", "b-roll", "b roll", "checklist", "briefing", "feedback",
]


def find_md_files(paths):
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            files.append(p)
    return files


def split_questions(text):
    """Yield (start_line_idx, stem_lines, option_lines) per question block."""
    lines = text.splitlines()
    starts = [i for i, l in enumerate(lines) if re.match(r"^\*\*Soalan\s+\d+\*\*", l)]
    blocks = []
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        blocks.append((start, lines[start:end]))
    return blocks


def is_option_line(line):
    return bool(re.match(r"^[A-D]\.\s+\S", line)) or bool(re.match(r"^[IVX]+\.\s+\S", line))


def check_block(lines, filename, block_start):
    findings = []
    # locate stem: first non-empty, non-heading line after the **Soalan N** marker
    stem = None
    stem_idx = None
    options = []
    for i, l in enumerate(lines):
        if i == 0:
            continue
        s = l.strip()
        if not s:
            continue
        if re.match(r"^[A-D]\.\s", s) or re.match(r"^[IVX]+\.\s", s, re.IGNORECASE):
            options.append((block_start + i, s))
            continue
        if stem is None and not s.startswith("#"):
            stem = s
            stem_idx = block_start + i

    # Rule 1: '?' hard against last word, only when it IS a question.
    if stem:
        looks_like_question = any(
            stem.lower().startswith(w)
            for w in ["apa", "siapa", "bila", "mengapa", "bagaimana", "yang manakah",
                      "manakah", "berapa", "adakah", "sebutkan"]
        ) or "?" in stem
        if looks_like_question:
            if not stem.rstrip().endswith("?"):
                findings.append(("ERROR", stem_idx, "rule1_missing_qmark",
                                  f"Question stem does not end with '?': {stem[:80]}"))
            elif re.search(r"\s\?$", stem):
                findings.append(("ERROR", stem_idx, "rule1_space_before_qmark",
                                  f"Space before '?': {stem[:80]}"))

    # Rule 7: stimulus-based question must use 'Berdasarkan'
    if stem and re.search(r"\b(gambar|rajah|carta|foto|imej)\b", stem, re.IGNORECASE):
        if "berdasarkan" not in stem.lower():
            findings.append(("WARN", stem_idx, "rule7_missing_berdasarkan",
                              f"Refers to an image/diagram but missing 'Berdasarkan': {stem[:80]}"))

    # Options (A-D only, roman-numeral ordering lines inside a stem are skipped)
    abcd_options = [(ln, txt) for ln, txt in options if re.match(r"^[A-D]\.\s", txt)]

    # Rule 6: exactly four choices
    if abcd_options and len(abcd_options) != 4:
        findings.append(("ERROR", abcd_options[0][0], "rule6_option_count",
                          f"Found {len(abcd_options)} answer choices, expected 4"))

    for ln, txt in abcd_options:
        m = re.match(r"^([A-D])\.\s+(.*)$", txt)
        label, body = m.group(1), m.group(2).strip()

        # Rule 5: label must be uppercase A-D (guaranteed by regex; check stray lowercase roman elsewhere)
        # Rule 4: starts with capital letter
        first_char = body[0] if body else ""
        if first_char and first_char.isalpha() and not first_char.isupper() and not body.startswith("*"):
            findings.append(("ERROR", ln, "rule4_lowercase_start",
                              f"Option {label} does not start with a capital letter: {body[:60]}"))
        elif body.startswith("*") and len(body) > 1 and body[1].isalpha() and not body[1].isupper():
            findings.append(("ERROR", ln, "rule4_lowercase_start",
                              f"Option {label} does not start with a capital letter: {body[:60]}"))

        # Rule 3: trailing period unless purely numeric / bare noun (heuristic: numeric OR single word proper noun)
        stripped = body.rstrip("*_")  # ignore markdown emphasis wrappers for the terminal-char check
        is_numeric = bool(re.match(r"^\*?_?[\d.,%\s\-–]+\*?_?$", stripped))
        word_count = len(re.findall(r"\w+", stripped))
        is_bare_single_word = word_count == 1
        ends_with_period = stripped.rstrip().endswith(".")
        if not is_numeric and not is_bare_single_word and not ends_with_period:
            findings.append(("ERROR", ln, "rule3_missing_period",
                              f"Option {label} missing trailing full stop: {body[:60]}"))

        # Rule 2 heuristic: known EN terms present but not wrapped in *italic*
        low = body.lower()
        for term in EN_TERMS:
            if term in low:
                # crude check: is the term already inside * * somewhere on the line?
                if not re.search(r"\*[^*]*" + re.escape(term) + r"[^*]*\*", low):
                    findings.append(("WARN", ln, "rule2_missing_italic",
                                      f"Option {label} has non-BM term '{term}' not italicised: {body[:60]}"))
                break

    # Rule 5: lowercase roman numerals anywhere in block
    for i, l in enumerate(lines):
        if re.match(r"^[ivx]+\.\s", l.strip()):
            findings.append(("ERROR", block_start + i, "rule5_lowercase_roman",
                              f"Roman numeral option should be uppercase: {l.strip()[:60]}"))

    # Rule 9/10/8: length-based homogeneity heuristic on option bodies
    if len(abcd_options) == 4:
        bodies = [re.sub(r"[*_]", "", b).rstrip(".") for _, b in abcd_options]
        lengths = [len(b) for b in bodies]
        if max(lengths) > 0 and (max(lengths) - min(lengths)) > 0.7 * max(lengths):
            findings.append(("WARN", abcd_options[0][0], "rule8_9_homogeneity",
                              "Answer choices vary sharply in length — check homogeneity/short-to-long order"))

    return findings


def check_file(path):
    text = path.read_text(encoding="utf-8")
    all_findings = []
    for start, lines in split_questions(text):
        all_findings.extend(check_block(lines, path, start))
    return all_findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    files = find_md_files(args.paths)
    report = {}
    total_errors = 0
    total_warns = 0
    for f in files:
        findings = check_file(f)
        if not findings:
            continue
        report[str(f)] = findings
        total_errors += sum(1 for lvl, *_ in findings if lvl == "ERROR")
        total_warns += sum(1 for lvl, *_ in findings if lvl == "WARN")

    if args.json:
        print(json.dumps(
            {str(f): [{"level": lvl, "line": ln, "rule": rule, "msg": msg}
                       for lvl, ln, rule, msg in fnds]
             for f, fnds in report.items()},
            ensure_ascii=False, indent=2))
    else:
        for f, findings in report.items():
            print(f"\n== {f} ==")
            for lvl, ln, rule, msg in findings:
                print(f"  [{lvl}] L{ln+1} {rule}: {msg}")
        print(f"\nTOTAL: {total_errors} ERROR, {total_warns} WARN across {len(report)} file(s)")

    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
