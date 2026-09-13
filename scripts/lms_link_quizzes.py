#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
Wire up Tuinalogy LMS Quizzes to lessons so students can take them interactively.

For each chapter (C01-C05, E01, E02):
  1. Creates a "Knowledge Assessment" Course Lesson with quiz_id set
  2. Appends the lesson to the chapter's Lesson Reference child table
  3. Fixes the quiz's course field to the active tuinalogy course

Usage: uv run scripts/lms_link_quizzes.py
"""

import sys
import requests

LMS_URL = "http://localhost:8001"
USERNAME = "Administrator"
PASSWORD = "admin"
COURSE = "tuinalogy-services-level-3"

# Map chapter short names to quiz names
QUIZ_MAP = {
    "C01": "tuinalogy-services-c01-knowledge-assessment",
    "C02": "tuinalogy-services-c02-knowledge-assessment",
    "C03": "tuinalogy-services-c03-knowledge-assessment",
    "C04": "tuinalogy-services-c04-knowledge-assessment",
    "C05": "tuinalogy-services-c05-knowledge-assessment",
    "E01": "tuinalogy-services-e01-knowledge-assessment",
    "E02": "tuinalogy-services-e02-knowledge-assessment",
}

session = requests.Session()
session.headers.update({"Expect": ""})


def login():
    resp = session.post(f"{LMS_URL}/api/method/login", data={"usr": USERNAME, "pwd": PASSWORD})
    resp.raise_for_status()
    print("Logged in.")


def get_course_chapters() -> dict[str, str]:
    """Returns {short_name: chapter_docname} e.g. {'C01': '0069 C01'}"""
    resp = session.get(f"{LMS_URL}/api/resource/LMS Course/{COURSE}")
    resp.raise_for_status()
    chapters = resp.json()["data"].get("chapters", [])
    result = {}
    for c in chapters:
        ch = c["chapter"]  # e.g. "0069 C01"
        short = ch.split(" ")[-1]  # "C01"
        result[short] = ch
    return result


def get_chapter_lessons(chapter_name: str) -> list[dict]:
    resp = session.get(f"{LMS_URL}/api/resource/Course Chapter/{chapter_name}")
    resp.raise_for_status()
    return resp.json()["data"].get("lessons", [])


def lesson_exists(chapter_name: str, quiz_id: str) -> str | None:
    """Return existing lesson name if a quiz lesson already exists in this chapter."""
    lessons = get_chapter_lessons(chapter_name)
    for l in lessons:
        lname = l.get("lesson", "")
        if "Knowledge Assessment" in lname:
            return lname
    return None


def create_quiz_lesson(chapter_name: str, cu_code: str, quiz_id: str) -> str:
    """Create a Course Lesson with quiz_id set."""
    title = f"Knowledge Assessment: {cu_code}"
    body = f"## 知识评估 — {cu_code}\n\n请完成以下选择题。每题均有唯一正确答案。\n\n*Please complete the multiple-choice quiz below. Each question has one correct answer.*"
    data = {
        "doctype": "Course Lesson",
        "title": title,
        "chapter": chapter_name,
        "course": COURSE,
        "body": body,
        "quiz_id": quiz_id,
    }
    resp = session.post(f"{LMS_URL}/api/resource/Course Lesson", json=data)
    resp.raise_for_status()
    name = resp.json()["data"]["name"]
    print(f"  Created lesson: {name}")
    return name


def append_lesson_to_chapter(chapter_name: str, lesson_name: str):
    """Append the new lesson to the chapter's lessons child table."""
    lessons = get_chapter_lessons(chapter_name)
    # Check if already linked
    if any(l.get("lesson") == lesson_name for l in lessons):
        print(f"  Already linked to chapter.")
        return
    lessons.append({"lesson": lesson_name})
    resp = session.put(
        f"{LMS_URL}/api/resource/Course Chapter/{chapter_name}",
        json={"lessons": lessons},
    )
    resp.raise_for_status()
    print(f"  Linked to chapter {chapter_name}")


def fix_quiz_course(quiz_name: str, lesson_name: str):
    """Update quiz course + lesson fields."""
    resp = session.put(
        f"{LMS_URL}/api/resource/LMS Quiz/{quiz_name}",
        json={"course": COURSE, "lesson": lesson_name},
    )
    resp.raise_for_status()
    print(f"  Quiz {quiz_name}: course + lesson updated")


def main():
    login()
    chapters = get_course_chapters()
    print(f"Found {len(chapters)} chapters: {list(chapters.keys())}")

    for cu_code, chapter_name in sorted(chapters.items()):
        quiz_id = QUIZ_MAP.get(cu_code)
        if not quiz_id:
            print(f"\n[{cu_code}] No quiz mapping — skipping")
            continue

        print(f"\n[{cu_code}] chapter={chapter_name} quiz={quiz_id}")

        # Check if KA lesson already exists
        existing = lesson_exists(chapter_name, quiz_id)
        if existing:
            print(f"  KA lesson already exists: {existing}")
            lesson_name = existing
        else:
            lesson_name = create_quiz_lesson(chapter_name, cu_code, quiz_id)
            append_lesson_to_chapter(chapter_name, lesson_name)

        fix_quiz_course(quiz_id, lesson_name)

    print("\nDone. Run 'lms cache' to refresh.")


if __name__ == "__main__":
    main()
