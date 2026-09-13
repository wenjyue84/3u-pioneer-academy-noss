#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
Upload Tuinalogy images to Frappe LMS and rewrite lesson body references.
Usage: uv run scripts/lms_fix_images.py
"""

import re
import sys
from pathlib import Path
import requests

LMS_URL = "http://localhost:8001"
USERNAME = "Administrator"
PASSWORD = "admin"
ASSETS_DIR = Path(r"C:\Users\Jyue\Documents\1-projects\noss-to-wim\tuinalogy-services\_assets")

session = requests.Session()
session.headers.update({"Expect": ""})


def login():
    resp = session.post(f"{LMS_URL}/api/method/login", data={"usr": USERNAME, "pwd": PASSWORD})
    resp.raise_for_status()
    print("Logged in.")


def upload_image(filepath: Path) -> str:
    """Upload a file to Frappe, return the file_url."""
    with open(filepath, "rb") as f:
        resp = session.post(
            f"{LMS_URL}/api/method/upload_file",
            data={"is_private": 0, "folder": "Home/Attachments"},
            files={"file": (filepath.name, f, _mime(filepath))},
        )
    resp.raise_for_status()
    data = resp.json()
    url = data.get("message", {}).get("file_url") or data.get("message", {}).get("file_url")
    if not url:
        raise ValueError(f"No file_url in response: {data}")
    return url


def _mime(p: Path) -> str:
    ext = p.suffix.lower()
    return {"jpg": "image/jpeg", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
            ".png": "image/png", ".svg": "image/svg+xml"}.get(ext, "application/octet-stream")


def get_all_lessons():
    resp = session.get(
        f"{LMS_URL}/api/resource/Course Lesson",
        params={"fields": '["name","body"]', "limit": 500, "filters": '[["body","like","%../_assets/%"]]'},
    )
    resp.raise_for_status()
    return resp.json().get("data", [])


def patch_lesson(name: str, body: str):
    resp = session.put(
        f"{LMS_URL}/api/resource/Course Lesson/{name}",
        json={"body": body},
        headers={"Expect": ""},
    )
    resp.raise_for_status()


def main():
    login()

    # Step 1: Upload all images, build filename → url map
    url_map: dict[str, str] = {}
    image_files = [p for p in ASSETS_DIR.rglob("*") if p.is_file() and p.suffix.lower() in (".jpg", ".jpeg", ".png", ".svg")]
    print(f"\nUploading {len(image_files)} images...")
    for img in image_files:
        try:
            url = upload_image(img)
            url_map[img.name] = url
            print(f"  ✓ {img.name} → {url}")
        except Exception as e:
            print(f"  ✗ {img.name}: {e}", file=sys.stderr)

    if not url_map:
        print("No images uploaded. Exiting.")
        return

    # Step 2: Fetch and patch lessons with broken image refs
    lessons = get_all_lessons()
    print(f"\nFound {len(lessons)} lessons with relative image references.")

    patched = 0
    for lesson in lessons:
        name = lesson["name"]
        body = lesson.get("body") or ""
        new_body = body

        # Replace all ../_assets/{subdir}/{filename} occurrences
        def replace_ref(m):
            filename = Path(m.group(1)).name
            if filename in url_map:
                return f"({url_map[filename]})"
            print(f"  ! {filename} not in upload map, leaving as-is")
            return m.group(0)

        new_body = re.sub(r'\(\.\./\_assets/[^)]+/([^)]+)\)', replace_ref, new_body)

        if new_body != body:
            try:
                patch_lesson(name, new_body)
                print(f"  ✓ patched: {name}")
                patched += 1
            except Exception as e:
                print(f"  ✗ failed: {name}: {e}", file=sys.stderr)

    print(f"\nDone. {patched}/{len(lessons)} lessons patched.")


if __name__ == "__main__":
    main()
