"""
NOSS IT-020 Textbook .docx Generator
Reads .md content files and generates NOSS-formatted .docx textbooks.
Usage: uv run --with python-docx scripts/generate_docx.py [--level 3|4|5|all]
"""

import re
import sys
import json
from pathlib import Path
from datetime import datetime

# python-docx imports
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

PROJECT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_DIR / "content"
OUTPUT_DIR = PROJECT_DIR / "output"
IMAGES_DIR = CONTENT_DIR / "images"
GDRIVE_STATE = PROJECT_DIR / "scripts" / ".gdrive-state.json"

LEVELS = {
    "3": {
        "code": "IT-020-3:2013",
        "title_en": "Computer System Operation",
        "title_bm": "Operasi Sistem Komputer",
        "level": "L3",
        "filename": "NOSS-IT-020-3-Computer-System-Operation.docx",
    },
    "4": {
        "code": "IT-020-4:2013",
        "title_en": "Computer Systems Administration",
        "title_bm": "Pentadbiran Sistem Komputer",
        "level": "L4",
        "filename": "NOSS-IT-020-4-Computer-Systems-Administration.docx",
    },
    "5": {
        "code": "IT-020-5:2013",
        "title_en": "Computer Systems Management",
        "title_bm": "Pengurusan Sistem Komputer",
        "level": "L5",
        "filename": "NOSS-IT-020-5-Computer-Systems-Management.docx",
    },
}

# ── Styling constants ──────────────────────────────────────────────

FONT_NAME = "Arial"
FONT_SIZE_BODY = Pt(10)
FONT_SIZE_HEADING1 = Pt(16)
FONT_SIZE_HEADING2 = Pt(13)
FONT_SIZE_HEADING3 = Pt(11)
FONT_SIZE_TABLE = Pt(9)
FONT_SIZE_SMALL = Pt(8)

COLOR_HEADER_BG = "1F4E79"       # Dark blue for NOSS header table
COLOR_HEADER_TEXT = "FFFFFF"      # White text on header
COLOR_TABLE_HEADER = "1F4E79"    # Dark blue for data table headers
COLOR_TABLE_HEADER_TEXT = "FFFFFF"  # White text on data table headers
COLOR_TABLE_ALT_ROW = "F2F7FB"   # Very light blue for alternating rows
COLOR_ACCENT = "2E75B6"          # Accent blue
COLOR_BORDER = "B4C6E0"          # Light blue-gray for table borders
COLOR_HEADING_ACCENT = "1F4E79"  # Dark blue for section heading accent
COLOR_COVER_LINE = "1F4E79"      # Divider line on cover page
COLOR_TOTALS_ROW = "D6E4F0"      # Light blue for totals/summary row


# ── Markdown parsing helpers ───────────────────────────────────────

def parse_md_tables(text):
    """Extract all Markdown tables from text as list of (headers, rows)."""
    tables = []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Detect table start: line starts with |
        if line.startswith("|") and i + 1 < len(lines):
            table_lines = [line]
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("|"):
                table_lines.append(lines[j].strip())
                j += 1

            if len(table_lines) >= 2:
                # Parse cells
                parsed_rows = []
                for tl in table_lines:
                    cells = [c.strip() for c in tl.split("|")]
                    # Remove empty first/last from leading/trailing |
                    if cells and cells[0] == "":
                        cells = cells[1:]
                    if cells and cells[-1] == "":
                        cells = cells[:-1]
                    parsed_rows.append(cells)

                # Check if row 1 is separator (---)
                if len(parsed_rows) > 1 and all(
                    re.match(r"^[-:]+$", c) for c in parsed_rows[1] if c
                ):
                    headers = parsed_rows[0]
                    rows = parsed_rows[2:]
                else:
                    headers = parsed_rows[0]
                    rows = parsed_rows[1:]

                tables.append((headers, rows))
            i = j
        else:
            i += 1
    return tables


def parse_md_sections(text):
    """Split markdown into sections by ## headings."""
    sections = []
    current_heading = ""
    current_body = []

    for line in text.split("\n"):
        if line.startswith("## "):
            if current_heading or current_body:
                sections.append((current_heading, "\n".join(current_body)))
            current_heading = line[3:].strip()
            current_body = []
        elif line.startswith("# ") and not current_heading:
            current_heading = line[2:].strip()
            current_body = []
        else:
            current_body.append(line)

    if current_heading or current_body:
        sections.append((current_heading, "\n".join(current_body)))

    return sections


def extract_title_from_md(text):
    """Get the first # heading from markdown."""
    for line in text.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


# ── docx building helpers ──────────────────────────────────────────

def set_cell_shading(cell, color):
    """Set cell background color."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def set_cell_borders(cell, color="000000", sz="4", val="single"):
    """Set all four borders on a cell."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    borders_xml = (
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:right w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(parse_xml(borders_xml))


