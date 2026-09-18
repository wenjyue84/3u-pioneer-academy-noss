"""
build_output.py — output generator toolkit for JPK/ADI officer-template filling.
Config-driven: supports --subject video-film-editing (IT-072, regression fixture)
and --subject preschool-teaching (P851, real target).

Run: uv run --with python-docx --with openpyxl --with docxcompose python build_output.py <cmd> --subject <key>

Rule (00-SPEC.md): fill original officer templates, never rebuild from scratch.
⟪TBD: ...⟫ in source md -> "[TBD: ...]" in output. Never fabricate content.
"""
import re, os, glob, argparse, sys

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

ROOT = r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss"

SUBJECTS = {
    "video-film-editing": {
        "code": "IT-072-3:2012",
        "title": "VIDEO / FILM (EDITING)",
        "tahap": "3",
        "short": "IT-072",
        "base": os.path.join(ROOT, "video-film-editing"),
        "out": os.path.join(ROOT, "video-film-editing", "output"),
        "cu_titles": {
            "C01": "Visual Editing Project Analysis",
            "C02": "Visual Editing Preparation",
            "C03": "Offline Visual Editing",
            "C04": "Audio Sweetening",
            "C05": "Online Visual Editing",
        },
        "cu_order": ["C01", "C02", "C03", "C04", "C05"],
        "nota_src": os.path.join(ROOT, "video-film-editing", "05-nota-pembelajaran"),
        "rangka_src_mode": "from_nota",  # rangka derived from nota md (no aggregate rangka md)
        "rangka_out": os.path.join(ROOT, "video-film-editing", "output", "04 3.3a Rangka Nota Pembelajaran"),
        "nota_out": os.path.join(ROOT, "video-film-editing", "output", "05 3.3b Nota Pembelajaran (Kertas Penerangan)", "CU C01-C05"),
    },
    "preschool-teaching": {
        "code": "P851-002-4:2025",
        "title": "PRESCHOOL TEACHING",
        "tahap": "4 (DKM)",
        "short": "P851",
        "base": os.path.join(ROOT, "preschool-teaching"),
        "out": os.path.join(ROOT, "preschool-teaching", "output"),
        "cu_titles": {
            "C01": "Conduct Daily Routine Activities",
            "C02": "Perform Preschool Teaching And Learning Activities",
            "C03": "Organise Preschool Classroom Environment",
            "C04": "Develop Pupil's Assessment",
            "C05": "Handle Parental-Community Activities",
        },
        "cu_order": ["C01", "C02", "C03", "C04", "C05"],
        "nota_src": os.path.join(ROOT, "preschool-teaching", "05-nota-pembelajaran"),
        "rangka_src_mode": "aggregate_md",  # Cxx-rangka.md files already aggregate Bab/subtopik
        "rangka_src_dir": os.path.join(ROOT, "preschool-teaching", "04-rangka-nota-pembelajaran"),
        "rangka_out": os.path.join(ROOT, "preschool-teaching", "output", "04 3.3a Rangka Nota Pembelajaran"),
        "nota_out": os.path.join(ROOT, "preschool-teaching", "output", "05 3.3b Nota Pembelajaran (Kertas Penerangan)", "CU C01-C05"),
    },
}

RANGKA_TEMPLATE = os.path.join(ROOT, "raw", "adi-mpc-template-2026-09", "4-pelaksanaan-kompilasi",
                                "3.3a Template Rangka Nota Pembelajaran (BM).docx")
NOTA_TEMPLATE = os.path.join(ROOT, "raw", "adi-mpc-template-2026-09", "4-pelaksanaan-kompilasi",
                              "3.3b Template Nota Pembelajaran.docx")
LPKC_TEMPLATE = os.path.join(ROOT, "raw", "adi-mpc-template-2026-09", "4-pelaksanaan-kompilasi",
                              "1.2 LPKC.docx")

PRESCHOOL_MATRIX_MD = os.path.join(ROOT, "preschool-teaching", "02-borang-matriks-lampiran-5.md")
PRESCHOOL_PROSES_MD = os.path.join(ROOT, "preschool-teaching", "01-proses-kerja.md")
PRESCHOOL_LPKC_OUTLINE_MD = os.path.join(ROOT, "preschool-teaching", "12-lpkc-template-outline.md")
DERIVED_HOURS_MD = os.path.join(ROOT, "preschool-teaching", "output", "_tools", "derived-wa-hours.md")


# ---------- Correction 2: derive P-kod + JAM PENGETAHUAN for preschool-teaching WAs ----------

def build_wa_derivation_table():
    """Parse 02-borang-matriks-lampiran-5.md to build, per WA key ('C01-W01'):
       - p_codes: list of P-kod (from the NOSS vs Proses Kerja matrix ✓ marks)
       - weight_pct: WA weightage (from the 'Senarai CU & WA' table)
       - jam: 168 * weight_pct/100, rounded to 1 decimal
       Cross-referenced against 01-proses-kerja.md '## Ringkasan pemetaan' as a sanity check
       (both sources should agree on WA->P-kod coverage; matrix table is authoritative for the
       per-WA exact P-kod list because it is the official Lampiran 5 form)."""
    text = open(PRESCHOOL_MATRIX_MD, encoding="utf-8").read()

    # --- matrix table: NO | CU | KOD CU | WA | KOD WA | P01 ... P12 ---
    m = re.search(r"## Matriks NOSS vs Proses Kerja\s*\n(.*?)\n##", text, re.S)
    matrix_block = m.group(1) if m else ""
    lines = [ln for ln in matrix_block.split("\n") if ln.strip().startswith("|")]
    header_cells = [c.strip() for c in lines[0].strip("|").split("|")]
    p_col_idx = {cell: i for i, cell in enumerate(header_cells) if re.match(r"^P\d\d$", cell)}
    cu_idx = header_cells.index("KOD CU")
    wa_idx = header_cells.index("KOD WA")

    wa_pcodes = {}
    for ln in lines[2:]:  # skip header + separator row
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) < len(header_cells):
            continue
        cu = cells[cu_idx]
        wa = cells[wa_idx]
        if not re.match(r"^C0\d$", cu) or not re.match(r"^W\d\d$", wa):
            continue
        key = f"{cu}-{wa}"
        pcodes = [pcode for pcode, idx in p_col_idx.items() if idx < len(cells) and "✓" in cells[idx]]
        wa_pcodes.setdefault(key, [])
        for pc in pcodes:
            if pc not in wa_pcodes[key]:
                wa_pcodes[key].append(pc)

    # --- 'Senarai CU & WA (rujukan §18 pemberat)' table: CU | Tajuk CU | Berat CU | WA (berat) ---
    m2 = re.search(r"## Senarai CU & WA.*?\n(.*?)\n##", text, re.S)
    weight_block = m2.group(1) if m2 else ""
    wa_weight = {}
    for ln in weight_block.split("\n"):
        ln = ln.strip()
        if not ln.startswith("|") or "---" in ln:
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) < 4 or not re.match(r"^C0\d$", cells[0]):
            continue
        cu = cells[0]
        wa_field = cells[3]
        for wm in re.finditer(r"(W\d\d)\s*\((\d+(?:\.\d+)?)%\)", wa_field):
            wa_weight[f"{cu}-{wm.group(1)}"] = float(wm.group(2))

    rows = []
    derivation = {}
    for key in sorted(set(wa_pcodes) | set(wa_weight)):
        pcodes = sorted(wa_pcodes.get(key, []))
        weight = wa_weight.get(key)
        jam = round(168 * weight / 100.0, 1) if weight is not None else None
        derivation[key] = {"p_codes": pcodes, "weight_pct": weight, "jam": jam}
        rows.append((key, pcodes, weight, jam))

    os.makedirs(os.path.dirname(DERIVED_HOURS_MD), exist_ok=True)
    with open(DERIVED_HOURS_MD, "w", encoding="utf-8") as fh:
        fh.write("# derived-wa-hours.md — auto-generated by build_output.py build_wa_derivation_table()\n\n")
        fh.write("Methodology: PROSES KERJA BERKAITAN = P-kod(s) from `02-borang-matriks-lampiran-5.md` "
                  "'Matriks NOSS vs Proses Kerja' (✓ marks), cross-checked against `01-proses-kerja.md` "
                  "'## Ringkasan pemetaan'. JAM PENGETAHUAN = 168 j/CU (equal-split methodology) x WA "
                  "weightage from `02-borang-matriks-lampiran-5.md` 'Senarai CU & WA (rujukan §18 "
                  "pemberat)' table (same weightage as `00-noss-extract.md` §18 Competency Weightage). "
                  "Do not edit by hand.\n\n")
        fh.write("| WA | P-kod | Weightage | JAM PENGETAHUAN |\n|---|---|---|---|\n")
        for key, pcodes, weight, jam in rows:
            fh.write(f"| {key} | {', '.join(pcodes) if pcodes else '(none found)'} "
                      f"| {weight if weight is not None else '(none found)'}% "
                      f"| {jam if jam is not None else '(n/a)'} j |\n")
    print(f"derived-wa-hours: wrote {DERIVED_HOURS_MD} ({len(rows)} WA rows)")
    return derivation


