#!/usr/bin/env python3
"""Extract the JPK government logo from a reference WIM PDF cover.

Usage:
    uv run --with pymupdf python extract_logo.py <subject_key>

Reads data/subjects.json, looks up the subject root, and extracts the first
reasonable-sized image from `raw/folder-1-wim-panduan/C01/0. COVER.pdf` to
`<subject_root>/_assets/logos/jpk-logo.png`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import fitz  # PyMuPDF

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
PROJECT_ROOT = SKILL_DIR.parent.parent.parent  # .claude/skills/wim-jpk-format/scripts -> project

COVER_PDF = PROJECT_ROOT / "raw" / "folder-1-wim-panduan" / "C01" / "0. COVER.pdf"


def extract_logo(dest: Path) -> int:
    if not COVER_PDF.exists():
        raise FileNotFoundError(f"Cover PDF not found: {COVER_PDF}")
    doc = fitz.open(str(COVER_PDF))
    best_bytes: bytes | None = None
    best_area = 0
    for page in doc:
        for img in page.get_images(full=True):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            area = pix.width * pix.height
            if pix.width >= 80 and pix.height >= 80 and area > best_area:
                if pix.n > 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                best_bytes = pix.tobytes("png")
                best_area = area
            pix = None
    doc.close()
    if best_bytes is None:
        raise RuntimeError("No suitable logo image found in cover PDF")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(best_bytes)
    return len(best_bytes)


def main() -> None:
    data_path = SKILL_DIR / "data" / "subjects.json"
    subjects = json.loads(data_path.read_text(encoding="utf-8"))
    keys = sys.argv[1:] or ["tuinalogy", "aesthetic", "bev", "it"]
    if keys == ["all"]:
        keys = ["tuinalogy", "aesthetic", "bev", "it"]
    for key in keys:
        meta = subjects[key]
        dest = PROJECT_ROOT / meta["root"] / "_assets" / "logos" / "jpk-logo.png"
        size = extract_logo(dest)
        print(f"[{key}] wrote {dest.relative_to(PROJECT_ROOT)} ({size} bytes)")
        attr = dest.parent / "ATTRIBUTION.md"
        attr.write_text(
            "# JPK Logo Attribution\n\n"
            "Source: JPK (Jabatan Pembangunan Kemahiran) public WIM sample — "
            "`raw/folder-1-wim-panduan/C01/0. COVER.pdf`.\n\n"
            "This is a Malaysian government crest used on official Written Instructional "
            "Materials. Used here for internal WIM training material compliance. "
            "No copyright claim.\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
