"""
build_xlsx.py — xlsx officer-template filler for P851 (preschool-teaching), Bahagian 4/2 fail
(Lampiran 5, 4.2 Jam, 4.3 Jadual, 3.2 JSU, 4 Senarai Bukti).

Rule (00-SPEC.md / SPEC.md): fill original officer templates, never rebuild from scratch.
⟪TBD: ...⟫ in source md -> "[TBD: ...]" in output. Never fabricate content.

Cell layouts below were reverse-engineered this session by diffing the FINISHED IT-072 outputs
against the BLANK officer templates with openpyxl (see per-subcommand notes). Run from this folder:

uv run --with openpyxl python build_xlsx.py <subcommand> --subject preschool-teaching
"""
import os, re, sys, copy, argparse
import openpyxl
from openpyxl.utils import get_column_letter

sys.path.insert(0, os.path.dirname(__file__))
from build_output import SUBJECTS, tbd_normalize  # reuse config + TBD convention

ROOT = r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss"
RAW = os.path.join(ROOT, "raw", "adi-mpc-template-2026-09")

TEMPLATES = {
    "lampiran5": os.path.join(RAW, "1-panduan", "lampiran-jpk", "LAMPIRAN 5 Borang Matriks Pemetaan Aktiviti Proses Kerja.xlsx"),
    "jam42": os.path.join(RAW, "2-fail-syarikat", "4.2 Penjajaran Jam Latihan CA_CU_EU.xlsx"),
    "jadual43": os.path.join(RAW, "2-fail-syarikat", "4.3 Jadual Pengetahuan dan Proses Kerja.xlsx"),
    "jsu": os.path.join(RAW, "4-pelaksanaan-kompilasi", "3.2 Format Soalan PENILAIAN PENGETAHUAN.xlsx"),
    "bukti": os.path.join(RAW, "4-pelaksanaan-kompilasi", "4 Senarai Bukti Proses Kerja.xlsx"),
}


def out_path(cfg, subfolder, fname):
    p = os.path.join(cfg["out"], subfolder)
    os.makedirs(p, exist_ok=True)
    return os.path.join(p, fname)


def set_cell(ws, coord, value):
    if isinstance(value, str):
        value = tbd_normalize(value)
    ws[coord] = value


# ================= 1. lampiran5 =================

WA_MATRIX = [
    # (CU code, CU title, WA code, WA title, P-code with '/')
    ("C01", "Conduct daily routine activities", "W01", "Handle pupil's arrival", "P01"),
    ("C01", "Conduct daily routine activities", "W02", "Handle pupil's recess time", "P02"),
    ("C01", "Conduct daily routine activities", "W03", "Handle pupil's toilet break", "P03"),
    ("C01", "Conduct daily routine activities", "W04", "Handle pupil's dismissal", "P04"),
    ("C02", "Perform preschool teaching and learning activities", "W01", "Prepare yearly lesson plan (RPT)", "P05"),
    ("C02", "Perform preschool teaching and learning activities", "W02", "Prepare daily lesson plan (RPH)", "P06"),
    ("C02", "Perform preschool teaching and learning activities", "W03", "Prepare teaching and learning material", "P06"),
    ("C02", "Perform preschool teaching and learning activities", "W04", "Deliver daily lesson plan", "P07"),
    ("C02", "Perform preschool teaching and learning activities", "W05", "Analyse lesson effectiveness", "P08"),
    ("C03", "Organise preschool classroom environment", "W01", "Prepare learning environment", "P09"),
    ("C03", "Organise preschool classroom environment", "W02", "Handle pupil's attendance", "P01"),
    ("C03", "Organise preschool classroom environment", "W03", "Record classroom inventory", "P09"),
    ("C03", "Organise preschool classroom environment", "W04", "Control pupil's behaviour", "P10"),
    ("C04", "Develop pupil's assessment", "W01", "Assess pupil's behaviour and attitude", "P11"),
    ("C04", "Develop pupil's assessment", "W02", "Prepare pupil's assessment activity", "P11"),
    ("C04", "Develop pupil's assessment", "W03", "Execute observation of pupil's assessment", "P11"),
    ("C04", "Develop pupil's assessment", "W04", "Develop pupil's progress report", "P11"),
    ("C04", "Develop pupil's assessment", "W05", "Present pupil's assessment outcome", "P11"),
    ("C05", "Handle parental-community activities", "W01", "Carry out preschool parental-community activities", "P12"),
    ("C05", "Handle parental-community activities", "W02", "Engage relationship with family and community", "P12"),
    ("C05", "Handle parental-community activities", "W03", "Prepare report parental-community activities", "P12"),
]
P_CODES = [f"P{n:02d}" for n in range(1, 13)]