def set_cell_margins(cell, top=40, bottom=40, left=80, right=80):
    """Set cell internal margins (padding) in twips."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    margins_xml = (
        f'<w:tcMar {nsdecls("w")}>'
        f'  <w:top w:w="{top}" w:type="dxa"/>'
        f'  <w:left w:w="{left}" w:type="dxa"/>'
        f'  <w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'  <w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(parse_xml(margins_xml))


def set_table_full_width(table):
    """Set table to use full page width."""
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>')
    tblW = parse_xml(f'<w:tblW {nsdecls("w")} w:w="5000" w:type="pct"/>')
    # Remove existing tblW if any
    existing = tblPr.findall(qn('w:tblW'))
    for e in existing:
        tblPr.remove(e)
    tblPr.append(tblW)


def set_table_borders(table, color="B4C6E0", sz="4"):
    """Set borders on the entire table (outer + inner)."""
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>')
    borders_xml = (
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    )
    # Remove existing borders
    existing = tblPr.findall(qn('w:tblBorders'))
    for e in existing:
        tblPr.remove(e)
    tblPr.append(parse_xml(borders_xml))


def add_rich_text_to_cell(cell, text, font_size=FONT_SIZE_TABLE, font_color=None,
                          bold_override=None, alignment=None):
    """Add text to a cell, parsing markdown bold (**text**) inline."""
    p = cell.paragraphs[0]
    if alignment:
        p.alignment = alignment
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)

    # Split text by bold markers
    parts = re.split(r'(\*\*.*?\*\*)', str(text))
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            run = p.add_run(part[2:-2])
            run.font.bold = True
        else:
            run = p.add_run(part)
            if bold_override:
                run.font.bold = True
        run.font.name = FONT_NAME
        run.font.size = font_size
        if font_color:
            run.font.color.rgb = RGBColor.from_string(font_color)


def add_formatted_paragraph(doc, text, style=None, bold=False, size=None,
                            alignment=None, space_after=None, space_before=None,
                            font_name=None, color=None):
    """Add a paragraph with formatting."""
    p = doc.add_paragraph()
    if style:
        p.style = style

    # Parse markdown bold in text
    parts = re.split(r'(\*\*.*?\*\*)', text)
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            run = p.add_run(part[2:-2])
            run.font.bold = True
        else:
            run = p.add_run(part)
            if bold:
                run.font.bold = True
        run.font.name = font_name or FONT_NAME
        if size:
            run.font.size = size
        if color:
            run.font.color.rgb = RGBColor.from_string(color)

    if alignment:
        p.alignment = alignment
    if space_after is not None:
        p.paragraph_format.space_after = space_after
    if space_before is not None:
        p.paragraph_format.space_before = space_before
    return p


def add_horizontal_line(doc, color=COLOR_COVER_LINE, thickness="12"):
    """Add a horizontal line (bottom border on an empty paragraph)."""
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    borders_xml = (
        f'<w:pBdr {nsdecls("w")}>'
        f'  <w:bottom w:val="single" w:sz="{thickness}" w:space="1" w:color="{color}"/>'
        f'</w:pBdr>'
    )
    pPr.append(parse_xml(borders_xml))
    p.paragraph_format.space_after = Pt(6)
    return p


def add_section_heading(doc, text, level=2):
    """Add a styled section heading with accent bar.

    For level=1 (CoCu titles), applies Heading 1 style to enable TOC field recognition.
    Custom NOSS formatting (colors, borders) is applied on top of the style.
    """
    if level == 1:
        size = FONT_SIZE_HEADING1
        # Apply Heading 1 style for TOC field recognition
        p = doc.add_paragraph(text, style='Heading 1')
    elif level == 2:
        size = FONT_SIZE_HEADING2
        p = doc.add_paragraph()
    else:
        size = FONT_SIZE_HEADING3
        p = doc.add_paragraph()

    # Apply custom NOSS formatting (only add runs if not already in heading style)
    if level != 1:
        run = p.add_run(text)
        run.font.name = FONT_NAME
        run.font.size = size
        run.font.bold = True
        run.font.color.rgb = RGBColor.from_string(COLOR_HEADING_ACCENT)
    else:
        # For Heading 1, customize the existing run
        run = p.runs[0] if p.runs else p.add_run(text)
        run.font.name = FONT_NAME
        run.font.size = size
        run.font.color.rgb = RGBColor.from_string(COLOR_HEADING_ACCENT)

    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(2)

    # Add thin accent line below heading
    pPr = p._p.get_or_add_pPr()
    borders_xml = (
        f'<w:pBdr {nsdecls("w")}>'
        f'  <w:bottom w:val="single" w:sz="6" w:space="2" w:color="{COLOR_ACCENT}"/>'
        f'</w:pBdr>'
    )
    pPr.append(parse_xml(borders_xml))
    return p


def add_page_header_footer(doc, level_info):
    """Add running header and footer with page numbers to all sections.

    Headers show program code on all sections.
    Footers show 'Page X of Y' format, but only on content sections (section 2+).
    First section (cover + TOC) has no page numbers.
    Page numbering restarts at 1 in the content section.
    """
    for section_idx, section in enumerate(doc.sections):
        # Header: program code on right (all sections)
        header = section.header
        header.is_linked_to_previous = False
        hp = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        run = hp.add_run(f"{level_info['code']}  |  {level_info['title_en']}  |  {level_info['level']}")
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE_SMALL
        run.font.color.rgb = RGBColor.from_string("808080")
        # Bottom border on header
        hpPr = hp._p.get_or_add_pPr()
        hbdr = parse_xml(
            f'<w:pBdr {nsdecls("w")}>'
            f'  <w:bottom w:val="single" w:sz="4" w:space="1" w:color="B4C6E0"/>'
            f'</w:pBdr>'
        )
        hpPr.append(hbdr)

        # Footer with page numbers only in content sections (section_idx >= 1)
        footer = section.footer
        footer.is_linked_to_previous = False

        # Only add page numbers if this is a content section (not cover/TOC)
        if section_idx >= 1:
            fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
            fp.alignment = WD_ALIGN_PARAGRAPH.CENTER

            # "3U Pioneer Academy" on left side
            run_left = fp.add_run("3U Pioneer Academy Sdn Bhd")
            run_left.font.name = FONT_NAME
            run_left.font.size = FONT_SIZE_SMALL
            run_left.font.color.rgb = RGBColor.from_string("808080")

            # Tab to center for page number
            run_tab = fp.add_run("\t\t")
            run_tab.font.size = FONT_SIZE_SMALL

            # "Page " prefix
            run_pre = fp.add_run("Page ")
            run_pre.font.name = FONT_NAME
            run_pre.font.size = FONT_SIZE_SMALL
            run_pre.font.color.rgb = RGBColor.from_string("808080")

            # Insert PAGE field (current page number)
            fld_char_begin = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
            fld_code = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> PAGE </w:instrText>')
            fld_char_end = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')

            run_begin = fp.add_run()
            run_begin._r.append(fld_char_begin)
            run_code = fp.add_run()
            run_code._r.append(fld_code)
            run_end = fp.add_run()
            run_end._r.append(fld_char_end)

            # " of " separator
            run_sep = fp.add_run(" of ")
            run_sep.font.name = FONT_NAME
            run_sep.font.size = FONT_SIZE_SMALL
            run_sep.font.color.rgb = RGBColor.from_string("808080")

            # Insert NUMPAGES field (total pages)
            fld_char_begin2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
            fld_code2 = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> NUMPAGES </w:instrText>')
            fld_char_end2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')

            run_begin2 = fp.add_run()
            run_begin2._r.append(fld_char_begin2)
            run_code2 = fp.add_run()
            run_code2._r.append(fld_code2)
            run_end2 = fp.add_run()
            run_end2._r.append(fld_char_end2)

            # Top border on footer
            fpPr = fp._p.get_or_add_pPr()
            fbdr = parse_xml(
                f'<w:pBdr {nsdecls("w")}>'
                f'  <w:top w:val="single" w:sz="4" w:space="1" w:color="B4C6E0"/>'
                f'</w:pBdr>'
            )
            fpPr.append(fbdr)


def create_noss_header_table(doc, level_info, cocu_num, cocu_title,
                              work_activities, total_cocu, page_range=""):
    """Create the standard NOSS header table (5 rows x 3 cols)."""
    table = doc.add_table(rows=5, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_full_width(table)

    # Set white borders for clean look on dark bg
    set_table_borders(table, color=COLOR_HEADER_TEXT, sz="4")

    # Row data
    rows_data = [
        ("PROGRAM CODE AND NAME", f"{level_info['code']} {level_info['title_en'].upper()}", ""),
        ("LEVEL", level_info['level'], ""),
        ("NO. AND UNIT TITLE OF COMPETENCY", f"CoCu {cocu_num}: {cocu_title}", ""),
        ("NO. AND WORK ACTIVITY STATEMENT", work_activities, ""),
        ("NO. CODE", f"{level_info['code']} - CoCu {cocu_num} / P({cocu_num}/{total_cocu})",
         f"PAGE: {page_range}" if page_range else ""),
    ]

    for i, (label, val1, val2) in enumerate(rows_data):
        row = table.rows[i]

        # First cell - label (dark blue bg, white text)
        cell0 = row.cells[0]
        p = cell0.paragraphs[0]
        run = p.add_run(label)
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE_TABLE
        run.font.bold = True
        run.font.color.rgb = RGBColor.from_string(COLOR_HEADER_TEXT)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        set_cell_shading(cell0, COLOR_HEADER_BG)
        cell0.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(cell0, top=30, bottom=30, left=100, right=60)

        # Second cell - value (light background)
        cell1 = row.cells[1]
        p = cell1.paragraphs[0]
        run = p.add_run(val1)
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE_TABLE
        run.font.bold = True
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        set_cell_shading(cell1, "EDF2F9")
        cell1.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(cell1, top=30, bottom=30, left=80, right=60)

        # Third cell - second value or merge
        cell2 = row.cells[2]
        if val2:
            p = cell2.paragraphs[0]
            run = p.add_run(val2)
            run.font.name = FONT_NAME
            run.font.size = FONT_SIZE_TABLE
            run.font.bold = True
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            set_cell_shading(cell2, "EDF2F9")
            cell2.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell2, top=30, bottom=30, left=80, right=60)
        elif i < 4:
            # Merge cells 1 and 2 for rows without page info
            cell1.merge(cell2)

    doc.add_paragraph()  # spacing
    return table


def create_data_table(doc, headers, rows, header_color=None, header_text_color=None):
    """Create a professional data table with borders, shading, and rich text."""
    if not headers or not rows:
        return None

    hdr_bg = header_color or COLOR_TABLE_HEADER
    hdr_text = header_text_color or COLOR_TABLE_HEADER_TEXT

    num_cols = len(headers)
    table = doc.add_table(rows=1 + len(rows), cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_full_width(table)
    set_table_borders(table, color=COLOR_BORDER, sz="4")

    # Header row
    for j, header in enumerate(headers):
        cell = table.rows[0].cells[j]
        p = cell.paragraphs[0]
        run = p.add_run(str(header))
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE_TABLE
        run.font.bold = True
        run.font.color.rgb = RGBColor.from_string(hdr_text)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        set_cell_shading(cell, hdr_bg)
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(cell, top=40, bottom=40, left=80, right=80)

    # Data rows
    for i, row_data in enumerate(rows):
        is_totals_row = any(
            "**" in str(c) or str(c).strip().startswith("100%")
            for c in row_data if c
        )

        for j in range(min(len(row_data), num_cols)):
            cell = table.rows[i + 1].cells[j]

            # Rich text parsing for bold markdown
            add_rich_text_to_cell(cell, row_data[j], font_size=FONT_SIZE_TABLE)

            # Alternating row shading
            if is_totals_row:
                set_cell_shading(cell, COLOR_TOTALS_ROW)
            elif i % 2 == 1:
                set_cell_shading(cell, COLOR_TABLE_ALT_ROW)

            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=30, bottom=30, left=80, right=80)

    doc.add_paragraph()  # spacing
    return table


def add_cover_page(doc, level_info):
    """Add a professional cover page for the textbook."""
    # Top spacing
    for _ in range(4):
        doc.add_paragraph()

    # Academy name
    add_formatted_paragraph(
        doc, "3U PIONEER ACADEMY SDN BHD",
        bold=True, size=Pt(18),
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color=COLOR_HEADER_BG
    )

    doc.add_paragraph()

    # Decorative line
    add_horizontal_line(doc, color=COLOR_COVER_LINE, thickness="18")

    doc.add_paragraph()

    # NOSS label
    add_formatted_paragraph(
        doc, "NATIONAL OCCUPATIONAL SKILLS STANDARD (NOSS)",
        bold=True, size=Pt(11),
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color="666666",
        space_after=Pt(8)
    )

    # Program code
    add_formatted_paragraph(
        doc, level_info["code"],
        bold=True, size=Pt(20),
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color=COLOR_HEADER_BG,
        space_after=Pt(4)
    )

    # Title EN
    add_formatted_paragraph(
        doc, level_info["title_en"].upper(),
        bold=True, size=Pt(20),
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color=COLOR_HEADER_BG,
        space_after=Pt(4)
    )

    # Title BM
    add_formatted_paragraph(
        doc, f"({level_info['title_bm']})",
        bold=False, size=FONT_SIZE_HEADING2,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color="666666",
        space_after=Pt(8)
    )

    doc.add_paragraph()

    # Decorative line
    add_horizontal_line(doc, color=COLOR_COVER_LINE, thickness="18")

    doc.add_paragraph()

    # Level badge
    add_formatted_paragraph(
        doc, f"LEVEL {level_info['level'][1:]}",
        bold=True, size=Pt(16),
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color=COLOR_ACCENT
    )

    doc.add_paragraph()
    doc.add_paragraph()

    # Date
    add_formatted_paragraph(
        doc, datetime.now().strftime('%d %B %Y'),
        size=FONT_SIZE_BODY,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color="999999"
    )

    # Page break
    doc.add_page_break()


def add_dynamic_toc_field(doc):
    """Add a dynamic Word TOC field that updates page numbers on document refresh.

    Uses Word field codes to create a TOC that:
    - Automatically pulls chapter titles from Heading 1 styles
    - Shows page numbers next to each entry
    - Updates when document is refreshed in Word (right-click > Update Field)
    """
    p = doc.add_paragraph()

    # TOC field code: \o "1-1" = outline level 1 only, \h = hyperlinks, \z = hide page numbers in web view
    toc_xml = (
        f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>'
    )
    fld_char_begin = parse_xml(toc_xml)

    # Field code instruction for TOC
    instr_xml = (
        f'<w:instrText {nsdecls("w")} xml:space="preserve"> TOC \\o "1-1" \\h \\z \\u </w:instrText>'
    )
    instr_text = parse_xml(instr_xml)

    fld_char_end_xml = (
        f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>'
    )
    fld_char_end = parse_xml(fld_char_end_xml)

    # Append the field components to the paragraph
    run = p.add_run()
    run._r.append(fld_char_begin)

    run = p.add_run()
    run._r.append(instr_text)

    run = p.add_run()
    run._r.append(fld_char_end)


def add_table_of_contents(doc, md_files, level_info):
    """Add a formatted table of contents with dynamic TOC field.

    Displays a title and accent line, then inserts a Word TOC field that
    automatically updates chapter titles and page numbers when refreshed.

    Also creates a new section after TOC to isolate cover/TOC pages from
    content page numbering. Page numbering restarts at 1 for content.
    """
    add_formatted_paragraph(
        doc, "TABLE OF CONTENTS",
        bold=True, size=FONT_SIZE_HEADING1,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color=COLOR_HEADING_ACCENT,
        space_after=Pt(6)
    )

    add_horizontal_line(doc, color=COLOR_ACCENT, thickness="6")

    doc.add_paragraph()

    # Insert dynamic TOC field instead of static table
    add_dynamic_toc_field(doc)

    doc.add_paragraph()
    doc.add_page_break()

    # Create a new section here to separate cover/TOC from content pages
    # This allows page numbering to restart from 1 in the content section
    new_section = doc.add_section()
    new_section.different_first_page_header_footer = False


def process_practical_exercises_section(doc, body):
    """Render Practical Exercises section with Lab subsections properly formatted."""
    # Parse the body to extract lab subsections (### Lab X.Y: ...)
    current_lab = None
    current_lab_content = []

    for line in body.split("\n"):
        stripped = line.strip()

        if stripped.startswith("### Lab"):
            # Save previous lab if any
            if current_lab:
                render_lab_section(doc, current_lab, "\n".join(current_lab_content))
            # Start new lab
            current_lab = stripped[4:].strip()  # Remove "### "
            current_lab_content = []
        elif current_lab is not None:
            current_lab_content.append(line)

    # Save last lab
    if current_lab:
        render_lab_section(doc, current_lab, "\n".join(current_lab_content))


def render_lab_section(doc, lab_title, lab_body):
    """Render a single lab subsection (### Lab X.Y)."""
    add_section_heading(doc, lab_title, level=3)

    current_subsection = None
    current_subsection_content = []

    for line in lab_body.split("\n"):
        stripped = line.strip()

        # Detect subsection markers (lines ending with colon and bold)
        if stripped.startswith("**") and stripped.endswith(":**"):
            # Save previous subsection
            if current_subsection:
                render_lab_subsection(doc, current_subsection, "\n".join(current_subsection_content))
            current_subsection = stripped.strip("*").rstrip(":")
            current_subsection_content = []
        elif current_subsection is not None:
            current_subsection_content.append(line)

    # Save last subsection
    if current_subsection:
        render_lab_subsection(doc, current_subsection, "\n".join(current_subsection_content))


def render_lab_subsection(doc, subsection_title, content):
    """Render a lab subsection (Objective, Duration, Equipment, Procedures, etc.)."""
    # Add subsection title as bold paragraph
    add_formatted_paragraph(
        doc, subsection_title,
        bold=True, size=FONT_SIZE_BODY, space_after=Pt(4)
    )

    # Parse content lines
    for line in content.split("\n"):
        stripped = line.strip()

        if not stripped:
            continue

        # Numbered list item (1., 2., etc.)
        if re.match(r"^[\d]+\.\s+", stripped):
            p = doc.add_paragraph(stripped, style='List Number')
            if p.runs:
                for run in p.runs:
                    run.font.name = FONT_NAME
                    run.font.size = FONT_SIZE_BODY
        # Checkbox item (- [ ] or - [x])
        elif re.match(r"^-\s+\[\s*[xX ]?\s*\]", stripped):
            checkbox_text = re.sub(r"^-\s+\[\s*[xX ]?\s*\]\s*", "", stripped)
            p = doc.add_paragraph(checkbox_text, style='List Bullet')
            if p.runs:
                for run in p.runs:
                    run.font.name = FONT_NAME
                    run.font.size = FONT_SIZE_BODY
        # Bullet item (-, *, or +)
        elif stripped.startswith(("-", "*", "+")) and len(stripped) > 1 and stripped[1] in (" ", "\t"):
            bullet_text = stripped[1:].strip()
            p = doc.add_paragraph(bullet_text, style='List Bullet')
            if p.runs:
                for run in p.runs:
                    run.font.name = FONT_NAME
                    run.font.size = FONT_SIZE_BODY
        # Regular text
        else:
            add_formatted_paragraph(doc, stripped, size=FONT_SIZE_BODY)


def process_references_section(doc, body):
    """Render References section with subsections and proper formatting."""
    current_subsection = None
    current_subsection_items = []

    for line in body.split("\n"):
        stripped = line.strip()

        # Detect subsection markers (### Official Standards, etc.)
        if stripped.startswith("### "):
            # Save previous subsection
            if current_subsection:
                render_references_subsection(doc, current_subsection, current_subsection_items)
            current_subsection = stripped[4:].strip()
            current_subsection_items = []
        elif current_subsection is not None:
            if stripped:
                current_subsection_items.append(stripped)

    # Save last subsection
    if current_subsection:
        render_references_subsection(doc, current_subsection, current_subsection_items)


def render_references_subsection(doc, subsection_title, items):
    """Render a References subsection with proper heading and items."""
    add_section_heading(doc, subsection_title, level=3)

    for item in items:
        if item.startswith("- "):
            # Bullet item
            bullet_text = item[2:].strip()
            p = doc.add_paragraph(bullet_text, style='List Bullet')
            if p.runs:
                for run in p.runs:
                    run.font.name = FONT_NAME
                    run.font.size = FONT_SIZE_BODY
        elif item.startswith("* "):
            # Bullet item with asterisk
            bullet_text = item[2:].strip()
            p = doc.add_paragraph(bullet_text, style='List Bullet')
            if p.runs:
                for run in p.runs:
                    run.font.name = FONT_NAME
                    run.font.size = FONT_SIZE_BODY
        else:
            # Regular text in subsection
            add_formatted_paragraph(doc, item, size=FONT_SIZE_BODY)


def add_image_to_doc(doc, image_path, caption="", md_dir=None):
    """Add an image to the document with optional caption."""
    # Resolve image path relative to the markdown file's directory or IMAGES_DIR
    img = Path(image_path)
    if not img.is_absolute():
        # Try relative to IMAGES_DIR first, then md_dir
        candidates = [IMAGES_DIR / img.name, IMAGES_DIR / image_path]
        if md_dir:
            candidates.insert(0, md_dir / image_path)
        for candidate in candidates:
            if candidate.exists():
                img = candidate
                break

    if not img.exists():
        return  # silently skip missing images

    # Add image centered, max width 14cm (fits A4 with margins)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(str(img), width=Cm(14))

    # Add caption below image
    if caption:
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = cap.add_run(caption)
        run.font.name = FONT_NAME
        run.font.size = FONT_SIZE_SMALL
        run.font.italic = True
        run.font.color.rgb = RGBColor.from_string("666666")
        cap.paragraph_format.space_after = Pt(8)


def process_generic_section(doc, body, md_dir=None):
    """Process a generic section: tables, text, and images."""
    # Process body text and tables
    body_tables = parse_md_tables(body)
    table_idx = 0
    in_table = False

    for line in body.split("\n"):
        stripped = line.strip()

        if stripped.startswith("|"):
            if not in_table:
                in_table = True
                if table_idx < len(body_tables):
                    h, r = body_tables[table_idx]
                    # Filter out separator rows
                    filtered_rows = [
                        row for row in r
                        if not all(re.match(r"^[-:]+$", c) for c in row if c)
                    ]
                    create_data_table(doc, h, filtered_rows)
                    table_idx += 1
            continue
        else:
            in_table = False

        # Skip Obsidian links and contact hour references
        if stripped.startswith("[[") or stripped.startswith("**Contact hour:**"):
            continue

        # Handle markdown images: ![caption](path)
        img_match = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", stripped)
        if img_match:
            caption = img_match.group(1)
            img_path = img_match.group(2)
            add_image_to_doc(doc, img_path, caption, md_dir)
            continue

        if stripped.startswith("**") and stripped.endswith("**"):
            add_formatted_paragraph(
                doc, stripped.strip("*"),
                bold=True, size=FONT_SIZE_BODY
            )
        elif stripped.startswith("---"):
            continue
        elif stripped.startswith("*") and stripped.endswith("*"):
            p = doc.add_paragraph()
            run = p.add_run(stripped.strip("*"))
            run.font.name = FONT_NAME
            run.font.size = FONT_SIZE_BODY
            run.font.italic = True
        elif stripped and not stripped.startswith("#") and not stripped.startswith("[["):
            add_formatted_paragraph(doc, stripped, size=FONT_SIZE_BODY)


def process_cocu_file(doc, md_path, level_info, cocu_num, total_cocu):
    """Process a single CoCu .md file and add it to the document."""
    text = md_path.read_text(encoding="utf-8")
    title = extract_title_from_md(text)

    # Extract work activities from the NOSS header table in the .md
    work_activities = ""
    tables = parse_md_tables(text)
    for headers, rows in tables:
        for row in rows:
            if any("WORK ACTIVITY" in str(c).upper() for c in row):
                for c in row:
                    if "WORK ACTIVITY" not in str(c).upper() and len(str(c)) > 10:
                        work_activities = str(c)
                        break

    # Add chapter heading with accent
    cocu_display = title.split(":", 1)[-1].strip() if ":" in title else title
    add_section_heading(doc, f"CoCu {cocu_num}: {cocu_display}", level=1)
    doc.add_paragraph()  # small gap

    # Add NOSS header table
    cocu_title = title.split(":", 1)[-1].strip() if ":" in title else title
    cocu_title = re.sub(r"^CoCu\s*\d+\s*:\s*", "", cocu_title).strip()
    # Also strip the hours suffix like "(300 hrs)"
    cocu_title = re.sub(r"\s*\(\d+\s*hrs?\)\s*$", "", cocu_title).strip()

    create_noss_header_table(
        doc, level_info, cocu_num, cocu_title,
        work_activities or "See work activities below",
        total_cocu
    )

    # Process each section and table
    md_dir = md_path.parent
    sections = parse_md_sections(text)
    for heading, body in sections:
        if not heading and not body.strip():
            continue

        # For the title section, skip the heading (already added above) but process the body
        if heading and heading == extract_title_from_md(text):
            process_generic_section(doc, body, md_dir)
            continue

        # Add section heading if present
        if heading:
            heading_lower = heading.lower()
            add_section_heading(doc, heading, level=2)

            # Route to specialized handlers for known section types
            if "practical exercises" in heading_lower:
                process_practical_exercises_section(doc, body)
            elif "references" in heading_lower:
                process_references_section(doc, body)
            elif "learning outcome matrix" in heading_lower:
                process_generic_section(doc, body, md_dir)
            else:
                process_generic_section(doc, body, md_dir)
        else:
            process_generic_section(doc, body, md_dir)

    # Page break after each CoCu
    doc.add_page_break()


def process_contact_hour_file(doc, md_path, level_info):
    """Process the contact hour distribution file."""
    text = md_path.read_text(encoding="utf-8")

    add_section_heading(doc, "CONTACT HOUR DISTRIBUTION", level=1)
    doc.add_paragraph()

    # Add program info
    add_formatted_paragraph(
        doc,
        f"Program: {level_info['code']} {level_info['title_en']} ({level_info['title_bm']})",
        bold=True, size=FONT_SIZE_BODY,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        color=COLOR_HEADING_ACCENT
    )
    add_formatted_paragraph(
        doc, f"Level: {level_info['level']}",
        bold=True, size=FONT_SIZE_BODY,
        alignment=WD_ALIGN_PARAGRAPH.CENTER,
        space_after=Pt(12),
        color=COLOR_HEADING_ACCENT
    )

    # Parse and add all tables
    tables = parse_md_tables(text)
    for headers, rows in tables:
        filtered_rows = [
            row for row in rows
            if not all(re.match(r"^[-:]+$", c) for c in row if c)
        ]
        if filtered_rows:
            create_data_table(doc, headers, filtered_rows)

    doc.add_page_break()


def process_standard_practice_file(doc, md_path, level_info):
    """Process the standard practice file."""
    text = md_path.read_text(encoding="utf-8")

    add_section_heading(doc, "STANDARD PRACTICE", level=1)
    doc.add_paragraph()

    sections = parse_md_sections(text)
    for heading, body in sections:
        if heading:
            add_section_heading(doc, heading, level=2)

        tables = parse_md_tables(body)
        table_idx = 0
        in_table = False

        for line in body.split("\n"):
            stripped = line.strip()
            if stripped.startswith("|"):
                if not in_table:
                    in_table = True
                    if table_idx < len(tables):
                        h, r = tables[table_idx]
                        create_data_table(doc, h, r)
                        table_idx += 1
                continue
            else:
                in_table = False

            if stripped and not stripped.startswith("---") and not stripped.startswith("[["):
                if stripped.startswith("**"):
                    add_formatted_paragraph(doc, stripped.strip("*"), bold=True, size=FONT_SIZE_BODY)
                else:
                    add_formatted_paragraph(doc, stripped, size=FONT_SIZE_BODY)

    doc.add_page_break()


def setup_document():
    """Create a new document with A4 page layout and default styles."""
    doc = Document()

    # Set A4 page size
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)
    section.top_margin = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.header_distance = Cm(1.0)
    section.footer_distance = Cm(1.0)

    # Set default font
    style = doc.styles["Normal"]
    font = style.font
    font.name = FONT_NAME
    font.size = FONT_SIZE_BODY

    # Set default paragraph spacing
    pf = style.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after = Pt(4)

    return doc


