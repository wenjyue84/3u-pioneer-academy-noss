"""Deterministically build `reference-textbook.docx` — the Pandoc reference template.

Run:
    uv run --with python-docx python build/_templates/build-reference-docx.py

Produces `build/_templates/reference-textbook.docx` used by both
`wim_md_to_docx.py` and `wim_consolidate_all.py` via `--reference-doc`.

Fonts are specified with a preferred face + CJK east-asia fallback; if the
preferred face is not installed Word silently substitutes, so we use
Windows-safe defaults (Cambria / Calibri / Consolas / Microsoft YaHei) but
leave Source Serif 4 / Source Sans 3 / Source Han Serif SC / JetBrains Mono
in the font name list as the requested identity.
"""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Mm, Pt, RGBColor, Twips

OUT = Path(__file__).parent / "reference-textbook.docx"

# --- Design tokens -----------------------------------------------------------

ACCENT = "1F3864"      # deep navy — headings
ACCENT_SOFT = "3C5A99"
RULE = "BFBFBF"
BAND = "F2F2F2"        # banded table row fill
HEADER_FILL = "E7E6E6"
CODE_FILL = "F6F8FA"
CODE_BORDER = "D0D7DE"

# Windows-safe typography with requested identity as primary name
FONT_SERIF = "Source Serif 4"       # body text
FONT_SERIF_FB = "Cambria"           # Windows fallback
FONT_SANS = "Source Sans 3"         # headings
FONT_SANS_FB = "Calibri"
FONT_MONO = "JetBrains Mono"
FONT_MONO_FB = "Consolas"
FONT_CJK = "Source Han Serif SC"    # Chinese
FONT_CJK_FB = "Microsoft YaHei"

# --- Helpers -----------------------------------------------------------------

def _set_font(run_or_rpr, ascii_name, cjk_name=None, hint="default"):
    """Set w:rFonts with ascii + eastAsia + hAnsi."""
    rpr = run_or_rpr
    rFonts = rpr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rpr.insert(0, rFonts)
    rFonts.set(qn("w:ascii"), ascii_name)
    rFonts.set(qn("w:hAnsi"), ascii_name)
    rFonts.set(qn("w:cs"), ascii_name)
    if cjk_name:
        rFonts.set(qn("w:eastAsia"), cjk_name)
    rFonts.set(qn("w:hint"), hint)


def _style_rpr(style):
    """Return (creating if needed) the <w:rPr> of a style element."""
    s = style.element
    rpr = s.find(qn("w:rPr"))
    if rpr is None:
        rpr = OxmlElement("w:rPr")
        s.append(rpr)
    return rpr


def _style_ppr(style):
    s = style.element
    ppr = s.find(qn("w:pPr"))
    if ppr is None:
        ppr = OxmlElement("w:pPr")
        # pPr must precede rPr
        rpr = s.find(qn("w:rPr"))
        if rpr is not None:
            s.insert(list(s).index(rpr), ppr)
        else:
            s.append(ppr)
    return ppr


def _set_color(rpr, hex_color):
    color = rpr.find(qn("w:color"))
    if color is None:
        color = OxmlElement("w:color")
        rpr.append(color)
    color.set(qn("w:val"), hex_color)


def _set_size(rpr, pt):
    sz = rpr.find(qn("w:sz"))
    if sz is None:
        sz = OxmlElement("w:sz")
        rpr.append(sz)
    sz.set(qn("w:val"), str(int(pt * 2)))
    szCs = rpr.find(qn("w:szCs"))
    if szCs is None:
        szCs = OxmlElement("w:szCs")
        rpr.append(szCs)
    szCs.set(qn("w:val"), str(int(pt * 2)))


def _set_bold(rpr, bold=True):
    b = rpr.find(qn("w:b"))
    if b is None and bold:
        rpr.append(OxmlElement("w:b"))
    elif b is not None and not bold:
        rpr.remove(b)


def _set_italic(rpr, italic=True):
    i = rpr.find(qn("w:i"))
    if i is None and italic:
        rpr.append(OxmlElement("w:i"))


def _set_smallcaps(rpr):
    sc = OxmlElement("w:smallCaps")
    sc.set(qn("w:val"), "1")
    rpr.append(sc)


