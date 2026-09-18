# Readability polish spec — output/ (Jay, 2026-09-18)

Goal: make every file in `output/` easier to read **without changing content or structure**. Text, order, headings, tables, numbers, filenames stay identical. Only presentation changes.

## Guard (mandatory, both before and after)
Extract all paragraph + table-cell text from each docx (python-docx, in document order) and all cell values from each xlsx (openpyxl, formulas as strings) into a `.before.json` / `.after.json` per file; the two must be **byte-identical**. Any file whose text changed must be reverted from the before-copy. Report the diff count (must be 0).

## Word (.docx) — generated documents only
Applies to: `04 3.3a …/*.docx`, `05 …/CU C01-C05/*.docx`, `05 …/Core Abilities L1-L3/*.docx`, `07 …/CU C01-C05/*.docx`, `07 …/Core Abilities L1-L3/*.docx`, `13 Buku Teks …/*.docx`.
Do NOT touch: official forms (`10 Lampiran 6`, `09 …/2_Borang Perakuan`, `08 3.1_Bukti`, `11 Fail Pelaksanaan`, `12 Fail Kompilasi`) and any `(format JPK)` folder — those follow the officer/JPK layout as-is.

Rules:
1. Body font Arial 11 pt (the JPK/officer house font), colour black; line spacing 1.15; space after paragraph 6 pt; justify off (left aligned) for body.
2. Section labels (TAJUK:, TUJUAN:, PENERANGAN:, SOALAN:, RUJUKAN:, I.–V. headings, "Bab n:" lines, "Objektif Pembelajaran", "Rumusan", "Aktiviti Kerja n:", "Soalan WAn", "BAHAGIAN …", "SKEMA JAWAPAN") → bold, 12 pt for Bab/section titles, 6 pt space before / 6 pt after; keep their text exactly.
3. Numbered sub-topic lines (`1. …`, `2. …` bold labels) → bold 11 pt, space before 6 pt.
4. Bullets / list paragraphs → hanging indent 0.63 cm, space after 2 pt.
5. Tables → style `Table Grid`, all borders, header row bold with light-grey shading (D9D9D9), cell font Arial 10, cell margins ~0.1 cm, `autofit` on, repeat header row on page break, no row splitting across pages.
6. Question papers: keep one blank line between questions; options A–D as separate lines with 0.63 cm indent; page break before SKEMA JAWAPAN kept.
7. Header table of each note (the officer template's identification table) stays untouched (it is the template's own formatting).
8. Page: A4, margins 2.54 cm (keep whatever the template already sets if it is a template-based file), widow/orphan control on.
9. Do not add, remove or reorder any paragraph, run text, table row or cell.

## Excel (.xlsx)
Applies to: `02 4.2 …`, `03 4.3 …`, `06 3.2 JSU …`, `09 …/4 Senarai Bukti …`. Lampiran 5 (`01 …`): only sheet `CU & WA` and `NOSS vs Proses Kerja` — widths/wrap only.
Rules: header rows bold + light-grey fill; wrap text on text columns; column widths sized to content (cap 60); freeze panes below the header row; vertical-align top; keep every value and every formula unchanged (formula count before == after); keep sheet names/order; print setup landscape + fit to 1 page wide for the wide sheets.

## PDFs
After polishing, re-export via Word COM (PowerShell `New-Object -ComObject Word.Application`, `Fields.Update()`, `ExportAsFixedFormat(path,17)`) only for files that already have a PDF sibling: `13 Buku Teks …/*.pdf`. Report page counts.

## Report
Per folder: files processed, text-diff count (0), formulas before/after, PDFs regenerated with page counts. Anything skipped and why.
