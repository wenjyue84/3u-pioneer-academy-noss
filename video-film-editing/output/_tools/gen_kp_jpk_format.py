# -*- coding: utf-8 -*-
"""Generate official-JPK-format Kertas Penerangan DOCX for the 47 Core Abilities notes."""
import re, os, sys
from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SRC_ROOT = Path(r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\11-core-abilities")
LOGO = Path(r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\_assets\jpk-logo-official.png")
OUT_DIR = Path(r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\05 3.3b Nota Pembelajaran (Kertas Penerangan)\Core Abilities L1-L3 (format JPK)")
OUT_DIR.mkdir(parents=True, exist_ok=True)

FOLDERS = [
    "L1-CA01-basic-working-communication",
    "L1-CA02-personal-behaviour-skill",
    "L1-CA03-work-place-ethics-awareness",
    "L1-CA04-safety-health-environment-awareness",
    "L2-CA01-communication-application",
    "L2-CA02-interpersonal-behaviour",
    "L2-CA03-work-place-culture-behaviour",
    "L2-CA04-health-safety-environmental-adaptation",
    "L3-CA01-effective-communication",
    "L3-CA02-information-technology-awareness",
    "L3-CA03-leadership-skill",
    "L3-CA04-work-place-ethics",
    "L3-CA05-administrative-skill",
    "L3-CA06-hse-consciousness",
]

def kp_sort_key(fname):
    # KP-1.1.md, KP-1.2_1.3.md, KP-4.2a.md, KP-6.1a.md ...
    stem = fname.stem.replace("KP-", "")
    # take leading numeric part before any letter, and letter suffix
    m = re.match(r"(\d+)\.(\d+)([a-z]?)", stem)
    if m:
        return (int(m.group(1)), int(m.group(2)), m.group(3))
    return (999, 999, stem)

def collect_files():
    items = []
    for folder in FOLDERS:
        d = SRC_ROOT / folder
        kps = sorted([p for p in d.glob("KP-*.md")], key=lambda p: kp_sort_key(p))
        for p in kps:
            items.append((folder, p))
    return items

# ---------- markdown inline parsing ----------
def add_runs_from_inline(paragraph, text, base_bold=False, base_italic=False):
    """Parse **bold**, *italic* and ***bold+italic*** markers (correctly nested) into runs.

    Uses a toggle-scan over runs of asterisks: a run of 1 toggles italic, 2 toggles bold,
    3 toggles both together. This correctly handles asymmetric nesting like
    "**2.2 Definisi *(Definition)***" (bold wraps a nested italic span, closed by *** = 1+2).
    Runs of 4+ asterisks, or an unmatched trailing run, are emitted as literal text.
    """
    tokens = re.split(r"(\*+)", text)
    bold = base_bold
    italic = base_italic
    for tok in tokens:
        if tok == "":
            continue
        if re.fullmatch(r"\*+", tok):
            n = len(tok)
            if n == 1:
                italic = not italic
                continue
            elif n == 2:
                bold = not bold
                continue
            elif n == 3:
                bold = not bold
                italic = not italic
                continue
            # 4+ asterisks: treat as literal text, fall through
        if tok == "":
            continue
        r = paragraph.add_run(tok)
        r.bold = bold
        r.italic = italic
        r.font.name = "Arial"
        r.font.size = Pt(11)
        r.font.name = "Arial"
        r.font.size = Pt(11)

def set_cell_text(cell, text, bold=False, italic=False, size=11, align=None):
    cell.text = ""
    p = cell.paragraphs[0]
    if align:
        p.alignment = align
    add_runs_from_inline(p, text, bold, italic)
    return p

# ---------- markdown document parsing ----------
def parse_md(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    header = {}
    i = 0
    # header table: lines like "| Label | Value |" until blank / non-table line, skip separator "|---|---|"
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2 and not re.match(r"^-+$", cells[0]) and not set(cells[0]) <= {"-"}:
                if not re.match(r"^:?-+:?$", cells[1]):
                    header[cells[0]] = cells[1]
            i += 1
            continue
        if line == "" and header:
            i += 1
            continue
        if line.startswith("##") :
            break
        i += 1
    # sections: split by "## " headings
    body = "\n".join(lines[i:])
    sections = {}
    parts = re.split(r"^##\s+(.+)$", body, flags=re.MULTILINE)
    # parts[0] is preamble (blank), then alternating heading/content
    for k in range(1, len(parts), 2):
        heading = parts[k].strip()
        content = parts[k+1] if k+1 < len(parts) else ""
        sections[heading.upper()] = content.strip("\n")
    return header, sections

# ---------- field helpers ----------
def add_field(paragraph, field_code, bold=False):
    run = paragraph.add_run()
    run.font.name = "Arial"
    run.font.size = Pt(11)
    run.bold = bold
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = field_code
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    t = OxmlElement('w:t')
    t.text = "1"
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(t)
    run._r.append(fldChar3)
    return run

def set_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top','left','bottom','right','insideH','insideV'):
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '4')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), '000000')
        borders.append(el)
    tblPr.append(borders)

def set_col_widths(table, widths_cm):
    for row in table.rows:
        for idx, w in enumerate(widths_cm):
            if idx < len(row.cells):
                row.cells[idx].width = Cm(w)

def shrink_margins(cell, top=40, bottom=40, left=80, right=80):
    tcPr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement('w:tcMar')
    for tag, val in (('top',top),('bottom',bottom),('start',left),('end',right)):
        node = OxmlElement(f'w:{tag}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        mar.append(node)
    tcPr.append(mar)

def set_font_default(doc):
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(11)
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), 'Arial')