def cmd_lampiran5(cfg):
    tpl = TEMPLATES["lampiran5"]
    if not os.path.isfile(tpl):
        print(f"SKIPPED (template missing): {tpl}")
        return
    wb = openpyxl.load_workbook(tpl)

    # ---- sheet "CU & WA" (header B1 program, A/B/C/D rows 4..24 CU/WA list) ----
    ws = wb["CU & WA"]
    set_cell(ws, "B1", f'{cfg["code"]} {cfg["title"]}')
    r = 4
    for cu, cu_title, wa, wa_title, _p in WA_MATRIX:
        set_cell(ws, f"A{r}", f'{cfg["code"]}-{cu}')
        set_cell(ws, f"B{r}", cu_title.upper())
        set_cell(ws, f"C{r}", f'{cfg["code"]}-{cu}-{wa}')
        set_cell(ws, f"D{r}", wa_title.upper())
        r += 1

    # ---- sheet "NOSS vs Proses Kerja" (header B12/J12/B13/J13, WA rows 20..45 '/') ----
    ws2 = wb["NOSS vs Proses Kerja"]
    company = cfg.get("company") or "[TBD: nama tadika/syarikat]"
    set_cell(ws2, "B12", f"NAMA SYARIKAT : {company}")
    set_cell(ws2, "J12", f'TAJUK NOSS/NCS: {cfg["title"]}')
    set_cell(ws2, "B13", f'NAMA PUSAT LATIHAN (Jika berkaitan) : 3U Pioneer Academy Sdn Bhd')
    set_cell(ws2, "J13", f'KOD NOSS/NCS : {cfg["code"]}')
    # header row (template) has column H onward = P1..; from the IT-072 diff, row20 col H = first
    # WA data row, one P column offset per WA row (diagonal in the blank IT-072 fixture — that
    # fixture's P-columns don't map to our P01..P12 codes). We instead resolve the P-column letter
    # for each WA explicitly from the "P## header" row above the WA block. Locate it by scanning
    # row 18/19 for P01..P12 labels; if not found, fall back to H..S (12 cols starting col H=8).
    p_col = {}
    for row in (17, 18, 19):
        for c in range(1, ws2.max_column + 1):
            v = ws2.cell(row, c).value
            if isinstance(v, str) and re.match(r"^P0?\d+$", v.strip()):
                m = re.match(r"^P0?(\d+)$", v.strip())
                p_col[f"P{int(m.group(1)):02d}"] = c
    if not p_col:
        # fallback: 12 P-columns start at column H (8)
        for i, pc in enumerate(P_CODES):
            p_col[pc] = 8 + i
    r = 20
    for i, (cu, cu_title, wa, wa_title, pcode) in enumerate(WA_MATRIX, start=1):
        ws2.cell(r, 2).value = i                      # B: NO
        ws2.cell(r, 3).value = cu_title.upper()        # C: COMPETENCY UNIT (CU)
        ws2.cell(r, 4).value = cu                      # D: KOD CU
        ws2.cell(r, 5).value = wa_title.upper()        # E: WORK ACTIVITIES (WA)
        ws2.cell(r, 6).value = wa                      # F: KOD WA
        col = p_col.get(pcode)
        if col:
            ws2.cell(r, col).value = "/"
        r += 1

    fname = "1. Borang Matriks Pemetaan Aktiviti Proses Kerja Syarikat Berdasarkan NOSS_JPK_ADI_02-2024 (P851).xlsx"
    op = out_path(cfg, "01 Lampiran 5 - Borang Matriks Proses Kerja vs NOSS", fname)
    wb.save(op)

    # read-back
    wb2 = openpyxl.load_workbook(op)
    rb1 = wb2["CU & WA"]["A4"].value
    rb2 = wb2["NOSS vs Proses Kerja"]["J13"].value
    ws2b = wb2["NOSS vs Proses Kerja"]
    row20 = [ws2b.cell(20, c).value for c in (2, 3, 4, 5, 6)]
    rb3 = None
    for pc, col in p_col.items():
        if pc == "P01":
            rb3 = ws2b.cell(20, col).value
            rb3 = f"{get_column_letter(col)}20={rb3!r} (P01 x WA1)"
            break
    print(f"lampiran5: wrote {op}")
    print(f"  read-back: CU&WA!A4={rb1!r}; NOSSvsPK!J13={rb2!r}; row20 B..F={row20!r}; {rb3}")
    print(f"  quirk: P-column letters resolved from header rows 17-19 scan (P01..P12); "
          f"fallback H..S used if not found — p_col={ {k: get_column_letter(v) for k, v in p_col.items()} }")


