# JPK PPT-PPA format contract

> **Two tiers of evidence.** The FB-018-3 files Jennifer owns are her *drafts* for
> a submission not yet made. The BEAUTY L1/L2/L3 files in
> `SOALAN & SKEMA - APPROVED` are papers **JPK has already accepted**. Where the
> two disagree, the approved set wins — and where the approved set disagrees with
> *itself*, the thing varies and must not be pinned.
>
> Local copies: `raw/jennifer-approved-beauty/` (12 papers) and
> `raw/jennifer-authoritative-fb018-3/` (4 drafts). All owned by
> `jennifer@character.com.mx`.

## 0a. Two template generations — follow the newer one

Her files are not one style. They are two, and mixing them is the thing to avoid.

| | **Older — JPK-approved** (BEAUTY L1/L2/L3) | **Newer — her 2026-08 draft** (FB-018-3) |
|---|---|---|
| Row numbering | `BIL` (6/6) | `NO.` (9 uses, `BIL` 0) |
| Competency-unit row | `SENARAI KOMPETENSI TERAS` | `NAMA UNIT KOMPETENSI` |
| NOSS row | `KOD DAN NAMA STANDARD/NOSS` | `KOD KOMPETENSI` |
| Date field | `TARIKH PEPERIKSAAN` | `TARIKH PENILAIAN` |
| Section letters | B–G | A–F |
| Equipment section | `PERALATAN DAN KELENGKAPAN` | `SENARAI PERALATAN` |
| Four-piece set | SOALAN + SKEMA + a separate `Senarai Peralatan` | SOALAN + SKEMA + ANSWER SHEET + EQUIPMENT VERIFICATION |

**Follow the newer generation.** She wrote it in August 2026 for the submission
this work supports, and its equipment form carries the JPK form number
`JPK/PPA-PPT/SP/1:2022` — later than the approvals the BEAUTY papers won. The
approved set is still the authority on anything the newer draft does not settle,
and on *what JPK will actually accept*.

All 44 of our documents are consistently on the newer generation; none carries an
older-generation token.

**Do not copy her abbreviations for their own sake.** Her approved skema head the
section column `BHGN`; ours spell `BAHAGIAN`. Matching her format means matching
what a reviewer must recognise, not matching every character.

## 0. What varies, and must not be enforced

Established by reading all six approved BEAUTY SOALAN:

| Element | L1 SET A/B | L2 and L3 SET A/B |
|---|---|---|
| Section letters | **A–F** | **B–G** |
| Duration heading | `TEMPOH` / `TEMPOH MASA` | `TEMPOH` |
| Equipment heading | `SENARAI PERALATAN` | `PERALATAN DAN KELENGKAPAN` |

Same author, same approved batch, two schemes. **The invariant is the sequence:**

```
TEMPOH → KETERAMPILAN → TUGASAN → SENARAI BAHAN → PERALATAN → KRITERIA PENILAIAN
```

An earlier version of `V11` asserted A–F as "fixed by the JPK format". It would
have failed four of her own approved papers. Our papers follow the L1 / FB-018-3
scheme, which is one of the two valid forms.

**Page-count declarations vary too, and JPK accepted them anyway.** Of the twelve
approved BEAUTY papers, only three declare a printed-page count matching their
PDF page count — `SOALAN AMALI BEAUTY SET A L1` declares 4 for a 9-page file, and
its body pages are numbered 9–14, i.e. the PDF is an excerpt of a larger
document. So a mismatch is a defect worth avoiding, but it demonstrably does not
block approval. Keep backfilling the real count; do not treat a mismatch in *her*
files as something she must fix before submitting.

That same paper carries **two different reference codes**: the cover reads
`S960-002-1:2020/2026/A/04`, the body pages `S960-002-1:2020/2025/A/03`.


Extracted 2026-08-25 by reading, page by page, the four documents in
`https://drive.google.com/drive/folders/1grg0ck28lAZHeMhmVB7g1vh4V80NlY_o`
whose Drive **owner is `jennifer@character.com.mx`**. Local copies:
`raw/jennifer-authoritative-fb018-3/`.

Ownership is the authority test. Everything else in that folder is owned by
`wenjyue@gmail.com` — our own uploads, which cannot be their own benchmark. Verify
with `mcp__claude_ai_Google_Drive__get_file_metadata` before treating any file as a
reference; the `owner` field is the only reliable signal, since filenames were
copied across both sets.

| File | Owner | Pages | Local |
|---|---|---|---|
| SOALAN PENILAIAN AMALI PPT （SET A).pdf | jennifer@character.com.mx | 14 | `jen-soalan-setA.pdf` |
| SKEMA PENILAIAN AMALI PPT-PPA (SET A).pdf | jennifer@character.com.mx | 11 | `jen-skema-setA.pdf` |
| ASSESSMENT ANSWER SHEET.pdf | jennifer@character.com.mx | 8 | `jen-answer-sheet.pdf` |
| EQUIPMENT VERIFICATION.pdf | jennifer@character.com.mx | 1 | `jen-equipment-verification.pdf` |

