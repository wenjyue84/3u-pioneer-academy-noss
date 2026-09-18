"""
build_forms.py -- extra officer-form generators for preschool-teaching (P851-002-4:2025).

Reuses SUBJECTS config, tbd_normalize(), clean_inline() etc. from build_output.py (same folder).
Never edits build_output.py or build_xlsx.py -- import only.

Run: uv run --with python-docx --with python-pptx python build_forms.py <subcommand> --subject preschool-teaching
Subcommands: soalan, rekod31, lampiran4, lampiran6, lpkc, syarikat, bakat, all
"""
import os
import re
import sys
import glob
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_output import SUBJECTS, ROOT, tbd_normalize, clean_inline, skip  # noqa: E402
import build_output as BO  # for cmd_lpkc reuse

RAW_TPL = os.path.join(ROOT, "raw", "adi-mpc-template-2026-09")
TPL_4PK = os.path.join(RAW_TPL, "4-pelaksanaan-kompilasi")
TPL_FS = os.path.join(RAW_TPL, "2-fail-syarikat")
TPL_CA = os.path.join(RAW_TPL, "core-abilities", "_txt")

SOALAN_TEMPLATE = os.path.join(TPL_4PK, "3.4b Template Penilaian Pengetahuan.docx")
REKOD31_TEMPLATE = os.path.join(TPL_4PK, "3.1 Bukti Penilaian Pengetahuan.docx")
LAMPIRAN4_TEMPLATE = os.path.join(TPL_4PK, "2 Borang Perakuan Pembimbing.docx")
LAMPIRAN6_TEMPLATE = os.path.join(TPL_4PK, "1.1 Borang Laporan Penilaian Bukti Kekompetenan.docx")

SYARIKAT_ISI_TPL = os.path.join(TPL_FS, "0_Isi Kandungan Fail Pelaksanaan ADI Pekerjaan.docx")
SYARIKAT_TAWARAN_TPL = os.path.join(TPL_FS, "3.1a Surat Tawaran Kerja BAKAT.docx")
SYARIKAT_PELANTIKAN_TPL = os.path.join(TPL_FS, "5 Contoh surat pelantikan personel ADI.docx")

PROSES_MD = os.path.join(ROOT, "preschool-teaching", "01-proses-kerja.md")
PENILAIAN_MD = os.path.join(ROOT, "preschool-teaching", "09-penilaian-kekompetenan.md")
BUKTI_MD = os.path.join(ROOT, "preschool-teaching", "08-senarai-bukti-proses-kerja.md")
SUSUNAN_MD = os.path.join(ROOT, "preschool-teaching", "10-susunan-fail-kompilasi.md")
SOALAN_DIR = os.path.join(ROOT, "preschool-teaching", "07-soalan-penilaian-pengetahuan")

TBD_SYARIKAT = "[TBD: nama tadika/syarikat | Jay | sebelum cetak]"


# ---------------- Core Abilities inventory (L1-L4 titles, per task spec) ----------------
CA_TITLES = {
    "L1": [
        ("CA01", "BASIC WORKING COMMUNICATION"),
        ("CA02", "PERSONAL BEHAVIOUR SKILL"),
        ("CA03", "WORK PLACE ETHICS AWARENESS"),
        ("CA04", "HEALTH, SAFETY AND ENVIRONMENTAL AWARENESS"),
    ],
    "L2": [
        ("CA01", "COMMUNICATION APPLICATION"),
        ("CA02", "INTERPERSONAL BEHAVIOUR"),
        ("CA03", "WORK PLACE CULTURE BEHAVIOUR"),
        ("CA04", "HEALTH, SAFETY AND ENVIRONMENTAL ADAPTATION"),
    ],
    "L3": [
        ("CA01", "EFFECTIVE COMMUNICATION"),
        ("CA02", "INFORMATION TECHNOLOGY AWARENESS"),
        ("CA03", "LEADERSHIP SKILL"),
        ("CA04", "WORK PLACE ETHICS"),
        ("CA05", "ADMINISTRATIVE SKILL"),
        ("CA06", "HSE CONSCIOUSNESS"),
    ],
    "L4": [
        ("CA01", "ORGANISATIONAL BEHAVIOUR AWARENESS"),
        ("CA02", "HEALTH, SAFETY & ENVIRONMENT MONITORING"),
        ("CA03", "RELATIONSHIP MANAGEMENT CAPABILITY"),
        ("CA04", "ETIQUETTE PRACTICES"),
        ("CA05", "STRATEGIC THINKING SKILL"),
        ("CA06", "EFFECTIVE COMMUNICATION COLLABORATION"),
        ("CA07", "CHANGE MANAGEMENT AWARENESS"),
        ("CA08", "SYSTEM TECHNOLOGY APPLICATION"),
    ],
}
CA_CODE = {"L1": "Z-009-1:2015", "L2": "Z-009-2:2015", "L3": "Z-009-3:2015", "L4": "Z-009-4:2015"}


def set_cell(cell, text, bold=None):
    text = tbd_normalize(str(text))
    for p in cell.paragraphs[1:]:
        p._element.getparent().remove(p._element)
    p = cell.paragraphs[0]
    for r in p.runs[1:]:
        r._element.getparent().remove(r._element)
    if p.runs:
        r = p.runs[0]
        r.text = text
    else:
        r = p.add_run(text)
    if bold is not None:
        r.bold = bold


