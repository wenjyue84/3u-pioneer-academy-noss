"""Render the evidence pages Jay will forward to Jennifer.

Two outputs, both high-DPI so they stay readable after WhatsApp recompression:
  1. Alvin's MySPIKE Perakuan Personel (page 1)
  2. Garis Panduan Lampiran 1 checklist page, which shows item 2.3 says only
     "Penyata kewangan syarikat" -- no "beraudit" anywhere.

Every crop is read back and asserted against its decisive sentence before it is
written, per the project rule in CLAUDE.md.
"""
import fitz
import pathlib

BASE = pathlib.Path(r"C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss")
OUT = BASE / "raw" / "jennifer-2026-07-30" / "share"
OUT.mkdir(parents=True, exist_ok=True)

DPI = 200


def render(pdf_path, page_no, out_name, must_contain):
    doc = fitz.open(pdf_path)
    page = doc[page_no]
    text = page.get_text()
    missing = [s for s in must_contain if s.lower() not in text.lower()]
    if missing:
        print(f"!! {out_name}: page {page_no} MISSING {missing}")
        return None
    pix = page.get_pixmap(dpi=DPI)
    dest = OUT / out_name
    pix.save(dest)
    print(f"OK {out_name}  ({pix.width}x{pix.height})  page index {page_no}")
    doc.close()
    return dest


# 1. Alvin's Perakuan Personel
render(
    BASE / "raw" / "jennifer-2026-07-30" / "Alvin-Pentauliahan-Personel.pdf",
    0,
    "01-alvin-perakuan-personel.png",
    ["ALVIN TEO KHAI MING", "1272157", "PD6192", "M731-001-3:2021",
     "19 December 2025", "18 December 2028"],
)

# 2. Sijil Pentauliahan (the centre accreditation)
render(
    BASE / "raw" / "jennifer-2026-07-30" / "Sijil-Pentauliahan-MT-Digital-Marketing.pdf",
    0,
    "02-sijil-pentauliahan-pd6192.png",
    ["CHARACTER HEALTH & FITNESS ACADEMY", "PD6192",
     "OPERASI PEMASARAN DIGITAL", "M731-001-3:2021"],
)

# 3. Garis Panduan Lampiran 1 checklist -- find the page carrying item 2.3
gp = BASE / "raw" / "ptpk" / "Garis-Panduan-TVET-Berimpak-Tinggi-19Mei2025.pdf"
doc = fitz.open(gp)
target = None
for i, page in enumerate(doc):
    t = page.get_text()
    if "Penyata kewangan syarikat" in t and "Sijil Akuan Pentauliahan" in t:
        target = i
        print(f"-> Lampiran 1 checklist found on PDF page index {i} (printed page {i+1})")
        break
doc.close()

if target is not None:
    render(
        gp, target, "03-gp-lampiran1-senarai-semak.png",
        ["Penyata kewangan syarikat", "Sijil Akuan Pentauliahan",
         "Sijil Kelayakan tenaga pengajar"],
    )

# Confirm the word "beraudit"/"audit" appears nowhere in the whole guideline,
# which is the actual point Jennifer needs.
doc = fitz.open(gp)
hits = []
for i, page in enumerate(doc):
    t = page.get_text().lower()
    for w in ("beraudit", "diaudit", "audited", "juruaudit"):
        if w in t:
            hits.append((i + 1, w))
doc.close()
print("audit-word hits across whole Garis Panduan:", hits if hits else "NONE")