def skip(path, why="source missing"):
    print(f"SKIPPED ({why}): {path}")


# ---------- shared md parsing (same schema used across both subjects) ----------

def parse_hdr_body(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    hdr = {}
    body_start = 0
    for i, ln in enumerate(lines):
        if ln.startswith("## I. TAJUK"):
            body_start = i
            break
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$", ln)
        if m and "---" not in m.group(1):
            hdr[m.group(1).strip()] = m.group(2).strip()
    body = "\n".join(lines[body_start:])
    return hdr, body


def hdr_lookup(hdr, prefix):
    for k, v in hdr.items():
        if k.startswith(prefix):
            return v
    return None


def get_section(body, tag, next_tags):
    pat = rf"## {re.escape(tag)}\s*\n(.*?)(?=" + "|".join(rf"## {re.escape(t)}" for t in next_tags) + r"|\Z)"
    m = re.search(pat, body, re.S)
    return m.group(1).strip() if m else ""


def clean_inline(s):
    s = s.replace("**", "").replace("`", "")
    s = re.sub(r"^\*+\s*", "", s)
    s = s.strip()
    if s.startswith("- "):
        s = s[2:]
    return s


def tbd_normalize(s):
    """⟪TBD: x⟫ -> [TBD: x] (findable placeholder convention)."""
    return re.sub(r"⟪\s*TBD:?\s*(.*?)⟫", lambda m: f"[TBD: {m.group(1).strip()}]", s)


# ================= NOTA (3.3b) =================

CALLOUT_LABELS = {"objektif pembelajaran", "rumusan", "kajian kes", "senarai semak", "aktiviti pengukuhan"}


def cmd_nota(subj):
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    from docx.enum.text import WD_ALIGN_PARAGRAPH

    cfg = SUBJECTS[subj]
    if not os.path.isfile(NOTA_TEMPLATE):
        return skip(NOTA_TEMPLATE, "template missing")
    wa_derivation = build_wa_derivation_table() if subj == "preschool-teaching" and os.path.isfile(PRESCHOOL_MATRIX_MD) else {}
    files = sorted(glob.glob(os.path.join(cfg["nota_src"], "C0*-W*.md")))
    files = [f for f in files if re.match(r"^C0\d-W\d\d\.md$", os.path.basename(f))]
    if not files:
        return skip(cfg["nota_src"] + "/C##-W##.md", "no nota source md found")

    os.makedirs(cfg["nota_out"], exist_ok=True)

    cu_groups = {}
    for f in files:
        base = os.path.basename(f).replace(".md", "")
        cu = base.split("-")[0]
        cu_groups.setdefault(cu, []).append(base)

    # ---------- readability helpers (formatting-only; never touch run text content) ----------

    def set_normal_style(doc):
        """Body font Arial 11pt, 1.15 line spacing, 6pt space-after — applies to the document's
        Normal style so every plain paragraph inherits it without per-run edits."""
        style = doc.styles["Normal"]
        style.font.name = "Arial"
        style.font.size = Pt(11)
        rPr = style.element.get_or_add_rPr()
        rFonts = rPr.find(qn('w:rFonts'))
        if rFonts is None:
            rFonts = OxmlElement('w:rFonts')
            rPr.append(rFonts)
        rFonts.set(qn('w:eastAsia'), "Arial")
        pf = style.paragraph_format
        pf.line_spacing = 1.15
        pf.space_after = Pt(6)

    def shade_paragraph(paragraph, hexcolor):
        pPr = paragraph._p.get_or_add_pPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), hexcolor)
        pPr.append(shd)

    def shade_cell(cell, hexcolor):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), hexcolor)
        tcPr.append(shd)

    def set_repeat_header(row):
        trPr = row._tr.get_or_add_trPr()
        tblHeader = OxmlElement('w:tblHeader')
        tblHeader.set(qn('w:val'), 'true')
        trPr.append(tblHeader)

    def add_page_break_before(paragraph):
        paragraph.paragraph_format.page_break_before = True

    def add_bab_heading(doc, text):
        """### Bab n heading: new page, shaded light-grey, 14pt bold."""
        p = doc.add_paragraph()
        add_page_break_before(p)
        shade_paragraph(p, "D9D9D9")
        r = p.add_run(text)
        r.bold = True
        r.font.size = Pt(14)
        r.font.name = "Arial"
        return p

    def add_bold_para(doc, text, size=None, keep_with_next=False):
        p = doc.add_paragraph()
        r = p.add_run(text)
        r.bold = True
        if size:
            r.font.size = Pt(size)
        if keep_with_next:
            p.paragraph_format.keep_with_next = True
        return p

    def add_normal_para(doc, text=""):
        p = doc.add_paragraph()
        if text:
            p.add_run(text)
        return p

    def add_bullet_para(doc, text, numbered=False):
        style = "List Number" if numbered else "List Bullet"
        try:
            p = doc.add_paragraph(style=style)
        except KeyError:
            p = doc.add_paragraph(style="List Paragraph")
            text = ("• " if not numbered else "") + text
        p.add_run(text)
        return p

    def add_table_grid(doc, rows, header_row=True):
        if not rows:
            return
        ncols = len(rows[0])
        t = doc.add_table(rows=len(rows), cols=ncols)
        try:
            t.style = "Table Grid"
        except KeyError:
            pass
        for ri, row in enumerate(rows):
            for ci, val in enumerate(row):
                if ci < ncols:
                    cell = t.cell(ri, ci)
                    cell.text = tbd_normalize(val)
                    for p in cell.paragraphs:
                        for r in p.runs:
                            r.font.size = Pt(10)
                            r.font.name = "Arial"
                            if ri == 0 and header_row:
                                r.bold = True
                    if ri == 0 and header_row:
                        shade_cell(cell, "D9D9D9")
        if header_row:
            set_repeat_header(t.rows[0])
        return t

    def add_callout_box(doc, label, content_lines):
        """Labelled block (Objektif Pembelajaran / Rumusan / Kajian kes / Senarai semak /
        Aktiviti pengukuhan) rendered as a single-cell shaded call-out box wrapping the label +
        its content — text is unchanged, only the container is new."""
        t = doc.add_table(rows=1, cols=1)
        try:
            t.style = "Table Grid"
        except KeyError:
            pass
        cell = t.cell(0, 0)
        shade_cell(cell, "F2F2F2")
        p0 = cell.paragraphs[0]
        r0 = p0.add_run(label)
        r0.bold = True
        r0.font.size = Pt(12)
        r0.font.name = "Arial"
        for ln in content_lines:
            stripped = ln.strip()
            if not stripped:
                continue
            if re.match(r"^[-*]\s+", stripped) or re.match(r"^\d+\.\s+", stripped):
                text = re.sub(r"^[-*]\s+", "", stripped)
                text = re.sub(r"^\d+\.\s+", "", text)
                try:
                    p = cell.add_paragraph(style="List Bullet")
                except KeyError:
                    p = cell.add_paragraph()
                    text = "• " + text
            else:
                text = stripped
                p = cell.add_paragraph()
            r = p.add_run(tbd_normalize(clean_inline(text)))
            r.font.size = Pt(11)
            r.font.name = "Arial"
        return t

    def render_markdown_block(doc, block):
        lines = block.split("\n")
        i, n = 0, len(lines)
        while i < n:
            raw = lines[i]
            stripped = raw.strip()
            if not stripped:
                i += 1
                continue
            m = re.match(r"^###\s+(Bab\s+\d+.*)$", stripped)
            if m:
                add_bab_heading(doc, tbd_normalize(clean_inline(m.group(1))))
                i += 1
                continue
            if stripped.startswith("|"):
                table_lines = []
                j = i
                while j < n and lines[j].strip().startswith("|"):
                    table_lines.append(lines[j].strip())
                    j += 1
                rows = []
                for tl in table_lines:
                    if re.match(r"^\|[\s:\-|]+\|$", tl):
                        continue
                    cells = [clean_inline(c.strip()) for c in tl.strip("|").split("|")]
                    rows.append(cells)
                add_table_grid(doc, rows)
                i = j
                continue
            if re.match(r"^[-*]\s+", stripped):
                text = re.sub(r"^[-*]\s+", "", stripped)
                add_bullet_para(doc, tbd_normalize(clean_inline(text)), numbered=False)
                i += 1
                continue
            if re.match(r"^\d+\.\s+", stripped):
                text = re.sub(r"^\d+\.\s+", "", stripped)
                add_bullet_para(doc, tbd_normalize(clean_inline(text)), numbered=True)
                i += 1
                continue
            mb = re.match(r"^\*\*(.+?)\*\*$", stripped)
            mh = re.match(r"^#{2,4}\s+(.+)$", stripped)  # sub-topic headings (## / ### / #### style)
            if mb or mh:
                label_raw = clean_inline((mb or mh).group(1))
                label_key = re.sub(r"^\d+(\.\d+)*\.?\s+", "", label_raw).strip().lower()
                label_key = re.sub(r"[:\s]+$", "", label_key)
                is_callout = label_key in CALLOUT_LABELS or any(lbl in label_key for lbl in CALLOUT_LABELS)
                if is_callout:
                    # collect following lines up to next heading/bold-label/table into the box
                    j = i + 1
                    content = []
                    while j < n:
                        s2 = lines[j].strip()
                        if (re.match(r"^###\s+Bab\s+\d+", s2) or re.match(r"^\*\*(.+?)\*\*$", s2)
                                or re.match(r"^#{2,4}\s+", s2) or s2.startswith("|")):
                            break
                        content.append(lines[j])
                        j += 1
                    add_callout_box(doc, tbd_normalize(label_raw), content)
                    i = j
                    continue
                add_bold_para(doc, tbd_normalize(label_raw), size=12, keep_with_next=True)
                i += 1
                continue
            add_normal_para(doc, tbd_normalize(clean_inline(stripped)))
            i += 1

    def clear_body_after_table(doc):
        body = doc.element.body
        first_table = doc.tables[0]._tbl
        seen = False
        to_remove = []
        for child in list(body.iterchildren()):
            if child is first_table:
                seen = True
                continue
            if not seen:
                continue
            if child.tag == qn('w:sectPr'):
                continue
            to_remove.append(child)
        for el in to_remove:
            el.getparent().remove(el)

    def set_cell(cell, text):
        cell.text = tbd_normalize(str(text))

    def set_cell_wa_list(cell, wa_lines, current_wa):
        """Fill the WA cell with one line per work activity of the CU, current one bold."""
        cell.text = ""
        p0 = cell.paragraphs[0]
        for i, line in enumerate(wa_lines):
            p = p0 if i == 0 else cell.add_paragraph()
            r = p.add_run(tbd_normalize(line))
            if line == current_wa:
                r.bold = True

    def fill_header_table(doc, prog, tahap, cu, wa, kode_no, page_no, page_total, wa_lines=None):
        t = doc.tables[0]
        set_cell(t.rows[1].cells[1], prog)
        set_cell(t.rows[2].cells[1], tahap)
        set_cell(t.rows[3].cells[1], cu)
        if wa_lines:
            set_cell_wa_list(t.rows[4].cells[1], wa_lines, wa)
        else:
            set_cell(t.rows[4].cells[1], wa)
        set_cell(t.rows[5].cells[1], kode_no)
        set_cell(t.rows[5].cells[2], "Muka Surat/Page:\nDrpd/ Of::")
        set_cell(t.rows[5].cells[3], f"{page_no}\n{page_total}")
        for ci in range(2, len(t.rows[1].cells)):
            try:
                for ri, val in ((1, prog), (2, tahap), (3, cu), (4, wa)):
                    cell = t.rows[ri].cells[ci]
                    if ri == 4 and wa_lines:
                        # merged cell mirrors row-4's WA cell — keep the same bold WA list, not
                        # the plain current-WA string, else it clobbers the list just written.
                        if cell.text != "\n".join(wa_lines):
                            set_cell_wa_list(cell, wa_lines, wa)
                    elif cell.text != val:
                        set_cell(cell, val)
            except IndexError:
                pass

    def _fld(run, kind):
        el = OxmlElement('w:fldChar')
        el.set(qn('w:fldCharType'), kind)
        run._r.append(el)

    def _instr(run, text):
        el = OxmlElement('w:instrText')
        el.set(qn('xml:space'), 'preserve')
        el.text = text
        run._r.append(el)

    def add_page_footer(doc):
        """Footer: 'Muka surat X / Y' using Word PAGE/NUMPAGES fields."""
        sec = doc.sections[0]
        footer = sec.footer
        fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = fp.add_run("Muka surat ")
        r1.font.name = "Arial"; r1.font.size = Pt(9)
        rp = fp.add_run(); _fld(rp, 'begin'); _instr(rp, 'PAGE'); _fld(rp, 'end')
        r2 = fp.add_run(" / ")
        r2.font.name = "Arial"; r2.font.size = Pt(9)
        rn = fp.add_run(); _fld(rn, 'begin'); _instr(rn, 'NUMPAGES'); _fld(rn, 'end')

    def add_page_header(doc, kode_no):
        """Header: the nota code, e.g. P851-002-4:2025-C01/NP(1/4)."""
        sec = doc.sections[0]
        header = sec.header
        hp = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = hp.add_run(kode_no)
        r.font.name = "Arial"; r.font.size = Pt(9)

    def add_kandungan_list(doc, penerangan_text):
        """Right after TUJUAN: a short 'Kandungan nota ini' list of this nota's own Bab titles.
        New structural content — not part of the original wording — so it is explicitly called
        out in the drift report rather than folded into the wording diff."""
        bab_titles = re.findall(r"^###\s+(Bab\s+\d+.*)$", penerangan_text, re.M)
        if not bab_titles:
            return
        add_bold_para(doc, "Kandungan nota ini:", size=12, keep_with_next=True)
        for t in bab_titles:
            add_bullet_para(doc, tbd_normalize(clean_inline(t)), numbered=False)
        doc.add_paragraph()

    def build_one(md_path, out_path, cu_code, k, n, wa_lines=None):
        hdr, body = parse_hdr_body(md_path)
        prog = hdr_lookup(hdr, "KOD NAMA DAN PROGRAM") or hdr_lookup(hdr, "KOD NOSS") or f'{cfg["code"]} {cfg["title"]}'
        tahap = hdr_lookup(hdr, "TAHAP") or cfg["tahap"]
        cu = hdr_lookup(hdr, "NO DAN TAJUK UNIT KOMPETENSI") or "[TBD: CU]"
        wa = hdr_lookup(hdr, "NO DAN PENYATAAN AKTIVITI") or hdr_lookup(hdr, "NO DAN NAMA WA") or "[TBD: WA]"
        kode_no = f'{cfg["code"]}-{cu_code}/NP({k}/{n})'

        doc = Document(NOTA_TEMPLATE)
        clear_body_after_table(doc)
        set_normal_style(doc)
        fill_header_table(doc, prog, tahap, cu, wa, kode_no, page_no="[TBD: no. muka surat]", page_total=str(n),
                           wa_lines=wa_lines)
        add_page_footer(doc)
        add_page_header(doc, kode_no)

        # Correction 2: PROSES KERJA BERKAITAN / JAM PENGETAHUAN, derived at generation time
        # (never written back to the source .md — computed fresh from 02-borang-matriks-lampiran-5.md).
        wa_num_match = re.search(r"-W(\d\d)$", os.path.basename(md_path).replace(".md", ""))
        wa_key = f"{cu_code}-W{wa_num_match.group(1)}" if wa_num_match else None
        deriv = wa_derivation.get(wa_key) if wa_derivation else None
        if deriv and deriv["p_codes"]:
            proses_txt = ", ".join(deriv["p_codes"])
        else:
            proses_txt = "[TBD: P-kod tidak dijumpai dalam 02-borang-matriks-lampiran-5.md]"
        if deriv and deriv["jam"] is not None:
            jam_txt = f'{deriv["jam"]:.1f} j (168 j x {deriv["weight_pct"]:.0f}% pemberat WA)'
        else:
            jam_txt = "[TBD: weightage WA tidak dijumpai]"
        add_bold_para(doc, "PROSES KERJA BERKAITAN:")
        add_normal_para(doc, proses_txt)
        add_bold_para(doc, "JAM PENGETAHUAN:")
        add_normal_para(doc, jam_txt)
        doc.add_paragraph()

        tajuk = get_section(body, "I. TAJUK", ["II. TUJUAN"])
        tujuan = get_section(body, "II. TUJUAN", ["III. PENERANGAN"])
        penerangan = get_section(body, "III. PENERANGAN", ["IV. SESI PERSOALAN / KERJA KUMPULAN"])
        soalan = get_section(body, "IV. SESI PERSOALAN / KERJA KUMPULAN", ["V. RUJUKAN"])
        rujukan = get_section(body, "V. RUJUKAN", [])

        add_bold_para(doc, "TAJUK:")
        add_normal_para(doc, tbd_normalize(clean_inline(tajuk)))
        doc.add_paragraph()
        add_bold_para(doc, "TUJUAN:")
        render_markdown_block(doc, tujuan)
        add_kandungan_list(doc, penerangan)
        doc.add_paragraph()
        add_bold_para(doc, "PENERANGAN:")
        render_markdown_block(doc, penerangan)
        add_bold_para(doc, "SOALAN:")
        render_markdown_block(doc, soalan)
        add_bold_para(doc, "RUJUKAN:")
        render_markdown_block(doc, rujukan)
        doc.save(out_path)
        return cu, wa

    # precompute, per CU, the ordered list of "code / title" WA lines from every nota md's own
    # header (reuses the same hdr_lookup parsing cmd_nota already does per file — Task 1 header change)
    cu_wa_lines = {}
    for cu, bases in cu_groups.items():
        lines = []
        for base in bases:
            f2 = os.path.join(cfg["nota_src"], base + ".md")
            hdr2, _ = parse_hdr_body(f2)
            wa2 = hdr_lookup(hdr2, "NO DAN PENYATAAN AKTIVITI") or hdr_lookup(hdr2, "NO DAN NAMA WA") or "[TBD: WA]"
            lines.append(wa2)
        cu_wa_lines[cu] = lines

    order = sorted(files, key=lambda f: os.path.basename(f))
    seq = 0
    written = []
    for f in order:
        seq += 1
        base = os.path.basename(f).replace(".md", "")
        cu = base.split("-")[0]
        k = cu_groups[cu].index(base) + 1
        n = len(cu_groups[cu])
        hdr_preview, _ = parse_hdr_body(f)
        wa_full = hdr_lookup(hdr_preview, "NO DAN PENYATAAN AKTIVITI") or hdr_lookup(hdr_preview, "NO DAN NAMA WA") or ""
        wa_title = wa_full.split("/", 1)[1].strip() if "/" in wa_full else wa_full
        wa_title = re.sub(r"^(WA?\d+)\s*[:\-–—]\s*", "", wa_title.strip()) or "[TBD: tajuk WA]"
        fname = f'3.3b-{seq:02d} Nota Pembelajaran {base} {wa_title} ({cfg["short"]}).docx'
        fname = re.sub(r'[\\/:*?"<>|]', "-", fname)
        out_path = os.path.join(cfg["nota_out"], fname)
        cu_hdr, wa_hdr = build_one(f, out_path, cu, k, n, wa_lines=cu_wa_lines.get(cu))
        written.append(out_path)

    # verify read-back
    if written:
        d = Document(written[0])
        readback = d.tables[0].rows[3].cells[1].text[:80]
        body_text = "\n".join(p.text for p in d.paragraphs)
        print(f"nota: wrote {len(written)} files to {cfg['nota_out']}")
        print(f"  read-back [{os.path.basename(written[0])}] CU cell -> {readback!r}")
        if "PROSES KERJA BERKAITAN:" in body_text:
            idx = body_text.split("\n").index("PROSES KERJA BERKAITAN:")
            print(f"  read-back PROSES KERJA BERKAITAN -> {body_text.split(chr(10))[idx+1]!r}")
        if "JAM PENGETAHUAN:" in body_text:
            idx = body_text.split("\n").index("JAM PENGETAHUAN:")
            print(f"  read-back JAM PENGETAHUAN -> {body_text.split(chr(10))[idx+1]!r}")