---

## 1. Language — Malay frame, English content

This is the rule, and it is not what "only one language" first sounded like.

| Element | Language |
|---|---|
| Section headings (`A. TEMPOH MASA`, `B. KETERAMPILAN`, `C. TUGASAN`, `D. SENARAI BAHAN / DOKUMEN`, `E. SENARAI PERALATAN`, `F. KRITERIA PENILAIAN`) | **Malay** |
| Table column headers (`NO.`, `BAHAN / DOKUMEN`, `UKURAN (UNIT)`, `KUANTITI (Bahan:Calon)`, `PERALATAN / KELENGKAPAN`) | **Malay** |
| Cover identification labels (`KOD DAN NAMA PUSAT BERTAULIAH/SYARIKAT`, `KOD KOMPETENSI`, `NAMA UNIT KOMPETENSI`, `NAMA CALON`…) | **Malay** |
| Fixed JPK boilerplate (`Arahan kepada calon`, `AMARAN`, `UNTUK KEGUNAAN PEMERIKSA SAHAJA`, `SKALA PEMARKAHAN`, `PERINGATAN`) | **Malay** |
| Criteria sub-labels (`1) Perkara Kritikal`, `2) Proses Kerja`, `3) Hasil Kerja`, `4) Sikap/ Keselamatan dan Alam Sekitar`) | **Malay** |
| **Everything else — task text, criteria descriptions, appendix forms, oral questions, marking descriptors** | **English** |

Jennifer's own paper, page 2:

```
A. TEMPOH MASA
: 3 HOURS

B. KETERAMPILAN
: CONDUCT MARKET & PRODUCT SURVEY, PREPARE ONLINE
  SALES COLLATERAL AND EVALUATE SALES PERFORMANCE
  FOR A PROPERTY SALES OPERATION.

C. TUGASAN :
1. The candidate is required to carry out sales and marketing activities for
   Seri Harmoni Residence based on the information and data provided…
```

Her complaint of 2026-08-24 22:47 — *"Only one language, here mixed language"* —
was about **inline pairs inside a single sentence**, e.g.
`Tinjauan Pasaran & Produk / Market & Product Survey`. Her own document never does
that: the Malay frame and the English content never appear in the same sentence.

> A first pass at this on 2026-08-25 morning converted everything to Malay. That
> is a different document from hers, and Set A and Set B must be parallel forms.
> Corrected the same day.

## 2. Cover — one bordered table, logo inside it

Not a stack of paragraphs. A single table with visible borders, occupying the top
two-thirds of page 1:

```
┌──────────────────────┬──────────────────────────────────────────┐
│   [Jata Negara]      │  JABATAN PEMBANGUNAN KEMAHIRAN           │
│   crest, centred     │  KEMENTERIAN SUMBER MANUSIA              │
│   in its own cell    │  ARAS 7 & 8 SETIA PERKASA 4,             │
│                      │  KOMPLEKS SETIA PERKASA                  │
│                      │  62530 PUTRAJAYA                         │
├──────────────────────┼──────────────────────────────────────────┤
│ KOD DAN NAMA PUSAT   │  CHARACTER INTERNATIONAL ACADEMY         │
│ BERTAULIAH/SYARIKAT  │  SDN. BHD.                               │
├──────────────────────┴──────────────────────────────────────────┤
│         SOALAN PENILAIAN AMALI PPT-PPA (SET A)   ← centred      │
├──────────────────────┬──────────────────────────────────────────┤
│ KOD KOMPETENSI       │  FB-018-3:2012 SALES & MARKETING OPERATION│
├──────────────────────┼──────────────────────────────────────────┤
│                      │  C01 MARKET & PRODUCT SURVEY      ← bold │
│ NAMA UNIT KOMPETENSI │  C02 DIRECT / RETAIL SALES               │
│                      │  C03 AFTER SALES SERVICE                 │
│                      │  C04 SELF SALES PERFORMANCE ASSESSMENT ← bold │
│                      │  C05 ONLINE SALES                 ← bold │
│                      │  C06 PRODUCT MARKETING                   │
├──────────────────────┼──────────────────────────────────────────┤
│ NAMA CALON           │                                          │
│ NO KAD PENGENALAN    │   (blank, for the candidate)             │
│ TARIKH PENILAIAN     │                                          │
│ MASA MULA            │                                          │
│ MASA TAMAT           │                                          │
└──────────────────────┴──────────────────────────────────────────┘
```