def generate_level(level_num):
    """Generate .docx for a single level."""
    level_info = LEVELS[str(level_num)]
    content_dir = CONTENT_DIR / f"IT-020-{level_num}"

    if not content_dir.exists():
        print(f"  [SKIP] Content directory not found: {content_dir}")
        return None

    # Collect .md files
    md_files = sorted(content_dir.glob("*.md"))
    if not md_files:
        print(f"  [SKIP] No .md files in {content_dir}")
        return None

    # Separate file types
    contact_hour_files = [f for f in md_files if "contact" in f.name.lower()]
    sp_files = [f for f in md_files if "standard-practice" in f.name.lower()]
    cocu_files = [f for f in md_files if f.name[:2].isdigit() and "cocu" in f.name.lower()]
    cocu_files = sorted(cocu_files)

    total_cocu = len(cocu_files)

    print(f"  Found: {len(contact_hour_files)} contact-hr, {len(sp_files)} SP, {total_cocu} CoCu files")

    # Create document
    doc = setup_document()

    # Cover page
    add_cover_page(doc, level_info)

    # Table of contents
    toc_entries = []
    for f in sp_files:
        toc_entries.append((f.name, "Standard Practice"))
    for f in contact_hour_files:
        toc_entries.append((f.name, "Contact Hour Distribution"))
    for f in cocu_files:
        title = extract_title_from_md(f.read_text(encoding="utf-8"))
        toc_entries.append((f.name, title))
    add_table_of_contents(doc, toc_entries, level_info)

    # Standard Practice
    for sp_file in sp_files:
        print(f"  Processing SP: {sp_file.name}")
        process_standard_practice_file(doc, sp_file, level_info)

    # Contact Hour Distribution
    for ch_file in contact_hour_files:
        print(f"  Processing contact hours: {ch_file.name}")
        process_contact_hour_file(doc, ch_file, level_info)

    # CoCu chapters
    for i, cocu_file in enumerate(cocu_files, 1):
        print(f"  Processing CoCu {i}/{total_cocu}: {cocu_file.name}")
        process_cocu_file(doc, cocu_file, level_info, i, total_cocu)

    # Add headers/footers
    add_page_header_footer(doc, level_info)

    # Save
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / level_info["filename"]
    doc.save(str(output_path))
    print(f"  Saved: {output_path}")
    return output_path