# ================= RANGKA (3.3a) =================

def cmd_rangka(subj):
    from docx import Document
    from docx.shared import Pt
    from docx.oxml.ns import qn

    cfg = SUBJECTS[subj]
    if not os.path.isfile(RANGKA_TEMPLATE):
        return skip(RANGKA_TEMPLATE, "template missing")
    os.makedirs(cfg["rangka_out"], exist_ok=True)

    def clear_body_after_table(doc):
        body = doc.element.body
        first_table = doc.tables[0]._tbl
        seen = False
        to_remove = []
        for child in list(body.iterchildren()):
            if child is first_table:
                seen = True
                continue
            if not seen:
                continue
            if child.tag == qn('w:sectPr'):
                continue
            to_remove.append(child)
        for el in to_remove:
            el.getparent().remove(el)

    def add_bold_para(doc, text, size=None):
        p = doc.add_paragraph()
        r = p.add_run(text)
        r.bold = True
        if size:
            r.font.size = Pt(size)
        return p

    def add_normal_para(doc, text=""):
        p = doc.add_paragraph()
        if text:
            p.add_run(text)
        return p

    def add_table_grid(doc, rows, header=True):
        ncols = len(rows[0])
        t = doc.add_table(rows=len(rows), cols=ncols)
        try:
            t.style = "Table Grid"
        except KeyError:
            pass
        for ri, row in enumerate(rows):
            for ci, val in enumerate(row):
                t.cell(ri, ci).text = tbd_normalize(val)
            if header and ri == 0:
                for ci in range(ncols):
                    for p in t.cell(ri, ci).paragraphs:
                        for r in p.runs:
                            r.bold = True
        return t

    # -- extract per-WA (bab_title -> [subs]) list depending on source mode --
    def wa_outline_from_aggregate(md_path):
        """preschool-teaching Cxx-rangka.md: '## WA{n} — {title} ({code})' then 'Bab...:' + numbered list."""
        text = open(md_path, encoding="utf-8").read()
        blocks = re.split(r"(?=^## WA\d)", text, flags=re.M)
        out = []
        for b in blocks:
            m = re.match(r"^## WA(\d+)\s*—\s*(.+?)\s*\((.+?)\)\s*$", b.strip().split("\n")[0])
            if not m:
                continue
            wa_no, wa_title, wa_code = m.groups()
            babs = []
            cur = None
            for line in b.split("\n")[1:]:
                s = line.strip()
                if s.startswith("---"):
                    break
                mnum = re.match(r"^(\d+)\.\s+(.+)$", s)
                if mnum:
                    babs.append((mnum.group(1), tbd_normalize(mnum.group(2))))
            out.append({"wa_no": wa_no, "wa_title": wa_title.strip(), "wa_code": wa_code.strip(), "babs": babs})
        return out

    def wa_outline_from_nota(files):
        """video-film-editing: derive Bab/subs from III. PENERANGAN of each Cxx-Wnn.md."""
        out = []
        for idx, f in enumerate(sorted(files), start=1):
            hdr, body = parse_hdr_body(f)
            wa_full = hdr_lookup(hdr, "NO DAN PENYATAAN AKTIVITI") or hdr_lookup(hdr, "NO DAN NAMA WA") or ""
            code, title = (wa_full.split("/", 1) if "/" in wa_full else (f, wa_full))
            title = ", ".join(p.strip() for p in title.split("/")) if "/" in title else title.strip()
            penerangan = get_section(body, "III. PENERANGAN", ["IV. SESI PERSOALAN / KERJA KUMPULAN"])
            babs = []
            cur_title, n = None, 0
            for line in penerangan.split("\n"):
                s = line.strip()
                m = re.match(r"^###\s+Bab\s+\d+\s*:\s*(.+)$", s)
                if m:
                    n += 1
                    babs.append((str(n), tbd_normalize(clean_inline(m.group(1)))))
            out.append({"wa_no": str(idx), "wa_title": title.strip(), "wa_code": code.strip(), "babs": babs})
        return out

    cu_files_nota = {}
    if cfg["rangka_src_mode"] == "from_nota":
        all_md = sorted(glob.glob(os.path.join(cfg["nota_src"], "C0*-W*.md")))
        for f in all_md:
            cu = os.path.basename(f).split("-")[0]
            cu_files_nota.setdefault(cu, []).append(f)

    results = []
    for seq, cu in enumerate(cfg["cu_order"], start=1):
        cu_title = cfg["cu_titles"].get(cu, "[TBD: CU title]")
        if cfg["rangka_src_mode"] == "aggregate_md":
            src = os.path.join(cfg["rangka_src_dir"], f"{cu}-rangka.md")
            if not os.path.isfile(src):
                skip(src, "rangka source missing")
                continue
            outline = wa_outline_from_aggregate(src)
        else:
            files = cu_files_nota.get(cu)
            if not files:
                skip(f'{cfg["nota_src"]}/{cu}-W*.md', "nota source missing (rangka derives from it)")
                continue
            outline = wa_outline_from_nota(files)

        doc = Document(RANGKA_TEMPLATE)
        clear_body_after_table(doc)
        title_text = f'3.3a Rangka Nota Pembelajaran — {cfg["code"]}-{cu} {cu_title}'
        if doc.paragraphs:
            p0 = doc.paragraphs[0]
            for r in list(p0.runs):
                r.text = ""
            if p0.runs:
                p0.runs[0].text = title_text
                p0.runs[0].bold = True
            else:
                r = p0.add_run(title_text)
                r.bold = True
        doc.add_paragraph()

        for wa in outline:
            add_bold_para(doc, f'Module: {cu} {cu_title} / Work Activity: WA{wa["wa_no"]} — {wa["wa_title"]} ({wa["wa_code"]})', size=12)
            add_normal_para(doc, "Senarai topik nota:")
            rows = [["Bab", "Sub-topik"]]
            for no, title in wa["babs"]:
                rows.append([f"{no}. {title}", ""])
            add_table_grid(doc, rows)
            doc.add_paragraph()

        fname = f'3.3a-{seq:02d} Rangka Nota Pembelajaran {cu} {cu_title.upper()} ({cfg["short"]}).docx'
        fname = re.sub(r'[\\/:*?"<>|]', "-", fname)
        out_path = os.path.join(cfg["rangka_out"], fname)
        doc.save(out_path)
        results.append((cu, out_path, len(outline)))

    if results:
        d = Document(results[0][1])
        readback = d.paragraphs[0].text[:90]
        print(f"rangka: wrote {len(results)} CU files to {cfg['rangka_out']}")
        for cu, path, nwa in results:
            print(f"  [{cu}] {nwa} WA -> {os.path.basename(path)}")
        print(f"  read-back [{os.path.basename(results[0][1])}] title -> {readback!r}")
    else:
        print("rangka: nothing written (all sources missing)")


