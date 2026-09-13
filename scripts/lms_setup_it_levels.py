#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
Set up IT Computer System Management Level 4 and Level 5 courses in the LMS,
then create a sequential Programme (L3 → L4 → L5) with enforce_course_order=1.

Level 3 already exists. This script creates L4/L5 as shell courses (no lessons yet)
and wires all three into a sequential Programme so students must complete L3 → L4 → L5.

Usage: uv run scripts/lms_setup_it_levels.py
"""

import sys
import requests

LMS_URL = "http://localhost:8001"
USERNAME = "Administrator"
PASSWORD = "admin"

L3_COURSE = "it-computer-system-management-level-3"

session = requests.Session()
session.headers.update({"Expect": ""})


def login():
    r = session.post(f"{LMS_URL}/api/method/login", data={"usr": USERNAME, "pwd": PASSWORD})
    r.raise_for_status()
    print("Logged in.")


def api_post(doctype, data):
    r = session.post(f"{LMS_URL}/api/resource/{doctype}", json=data)
    if not r.ok:
        print(f"  ERROR {r.status_code}: {r.text[:400]}", file=sys.stderr)
        r.raise_for_status()
    return r.json().get("data", {})


def get_course_by_title(title: str) -> str | None:
    """Return existing course name if a course with this title already exists."""
    r = session.get(
        f"{LMS_URL}/api/resource/LMS Course",
        params={"fields": '["name","title"]', "filters": f'[["title","=","{title}"]]', "limit": 1},
    )
    r.raise_for_status()
    results = r.json().get("data", [])
    return results[0]["name"] if results else None


def setup_course(title: str, short_intro: str, description: str) -> str:
    """Create course if not exists. Returns the course name."""
    existing = get_course_by_title(title)
    if existing:
        print(f"  Course '{title}' already exists: {existing} — skipping.")
        return existing

    data = api_post("LMS Course", {
        "title": title,
        "short_introduction": short_intro,
        "description": description,
        "published": 1,
        "paid_course": 0,
        "enable_certification": 1,
        "instructors": [{"instructor": "Administrator"}],
    })
    name = data["name"]
    print(f"  Created course: {name}")
    return name


def setup_programme(l4_name: str, l5_name: str):
    """Create the sequential IT Programme if not exists."""
    prog_title = "IT Computer System Management Programme"

    r = session.get(f"{LMS_URL}/api/resource/LMS Program/{prog_title}")
    if r.ok:
        print(f"  Programme '{prog_title}' already exists — skipping.")
        return

    data = api_post("LMS Program", {
        "title": prog_title,
        "published": 1,
        "enforce_course_order": 1,
        "program_courses": [
            {"course": L3_COURSE},
            {"course": l4_name},
            {"course": l5_name},
        ],
    })
    print(f"  Created Programme: {data.get('name')}")


def main():
    login()

    print("\n[1] Creating IT Level 4 course...")
    l4_name = setup_course(
        title="IT Computer System Management (Level 4)",
        short_intro="IT-020-4:2013 — Computer Systems Administration (Level 4)",
        description=(
            "NOSS IT-020-4:2013 Computer Systems Administration. "
            "Covers server infrastructure, network administration, and IT governance. "
            "Prerequisite: IT Computer System Management (Level 3)."
        ),
    )

    print("\n[2] Creating IT Level 5 course...")
    l5_name = setup_course(
        title="IT Computer System Management (Level 5)",
        short_intro="IT-020-5:2013 — Computer Systems Management (Level 5)",
        description=(
            "NOSS IT-020-5:2013 Computer Systems Management. "
            "Covers enterprise IT management, strategic planning, and ICT governance. "
            "Prerequisite: IT Computer System Management (Level 4)."
        ),
    )

    print("\n[3] Creating sequential IT Programme (L3 → L4 → L5)...")
    setup_programme(l4_name, l5_name)

    print("\nDone. Run 'lms cache' to refresh.")


if __name__ == "__main__":
    main()
