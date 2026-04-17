"""Convert raw/folder-2-sample-wim/C01 PDFs to markdown with meaningful filenames.

Teacher-friendly names: `<seq>-<role>-<topic>.md`
  role    = cover | toc | committee | cpc | cocu | jpw | schedule | lesson-plan
            | info-sheet | assignment | work-sheet
  topic   = slugified English gist of the WIM topic (for KP/KT/KK only)

Source: FB-025-4:2012 Administrative Management Level 4, CU C01.
"""
from __future__ import annotations

import re
from pathlib import Path

from markitdown import MarkItDown

SRC = Path("raw/folder-2-sample-wim/C01")
DST = Path("raw/md/folder-2-sample-wim/C01")

# Explicit map: source pdf filename -> output md filename.
# Based on TAJUK (topic) extracted from each PDF + role inferred from filename.
FILE_MAP: dict[str, str] = {
    "0.COVER C01.pdf":                                 "00-cover.md",
    "0. ISI KANDUNGAN WIM C01.pdf":                     "00-table-of-contents.md",
    "1. AHLI JAWATANKUASA PEMBANGUNAN.pdf":             "01-development-committee.md",
    "2.CPC.pdf":                                        "02-competency-profile-chart.md",
    "3.Cocu.pdf":                                       "03-curriculum-of-competency-unit.md",
    "4. JPW  C01.pdf":                                  "04-jpw-weighting-determination.md",
    "5. JADUAL PENETAPAN PERATUSAN MASA AKTIVITI PEMBELAJARAN DAN PENILAIAN C01.pdf":
        "05-learning-assessment-time-percentage.md",
    "6. JADUAL PEMBAHAGIAN MASA PEMBELAJARAN BERSEMUKA C01.pdf":
        "06-face-to-face-learning-time-division.md",

    # Topic 1: Pembangunan Latihan Kakitangan = Staff Training Development
    "7.FB-025-42012-C01 KP (1-3) PM(KUNING).pdf":       "07-lesson-plan-kp1-staff-training-development.md",
    "8.FB-025-42012-C01 KP (1-3)(PUTIH).pdf":           "08-info-sheet-kp1-staff-training-development.md",
    "9.FB-025-42012-C01 KT (1-3)PINK.pdf":              "09-assignment-kt1-staff-training-development.md",
    "10.FB-025-42012-C01 KK(1-3)PM(KUNING).pdf":        "10-lesson-plan-kk1-handle-staff-training.md",
    "11.FB-025-42012-C01 KK(1-3)(BIRU).pdf":            "11-work-sheet-kk1-handle-staff-training.md",

    # Topic 2: Pengendalian Motivasi Kakitangan = Staff Motivation Handling
    "12.FB-025-42012-C01 KP (2-3) PM(KUNING).pdf":      "12-lesson-plan-kp2-staff-motivation-handling.md",
    "13.FB-025-42012-C01 KP (2-3)(PUTIH).pdf":          "13-info-sheet-kp2-staff-motivation-handling.md",
    "14.FB-025-42012-C01 KT (2-3)PINK.pdf":             "14-assignment-kt2-staff-motivation-handling.md",
    "15.FB-025-42012-C01 KK(2-3)PM(KUNING).pdf":        "15-lesson-plan-kk2-handle-motivation-session.md",
    "16.FB-025-42012-C01 KK(2-3)(BIRU).pdf":            "16-work-sheet-kk2-handle-motivation-session.md",

    # Topic 3: Penilaian Pembangunan Kakitangan = Staff Development Evaluation
    "17.FB-025-42012-C01 KP (3-3) PM(KUNING).pdf":      "17-lesson-plan-kp3-staff-development-evaluation.md",
    "18.FB-025-42012-C01 KP (3-3)(PUTIH).pdf":          "18-info-sheet-kp3-staff-development-evaluation.md",
    "19.FB-025-42012-C01 KT (3-3)PINK.pdf":             "19-assignment-kt3-staff-development-evaluation.md",
    "20. FB-025-42012-C01 KK(3-3)PM(KUNING).pdf":       "20-lesson-plan-kk3-handle-succession-plan.md",
    "21. FB-025-42012-C01 KK(3-3)(BIRU).pdf":           "21-work-sheet-kk3-handle-succession-plan.md",
}


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    md = MarkItDown()

    # Sanity check: every source pdf in SRC is in the map
    src_pdfs = {p.name for p in SRC.glob("*.pdf")}
    mapped = set(FILE_MAP.keys())
    missing = src_pdfs - mapped
    if missing:
        print("[WARN] unmapped pdfs:", sorted(missing))

    readme_lines: list[str] = [
        "# C01 Reference WIM - Administrative Staff Development Management",
        "",
        "**Source:** FB-025-4:2012 Administrative Management Level 4, CU C01",
        "**Purpose:** Teacher reference for WIM structure / formatting. Filenames renamed "
        "from the original JPK numbering (e.g. `7.FB-025-42012-C01 KP (1-3) PM(KUNING).pdf`) "
        "to descriptive English names so the topic is obvious at a glance.",
        "",
        "## Topics in this CU",
        "",
        "1. **Staff Training Development** (Pembangunan Latihan Kakitangan)",
        "2. **Staff Motivation Handling** (Pengendalian Motivasi Kakitangan)",
        "3. **Staff Development Evaluation** (Penilaian Pembangunan Kakitangan)",
        "",
        "## File index",
        "",
        "| File | Role | Source PDF |",
        "| --- | --- | --- |",
    ]

    for src_name, dst_name in FILE_MAP.items():
        src_path = SRC / src_name
        dst_path = DST / dst_name
        if not src_path.exists():
            print(f"[SKIP] missing: {src_name}")
            continue
        try:
            result = md.convert(str(src_path))
            text = result.text_content
        except Exception as e:
            print(f"[ERR] {src_name}: {e}")
            continue

        role = _classify_role(dst_name)
        header = (
            f"---\n"
            f"source_pdf: {src_name}\n"
            f"role: {role}\n"
            f"noss: FB-025-4:2012\n"
            f"cu: C01\n"
            f"cu_title: ADMINISTRATIVE STAFF DEVELOPMENT MANAGEMENT\n"
            f"---\n\n"
        )
        dst_path.write_text(header + text, encoding="utf-8")
        readme_lines.append(f"| `{dst_name}` | {role} | `{src_name}` |")
        print(f"[OK] {src_name} -> {dst_name}")

    readme_lines.append("")
    (DST / "00-README.md").write_text("\n".join(readme_lines), encoding="utf-8")
    print(f"\n[DONE] {len(FILE_MAP)} files -> {DST}")


def _classify_role(dst_name: str) -> str:
    if "lesson-plan" in dst_name: return "lesson-plan (PM, yellow)"
    if "info-sheet" in dst_name:  return "info-sheet (KP, white)"
    if "assignment" in dst_name:  return "assignment (KT, pink)"
    if "work-sheet" in dst_name:  return "work-sheet (KK, blue)"
    if "cover" in dst_name:       return "cover"
    if "contents" in dst_name:    return "table-of-contents"
    if "committee" in dst_name:   return "development-committee"
    if "cpc" in dst_name:         return "competency-profile-chart"
    if "curriculum" in dst_name:  return "cocu (curriculum)"
    if "jpw" in dst_name:         return "jpw (weighting)"
    if "percentage" in dst_name:  return "time-percentage-schedule"
    if "face-to-face" in dst_name:return "time-division-schedule"
    return "other"


if __name__ == "__main__":
    main()
