#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
Fix broken local .md file references in Frappe LMS lesson bodies.

Replaces references like:
  - 00-tuina-terminology.md（...）  →  Tuina Terminology Reference（...）
  - 00-cocu.md（...）               →  NOSS CoCU Reference（...）
  - `KT-01-some-file.md`           →  KT-01-some-file  (strip .md + backticks)

Usage: uv run scripts/lms_fix_md_refs.py
"""

import re
import sys
import requests

LMS_URL = "http://localhost:8001"
USERNAME = "Administrator"
PASSWORD = "admin"

session = requests.Session()
session.headers.update({"Expect": ""})


def login():
    resp = session.post(f"{LMS_URL}/api/method/login", data={"usr": USERNAME, "pwd": PASSWORD})
    resp.raise_for_status()
    print("Logged in.")


def get_active_lesson_names() -> list[str]:
    """Return lesson names linked to the active tuinalogy course only."""
    # Get chapters from the course document (child table has full fields)
    resp = session.get(f"{LMS_URL}/api/resource/LMS Course/tuinalogy-services-level-3")
    resp.raise_for_status()
    chapters = [c["chapter"] for c in resp.json().get("data", {}).get("chapters", [])]

    # Get lessons from each chapter document
    lessons = []
    for ch in chapters:
        r = session.get(f"{LMS_URL}/api/resource/Course Chapter/{ch}")
        r.raise_for_status()
        chapter_lessons = r.json().get("data", {}).get("lessons", [])
        lessons += [x["lesson"] for x in chapter_lessons if x.get("lesson")]
    return lessons


def get_lesson_body(name: str) -> str:
    resp = session.get(f"{LMS_URL}/api/resource/Course Lesson/{name}",
                       params={"fields": '["body"]'})
    resp.raise_for_status()
    return resp.json().get("data", {}).get("body") or ""


def patch_lesson(name: str, body: str):
    resp = session.put(f"{LMS_URL}/api/resource/Course Lesson/{name}", json={"body": body})
    resp.raise_for_status()


def fix_md_refs(body: str) -> str:
    # 1. 00-tuina-terminology.md (with optional Chinese annotation in parens)
    body = re.sub(
        r'00-tuina-terminology\.md(（[^）]*）)?',
        lambda m: f"Tuina Terminology Reference{m.group(1) or ''}",
        body,
    )

    # 2. 00-cocu.md (with optional Chinese annotation in parens or §)
    body = re.sub(
        r'00-cocu\.md(（[^）]*）|（[^(]*\)| 第[^\n、，]*| §[^\n、，]*)?',
        lambda m: f"NOSS CoCU Reference{m.group(1) or ''}",
        body,
    )

    # 3. Backtick-wrapped .md filenames: `KT-01-some-file.md` → KT-01-some-file
    body = re.sub(r'`([A-Za-z0-9_-]+)\.md`', r'\1', body)

    # 4. Bare filename.md references in text (not inside a URL/link)
    # e.g. 可参考 00-cocu.md → 可参考 NOSS CoCU Reference (already handled above)
    # Catch any remaining .md refs that slipped through
    body = re.sub(r'\b(KP|KT|KK|KA|PA|PM)[- ](\d+)[^\s）)]*?\.md\b',
                  lambda m: m.group(0).replace('.md', ''), body)

    return body


def main():
    login()
    lesson_names = get_active_lesson_names()
    print(f"Checking {len(lesson_names)} active course lessons...")

    patched = 0
    skipped = 0
    for name in lesson_names:
        body = get_lesson_body(name)
        if ".md" not in body:
            skipped += 1
            continue
        new_body = fix_md_refs(body)
        if new_body == body:
            skipped += 1
            continue
        try:
            patch_lesson(name, new_body)
            print(f"  ✓ {name}")
            patched += 1
        except Exception as e:
            print(f"  ✗ {name}: {e}", file=sys.stderr)

    print(f"\nDone. {patched} patched, {skipped} skipped (no .md refs).")


if __name__ == "__main__":
    main()