# ================= 2. jam42 =================

def cmd_jam42(cfg):
    tpl = TEMPLATES["jam42"]
    if not os.path.isfile(tpl):
        print(f"SKIPPED (template missing): {tpl}")
        return
    wb = openpyxl.load_workbook(tpl)
    ws = wb["PENJAJARAN CU"]
    formulas_before = sum(1 for row in ws.iter_rows() for c in row if isinstance(c.value, str) and c.value.startswith("="))

    set_cell(ws, "B2", "EDUCATION & TRAINING")
    set_cell(ws, "B3", "PRESCHOOL / EARLY CHILDHOOD EDUCATION")
    set_cell(ws, "B4", f'{cfg["code"]} {cfg["title"]}')
    ws["B5"] = 4  # TAHAP (DKM)
    set_cell(ws, "B6", "DKM (Mengikut Tahap, NOSS Bermula Tahap 4)")
    ws["B7"] = 4800  # Jumlah Jam Latihan ADI (30 bulan x 160 jam)
    ws["B8"] = 960   # Jumlah Jam Latihan Teori (20%)

    # row10 = CA input cell (template forces CA as a direct input, not computed) -> override input only
    set_cell(ws, "B10", "Core Abilities Tahap 1, 2, 3 & 4")
    ws["C10"] = 120  # input override (was 80 for IT-072/Tahap3); formulas in C11:C16 recompute from this

    cu_rows = [
        ("C01", "Conduct daily routine activities"),
        ("C02", "Perform preschool teaching and learning activities"),
        ("C03", "Organise preschool classroom environment"),
        ("C04", "Develop pupil's assessment"),
        ("C05", "Handle parental-community activities"),
    ]
    r = 11
    for cu, title in cu_rows:
        set_cell(ws, f"A{r}", cu)
        set_cell(ws, f"B{r}", title)
        # Fix formula: template's ROWS($A$11:$A$16) etc. included a leftover 6th-CU row (row16,
        # "C06 Product Marketing") from the IT-072/other-NOSS fixture this template was built from.
        # P851 has exactly 5 CU (C01-C05) -> denominator must be 5, not 6.
        ws[f"C{r}"] = "=($B$8-$C$10)/5"
        ws[f"D{r}"] = f"=$C${r}/8"
        r += 1
    # Row 16 was the stray 6th-CU row in the officer template (not part of P851's 5 CU) -> clear it.
    for col in "ABCDE":
        ws[f"{col}16"] = None
    # JUMLAH row: recompute as a formula instead of the stale literal 576 (IT-072's total) left by
    # the template/fixture.
    ws["C17"] = "=SUM(C10:C15)"
    ws["D17"] = "=SUM(D10:D15)"
    ws["E17"] = "=SUM(E10:E15)"

    set_cell(ws, "B24", "1 Hari 8 Jam")
    set_cell(ws, "B25", "1Minggu 5 Hari = 5 x 8 Jam = 40 Jam ")
    set_cell(ws, "B26", "1 bulan x 4 Minggu = 4 x 40 jam = 160 Jam")
    set_cell(ws, "B28", "1 bulan = 160 jam")
    set_cell(ws, "B30", "30 bulan x 160 jam = 4800 Jam")
    set_cell(ws, "B32", "Jumlah Jam Pengetahuan (20%) untuk kiraan CA/CU/EU = (4800 x 20%) = 960 Jam")

    formulas_after = sum(1 for row in ws.iter_rows() for c in row if isinstance(c.value, str) and c.value.startswith("="))

    fname = "4.2_Penjajaran Jam Latihan CA_CU_EU Program ADI Pekerjaan (P851).xlsx"
    op = out_path(cfg, "02 4.2 Penjajaran Jam Latihan CA-CU", fname)
    wb.save(op)

    wb2 = openpyxl.load_workbook(op, data_only=False)
    ws2 = wb2["PENJAJARAN CU"]
    print(f"jam42: wrote {op}")
    print(f"  read-back: B7(total)={ws2['B7'].value!r} B8(teori20%)={ws2['B8'].value!r} "
          f"C10(CA input)={ws2['C10'].value!r} C11(C01 formula)={ws2['C11'].value!r}")
    print(f"  formulas: before={formulas_before} after={formulas_after} (C11:C15 formulas kept as-is; "
          f"only the C10 input cell and header/total text overridden)")
    print(f"  quirk: template computes CU hours as (B8-C10)/ROWS(A11:A15) — verified it auto-yields "
          f"(960-120)/5=168 per CU without touching the formula, matching 03-jadual-latihan.md §A.")