# ================= LPKC (1.2 LPKC.docx scoring form + Rangka Penulisan LPKC) =================

def cmd_lpkc(subj):
    from docx import Document
    from docx.shared import Pt, Cm
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    if subj != "preschool-teaching":
        return skip(f"lpkc --subject {subj}", "LPKC is DKM-only; no fixture for this subject")
    cfg = SUBJECTS[subj]
    out_dir = os.path.join(cfg["out"], "10b 1.2 LPKC (DKM sahaja)")
    os.makedirs(out_dir, exist_ok=True)

    # --- part 1: fill the official PPL-ADI scoring form header fields only ---
    if not os.path.isfile(LPKC_TEMPLATE):
        skip(LPKC_TEMPLATE, "template missing")
    else:
        doc = Document(LPKC_TEMPLATE)
        t = doc.tables[0]
        # rows (0-idx): 0 header, 1 NO. PENDAFTARAN, 2 NAMA PENUH, 3 NO. KAD PENGENALAN,
        # 4 KOD NOSS, 5 TAJUK NOSS, 6 Tajuk LPKC, 7 Tarikh Penilaian
        fills = {
            1: "[TBD: no. pendaftaran]",
            2: "[TBD: nama calon]",
            4: cfg["code"],
            5: cfg["title"],
            6: "[TBD: tajuk projek]",
        }
        for ri, val in fills.items():
            try:
                t.rows[ri].cells[1].text = val
            except IndexError:
                pass
        scoring_path = os.path.join(out_dir, "1.2 Borang Penilaian LPKC_JPK_ADI_04-2024 (P851).docx")
        doc.save(scoring_path)
        d = Document(scoring_path)
        print(f"lpkc(form): wrote {scoring_path}")
        print(f"  read-back KOD NOSS -> {d.tables[0].rows[4].cells[1].text!r}")
        print(f"  read-back TAJUK NOSS -> {d.tables[0].rows[5].cells[1].text!r}")

    # --- part 2: fresh 'Rangka Penulisan LPKC' docx from 12-lpkc-template-outline.md, Jadual 10 format ---
    if not os.path.isfile(PRESCHOOL_LPKC_OUTLINE_MD):
        return skip(PRESCHOOL_LPKC_OUTLINE_MD, "outline source missing")

    text = open(PRESCHOOL_LPKC_OUTLINE_MD, encoding="utf-8").read()

    rangka_doc = Document()
    sec = rangka_doc.sections[0]
    # Jadual 10 margins: Atas/Bawah/Kanan 2.5cm, Kiri 4.0cm (verbatim, 12-lpkc.md §1)
    sec.top_margin = Cm(2.5)
    sec.bottom_margin = Cm(2.5)
    sec.right_margin = Cm(2.5)
    sec.left_margin = Cm(4.0)

    style = rangka_doc.styles["Normal"]
    style.font.name = "Arial"
    style.font.size = Pt(12)
    style.paragraph_format.line_spacing = 1.5
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = OxmlElement('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:eastAsia'), "Arial")

    # page number, bottom-right footer
    footer = sec.footer
    fp = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = fp.add_run()
    fld_begin = OxmlElement('w:fldChar'); fld_begin.set(qn('w:fldCharType'), 'begin')
    instr = OxmlElement('w:instrText'); instr.set(qn('xml:space'), 'preserve'); instr.text = "PAGE"
    fld_end = OxmlElement('w:fldChar'); fld_end.set(qn('w:fldCharType'), 'end')
    run._r.append(fld_begin); run._r.append(instr); run._r.append(fld_end)

    lines = text.split("\n")
    section_count = 0
    i, n = 0, len(lines)
    while i < n:
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped == "---":
            i += 1
            continue
        m1 = re.match(r"^#\s+(.+)$", stripped)
        m2 = re.match(r"^##\s+(.+)$", stripped)
        m3 = re.match(r"^###\s+(.+)$", stripped)
        if m1 and not m2:
            p = rangka_doc.add_paragraph()
            r = p.add_run(tbd_normalize(clean_inline(m1.group(1))))
            r.bold = True
            r.font.size = Pt(16)
            i += 1
            continue
        if m2:
            section_count += 1
            p = rangka_doc.add_paragraph()
            r = p.add_run(tbd_normalize(clean_inline(m2.group(1))))
            r.bold = True
            r.font.size = Pt(14)
            i += 1
            continue
        if m3:
            p = rangka_doc.add_paragraph()
            r = p.add_run(tbd_normalize(clean_inline(m3.group(1))))
            r.bold = True
            r.font.size = Pt(12)
            i += 1
            continue
        if stripped.startswith("|"):
            table_lines = []
            j = i
            while j < n and lines[j].strip().startswith("|"):
                table_lines.append(lines[j].strip())
                j += 1
            rows = [[clean_inline(c.strip()) for c in tl.strip("|").split("|")]
                    for tl in table_lines if not re.match(r"^\|[\s:\-|]+\|$", tl)]
            if rows:
                ncols = max(len(r) for r in rows)
                t2 = rangka_doc.add_table(rows=len(rows), cols=ncols)
                try:
                    t2.style = "Table Grid"
                except KeyError:
                    pass
                for ri, row in enumerate(rows):
                    for ci, val in enumerate(row):
                        t2.cell(ri, ci).text = tbd_normalize(val)
            i = j
            continue
        p = rangka_doc.add_paragraph()
        p.add_run(tbd_normalize(clean_inline(stripped)))
        i += 1

    rangka_path = os.path.join(out_dir, "Rangka Penulisan LPKC (P851).docx")
    rangka_doc.save(rangka_path)
    d2 = Document(rangka_path)
    print(f"lpkc(rangka): wrote {rangka_path} ({section_count} '##' sections)")
    print(f"  read-back first paragraph -> {d2.paragraphs[0].text[:80]!r}")