def parse_hdr_table(md_path):
    """Parse the leading '| KEY | VAL |' block of a 07-soalan Cxx.md file into a dict."""
    text = open(md_path, encoding="utf-8").read()
    hdr = {}
    for ln in text.split("\n"):
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$", ln)
        if m and "---" not in m.group(1):
            hdr[m.group(1).strip()] = m.group(2).strip()
    return hdr, text


def get_section(text, tag, next_tags):
    pat = rf"## {re.escape(tag)}\s*\n(.*?)(?=" + "|".join(rf"## {re.escape(t)}" for t in next_tags) + r"|\Z)"
    m = re.search(pat, text, re.S)
    return m.group(1).strip() if m else ""


# ================= 1. soalan (3.4b) =================

def cmd_soalan(subj):
    from docx import Document
    from docx.enum.text import WD_BREAK

    cfg = SUBJECTS[subj]
    if not os.path.isfile(SOALAN_TEMPLATE):
        return skip(SOALAN_TEMPLATE, "template missing")

    out_dir = os.path.join(cfg["out"], "07 3.4b Soalan Penilaian Pengetahuan", "CU C01-C05")
    os.makedirs(out_dir, exist_ok=True)

    def clear_sample_body(doc):
        paras = doc.paragraphs
        start = None
        for i, p in enumerate(paras):
            if p.text.strip() == "Soalan WA1":
                start = i
                break
        if start is None:
            raise RuntimeError("Anchor 'Soalan WA1' not found in 3.4b template")
        for p in paras[start:]:
            el = p._element
            parent = el.getparent()
            if parent is not None:
                parent.remove(el)

    def add_para(doc, text="", bold=False, size=None):
        p = doc.add_paragraph()
        if text:
            r = p.add_run(tbd_normalize(text))
            r.bold = bold
            if size:
                from docx.shared import Pt
                r.font.size = Pt(size)
        return p

    def add_page_break(doc):
        p = doc.add_paragraph()
        r = p.add_run()
        r.add_break(WD_BREAK.PAGE)

    def add_table(doc, rows, bold_header=True):
        if not rows:
            return
        ncols = max(len(r) for r in rows)
        t = doc.add_table(rows=len(rows), cols=ncols)
        try:
            t.style = "Table Grid"
        except KeyError:
            pass
        for ri, row in enumerate(rows):
            for ci, val in enumerate(row):
                if ci < ncols:
                    set_cell(t.cell(ri, ci), val, bold=(bold_header and ri == 0) or None)
        return t

    def fill_header(doc, prog, cu, tempoh, jumlah, lulus):
        t = doc.tables[0]
        rows = {r.cells[0].text.strip(): r for r in t.rows}
        set_cell(rows["NAMA SYARIKAT"].cells[1], TBD_SYARIKAT)
        set_cell(rows["NAMA PUSAT LATIHAN"].cells[1], "3U Pioneer Academy Sdn Bhd")
        set_cell(rows["NAMA & KOD PROGRAM"].cells[1], prog)
        set_cell(rows["NAMA & KOD CU"].cells[1], cu)
        set_cell(rows["TEMPOH PENILAIAN"].cells[1], tempoh)
        # append JUMLAH SOALAN / MARKAH LULUS as a small block after the header table
        return jumlah, lulus

    def render_table_block(doc, block_text):
        lines = [ln for ln in block_text.split("\n") if ln.strip().startswith("|")]
        rows = []
        for ln in lines:
            if re.match(r"^\|[\s:\-|]+\|$", ln.strip()):
                continue
            rows.append([clean_inline(c.strip()) for c in ln.strip().strip("|").split("|")])
        add_table(doc, rows)

    def render_paragraphs(doc, block_text):
        for raw in block_text.split("\n"):
            s = raw.strip()
            if not s:
                continue
            if s == "---":
                continue
            add_para(doc, clean_inline(s))

    def build_one(md_path, out_path, seq, cu_title):
        hdr, text = parse_hdr_table(md_path)
        prog = hdr.get("NAMA & KOD PROGRAM", f'{cfg["title"]} \u2014 {cfg["code"]}')
        cu = hdr.get("NAMA & KOD CU", "[TBD: CU]")
        tempoh = hdr.get("TEMPOH PENILAIAN", "1 JAM")
        jumlah = hdr.get("JUMLAH SOALAN", "2 SOALAN SUBJEKTIF (1 STRUKTUR + 1 ESEI) \u2014 40 MARKAH")
        lulus = hdr.get("MARKAH LULUS", "60 % (24/40)")

        doc = Document(SOALAN_TEMPLATE)
        clear_sample_body(doc)
        fill_header(doc, prog, cu, tempoh, jumlah, lulus)
        add_para(doc, "")
        add_para(doc, f"JUMLAH SOALAN: {jumlah}", bold=True)
        add_para(doc, f"MARKAH LULUS: {lulus}", bold=True)
        add_para(doc, "")

        jsu = get_section(text, "JSU (Jadual Spesifikasi Ujian) \u2014 Subjektif", ["BAHAGIAN A"])
        bah_a = get_section(text, "BAHAGIAN A \u2014 SOALAN STRUKTUR (20 markah)", ["BAHAGIAN B"])
        bah_b = get_section(text, "BAHAGIAN B \u2014 SOALAN ESEI (20 markah)", ["SKEMA JAWAPAN"])
        skema = get_section(text, "SKEMA JAWAPAN", [])

        add_para(doc, "JSU (Jadual Spesifikasi Ujian) \u2014 Subjektif", bold=True, size=13)
        render_table_block(doc, jsu)
        add_para(doc, "")

        add_para(doc, "BAHAGIAN A \u2014 SOALAN STRUKTUR (20 markah)", bold=True, size=13)
        render_paragraphs(doc, bah_a)
        add_para(doc, "")

        add_para(doc, "BAHAGIAN B \u2014 SOALAN ESEI (20 markah)", bold=True, size=13)
        render_paragraphs(doc, bah_b)

        add_page_break(doc)
        add_para(doc, "SKEMA JAWAPAN", bold=True, size=14)
        # SKEMA has ### subsections + tables interleaved -> walk line by line
        lines = skema.split("\n")
        i, n = 0, len(lines)
        while i < n:
            raw = lines[i]
            s = raw.strip()
            if not s:
                i += 1
                continue
            m3 = re.match(r"^###\s+(.+)$", s)
            if m3:
                add_para(doc, clean_inline(m3.group(1)), bold=True, size=12)
                i += 1
                continue
            mb = re.match(r"^\*\*(.+?)\*\*$", s)
            if mb:
                add_para(doc, clean_inline(mb.group(1)), bold=True)
                i += 1
                continue
            if s.startswith("|"):
                table_lines = []
                j = i
                while j < n and lines[j].strip().startswith("|"):
                    table_lines.append(lines[j].strip())
                    j += 1
                rows = [[clean_inline(c.strip()) for c in tl.strip("|").split("|")]
                        for tl in table_lines if not re.match(r"^\|[\s:\-|]+\|$", tl)]
                add_table(doc, rows)
                i = j
                continue
            add_para(doc, clean_inline(s))
            i += 1

        doc.save(out_path)
        return prog, cu

    files = sorted(glob.glob(os.path.join(SOALAN_DIR, "C0?.md")))
    written = []
    for seq, f in enumerate(files, start=1):
        cu = os.path.basename(f).replace(".md", "")
        cu_title = cfg["cu_titles"].get(cu, "[TBD: CU title]")
        fname = f'3.4b-{seq:02d} Penilaian Pengetahuan {cu} {cu_title} ({cfg["short"]}).docx'
        fname = re.sub(r'[\\/:*?"<>|]', "-", fname)
        out_path = os.path.join(out_dir, fname)
        prog, cuv = build_one(f, out_path, seq, cu_title)
        written.append(out_path)

    print(f"soalan: wrote {len(written)} files to {out_dir}")
    pdf_ok = []
    if written:
        d = Document(written[0])
        print(f"  read-back [{os.path.basename(written[0])}] table0 CU cell -> {d.tables[0].rows[4].cells[1].text!r}")
        body_text = "\n".join(p.text for p in d.paragraphs)
        print(f"  read-back contains 'BAHAGIAN A' -> {'BAHAGIAN A' in body_text}")
        print(f"  read-back contains 'SKEMA JAWAPAN' -> {'SKEMA JAWAPAN' in body_text}")

        # PDF export via Export-Pdf.ps1
        export_ps1 = os.path.join(os.path.dirname(__file__), "Export-Pdf.ps1")
        if os.path.isfile(export_ps1):
            import subprocess
            for p in written:
                try:
                    r = subprocess.run(
                        ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", export_ps1, p],
                        capture_output=True, text=True, timeout=120)
                    pdf_path = os.path.splitext(p)[0] + ".pdf"
                    if os.path.isfile(pdf_path):
                        pdf_ok.append(pdf_path)
                    else:
                        print(f"  PDF export FAILED for {os.path.basename(p)}: {r.stdout[-300:]} {r.stderr[-300:]}")
                except Exception as e:
                    print(f"  PDF export EXCEPTION for {os.path.basename(p)}: {e}")
        else:
            print(f"  PDF export skipped: {export_ps1} not found")
    print(f"soalan: PDF produced for {len(pdf_ok)}/{len(written)} files")
    return written


