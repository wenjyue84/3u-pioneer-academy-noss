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
REFERENCE_DOC = ROOT / "build" / "_templates" / "reference-textbook.docx"
LUA_FILTER = ROOT / "build" / "filters" / "callouts.lua"
LOGO_PATH = ROOT / "tuinalogy-services" / "_assets" / "logos" / "jpk-logo.png"

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
    """Return (doc_type, seq_num).

    Accepts both bare codes (e.g. `KA.md`, `PM-teori.md`, `KP-01.md`) and
    descriptive variants (e.g. `KA-centre-management.md`, `PM-teori-sports-tuina.md`,
    `KP-01-eight-core-techniques.md`). The optional suffix is ignored for classification.
    """
    stem = Path(filename).stem
    if stem == "PM-teori" or stem.startswith("PM-teori-"):
        return ("PM-teori", 0)
    if stem == "PM-amali" or stem.startswith("PM-amali-"):
        return ("PM-amali", 0)
    if stem == "KA" or stem.startswith("KA-"):
        return ("KA", 0)
    if stem == "PA" or stem.startswith("PA-"):
        return ("PA", 0)
    m = re.match(r"^(KP|KT|KK)-(\d+)(?:-|$)", stem)
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
    """Rewrite relative image paths to absolute (pandoc needs this when concatenating).

    Handles both markdown syntax `![alt](path)` and HTML `<img src="path">`
    (the JPK envelope uses HTML tables with embedded `<img>` for the logo)."""
    def resolve(path: str) -> str | None:
        path = path.strip()
        if path.startswith(("http://", "https://", "/")):
            return None
        abs_path = (base_dir / path).resolve()
        if abs_path.exists():
            return abs_path.as_posix()
        return None

    def repl_md(m: re.Match) -> str:
        alt = m.group(1)
        resolved = resolve(m.group(2))
        return f"![{alt}]({resolved})" if resolved else m.group(0)

    def repl_html(m: re.Match) -> str:
        before, open_q, path, close_q = m.group(1), m.group(2), m.group(3), m.group(4)
        resolved = resolve(path)
        if not resolved:
            return m.group(0)
        return f"{before}{open_q}{resolved}{close_q}"

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl_md, text)
    # HTML <img src="..."> or <img src='...'>
    text = re.sub(r"(<img\b[^>]*?\bsrc=)(['\"])([^'\"]+)(['\"])",
                  repl_html, text, flags=re.IGNORECASE)
    return text


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
        "--from", "markdown+raw_html+smart+fenced_divs",
        "--to", "docx",
        "--number-sections",
        "--wrap=none",
        "--resource-path", str(ROOT),
    ]
    if REFERENCE_DOC.exists():
        cmd += ["--reference-doc", str(REFERENCE_DOC)]
    if LUA_FILTER.exists():
        cmd += ["--lua-filter", str(LUA_FILTER)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("pandoc stderr:", result.stderr, file=sys.stderr)
        raise SystemExit(1)


def _is_jpk_envelope_table(tbl) -> bool:
    """Detect the JPK envelope table so we do not restyle it."""
    try:
        first_cell_xml = tbl._tbl.xml[:4000]
    except Exception:
        return False
    needles = (
        "JABATAN PEMBANGUNAN KEMAHIRAN",
        "PUSAT PENTADBIRAN KERAJAAN",
        "jpk-logo.png",
    )
    return any(n in first_cell_xml for n in needles)


def apply_table_style(doc: Document) -> None:
    """Apply a textbook look to body tables: header shading, repeating header,
    thin horizontal rules only, banded rows.  Skips the JPK envelope table."""
    HEADER_FILL = "E7E6E6"
    BAND_FILL = "F7F7F7"
    RULE_COLOR = "7F7F7F"

    for tbl in doc.tables:
        if _is_jpk_envelope_table(tbl):
            continue

        tbl_elem = tbl._tbl
        # Clear any existing tblBorders / tblPr borders
        tblPr = tbl_elem.find(qn("w:tblPr"))
        if tblPr is None:
            tblPr = OxmlElement("w:tblPr")
            tbl_elem.insert(0, tblPr)
        existing = tblPr.find(qn("w:tblBorders"))
        if existing is not None:
            tblPr.remove(existing)
        borders = OxmlElement("w:tblBorders")
        for side in ("top", "bottom", "insideH"):
            b = OxmlElement(f"w:{side}")
            b.set(qn("w:val"), "single")
            b.set(qn("w:sz"), "6" if side == "insideH" else "12")
            b.set(qn("w:color"), RULE_COLOR)
            borders.append(b)
        for side in ("left", "right", "insideV"):
            b = OxmlElement(f"w:{side}")
            b.set(qn("w:val"), "nil")
            borders.append(b)
        tblPr.append(borders)

        # Shade + bold header row; mark it as repeating
        if tbl.rows:
            hdr_row = tbl.rows[0]
            trPr = hdr_row._tr.find(qn("w:trPr"))
            if trPr is None:
                trPr = OxmlElement("w:trPr")
                hdr_row._tr.insert(0, trPr)
            if trPr.find(qn("w:tblHeader")) is None:
                trPr.append(OxmlElement("w:tblHeader"))
            for cell in hdr_row.cells:
                tcPr = cell._tc.get_or_add_tcPr()
                shd = tcPr.find(qn("w:shd"))
                if shd is None:
                    shd = OxmlElement("w:shd")
                    tcPr.append(shd)
                shd.set(qn("w:val"), "clear")
                shd.set(qn("w:color"), "auto")
                shd.set(qn("w:fill"), HEADER_FILL)
                for para in cell.paragraphs:
                    for run in para.runs:
                        run.bold = True

        # Band alternate body rows
        for i, row in enumerate(tbl.rows[1:], start=1):
            if i % 2 == 0:
                for cell in row.cells:
                    tcPr = cell._tc.get_or_add_tcPr()
                    if tcPr.find(qn("w:shd")) is None:
                        shd = OxmlElement("w:shd")
                        shd.set(qn("w:val"), "clear")
                        shd.set(qn("w:color"), "auto")
                        shd.set(qn("w:fill"), BAND_FILL)
                        tcPr.append(shd)


def promote_italic_captions(doc: Document) -> None:
    """Restyle italic-only paragraphs whose text starts with a figure/table
    marker (e.g. '图 C01-1-1:' or '*Figure 3.2:*' / 'Table 1 ...') to the
    Caption style so that number_figure_captions() can SEQ-number them."""
    prefixes = ("图 ", "图：", "表 ", "表：",
                "figure ", "fig. ", "fig.", "table ")
    for para in doc.paragraphs:
        if para.style.name in ("Caption", "Image Caption"):
            continue
        txt = para.text.strip()
        if not txt:
            continue
        low = txt.lower()
        if not (any(low.startswith(p) for p in prefixes) or
                txt.startswith("图") or txt.startswith("表")):
            continue
        # Require every non-empty run be italic (heuristic for caption line)
        runs = [r for r in para.runs if (r.text or "").strip()]
        if not runs:
            continue
        if not all(r.italic for r in runs):
            continue
        try:
            para.style = doc.styles["Caption"]
        except KeyError:
            pass


_SYNTHETIC_HEADINGS_LOWER = {
    "contents", "table of contents", "list of figures", "list of tables",
    LBL_CONTENTS.lower(), LBL_LIST_FIGURES.lower(), LBL_LIST_TABLES.lower(),
    "目录", "插图目录", "表格目录",
} if False else set()  # populated at import time via _init_synthetic


def _init_synthetic():
    """Populate the synthetic-heading allow-list after module constants exist."""
    global _SYNTHETIC_HEADINGS_LOWER
    _SYNTHETIC_HEADINGS_LOWER = {
        "contents", "table of contents", "list of figures", "list of tables",
        LBL_CONTENTS.lower(), LBL_LIST_FIGURES.lower(), LBL_LIST_TABLES.lower(),
        "目录", "插图目录", "表格目录",
    }


def _is_real_subject_h1(para) -> bool:
    """True if this Heading-1 paragraph names a subject chapter (not Contents /
    List of Figures / List of Tables)."""
    if not _SYNTHETIC_HEADINGS_LOWER:
        _init_synthetic()
    if para.style.name != "Heading 1":
        return False
    txt = para.text.strip().lower()
    return txt not in _SYNTHETIC_HEADINGS_LOWER


# Global caption registry populated by number_figure_captions(); consumed by
# build_lof_lot_static().  Shape: list[dict(kind, label, text, bookmark)].
_CAPTIONS: list[dict] = []


def number_figure_captions(doc: Document) -> None:
    """Rewrite Caption paragraphs with literal 'Figure N.M' / 'Table N.M' text
    and wrap each caption in a bookmark so LOF/LOT + TOC can link to it.

    No SEQ fields are emitted — everything is static text so WPS Office,
    LibreOffice, and Word all render identically on first open."""
    global _CAPTIONS
    _CAPTIONS = []
    caption_styles = {"Image Caption", "Caption"}
    chapter_idx = 0
    fig_in_ch = 0
    tbl_in_ch = 0
    bm_id = 9000  # start above likely pandoc-generated bookmark ids

    for para in doc.paragraphs:
        if _is_real_subject_h1(para):
            chapter_idx += 1
            fig_in_ch = 0
            tbl_in_ch = 0
            continue

        if para.style.name not in caption_styles:
            continue
        text = para.text.strip()
        if not text:
            continue

        lower = text.lower()
        is_table = lower.startswith("table") or text.startswith("表")
        is_fig = (lower.startswith("figure") or text.startswith("图") or
                  lower.startswith("fig."))
        if not (is_fig or is_table):
            is_fig = True  # default for captions under images

        if is_table:
            tbl_in_ch += 1
            kind = "Table"
            number = f"{max(chapter_idx, 1)}.{tbl_in_ch}"
            bi_en, bi_cn = LBL_TABLE_BI
        else:
            fig_in_ch += 1
            kind = "Figure"
            number = f"{max(chapter_idx, 1)}.{fig_in_ch}"
            bi_en, bi_cn = LBL_FIGURE_BI

        # Strip any pre-existing "Figure:" / "图" label
        stripped = text
        for token in ("Figure:", "Fig.", "Figure", "图", "Table:", "Table", "表"):
            if stripped.startswith(token):
                stripped = stripped[len(token):].lstrip(" :：-")
                break

        label = f"{bi_en} {number}  ·  {bi_cn} {number}"
        bookmark = f"_caption_{bm_id}"
        bm_id += 1

        p = para._p
        for r in list(p.findall(qn("w:r"))):
            p.remove(r)

        # Bookmark start wrapping the whole caption
        bm_start = OxmlElement("w:bookmarkStart")
        bm_start.set(qn("w:id"), str(bm_id))
        bm_start.set(qn("w:name"), bookmark)
        p.append(bm_start)

        def _add_text_run(txt: str, italic: bool = False, bold: bool = False):
            r = OxmlElement("w:r")
            rPr = OxmlElement("w:rPr")
            if italic:
                rPr.append(OxmlElement("w:i"))
            if bold:
                rPr.append(OxmlElement("w:b"))
            r.append(rPr)
            t = OxmlElement("w:t")
            t.set(qn("xml:space"), "preserve")
            t.text = txt
            r.append(t)
            p.append(r)

        _add_text_run(f"{label}  ", bold=True)
        _add_text_run(stripped, italic=True)

        bm_end = OxmlElement("w:bookmarkEnd")
        bm_end.set(qn("w:id"), str(bm_id))
        p.append(bm_end)
        bm_id += 1

        _CAPTIONS.append({
            "kind": kind,
            "label": label,
            "text": stripped,
            "bookmark": bookmark,
        })


def add_drop_caps(doc: Document) -> None:
    """Add a 3-line drop cap to the first body paragraph after each Heading 1."""
    body = doc.element.body
    paragraphs = [p for p in body.iterchildren(qn("w:p"))]
    i = 0
    while i < len(paragraphs):
        p = paragraphs[i]
        pPr = p.find(qn("w:pPr"))
        if pPr is not None:
            pStyle = pPr.find(qn("w:pStyle"))
            if pStyle is not None and pStyle.get(qn("w:val")) == "Heading1":
                # Find next normal-body paragraph that has text
                for j in range(i + 1, min(i + 8, len(paragraphs))):
                    q = paragraphs[j]
                    # Skip nested headings / empty paras
                    q_pPr = q.find(qn("w:pPr"))
                    q_style = None
                    if q_pPr is not None:
                        qs = q_pPr.find(qn("w:pStyle"))
                        if qs is not None:
                            q_style = qs.get(qn("w:val"))
                    if q_style and q_style.startswith("Heading"):
                        continue
                    # Must contain a non-empty text run
                    texts = [t.text or "" for t in q.iter(qn("w:t"))]
                    if not any(tt.strip() for tt in texts):
                        continue
                    # Split the first character of the first run into its own run,
                    # then mark the paragraph with framePr dropCap drop lines=3.
                    first_run = q.find(qn("w:r"))
                    if first_run is None:
                        break
                    first_text = first_run.find(qn("w:t"))
                    if first_text is None or not (first_text.text and first_text.text.strip()):
                        break
                    original = first_text.text
                    # Pick the first non-whitespace character
                    stripped = original.lstrip()
                    if not stripped:
                        break
                    first_char = stripped[0]
                    rest = original[len(original) - len(stripped) + 1:]
                    first_text.text = rest

                    # Build the drop-cap paragraph immediately before q
                    dc_p = OxmlElement("w:p")
                    dc_pPr = OxmlElement("w:pPr")
                    framePr = OxmlElement("w:framePr")
                    framePr.set(qn("w:dropCap"), "drop")
                    framePr.set(qn("w:lines"), "3")
                    framePr.set(qn("w:wrap"), "around")
                    framePr.set(qn("w:vAnchor"), "text")
                    framePr.set(qn("w:hAnchor"), "text")
                    dc_pPr.append(framePr)
                    spacing = OxmlElement("w:spacing")
                    spacing.set(qn("w:line"), "900")
                    spacing.set(qn("w:lineRule"), "exact")
                    dc_pPr.append(spacing)
                    dc_p.append(dc_pPr)
                    dc_r = OxmlElement("w:r")
                    dc_rPr = OxmlElement("w:rPr")
                    rFonts = OxmlElement("w:rFonts")
                    rFonts.set(qn("w:ascii"), "Source Sans 3")
                    rFonts.set(qn("w:hAnsi"), "Source Sans 3")
                    rFonts.set(qn("w:eastAsia"), "Source Han Serif SC")
                    dc_rPr.append(rFonts)
                    sz = OxmlElement("w:sz")
                    sz.set(qn("w:val"), "140")  # 70 pt
                    dc_rPr.append(sz)
                    color = OxmlElement("w:color")
                    color.set(qn("w:val"), "1F3864")
                    dc_rPr.append(color)
                    b = OxmlElement("w:b")
                    dc_rPr.append(b)
                    dc_r.append(dc_rPr)
                    dc_t = OxmlElement("w:t")
                    dc_t.text = first_char
                    dc_r.append(dc_t)
                    dc_p.append(dc_r)
                    q.addprevious(dc_p)
                    break
        i += 1


# Bilingual labels: always EN + 中文 side-by-side
LBL_CONTENTS       = "Contents  ·  目录"
LBL_LIST_FIGURES   = "List of Figures  ·  插图目录"
LBL_LIST_TABLES    = "List of Tables  ·  表格目录"
LBL_FIGURE_BI      = ("Figure", "图")
LBL_TABLE_BI       = ("Table", "表")
LBL_BOOK_HEADER    = "Written Instructional Materials  ·  书面教材  ·  Bahan Pengajaran Bertulis"


def _mk_heading_para(text: str, style: str = "TOCHeading"):
    p = OxmlElement("w:p")
    pPr = OxmlElement("w:pPr")
    pStyle = OxmlElement("w:pStyle")
    pStyle.set(qn("w:val"), style)
    pPr.append(pStyle)
    p.append(pPr)
    r = OxmlElement("w:r")
    t = OxmlElement("w:t")
    t.text = text
    r.append(t)
    p.append(r)
    return p


def _mk_link_para(pstyle: str, bookmark: str, label: str, text: str):
    """A TOC/LOF entry: internal hyperlink to bookmark, no page number."""
    p = OxmlElement("w:p")
    pPr = OxmlElement("w:pPr")
    pStyle = OxmlElement("w:pStyle")
    pStyle.set(qn("w:val"), pstyle)
    pPr.append(pStyle)
    p.append(pPr)

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("w:anchor"), bookmark)
    hyperlink.set(qn("w:history"), "1")

    def _run(txt: str, bold: bool = False):
        r = OxmlElement("w:r")
        rPr = OxmlElement("w:rPr")
        rStyle = OxmlElement("w:rStyle")
        rStyle.set(qn("w:val"), "Hyperlink")
        rPr.append(rStyle)
        if bold:
            rPr.append(OxmlElement("w:b"))
        r.append(rPr)
        t = OxmlElement("w:t")
        t.set(qn("xml:space"), "preserve")
        t.text = txt
        r.append(t)
        return r

    if label:
        hyperlink.append(_run(f"{label}  ", bold=True))
    hyperlink.append(_run(text))
    p.append(hyperlink)
    return p