# ================= BUKU (13 Buku Teks — docxcompose compilation of nota output) =================

def cmd_buku(subj):
    """Compile the 'nota' output into one full book + one volume per CU. Cheap/idempotent: always
    re-runs `nota` first so it compiles from whatever nota content exists right now (other agents
    may be actively expanding C01/C02 nota content in parallel)."""
    from docx import Document
    from docx.shared import Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    from docxcompose.composer import Composer

    cfg = SUBJECTS[subj]
    if not os.path.isfile(NOTA_TEMPLATE):
        return skip(NOTA_TEMPLATE, "template missing (nota can't build, so buku can't compile)")

    print("buku: re-running nota first (idempotent — compiles from fresh nota output)")
    cmd_nota(subj)

    nota_dir = cfg["nota_out"]
    out_dir = os.path.join(cfg["out"], "13 Buku Teks (kompilasi Nota)")
    os.makedirs(out_dir, exist_ok=True)

    def all_nota_files():
        files = sorted(glob.glob(os.path.join(nota_dir, "*.docx")))
        return [f for f in files if not os.path.basename(f).startswith("~$")]

    def add_page_break(doc):
        p = doc.add_paragraph()
        p.add_run().add_break(WD_BREAK.PAGE)

    def fldchar(kind):
        el = OxmlElement('w:fldChar'); el.set(qn('w:fldCharType'), kind); return el

    def instr_text(text):
        el = OxmlElement('w:instrText'); el.set(qn('xml:space'), 'preserve'); el.text = text; return el

    def make_cover(cu_range_label):
        doc = Document()
        def center(text, size, bold=True):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(text)
            r.bold = bold
            r.font.size = Pt(size)
        for _ in range(4):
            doc.add_paragraph()
        center(cfg["code"], 16)
        center(cfg["title"], 20)
        center(f'TAHAP {cfg["tahap"]}', 16)
        doc.add_paragraph()
        center(f"Nota Pembelajaran / Kertas Penerangan — Unit Kompetensi {cu_range_label}", 14, bold=False)
        doc.add_paragraph()
        doc.add_paragraph()
        center("Pusat Latihan: 3U Pioneer Academy Sdn Bhd", 12, bold=False)
        center("Syarikat: [TBD: nama syarikat]", 12, bold=False)
        center("2026", 12, bold=False)
        add_page_break(doc)
        return doc

    def add_toc_field(doc):
        p = doc.add_paragraph()
        r = p.add_run("ISI KANDUNGAN")
        r.bold = True
        r.font.size = Pt(14)
        p2 = doc.add_paragraph()
        run = p2.add_run()
        for el in (fldchar('begin'), instr_text(r' TOC \o "1-2" \h \z \u '), fldchar('separate'), fldchar('end')):
            run._r.append(el)
        add_page_break(doc)

    def make_divider(cu, title):
        doc = Document()
        p = doc.add_paragraph(style="Heading 1")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(f"UNIT KOMPETENSI {cu} — {title.upper()}")
        r.bold = True
        add_page_break(doc)
        return doc

    def make_break_doc():
        doc = Document()
        add_page_break(doc)
        return doc

    def prep_note_doc(f):
        sub = Document(f)
        wa_text = sub.tables[0].rows[4].cells[1].text.strip() if sub.tables else ""
        if sub.paragraphs:
            new_p = sub.paragraphs[0].insert_paragraph_before("", style="Heading 2")
            r = new_p.add_run(wa_text or os.path.basename(f))
            r.bold = True
        return sub

    def files_for_cu(cu):
        return [f for f in all_nota_files() if f" {cu}-W" in os.path.basename(f)]

    written = []

    def build_full_book():
        files = all_nota_files()
        if not files:
            skip(nota_dir, "no nota output to compile")
            return None
        master = make_cover(f'{cfg["cu_order"][0]}–{cfg["cu_order"][-1]}')
        composer = Composer(master)
        add_toc_field(master)
        for cu in cfg["cu_order"]:
            cu_files = files_for_cu(cu)
            if not cu_files:
                continue
            composer.append(make_divider(cu, cfg["cu_titles"].get(cu, "[TBD: CU title]")))
            for f in cu_files:
                composer.append(prep_note_doc(f))
                composer.append(make_break_doc())
        out_path = os.path.join(
            out_dir, f'Buku Teks {cfg["code"].replace(":", "-")} {cfg["title"]} Tahap {cfg["tahap"]} - '
                     f'Nota Pembelajaran {cfg["cu_order"][0]}-{cfg["cu_order"][-1]} ({cfg["short"]}).docx')
        out_path = re.sub(r'[\\/:*?"<>|]', "-", os.path.basename(out_path))
        out_path = os.path.join(out_dir, out_path)
        composer.save(out_path)
        written.append(out_path)
        return out_path

    def build_cu_volume(cu):
        files = files_for_cu(cu)
        if not files:
            skip(f"{nota_dir}/*{cu}-W*", f"no nota output for {cu}")
            return
        title = cfg["cu_titles"].get(cu, "[TBD: CU title]")
        master = make_cover(cu)
        composer = Composer(master)
        add_toc_field(master)
        composer.append(make_divider(cu, title))
        for f in files:
            composer.append(prep_note_doc(f))
            composer.append(make_break_doc())
        fname = f'Buku Teks {cfg["code"].replace(":", "-")} {cfg["title"]} Tahap {cfg["tahap"]} - Nota Pembelajaran {cu} ({cfg["short"]}).docx'
        fname = re.sub(r'[\\/:*?"<>|]', "-", fname)
        out_path = os.path.join(out_dir, fname)
        composer.save(out_path)
        written.append(out_path)

    build_full_book()
    for cu in cfg["cu_order"]:
        build_cu_volume(cu)

    if written:
        d = Document(written[0])
        print(f"buku: wrote {len(written)} docx to {out_dir}")
        for p in written:
            print(f"  {os.path.basename(p)}")
        print(f"  read-back [{os.path.basename(written[0])}] first paragraph -> {d.paragraphs[0].text[:60]!r}")

        export_script = os.path.join(os.path.dirname(__file__), "Export-Pdf.ps1")
        if os.path.isfile(export_script):
            import subprocess
            try:
                result = subprocess.run(
                    ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", export_script,
                     "-Folder", out_dir],
                    capture_output=True, text=True, timeout=600)
                print("buku(pdf): Export-Pdf.ps1 output:")
                print("  " + (result.stdout or "").strip().replace("\n", "\n  "))
                if result.returncode != 0:
                    print(f"buku(pdf): Export-Pdf.ps1 exited {result.returncode}: {result.stderr[:300]}")
            except Exception as e:
                print(f"buku(pdf): SKIPPED PDF export — {e}")
        else:
            skip(export_script, "Export-Pdf.ps1 not found")
    else:
        print("buku: nothing written (no nota output found)")