# ================= 2. rekod31 (3.1 Bukti Penilaian Pengetahuan) =================

def cmd_rekod31(subj):
    from docx import Document
    import copy

    cfg = SUBJECTS[subj]
    if not os.path.isfile(REKOD31_TEMPLATE):
        return skip(REKOD31_TEMPLATE, "template missing")
    out_dir = os.path.join(cfg["out"], "08 3.1 Bukti Rekod Penilaian Pengetahuan")
    os.makedirs(out_dir, exist_ok=True)

    doc = Document(REKOD31_TEMPLATE)

    # -- header paragraphs block 1 (CU) --
    for p in doc.paragraphs:
        t = p.text
        if t.startswith("NAMA PUSAT LATIHAN:"):
            p.runs[-1].text = "3U Pioneer Academy Sdn Bhd" if p.runs else None
            if p.runs:
                p.runs[0].text = "NAMA PUSAT LATIHAN:\t3U Pioneer Academy Sdn Bhd"
        elif t.startswith("NAMA SYARIKAT:"):
            if p.runs:
                p.runs[0].text = f"NAMA SYARIKAT:\t\t{TBD_SYARIKAT}"
        elif t.startswith("KOD PROGRAM:"):
            if p.runs:
                p.runs[0].text = f'KOD PROGRAM:\t\t{cfg["code"]}'
        elif t.startswith("NAMA PROGRAM:") and "CORE ABILITIES" not in t:
            if p.runs:
                p.runs[0].text = f'NAMA PROGRAM:\t\t{cfg["title"]}'
        elif t.startswith("TAHAP PROGRAM:"):
            if p.runs:
                p.runs[0].text = f'TAHAP PROGRAM:\t\tTAHAP {cfg["tahap"]}'
        elif t.startswith("TARIKH MULA LATIHAN:"):
            if p.runs:
                p.runs[0].text = "TARIKH MULA LATIHAN:\t[TBD: tarikh mula latihan]"
        elif t.startswith("TARIKH TAMAT LATIHAN:"):
            if p.runs:
                p.runs[0].text = "TARIKH TAMAT LATIHAN:\t[TBD: tarikh tamat latihan]"

    # second block (Core Abilities header) - KOD PROGRAM/NAMA PROGRAM already correct (Z-009-4:2015);
    # only fix NAMA PUSAT LATIHAN / NAMA SYARIKAT / TAHAP PROGRAM / dates (2nd occurrence)
    seen_pusat = 0
    seen_syarikat = 0
    seen_tahap = 0
    seen_mula = 0
    seen_tamat = 0
    for p in doc.paragraphs:
        t = p.text
        if t.startswith("NAMA PUSAT LATIHAN:"):
            seen_pusat += 1
            if seen_pusat == 2 and p.runs:
                p.runs[0].text = "NAMA PUSAT LATIHAN:\t3U Pioneer Academy Sdn Bhd"
        elif t.startswith("NAMA SYARIKAT:"):
            seen_syarikat += 1
            if seen_syarikat == 2 and p.runs:
                p.runs[0].text = f"NAMA SYARIKAT:\t\t{TBD_SYARIKAT}"
        elif t.startswith("TAHAP PROGRAM:"):
            seen_tahap += 1
            if seen_tahap == 2 and p.runs:
                p.runs[0].text = f'TAHAP PROGRAM:\t\tTAHAP {cfg["tahap"]}'
        elif t.startswith("TARIKH MULA LATIHAN:"):
            seen_mula += 1
            if seen_mula == 2 and p.runs:
                p.runs[0].text = "TARIKH MULA LATIHAN:\t[TBD: tarikh mula latihan]"
        elif t.startswith("TARIKH TAMAT LATIHAN:"):
            seen_tamat += 1
            if seen_tamat == 2 and p.runs:
                p.runs[0].text = "TARIKH TAMAT LATIHAN:\t[TBD: tarikh tamat latihan]"

    # -- table 0: 5 CU rows (Struktur/Esei, 40 markah, lulus 24) --
    t0 = doc.tables[0]
    cu_order = cfg["cu_order"]
    # ensure enough rows (template has 6 data rows; we need 5) -> just reuse first 5, clear the 6th's text
    for i, cu in enumerate(cu_order):
        row = t0.rows[i + 1]
        set_cell(row.cells[1], f'PENILAIAN PENGETAHUAN \n{cfg["code"]}-{cu}')
        set_cell(row.cells[2], "1 Struktur + 1 Esei, 40 markah")
        set_cell(row.cells[3], "Lulus \u2265 24/40 (60%)")
    # 6th data row unused -> clear
    if len(t0.rows) > len(cu_order) + 1:
        for c in t0.rows[len(cu_order) + 1].cells:
            set_cell(c, "")

    # -- table 1: Core Abilities rows, need 22 (L1x4 + L2x4 + L3x6 + L4x8) --
    t1 = doc.tables[1]
    ca_flat = []
    for lvl in ("L1", "L2", "L3", "L4"):
        for code, title in CA_TITLES[lvl]:
            ca_flat.append((lvl, code, title))
    # existing data rows: index 1..6 (6 rows); need 22 -> add 16 more by cloning row 1's xml
    template_row = t1.rows[1]._tr
    while len(t1.rows) - 1 < len(ca_flat):
        new_tr = copy.deepcopy(template_row)
        t1._tbl.append(new_tr)
    for i, (lvl, code, title) in enumerate(ca_flat):
        row = t1.rows[i + 1]
        set_cell(row.cells[0], f"{i + 1}.")
        set_cell(row.cells[1], f"PENILAIAN PENGETAHUAN \n{CA_CODE[lvl]}-{code} {title}")
        set_cell(row.cells[2], "20 MCQ")
        set_cell(row.cells[3], "")

    out_path = os.path.join(out_dir, f'3.1_Bukti Penilaian Pengetahuan ({cfg["short"]}).docx')
    doc.save(out_path)

    d = Document(out_path)
    print(f"rekod31: wrote {out_path}")
    print(f"  read-back CU row1 -> {d.tables[0].rows[1].cells[1].text!r}")
    print(f"  read-back CA rows count -> {len(d.tables[1].rows) - 1} (expect 22)")
    print(f"  read-back CA row22 -> {d.tables[1].rows[22].cells[1].text!r}")
    return out_path