def insert_list_of_figures_tables(doc: Document) -> None:
    """Build List of Figures + List of Tables from _CAPTIONS as literal text.

    Relies on number_figure_captions() having already populated _CAPTIONS and
    inserted bookmarks.  Inserted immediately after the static TOC.
    """
    body = doc.element.body
    # Find the "Contents" heading that build_static_toc() inserted; append after
    # the last TOC entry (which is the last child of a consecutive TOC1-3 run
    # that follows the "Contents" heading).  Simpler: append at the anchor
    # tracked by build_static_toc() via a sentinel comment.  We look for the
    # last paragraph with pStyle starting with "TOC" before any Heading 1.
    toc_anchor = None
    for p in body.iterchildren(qn("w:p")):
        pPr = p.find(qn("w:pPr"))
        if pPr is None:
            continue
        pStyle = pPr.find(qn("w:pStyle"))
        if pStyle is None:
            continue
        val = pStyle.get(qn("w:val")) or ""
        if val in ("Heading1",) and _is_real_subject_h1_element(p):
            break
        if val.startswith("TOC") or val == "TOCHeading":
            toc_anchor = p
    if toc_anchor is None:
        # No TOC to hook onto — bail out quietly
        return
    if not _CAPTIONS:
        return

    figures = [c for c in _CAPTIONS if c["kind"] == "Figure"]
    tables = [c for c in _CAPTIONS if c["kind"] == "Table"]

    new_nodes = []
    if figures:
        new_nodes.append(_mk_heading_para(LBL_LIST_FIGURES, style="TOCHeading"))
        for cap in figures:
            new_nodes.append(_mk_link_para("TOC1", cap["bookmark"],
                                           cap["label"], cap["text"]))
    if tables:
        new_nodes.append(_mk_heading_para(LBL_LIST_TABLES, style="TOCHeading"))
        for cap in tables:
            new_nodes.append(_mk_link_para("TOC1", cap["bookmark"],
                                           cap["label"], cap["text"]))

    anchor = toc_anchor
    for node in new_nodes:
        anchor.addnext(node)
        anchor = node