def main():
    """Main entry point."""
    # Parse args
    level_arg = "all"
    if len(sys.argv) > 1:
        if sys.argv[1] == "--level" and len(sys.argv) > 2:
            level_arg = sys.argv[2]
        else:
            level_arg = sys.argv[1]

    levels_to_generate = ["3", "4", "5"] if level_arg == "all" else [level_arg]

    print(f"NOSS IT-020 Textbook Generator")
    print(f"Generating levels: {', '.join(levels_to_generate)}")
    print(f"Content dir: {CONTENT_DIR}")
    print(f"Output dir: {OUTPUT_DIR}")
    print()

    generated = []
    for level in levels_to_generate:
        if level not in LEVELS:
            print(f"[ERROR] Unknown level: {level}")
            continue

        print(f"[L{level}] Generating {LEVELS[level]['title_en']}...")
        path = generate_level(level)
        if path:
            generated.append((level, path))
            print(f"[L{level}] Done.\n")
        else:
            print(f"[L{level}] Skipped.\n")

    # Summary
    print("=" * 60)
    print(f"Generated {len(generated)} textbook(s):")
    for level, path in generated:
        size_kb = path.stat().st_size / 1024
        print(f"  L{level}: {path.name} ({size_kb:.1f} KB)")

    # Update gdrive state
    if GDRIVE_STATE.exists():
        state = json.loads(GDRIVE_STATE.read_text(encoding="utf-8"))
        state["last_build"] = datetime.now().isoformat()
        state["generated_files"] = {
            f"IT-020-{level}": str(path) for level, path in generated
        }
        GDRIVE_STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