# ================= 3. lampiran4 (2 Borang Perakuan Pembimbing) =================

def cmd_lampiran4(subj):
    from docx import Document

    cfg = SUBJECTS[subj]
    if not os.path.isfile(LAMPIRAN4_TEMPLATE):
        return skip(LAMPIRAN4_TEMPLATE, "template missing")
    out_dir = os.path.join(cfg["out"], "09 4 Senarai Bukti Proses Kerja + Lampiran 4 Perakuan Pembimbing")
    os.makedirs(out_dir, exist_ok=True)

    proses_text = open(PROSES_MD, encoding="utf-8").read()
    p_titles = {}
    for m in re.finditer(r"^\|\s*(P\d\d)\s*\|\s*(.+?)\s*\|\s*C0\d", proses_text, re.M):
        p_titles[m.group(1)] = m.group(2).strip()

    doc = Document(LAMPIRAN4_TEMPLATE)
    t = doc.tables[0]
    # data rows 2..11 (0-idx), 4 P-columns each (0,2,4,6) with header in that same row (P1..P40) and
    # tick cell to the right (odd col). We only have P01-P12; mark the corresponding cells with a check
    # and leave header label as-is (official form goes to P40, spec says leave beyond P12 blank).
    for ri in range(2, 12):
        row = t.rows[ri]
        for base_col in (0, 2, 4, 6):
            label = row.cells[base_col].text.strip()
            m = re.match(r"^P(\d+)$", label)
            if not m:
                continue
            pnum = int(m.group(1))
            pkod = f"P{pnum:02d}"
            if pnum <= 12:
                title = p_titles.get(pkod, "")
                set_cell(row.cells[base_col], f"{pkod}" + (f" \u2014 {title}" if title else ""))
                set_cell(row.cells[base_col + 1], "\u2611")  # ticked: candidate completed all P01-P12
            # else (P13-P40): leave blank, not used by this NOSS

    out_path = os.path.join(out_dir, f'2_Borang Perakuan Pembimbing ADI Pekerjaan_JPK_ADI_01-2024 ({cfg["short"]}).docx')
    doc.save(out_path)

    d = Document(out_path)
    print(f"lampiran4: wrote {out_path}")
    print(f"  read-back P01 label -> {d.tables[0].rows[2].cells[0].text!r}")
    print(f"  read-back P01 tick -> {d.tables[0].rows[2].cells[1].text!r}")
    print(f"  read-back P12 label -> {d.tables[0].rows[11].cells[0].text!r}")
    return out_path