def _is_real_subject_h1_element(p) -> bool:
    """Element-level variant of _is_real_subject_h1 (takes raw <w:p>)."""
    if not _SYNTHETIC_HEADINGS_LOWER:
        _init_synthetic()
    pPr = p.find(qn("w:pPr"))
    if pPr is None:
        return False
    pStyle = pPr.find(qn("w:pStyle"))
    if pStyle is None or pStyle.get(qn("w:val")) != "Heading1":
        return False
    txt = "".join(t.text or "" for t in p.iter(qn("w:t"))).strip().lower()
    return txt not in _SYNTHETIC_HEADINGS_LOWER


def build_static_toc(doc: Document) -> None:
    """Generate a static main TOC at the top of the document body: 'Contents'
    heading + one hyperlinked line per H1/H2/H3.  Bookmarks are added to each
    target heading so the hyperlinks resolve on open in WPS/LibreOffice/Word."""
    body = doc.element.body

    # Collect headings, assigning a bookmark to each.
    bm_id = 8000
    entries = []  # list of (level, text, bookmark)
    for p in body.iterchildren(qn("w:p")):
        pPr = p.find(qn("w:pPr"))
        if pPr is None:
            continue
        pStyle = pPr.find(qn("w:pStyle"))
        if pStyle is None:
            continue
        val = pStyle.get(qn("w:val"))
        lvl_map = {"Heading1": 1, "Heading2": 2, "Heading3": 3}
        level = lvl_map.get(val)
        if level is None:
            continue
        text = "".join(t.text or "" for t in p.iter(qn("w:t"))).strip()
        if not text:
            continue
        # Skip the synthetic TOC/LOF/LOT headings we inject
        if text.lower() in ("contents", "list of figures", "list of tables"):
            continue
        if text in (LBL_CONTENTS, LBL_LIST_FIGURES, LBL_LIST_TABLES):
            continue
        bookmark = f"_Toc_{bm_id}"
        # Insert bookmark around the heading content
        bm_start = OxmlElement("w:bookmarkStart")
        bm_start.set(qn("w:id"), str(bm_id))
        bm_start.set(qn("w:name"), bookmark)
        bm_end = OxmlElement("w:bookmarkEnd")
        bm_end.set(qn("w:id"), str(bm_id))
        # Put start right after pPr, end at end of paragraph
        pPr.addnext(bm_start)
        p.append(bm_end)
        bm_id += 1
        entries.append((level, text, bookmark))

    if not entries:
        return

    # Find where to insert the TOC: right before the first real subject H1.
    anchor = None
    for p in body.iterchildren(qn("w:p")):
        if _is_real_subject_h1_element(p):
            anchor = p
            break
    if anchor is None:
        # Insert at very top
        first = next(body.iterchildren(qn("w:p")), None)
        anchor = first

    # Build nodes: "Contents" heading + TOC1/TOC2/TOC3 hyperlinked entries
    toc_heading = _mk_heading_para(LBL_CONTENTS, style="TOCHeading")
    toc_nodes = [toc_heading]
    for level, text, bookmark in entries:
        toc_nodes.append(_mk_link_para(f"TOC{level}", bookmark, "", text))

    if anchor is None:
        for node in toc_nodes:
            body.append(node)
    else:
        for node in toc_nodes:
            anchor.addprevious(node)


