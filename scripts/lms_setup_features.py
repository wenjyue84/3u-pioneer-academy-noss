#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
Set up student-facing LMS features for 3U Pioneer Academy NOSS courses:
  1. Completion Certificates (enable on all 4 courses + LMS Settings)
  2. NOSS Level 3 Programme (groups all 4 courses)
  3. April 2026 Intake Batch (cohort with timetable)
  4. Badges — First Step, Quiz Champion, Graduate

Usage: uv run scripts/lms_setup_features.py
"""

import io
import sys
import json
import datetime
import requests

LMS_URL = "http://localhost:8001"
USERNAME = "Administrator"
PASSWORD = "admin"

COURSES = [
    "tuinalogy-services-level-3",
    "aesthetic-services-level-3",
    "bev-diagnostic-rectification-level-3",
    "it-computer-system-management-level-3",
]

session = requests.Session()
session.headers.update({"Expect": ""})


def login():
    r = session.post(f"{LMS_URL}/api/method/login", data={"usr": USERNAME, "pwd": PASSWORD})
    r.raise_for_status()
    print("Logged in.")


def api_put(doctype, name, data):
    r = session.put(f"{LMS_URL}/api/resource/{doctype}/{name}", json=data)
    r.raise_for_status()
    return r.json().get("data", {})


def api_post(doctype, data):
    r = session.post(f"{LMS_URL}/api/resource/{doctype}", json=data)
    if not r.ok:
        print(f"  ERROR {r.status_code}: {r.text[:300]}", file=sys.stderr)
        r.raise_for_status()
    return r.json().get("data", {})


def upload_svg(filename: str, svg_content: str) -> str:
    """Upload an SVG string as a file, return the /files/... URL."""
    r = session.post(
        f"{LMS_URL}/api/method/upload_file",
        data={"is_private": 0, "folder": "Home/Attachments"},
        files={"file": (filename, io.BytesIO(svg_content.encode()), "image/svg+xml")},
    )
    r.raise_for_status()
    url = r.json().get("message", {}).get("file_url", "")
    print(f"  Uploaded {filename} → {url}")
    return url


# ── Step 1: Certificates ────────────────────────────────────────────────────

def setup_certificates():
    print("\n[1] Enabling completion certificates...")

    # Enable in LMS Settings
    api_put("LMS Settings", "LMS Settings", {
        "certifications": 1,
        "certified_members": 1,
    })
    print("  LMS Settings: certifications + certified_members enabled")

    # Enable on each course
    for course in COURSES:
        api_put("LMS Course", course, {"enable_certification": 1})
        print(f"  {course}: enable_certification = 1")


# ── Step 2: Programme ────────────────────────────────────────────────────────

def setup_programme():
    print("\n[2] Creating NOSS Level 3 Programme...")

    # Check if already exists
    r = session.get(f"{LMS_URL}/api/resource/LMS Program/NOSS Level 3 Programme")
    if r.ok:
        print("  Programme already exists — skipping.")
        return

    data = api_post("LMS Program", {
        "doctype": "LMS Program",
        "title": "NOSS Level 3 Programme",
        "published": 1,
        "enforce_course_order": 0,
        "program_courses": [{"course": c} for c in COURSES],
    })
    print(f"  Created: {data.get('name')}")


# ── Step 3: Batch ────────────────────────────────────────────────────────────

def _timetable_entries():
    """Generate Mon/Wed/Fri 09:00–12:00 entries from 2026-04-21 to 2026-07-31."""
    entries = []
    start = datetime.date(2026, 4, 21)
    end = datetime.date(2026, 7, 31)
    current = start
    while current <= end:
        if current.weekday() in (0, 2, 4):  # Mon=0, Wed=2, Fri=4
            entries.append({
                "date": str(current),
                "start_time": "09:00:00",
                "end_time": "12:00:00",
                "duration": "3 hours",
            })
        current += datetime.timedelta(days=1)
    return entries


def setup_batch():
    print("\n[3] Creating April 2026 Intake Batch...")

    r = session.get(f"{LMS_URL}/api/resource/LMS Batch/noss-level-3-april-2026-intake")
    if r.ok:
        print("  Batch already exists — skipping.")
        return

    timetable = _timetable_entries()
    print(f"  Generating {len(timetable)} timetable entries (Mon/Wed/Fri)...")

    data = api_post("LMS Batch", {
        "doctype": "LMS Batch",
        "title": "NOSS Level 3 — April 2026 Intake",
        "start_date": "2026-04-21",
        "end_date": "2026-07-31",
        "start_time": "09:00:00",
        "end_time": "12:00:00",
        "timezone": "Asia/Kuala_Lumpur",
        "medium": "Offline",
        "description": "April 2026 intake for NOSS Level 3 subjects — Tuinalogy, Aesthetic, BEV, IT.",
        "batch_details": "This batch covers all 4 NOSS Level 3 subjects under JPK accreditation. Classes run Mon/Wed/Fri, 9am–12pm.",
        "published": 1,
        "allow_self_enrollment": 1,
        "seat_count": 30,
        "certification": 1,
        "instructors": [{"instructor": "Administrator"}],
        "courses": [{"course": c} for c in COURSES],
        "timetable": timetable,
    })
    print(f"  Created: {data.get('name')} with {len(timetable)} sessions")


# ── Step 4: Badges ───────────────────────────────────────────────────────────

BADGE_SVGS = {
    "badge-first-step.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="48" fill="#4CAF50" stroke="#2E7D32" stroke-width="3"/>
  <text x="50" y="62" font-size="40" text-anchor="middle" font-family="Arial">🎯</text>
  <text x="50" y="88" font-size="11" text-anchor="middle" fill="white" font-family="Arial" font-weight="bold">FIRST STEP</text>
</svg>""",
    "badge-quiz-champion.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="48" fill="#2196F3" stroke="#1565C0" stroke-width="3"/>
  <text x="50" y="62" font-size="40" text-anchor="middle" font-family="Arial">✅</text>
  <text x="50" y="85" font-size="9" text-anchor="middle" fill="white" font-family="Arial" font-weight="bold">QUIZ CHAMPION</text>