def _add_border(parent, side, size_eighths=8, color="auto", space=4):
    pbdr = parent.find(qn("w:pBdr"))
    if pbdr is None:
        pbdr = OxmlElement("w:pBdr")
        parent.append(pbdr)
    b = OxmlElement(f"w:{side}")
    b.set(qn("w:val"), "single")
    b.set(qn("w:sz"), str(size_eighths))
    b.set(qn("w:space"), str(space))
    b.set(qn("w:color"), color)
    pbdr.append(b)


def _set_shading(parent, fill):
    shd = parent.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        parent.append(shd)
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)


def _set_spacing(ppr, before=None, after=None, line=None, line_rule="auto"):
    spacing = ppr.find(qn("w:spacing"))
    if spacing is None:
        spacing = OxmlElement("w:spacing")
        ppr.append(spacing)
    if before is not None:
        spacing.set(qn("w:before"), str(int(before * 20)))  # pt → twips
    if after is not None:
        spacing.set(qn("w:after"), str(int(after * 20)))
    if line is not None:
        spacing.set(qn("w:line"), str(int(line * 240)))  # 1.0 = 240
        spacing.set(qn("w:lineRule"), line_rule)


def _set_indent(ppr, first_line_mm=None, left_mm=None):
    ind = ppr.find(qn("w:ind"))
    if ind is None:
        ind = OxmlElement("w:ind")
        ppr.append(ind)
    if first_line_mm is not None:
        ind.set(qn("w:firstLine"), str(int(first_line_mm * 56.69)))  # mm → twips
    if left_mm is not None:
        ind.set(qn("w:left"), str(int(left_mm * 56.69)))


def _set_keep_with_next(ppr):
    if ppr.find(qn("w:keepNext")) is None:
        ppr.append(OxmlElement("w:keepNext"))


def _set_page_break_before(ppr):
    if ppr.find(qn("w:pageBreakBefore")) is None:
        ppr.append(OxmlElement("w:pageBreakBefore"))


def _set_alignment(ppr, val):
    jc = ppr.find(qn("w:jc"))
    if jc is None:
        jc = OxmlElement("w:jc")
        ppr.append(jc)
    jc.set(qn("w:val"), val)


# --- Main --------------------------------------------------------------------