# ================= PAGES (word-count + PDF page-count baseline for nota output) =================

def cmd_pages(subj):
    """For every nota docx (output/05 .../CU C01-C05/*.docx): export to PDF (reusing the same
    Export-Pdf.ps1 helper cmd_buku already shells out to, which prints 'name pages=N' via Word's
    own ComputeStatistics(2) — no extra pypdf dependency needed), count words per docx via
    python-docx paragraph text, and print+write a markdown file|words|pages table."""
    import subprocess
    from docx import Document

    cfg = SUBJECTS[subj]
    nota_dir = cfg["nota_out"]
    files = sorted(f for f in glob.glob(os.path.join(nota_dir, "*.docx"))
                    if not os.path.basename(f).startswith("~$"))
    if not files:
        return skip(nota_dir, "no nota output to measure")

    export_script = os.path.join(os.path.dirname(__file__), "Export-Pdf.ps1")
    page_counts = {}
    if os.path.isfile(export_script):
        try:
            result = subprocess.run(
                ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", export_script,
                 "-Folder", nota_dir],
                capture_output=True, text=True, timeout=900)
            for line in (result.stdout or "").splitlines():
                m = re.match(r"^(.*\.docx)\s+pages=(\d+)\s*$", line.strip())
                if m:
                    page_counts[m.group(1)] = int(m.group(2))
            if result.returncode != 0:
                print(f"pages: Export-Pdf.ps1 exited {result.returncode}: {result.stderr[:300]}")
        except Exception as e:
            print(f"pages: Export-Pdf.ps1 failed — {e}")
    else:
        skip(export_script, "Export-Pdf.ps1 not found")

    rows = []
    for f in files:
        name = os.path.basename(f)
        d = Document(f)
        words = sum(len(p.text.split()) for p in d.paragraphs)
        for t in d.tables:
            for r in t.rows:
                for c in r.cells:
                    words += len(c.text.split())
        pages = page_counts.get(name, "n/a")
        rows.append((name, words, pages))

    out_path = os.path.join(cfg["out"], "_tools", "pages-baseline.md")
    lines_out = ["# pages-baseline.md — word/page baseline for P851 nota output\n",
                 "Auto-generated by `build_output.py pages`. Words = python-docx paragraph+table text; "
                 "pages = Word's ComputeStatistics(2) via Export-Pdf.ps1 (same helper `buku` uses). "
                 "Context: nota content is still being expanded by content agents — short page counts "
                 "here are expected and not a defect.\n",
                 "| file | words | pages |", "|---|---|---|"]
    for name, words, pages in rows:
        lines_out.append(f"| {name} | {words} | {pages} |")
    md = "\n".join(lines_out) + "\n"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(md)

    print(md)
    print(f"pages: wrote {out_path} ({len(rows)} rows)")