def parse_wa_evidence_table():
    """Parse '## Susunan Semula PK ke CU-WA' table in 08-senarai-bukti-proses-kerja.md.
    Returns {(CU, WA): "Bukti N, M, ..."}; CU column is forward-filled (blank = same as previous row)."""
    text = open(BUKTI_MD, encoding="utf-8").read()
    m = re.search(r"## Susunan Semula PK ke CU-WA.*?\n\|\s*CU\s*\|\s*WA\s*\|\s*No Bukti\s*\|\n(.*?)\n\n", text, re.S)
    if not m:
        return {}
    result = {}
    last_cu = None
    for ln in m.group(1).split("\n"):
        ln = ln.strip()
        if not ln.startswith("|") or "---" in ln:
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        if len(cells) < 3:
            continue
        cu, wa, bukti = cells[0], cells[1], cells[2]
        if cu:
            last_cu = cu
        if not last_cu or not wa or not bukti:
            continue
        result[(last_cu, wa)] = f"Bukti {bukti}"
    return result


# ================= 4. lampiran6 (1.1 Borang Laporan Penilaian Bukti Kekompetenan) =================

def cmd_lampiran6(subj):
    from docx import Document
    import copy

    cfg = SUBJECTS[subj]
    if not os.path.isfile(LAMPIRAN6_TEMPLATE):
        return skip(LAMPIRAN6_TEMPLATE, "template missing")
    out_dir = os.path.join(cfg["out"], "10 Lampiran 6 Laporan Penilaian Bukti Kekompetenan")
    os.makedirs(out_dir, exist_ok=True)

    doc = Document(LAMPIRAN6_TEMPLATE)

    # header candidate/programme info (table 0)
    t0 = doc.tables[0]
    set_cell(t0.rows[2].cells[1], cfg["code"])
    set_cell(t0.rows[3].cells[1], cfg["title"])

    # WA-level evidence rows: 21 WA total (C01 W01-04, C02 W01-05, C03 W01-04, C04 W01-05, C05 W01-03)
    wa_counts = {"C01": 4, "C02": 5, "C03": 4, "C04": 5, "C05": 3}
    wa_rows = []
    for cu in cfg["cu_order"]:
        for w in range(1, wa_counts[cu] + 1):
            wa_rows.append((cu, f"W{w:02d}"))

    wa_evidence = parse_wa_evidence_table()

    t2 = doc.tables[2]  # NO.CU/DUTI - NO.WA/TASK table, 3 header rows then data
    tmpl_row = t2.rows[3]._tr
    while len(t2.rows) - 3 < len(wa_rows):
        t2._tbl.append(copy.deepcopy(tmpl_row))
    for i, (cu, wa) in enumerate(wa_rows):
        row = t2.rows[i + 3]
        set_cell(row.cells[0], f"{i + 1}.")
        set_cell(row.cells[1], cu)
        set_cell(row.cells[2], wa)
        evid = wa_evidence.get((cu, wa), "")
        set_cell(row.cells[3], evid if evid else "[TBD: rujuk 08-senarai-bukti-proses-kerja.md]")

    # Core Abilities rows in table 3 -> 22 modules L1-L4
    t3 = doc.tables[3]
    ca_flat = []
    for lvl in ("L1", "L2", "L3", "L4"):
        for code, title in CA_TITLES[lvl]:
            ca_flat.append(f"{CA_CODE[lvl]}-{code}")
    tmpl_row3 = t3.rows[3]._tr
    while len(t3.rows) - 3 < len(ca_flat):
        t3._tbl.append(copy.deepcopy(tmpl_row3))
    for i, ca in enumerate(ca_flat):
        row = t3.rows[i + 3]
        set_cell(row.cells[0], f"{i + 1}.")
        set_cell(row.cells[1], ca)
        set_cell(row.cells[2], "")

    # Proses kerja (work-activity evidence) table -> table 7, P01-P12 rows with evidence codes from 09 section B
    penilaian_text = open(PENILAIAN_MD, encoding="utf-8").read()
    bagian_b = get_section(penilaian_text, "C3) Rekod Bukti Pengalaman Kerja", ["Pengesahan PPL-ADI komponen pengalaman kerja"])
    # fallback: parse the P0x rows table directly from section B/C3 by BIL/NO CU/NO WA/SENARAI KOD BUKTI
    p_evid_rows = []
    m_tbl = re.search(r"\| BIL \| NO\. CU \| NO\. WA \| SENARAI KOD BUKTI.*?\n(.*?)\n\nPengesahan", penilaian_text, re.S)
    if m_tbl:
        for ln in m_tbl.group(1).split("\n"):
            ln = ln.strip()
            if not ln.startswith("|") or "---" in ln:
                continue
            cells = [c.strip() for c in ln.strip("|").split("|")]
            if len(cells) >= 4:
                p_evid_rows.append(cells)

    t7 = doc.tables[7]
    # collapse into P01..P12 (join multi-WA rows under same BIL into one PROSES KERJA row w/ combined evidence)
    proses_text2 = open(PROSES_MD, encoding="utf-8").read()
    p_titles2 = {}
    for m in re.finditer(r"^\|\s*(P\d\d)\s*\|\s*(.+?)\s*\|\s*C0\d", proses_text2, re.M):
        p_titles2[m.group(1)] = m.group(2).strip()

    # walk p_evid_rows, forward-fill BIL/NO CU, group evidence by BIL (BIL maps 1:1 to CU not P-kod;
    # since 09.md section C3 groups by CU not by P-kod, fall back to 01-proses-kerja.md P01-P12 list directly)
    p_rows_final = [(pk, p_titles2.get(pk, "")) for pk in sorted(p_titles2, key=lambda x: int(x[1:]))]
    tmpl_row7 = t7.rows[3]._tr
    while len(t7.rows) - 3 < len(p_rows_final):
        t7._tbl.append(copy.deepcopy(tmpl_row7))
    for i, (pk, title) in enumerate(p_rows_final):
        row = t7.rows[i + 3]
        set_cell(row.cells[0], f"{i + 1}.")
        set_cell(row.cells[1], f"{pk} \u2014 {title}" if title else pk)
        set_cell(row.cells[2], "[TBD: senarai kod bukti sebenar (rujuk 08-senarai-bukti-proses-kerja.md)]")

    out_path = os.path.join(
        out_dir,
        f'1.1 Borang Laporan Penilaian Bukti Kekompetenan Calon Melalui Kaedah ADI Pekerjaan_JPK_ADI_03-2024 ({cfg["short"]}).docx')
    doc.save(out_path)

    d = Document(out_path)
    print(f"lampiran6: wrote {out_path}")
    print(f"  read-back KOD NOSS -> {d.tables[0].rows[2].cells[1].text!r}")
    print(f"  read-back WA rows -> {len(d.tables[2].rows) - 3} (expect 21)")
    for idx in (0, 5, 20):
        r = d.tables[2].rows[idx + 3]
        print(f"    WA row {idx+1}: {[c.text for c in r.cells]}")
    print(f"  read-back CA rows -> {len(d.tables[3].rows) - 3} (expect 22)")
    print(f"  read-back proses kerja rows -> {len(d.tables[7].rows) - 3} (expect 12)")
    return out_path


