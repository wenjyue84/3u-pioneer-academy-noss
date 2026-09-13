#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
Create only quizzes (KA files) for a subject — skip lessons.
Usage: uv run python lms_quiz_only.py it-computer-system
"""

import sys
import json
import requests
from pathlib import Path

# Import shared functions from lms_import
sys.path.insert(0, str(Path(__file__).parent))
from lms_import import (
    LMS_URL, USERNAME, PASSWORD, SUBJECTS, NOSS_DIR,
    parse_ka_mcq, create_lms_quiz, create_lms_question,
    api_create, api_search, login, session, strip_jpk_envelope
)


def get_course_name(subject_info):
    """Get or create the LMS course and return its name"""
    course_data = {
        "doctype": "LMS Course",
        "title": subject_info["title"],
        "short_introduction": subject_info["description"],
        "description": subject_info["description"],
        "published": 1,
        "paid_course": 0,
        "instructors": [{"instructor": "Administrator"}],
    }
    course_doc = api_create("LMS Course", course_data)
    if not course_doc:
        print(f"[ERROR] Could not get course: {subject_info['title']}")
        return None
    return course_doc.get("name")


def get_chapter_name(cu_name, course_name):
    """Get or create a course chapter and return its name"""
    chapter_data = {
        "doctype": "Course Chapter",
        "title": cu_name.upper(),
        "course": course_name,
    }
    chapter_doc = api_create("Course Chapter", chapter_data)
    if not chapter_doc:
        return None
    return chapter_doc.get("name")


def quiz_exists(title):
    """Check if a quiz with this title already exists"""
    existing = api_search("LMS Quiz", [["title", "=", title]])
    return existing is not None


def process_ka_only(subject_folder):
    subject_info = SUBJECTS.get(subject_folder)
    if not subject_info:
        print(f"[ERROR] Unknown subject: {subject_folder}")
        return

    subject_path = NOSS_DIR / subject_folder
    if not subject_path.exists():
        print(f"[ERROR] Folder not found: {subject_path}")
        return

    print(f"\n{'='*60}")
    print(f"  Subject (quiz-only): {subject_info['title']}")
    print(f"{'='*60}")

    course_name = get_course_name(subject_info)
    if not course_name:
        return
    print(f"  Course: {course_name}")

    cu_folders = sorted([
        d for d in subject_path.iterdir()
        if d.is_dir() and not d.name.startswith("_")
    ])

    for cu_path in cu_folders:
        cu_name = cu_path.name
        ka_files = sorted(cu_path.glob("KA*.md"))
        if not ka_files:
            continue

        print(f"\n  --- Chapter: {cu_name} ---")

        for ka_file in ka_files:
            print(f"    [KA] Parsing quiz: {ka_file.name}")
            try:
                content = ka_file.read_text(encoding="utf-8")
            except Exception as e:
                print(f"    [ERROR] Read failed: {e}")
                continue

            questions = parse_ka_mcq(content)
            print(f"         Found {len(questions)} MCQ questions")

            if not questions:
                continue

            quiz_title = f"{subject_info['short']} {cu_name} — Knowledge Assessment"

            # Skip if quiz already exists
            if quiz_exists(quiz_title):
                print(f"         [EXIST] Quiz already exists: {quiz_title}")
                continue

            chapter_name = get_chapter_name(cu_name, course_name)
            if not chapter_name:
                print(f"    [ERROR] Could not get chapter for {cu_name}")
                continue

            quiz_doc = create_lms_quiz(quiz_title, questions, course_name)
            if quiz_doc:
                quiz_id = quiz_doc.get("name")
                # Also create lesson linking to quiz
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
                print(f"    [ERROR] Failed to create quiz: {quiz_title}")

    print(f"\n  Done: {subject_info['title']}")


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else None
    if not target:
        print("Usage: python lms_quiz_only.py <subject_folder>")
        print(f"Valid: {', '.join(SUBJECTS.keys())}")
        sys.exit(1)

    login()

    if target == "all":
        for subject_folder in SUBJECTS:
            process_ka_only(subject_folder)
    elif target in SUBJECTS:
        process_ka_only(target)
    else:
        print(f"Unknown target: {target}")
        print(f"Valid: all, {', '.join(SUBJECTS.keys())}")
        sys.exit(1)

    print("\n\nQuiz import complete.")


if __name__ == "__main__":
    main()
