"""Render a PPT-PPA markdown paper to a JPK-format .docx.

Why this exists rather than reusing `build/wim_md_to_docx.py`:

That script renders **WIM teaching materials** and hands pandoc
`build/_templates/reference-textbook.docx`, whose `Normal` style is
*Source Serif 4, justified*. Two consequences on the reviewer's machine:

  * Source Serif 4 is not installed on macOS, so Word substitutes a fallback —
    which is why Jennifer's screenshots of 2026-08-24 show typewriter-looking
    text where the source says nothing of the sort.
  * Justified alignment on short lines opens the word gaps she described as
    "跳来跳去…看了觉得很晕".

And pandoc emits tables in the borderless `Table` style, so every table in the
paper printed as bare columns of text. She asked for "画线的表格" — ruled tables.

So: Arial (present on every Windows and macOS install), left-aligned, and a hard
pass that puts real borders on every table in the document. Nothing here is
decorative; each choice traces to a defect that was reported.

Usage:
    uv run --with python-docx python -m _engine.render.ppa_docx \
        output/jennifer-ppa-soalan/fb-018-3-set-b-soalan.md \
        --output output/jennifer-ppa-soalan/docx/fb-018-3-set-b-soalan.docx
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parents[2]
REFERENCE_DOC = ROOT / "_engine" / "render" / "_reference-ppa.docx"
LOGO = ROOT / "aesthetic-services" / "_assets" / "logos" / "jpk-logo.png"

BODY_FONT = "Arial"
BODY_SIZE = Pt(11)
HEADER_FILL = "D9D9D9"


# --------------------------------------------------------------------------- #
# Reference document
# --------------------------------------------------------------------------- #

def build_reference(dest: Path = REFERENCE_DOC) -> Path:
    """Create the pandoc `--reference-doc` this renderer needs.

    Regenerated on demand rather than committed as a binary: the style decisions
    are then reviewable as code instead of hidden inside a .docx.
    """
    doc = Document()

    for section in doc.sections:
        section.page_width, section.page_height = Cm(21.0), Cm(29.7)
        section.top_margin = section.bottom_margin = Cm(2.5)
        section.left_margin = section.right_margin = Cm(2.5)

    normal = doc.styles["Normal"]
    normal.font.name = BODY_FONT
    normal.font.size = BODY_SIZE
    normal.font.color.rgb = RGBColor(0, 0, 0)
    _force_font(normal.element, BODY_FONT)
    pf = normal.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT      # never JUSTIFY — see module docstring
    pf.space_after = Pt(6)
    pf.line_spacing = 1.15

    for name, size, bold in (("Heading 1", 14, True),
                             ("Heading 2", 13, True),
                             ("Heading 3", 12, True),
                             ("Heading 4", 11, True)):
        try:
            st = doc.styles[name]
        except KeyError:
            continue
        st.font.name = BODY_FONT
        st.font.size = Pt(size)
        st.font.bold = bold
        st.font.color.rgb = RGBColor(0, 0, 0)   # not Word's default blue
        _force_font(st.element, BODY_FONT)
        st.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        st.paragraph_format.space_before = Pt(12)
        st.paragraph_format.space_after = Pt(6)

    dest.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(dest))
    return dest


def _force_font(style_element, font_name: str) -> None:
    """python-docx sets only `w:ascii`; East Asian and complex-script runs ignore it."""
    rpr = style_element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), font_name)


# --------------------------------------------------------------------------- #
# Post-processing
# --------------------------------------------------------------------------- #

def rule_all_tables(doc: Document) -> int:
    """Put a visible single border on every cell of every table.

    Setting `table.style = 'Table Grid'` is not enough: pandoc's tables carry
    direct `tblBorders` formatting of `none`, which wins over the style. The
    borders have to be written onto the table properties directly.
    """
    n = 0
    for table in doc.tables:
        tbl_pr = table._tbl.tblPr
        for old in tbl_pr.findall(qn("w:tblBorders")):
            tbl_pr.remove(old)
        borders = OxmlElement("w:tblBorders")
        for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
            el = OxmlElement(f"w:{side}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "8")          # 8 eighths of a point = 1pt
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), "000000")
            borders.append(el)
        tbl_pr.append(borders)

        table.alignment = WD_TABLE_ALIGNMENT.LEFT
        size_columns(table)
        _shade_header_row(table)
        _repeat_header_row(table)
        for row in table.rows:
            _keep_row_together(row)
            for cell in row.cells:
                _pad_cell(cell)
                for para in cell.paragraphs:
                    para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
                    para.paragraph_format.space_after = Pt(2)
        n += 1
    return n


def _is_header_row(row) -> bool:
    """Decide whether row 0 is a column heading or just the first data row.

    Markdown tables written headerless (`| | |` above the rule) lose that fact in
    pandoc's docx output — the empty row is dropped and the first *data* row
    becomes row 0. Shading it turns a candidate-details form into something that
    looks like a table heading: on the FB-018-3 cover, `NAMA CALON` came out grey
    and bold as if it were a column title.

    A heading never contains a fill-in blank and never contains an empty cell.
    """
    texts = [c.text.strip() for c in row.cells]
    if any(not t for t in texts):
        return False
    if any(re.search(r"_{5,}", t) for t in texts):
        return False
    # The cover table's first row is the crest beside the JPK address, not a
    # column heading. Shading it would grey out the masthead.
    if any(LOGO_TOKEN in t for t in texts):
        return False
    return True


def _shade_header_row(table) -> None:
    if not table.rows or not _is_header_row(table.rows[0]):
        return
    for cell in table.rows[0].cells:
        tc_pr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), HEADER_FILL)
        tc_pr.append(shd)
        for para in cell.paragraphs:
            for run in para.runs:
                run.bold = True


def size_columns(table, page_width_cm: float = 16.0) -> None:
    """Give each column a width proportional to how much text it holds.

    Word's default is to split evenly, which is why a `NO.` column holding single
    digits ends up as wide as a column of full sentences — and then the header
    "NO." wraps to three lines reading "N / O / .", and a 13-row checklist that
    belongs on one page spills onto two.

    Square-root normalisation rather than raw length: a column with 40-character
    cells needs more room than one with 4-character cells, but not ten times more.
    """
    import math

    cols = len(table.columns)
    if cols <= 1:
        return
    page_width = Cm(page_width_cm)
    lengths = [0] * cols
    # A column can never be narrower than its longest unbreakable word, or Word
    # breaks mid-word: a "NO." heading came out stacked as "N / O / ." and
    # "RATIO (P:C)" as "RATI / O / (P:C)".
    longest_word = [0] * cols
    for row in table.rows:
        # A row marked for spanning gets merged across every column later, so its
        # text says nothing about how wide column 1 should be. Measuring it made
        # column 1 enormous and squeezed the rest — a 13-row form that fitted on
        # one page spilled onto two once a spanned sign-off row was added.
        if SPAN_TOKEN in row.cells[0].text:
            continue
        for i, cell in enumerate(row.cells[:cols]):
            text = cell.text.strip()
            lengths[i] = max(lengths[i], len(text))
            for word in text.split():
                longest_word[i] = max(longest_word[i], len(word))

    # Arial 10pt averages ~0.19 cm per character; cell margins add ~0.28 cm.
    floors = [max(int(Cm(0.19 * w + 0.32)), int(Cm(0.9))) for w in longest_word]

    roots = [math.sqrt(max(n, 2)) for n in lengths]
    total = sum(roots) or 1
    widths = [max(int(page_width * r / total), floors[i])
              for i, r in enumerate(roots)]
    if sum(widths) > int(page_width):
        # Shrink only what is above its floor, so the tight columns stay legible.
        excess = sum(widths) - int(page_width)
        slack = [w - floors[i] for i, w in enumerate(widths)]
        pool = sum(s for s in slack if s > 0)
        if pool > 0:
            widths = [w - int(excess * max(slack[i], 0) / pool)
                      for i, w in enumerate(widths)]

    # Setting cell.width alone is not enough. Word lays the table out from the
    # `w:tblGrid` pandoc emitted and from `w:tblLayout`; unless the layout is
    # pinned to fixed and the grid rewritten, the per-cell widths are advisory and
    # get ignored — which is why an earlier attempt at this changed nothing on the
    # rendered page.
    table.autofit = False
    tbl_pr = table._tbl.tblPr
    for old in tbl_pr.findall(qn("w:tblLayout")):
        tbl_pr.remove(old)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tbl_pr.append(layout)

    grid = table._tbl.find(qn("w:tblGrid"))
    if grid is not None:
        table._tbl.remove(grid)
    grid = OxmlElement("w:tblGrid")
    for w in widths:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(int(w / 635)))      # EMU → twips
        grid.append(col)
    table._tbl.insert(list(table._tbl).index(tbl_pr) + 1, grid)

    for i, column in enumerate(table.columns):
        for cell in column.cells:
            cell.width = widths[i]


def _repeat_header_row(table) -> None:
    """Repeat the header on every page a table spills onto.

    A continuation page whose columns have no headings is exactly the "看不懂"
    complaint: the reader has to page backwards to find out what column three is.
    """
    if not table.rows:
        return
    tr_pr = table.rows[0]._tr.get_or_add_trPr()
    if tr_pr.find(qn("w:tblHeader")) is None:
        el = OxmlElement("w:tblHeader")
        el.set(qn("w:val"), "true")
        tr_pr.append(el)


def _keep_row_together(row) -> None:
    """Stop Word breaking a single row across a page boundary."""
    tr_pr = row._tr.get_or_add_trPr()
    if tr_pr.find(qn("w:cantSplit")) is None:
        tr_pr.append(OxmlElement("w:cantSplit"))


def _pad_cell(cell) -> None:
    """Without margins the text sits flush against the rule and reads as cramped."""
    tc_pr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for side, twips in (("top", "60"), ("start", "80"),
                        ("bottom", "60"), ("end", "80")):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), twips)
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tc_pr.append(mar)


LOGO_TOKEN = "⟪LOGO⟫"

# A pipe-table cell is one line of markdown, so there is no way to write a line
# break inside it. `<br>` does not survive pandoc's docx writer — it is dropped
# silently, which welds words together ("KEMAHIRANKEMENTERIAN SUMBER MANUSIAARAS").
# This sentinel passes through as plain text and is turned into a real `w:br`
# afterwards, which keeps each run's bold intact — needed on the cover, where the
# three practically-assessed units are bold and the other three are not.
BREAK_TOKEN = "⏎"

# Markdown pipe tables cannot merge cells, but the JPK cover has one row — the
# paper's own title — spanning the full width and centred. Prefixing that cell
# with this token asks the renderer to merge the row and centre it.
SPAN_TOKEN = "⟪SPAN⟫"


def apply_row_spans(doc: Document) -> int:
    """Merge and centre any table row whose first cell starts with SPAN_TOKEN."""
    n = 0
    for table in doc.tables:
        for row in table.rows:
            cells = row.cells
            if len(cells) < 2 or SPAN_TOKEN not in cells[0].text:
                continue
            for para in cells[0].paragraphs:
                for run in para.runs:
                    run.text = run.text.replace(SPAN_TOKEN, "")
            merged = cells[0]
            for other in cells[1:]:
                merged = merged.merge(other)
            for para in merged.paragraphs:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            n += 1
    return n


def apply_line_breaks(doc: Document) -> int:
    """Replace every BREAK_TOKEN with a Word line break, run by run."""
    n = 0

    def walk(paragraphs):
        nonlocal n
        for para in paragraphs:
            for run in para.runs:
                if BREAK_TOKEN not in run.text:
                    continue
                parts = run.text.split(BREAK_TOKEN)
                run.text = parts[0]
                for part in parts[1:]:
                    run._r.append(OxmlElement("w:br"))
                    t = OxmlElement("w:t")
                    t.set(qn("xml:space"), "preserve")
                    t.text = part
                    run._r.append(t)
                    n += 1

    walk(doc.paragraphs)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                walk(cell.paragraphs)
    return n


def insert_logo(doc: Document, logo: Path = LOGO) -> str:
    """Place the Jata Negara crest where the JPK cover puts it.

    Jennifer, 2026-08-24: "一定要有政府Logo". Her own papers do not float the crest
    above the page — it sits **inside the top-left cell of the cover table**, with
    the JPK Putrajaya address in the cell beside it. Reproducing that means the
    markdown carries a ⟪LOGO⟫ token in that cell and this swaps the token for the
    image.

    Returns "cell" when the token was found and replaced, "top" when it fell back
    to a centred paragraph above the body, or "missing" when the asset is absent.
    """
    if not logo.exists():
        return "missing"

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                if LOGO_TOKEN not in cell.text:
                    continue
                for para in list(cell.paragraphs):
                    if LOGO_TOKEN in para.text:
                        for run in list(para.runs):
                            run._r.getparent().remove(run._r)
                        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        para.paragraph_format.space_before = Pt(4)
                        para.paragraph_format.space_after = Pt(4)
                        para.add_run().add_picture(str(logo), height=Cm(2.0))
                        return "cell"

    # No token, no crest. Not every document in the set carries one — the JPK
    # equipment-verification form (JPK/PPA-PPT/SP/1:2022) has only its form number
    # in the top-right corner. An earlier version floated the crest above any
    # document that lacked the token, which put it on a form that should not have
    # had it.
    return "none"


def add_running_heads(doc: Document, reference_code: str = "") -> None:
    """Reference code top right, page number bottom centre — the JPK arrangement.

    Verified against `raw/jennifer-authoritative-fb018-3/jen-soalan-setA.pdf`,
    where every page carries `FB-018-3:2012/2026/A/01` in the top-right corner and
    a bare page number centred at the foot. An earlier version of this renderer
    put both in the footer, which is not the format.
    """
    for section in doc.sections:
        if reference_code:
            header = section.header
            para = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
            para.text = ""
            para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            run = para.add_run(reference_code)
            run.bold = True
            run.font.size = Pt(9)
            run.font.name = BODY_FONT
            _force_run_font(run)

        footer = section.footer
        para = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        para.text = ""
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        _add_field(para, "PAGE")


def _add_field(paragraph, instr: str) -> None:
    run = paragraph.add_run()
    run.font.size = Pt(9)
    run.font.name = BODY_FONT
    begin = OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"), "begin")
    text = OxmlElement("w:instrText"); text.set(qn("xml:space"), "preserve")
    text.text = f" {instr} "
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end")
    for el in (begin, text, end):
        run._r.append(el)


def strip_inline_reference_codes(doc: Document, reference_code: str) -> int:
    """Delete body paragraphs that are nothing but the paper reference code.

    The code belongs in the page header, where `add_running_heads` puts it. The
    markdown carries it so the renderer can find it, and authors tend to repeat it
    at section breaks — which then renders as a stray bold line mid-page.
    """
    if not reference_code:
        return 0
    n = 0
    for para in list(doc.paragraphs):
        if para.text.strip().strip("*").strip() == reference_code:
            para._p.getparent().remove(para._p)
            n += 1
    return n


def normalise_paragraphs(doc: Document, table_font_pt: float = 10) -> None:
    """Left-align everything and pin the font, including runs pandoc styled itself.

    `table_font_pt` is a deliberate knob rather than something inferred. The JPK
    equipment-verification form is a single page by design; at 10pt its thirteen
    rows spill onto a second. Rather than have the renderer guess when to shrink,
    the caller says so.
    """
    for para in doc.paragraphs:
        if para.paragraph_format.alignment == WD_ALIGN_PARAGRAPH.JUSTIFY:
            para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        for run in para.runs:
            run.font.name = BODY_FONT
            _force_run_font(run)
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    para.paragraph_format.space_before = Pt(0)
                    para.paragraph_format.space_after = Pt(1)
                    para.paragraph_format.line_spacing = 1.0
                    for run in para.runs:
                        run.font.name = BODY_FONT
                        run.font.size = Pt(table_font_pt)
                        _force_run_font(run)


def _force_run_font(run) -> None:
    rpr = run._r.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), BODY_FONT)


# --------------------------------------------------------------------------- #

def set_margins(doc: Document, cm: float) -> None:
    """Override the 2.5 cm page margins.

    The JPK equipment-verification form is one page by design. At 2.5 cm all
    round, 5 cm of the height is margin and the signature block is pushed onto a
    second page on its own — which reads as a printing error on a form an officer
    signs. Narrowing the margins is the honest fix; shrinking the type further
    would make the checklist hard to read in the room.
    """
    for section in doc.sections:
        section.top_margin = section.bottom_margin = Cm(cm)
        section.left_margin = section.right_margin = Cm(cm)


def render(md: Path, out: Path, reference_code: str = "", logo: bool = True,
           table_font_pt: float = 10, margin_cm: float | None = None) -> dict:
    if not REFERENCE_DOC.exists():
        build_reference()

    out.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        "pandoc", str(md), "-o", str(out),
        "--from", "markdown+raw_html+smart+pipe_tables",
        "--to", "docx",
        "--wrap=none",
        "--reference-doc", str(REFERENCE_DOC),
        "--resource-path", str(ROOT),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"pandoc failed for {md.name}:\n{r.stderr}")

    doc = Document(str(out))
    if margin_cm is not None:
        set_margins(doc, margin_cm)
    normalise_paragraphs(doc, table_font_pt)
    breaks = apply_line_breaks(doc)
    tables = rule_all_tables(doc)
    # After rule_all_tables, which left-aligns every cell — a spanned title row is
    # centred, so it has to be applied last or the alignment is overwritten.
    spans = apply_row_spans(doc)
    logo_where = insert_logo(doc) if logo else "skipped"
    stripped = strip_inline_reference_codes(doc, reference_code)
    add_running_heads(doc, reference_code)
    doc.save(str(out))
    return {"tables_ruled": tables, "logo": logo_where, "breaks": breaks,
            "spans": spans, "refcodes_stripped": stripped, "output": str(out)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", nargs="*", help="input .md file(s)")
    ap.add_argument("--output", help="output .docx (only valid with one input)")
    ap.add_argument("--outdir", help="output directory for multiple inputs")
    ap.add_argument("--ref-code", default="", help="paper reference code for the footer")
    ap.add_argument("--no-logo", action="store_true")
    ap.add_argument("--table-font-pt", type=float, default=10,
                    help="table body font size; 9 fits the single-page JPK forms")
    ap.add_argument("--margin-cm", type=float, default=None,
                    help="override page margins; 1.8 keeps the JPK equipment form to one page")
    ap.add_argument("--rebuild-reference", action="store_true",
                    help="regenerate _reference-ppa.docx and exit")
    args = ap.parse_args()

    if args.rebuild_reference:
        print(f"wrote {build_reference()}")
        return

    inputs = [Path(p) for p in args.input]
    if args.output and len(inputs) > 1:
        sys.exit("--output takes a single input; use --outdir for several")

    for md in inputs:
        out = (Path(args.output) if args.output
               else Path(args.outdir or md.parent / "docx") / f"{md.stem}.docx")
        info = render(md, out, args.ref_code, logo=not args.no_logo,
                      table_font_pt=args.table_font_pt,
                      margin_cm=args.margin_cm)
        print(f"OK  {md.name} -> {Path(info['output']).name}  "
              f"({info['tables_ruled']} tables ruled, logo={info['logo']})")


if __name__ == "__main__":
    main()