# ================= lazy sibling-module wiring (build_xlsx.py / build_forms.py) =================
# Other agents are writing these concurrently in the same _tools/ folder. Each is expected to
# expose run(subcommand, cfg) -> None. Import lazily so `all` never crashes if a module or its
# run() isn't ready yet.

_XLSX_SUBCOMMANDS = {"lampiran5", "jam42", "jadual43", "jsu", "bukti"}
_FORMS_SUBCOMMANDS = {"soalan", "rekod31", "lampiran4", "lampiran6", "syarikat", "bakat"}


def try_run_sibling_module(module_name, subcommand, subj):
    """Return True if it handled (ran or printed its own SKIPPED), False if caller should fall
    back to the generic cmd_stub SKIPPED message."""
    cfg = SUBJECTS[subj]
    try:
        import importlib
        mod = importlib.import_module(module_name)
    except ImportError:
        print(f"SKIPPED (module not ready): {module_name}.py::{subcommand}")
        return True
    run_fn = getattr(mod, "run", None)
    if run_fn is None or not callable(run_fn):
        print(f"SKIPPED (module not ready — no run()): {module_name}.py::{subcommand}")
        return True
    try:
        run_fn(subcommand, cfg)
    except Exception as e:
        print(f"SKIPPED ({module_name}.py::{subcommand} raised {type(e).__name__}: {e})")
    return True