def front_matter_roman_numerals(doc: Document) -> None:
    """Split the document into front matter (cover + TOC + LOF/LOT using
    lower-roman page numbers) and main matter (starting at Chapter 1 = first
    Heading 1 that is actually a subject) using Arabic numerals restarting
    at 1."""
    body = doc.element.body
    paragraphs = list(body.iterchildren(qn("w:p")))

    # Find the first real Heading 1 (subject) — skip "Contents", "List of Figures", etc.
    break_before = None
    for p in paragraphs:
        pPr = p.find(qn("w:pPr"))
        if pPr is None:
            continue
        pStyle = pPr.find(qn("w:pStyle"))
        if pStyle is None:
            continue
        if pStyle.get(qn("w:val")) != "Heading1":
            continue
        # Is it a "real" subject heading?  Check the visible text.
        txt = "".join(t.text or "" for t in p.iter(qn("w:t")))
        if txt.strip().lower() in ("contents", "table of contents",
                                   "list of figures", "list of tables"):
            continue
        break_before = p
        break
    if break_before is None:
        return

    # Inject a section break BEFORE the first chapter.  We do this by inserting
    # a dummy paragraph whose pPr carries a <w:sectPr> — that terminates the
    # preceding (front matter) section.
    front_sect_p = OxmlElement("w:p")
    front_pPr = OxmlElement("w:pPr")
    front_sect_p.append(front_pPr)
    front_sectPr = OxmlElement("w:sectPr")
    pgNumType = OxmlElement("w:pgNumType")
    pgNumType.set(qn("w:fmt"), "lowerRoman")
    pgNumType.set(qn("w:start"), "1")
    front_sectPr.append(pgNumType)
    type_el = OxmlElement("w:type")
    type_el.set(qn("w:val"), "nextPage")
    front_sectPr.append(type_el)
    front_pPr.append(front_sectPr)
    break_before.addprevious(front_sect_p)

    # Now the final <w:sectPr> in body applies to the MAIN matter — set it to
    # Arabic starting at 1.
    final_sectPr = body.find(qn("w:sectPr"))
    if final_sectPr is not None:
        # Remove any existing pgNumType
        for existing in final_sectPr.findall(qn("w:pgNumType")):
            final_sectPr.remove(existing)
        main_pgNum = OxmlElement("w:pgNumType")
        main_pgNum.set(qn("w:fmt"), "decimal")
        main_pgNum.set(qn("w:start"), "1")
        final_sectPr.append(main_pgNum)


