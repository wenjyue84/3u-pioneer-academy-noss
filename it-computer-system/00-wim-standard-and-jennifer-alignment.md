# WIM Standard & Jennifer-Alignment — IT-020 Computer System

**Created:** 2026-06-23
**Purpose:** Define the verified WIM standard (from Jennifer's NOSS-passing samples), record the best-of-breed decisions between Jennifer's version and ours, and lay out the build plan to bring all IT-020 WIM into full conformance.

> Read this before authoring or regenerating any IT-020 WIM file.

---

## 1. The two-layer model — NOSS vs WIM (do not confuse)

| Layer | What it is | Where it lives |
|-------|-----------|----------------|
| **NOSS** | The occupational *standard* (CoCU, work activities, hours). The INPUT. | Jay's 3 Google Docs (IT-020-3/4/5) + `raw/NOSS-IT-020-*.docx` |
| **WIM** | The *teaching materials* derived from the NOSS (KP/KK/KT/KA/PA/PM). The OUTPUT. | `it-computer-system/L{3,4,5}-C##/` |

Jennifer's shared Drive folder contains **WIM** (verified, NOSS-passing) — **not** NOSS. WIM is produced *from* NOSS; the two are never swapped. "Enhance my NOSS using Jennifer's files" therefore means: use Jennifer's WIM as the verified *format/standard reference* for the WIM we build, **not** edit the NOSS docs.

---

## 2. Jennifer's verified standard (the gold reference)

Source: `raw/folder-3-jennifer-it020-2026-06-21/` (PDFs/DOC) + `raw/md/folder-3-jennifer-it020/` (markdown). Verified to pass NOSS for IT-020-3:2013.

### 2.1 JPK envelope (every WIM document begins with this)
- Logo (left) + **JABATAN PEMBANGUNAN KEMAHIRAN (JPK)** Putrajaya address (right)
- Document-type heading: `KERTAS PENERANGAN`, `KERTAS KERJA`, etc.
- Metadata table: `KOD DAN NAMA PROGRAM` · `TAHAP` · `KOD DAN TAJUK UNIT KOMPETENSI` · `NO. DAN PERNYATAAN AKTIVITI KERJA` (the full work-activity list) · `NO. KOD` · `Muka Surat` · `WARNA KERTAS`
- `TAJUK:` (real topic title) → `TUJUAN:` → body (`PENERANGAN` / `SOALAN` / `RUJUKAN`)

### 2.2 Document types & paper colours
| Code | Type | Paper |
|------|------|-------|
| KP | Kertas Penerangan (Information Sheet) | PUTIH (White) |
| KT | Kertas Tugasan (Assignment Sheet) | MERAH JAMBU (Pink) |
| KK | Kertas Kerja (Work Sheet) | BIRU (Blue) |
| KA | Kertas Penilaian Pengetahuan (Knowledge Assessment) | MERAH JAMBU (Pink) |
| PA | Kertas Penilaian Prestasi (Performance Assessment) | BIRU MUDA (Light Blue) |
| PM-teori / PM-amali | Pelan Mengajar (Lesson Plan) | KUNING (Yellow) |

### 2.3 Document coding
- Jennifer's samples use single-letter codes: `IT-020-3:2013-C01/P(1/18)` (Penerangan), `…/K(1/4)` (Kerja), `…/P(2/6)PM` (lesson plan), numbered sequentially across the whole CU, **no level prefix** in the code (the `-3:` in the NOSS code already encodes the level).
- **OPEN DECISION** — see §6. Our project (and the other 3 subjects) use two-letter codes `KP/KK/KT` tied one-per-work-activity, e.g. `IT-020-3:2013-C01/KP(1/7)`. Both are valid JPK conventions; pick one for consistency.

---

## 3. Best-of-breed decisions (Jennifer vs ours)

| Aspect | Winner | Rationale |
|--------|--------|-----------|
| Programme name (L3) | **Jennifer** | Ours was wrong ("Computer System Management"); correct = **Computer System Operation / Operasi Sistem Komputer** |
| CU titles & work activities | **Jennifer / NOSS** | Ours had fabricated 4-WA CUs; corrected to the real 7 CUs / 30 WAs |
| Envelope coding (no `L3-` prefix) | **Jennifer** | `IT-020-3:2013-C01` not `…-L3-C01` |
| Single clean header | **Jennifer** | Removed our redundant native header that duplicated the envelope |
| Body content depth | **Ours** | Our KP/KK have richer structure (learning objectives, tables, common-errors, decision criteria, labs) |
| Coverage / completeness | **Ours** | We have full KP/KK/KT×WA + KA/PA/PM per CU; Jennifer only shared sample sheets |
| Bilingual EN/BM phrasing | **Ours** | Kept where clearer |

Net: **keep our richer bodies, adopt Jennifer's correct envelope/metadata/coding and single-header layout.**

---

## 4. Corrected IT-020-3:2013 CU map (7 CUs, 1,200 hrs)

| CU | Title (EN) | WAs | Hrs |
|----|-----------|-----|-----|
| C01 | Computer System Set-up | 7 | 300 |
| C02 | Computer System Maintenance | 4 | 120 |
| C03 | Computer System Repair | 4 | 180 |
| C04 | Server Installation | 5 | 240 |
| C05 | Server Maintenance | 4 | 180 |
| C06 | Computer Network Connectivity Set-up | 5 | 120 |
| C07 | Mobile Device Configuration | 4 | 60 |

Authoritative work-activity lists are now in `.claude/skills/wim-jpk-format/data/subjects.json` (`it` block) and `raw/NOSS-IT-020-3-*.docx`.

---

## 5. Current state — COMPLETE (2026-06-23)

All 20 CUs across the 3 levels are authored and fully conformant to the standard above (correct JPK envelope, programme name, CU title, codes, single header). **362 WIM files total.**

| Level | Programme | CUs | Files | Status |
|-------|-----------|-----|-------|--------|
| L3 | Computer System Operation | 7 (C01–C07) | 127 | ✅ complete |
| L4 | Computer Systems Administration | 6 (C01–C06) | 114 | ✅ complete |
| L5 | Computer Systems Management | 7 (C01–C06 + elective E01) | 121 | ✅ complete |

Per-CU file count = (3 × work-activities) KP+KK+KT + KA + PA + PM-teori + PM-amali.

Jennifer samples used as the verified reference: C01 KP(1/18 & 4/18), C02 KP(1/16), C07 KK(1/4), C07 PM(2/6 & 3/6) — in `raw/md/folder-3-jennifer-it020/`.

### Remaining — publish to Google Drive
Build `.docx` (`build/` pipeline) and/or mirror the folder structure into Jay's Google Drive (`docs.google.com`). Outward-facing write — confirm approach + authorization before executing.

---

## 6. Open decision (needs Jay)
**Coding convention:** keep our `KP/KK/KT(n/total-per-WA)` (consistent with the other 3 subjects + project CLAUDE.md) **or** switch IT to Jennifer's `P/K(n/total-sheets)` single-letter scheme for exact match to her samples. Default if unspecified: keep `KP/KK/KT`.

---

## 7. Fixes applied 2026-06-23
1. `subjects.json` `it` block — corrected programme name + all 7 CUs (titles + work activities) from NOSS/Jennifer.
2. `enhance_wim_jpk.py` — emit codes without the redundant `L3-` prefix; strip the redundant native header; recover real `TAJUK` title; CU-title fallback for KA/PA/PM; skip numbered lists in TUJUAN extraction.
3. L3-C01 — archived 25 bare-code duplicates, regenerated 25 descriptive files with correct envelopes (verified).
4. L3-C02 — archived bare KA duplicate, regenerated correct envelope.