# ================= 5. lpkc (reuse build_output.cmd_lpkc) =================

def cmd_lpkc(subj):
    return BO.cmd_lpkc(subj)


# ================= 6. syarikat (Fail Pelaksanaan ADI - Syarikat) =================

def cmd_syarikat(subj):
    from docx import Document

    cfg = SUBJECTS[subj]
    out_dir = os.path.join(cfg["out"], "11 Fail Pelaksanaan ADI (Syarikat)")
    os.makedirs(out_dir, exist_ok=True)
    written = []

    susunan_text = open(SUSUNAN_MD, encoding="utf-8").read()
    section_a = get_section(susunan_text, "A. Fail Pelaksanaan ADI Pekerjaan (satu untuk tadika/syarikat / program)",
                             ["B. Fail Kompilasi Kemahiran Kerja"])

    # -- 0_Isi Kandungan --
    if os.path.isfile(SYARIKAT_ISI_TPL):
        doc = Document(SYARIKAT_ISI_TPL)
        t = doc.tables[0]
        rows_a = [ln for ln in section_a.split("\n") if ln.strip().startswith("|") and "---" not in ln]
        parsed = []
        for ln in rows_a[1:]:
            cells = [clean_inline(c.strip()) for c in ln.strip().strip("|").split("|")]
            if len(cells) >= 4 and cells[0].isdigit():
                parsed.append(cells)
        for row_data in parsed:
            bahagian = row_data[0]
            for row in t.rows[1:]:
                if row.cells[0].text.strip().rstrip(".") == bahagian:
                    set_cell(row.cells[1], tbd_normalize(row_data[1]))
                    break
        out_path = os.path.join(out_dir, f'0_Isi Kandungan ({cfg["short"]}).docx')
        doc.save(out_path)
        written.append(out_path)
    else:
        skip(SYARIKAT_ISI_TPL, "template missing")

    # -- 3.1a Surat Tawaran Kerja BAKAT (instructional stub template; fill placeholder header only) --
    if os.path.isfile(SYARIKAT_TAWARAN_TPL):
        doc = Document(SYARIKAT_TAWARAN_TPL)
        doc.add_paragraph("")
        p = doc.add_paragraph()
        r = p.add_run(f'Program: {cfg["code"]} {cfg["title"]} \u2014 Tahap {cfg["tahap"]}')
        r.bold = True
        doc.add_paragraph(tbd_normalize("Nama Syarikat: \u27ea TBD: nama tadika/syarikat \u27eb"))
        doc.add_paragraph(tbd_normalize("Nama Bakat / No. KP: \u27ea TBD: nama bakat | No. KP \u27eb"))
        out_path = os.path.join(out_dir, f'3.1a Surat Tawaran Kerja BAKAT ({cfg["short"]}).docx')
        doc.save(out_path)
        written.append(out_path)
    else:
        skip(SYARIKAT_TAWARAN_TPL, "template missing")

    # -- 5 Contoh surat pelantikan personel ADI --
    if os.path.isfile(SYARIKAT_PELANTIKAN_TPL):
        doc = Document(SYARIKAT_PELANTIKAN_TPL)
        for p in doc.paragraphs:
            if p.text.strip().startswith("Nama Syarikat"):
                if p.runs:
                    p.runs[-1].text = " [TBD: nama tadika/syarikat]"
        t = doc.tables[0]
        for ri in range(1, 5):  # Pembimbing/Pengajar/Penyelaras Syarikat/Penyelaras Pusat Latihan rows
            set_cell(t.rows[ri].cells[3], f'{cfg["code"]} {cfg["title"]}')
        out_path = os.path.join(out_dir, f'5 Contoh surat pelantikan personel ADI ({cfg["short"]}).docx')
        doc.save(out_path)
        written.append(out_path)
    else:
        skip(SYARIKAT_PELANTIKAN_TPL, "template missing")

    print(f"syarikat: wrote {len(written)} files to {out_dir}")
    for p in written:
        d = Document(p)
        first_nonempty = next((pp.text for pp in d.paragraphs if pp.text.strip()), "")
        print(f"  read-back [{os.path.basename(p)}] -> {first_nonempty[:80]!r}")
    return written