def build():
    doc = Document()
    styles = doc.styles

    # --- Normal: body text --------------------------------------------------
    normal = styles["Normal"]
    n_rpr = _style_rpr(normal)
    _set_font(n_rpr, FONT_SERIF, FONT_CJK)
    _set_size(n_rpr, 10.5)
    n_ppr = _style_ppr(normal)
    _set_spacing(n_ppr, before=0, after=0, line=1.3)
    _set_alignment(n_ppr, "both")        # justified
    _set_indent(n_ppr, first_line_mm=5)

    # --- Body First: first paragraph after heading (no first-line indent) ---
    try:
        body_first = styles.add_style("Body First", WD_STYLE_TYPE.PARAGRAPH)
    except ValueError:
        body_first = styles["Body First"]
    body_first.base_style = normal
    bf_ppr = _style_ppr(body_first)
    _set_indent(bf_ppr, first_line_mm=0)

    # --- Heading 1 ----------------------------------------------------------
    h1 = styles["Heading 1"]
    h1_rpr = _style_rpr(h1)
    _set_font(h1_rpr, FONT_SANS, FONT_CJK)
    _set_size(h1_rpr, 24)
    _set_bold(h1_rpr, True)
    _set_color(h1_rpr, ACCENT)
    h1_ppr = _style_ppr(h1)
    _set_spacing(h1_ppr, before=24, after=12, line=1.1)
    _set_page_break_before(h1_ppr)
    _set_keep_with_next(h1_ppr)
    _add_border(h1_ppr, "bottom", size_eighths=8, color=ACCENT, space=6)

    # --- Heading 2 ----------------------------------------------------------
    h2 = styles["Heading 2"]
    h2_rpr = _style_rpr(h2)
    _set_font(h2_rpr, FONT_SANS, FONT_CJK)
    _set_size(h2_rpr, 16)
    _set_bold(h2_rpr, True)
    _set_color(h2_rpr, ACCENT)
    _set_smallcaps(h2_rpr)
    h2_ppr = _style_ppr(h2)
    _set_spacing(h2_ppr, before=18, after=6, line=1.15)
    _set_keep_with_next(h2_ppr)

    # --- Heading 3 ----------------------------------------------------------
    h3 = styles["Heading 3"]
    h3_rpr = _style_rpr(h3)
    _set_font(h3_rpr, FONT_SANS, FONT_CJK)
    _set_size(h3_rpr, 13)
    _set_bold(h3_rpr, True)
    _set_color(h3_rpr, ACCENT_SOFT)
    h3_ppr = _style_ppr(h3)
    _set_spacing(h3_ppr, before=12, after=4, line=1.2)
    _set_keep_with_next(h3_ppr)

    # --- Heading 4 ----------------------------------------------------------
    h4 = styles["Heading 4"]
    h4_rpr = _style_rpr(h4)
    _set_font(h4_rpr, FONT_SANS, FONT_CJK)
    _set_size(h4_rpr, 11)
    _set_italic(h4_rpr, True)
    _set_color(h4_rpr, ACCENT_SOFT)
    h4_ppr = _style_ppr(h4)
    _set_spacing(h4_ppr, before=10, after=2)
    _set_keep_with_next(h4_ppr)

    # --- Caption ------------------------------------------------------------
    try:
        cap = styles["Caption"]
    except KeyError:
        cap = styles.add_style("Caption", WD_STYLE_TYPE.PARAGRAPH)
    cap_rpr = _style_rpr(cap)
    _set_font(cap_rpr, FONT_SANS, FONT_CJK)
    _set_size(cap_rpr, 9)
    _set_italic(cap_rpr, True)
    _set_color(cap_rpr, "595959")
    cap_ppr = _style_ppr(cap)
    _set_alignment(cap_ppr, "center")
    _set_spacing(cap_ppr, before=2, after=8)
    _set_indent(cap_ppr, first_line_mm=0)

    # --- Quote --------------------------------------------------------------
    try:
        quote = styles["Quote"]
    except KeyError:
        quote = styles.add_style("Quote", WD_STYLE_TYPE.PARAGRAPH)
    q_rpr = _style_rpr(quote)
    _set_font(q_rpr, FONT_SERIF, FONT_CJK)
    _set_size(q_rpr, 10)
    _set_italic(q_rpr, True)
    _set_color(q_rpr, "3F3F3F")
    q_ppr = _style_ppr(quote)
    _set_indent(q_ppr, first_line_mm=0, left_mm=10)
    _set_spacing(q_ppr, before=6, after=6, line=1.25)
    _add_border(q_ppr, "left", size_eighths=24, color=ACCENT, space=8)

    # --- Source Code --------------------------------------------------------
    try:
        code = styles.add_style("Source Code", WD_STYLE_TYPE.PARAGRAPH)
    except ValueError:
        code = styles["Source Code"]
    c_rpr = _style_rpr(code)
    _set_font(c_rpr, FONT_MONO, FONT_CJK)
    _set_size(c_rpr, 9.5)
    c_ppr = _style_ppr(code)
    _set_indent(c_ppr, first_line_mm=0)
    _set_spacing(c_ppr, before=4, after=4, line=1.15)
    _set_alignment(c_ppr, "left")
    _set_shading(c_ppr, CODE_FILL)
    for side in ("top", "left", "bottom", "right"):
        _add_border(c_ppr, side, size_eighths=4, color=CODE_BORDER, space=2)

    # --- Callouts -----------------------------------------------------------
    callout_specs = [
        ("Callout Note",       "FFF8E1", "E6A23C"),
        ("Callout Warning",    "FDE7E9", "C0392B"),
        ("Callout Definition", "E3F2FD", "2E86AB"),
        ("Callout Example",    "E8F5E9", "2E7D32"),
    ]
    for name, fill, border_color in callout_specs:
        try:
            cs = styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        except ValueError:
            cs = styles[name]
        cs.base_style = normal
        cs_rpr = _style_rpr(cs)
        _set_font(cs_rpr, FONT_SERIF, FONT_CJK)
        _set_size(cs_rpr, 10)
        cs_ppr = _style_ppr(cs)
        _set_shading(cs_ppr, fill)
        _set_indent(cs_ppr, first_line_mm=0, left_mm=3)
        _set_spacing(cs_ppr, before=6, after=6, line=1.25)
        _set_alignment(cs_ppr, "left")
        _add_border(cs_ppr, "left", size_eighths=24, color=border_color, space=8)
        _add_border(cs_ppr, "top", size_eighths=4, color=border_color, space=4)
        _add_border(cs_ppr, "bottom", size_eighths=4, color=border_color, space=4)
        _add_border(cs_ppr, "right", size_eighths=4, color=border_color, space=4)

    # --- Pull Quote (content uses ::: {.pullquote} fenced div) -------------
    try:
        pq = styles.add_style("Pull Quote", WD_STYLE_TYPE.PARAGRAPH)
    except ValueError:
        pq = styles["Pull Quote"]
    pq_rpr = _style_rpr(pq)
    _set_font(pq_rpr, FONT_SANS, FONT_CJK)
    _set_size(pq_rpr, 14)
    _set_italic(pq_rpr, True)
    _set_color(pq_rpr, ACCENT)
    pq_ppr = _style_ppr(pq)
    _set_alignment(pq_ppr, "center")
    _set_indent(pq_ppr, first_line_mm=0, left_mm=12)
    _set_spacing(pq_ppr, before=12, after=12, line=1.3)
    _add_border(pq_ppr, "top", size_eighths=8, color=ACCENT, space=8)
    _add_border(pq_ppr, "bottom", size_eighths=8, color=ACCENT, space=8)

    # --- TOC Heading (for List of Figures / Tables) ------------------------
    try:
        tocHdg = styles.add_style("TOC Heading", WD_STYLE_TYPE.PARAGRAPH)
    except ValueError:
        tocHdg = styles["TOC Heading"]
    tocHdg.base_style = styles["Heading 1"]
    th_ppr = _style_ppr(tocHdg)
    # Do NOT break before every TOC heading — but it inherits from H1 which has
    # pageBreakBefore.  Override by removing.
    pbb = th_ppr.find(qn("w:pageBreakBefore"))
    if pbb is not None:
        th_ppr.remove(pbb)

    # --- Title / Subtitle for cover page -----------------------------------
    try:
        title = styles["Title"]
    except KeyError:
        title = styles.add_style("Title", WD_STYLE_TYPE.PARAGRAPH)
    t_rpr = _style_rpr(title)
    _set_font(t_rpr, FONT_SANS, FONT_CJK)
    _set_size(t_rpr, 32)
    _set_bold(t_rpr, True)
    _set_color(t_rpr, ACCENT)
    t_ppr = _style_ppr(title)
    _set_alignment(t_ppr, "center")
    _set_spacing(t_ppr, before=0, after=12, line=1.1)

    try:
        subtitle = styles["Subtitle"]
    except KeyError:
        subtitle = styles.add_style("Subtitle", WD_STYLE_TYPE.PARAGRAPH)
    st_rpr = _style_rpr(subtitle)
    _set_font(st_rpr, FONT_SANS, FONT_CJK)
    _set_size(st_rpr, 16)
    _set_italic(st_rpr, True)
    _set_color(st_rpr, "595959")
    st_ppr = _style_ppr(subtitle)
    _set_alignment(st_ppr, "center")
    _set_spacing(st_ppr, before=6, after=24)

    # --- Section properties (page size / mirror margins / headers/footers) -
    section = doc.sections[0]
    # A4 portrait
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    # Mirror margins for book-style recto/verso
    section.top_margin = Cm(2.2)
    section.bottom_margin = Cm(2.5)
    section.left_margin = Cm(2.8)    # inner (binding)
    section.right_margin = Cm(2.0)   # outer
    section.gutter = Cm(0.6)

    sectPr = section._sectPr
    # Mirror margins
    mirror = sectPr.find(qn("w:mirrorMargins"))
    if mirror is None:
        sectPr.insert(0, OxmlElement("w:mirrorMargins"))
    # Different first page (cover)
    titlePg = sectPr.find(qn("w:titlePg"))
    if titlePg is None:
        sectPr.append(OxmlElement("w:titlePg"))

    # Different odd/even headers — set in settings.xml
    settings = doc.settings.element
    if settings.find(qn("w:evenAndOddHeaders")) is None:
        settings.append(OxmlElement("w:evenAndOddHeaders"))

    # --- Save template ------------------------------------------------------
    doc.save(str(OUT))
    size_kb = OUT.stat().st_size / 1024
    print(f"[OK] wrote {OUT}  ({size_kb:.1f} KB)")


if __name__ == "__main__":
    build()
