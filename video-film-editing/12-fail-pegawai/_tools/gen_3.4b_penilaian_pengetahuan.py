"""
Generate 3.4b Penilaian Pengetahuan (Word) papers from officer template.
Fills raw/adi-mpc-template-2026-09/4-pelaksanaan-kompilasi/3.4b Template Penilaian Pengetahuan.docx
with content parsed from:
  - video-film-editing/07-soalan-penilaian-pengetahuan/{C01..C05,E01}.md  -> 6 CU papers
  - video-film-editing/11-core-abilities/*/Soalan-*.md                   -> 14 Core Ability papers

Usage: uv run --with python-docx python gen_3.4b_penilaian_pengetahuan.py
"""
import copy
import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.oxml.ns import qn

ROOT = Path(r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss")
VFE = ROOT / "video-film-editing"
TEMPLATE = ROOT / "raw/adi-mpc-template-2026-09/4-pelaksanaan-kompilasi/3.4b Template Penilaian Pengetahuan.docx"

OUT_CU = VFE / "12-fail-pegawai/4. Pelaksanaan Kompilasi Kemahiran Kerja_Bakat/3.4b Penilaian Pengetahuan"
OUT_CA = VFE / "12-fail-pegawai/4. Pelaksanaan Kompilasi Kemahiran Kerja_Bakat/3.4b Penilaian Pengetahuan Core Abilities"
OUT_CU.mkdir(parents=True, exist_ok=True)
OUT_CA.mkdir(parents=True, exist_ok=True)

NAMA_PUSAT_LATIHAN = "3U Pioneer Academy Sdn Bhd"
NAMA_SYARIKAT = "[TBD: nama syarikat]"
PROGRAM_CU = "IT-072-3:2012 / VIDEO / FILM (EDITING)"


# ---------------------------------------------------------------- helpers --

def set_cell_text(cell, text, bold=None):
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
        r.font.name = "Arial"
    if bold is not None:
        r.bold = bold


def strip_md(text):
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = text.replace("`", "")
    return text.strip()


def add_para(doc, text="", bold=False, size=None, space_after=None):
    p = doc.add_paragraph()
    if text:
        r = p.add_run(text)
        r.font.name = "Arial"
        r.bold = bold
        if size:
            r.font.size = size
    if space_after is not None:
        p.paragraph_format.space_after = space_after
    return p


def add_page_break(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    r.add_break(WD_BREAK.PAGE)


def clear_sample_body(doc):
    """Remove sample question content, keep header tables + arahan block."""
    paras = doc.paragraphs
    start = None
    for i, p in enumerate(paras):
        if p.text.strip() == "Soalan WA1":
            start = i
            break
    if start is None:
        raise RuntimeError("Anchor 'Soalan WA1' not found in template")
    for p in paras[start:]:
        el = p._element
        parent = el.getparent()
        if parent is not None:
            parent.remove(el)


def fill_header(doc, nama_program, nama_cu, tempoh):
    table = doc.tables[0]
    rows = {r.cells[0].text.strip(): r for r in table.rows}
    set_cell_text(rows["NAMA SYARIKAT"].cells[1], NAMA_SYARIKAT)
    set_cell_text(rows["NAMA PUSAT LATIHAN"].cells[1], NAMA_PUSAT_LATIHAN)
    set_cell_text(rows["NAMA & KOD PROGRAM"].cells[1], nama_program)
    set_cell_text(rows["NAMA & KOD CU"].cells[1], nama_cu)
    set_cell_text(rows["TEMPOH PENILAIAN"].cells[1], tempoh)
    # NAMA BAKAT / NO KAD PENGENALAN / TARIKH PENILAIAN left blank for candidate


ARAS_MAP = {"rendah": "RENDAH", "sederhana": "SEDERHANA", "tinggi": "TINGGI"}
KONSTRUK_MAP = {
    "prosedur": "PROSEDUR",
    "fakta/teori": "FAKTA/TEORI",
    "sikap/kesel./persek.": "SIKAP / KESELAMATAN / PERSEKITARAN",
    "sikap/keselamatan/persekitaran": "SIKAP / KESELAMATAN / PERSEKITARAN",
}


# ------------------------------------------------------------ CU parsing --

def parse_cu_md(path: Path):
    text = path.read_text(encoding="utf-8")

    m = re.search(r"NAMA & KOD PROGRAM \| (.+?) \|", text)
    prog_raw = m.group(1).strip() if m else ""
    # "VIDEO / FILM (EDITING) — IT-072-3:2012" -> "IT-072-3:2012 / VIDEO / FILM (EDITING)"
    nama_program = PROGRAM_CU

    m = re.search(r"NAMA & KOD CU \| (.+?) \|", text)
    nama_cu = m.group(1).strip() if m else ""

    m = re.search(r"TEMPOH PENILAIAN \| (.+?) \|", text)
    tempoh = m.group(1).strip() if m else "30 MINIT"

    # Bahagian A block
    a_match = re.search(r"## BAHAGIAN A.*?\n(.*?)\n## BAHAGIAN B", text, re.S)
    section_a = a_match.group(1) if a_match else ""

    wa_blocks = re.split(r"\n### (Soalan WA\d+ — .+)\n", section_a)
    # wa_blocks[0] is preamble before first WA header; then alternating header, body
    was = []
    for i in range(1, len(wa_blocks), 2):
        header = wa_blocks[i].strip()
        body = wa_blocks[i + 1]
        wa_num = re.match(r"Soalan (WA\d+)", header).group(1)
        title = header.split("—", 1)[1].strip() if "—" in header else ""
        # split into individual questions
        q_chunks = re.split(r"\n\*\*Soalan (\d+)\*\* — (\w+) · (\S+) · (.+?)\n", body)
        questions = []
        for j in range(1, len(q_chunks), 5):
            num, wa, aras, konstruk = q_chunks[j:j + 4]
            qbody = q_chunks[j + 4]
            questions.append({
                "num": int(num), "wa": wa, "aras": aras.strip(),
                "konstruk": konstruk.strip(), "body": qbody.strip("\n"),
            })
        was.append({"wa": wa_num, "title": title, "questions": questions})

    # Bahagian B skema table
    b_match = re.search(r"## BAHAGIAN B.*?\n(.*?)\n## BAHAGIAN C", text, re.S)
    section_b = b_match.group(1) if b_match else ""
    skema_rows = []
    for line in section_b.splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line or line.startswith("| No"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) >= 6 and cols[0].isdigit():
            skema_rows.append({"no": cols[0], "jawapan": cols[4], "rujukan": cols[5]})

    # Bahagian C JSU table
    c_match = re.search(r"## BAHAGIAN C.*?\n(.*?)(?:\n---|\Z)", text, re.S)
    section_c = c_match.group(1) if c_match else ""
    jsu_rows = []
    for line in section_c.splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line or line.startswith("| WA"):
            continue
        cols = [c.strip("*").strip() for c in line.strip("|").split("|")]
        if len(cols) >= 8:
            jsu_rows.append(cols)

    return {
        "nama_program": nama_program, "nama_cu": nama_cu, "tempoh": tempoh,
        "was": was, "skema_rows": skema_rows, "jsu_rows": jsu_rows,
    }


def render_question_body(doc, qbody):
    """qbody: stem line(s), optional I./II./... lines, options A-D, Jawapan line (dropped)."""
    lines = [l for l in qbody.splitlines()]
    stem_lines = []
    roman_lines = []
    option_lines = []
    i = 0
    n = len(lines)
    # collect stem until blank line or roman/option start
    while i < n:
        l = lines[i].strip()
        if l == "":
            i += 1
            continue
        if re.match(r"^[IVX]+\.\s", l):
            break
        if re.match(r"^[A-D]\.\s", l):
            break
        if l.lower().startswith("jawapan"):
            i += 1
            continue
        stem_lines.append(l)
        i += 1
    while i < n:
        l = lines[i].strip()
        if l == "":
            i += 1
            continue
        if re.match(r"^[IVX]+\.\s", l):
            roman_lines.append(l)
            i += 1
            continue
        break
    while i < n:
        l = lines[i].strip()
        if l == "":
            i += 1
            continue
        if re.match(r"^[A-D]\.\s", l):
            option_lines.append(l)
            i += 1
            continue
        if l.lower().startswith("jawapan"):
            i += 1
            continue
        i += 1

    for l in stem_lines:
        add_para(doc, strip_md(l))
    for l in roman_lines:
        add_para(doc, strip_md(l))
    for l in option_lines:
        add_para(doc, strip_md(l))
    add_para(doc, "")


def add_skema_table(doc, skema_rows, extra_cols=False):
    add_page_break(doc)
    add_para(doc, "BAHAGIAN B — SKEMA JAWAPAN", bold=True)
    add_para(doc, "")
    table = doc.add_table(rows=1, cols=3)
    table.style = "Table Grid"
    hdr = table.rows[0].cells
    hdr[0].text, hdr[1].text, hdr[2].text = "No", "Jawapan", "Rujukan"
    for row in skema_rows:
        cells = table.add_row().cells
        cells[0].text = row["no"]
        cells[1].text = row["jawapan"]
        cells[2].text = strip_md(row["rujukan"])
    add_para(doc, "")


def add_jsu_table(doc, jsu_rows):
    add_para(doc, "BAHAGIAN C — SEMAKAN JSU", bold=True)
    add_para(doc, "")
    header = ["WA", "Bil. Soalan", "Rendah", "Sederhana", "Tinggi", "Prosedur", "Fakta/Teori", "Sikap/Kesel./Persek."]
    table = doc.add_table(rows=1, cols=len(header))
    table.style = "Table Grid"
    for c, h in zip(table.rows[0].cells, header):
        c.text = h
    for row in jsu_rows:
        cells = table.add_row().cells
        for c, v in zip(cells, row):
            c.text = v


def build_cu_paper(md_path: Path, out_path: Path, cu_code: str):
    data = parse_cu_md(md_path)
    doc = Document(TEMPLATE)
    clear_sample_body(doc)
    fill_header(doc, data["nama_program"], data["nama_cu"], data["tempoh"])

    add_para(doc, "")
    add_para(doc, "BAHAGIAN A — SOALAN OBJEKTIF", bold=True)
    add_para(doc, "")
    for wa in data["was"]:
        add_para(doc, f"Soalan {wa['wa']} — {wa['title']}", bold=True)
        for q in wa["questions"]:
            aras_u = ARAS_MAP.get(q["aras"].lower(), q["aras"].upper())
            konstruk_u = KONSTRUK_MAP.get(q["konstruk"].lower(), q["konstruk"].upper())
            add_para(doc, f"\u2705 {q['num']}. SOALAN TAHAP {aras_u} \u2014 KONSTRUK {konstruk_u}", bold=True)
            render_question_body(doc, q["body"])

    add_skema_table(doc, data["skema_rows"])
    add_jsu_table(doc, data["jsu_rows"])

    doc.save(out_path)
    return data


# ------------------------------------------------------------ CA parsing --

def parse_ca_md(path: Path):
    text = path.read_text(encoding="utf-8")

    m = re.search(r"KOD UNIT CORE ABILITY \| (.+?) \|", text)
    kod = m.group(1).strip() if m else ""
    m = re.search(r"NAMA UNIT ABILITY \| (.+?) \|", text)
    nama = m.group(1).strip() if m else ""
    m = re.search(r"MASA \| (.+?) \|", text)
    masa = m.group(1).strip() if m else "30 minit"

    body_match = re.search(r"MUKA SURAT BERCETAK\s*\n---\s*\n(.*?)\n---\s*\n\*\*SKEMA JAWAPAN\*\*", text, re.S)
    body = body_match.group(1) if body_match else ""

    q_chunks = re.split(r"\n(\d+)\.\s", "\n" + body)
    questions = []
    for j in range(1, len(q_chunks), 2):
        num = q_chunks[j]
        qtext = q_chunks[j + 1].strip("\n")
        questions.append({"num": int(num), "body": qtext})

    skema_match = re.search(r"\*\*SKEMA JAWAPAN\*\*\s*\n\n(.*?)\n\n\*\*Markah", text, re.S)
    skema_section = skema_match.group(1) if skema_match else ""
    skema_rows = []
    for line in skema_section.splitlines():
        line = line.strip()
        if not line.startswith("|") or "---" in line or line.startswith("| No"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) >= 3 and cols[0].isdigit():
            skema_rows.append({"no": cols[0], "jawapan": cols[1], "rujukan": cols[2]})

    return {"kod": kod, "nama": nama, "masa": masa, "questions": questions, "skema_rows": skema_rows}


def render_ca_question_body(doc, qbody):
    lines = qbody.splitlines()
    stem_lines, roman_lines, option_lines = [], [], []
    i, n = 0, len(lines)
    while i < n:
        l = lines[i].strip()
        if l == "":
            i += 1
            continue
        if re.match(r"^[IVX]+\.\s", l) or re.match(r"^[A-D]\.\s", l):
            break
        stem_lines.append(l)
        i += 1
    while i < n:
        l = lines[i].strip()
        if l == "":
            i += 1
            continue
        if re.match(r"^[IVX]+\.\s", l):
            roman_lines.append(l)
            i += 1
            continue
        break
    while i < n:
        l = lines[i].strip()
        if l == "":
            i += 1
            continue
        if re.match(r"^[A-D]\.\s", l):
            option_lines.append(l)
        i += 1

    for l in stem_lines:
        add_para(doc, strip_md(l))
    for l in roman_lines:
        add_para(doc, strip_md(l))
    for l in option_lines:
        add_para(doc, strip_md(l))
    add_para(doc, "")


def build_ca_paper(md_path: Path, out_path: Path, ca_code: str, tempoh_override=None):
    data = parse_ca_md(md_path)
    doc = Document(TEMPLATE)
    clear_sample_body(doc)
    nama_program = f"Z-009-x:2015 / CORE ABILITIES ({PROGRAM_CU.split(' / ')[0]} VIDEO / FILM (EDITING))"
    nama_cu = f"{data['kod']} \u2014 {data['nama']}"
    tempoh = tempoh_override or ("60 MINIT" if "L3-CA03" in ca_code else "30 MINIT")
    fill_header(doc, nama_program, nama_cu, tempoh)

    add_para(doc, "")
    add_para(doc, "SOALAN PENILAIAN PENGETAHUAN (OBJEKTIF)", bold=True)
    add_para(doc, "")
    for q in data["questions"]:
        add_para(doc, f"\u2705 {q['num']}. SOALAN PENILAIAN PENGETAHUAN", bold=True)
        render_ca_question_body(doc, q["body"])

    add_skema_table(doc, data["skema_rows"])

    doc.save(out_path)
    return data


# --------------------------------------------------------------------- main

def main():
    cu_files = ["C01", "C02", "C03", "C04", "C05", "E01"]
    for i, code in enumerate(cu_files, start=1):
        md_path = VFE / f"07-soalan-penilaian-pengetahuan/{code}.md"
        data = parse_cu_md(md_path)
        # extract CU title from nama_cu "TITLE — CODE"
        parts = re.split(r"\s*[/\u2014]\s*", data["nama_cu"])
        code_pat = re.compile(r"^[A-Z0-9]+-\d+(-\d)?:\d{4}")
        title = next((p.strip() for p in parts if not code_pat.match(p.strip())), parts[0]).strip()
        out_name = f"3.4b-{i:02d} Penilaian Pengetahuan {code} {title} (IT-072).docx"
        out_path = OUT_CU / out_name
        build_cu_paper(md_path, out_path, code)
        print("CU:", out_path.name)

    ca_dirs = sorted((VFE / "11-core-abilities").iterdir())
    ca_dirs = [d for d in ca_dirs if d.is_dir()]
    i = 0
    for d in ca_dirs:
        m = re.match(r"(L\d-CA\d+)-(.+)", d.name)
        ca_code, slug = m.group(1), m.group(2)
        soalan_files = list(d.glob("Soalan-*.md"))
        if not soalan_files:
            print("MISSING soalan md for", d.name)
            continue
        md_path = soalan_files[0]
        i += 1
        data_probe = parse_ca_md(md_path)
        title = data_probe["nama"] or slug.replace("-", " ").title()
        out_name = f"3.4b-CA-{i:02d} Penilaian Pengetahuan {ca_code} {title} (IT-072).docx"
        out_path = OUT_CA / out_name
        build_ca_paper(md_path, out_path, ca_code)
        print("CA:", out_path.name)


if __name__ == "__main__":
    main()