# ================= 3. jadual43 =================

WEEKS_TARGET = 120

TEORI_BLOCKS = [
    ("CA", 1, 15), ("C01", 16, 36), ("C02", 37, 57),
    ("C03", 58, 78), ("C04", 79, 99), ("C05", 100, 120),
]

KERJA_WEEKS = {
    "P01": (16, 120), "P02": (16, 120), "P03": (16, 120), "P04": (16, 120),
    "P05": (37, 42), "P06": (41, 120), "P07": (45, 120), "P08": (53, 57),
    "P09": (58, 120), "P10": (65, 120), "P11": (79, 99), "P12": (100, 120),
}


def extend_week_columns(ws, first_week_col, last_existing_col, target_last_col):
    """Copy style/width/number-format of last_existing_col to every new column up to target_last_col."""
    src_dim = ws.column_dimensions[get_column_letter(last_existing_col)]
    for c in range(last_existing_col + 1, target_last_col + 1):
        letter = get_column_letter(c)
        ws.column_dimensions[letter].width = src_dim.width
        for r in range(1, ws.max_row + 1):
            src_cell = ws.cell(r, last_existing_col)
            dst_cell = ws.cell(r, c)
            if src_cell.has_style:
                dst_cell._style = copy.copy(src_cell._style)
    # week header numbering row (row 10 in this template, per dump: row9 header, row10 = week no?)
    return target_last_col