# ================= 7. bakat (Fail Kompilasi Kemahiran Kerja) =================

def cmd_bakat(subj):
    from docx import Document
    from docx.shared import Pt

    cfg = SUBJECTS[subj]
    out_dir = os.path.join(cfg["out"], "12 Fail Kompilasi Kemahiran Kerja (Bakat)")
    os.makedirs(out_dir, exist_ok=True)
    written = []

    # -- 1_Muka Hadapan (cover page, built from scratch, python-docx) --
    doc = Document()
    for text, size, bold in [
        ("FAIL KOMPILASI KEMAHIRAN KERJA", 20, True),
        ("(ADI Pekerjaan)", 14, False),
        ("", 12, False),
        (f'KOD PROGRAM: {cfg["code"]}', 14, True),
        (f'NAMA PROGRAM: {cfg["title"]} TAHAP {cfg["tahap"]}', 14, True),
        ("", 12, False),
        ("NAMA CALON: [TBD: nama calon]", 13, False),
        ("NO. KAD PENGENALAN: [TBD: no. kad pengenalan]", 13, False),
        ("NAMA PUSAT LATIHAN: 3U Pioneer Academy Sdn Bhd", 13, False),
        (f"NAMA TADIKA/SYARIKAT: {TBD_SYARIKAT}", 13, False),
    ]:
        p = doc.add_paragraph()
        p.alignment = 1  # center
        if text:
            r = p.add_run(text)
            r.bold = bold
            r.font.size = Pt(size)
    out_path1 = os.path.join(out_dir, f'1_Muka Hadapan Kompilasi Kemahiran Kerja ({cfg["short"]}).docx')
    doc.save(out_path1)
    written.append(out_path1)

    # -- 2_Isi Kandungan.pptx --
    from pptx import Presentation
    from pptx.util import Inches, Pt as PPt

    susunan_text = open(SUSUNAN_MD, encoding="utf-8").read()
    section_b = get_section(susunan_text, "B. Fail Kompilasi Kemahiran Kerja (satu untuk setiap Bakat)", ["C. Peta"])
    rows_b = [ln for ln in section_b.split("\n") if ln.strip().startswith("|") and "---" not in ln]
    entries = []
    for ln in rows_b[1:]:
        cells = [clean_inline(c.strip()) for c in ln.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0].isdigit():
            entries.append((cells[0], cells[1]))

    prs = Presentation()
    blank = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank)
    tb = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(0.8))
    tf = tb.text_frame
    tf.text = f'ISI KANDUNGAN \u2014 FAIL KOMPILASI KEMAHIRAN KERJA ({cfg["short"]})'
    tf.paragraphs[0].font.size = PPt(24)
    tf.paragraphs[0].font.bold = True

    body = slide.shapes.add_textbox(Inches(0.5), Inches(1.3), Inches(9), Inches(5.5))
    btf = body.text_frame
    btf.word_wrap = True
    first = True
    for no, content in entries:
        para = btf.paragraphs[0] if first else btf.add_paragraph()
        first = False
        para.text = f"{no}. {tbd_normalize(content)}"
        para.font.size = PPt(14)
    # LPKC entry explicit line (already included as item 10 from section_b, but ensure present)
    if not any(no == "10" for no, _ in entries):
        para = btf.add_paragraph()
        para.text = "10. LPKC (Laporan Projek Kompetensi Calon) \u2014 khusus DKM"
        para.font.size = PPt(14)

    out_path2 = os.path.join(out_dir, f'2_Isi Kandungan ({cfg["short"]}).pptx')
    prs.save(out_path2)
    written.append(out_path2)

    # -- 3_Fail Separator (P01-P12 titles, one per page) --
    proses_text = open(PROSES_MD, encoding="utf-8").read()
    p_titles = {}
    for m in re.finditer(r"^\|\s*(P\d\d)\s*\|\s*(.+?)\s*\|\s*C0\d", proses_text, re.M):
        p_titles[m.group(1)] = m.group(2).strip()

    doc3 = Document()
    ordered = sorted(p_titles, key=lambda x: int(x[1:]))
    for i, pk in enumerate(ordered):
        p = doc3.add_paragraph()
        p.alignment = 1
        r = p.add_run(pk)
        r.bold = True
        r.font.size = Pt(28)
        p2 = doc3.add_paragraph()
        p2.alignment = 1
        r2 = p2.add_run(p_titles[pk])
        r2.font.size = Pt(16)
        if i < len(ordered) - 1:
            from docx.enum.text import WD_BREAK
            br_p = doc3.add_paragraph()
            br_p.add_run().add_break(WD_BREAK.PAGE)
    out_path3 = os.path.join(out_dir, f'3_Fail Separator (Color Paper) ({cfg["short"]}).docx')
    doc3.save(out_path3)
    written.append(out_path3)

    print(f"bakat: wrote {len(written)} files to {out_dir}")
    d1 = Document(out_path1)
    print(f"  read-back [{os.path.basename(out_path1)}] -> {d1.paragraphs[3].text!r}")
    prs2 = Presentation(out_path2)
    slide0 = prs2.slides[0]
    texts = [sh.text_frame.text[:60] for sh in slide0.shapes if sh.has_text_frame]
    print(f"  read-back [{os.path.basename(out_path2)}] slide0 texts -> {texts}")
    d3 = Document(out_path3)
    print(f"  read-back [{os.path.basename(out_path3)}] first para -> {d3.paragraphs[0].text!r}")
    return written