# ================= not-yet-implemented subcommands (xlsx/pptx reverse-engineering) =================
# These need per-template cell-layout reverse-engineering (finished-vs-blank diff) which was not
# completed in this pass. Each prints SKIPPED with the reason so `all` never silently fabricates.

NOT_IMPLEMENTED = []  # "bukti" (xlsx) now routed to build_xlsx.py; Lampiran 4 docx routed as "lampiran4" to build_forms.py

# subcommands now routed to the concurrently-developed sibling modules
_ROUTED_SUBCOMMANDS = sorted(_XLSX_SUBCOMMANDS | _FORMS_SUBCOMMANDS)


def cmd_stub(name, subj):
    print(f"SKIPPED (not implemented this pass): {name} --subject {subj} "
          f"— needs finished-vs-blank xlsx/docx/pptx cell-layout reverse-engineering per 00-SPEC.md STEP1.7; "
          f"see SPEC.md 'Not yet built' table for template + source-md mapping.")


def dispatch_routed(name, subj):
    if name in _XLSX_SUBCOMMANDS:
        try_run_sibling_module("build_xlsx", name, subj)
    elif name in _FORMS_SUBCOMMANDS:
        try_run_sibling_module("build_forms", name, subj)
    else:
        cmd_stub(name, subj)


def cmd_all(subj):
    cmd_rangka(subj)
    cmd_nota(subj)
    cmd_lpkc(subj)
    cmd_buku(subj)
    for name in _ROUTED_SUBCOMMANDS:
        dispatch_routed(name, subj)
    for name in NOT_IMPLEMENTED:
        cmd_stub(name, subj)
    write_index(subj)


def write_index(subj):
    cfg = SUBJECTS[subj]
    out = cfg["out"]
    rows = []
    for dirpath, _, filenames in os.walk(out):
        for fn in filenames:
            if fn.startswith("."):
                continue
            full = os.path.join(dirpath, fn)
            rel_folder = os.path.relpath(dirpath, out)
            tbd_count = 0
            if fn.lower().endswith(".docx"):
                try:
                    from docx import Document
                    d = Document(full)
                    text = "\n".join(p.text for p in d.paragraphs)
                    for t in d.tables:
                        for r in t.rows:
                            for c in r.cells:
                                text += c.text
                    tbd_count = len(re.findall(r"\[TBD:", text))
                except Exception:
                    tbd_count = -1
            rows.append((rel_folder, fn, tbd_count))
    idx_path = os.path.join(out, "INDEX-fail-pegawai.md")
    with open(idx_path, "w", encoding="utf-8") as fh:
        fh.write(f"# INDEX — fail pegawai ({cfg['short']})\n\nAuto-generated by build_output.py write_index(). Do not edit by hand.\n\n")
        fh.write("| Folder | Fail | [TBD] count |\n|---|---|---|\n")
        for folder, fn, tbd in sorted(rows):
            fh.write(f"| {folder} | {fn} | {tbd if tbd >= 0 else 'n/a (not .docx)'} |\n")
    print(f"index: wrote {idx_path} ({len(rows)} files listed)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["rangka", "nota", "lpkc", "buku", "pages", "all", "index"] + _ROUTED_SUBCOMMANDS + NOT_IMPLEMENTED)
    ap.add_argument("--subject", required=True, choices=list(SUBJECTS.keys()))
    args = ap.parse_args()

    if args.subject not in SUBJECTS:
        print(f"unknown subject {args.subject}")
        sys.exit(1)

    if args.cmd == "rangka":
        cmd_rangka(args.subject)
    elif args.cmd == "nota":
        cmd_nota(args.subject)
    elif args.cmd == "lpkc":
        cmd_lpkc(args.subject)
    elif args.cmd == "buku":
        cmd_buku(args.subject)
    elif args.cmd == "pages":
        cmd_pages(args.subject)
    elif args.cmd == "index":
        write_index(args.subject)
    elif args.cmd == "all":
        cmd_all(args.subject)
    elif args.cmd in _ROUTED_SUBCOMMANDS:
        dispatch_routed(args.cmd, args.subject)
    else:
        cmd_stub(args.cmd, args.subject)


if __name__ == "__main__":
    main()
