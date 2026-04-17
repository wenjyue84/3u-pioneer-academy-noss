"""Consolidate all WIM markdown files across 4 subjects into a single .docx.

Produces one coloured, paginated document with:
- Cover page
- Table of Contents (Word field — right-click -> Update Field after opening)
- Per-subject and per-CU section headings
- Colour-coded doc-type headings (KP/KT/KK/PM/PA/KA)
- Page numbers in footer
- Preserves inline image references (images resolved relative to each source file)

Usage:
    uv run python build/wim_consolidate_all.py [--output out.docx] [--subject tuina|aesthetic|bev|it|all]
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(__file__).resolve().parent.parent

SUBJECTS = [
    {
        "key": "tuina",
        "dir": "tuinalogy-services",
        "title_en": "Tuinalogy Services (推拿疗法)",
        "title_bm": "Perkhidmatan Tuinalogi",
        "noss": "MP-031-3:2016",
        "level": "Level 3",
    },
    {
        "key": "aesthetic",
        "dir": "aesthetic-services",
        "title_en": "Aesthetic Services",
        "title_bm": "Perkhidmatan Estetik",
        "noss": "S960-002-3:2020",
        "level": "Level 3",
    },
    {
        "key": "bev",
        "dir": "bev-diagnostic-rectification",
        "title_en": "Battery Electric Vehicle Diagnostic & Rectification",
        "title_bm": "Diagnostik dan Pembaikan Kenderaan Elektrik Bateri",
        "noss": "G452-010-3:2023",
        "level": "Level 3",
    },
    {
        "key": "it",
        "dir": "it-computer-system",
        "title_en": "Computer System Management",
        "title_bm": "Pengurusan Sistem Komputer",
        "noss": "IT-020-3/4/5:2013",
        "level": "Levels 3, 4, 5",
    },
]

DOC_TYPE_COLORS = {
    "PM": RGBColor(0xB8, 0x86, 0x0B),  # Yellow-ish (dark goldenrod for readable heading)
    "KP": RGBColor(0x1F, 0x3A, 0x68),  # Dark blue (white paper -> readable text)
    "KT": RGBColor(0xC7, 0x15, 0x85),  # Pink/magenta
    "KK": RGBColor(0x0B, 0x5E, 0xA6),  # Blue
    "KA": RGBColor(0xC7, 0x15, 0x85),  # Pink
    "PA": RGBColor(0x1F, 0x7A, 0xAE),  # Light blue
}

DOC_TYPE_LABELS = {
    "PM": "Lesson Plan",
    "KP": "Information Sheet",
    "KT": "Assignment Sheet",
    "KK": "Work Sheet",
    "KA": "Knowledge Assessment",
    "PA": "Performance Assessment",
}

# Doc-type ordering within each CU (teori + practical)
DOC_TYPE_ORDER = {
    "PM-teori": 0,
    "KP": 1,
    "KT": 2,
    "PM-amali": 3,
    "KK": 4,
    "KA": 5,
    "PA": 6,
}


def classify_doc(filename: str) -> tuple[str, int]:
    """Return (doc_type, seq_num)."""
    stem = Path(filename).stem
    if stem == "PM-teori":
        return ("PM-teori", 0)
    if stem == "PM-amali":
        return ("PM-amali", 0)
    if stem == "KA":
        return ("KA", 0)
    if stem == "PA":
        return ("PA", 0)
    m = re.match(r"^(KP|KT|KK)-(\d+)$", stem)
    if m:
        return (m.group(1), int(m.group(2)))
    return ("OTHER", 0)


def sort_key(md_path: Path) -> tuple:
    doc_type, seq = classify_doc(md_path.name)
    order = DOC_TYPE_ORDER.get(doc_type, 99)
    return (order, seq)


def collect_cus(subject_dir: Path) -> list[tuple[str, Path]]:
    """Return [(cu_label, cu_path)] sorted."""
    cus = []
    for child in sorted(subject_dir.iterdir()):
        if child.is_dir() and re.match(r"^(L\d+-)?[CE]\d+$", child.name):
            cus.append((child.name, child))
    # Also pick up it-computer-system/level-4 and level-5
    for child in sorted(subject_dir.iterdir()):
        if child.is_dir() and re.match(r"^level-[45]$", child.name):
            cus.append((child.name.upper(), child))
    return cus


def collect_md_files(cu_dir: Path) -> list[Path]:
    """Return sorted .md files within a CU directory (non-recursive)."""
    files = [p for p in cu_dir.iterdir()
             if p.is_file() and p.suffix == ".md" and not p.name.startswith("00-")]
    return sorted(files, key=sort_key)


def shift_headings(text: str, levels: int) -> str:
    """Push every markdown heading down by N levels."""
    prefix = "#" * levels

    def repl(m: re.Match) -> str:
        hashes = m.group(1)
        # Cap at 6 levels (Word doesn't handle deeper headings cleanly)
        new = (prefix + hashes)[:6]
        return f"{new} {m.group(2)}"

    return re.sub(r"^(#{1,6})\s+(.*)$", repl, text, flags=re.MULTILINE)


def resolve_image_paths(text: str, base_dir: Path) -> str:
    """Rewrite relative image paths to absolute (pandoc needs this when concatenating)."""
    def repl(m: re.Match) -> str:
        alt = m.group(1)
        path = m.group(2).strip()
        if path.startswith(("http://", "https://", "/")):
            return m.group(0)
        # Resolve relative to the markdown file's directory
        abs_path = (base_dir / path).resolve()
        if abs_path.exists():
            # Pandoc prefers forward slashes
            return f"![{alt}]({abs_path.as_posix()})"
        return m.group(0)

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl, text)


def build_master_markdown(subjects: list[dict], tmp_dir: Path) -> Path:
    """Concatenate all WIM .md files into a single master markdown."""
    master = tmp_dir / "master.md"
    parts: list[str] = []

    # Cover / title material is added to the docx in post-processing, so
    # master.md starts directly with subject sections.
    for subj in subjects:
        subj_dir = ROOT / subj["dir"]
        if not subj_dir.exists():
            continue

        # Subject title — H1 (top-level)
        parts.append(f"\n\n# {subj['title_en']} / {subj['title_bm']}\n")
        parts.append(f"\n**NOSS:** {subj['noss']} · **{subj['level']}**\n\n")

        cus = collect_cus(subj_dir)
        for cu_label, cu_path in cus:
            parts.append(f"\n\n## {cu_label} — Competency Unit\n\n")

            md_files = collect_md_files(cu_path)
            for md in md_files:
                doc_type, seq = classify_doc(md.name)
                label = DOC_TYPE_LABELS.get(doc_type, doc_type)
                seq_str = f" {seq}" if seq > 0 else ""
                parts.append(f"\n\n### [{cu_label}/{md.stem}] {label}{seq_str}\n\n")
                text = md.read_text(encoding="utf-8")
                # Strip the file's own top H1 (we replace with our own H3 above)
                text = re.sub(r"\A\s*#\s+[^\n]*\n", "", text)
                # Push remaining headings down so none clash with our H1/H2/H3 structure
                text = shift_headings(text, 3)
                # Resolve image paths so pandoc can embed them
                text = resolve_image_paths(text, md.parent)
                parts.append(text)
                parts.append("\n\n")

    master.write_text("".join(parts), encoding="utf-8")
    return master


def run_pandoc(master_md: Path, output_docx: Path) -> None:
    cmd = [
        "pandoc",
        str(master_md),
        "-o", str(output_docx),
        "--from", "markdown+raw_html+smart",
        "--to", "docx",
        "--toc",
        "--toc-depth=3",
        "--number-sections",
        "--wrap=none",
        "--resource-path", str(ROOT),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("pandoc stderr:", result.stderr, file=sys.stderr)
        raise SystemExit(1)


def add_page_numbers(doc: Document) -> None:
    """Add 'Page X of Y' in footer of every section."""
    for section in doc.sections:
        footer = section.footer
        para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para.text = ""  # clear

        run = para.add_run()
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

        def add_field(instr: str) -> None:
            fldChar_begin = OxmlElement("w:fldChar")
            fldChar_begin.set(qn("w:fldCharType"), "begin")
            instrText = OxmlElement("w:instrText")
            instrText.text = instr
            fldChar_end = OxmlElement("w:fldChar")
            fldChar_end.set(qn("w:fldCharType"), "end")
            run._r.append(fldChar_begin)
            run._r.append(instrText)
            run._r.append(fldChar_end)

        run.add_text("Page ")
        add_field("PAGE")
        run.add_text(" of ")
        add_field("NUMPAGES")


def insert_cover_page(doc: Document) -> None:
    """Insert a title/cover page before all existing content."""
    body = doc.element.body

    def mk_para(text: str, *, size_pt: int, bold: bool, color: RGBColor | None = None,
                align: int = WD_ALIGN_PARAGRAPH.CENTER, space_after_pt: int = 6) -> OxmlElement:
        p = OxmlElement("w:p")
        pPr = OxmlElement("w:pPr")
        jc = OxmlElement("w:jc")
        jc.set(qn("w:val"), "center" if align == WD_ALIGN_PARAGRAPH.CENTER else "left")
        pPr.append(jc)
        spacing = OxmlElement("w:spacing")
        spacing.set(qn("w:after"), str(space_after_pt * 20))
        pPr.append(spacing)
        p.append(pPr)

        r = OxmlElement("w:r")
        rPr = OxmlElement("w:rPr")
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), str(size_pt * 2))
        rPr.append(sz)
        if bold:
            b = OxmlElement("w:b")
            rPr.append(b)
        if color is not None:
            col = OxmlElement("w:color")
            col.set(qn("w:val"), f"{color[0]:02X}{color[1]:02X}{color[2]:02X}")
            rPr.append(col)
        r.append(rPr)
        t = OxmlElement("w:t")
        t.set(qn("xml:space"), "preserve")
        t.text = text
        r.append(t)
        p.append(r)
        return p

    def mk_blank(lines: int = 1) -> list[OxmlElement]:
        return [OxmlElement("w:p") for _ in range(lines)]

    def mk_page_break() -> OxmlElement:
        p = OxmlElement("w:p")
        r = OxmlElement("w:r")
        br = OxmlElement("w:br")
        br.set(qn("w:type"), "page")
        r.append(br)
        p.append(r)
        return p

    # Build cover in reverse so we can insert at index 0
    elements: list = []
    elements += mk_blank(4)
    elements.append(mk_para("WRITTEN INSTRUCTIONAL MATERIALS",
                            size_pt=14, bold=True,
                            color=RGBColor(0x55, 0x55, 0x55)))
    elements.append(mk_para("Bahan Pengajaran Bertulis (WIM)",
                            size_pt=12, bold=False,
                            color=RGBColor(0x77, 0x77, 0x77)))
    elements += mk_blank(2)
    elements.append(mk_para("Consolidated Edition",
                            size_pt=28, bold=True,
                            color=RGBColor(0x1F, 0x3A, 0x68)))
    elements += mk_blank(1)
    elements.append(mk_para("NOSS → WIM Conversion Project",
                            size_pt=16, bold=False,
                            color=RGBColor(0x33, 0x33, 0x33)))
    elements += mk_blank(3)
    elements.append(mk_para("Covers 4 subjects:",
                            size_pt=12, bold=True))
    for subj in SUBJECTS:
        elements.append(mk_para(f"• {subj['title_en']}  ({subj['noss']}, {subj['level']})",
                                size_pt=11, bold=False,
                                color=RGBColor(0x33, 0x33, 0x33)))
    elements += mk_blank(6)
    elements.append(mk_para("Generated: 2026-04-17", size_pt=10, bold=False,
                            color=RGBColor(0x77, 0x77, 0x77)))
    elements.append(mk_page_break())

    # Insert at the very beginning of body (index 0 onwards)
    for i, el in enumerate(elements):
        body.insert(i, el)


def colorize_headings(doc: Document) -> None:
    """Recolour H3 headings based on doc-type keyword in the heading text."""
    for para in doc.paragraphs:
        if para.style.name not in ("Heading 1", "Heading 2", "Heading 3"):
            continue
        text = para.text

        # Match [CU/DocCode] pattern, e.g. [C01/KP-01]
        m = re.search(r"\[(?:L\d+-)?[CE]\d+/(PM-teori|PM-amali|KP|KT|KK|KA|PA)", text)
        if m:
            dt = m.group(1)
            dt_key = "PM" if dt.startswith("PM") else dt
            color = DOC_TYPE_COLORS.get(dt_key)
            if color:
                for run in para.runs:
                    run.font.color.rgb = color
                    run.font.bold = True
            continue

        # Subject H1 gets a distinct colour
        if para.style.name == "Heading 1":
            for run in para.runs:
                run.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
                run.font.bold = True

        # CU H2 a slightly lighter colour
        elif para.style.name == "Heading 2":
            for run in para.runs:
                run.font.color.rgb = RGBColor(0x0B, 0x5E, 0xA6)
                run.font.bold = True


def set_margins(doc: Document) -> None:
    for section in doc.sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.2)
        section.right_margin = Cm(2.2)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default=None,
                        help="Output .docx path (default: ./build/WIM-Consolidated-All.docx)")
    parser.add_argument("--subject", choices=["tuina", "aesthetic", "bev", "it", "all"],
                        default="all",
                        help="Which subject(s) to include (default: all)")
    args = parser.parse_args()

    subjects = SUBJECTS if args.subject == "all" else [s for s in SUBJECTS if s["key"] == args.subject]

    output_path = Path(args.output) if args.output else (ROOT / "build" / "WIM-Consolidated-All.docx")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        print(f"[1/4] Concatenating markdown for {len(subjects)} subject(s)...")
        master_md = build_master_markdown(subjects, tmp)
        size_kb = master_md.stat().st_size // 1024
        print(f"      master.md = {size_kb} KB")

        print(f"[2/4] Running pandoc -> {output_path.name} ...")
        run_pandoc(master_md, output_path)

    print("[3/4] Post-processing (cover page, page numbers, colours)...")
    doc = Document(str(output_path))
    insert_cover_page(doc)
    colorize_headings(doc)
    add_page_numbers(doc)
    set_margins(doc)
    doc.save(str(output_path))

    print(f"[4/4] Done -> {output_path}")
    print(f"      {output_path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