# ================= main =================

SUBCOMMANDS = {
    "soalan": cmd_soalan,
    "rekod31": cmd_rekod31,
    "lampiran4": cmd_lampiran4,
    "lampiran6": cmd_lampiran6,
    "lpkc": cmd_lpkc,
    "syarikat": cmd_syarikat,
    "bakat": cmd_bakat,
}


def run(subcommand, cfg):
    """cfg: a subject-config dict as defined in build_output.SUBJECTS (not used directly here --
    subcommands look up SUBJECTS[subj] themselves for consistency with build_output.py, but we
    accept cfg for interface compliance and derive subj from cfg['short'] if needed)."""
    subj = None
    for k, v in SUBJECTS.items():
        if v is cfg or v == cfg:
            subj = k
            break
    if subj is None:
        raise ValueError("cfg not found in SUBJECTS; pass a dict from build_output.SUBJECTS")
    if subcommand == "all":
        for name, fn in SUBCOMMANDS.items():
            fn(subj)
        return
    fn = SUBCOMMANDS.get(subcommand)
    if fn is None:
        raise ValueError(f"unknown subcommand {subcommand}")
    return fn(subj)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject", required=True, choices=list(SUBJECTS.keys()))
    ap.add_argument("--subcommand", required=True, choices=list(SUBCOMMANDS.keys()) + ["all"])
    args = ap.parse_args()
    run(args.subcommand, SUBJECTS[args.subject])


if __name__ == "__main__":
    main()