LABEL_EN = {
    "KOD DAN NAMA PROGRAM": "PROGRAM'S CODE AND NAME",
    "TAHAP": "LEVEL",
    "NO. DAN TAJUK KEBOLEHAN TERAS": "CORE ABILITY NO. AND TITLE",
    "NO. DAN PENYATAAN KEBOLEHAN": "ABILITY NO. AND STATEMENT",
    "NO. KOD": "CODE NO.",
    "TAJUK": "TITLE",
    "KONTEKS PROGRAM": "PROGRAMME CONTEXT",
    "NAMA BAKAT / TARIKH": "TRAINEE'S NAME / DATE",
}

def build_page1_header_table(doc_or_header, header_fields, code_no, programme_extra):
    try:
        table = doc_or_header.add_table(rows=7, cols=3, width=Cm(17.0))
    except TypeError:
        table = doc_or_header.add_table(rows=7, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table)

    # Row 0: logo | title (merge cols 1-2)
    row0 = table.rows[0]
    row0.cells[1].merge(row0.cells[2])
    logo_cell, title_cell = row0.cells[0], row0.cells[1]
    logo_cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    p_logo = logo_cell.paragraphs[0]
    p_logo.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p_logo.add_run()
    if LOGO.exists():
        run.add_picture(str(LOGO), height=Cm(3.9))

    title_cell.text = ""
    addr_lines = [
        "JABATAN PEMBANGUNAN KEMAHIRAN",
        "KEMENTERIAN SUMBER MANUSIA",
        "ARAS 7 & 8 BLOK D4, KOMPLEK D",
        "PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN",
        "62530 PUTRAJAYA",
    ]
    for idx, ln in enumerate(addr_lines):
        p = title_cell.paragraphs[0] if idx == 0 else title_cell.add_paragraph()
        r = p.add_run(ln)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(11)
    p_blank = title_cell.add_paragraph()
    p_title = title_cell.add_paragraph()
    r = p_title.add_run("KERTAS PENERANGAN")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(20)
    p_sub = title_cell.add_paragraph()
    r1 = p_sub.add_run("(")
    r1.bold = True; r1.font.name="Arial"; r1.font.size=Pt(12)
    r2 = p_sub.add_run("INFORMATION SHEET")
    r2.bold = True; r2.italic = True; r2.font.name="Arial"; r2.font.size=Pt(12)
    r3 = p_sub.add_run(")")
    r3.bold = True; r3.font.name="Arial"; r3.font.size=Pt(12)

    def label_para(cell, bm, en):
        cell.text = ""
        p = cell.paragraphs[0]
        r = p.add_run(bm + " / ")
        r.bold = True; r.font.name="Arial"; r.font.size=Pt(11)
        r2 = p.add_run(en)
        r2.bold = True; r2.italic = True; r2.font.name="Arial"; r2.font.size=Pt(11)
        return p

    labels_order = [
        "KOD DAN NAMA PROGRAM",
        "TAHAP",
        "NO. DAN TAJUK KEBOLEHAN TERAS",
        "NO. DAN PENYATAAN KEBOLEHAN",
    ]
    row_idx = 1
    for lab in labels_order:
        row = table.rows[row_idx]
        row.cells[1].merge(row.cells[2])
        label_para(row.cells[0], lab, LABEL_EN[lab])
        val = header_fields.get(lab, "")
        if lab == "KOD DAN NAMA PROGRAM" and programme_extra:
            val = f"{val} {programme_extra}"
        # multiple ability statements separated by " / " -> split into lines if contains numbering pattern
        set_cell_text(row.cells[1], val, bold=True)
        row_idx += 1

    # NO. KOD row with page info
    row = table.rows[5]
    label_para(row.cells[0], "NO. KOD", LABEL_EN["NO. KOD"])
    set_cell_text(row.cells[1], code_no, bold=True)
    pcell = row.cells[2]
    pcell.text = ""
    p1 = pcell.paragraphs[0]
    r = p1.add_run("Mukasurat / ")
    r.bold = True; r.font.name="Arial"; r.font.size=Pt(11)
    r2 = p1.add_run("Page")
    r2.bold = True; r2.italic = True; r2.font.name="Arial"; r2.font.size=Pt(11)
    r3 = p1.add_run(" : ")
    r3.bold = True; r3.font.name="Arial"; r3.font.size=Pt(11)
    add_field(p1, "PAGE", bold=True)
    p2 = pcell.add_paragraph()
    r = p2.add_run("Drpd / ")
    r.bold = True; r.font.name="Arial"; r.font.size=Pt(11)
    r2 = p2.add_run("of")
    r2.bold = True; r2.italic = True; r2.font.name="Arial"; r2.font.size=Pt(11)
    r3 = p2.add_run(" : ")
    r3.bold = True; r3.font.name="Arial"; r3.font.size=Pt(11)
    add_field(p2, "NUMPAGES", bold=True)

    # blank spacer row (merged) - use for spacing like the source has empty row before TAJUK
    row = table.rows[6]
    row.cells[0].merge(row.cells[1]).merge(row.cells[2])
    set_cell_text(row.cells[0], "")

    set_col_widths(table, [4.5, 8.5, 4.0])
    for row in table.rows:
        for c in row.cells:
            shrink_margins(c)
    return table