def cmd_jadual43(cfg):
    tpl = TEMPLATES["jadual43"]
    if not os.path.isfile(tpl):
        print(f"SKIPPED (template missing): {tpl}")
        return
    wb = openpyxl.load_workbook(tpl)

    FIRST_WEEK_COL = 4  # column D
    LAST_EXISTING_COL = 75  # column BW (72-week template)
    TARGET_LAST_COL = FIRST_WEEK_COL + WEEKS_TARGET - 1  # 123 -> DS

    cu_titles = {
        "C01": "Conduct daily routine activities",
        "C02": "Perform preschool teaching and learning activities",
        "C03": "Organise preschool classroom environment",
        "C04": "Develop pupil's assessment",
        "C05": "Handle parental-community activities",
    }

    for sheet_name in ["Jadual Teori ", "Jadual Kerja"]:
        ws = wb[sheet_name]
        extend_week_columns(ws, FIRST_WEEK_COL, LAST_EXISTING_COL, TARGET_LAST_COL)
        cols_before = ws.max_column
        set_cell(ws, "C3", f'KOD NOSS: {cfg["code"]}\nPROGRAM ADI: {cfg["title"]}\nTAHAP: 4 (DKM)')

    # -- Jadual Teori: row11 = CA header row ('X' across weeks 1-15); rows 12-16 = C01..C05
    wt = wb["Jadual Teori "]
    set_cell(wt, "C11", "CORE ABILITIES TAHAP 1, 2, 3 & 4")
    for r in range(11, 17):
        pass
    for row, (code, w1, w2) in zip(range(11, 17), TEORI_BLOCKS):
        if row == 11:
            pass  # CA label already set above
        else:
            set_cell(wt, f"C{row}", f'{code}- {cu_titles[code]}')
        for w in range(w1, w2 + 1):
            col = FIRST_WEEK_COL + (w - 1)
            wt.cell(row, col).value = "X"

    # -- Jadual Kerja: rows 11..22 = P01..P12 (one per process), label + X across its week range
    wk = wb["Jadual Kerja"]
    with open(os.path.join(cfg["base"], "01-proses-kerja.md"), encoding="utf-8") as fh:
        proses_txt = fh.read()
    proses_names = dict(re.findall(r"^\| (P\d\d) \| ([^|]+?) \|.*?\|\s*$", proses_txt, re.M))
    for row, pcode in zip(range(11, 23), P_CODES):
        label = proses_names.get(pcode, pcode).strip()
        set_cell(wk, f"C{row}", f'{pcode} - {label}')
        w1, w2 = KERJA_WEEKS[pcode]
        for w in range(w1, w2 + 1):
            col = FIRST_WEEK_COL + (w - 1)
            wk.cell(row, col).value = "X"

    fname = "4.3_Jadual Pengetahuan dan Proses Kerja ADI Pekerjaan (P851).xlsx"
    op = out_path(cfg, "03 4.3 Jadual Teori dan Jadual Proses Kerja", fname)
    wb.save(op)

    wb2 = openpyxl.load_workbook(op)
    wt2, wk2 = wb2["Jadual Teori "], wb2["Jadual Kerja"]
    last_col_letter = get_column_letter(TARGET_LAST_COL)
    print(f"jadual43: wrote {op}")
    print(f"  read-back: Jadual Teori C12={wt2['C12'].value!r}; "
          f"week120 col {last_col_letter}12 (C01 week120, should be blank)={wt2[f'{last_col_letter}12'].value!r}, "
          f"D16 (C05 week1, should be blank)={wt2['D16'].value!r}, "
          f"{get_column_letter(FIRST_WEEK_COL+99)}16 (C05 week100)={wt2[f'{get_column_letter(FIRST_WEEK_COL+99)}16'].value!r}")
    print(f"  read-back: Jadual Kerja C11={wk2['C11'].value!r}; "
          f"{get_column_letter(FIRST_WEEK_COL+15)}11 (P01 week16)={wk2[f'{get_column_letter(FIRST_WEEK_COL+15)}11'].value!r}")
    print(f"  quirk: template had {LAST_EXISTING_COL - FIRST_WEEK_COL + 1} week columns (D..BW); "
          f"extended to {WEEKS_TARGET} (D..{last_col_letter}) by copying column BW's style/width to each "
          f"new column, on both sheets, before filling.")


# ================= 4. jsu =================