The centre name is **CHARACTER INTERNATIONAL ACADEMY SDN. BHD.** `VIZTECH TRADING
SDN. BHD.` appears only in files we uploaded ourselves — it was copied in by
mistake and is a different accredited centre.

Below the table, in this order: `Arahan kepada calon:` (six numbered items),
`KERTAS INI MENGANDUNGI n MUKA SURAT BERCETAK` (centred, bold), and a small
bordered signature box for `Disemak dan Disahkan oleh : Fasilitator Pembangunan
Soalan / PPL :` with `Nama :`, `Tarikh :`, `No. Rujukan Fasi :`.

### Authoring tokens

A pipe-table cell is one line of markdown, so a cover table cannot be written with
plain markdown alone. Two sentinels bridge that; `_engine/render/ppa_docx.py`
resolves both.

| Token | Becomes | Why not the obvious thing |
|---|---|---|
| `⟪LOGO⟫` | the Jata Negara crest, centred in that cell | An image in a markdown table cell survives pandoc badly; the token is unambiguous and lets the renderer size it |
| `⏎` | a real Word line break (`w:br`) inside the run | `<br>` is dropped silently by pandoc's docx writer, welding words together — `KEMAHIRANKEMENTERIAN SUMBER MANUSIAARAS`. A `w:br` also preserves each run's bold, which the cover needs |

So the cover's first two rows are authored as:

```markdown
| ⟪LOGO⟫ | **JABATAN PEMBANGUNAN KEMAHIRAN**⏎**KEMENTERIAN SUMBER MANUSIA**⏎ARAS 7 & 8 SETIA PERKASA 4,⏎KOMPLEKS SETIA PERKASA⏎62530 PUTRAJAYA |
|---|---|
| **KOD DAN NAMA PUSAT BERTAULIAH/SYARIKAT** | CHARACTER INTERNATIONAL ACADEMY SDN. BHD. |
```

The renderer also knows not to shade a row containing `⟪LOGO⟫`: it is a masthead,
not a column heading.

## 3. Bold on the cover means "assessed practically" — CONFIRMED

**Confirmed by Jay, 2026-08-25 23:39: "the bold is her selected cu for exam."**

So the cover is not decoration — it is where the competency-unit selection is
*recorded*. Two consequences:

1. **Read it.** Any paper Jennifer owns states her CU choice in its cover
   formatting. Extract it with span fonts before asking her:
   ```bash
   uv run --with pymupdf python -c "
   import pymupdf
   for b in pymupdf.open('<her.pdf>')[0].get_text('dict')['blocks']:
     for l in b.get('lines', []):
       for s in l['spans']:
         if s['text'].strip()[:1] in 'CEM' and s['text'].strip()[1:3].isdigit():
           print('BOLD' if 'Bold' in s['font'] else '    ', s['text'].strip())"
   ```
2. **Do not write it without her.** Bolding a unit asserts a decision. Where no
   profile exists yet, every unit stays unbolded — which is why the N821, M731,
   G471 and FB-018-45 covers currently show none.

Checked 2026-08-25: of the five other subjects, **none has a Jennifer-owned paper
at all** — her folders hold only the official NOSS PDFs and our uploads. Her
selection for those genuinely does not exist yet, and the worksheets in
`_engine/worksheets/` are the only way to obtain it.



Verified mechanically by span font in `jen-skema-setA.pdf` page 1:

```
BOLD  C01 MARKET & PRODUCT SURVEY            [Arial-BoldMT]
      C02 DIRECT / RETAIL SALES              [ArialMT]
      C03 AFTER SALES SERVICE                [ArialMT]
BOLD  C04 SELF SALES PERFORMANCE ASSESSMENT  [Arial-BoldMT]
BOLD  C05 ONLINE SALES                       [Arial-BoldMT]
      C06 PRODUCT MARKETING                  [ArialMT]
```

C01, C04, C05 — exactly the three units Jennifer later spelled out in words at
00:02 on 2026-08-25. **The selection had been in the document all along, encoded as
bold**, and text extraction drops formatting, so the generator saw six identical
units and chose for itself.

WhatsApp, 2026-08-24 23:17:
> **Jay:** 你这边加粗的意思是选那些加粗的 cu 对吗？可能 ai 误会了
> **Jennifer:** 对

This is why `_engine/profiles/*.json` exists: a decision carried only by visual
formatting does not survive a pipeline. Carry it as data.

## 4. Page header

Every page, **top right**, small bold: the paper reference code.

```
FB-018-3:2012/2026/A/01
```

Format: `<NOSS code>/<year>/<SET letter>/<running number>`. The page number sits
centred at the **bottom**. Not the other way round.

## 5. Section order and shape — SOALAN

