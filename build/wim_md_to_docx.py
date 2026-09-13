"""WIM Markdown to DOCX export pipeline with JPK format compliance.

Usage:
    uv run python build/wim_md_to_docx.py <input.md> --style KP --output out.docx

Requires: python-docx, pandoc (in PATH)
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Pt, RGBColor, Cm

ROOT = Path(__file__).resolve().parent.parent
REFERENCE_DOC = ROOT / "build" / "_templates" / "reference-textbook.docx"
LUA_FILTER = ROOT / "build" / "filters" / "callouts.lua"

# Paper color map for --style flag (RGB approximations)
PAPER_COLORS: dict[str, RGBColor | None] = {
    "KP": None,                          # White (default)
    "KT": RGBColor(0xFF, 0xC0, 0xCB),   # Pink
    "KK": RGBColor(0xAD, 0xD8, 0xE6),   # Blue
    "PA": RGBColor(0xB0, 0xD0, 0xE8),   # Light blue
    "KA": RGBColor(0xFF, 0xC0, 0xCB),   # Pink (same as KT)
    "PM": RGBColor(0xFF, 0xFF, 0xA0),   # Yellow
}

DOC_TYPE_LABELS: dict[str, str] = {
    "KP": "KERTAS PENERANGAN / INFORMATION SHEET",
    "KT": "KERTAS TUGASAN / ASSIGNMENT SHEET",
    "KK": "KERTAS KERJA / WORK SHEET",
    "PA": "PENILAIAN PRESTASI / PERFORMANCE ASSESSMENT",
    "KA": "PENILAIAN PENGETAHUAN / KNOWLEDGE ASSESSMENT",
    "PM": "PELAN MENGAJAR / LESSON PLAN",
}


def parse_wim_metadata(md_path: Path) -> dict[str, str]:
    """Extract WIM Code, CU, and document type from markdown content and file path."""
    text = md_path.read_text(encoding="utf-8")

    # Try extracting from **Kod WIM / WIM Code:** line
    wim_code_match = re.search(r"\*\*Kod WIM.*?\*\*[:\s]+([^\n]+)", text)
    wim_code = wim_code_match.group(1).strip() if wim_code_match else ""

    # Derive from file path: e.g. bev-diagnostic-rectification/C01/KP-01.md
    parts = md_path.parts
    cu = ""
    doc_type = ""
    for part in parts:
        if re.match(r"^C\d+$", part, re.IGNORECASE):
            cu = part.upper()
        stem = md_path.stem  # e.g. KP-01
        dt_match = re.match(r"^(KP|KT|KK|PA|KA|PM)", stem, re.IGNORECASE)
        if dt_match:
            doc_type = dt_match.group(1).upper()

    # Parse NOSS code from WIM code or derive from path
    noss_code = ""
    if wim_code:
        noss_match = re.match(r"([A-Z]\d{3}-\d{3}-\d:\d{4})", wim_code)
        if noss_match:
            noss_code = noss_match.group(1)

    if not noss_code:
        # Infer from folder name
        folder = parts[-3] if len(parts) >= 3 else ""
        if "bev" in folder.lower():
            noss_code = "G452-010-3:2023"
        elif "aesthetic" in folder.lower():
            noss_code = "S960-002-3:2020"
        elif "it-computer" in folder.lower():
            noss_code = "IT-020-3:2013"

    return {
        "wim_code": wim_code or f"{noss_code}-{cu}/{doc_type}",
        "noss_code": noss_code,
        "cu": cu,
        "doc_type": doc_type,
    }


def add_header_box(doc: Document, meta: dict[str, str], style_key: str) -> None:
    """Insert JPK-format header table at the start of the document."""
    doc_label = DOC_TYPE_LABELS.get(style_key, style_key)

    # Insert header table before all existing paragraphs
    table = doc.add_table(rows=2, cols=3)
    # Add borders to all cells manually (Table Grid style may not exist in pandoc output)
    for row in table.rows:
        for cell in row.cells:
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcBorders = OxmlElement("w:tcBorders")
            for side in ("top", "left", "bottom", "right"):
                border = OxmlElement(f"w:{side}")
                border.set(qn("w:val"), "single")
                border.set(qn("w:sz"), "4")
                border.set(qn("w:color"), "000000")
                tcBorders.append(border)
            tcPr.append(tcBorders)

    # Row 0: NOSS Code | Competency Unit | Document Type
    row0 = table.rows[0].cells
    row0[0].text = f"NOSS: {meta['noss_code']}"
    row0[1].text = f"CU: {meta['cu']}"
    row0[2].text = f"Kod: {meta['wim_code']}"

    # Row 1: Document type label spanning all columns
    row1 = table.rows[1].cells
    row1[0].merge(row1[1]).merge(row1[2])
    row1[0].text = doc_label

    # Bold all header cells
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in para.runs:
                    run.bold = True
                    run.font.size = Pt(10)

    # Move the header table to the top of the document body
    body = doc.element.body
    tbl_elem = table._tbl
    body.remove(tbl_elem)
    body.insert(0, tbl_elem)

    # Add a blank paragraph after header
    sep = OxmlElement("w:p")
    body.insert(1, sep)


def fix_paragraph_alignment(doc: Document) -> None:
    """Force LEFT alignment on body paragraphs — pandoc reference-doc may use Justify."""
    for para in doc.paragraphs:
        if para.alignment == WD_ALIGN_PARAGRAPH.JUSTIFY:
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT


def auto_size_tables(doc: Document, page_width_cm: float = 16.0) -> None:
    """Distribute table column widths proportionally (sqrt of max content length).

    Prevents equal-width splitting that causes mid-word wrapping in wide tables.
    Page width defaults to A4 (21cm) minus 2×2.5cm margins = 16cm.
    """
    import math
    page_width = Cm(page_width_cm)
    for table in doc.tables:
        cols = len(table.columns)
        if cols <= 1:
            continue
        # Measure max text length per column (headers + data rows)
        col_lens = [0] * cols
        for row in table.rows:
            for i, cell in enumerate(row.cells[:cols]):
                col_lens[i] = max(col_lens[i], len(cell.text.strip()))
        col_lens = [max(l, 2) for l in col_lens]  # floor: 2-char minimum
        # Square-root normalisation prevents extreme width skew
        sqrts = [math.sqrt(l) for l in col_lens]
        total_sqrt = sum(sqrts) or 1
        # Assign widths; enforce 0.8cm floor per column
        min_w = int(Cm(0.8))
        widths = [max(int(page_width * s / total_sqrt), min_w) for s in sqrts]
        # Scale down if total exceeds page width
        total_w = sum(widths)
        if total_w > int(page_width):
            scale = int(page_width) / total_w
            widths = [max(int(w * scale), min_w) for w in widths]
        # Apply widths to every cell in each column
        for i, col in enumerate(table.columns):
            for cell in col.cells:
                cell.width = widths[i]


def apply_paper_watermark(doc: Document, style_key: str) -> None:
    """Add a shading background to all paragraphs to simulate paper color."""
    color = PAPER_COLORS.get(style_key)
    if color is None:
        return  # White paper — no shading needed

    hex_color = f"{color[0]:02X}{color[1]:02X}{color[2]:02X}"
    for section in doc.sections:
        # Set page background via document settings (word background-color)
        # This applies a section-level fill via XML shading on each paragraph
        pass

    # Apply shading to all paragraphs as a visual approximation
    for para in doc.paragraphs:
        pPr = para._p.get_or_add_pPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), hex_color)
        pPr.append(shd)


def _strip_yaml_frontmatter(md_path: Path) -> Path:
    """If the md starts with `---\n...\n---`, write a stripped copy to a temp file."""
    import tempfile
    text = md_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return md_path
    end = text.find("\n---", 3)
    if end < 0:
        return md_path
    body = text[end + 4:].lstrip("\n")
    tmp = Path(tempfile.mkstemp(suffix=".md")[1])
    tmp.write_text(body, encoding="utf-8")
    return tmp


def convert_md_to_docx(md_path: Path, output_path: Path, style_key: str) -> None:
    """Full pipeline: pandoc conversion + python-docx post-processing."""
    pandoc_exe = "pandoc"

    # Step 1: Convert .md to .docx via pandoc using textbook template
    src = _strip_yaml_frontmatter(md_path)
    cmd = [
        pandoc_exe, str(src),
        "-o", str(output_path),
        "--from", "markdown+raw_html+smart+fenced_divs",
        "--to", "docx",
        "--wrap=none",
        "--resource-path", str(ROOT),
    ]
    if REFERENCE_DOC.exists():
        cmd += ["--reference-doc", str(REFERENCE_DOC)]
    if LUA_FILTER.exists():
        cmd += ["--lua-filter", str(LUA_FILTER)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"pandoc error: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    # Step 2: Post-process with python-docx
    meta = parse_wim_metadata(md_path)
    doc = Document(str(output_path))

    # Fix formatting: force LEFT alignment + proportional table column widths
    fix_paragraph_alignment(doc)
    auto_size_tables(doc)

    # Add JPK header box
    add_header_box(doc, meta, style_key)

    # Apply paper color watermark
    apply_paper_watermark(doc, style_key)

    # Set margins (2.5 cm all sides per JPK standard)
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    doc.save(str(output_path))
    print(f"Exported: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="WIM Markdown to DOCX exporter")
    parser.add_argument("input", help="Input .md file path")
    parser.add_argument("--style", choices=list(PAPER_COLORS.keys()), default="KP",
                        help="WIM document type / paper color style")
    parser.add_argument("--output", default=None, help="Output .docx file path")
    args = parser.parse_args()

    md_path = Path(args.input)
    if not md_path.exists():
        print(f"Error: input file not found: {md_path}", file=sys.stderr)
        sys.exit(1)

    output_path = Path(args.output) if args.output else md_path.with_suffix(".docx")
    convert_md_to_docx(md_path, output_path, args.style)


if __name__ == "__main__":
    main()