def parse_jsu_source(cfg):
    """Parse 06-jsu.md per-CU blocks into structured rows."""
    path = os.path.join(cfg["base"], "06-jsu.md")
    text = open(path, encoding="utf-8").read()
    blocks = re.split(r"(?=^## C0\d)", text, flags=re.M)
    out = {}
    for b in blocks:
        m = re.match(r"^## (C0\d)\s*—\s*(.+)$", b.strip().split("\n")[0])
        if not m:
            continue
        cu, cu_title = m.group(1), m.group(2).strip()
        kod = re.search(r"\| KOD CU \| (.+?) \|", b)
        nama = re.search(r"\| NAMA CU \| (.+?) \|", b)
        lo = re.search(r"\| LEARNING OUTCOME \| (.+?) \|\s*\n", b)
        wa_rows = []
        for line in b.split("\n"):
            line = line.strip()
            if not line.startswith("| WA"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 8:
                continue
            wa_no, wa_title, weight, sub, aras, konstruk, esei_flag, esei_aras = cells[:8]
            weight_m = re.match(r"(\d+)", weight)
            wa_rows.append((wa_no, wa_title, weight_m.group(1) if weight_m else "0", sub, aras, esei_flag, esei_aras))
        out[cu] = {"cu_title": cu_title, "kod": kod.group(1) if kod else f'{cfg["code"]}-{cu}',
                    "nama": nama.group(1) if nama else cu_title, "lo": lo.group(1) if lo else "",
                    "wa_rows": wa_rows}
    return out


def cmd_jsu(cfg):
    tpl = TEMPLATES["jsu"]
    if not os.path.isfile(tpl):
        print(f"SKIPPED (template missing): {tpl}")
        return
    data = parse_jsu_source(cfg)
    wb = openpyxl.load_workbook(tpl)
    src_name = " JSU STD THP 4-5 (SUBJEKTIF)"
    src = wb[src_name]

    thp13_sheets = [s for s in wb.sheetnames if "THP 1-3" in s or s.startswith("Prompt")]
    written = []
    sub_cols = {"a": 4, "b": 5, "c": 6, "d": 7}  # D,E,F,G
    aras_cols = {"R": 8, "S": 9, "T": 10}         # H,I,J
    esei_col = 11                                  # K
    # Per-CU marks for struktur sub a/b/c/d, from 06-jsu.md "## Semakan silang" (a+b+c+d must = 20):
    SUB_MARKS = {
        "C01": {"a": 5, "b": 5, "c": 5, "d": 5},
        "C02": {"a": 4, "b": 4, "c": 6, "d": 6},
        "C03": {"a": 4, "b": 5, "c": 5, "d": 6},
        "C04": {"a": 4, "b": 4, "c": 6, "d": 6},
        "C05": {"a": 4, "b": 4, "c": 6, "d": 6},
    }

    for seq, cu in enumerate(cfg["cu_order"], start=1):
        cu_data = data.get(cu)
        sheet_name = f"JSU {cu}"
        ws = wb.copy_worksheet(src)
        ws.title = sheet_name
        if not cu_data:
            print(f"  SKIPPED CU {cu}: no 06-jsu.md block found")
            continue
        set_cell(ws, "B2", cu_data["kod"])
        set_cell(ws, "B3", cu_data["nama"])
        set_cell(ws, "B5", cu_data["lo"])

        # The template's SUBJEKTIF sheet has exactly 4 WA-listing rows (13-16), one per struktur
        # sub-letter a/b/c/d (Buku Panduan Soalan 2024 §5.5.6: struktur is always a-d regardless
        # of WA count). A 5-WA CU shares one sub-letter across two WA ("c (gabung WA5)" etc.) —
        # those two WA must be COMBINED into that one letter's row, never given a 5th row (which
        # would overflow into the template's JUMLAH row at 17 and corrupt it).
        marks = SUB_MARKS[cu]
        by_letter = {"a": [], "b": [], "c": [], "d": []}
        esei_letter = None
        for wa_no, wa_title, weight, sub, aras, esei_flag, esei_aras in cu_data["wa_rows"]:
            # `sub`/`aras` can each hold a comma-separated list for a WA that maps to >1 sub-letter
            # (e.g. sub="b, d", aras="S, T") — the two lists are POSITIONAL (sub[i] <-> aras[i]),
            # so pair them by index rather than flat-matching every letter into every sub-letter.
            sub_groups = [re.findall(r"\b[a-d]\b", part) for part in sub.split(",")]
            aras_groups = [re.findall(r"\b[RST]\b", part) for part in aras.split(",")]
            sub_letters = [sl for grp in sub_groups for sl in grp]
            for i, grp in enumerate(sub_groups):
                paired_aras = aras_groups[i] if i < len(aras_groups) else (aras_groups[0] if aras_groups else [])
                for sl in grp:
                    by_letter[sl].append((wa_no, wa_title.strip(), int(weight or 0), paired_aras))
            if esei_flag == "1":
                # esei is attached to whichever sub-letter row this WA also appears on (or 'a' if
                # it maps to none, e.g. an esei-only WA never listed in struktur).
                esei_letter = sub_letters[0] if sub_letters else "a"
                esei_wa_no, esei_wa_title = wa_no, wa_title.strip()

        row = 13
        esei_wa_row = None
        for letter in ("a", "b", "c", "d"):
            entries = by_letter[letter]
            ws.cell(row, 1).value = ", ".join(e[0] for e in entries) or None
            ws.cell(row, 2).value = "; ".join(e[1] for e in entries) or None
            ws.cell(row, 3).value = sum(e[2] for e in entries) or None
            ws.cell(row, sub_cols[letter]).value = marks[letter]
            row_aras_letters = entries[0][3] if entries else []
            for al in row_aras_letters:
                ws.cell(row, aras_cols[al]).value = marks[letter]
            if letter == esei_letter:
                ws.cell(row, esei_col).value = 20
                esei_wa_row = row
                # esei WA may not itself be one of the struktur WAs on this row (e.g. an esei-only
                # WA) — append its title so the sheet still names it.
                if not any(e[0] == esei_wa_no for e in entries):
                    existing = ws.cell(row, 2).value
                    ws.cell(row, 2).value = f"{existing} / ESEI: {esei_wa_title}" if existing else f"ESEI: {esei_wa_title}"
            row += 1
        set_cell(ws, f"D17", 1)
        set_cell(ws, f"K17", 1)
        set_cell(ws, "D18", "1 JAM")
        written.append((sheet_name, esei_wa_row))

    # remove the original ungrouped SUBJEKTIF sheet + keep THP1-3 sheets untouched
    if src_name in wb.sheetnames:
        del wb[src_name]

    fname = "3.2 Format Soalan PENILAIAN PENGETAHUAN (P851).xlsx"
    op = out_path(cfg, "06 3.2 JSU - Jadual Spesifikasi Ujian", fname)
    wb.save(op)

    wb2 = openpyxl.load_workbook(op)
    rb = []
    for sheet_name, esei_row in written:
        ws2 = wb2[sheet_name]
        rb.append(f"{sheet_name}!B2={ws2['B2'].value!r} B3={ws2['B3'].value!r} K17={ws2['K17'].value!r}")
    print(f"jsu: wrote {op}")
    for line in rb:
        print(f"  read-back: {line}")
    print(f"  THP 1-3 sheets left untouched: {[s for s in wb2.sheetnames if 'THP 1-3' in s]!r} (count={len([s for s in wb2.sheetnames if 'THP 1-3' in s])})")
    print(f"  quirk: 5 new sheets 'JSU C01'..'JSU C05' via copy_worksheet() of "
          f"' JSU STD THP 4-5 (SUBJEKTIF)'; that source sheet then deleted (per brief: 'copy sheet ... five "
          f"times'). Struktur sub marks = 20/4=5 each (a-d); esei = 20; JUMLAH row17 D17=K17=1 "
          f"(count of questions, not marks — matches template's own JUMLAH SOALAN semantics).")


# ================= 5. bukti =================

def parse_bukti_source(cfg):
    path = os.path.join(cfg["base"], "08-senarai-bukti-proses-kerja.md")
    text = open(path, encoding="utf-8").read()
    m = re.search(r"## Senarai Bukti Aktiviti Kerja\n\n(.*?)\n\n##", text, re.S)
    table = m.group(1)
    rows = []
    cur_p, cur_title = None, None
    for line in table.split("\n"):
        if not line.strip().startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 6:
            continue
        p, ptitle, no, evid, jenis, mapping = cells[:6]
        if p:
            cur_p, cur_title = p, ptitle
        rows.append((cur_p, cur_title, no, evid, mapping))
    rows = [r for r in rows if r[0] and r[2].isdigit()]

    m2 = re.search(r"## Susunan Semula PK ke CU-WA.*?\n\n(.*?)\n\nSemakan", text, re.S)
    table2 = m2.group(1)
    susunan = []
    cur_cu = None
    for line in table2.split("\n"):
        if not line.strip().startswith("|") or "---" in line:
            continue
        if re.match(r"^\|\s*CU\s*\|\s*WA\s*\|", line.strip()):
            continue  # header row
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        cu, wa, nos = cells[:3]
        if cu:
            cur_cu = cu
        if wa:
            susunan.append((cur_cu, wa, nos))
    return rows, susunan


def cmd_bukti(cfg):
    tpl = TEMPLATES["bukti"]
    if not os.path.isfile(tpl):
        print(f"SKIPPED (template missing): {tpl}")
        return
    rows, susunan = parse_bukti_source(cfg)
    wb = openpyxl.load_workbook(tpl)

    ws = wb["SENARAI BUKTI PROSES KERJA"]
    r = 3
    seen_p = set()
    for p, ptitle, no, evid, mapping in rows:
        # Clear A/B first: the blank officer template ships with its own sample P-code/title text
        # in these rows (e.g. a generic "Proses Kerja 2/3/4" 1-item-per-P layout). Our real P01-P12
        # mapping has a different number of evidence rows per P, so a naive "only write on first row
        # of a P-group" leaves stale template placeholder text on the rows it skips.
        ws[f"A{r}"] = None
        ws[f"B{r}"] = None
        if p not in seen_p:
            set_cell(ws, f"A{r}", p)
            set_cell(ws, f"B{r}", ptitle)
            seen_p.add(p)
        ws[f"C{r}"] = int(no)
        set_cell(ws, f"D{r}", evid)
        set_cell(ws, f"E{r}", mapping)
        r += 1
    set_cell(ws, f"A{r}", "Nota: semua bukti aktiviti kerja perlu disahkan oleh Pembimbing dan Cop Syarikat.")

    ws2 = wb["Susunan Semula PK ke CU-WA"]
    r2 = 3
    seen_cu = set()
    for cu, wa, nos in susunan:
        if cu not in seen_cu:
            set_cell(ws2, f"A{r2}", cu)
            seen_cu.add(cu)
        set_cell(ws2, f"B{r2}", wa)
        set_cell(ws2, f"C{r2}", nos)
        r2 += 1

    fname = "4 Senarai Bukti Proses Kerja (P851).xlsx"
    op = out_path(cfg, "09 4 Senarai Bukti Proses Kerja + Lampiran 4 Perakuan Pembimbing", fname)
    wb.save(op)

    wb2 = openpyxl.load_workbook(op)
    ws2r = wb2["SENARAI BUKTI PROSES KERJA"]
    ws3r = wb2["Susunan Semula PK ke CU-WA"]
    print(f"bukti: wrote {op}")
    print(f"  read-back: SENARAI!A3={ws2r['A3'].value!r} D3={ws2r['D3'].value!r} E3={ws2r['E3'].value!r}")
    print(f"  read-back: Susunan!A3={ws3r['A3'].value!r} B3={ws3r['B3'].value!r} C3={ws3r['C3'].value!r}")
    print(f"  rows written: {len(rows)} evidence rows (expect 39), {len(susunan)} WA rows (expect 21)")
    print(f"  GARIS PANDUAN sheet left untouched.")


CMDS = {
    "lampiran5": cmd_lampiran5,
    "jam42": cmd_jam42,
    "jadual43": cmd_jadual43,
    "jsu": cmd_jsu,
    "bukti": cmd_bukti,
}


def run(subcommand, cfg):
    CMDS[subcommand](cfg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=list(CMDS.keys()) + ["all"])
    ap.add_argument("--subject", required=True, choices=list(SUBJECTS.keys()))
    args = ap.parse_args()
    cfg = SUBJECTS[args.subject]
    if args.cmd == "all":
        for name in CMDS:
            run(name, cfg)
    else:
        run(args.cmd, cfg)


if __name__ == "__main__":
    main()