def build_running_header(section, code_no):
    header = section.header
    header.is_linked_to_previous = False
    # clear default paragraph
    for p in list(header.paragraphs):
        p.text = ""
    table = header.add_table(rows=1, cols=3, width=Cm(17.0))
    set_table_borders(table)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    row = table.rows[0]
    p0 = row.cells[0].paragraphs[0]
    r = p0.add_run("NO. KOD /")
    r.bold = True; r.font.name = "Arial"; r.font.size = Pt(10)
    r2 = p0.add_run("CODE NO.")
    r2.bold = True; r2.italic = True; r2.font.name = "Arial"; r2.font.size = Pt(10)
    set_cell_text(row.cells[1], code_no, bold=True, size=10)
    pcell = row.cells[2]
    pcell.text = ""
    p1 = pcell.paragraphs[0]
    r = p1.add_run("Mukasurat/ ")
    r.bold = True; r.font.size = Pt(10); r.font.name="Arial"
    r2 = p1.add_run("Page")
    r2.bold = True; r2.italic = True; r2.font.size = Pt(10); r2.font.name="Arial"
    r3 = p1.add_run(" : ")
    r3.bold = True; r3.font.size = Pt(10); r3.font.name="Arial"
    add_field(p1, "PAGE", bold=True)
    p2 = pcell.add_paragraph()
    r = p2.add_run("Drpd. / ")
    r.bold = True; r.font.size = Pt(10); r.font.name="Arial"
    r2 = p2.add_run("of")
    r2.bold = True; r2.italic = True; r2.font.size = Pt(10); r2.font.name="Arial"
    r3 = p2.add_run(": ")
    r3.bold = True; r3.font.size = Pt(10); r3.font.name="Arial"
    add_field(p2, "NUMPAGES", bold=True)
    set_col_widths(table, [4.0, 6.5, 4.0])
    for c in row.cells:
        shrink_margins(c)