`A. TEMPOH MASA` → `B. KETERAMPILAN` → `C. TUGASAN` → `D. SENARAI BAHAN / DOKUMEN`
→ `E. SENARAI PERALATAN` → `F. KRITERIA PENILAIAN` → `APPENDIX 1…5`.

- A and B use a colon-led value on the following line (`: 3 HOURS`).
- `B. KETERAMPILAN` names only what is assessed **practically**. Hers reads
  "CONDUCT MARKET & PRODUCT SURVEY, PREPARE ONLINE SALES COLLATERAL AND EVALUATE
  SALES PERFORMANCE" — three things, matching the three bold units. No direct
  sales pitch, no inventory control.
- `C. TUGASAN` item 1 lists activities I / II / III; item 2 lists the forms the
  candidate must complete, with the parenthetical
  `(Handwriting or Digital Form submission are acceptable)`.
- D and E are bordered tables: `NO. | … | UKURAN (UNIT) | KUANTITI (Bahan:Calon)`.
- F lists the four criteria with Malay labels and English descriptions, and closes
  with the boxed `PERINGATAN:` about the critical item.
- Appendices: 1 company/product brief · 2 market survey raw + verified data ·
  3 survey planning & questionnaire form · 4 online sales collateral & FAQ form ·
  5 self sales performance assessment report form.

## 6. SKEMA specifics

Cover carries three blocks the SOALAN does not:

```
UNTUK KEGUNAAN PEMERIKSA SAHAJA        ← centred, bold

AMARAN
Skema Pemarkahan ini SULIT. Kegunaannya khusus untuk pemeriksa yang berkenaan
sahaja. Sebarang maklumat dalam Skema Pemarkahan ini tidak boleh dimaklumkan
kepada sesiapa.

SKEMA PEMARKAHAN INI MENGANDUNGI n MUKA SURAT BERCETAK TERMASUK MUKA HADAPAN
```

Its identification table ends with a `TARIKH` row instead of the candidate block,
and labels the elective row `NAMA UNIT KOMPETENSI ELEKTIF`.

Page 2 carries the marking scale, verbatim:

```
SKALA PEMARKAHAN
0 = Tidak Dilakukan/Salah   1 = Tidak Memuaskan   2 = Memuaskan   3 = Sangat Memuaskan

Pengiraan Pemarkahan:
   Markah Diperolehi
  ─────────────────── X % Pemberat
     Markah Penuh

• % Pemberat akan ditentukan oleh pakar yang membangunkan soalan
```

## 7. ASSESSMENT ANSWER SHEET is a model answer, not a blank form

8 pages. It reproduces Appendices 3, 4 and 5 **with the correct answers filled in,
printed in red**, against the same scenario as the SOALAN (hers: Seri Harmoni
Residence). It is the examiner's reference for what a competent candidate's
completed forms should look like.

> Our version was three pages of blank answer blocks — a different document
> entirely. This file had never been audited before 2026-08-25; the 2026-08-21
> audit listed it as `未审`.

## 8. EQUIPMENT VERIFICATION is one page, on a JPK form

Header top right: `JPK/PPA-PPT/SP/1:2022` — a JPK form number, not ours to invent.

Title: `VERIFICATION FORM FOR PPA-PPT EQUIPMENT CHECK`, then
`Applicant / PPA-PPT: ______` and `Verification Date: ______`.

A header block table:

| | |
|---|---|
| NOSS Code & Programme Name | FB-018-3:2012 SALES & MARKETING OPERATION |
| SET | (SET A / SET B) |
| Competency | (the three practical units) |
| Critical Item | (the critical-item sentence) |
| Assessment Duration | 3 HOURS |

Then the checklist — one page, 14 rows in hers:

| NO. | LIST OF EQUIPMENT, MATERIALS AND DOCUMENTS BASED ON QUANTITY | RATIO (P:C) | QUANTITY AVAILABLE — Filled by Applicant | QUANTITY AVAILABLE — JPK Verification |
|---|---|---|---|---|

Closing: `Signature: ______` and `Date: ______`.

> Ours was three pages with an invented structure.

## 9. Known defects in the authoritative files

Recorded, not copied:

- SKEMA cover declares `14 MUKA SURAT` but the PDF is **11 pages**. SOALAN
  declares `13` but is **14 pages**. Do not reproduce; render and backfill.
- `D. SENARAI BAHAN / DOCUMEN` — Malay is `DOKUMEN`. Hers has the typo on the
  SOALAN. We use the correct spelling.
- The cover lists `E01 INVENTORY CONTROL` as an elective, but nothing in the paper
  or the skema scores it. Jennifer's instruction of 2026-08-25 00:02 removes E01
  entirely, which resolves this.
- `Terlibut` for `Terlibat` in the skema's `CU Terlibat` column.