def add_running_header(doc: Document) -> None:
    """Stamp a literal running header into every section so WPS Office and
    LibreOffice display it correctly without needing to update any field.

    Uses a single book-level title string (no per-page chapter name) since
    STYLEREF would be required for per-page lookup and that is the very
    behaviour we are avoiding."""
    book_title = LBL_BOOK_HEADER
    for section in doc.sections:
        section.header_distance = Cm(1.2)
        section.footer_distance = Cm(1.2)
        header = section.header
        # Clear existing header content
        for para in list(header.paragraphs):
            para.clear()

        para = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = para.add_run(book_title)
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
        run.font.italic = True


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
    """Insert a JPK-style title/cover page before all existing content.

    Mirrors the sample WIM PDFs in raw/folder-2-sample-wim/: government logo
    at the top, bilingual (EN / 中文 / BM) institutional address, and a
    tri-lingual document identity block."""
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

    def mk_logo_para() -> OxmlElement | None:
        """Append a temporary paragraph at doc end, add picture, then detach
        its XML so we can insert at index 0."""
        if not LOGO_PATH.exists():
            return None
        try:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run()
            run.add_picture(str(LOGO_PATH), width=Cm(3.5))
            # Detach from body tail; caller re-inserts at top
            el = p._p
            el.getparent().remove(el)
            return el
        except Exception as exc:
            print(f"      [warn] could not embed logo {LOGO_PATH}: {exc}", file=sys.stderr)
            return None

    elements: list = []

    # Government logo (JPK crest)
    logo_el = mk_logo_para()
    if logo_el is not None:
        elements.append(logo_el)
        elements += mk_blank(1)

    # JPK institutional header (matches raw/folder-2-sample-wim/ PDFs)
    elements.append(mk_para("JABATAN PEMBANGUNAN KEMAHIRAN",
                            size_pt=13, bold=True,
                            color=RGBColor(0x1F, 0x3A, 0x68)))
    elements.append(mk_para("DEPARTMENT OF SKILLS DEVELOPMENT  ·  技能发展局",
                            size_pt=10, bold=False,
                            color=RGBColor(0x55, 0x55, 0x55)))
    elements.append(mk_para("KEMENTERIAN SUMBER MANUSIA",
                            size_pt=10, bold=False,
                            color=RGBColor(0x55, 0x55, 0x55)))
    elements.append(mk_para("MINISTRY OF HUMAN RESOURCES  ·  人力资源部",
                            size_pt=10, bold=False,
                            color=RGBColor(0x55, 0x55, 0x55)))
    elements.append(mk_para("ARAS 7-8, BLOK D4, KOMPLEKS D",
                            size_pt=9, bold=False,
                            color=RGBColor(0x77, 0x77, 0x77)))
    elements.append(mk_para("PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN",
                            size_pt=9, bold=False,
                            color=RGBColor(0x77, 0x77, 0x77)))
    elements.append(mk_para("62530 PUTRAJAYA, MALAYSIA",
                            size_pt=9, bold=False,
                            color=RGBColor(0x77, 0x77, 0x77)))
    elements += mk_blank(2)

    # Document identity — tri-lingual (EN / 中文 / BM)
    elements.append(mk_para("WRITTEN INSTRUCTIONAL MATERIALS",
                            size_pt=16, bold=True,
                            color=RGBColor(0x1F, 0x3A, 0x68)))
    elements.append(mk_para("书面教材",
                            size_pt=15, bold=True,
                            color=RGBColor(0x1F, 0x3A, 0x68)))
    elements.append(mk_para("BAHAN PENGAJARAN BERTULIS (WIM)",
                            size_pt=13, bold=False,
                            color=RGBColor(0x55, 0x55, 0x55)))
    elements += mk_blank(2)

    # Edition title — tri-lingual
    elements.append(mk_para("Consolidated Edition  ·  合订本  ·  Edisi Konsolidasi",
                            size_pt=22, bold=True,
                            color=RGBColor(0x1F, 0x3A, 0x68)))
    elements += mk_blank(1)
    elements.append(mk_para("NOSS → WIM Conversion Project",
                            size_pt=13, bold=False,
                            color=RGBColor(0x33, 0x33, 0x33)))
    elements.append(mk_para("国家职业技能标准 → 书面教材转换项目",
                            size_pt=12, bold=False,
                            color=RGBColor(0x33, 0x33, 0x33)))
    elements.append(mk_para("Projek Penukaran NOSS kepada WIM",
                            size_pt=11, bold=False,
                            color=RGBColor(0x55, 0x55, 0x55)))
    elements += mk_blank(2)

    # Subjects covered — tri-lingual label
    elements.append(mk_para("Covers 4 subjects  ·  涵盖 4 个科目  ·  Meliputi 4 Subjek:",
                            size_pt=11, bold=True))
    for subj in SUBJECTS:
        elements.append(mk_para(f"•  {subj['title_en']}  ·  {subj['title_bm']}  "
                                f"({subj['noss']}, {subj['level']})",
                                size_pt=10, bold=False,
                                color=RGBColor(0x33, 0x33, 0x33)))
    elements += mk_blank(3)
    elements.append(mk_para("Generated  ·  生成日期  ·  Dijana: 2026-04-17",
                            size_pt=9, bold=False,
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


def add_page_breaks_per_document(doc: Document) -> None:
    """Force a page break before every Heading 2 (CU) and Heading 3 (each
    individual .md file like KP-01 / KK-02 / etc.) so every CU and every
    source document starts on a fresh page.

    Implementation: set the <w:pageBreakBefore/> paragraph property. This is
    universally honoured by Word, WPS Office, and LibreOffice — no field
    update needed.
    """
    # First H1 does NOT get a break (section break + cover already handle it).
    # Every *subsequent* real subject H1 does (already handled by
    # front_matter_roman_numerals which starts a new section at each subject).
    seen_first_h2 = False
    seen_first_h3_in_cu = {}

    for para in doc.paragraphs:
        style = para.style.name
        if style not in ("Heading 2", "Heading 3"):
            if style == "Heading 1":
                # Reset the "first H2 in subject" tracker at each subject H1
                seen_first_h2 = False
                seen_first_h3_in_cu.clear()
            continue

        text = para.text.strip()

        # Skip TOC / LOF / LOT synthetic headings
        low = text.lower()
        if low in _SYNTHETIC_HEADINGS_LOWER or text in (LBL_CONTENTS, LBL_LIST_FIGURES, LBL_LIST_TABLES):
            continue

        if style == "Heading 2":
            # First H2 inside a subject: skip break — the subject H1 already
            # owns the fresh page. Every *subsequent* H2 (new CU) gets a break.
            if not seen_first_h2:
                seen_first_h2 = True
                continue
            # New CU — reset H3 tracker
            seen_first_h3_in_cu.clear()
            _set_page_break_before(para)
            continue

        # Heading 3: every .md file gets a page break, except the very first
        # H3 inside its enclosing CU (that CU's H2 already owns the new page).
        cu_key = id(para)  # placeholder; real CU id below
        # We need to know which CU this H3 is in. Use text of the last H2
        # seen as the key:
        cu_id = _last_seen_h2_id(para, doc)
        if cu_id not in seen_first_h3_in_cu:
            seen_first_h3_in_cu[cu_id] = True
            continue
        _set_page_break_before(para)


def _set_page_break_before(para) -> None:
    """Set <w:pageBreakBefore/> on a paragraph's pPr."""
    pPr = para._p.find(qn("w:pPr"))
    if pPr is None:
        pPr = OxmlElement("w:pPr")
        para._p.insert(0, pPr)
    existing = pPr.find(qn("w:pageBreakBefore"))
    if existing is None:
        pbb = OxmlElement("w:pageBreakBefore")
        pPr.append(pbb)


# Cache of (paragraph-element-id -> enclosing H2 text) built on first call
_H2_CACHE: dict[int, str] = {}
_H2_CACHE_DOC_ID: int | None = None


def _last_seen_h2_id(para, doc) -> str:
    """Return an identifier for the nearest preceding Heading 2 paragraph."""
    global _H2_CACHE, _H2_CACHE_DOC_ID
    doc_id = id(doc)
    if _H2_CACHE_DOC_ID != doc_id:
        _H2_CACHE = {}
        _H2_CACHE_DOC_ID = doc_id
        current = "<pre-h2>"
        for p in doc.paragraphs:
            if p.style.name == "Heading 2":
                current = p.text.strip() or "<unnamed-h2>"
            _H2_CACHE[id(p._p)] = current
    return _H2_CACHE.get(id(para._p), "<pre-h2>")


def inject_envelope_logos(doc: Document) -> None:
    """Replace every JPK-envelope paragraph with a proper 2-column table
    carrying the logo on the left and the address lines on the right
    (matches the reference PDF in raw/folder-2-sample-wim/).

    Pandoc's docx writer collapses the source `<table><tr><td><img></td>
    <td>address</td></tr></table>` envelope into a single body paragraph
    whose text runs "JABATAN PEMBANGUNAN KEMAHIRAN (JPK) TINGKAT 7-8 …".
    Since there is no `w:tbl` to inject into, we synthesise one here.
    Idempotent — a paragraph is only processed if it starts with the
    exact JPK address header and is not already preceded by an envelope
    table.
    """
    if not LOGO_PATH.exists():
        return
    body = doc.element.body
    address_prefix = "JABATAN PEMBANGUNAN KEMAHIRAN"

    # Collect the envelope paragraphs up-front; we'll mutate the tree after.
    targets = []
    for p in doc.paragraphs:
        text = p.text.strip()
        if text.startswith(address_prefix):
            # Skip cover-page header (its address is a short stand-alone line,
            # not the full "(JPK) TINGKAT 7-8 …" one-liner). We only want
            # the envelope that pandoc collapsed from the HTML <table>.
            if "(JPK)" in text and "TINGKAT" in text:
                targets.append((p, text))

    if not targets:
        return

    injected = 0
    for para, full_text in targets:
        # Split the run-together address back into 4 logical lines
        parts = _split_jpk_address(full_text)

        # Build a 2-column table:  [logo] | [address lines]
        tbl = doc.add_table(rows=1, cols=2)
        tbl.autofit = False
        # Left cell = logo
        left = tbl.rows[0].cells[0]
        left.width = Cm(4.0)
        lp = left.paragraphs[0]
        lp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        try:
            lp.add_run().add_picture(str(LOGO_PATH), width=Cm(3.2))
        except Exception as exc:
            print(f"      [warn] envelope logo inject failed: {exc}", file=sys.stderr)
        # Right cell = address lines (bold first line, rest plain)
        right = tbl.rows[0].cells[1]
        right.width = Cm(12.0)
        # Replace default empty paragraph with first address line (bold)
        right_paras = right.paragraphs
        first_para = right_paras[0]
        first_run = first_para.add_run(parts[0] if parts else full_text)
        first_run.bold = True
        first_run.font.size = Pt(10)
        for extra in parts[1:]:
            rp = right.add_paragraph(extra)
            for r in rp.runs:
                r.font.size = Pt(10)

        # Remove inside-vertical borders so the envelope reads as one unit
        tblPr = tbl._tbl.find(qn("w:tblPr"))
        if tblPr is None:
            tblPr = OxmlElement("w:tblPr")
            tbl._tbl.insert(0, tblPr)
        borders = OxmlElement("w:tblBorders")
        for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
            b = OxmlElement(f"w:{side}")
            b.set(qn("w:val"), "nil")
            borders.append(b)
        existing = tblPr.find(qn("w:tblBorders"))
        if existing is not None:
            tblPr.remove(existing)
        tblPr.append(borders)

        # Detach the new table from doc end and insert it BEFORE the
        # envelope paragraph, then remove that paragraph.
        new_tbl_el = tbl._tbl
        new_tbl_el.getparent().remove(new_tbl_el)
        para._p.addprevious(new_tbl_el)
        para._p.getparent().remove(para._p)
        injected += 1

    if injected:
        print(f"      rebuilt {injected} JPK envelope table(s) with logo")


def _split_jpk_address(full: str) -> list[str]:
    """Split the pandoc-collapsed envelope text back into address lines."""
    # Known canonical splits — tolerate minor whitespace variance
    markers = [
        "JABATAN PEMBANGUNAN KEMAHIRAN (JPK)",
        "TINGKAT 7-8, BLOK D4, KOMPLEKS D,",
        "PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,",
        "62530 PUTRAJAYA",
    ]
    result = []
    cursor = full
    for m in markers:
        idx = cursor.find(m)
        if idx < 0:
            continue
        result.append(m)
        cursor = cursor[idx + len(m):].lstrip(" ,")
    # If trailing content remains (e.g. extra suffix), append it
    tail = cursor.strip(" ,")
    if tail:
        result.append(tail)
    return result or [full]


def disable_even_odd_headers(doc: Document) -> None:
    """Remove <w:evenAndOddHeaders/> from settings.xml so the single default
    footer (with PAGE/NUMPAGES) applies to every page — not just odd ones.

    The reference-textbook.docx template enables this setting for a
    book-style mirror layout. After consolidation we flatten to one long
    section with a single footer; if the setting survives, even pages
    render with no page number at all (Word/WPS look for a non-existent
    even-page footer and show blank)."""
    try:
        settings = doc.settings.element
    except Exception:
        return
    for node in settings.findall(qn("w:evenAndOddHeaders")):
        settings.remove(node)
    # Also unify any per-section even footer ref so nothing hides the default
    for sect in doc.sections:
        sectPr = sect._sectPr
        for ref in list(sectPr.findall(qn("w:footerReference"))):
            t = ref.get(qn("w:type"))
            if t == "even":
                sectPr.remove(ref)
        for ref in list(sectPr.findall(qn("w:headerReference"))):
            t = ref.get(qn("w:type"))
            if t == "even":
                sectPr.remove(ref)


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

    print("[3/4] Post-processing (static TOC / LOF / LOT — WPS-friendly)...")
    doc = Document(str(output_path))
    insert_cover_page(doc)
    inject_envelope_logos(doc)           # restore JPK logo that pandoc drops
    colorize_headings(doc)
    apply_table_style(doc)
    promote_italic_captions(doc)
    number_figure_captions(doc)          # literal numbers + bookmarks
    add_drop_caps(doc)
    build_static_toc(doc)                # static TOC with hyperlinks
    insert_list_of_figures_tables(doc)   # static LOF + LOT
    add_page_breaks_per_document(doc)    # new CU + new .md file -> new page
    front_matter_roman_numerals(doc)
    add_running_header(doc)              # literal title, no STYLEREF
    add_page_numbers(doc)                # PAGE / NUMPAGES are universal
    disable_even_odd_headers(doc)        # ensure footer renders on EVERY page
    set_margins(doc)
    doc.save(str(output_path))

    print(f"[4/4] Done -> {output_path}")
    print(f"      {output_path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
