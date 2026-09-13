#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
Import NOSS-to-WIM content into Frappe LMS
Usage: uv run python lms_import.py [subject_folder]
       uv run python lms_import.py aesthetic-services
       uv run python lms_import.py all
"""

import os
import re
import sys
import json
import requests
from pathlib import Path

# Config
LMS_URL = "http://localhost:8001"
USERNAME = "Administrator"
PASSWORD = "admin"
NOSS_DIR = Path(r"C:\Users\Jyue\Documents\1-projects\noss-to-wim")

# Subject mapping
SUBJECTS = {
    "aesthetic-services": {
        "title": "Aesthetic Services (Level 3)",
        "short": "Aesthetic Services",
        "code": "S960-002-3:2020",
        "description": "NOSS S960-002-3:2020 — Aesthetic Services Level 3",
    },
    "tuinalogy-services": {
        "title": "Tuinalogy Services (Level 3)",
        "short": "Tuinalogy Services",
        "code": "MP-031-3:2016",
        "description": "NOSS MP-031-3:2016 — Tuinalogy Services Level 3 (推拿疗法)",
    },
    "bev-diagnostic-rectification": {
        "title": "BEV Diagnostic & Rectification (Level 3)",
        "short": "BEV Diagnostic",
        "code": "G452-010-3:2023",
        "description": "NOSS G452-010-3:2023 — Battery Electric Vehicle Diagnostic and Rectification Level 3",
    },
    "it-computer-system": {
        "title": "IT Computer System Management (Level 3)",
        "short": "IT Computer System",
        "code": "IT-020-3:2013",
        "description": "NOSS IT-020-3:2013 — IT Computer System Management Level 3",
    },
}

# File type labels for lesson titles
FILE_TYPE_LABELS = {
    "KP": "Information Sheet",
    "KT": "Assignment Sheet",
    "KK": "Work Sheet",
    "PA": "Performance Assessment",
    "PM-TEORI": "Theory Lesson Plan",
    "PM-AMALI": "Practical Lesson Plan",
}

session = requests.Session()


def login():
    resp = session.post(f"{LMS_URL}/api/method/login", data={
        "usr": USERNAME,
        "pwd": PASSWORD
    })
    resp.raise_for_status()
    print("Logged in successfully.")


def api_get(doctype, name):
    resp = session.get(f"{LMS_URL}/api/resource/{doctype}/{name}")
    if resp.status_code == 200:
        return resp.json().get("data")
    return None


def api_search(doctype, filters):
    """Search for a doc by filters, return first match name or None"""
    import urllib.parse
    f = json.dumps(filters)
    resp = session.get(
        f"{LMS_URL}/api/resource/{doctype}",
        params={"filters": f, "fields": '["name","title"]', "limit": 1}
    )
    if resp.status_code == 200:
        data = resp.json().get("data", [])
        if data:
            return data[0].get("name")
    return None


def api_create(doctype, data):
    resp = session.post(
        f"{LMS_URL}/api/resource/{doctype}",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data)
    )
    if resp.status_code in (200, 201):
        return resp.json().get("data")
    elif resp.status_code == 409:
        # Already exists — fetch its real Frappe name by title search
        title = data.get("title", data.get("name", ""))
        filters = [["title", "=", title]]
        if doctype == "Course Chapter" and "course" in data:
            filters.append(["course", "=", data["course"]])
        existing_name = api_search(doctype, filters)
        if existing_name:
            print(f"  [EXIST] {doctype}: {existing_name}")
            return {"name": existing_name, "_existed": True}
        print(f"  [EXIST] {doctype}: {title} (name lookup failed)")
        return {"name": title, "_existed": True}
    else:
        error = resp.text[:300]
        print(f"  [ERROR {resp.status_code}] {doctype}: {error}")
        return None


def strip_jpk_envelope(content):
    """Remove JPK envelope HTML block from markdown content"""
    content = re.sub(
        r'<!-- JPK_ENVELOPE_v1 -->.*?<!-- /JPK_ENVELOPE_v1 -->',
        '',
        content,
        flags=re.DOTALL
    )
    return content.strip()


def get_file_type(filename_stem):
    """Determine the file type from stem: KP, KT, KK, KA, PA, PM-TEORI, PM-AMALI"""
    stem = filename_stem.upper()
    if stem.startswith("KA"):
        return "KA"
    elif stem.startswith("KP"):
        return "KP"
    elif stem.startswith("KT"):
        return "KT"
    elif stem.startswith("KK"):
        return "KK"
    elif stem.startswith("PA"):
        return "PA"
    elif stem.startswith("PM-TEORI") or stem.startswith("PM_TEORI"):
        return "PM-TEORI"
    elif stem.startswith("PM-AMALI") or stem.startswith("PM_AMALI"):
        return "PM-AMALI"
    elif stem.startswith("PM"):
        return "PM-TEORI"
    return "OTHER"


def make_lesson_title(file_stem, file_type):
    """Generate a human-readable lesson title from file stem and type"""
    label = FILE_TYPE_LABELS.get(file_type, file_type)
    # Extract sequence and topic from stem like KP-01-prepare-body-consultation-work-area
    parts = file_stem.split("-")
    if len(parts) >= 3 and parts[1].isdigit():
        seq = parts[1]
        topic = " ".join(p.capitalize() for p in parts[2:])
        return f"{label} {seq}: {topic}"
    else:
        # KA, PA, PM-teori etc — extract topic after type prefix
        topic_parts = [p for p in parts if not p.upper() in ("KA", "KP", "KT", "KK", "PA", "PM", "TEORI", "AMALI")]
        topic = " ".join(p.capitalize() for p in topic_parts) if topic_parts else file_stem
        return f"{label}: {topic}"


def parse_ka_mcq(content):
    """
    Parse MCQ questions from KA file.
    Handles 3 formats:
      - Aesthetic/IT: **N.** questions, A./B. options on separate lines, key: 1-C, 2-B
      - BEV: **AN.** questions, - A. options, key: A1: B | A2: C
      - Tuinalogy: N. question A) opt　B) opt on one line, key in table | 11–25 | B,B,C...
    Returns list of dicts: {question_num, question, options {A:text,...}, correct letter}
    """
    answer_key = {}

    # --- Answer key extraction ---

    # Format 1 (Aesthetic/IT): "1-C, 2-B, 3-C, ..."
    for m in re.finditer(r'(\d+)-([A-D])\b', content):
        num = int(m.group(1))
        if 1 <= num <= 10 and num not in answer_key:
            answer_key[num] = m.group(2)

    # Format 2 (BEV): "A1: B | A2: C | ..." OR "A1:C A2:B ..." — mapped to 1..10
    bev_key_match = re.search(r'A(\d+):\s*([A-D])', content)
    if bev_key_match:
        for m in re.finditer(r'A(\d+):\s*([A-D])', content):
            answer_key[int(m.group(1))] = m.group(2)

    # Format 3 (Tuinalogy): table row "| 11–25 | B, B, C, ..." -> map 11..25
    tui_key_match = re.search(r'\|\s*(\d+)[–-](\d+)\s*\|\s*([A-D](?:,\s*[A-D])+)', content)
    if tui_key_match:
        start_num = int(tui_key_match.group(1))
        letters = [x.strip() for x in tui_key_match.group(3).split(',')]
        for i, letter in enumerate(letters):
            answer_key[start_num + i] = letter

    # --- Question parsing ---

    questions = []

    # Format 1: **N.** (aesthetic/IT) — multi-line or same-line options A./B./C./D.
    aesthetic_section = re.search(
        r'(?:## Section A|## SECTION A).*?(?=## Section B|## SECTION B|## Marking|---\s*\n##)',
        content, re.DOTALL | re.IGNORECASE
    )
    if aesthetic_section:
        section_text = aesthetic_section.group(0)
        q_blocks = re.split(r'\n\s*\*\*(\d+)\.\*\*\s*', section_text)
        i = 1
        while i < len(q_blocks) - 1:
            q_num_str = q_blocks[i]
            q_body = q_blocks[i + 1]
            i += 2
            if not q_num_str.isdigit():
                continue
            q_num = int(q_num_str)

            options = {}
            q_text = q_body.strip()

            # Try multi-line options: each A./B./C./D. on its own line (with optional "- " prefix)
            opt_pattern = re.compile(r'\n\s*-?\s*([A-D])[.)]\s+(.*?)(?=\n\s*-?\s*[A-D][.)]\s+|\Z)', re.DOTALL)
            opt_start = re.search(r'\n\s*-?\s*[A-D][.)]\s+', q_body)
            if opt_start:
                q_text = q_body[:opt_start.start()].strip()
                for om in opt_pattern.finditer(q_body):
                    options[om.group(1)] = om.group(2).strip()

            # Fallback: inline options on one line "A. opt B. opt C. opt D. opt"
            # Also trigger when multi-line only captured A (B/C/D on same line as A)
            if not options or len(options) < 4:
                inline_m = re.search(
                    r'A\.\s+(.*?)\s+B\.\s+(.*?)\s+C\.\s+(.*?)\s+D\.\s+(.*?)(?:\s*$|\s*\|)',
                    q_body
                )
                if inline_m:
                    # Question text is everything before the A. match
                    q_text = q_body[:inline_m.start()].strip()
                    options = {
                        "A": inline_m.group(1).strip(),
                        "B": inline_m.group(2).strip(),
                        "C": inline_m.group(3).strip(),
                        "D": inline_m.group(4).strip(),
                    }

            if q_text and options:
                questions.append({
                    "question_num": q_num,
                    "question": q_text,
                    "options": options,
                    "correct": answer_key.get(q_num, "A"),
                })

    # Format 2: **AN.** (BEV) — multi-line options "- A. text"
    if not questions:
        bev_section = re.search(
            r'(?:## SECTION A|## Section A).*?(?=## SECTION B|## Section B|---\s*\n##)',
            content, re.DOTALL | re.IGNORECASE
        )
        if bev_section:
            section_text = bev_section.group(0)
            q_blocks = re.split(r'\n\s*\*\*A(\d+)\.\*\*\s*', section_text)
            i = 1
            while i < len(q_blocks) - 1:
                q_num = int(q_blocks[i])
                q_body = q_blocks[i + 1]
                i += 2
                opt_start = re.search(r'\n\s*-\s*[A-D][.)]\s+', q_body)
                q_text = q_body[:opt_start.start()].strip() if opt_start else q_body.strip()
                options = {}
                for om in re.finditer(r'\n\s*-\s*([A-D])[.)]\s+(.*?)(?=\n\s*-\s*[A-D][.)]\s+|\Z)', q_body, re.DOTALL):
                    options[om.group(1)] = om.group(2).strip()
                if q_text and options:
                    questions.append({
                        "question_num": q_num,
                        "question": q_text,
                        "options": options,
                        "correct": answer_key.get(q_num, "A"),
                    })

    # Format 3: Tuinalogy — "N. text：A) opt　B) opt　C) opt　D) opt" on one line
    # Note: question text ends with ：(fullwidth colon) directly before A), no space required
    if not questions:
        for m in re.finditer(
            r'^\s*(\d+)[.)]\s+(.*?)[：:]?\s*A[)）]\s*(.*?)[\s　]+B[)）]\s*(.*?)[\s　]+C[)）]\s*(.*?)[\s　]+D[)）]\s*(.*?)$',
            content, re.MULTILINE
        ):
            q_num = int(m.group(1))
            if q_num < 10:  # Skip fill-in-blank (questions 1-10 in tuinalogy)
                continue
            questions.append({
                "question_num": q_num,
                "question": m.group(2).strip().rstrip('：:'),
                "options": {
                    "A": m.group(3).strip(),
                    "B": m.group(4).strip(),
                    "C": m.group(5).strip(),
                    "D": m.group(6).strip(),
                },
                "correct": answer_key.get(q_num, "A"),
            })

    # Format 4: Single-line MCQ (Aesthetic C03+) — "**N.** question A. opt B. opt C. opt D. opt"
    if not questions:
        for m in re.finditer(
            r'^\s*\*\*(\d+)\.\*\*\s+(.*?)\s+A\.\s+(.*?)\s+B\.\s+(.*?)\s+C\.\s+(.*?)\s+D\.\s+(.*?)$',
            content, re.MULTILINE
        ):
            q_num = int(m.group(1))
            questions.append({
                "question_num": q_num,
                "question": m.group(2).strip(),
                "options": {
                    "A": m.group(3).strip(),
                    "B": m.group(4).strip(),
                    "C": m.group(5).strip(),
                    "D": m.group(6).strip(),
                },
                "correct": answer_key.get(q_num, "A"),
            })

    # Format 5: IT — "**N.**" with "- (a)/(b)/(c)/(d)" options (lowercase, no answer key in file)
    if not questions:
        it_section = re.search(
            r'(?:BAHAGIAN A|SECTION A).*?(?=BAHAGIAN B|SECTION B|---)',
            content, re.DOTALL | re.IGNORECASE
        )
        section_for_it = it_section.group(0) if it_section else content
        q_blocks = re.split(r'\n\s*\*\*(\d+)\.\*\*\s*', section_for_it)
        i = 1
        while i < len(q_blocks) - 1:
            q_num_str = q_blocks[i]
            q_body = q_blocks[i + 1]
            i += 2
            if not q_num_str.isdigit():
                continue
            q_num = int(q_num_str)
            # Options: "- (a) text" lowercase
            opt_start = re.search(r'\n\s*-\s*\(([a-d])\)', q_body)
            q_text = q_body[:opt_start.start()].strip() if opt_start else q_body.strip()
            options = {}
            letter_map = {"a": "A", "b": "B", "c": "C", "d": "D"}
            for om in re.finditer(r'\n\s*-\s*\(([a-d])\)\s*(.*?)(?=\n\s*-\s*\([a-d]\)|\Z)', q_body, re.DOTALL):
                options[letter_map[om.group(1)]] = om.group(2).strip()
            if q_text and len(options) >= 2:
                questions.append({
                    "question_num": q_num,
                    "question": q_text,
                    "options": options,
                    "correct": answer_key.get(q_num, "A"),
                })

    # Format 6: BEV C02+ inline — "**A1.** question text A. opt B. opt C. opt D. opt"
    # (BEV section found but options not on separate lines — inline without "- " prefix)
    if not questions:
        bev_section2 = re.search(
            r'(?:## SECTION A|## Section A).*?(?=## SECTION B|## Section B|---\s*\n##|\Z)',
            content, re.DOTALL | re.IGNORECASE
        )
        if bev_section2:
            section_text = bev_section2.group(0)
            for m in re.finditer(
                r'\*\*A(\d+)\.\*\*\s+(.*?)\s+A\.\s+(.*?)\s+B\.\s+(.*?)\s+C\.\s+(.*?)\s+D\.\s+(.*?)(?:\n|$)',
                section_text
            ):
                q_num = int(m.group(1))
                questions.append({
                    "question_num": q_num,
                    "question": m.group(2).strip(),
                    "options": {
                        "A": m.group(3).strip(),
                        "B": m.group(4).strip(),
                        "C": m.group(5).strip(),
                        "D": m.group(6).strip(),
                    },
                    "correct": answer_key.get(q_num, "A"),
                })

    # Format 7: IT L3-C02+ "### Q1 — Title" with "(a) opt  (b) opt  (c) opt  (d) opt"
    # and "**Answer:** (b)" on its own line
    if not questions:
        for m in re.finditer(
            r'### Q(\d+)[^\n]*\n(?:.*?\n)*?(?:.*?\n)?(.*?)\n\n\(a\)\s+(.*?)\s+\(b\)\s+(.*?)\s+\(c\)\s+(.*?)\s+\(d\)\s+(.*?)\n\n\*\*Answer:\*\*\s+\(([a-d])\)',
            content, re.DOTALL
        ):
            pass  # complex multiline — use block approach below

        # Block-based approach for IT Q# format
        q_blocks_it = re.split(r'\n### Q(\d+)[^\n]*\n', content)
        i = 1
        letter_map = {"a": "A", "b": "B", "c": "C", "d": "D"}
        while i < len(q_blocks_it) - 1:
            q_num_str = q_blocks_it[i]
            q_body = q_blocks_it[i + 1]
            i += 2
            if not q_num_str.isdigit():
                continue
            q_num = int(q_num_str)
            # Only process MCQ blocks (skip Short Answer, Scenario)
            if "**Type:** MCQ" not in q_body and "Type:** MCQ" not in q_body:
                continue
            # Find the question text (line after metadata line)
            lines_body = [l for l in q_body.strip().split('\n') if l.strip()]
            # Skip metadata lines (Type/Difficulty/Marks/LO Ref)
            q_text = ""
            options_line = ""
            answer_letter = "A"
            for j, line in enumerate(lines_body):
                if line.startswith("**Type:**") or line.startswith("**Difficulty:**"):
                    continue
                # Options line: starts with (a)
                if re.match(r'\(a\)', line.strip()):
                    options_line = line.strip()
                    continue
                # Answer line
                ans_m = re.search(r'\*\*Answer:\*\*\s+\(([a-d])\)', line)
                if ans_m:
                    answer_letter = letter_map[ans_m.group(1)]
                    continue
                if not q_text and not line.startswith("**"):
                    q_text = line.strip()
            if not q_text or not options_line:
                continue
            # Parse "(a) opt  (b) opt  (c) opt  (d) opt"
            opts_m = re.search(
                r'\(a\)\s+(.*?)\s+\(b\)\s+(.*?)\s+\(c\)\s+(.*?)\s+\(d\)\s+(.*?)$',
                options_line
            )
            if not opts_m:
                continue
            options = {
                "A": opts_m.group(1).strip(),
                "B": opts_m.group(2).strip(),
                "C": opts_m.group(3).strip(),
                "D": opts_m.group(4).strip(),
            }
            questions.append({
                "question_num": q_num,
                "question": q_text,
                "options": options,
                "correct": answer_letter,
            })

    # Format 8: Tuinalogy E01/E02 — "N. question" + "- A. opt  **B. opt**  C. opt  D. opt"
    # Correct answer is bold: **B. opt**
    if not questions:
        # Look for numbered questions with "- A." option lines below
        q_blocks_tui = re.split(r'\n(\d+)\.\s+', content)
        i = 1
        while i < len(q_blocks_tui) - 1:
            q_num_str = q_blocks_tui[i]
            q_body = q_blocks_tui[i + 1]
            i += 2
            if not q_num_str.isdigit():
                continue
            q_num = int(q_num_str)
            # Only MCQ (first line of q_body should be question text, second line starts with "- A.")
            lines_b = q_body.split('\n')
            if len(lines_b) < 2:
                continue
            q_text = lines_b[0].strip()
            # Find the options line (starts with "- A." or "   - A.")
            opt_line = ""
            for line in lines_b[1:]:
                if re.search(r'-\s+\**A\.', line):
                    opt_line = line.strip()
                    break
            if not opt_line:
                continue
            # Parse "A. opt  **B. opt**  C. opt  D. opt" — bold marks correct answer
            # Remove leading "- "
            opt_line = re.sub(r'^-\s*', '', opt_line)
            # Find correct answer (bolded option letter)
            correct_m = re.search(r'\*\*([A-D])\.\s', opt_line)
            answer_letter = correct_m.group(1) if correct_m else "A"
            # Strip bold markers for clean option text
            opt_line_clean = re.sub(r'\*\*', '', opt_line)
            opts_m = re.search(
                r'A\.\s+(.*?)\s+B\.\s+(.*?)\s+C\.\s+(.*?)\s+D\.\s+(.*?)$',
                opt_line_clean
            )
            if not opts_m:
                continue
            options = {
                "A": opts_m.group(1).strip(),
                "B": opts_m.group(2).strip(),
                "C": opts_m.group(3).strip(),
                "D": opts_m.group(4).strip(),
            }
            questions.append({
                "question_num": q_num,
                "question": q_text,
                "options": options,
                "correct": answer_letter,
            })

    # Format 10: BEV C04 "**Q1.**" with inline options + table answer key "| Q1 | B | Q6 | C |"
    if not questions:
        # Extract answer key from table: | Q1 | B | Q6 | C |
        q_table_key = {}
        for row_m in re.finditer(r'\|\s*Q(\d+)\s*\|\s*([A-D])\s*\|', content):
            q_table_key[int(row_m.group(1))] = row_m.group(2)

        bev_q_section = re.search(
            r'(?:Section A|SECTION A|Bahagian A)[^\n]*\n.*?(?=## |### Bahagian B|---\s*\n##|\Z)',
            content, re.DOTALL | re.IGNORECASE
        )
        section_for_q = bev_q_section.group(0) if bev_q_section else content
        for m in re.finditer(
            r'\*\*Q(\d+)\.\*\*\s+(.*?)\s+A\.\s+(.*?)\s+B\.\s+(.*?)\s+C\.\s+(.*?)\s+D\.\s+(.*?)(?:\n|$)',
            section_for_q
        ):
            q_num = int(m.group(1))
            correct = q_table_key.get(q_num, answer_key.get(q_num, "A"))
            questions.append({
                "question_num": q_num,
                "question": m.group(2).strip(),
                "options": {
                    "A": m.group(3).strip(),
                    "B": m.group(4).strip(),
                    "C": m.group(5).strip(),
                    "D": m.group(6).strip(),
                },
                "correct": correct,
            })

    # Format 9: Tuinalogy C04 Chinese MCQ — "N. question" + "   A. opt B. opt C. opt D. opt" (indented, inline)
    # No answer key — default to A (or first option)
    if not questions:
        # Look for numbered questions where next non-blank line has "   A." indented options
        lines_all = content.split('\n')
        j = 0
        while j < len(lines_all):
            line = lines_all[j]
            # Question line: "N. text" where N is 1-25
            q_m = re.match(r'^(\d+)\.\s+(.+)$', line.strip())
            if q_m and 1 <= int(q_m.group(1)) <= 25:
                q_num = int(q_m.group(1))
                q_text = q_m.group(2).strip()
                # Look ahead for the options line (indented with spaces, starts with A.)
                opt_line = ""
                for k in range(j + 1, min(j + 4, len(lines_all))):
                    if re.match(r'\s+A\.', lines_all[k]):
                        opt_line = lines_all[k].strip()
                        break
                if opt_line:
                    opts_m = re.search(
                        r'A\.\s+(.*?)\s+B\.\s+(.*?)\s+C\.\s+(.*?)\s+D\.\s+(.*?)$',
                        opt_line
                    )
                    if opts_m:
                        questions.append({
                            "question_num": q_num,
                            "question": q_text,
                            "options": {
                                "A": opts_m.group(1).strip(),
                                "B": opts_m.group(2).strip(),
                                "C": opts_m.group(3).strip(),
                                "D": opts_m.group(4).strip(),
                            },
                            "correct": answer_key.get(q_num, "A"),
                        })
            j += 1

    # Cap at 10 questions for LMS quiz
    return questions[:10]


def create_lms_question(q_data):
    """Create an LMS Question doctype record"""
    options = q_data.get("options", {})
    correct = q_data.get("correct", "A")

    data = {
        "doctype": "LMS Question",
        "question": q_data["question"],
        "type": "Choices",
        "option_1": options.get("A", ""),
        "option_2": options.get("B", ""),
        "option_3": options.get("C", ""),
        "option_4": options.get("D", ""),
        "is_correct_1": 1 if correct == "A" else 0,
        "is_correct_2": 1 if correct == "B" else 0,
        "is_correct_3": 1 if correct == "C" else 0,
        "is_correct_4": 1 if correct == "D" else 0,
    }

    return api_create("LMS Question", data)


def create_lms_quiz(title, questions_data, course):
    """Create LMS Quiz with questions"""
    q_docs = []
    for q in questions_data:
        q_doc = create_lms_question(q)
        if q_doc:
            q_docs.append(q_doc.get("name"))

    if not q_docs:
        print("    [WARN] No questions created for quiz, skipping.")
        return None

    quiz_data = {
        "doctype": "LMS Quiz",
        "title": title,
        "course": course,
        "total_marks": len(q_docs) * 2,
        "passing_percentage": 60,
        "questions": [{"question": q} for q in q_docs],
    }

    return api_create("LMS Quiz", quiz_data)


def import_subject(subject_folder):
    subject_info = SUBJECTS.get(subject_folder)
    if not subject_info:
        print(f"[ERROR] Unknown subject: {subject_folder}")
        return

    subject_path = NOSS_DIR / subject_folder
    if not subject_path.exists():
        print(f"[ERROR] Folder not found: {subject_path}")
        return

    print(f"\n{'='*60}")
    print(f"  Subject: {subject_info['title']}")
    print(f"{'='*60}")

    # Create LMS Course
    course_data = {
        "doctype": "LMS Course",
        "title": subject_info["title"],
        "short_introduction": subject_info["description"],
        "description": subject_info["description"],
        "published": 1,
        "paid_course": 0,
        "instructors": [
            {"instructor": "Administrator"}
        ],
    }
    course_doc = api_create("LMS Course", course_data)
    if not course_doc:
        print(f"[ERROR] Failed to create course: {subject_info['title']}")
        return

    course_name = course_doc.get("name")
    print(f"  Course: {course_name}")

    # Get CU folders (skip _ prefixed)
    cu_folders = sorted([
        d for d in subject_path.iterdir()
        if d.is_dir() and not d.name.startswith("_")
    ])

    for cu_path in cu_folders:
        cu_name = cu_path.name
        print(f"\n  --- Chapter: {cu_name} ---")

        # Create Course Chapter
        chapter_title = cu_name.upper()
        chapter_data = {
            "doctype": "Course Chapter",
            "title": chapter_title,
            "course": course_name,
        }
        chapter_doc = api_create("Course Chapter", chapter_data)
        if not chapter_doc:
            print(f"    [ERROR] Failed to create chapter: {chapter_title}")
            continue

        chapter_name = chapter_doc.get("name")
        print(f"    Chapter: {chapter_name}")

        # Process lesson files in sorted order
        lesson_files = sorted(cu_path.glob("*.md"))

        for lesson_file in lesson_files:
            stem = lesson_file.stem
            file_type = get_file_type(stem)

            try:
                content = lesson_file.read_text(encoding="utf-8")
            except Exception as e:
                print(f"    [ERROR] Read failed for {lesson_file.name}: {e}")
                continue

            if file_type == "KA":
                # Parse and create quiz
                print(f"    [KA] Parsing quiz: {lesson_file.name}")
                questions = parse_ka_mcq(content)
                print(f"         Found {len(questions)} MCQ questions")

                if questions:
                    quiz_title = f"{subject_info['short']} {cu_name} — Knowledge Assessment"
                    quiz_doc = create_lms_quiz(quiz_title, questions, course_name)

                    if quiz_doc:
                        quiz_id = quiz_doc.get("name")
                        # Create a lesson that links to the quiz
                        lesson_data = {
                            "doctype": "Course Lesson",
                            "title": f"{cu_name} — Knowledge Assessment",
                            "chapter": chapter_name,
                            "course": course_name,
                            "body": strip_jpk_envelope(content)[:5000],
                            "quiz_id": quiz_id,
                        }
                        api_create("Course Lesson", lesson_data)
                        print(f"         Quiz created: {quiz_id} ({len(questions)} questions)")

            else:
                # Regular lesson (KP, KT, KK, PA, PM-teori, PM-amali)
                lesson_title = make_lesson_title(stem, file_type)
                clean_body = strip_jpk_envelope(content)

                lesson_data = {
                    "doctype": "Course Lesson",
                    "title": lesson_title,
                    "chapter": chapter_name,
                    "course": course_name,
                    "body": clean_body,
                }
                lesson_doc = api_create("Course Lesson", lesson_data)
                if lesson_doc:
                    print(f"    [OK] {lesson_title[:70]}")

    print(f"\n  Done: {subject_info['title']}")


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "all"

    login()

    if target == "all":
        for subject_folder in SUBJECTS:
            import_subject(subject_folder)
    elif target in SUBJECTS:
        import_subject(target)
    else:
        print(f"Unknown target: {target}")
        print(f"Valid: all, {', '.join(SUBJECTS.keys())}")
        sys.exit(1)

    print("\n\nImport complete.")


if __name__ == "__main__":
    main()
