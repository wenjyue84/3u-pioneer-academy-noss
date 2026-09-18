import re, os, glob
import docx
from docx import Document
from docx.shared import Pt

ROOT = r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss"
TEMPLATE_DIR = os.path.join(ROOT, r"video-film-editing\output\04 3.3a Rangka Nota Pembelajaran")
SRC_DIR = os.path.join(ROOT, r"video-film-editing\05-nota-pembelajaran")

CU_TITLES = {
    "C01": "Visual Editing Project Analysis",
    "C02": "Visual Editing Preparation",
    "C03": "Offline Visual Editing",
    "C04": "Audio Sweetening",
    "C05": "Online Visual Editing",
}

def clean_inline(s):
    s = s.replace("**", "").replace("`", "").strip()
    return s

def parse_md(path):
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

def extract_outline(penerangan):
    """Return list of (bab_title, [sub-topic strings])."""
    babs = []
    cur = None
    for line in penerangan.split("\n"):
        s = line.strip()
        m = re.match(r"^###\s+(Bab\s+\d+\s*:\s*.+)$", s)
        if m:
            cur = {"title": clean_inline(m.group(1)), "subs": []}
            babs.append(cur)
            continue
        m2 = re.match(r"^\*\*(\d+)\.\s+(.+?)\*\*$", s)
        if m2 and cur is not None:
            label = m2.group(2).strip()
            if label.lower() != "rumusan":
                cur["subs"].append(f"{m2.group(1)}. {label}")
    return babs

def wa_title_from_hdr(hdr, fallback_code=""):
    wa_stmt_full = (hdr_lookup(hdr, "NO DAN PENYATAAN AKTIVITI") or hdr_lookup(hdr, "NO DAN NAMA WA") or "")
    if "/" in wa_stmt_full:
        code = wa_stmt_full.split("/")[0].strip()
        rest = wa_stmt_full.split("/", 1)[1]
        title = ", ".join(part.strip() for part in rest.split("/"))
    else:
        code = fallback_code
        title = re.sub(r"^W\d+\s*[—\-–:]\s*", "", wa_stmt_full.strip())
    return code, title

def clear_body_after_table(doc):
    from docx.oxml.ns import qn
    body = doc.element.body
    first_table = doc.tables[0]._tbl
    seen_first_table = False
    to_remove = []
    for child in list(body.iterchildren()):
        if child is first_table:
            seen_first_table = True
            continue
        if not seen_first_table:
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
            t.cell(ri, ci).text = val
        if header and ri == 0:
            for ci in range(ncols):
                for p in t.cell(ri, ci).paragraphs:
                    for r in p.runs:
                        r.bold = True
    return t

def build(cu_code, cu_title, files, out_path):
    tpl_glob = glob.glob(os.path.join(TEMPLATE_DIR, f"*{cu_code}*.docx"))
    assert tpl_glob, f"no existing template found for {cu_code}"
    doc = Document(tpl_glob[0])

    # restyle title paragraph (first paragraph)
    title_text = f"3.3a Rangka Nota Pembelajaran — IT-072-3:2012-{cu_code} {cu_title}"
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

    clear_body_after_table(doc)

    n_wa = len(files)
    doc.add_paragraph()
    for idx, f in enumerate(sorted(files), start=1):
        hdr, body = parse_md(f)
        base = os.path.basename(f).replace(".md", "")
        fallback_code = f"IT-072-3:2012-{base}"
        wa_code, wa_title = wa_title_from_hdr(hdr, fallback_code)
        penerangan = get_section(body, "III. PENERANGAN", ["IV. SESI PERSOALAN / KERJA KUMPULAN"])
        babs = extract_outline(penerangan)

        add_bold_para(doc, f"Module: {cu_code} {cu_title} / Work Activity: WA{idx} — {wa_title} ({wa_code})", size=12)
        add_normal_para(doc, "Senarai topik nota:")
        rows = [["Bab", "Sub-topik"]]
        for b in babs:
            subs = "\n".join(b["subs"]) if b["subs"] else ""
            rows.append([b["title"], subs])
        add_table_grid(doc, rows)
        doc.add_paragraph()

    doc.save(out_path)
    return n_wa, sum(len(b["subs"]) for f in files for b in extract_outline(get_section(parse_md(f)[1], "III. PENERANGAN", ["IV. SESI PERSOALAN / KERJA KUMPULAN"])))

def main():
    all_md = sorted(glob.glob(os.path.join(SRC_DIR, "C0*-W*.md")))
    by_cu = {}
    for f in all_md:
        base = os.path.basename(f)
        cu = base.split("-")[0]
        by_cu.setdefault(cu, []).append(f)

    seq_map = {"C01": 1, "C02": 2, "C03": 3, "C04": 4, "C05": 5}
    for cu, seq in seq_map.items():
        files = by_cu[cu]
        cu_title = CU_TITLES[cu]
        existing = glob.glob(os.path.join(TEMPLATE_DIR, f"3.3a-{seq:02d}*.docx"))
        assert existing, f"no existing 3.3a file for {cu}"
        out_path = existing[0]  # overwrite same filename in place
        n_wa, n_subs = build(cu, cu_title, files, out_path)
        print(f"[{cu}] {len(files)} WA -> {os.path.basename(out_path)} (tables written)")

if __name__ == "__main__":
    main()