def build_footer(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_field(p, "PAGE")

def add_heading_line(doc, bm, en, bold=True):
    p = doc.add_paragraph()
    r = p.add_run(bm)
    r.bold = True; r.font.name="Arial"; r.font.size=Pt(12)
    r2 = p.add_run("/")
    r2.bold = True; r2.font.name="Arial"; r2.font.size=Pt(12)
    r3 = p.add_run(en)
    r3.bold = True; r3.italic = True; r3.font.name="Arial"; r3.font.size=Pt(12)
    r4 = p.add_run(":")
    r4.bold = True; r4.font.name="Arial"; r4.font.size=Pt(12)
    return p

def render_markdown_block(doc, text):
    """Very small markdown renderer: headings ### , bullets -, numbered '**n.**', tables, paragraphs."""
    lines = text.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if stripped == "":
            i += 1
            continue
        # sub-heading ###
        m = re.match(r"^###\s+(.+)$", stripped)
        if m:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            add_runs_from_inline(p, m.group(1), base_bold=True)
            for run in p.runs:
                run.bold = True
                run.font.size = Pt(12)
            i += 1
            continue
        # markdown table
        if stripped.startswith("|"):
            tbl_lines = []
            while i < n and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i].strip())
                i += 1
            rows = []
            for tl in tbl_lines:
                cells = [c.strip() for c in tl.strip("|").split("|")]
                if all(re.match(r"^:?-+:?$", c) for c in cells):
                    continue
                rows.append(cells)
            if rows:
                ncols = max(len(r) for r in rows)
                t = doc.add_table(rows=len(rows), cols=ncols)
                set_table_borders(t)
                for ri, r in enumerate(rows):
                    for ci in range(ncols):
                        val = r[ci] if ci < len(r) else ""
                        set_cell_text(t.rows[ri].cells[ci], val, bold=(ri == 0))
                doc.add_paragraph()
            continue
        # bullet list
        if re.match(r"^[-*]\s+", stripped) and not re.match(r"^\*\*", stripped):
            p = doc.add_paragraph(style='List Bullet')
            content = re.sub(r"^[-*]\s+", "", stripped)
            add_runs_from_inline(p, content)
            i += 1
            continue
        # numbered like "**1.** text" or "1. text" or "1 text"
        # default paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(8)
        add_runs_from_inline(p, stripped)
        i += 1
    return

def build_doc(folder, path, seq, out_dir):
    header_fields, sections = parse_md(path)
    code_no = header_fields.get("NO. KOD", "")
    tajuk = header_fields.get("TAJUK", "")
    tajuk_bm = tajuk
    programme_extra = "(untuk program IT-072-3:2012 VIDEO / FILM (EDITING))"

    doc = Document()
    set_font_default(doc)
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(2.0)
    section.right_margin = Cm(2.0)
    section.top_margin = Cm(1.5)
    section.bottom_margin = Cm(1.5)
    section.different_first_page_header_footer = True

    # Page 1 first-page header: leave empty (the identification table now lives in the body,
    # exactly like the official page 1).
    section.first_page_header.is_linked_to_previous = False
    for p in list(section.first_page_header.paragraphs):
        p.text = ""

    # Running header for page 2+
    build_running_header(section, code_no)

    # footer same both
    build_footer(section)
    section.first_page_footer.is_linked_to_previous = False
    fp = section.first_page_footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_field(fp, "PAGE")

    # Body content starts with the full identification table (page-1 block), then TAJUK etc.
    build_page1_header_table(doc, header_fields, code_no, programme_extra)
    doc.add_paragraph()

    add_heading_line(doc, "TAJUK", "TITLE")
    p = doc.paragraphs[-1]
    p.add_run("  ")
    add_runs_from_inline(p, tajuk_bm, base_bold=True)
    doc.add_paragraph()

    add_heading_line(doc, "TUJUAN", "PURPOSE")
    doc.add_paragraph()
    tujuan_text = sections.get("TUJUAN", "")
    render_markdown_block(doc, tujuan_text)

    add_heading_line(doc, "PENERANGAN", "INFORMATION")
    doc.add_paragraph()
    penerangan_text = sections.get("PENERANGAN", "")
    render_markdown_block(doc, penerangan_text)

    add_heading_line(doc, "SOALAN", "QUESTION")
    doc.add_paragraph()
    soalan_text = sections.get("SOALAN", "")
    render_markdown_block(doc, soalan_text)

    add_heading_line(doc, "RUJUKAN", "REFERENCES")
    doc.add_paragraph()
    rujukan_text = sections.get("RUJUKAN", "")
    render_markdown_block(doc, rujukan_text)

    # filename
    safe_title = re.sub(r'[\\/:*?"<>|]', '-', tajuk_bm)[:40].strip()
    kp_num = path.stem.replace("KP-", "")
    fname = f"KP-CA-{seq:02d} KP{kp_num} {safe_title} (IT-072).docx"
    fname = re.sub(r"\s+", " ", fname)
    out_path = out_dir / fname
    doc.save(str(out_path))
    return out_path

def main():
    items = collect_files()
    print(f"Total files: {len(items)}")
    results = []
    for idx, (folder, path) in enumerate(items, start=1):
        try:
            out_path = build_doc(folder, path, idx, OUT_DIR)
            print(idx, "OK", out_path.name)
            results.append(out_path)
        except Exception as e:
            print(idx, "FAIL", folder, path.name, repr(e))
            raise
    print("Done", len(results))

if __name__ == "__main__":
    main()