</svg>""",
    "badge-graduate.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="48" fill="#FF9800" stroke="#E65100" stroke-width="3"/>
  <text x="50" y="62" font-size="40" text-anchor="middle" font-family="Arial">🏆</text>
  <text x="50" y="88" font-size="11" text-anchor="middle" fill="white" font-family="Arial" font-weight="bold">GRADUATE</text>
</svg>""",
}

BADGE_DEFS = [
    {
        "title": "First Step",
        "description": "Awarded when you enrol in your first course. Every journey begins with a single step!",
        "svg_key": "badge-first-step.svg",
        "reference_doctype": "LMS Enrollment",
        "event": "New",
        "user_field": "member",
        "condition": "True",
        "grant_only_once": 1,
    },
    {
        "title": "Quiz Champion",
        "description": "Awarded when you pass a Knowledge Assessment quiz. Keep up the great work!",
        "svg_key": "badge-quiz-champion.svg",
        "reference_doctype": "LMS Quiz Submission",
        "event": "New",
        "user_field": "member",
        "condition": "doc.score >= doc.passing_percentage",
        "grant_only_once": 0,
    },
    {
        "title": "Graduate",
        "description": "Awarded upon successful completion of a NOSS Level 3 course. Congratulations!",
        "svg_key": "badge-graduate.svg",
        "reference_doctype": "LMS Enrollment",
        "event": "New",
        "user_field": "member",
        "condition": "True",
        "grant_only_once": 1,
    },
]


def setup_badges():
    print("\n[4] Creating badges...")

    # Upload SVG images
    url_map = {}
    for filename, svg in BADGE_SVGS.items():
        url = upload_svg(filename, svg)
        url_map[filename] = url

    # Check existing badges
    existing = session.get(f"{LMS_URL}/api/resource/LMS Badge",
                           params={"fields": '["title"]', "limit": 20})
    existing_titles = {b["title"] for b in existing.json().get("data", [])}

    for badge in BADGE_DEFS:
        if badge["title"] in existing_titles:
            print(f"  Badge '{badge['title']}' already exists — skipping.")
            continue
        payload = {
            "doctype": "LMS Badge",
            "enabled": 1,
            "title": badge["title"],
            "description": badge["description"],
            "image": url_map[badge["svg_key"]],
            "reference_doctype": badge["reference_doctype"],
            "event": badge["event"],
            "user_field": badge["user_field"],
            "condition": badge["condition"],
            "grant_only_once": badge["grant_only_once"],
        }
        data = api_post("LMS Badge", payload)
        print(f"  Created badge: {data.get('name')}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    login()
    setup_certificates()
    setup_programme()
    setup_batch()
    setup_badges()
    print("\nAll features set up. Run 'lms cache' to refresh.")


if __name__ == "__main__":
    main()
