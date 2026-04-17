# JPK WIM Format Specification

**Status:** Canonical. This is the format every WIM `.md` in this project must follow.
**Source of truth:** Reference PDFs under `raw/folder-1-wim-panduan/` and `raw/folder-2-sample-wim/` — official JPK (Jabatan Pembangunan Kemahiran) samples.
**Implemented by:** `.claude/skills/wim-jpk-format/` (skill + scripts).

## 1. Why a fixed format

Malaysian JPK (Jabatan Pembangunan Kemahiran, Ministry of Human Resources) requires every Written Instructional Material submitted for NOSS accreditation to follow a rigid house style. Jennifer's reference samples confirm every WIM begins with:

1. Government crest / JPK logo (first page)
2. JPK Putrajaya address block (Malay)
3. Malay document-type label (e.g. `KERTAS PENERANGAN`)
4. Structured identification table (program / level / CU / work activities / WIM code / paper colour)
5. Document-type-specific fields (TAJUK, TUJUAN, TEMPAT, TEMPOH, ARAHAN as applicable)

Without this envelope the material will be rejected at JPK review regardless of pedagogical quality.

## 2. Scope

Applies to every `.md` inside a CU folder across the 4 subjects:

| Subject | Folder | NOSS code |
|---------|--------|-----------|
| Tuinalogy Services | `tuinalogy-services/` | MP-031-3:2016 |
| Aesthetic Services | `aesthetic-services/` | S960-002-3:2020 |
| BEV Diagnostic & Rectification | `bev-diagnostic-rectification/` | G452-010-3:2023 |
| Computer System Management | `it-computer-system/` | IT-020-3:2013 |

**In scope:** `PM-teori.md`, `PM-amali.md`, `KP-*.md`, `KT-*.md`, `KK-*.md`, `KA.md`, `PA.md`.
**Out of scope** (skipped by the enhancer): `00-README.md`, `00-cocu.md`, `00-noss-extract.md`, `01-jpw-distribution.md` — these are overview / metadata, not WIM deliverables.

## 3. Envelope template

Every WIM begins with this block, delimited by HTML comment markers for idempotency:

```markdown
<!-- JPK_ENVELOPE_v1 -->
![JPK Logo](../_assets/logos/jpk-logo.png)

**JABATAN PEMBANGUNAN KEMAHIRAN (JPK)**
TINGKAT 7-8, BLOK D4, KOMPLEKS D,
PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,
62530 PUTRAJAYA

## {DOCUMENT_TYPE_LABEL}

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | {NOSS} {PROGRAM_NAME_BM} |
| TAHAP | {LEVEL} |
| KOD DAN TAJUK UNIT KOMPETENSI | {NOSS}-{CU} {CU_TITLE_EN} |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. {WA1}<br>2. {WA2}<br>3. {WA3}<br>4. {WA4} |
| NO. KOD | {WIM_CODE} |
| Muka Surat | 1/1 |
| WARNA KERTAS | {COLOR_BM} ({COLOR_EN}) |

**TAJUK:** {title from existing H1}

**TUJUAN:** {first paragraph of existing intro / learning outcomes}

{doc-type-specific fields: see section 5}
<!-- /JPK_ENVELOPE_v1 -->

{original content preserved below, untouched}
```

## 4. Document types

| Doc ID | Malay label (`DOCUMENT_TYPE_LABEL`) | Paper colour | Code suffix |
|--------|-------------------------------------|---------------|-------------|
| PM-teori | `PELAN MENGAJAR – TEORI` | KUNING (Yellow) | `/PM(TEORI)` |
| PM-amali | `PELAN MENGAJAR – AMALI` | KUNING (Yellow) | `/PM(AMALI)` |
| KP | `KERTAS PENERANGAN` | PUTIH (White) | `/KP({seq}/{total})` |
| KT | `KERTAS TUGASAN` | MERAH JAMBU (Pink) | `/KT({seq}/{total})` |
| KK | `KERTAS KERJA` | BIRU (Blue) | `/KK({seq}/{total})` |
| KA | `KERTAS PENILAIAN PENGETAHUAN` | MERAH JAMBU (Pink) | `/KA` |
| PA | `KERTAS PENILAIAN PRESTASI` | BIRU MUDA (Light Blue) | `/PA` |

WIM code format: `{NOSS}-{CU}{suffix}`. Example: `MP-031-3:2016-C01/KP(1/4)`.

## 5. Doc-type-specific fields

Added below `TUJUAN`, above `<!-- /JPK_ENVELOPE_v1 -->`:

**PM-teori / PM-amali:**
- `**TEMPAT:**` — `BILIK KULIAH` for teori, `BILIK AMALI / MAKMAL` for amali
- `**TEMPOH:**` — hours per JPW/RK
- `**TUJUAN PENGAJARAN:**` — lesson outcomes
- `**ALAT BANTUAN MENGAJAR:**` — teaching aids

**KT / KK:**
- `**ARAHAN:**` — instructions for trainee to follow the task/work procedure

**KA / PA:**
- `**ARAHAN:**` — instructions for the assessment

## 6. Idempotency contract

The enhancer (`scripts/enhance_wim_jpk.py`) uses the HTML comment markers `<!-- JPK_ENVELOPE_v1 -->` / `<!-- /JPK_ENVELOPE_v1 -->` to detect and replace the envelope:

- If markers present: strip old envelope, rebuild from current subject metadata.
- If markers absent: prepend new envelope above the existing content.
- Legacy in-file metadata lines (e.g. `**WIM 编码：**`, `**NOSS：**`, `**CU：**`, `**时数：**`) are stripped because that data now lives in the identification table.
- Running the enhancer twice on a clean tree produces an empty diff.

## 7. Assets

Per-subject JPK logo at `<subject>/_assets/logos/jpk-logo.png` (66 KB, extracted once from `raw/folder-1-wim-panduan/C01/0. COVER.pdf`). Each logo folder includes `ATTRIBUTION.md` noting it is a Malaysian government crest used for official WIM compliance.

## 8. Per-subject metadata

Centralised in `.claude/skills/wim-jpk-format/data/subjects.json`:
- `root` — subject folder name
- `noss_code`, `program_en`, `program_bm`, `level`
- `cus.{CU}.title_en`, `cus.{CU}.title_bm`, `cus.{CU}.work_activities[]`

When adding a new CU or subject, update `subjects.json` and re-run.

## 9. Usage

```bash
# Extract logo once per subject (requires pymupdf)
uv run --with pymupdf python .claude/skills/wim-jpk-format/scripts/extract_logo.py all

# Dry-run (writes .md.preview beside each file)
python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py tuinalogy --cu C01 --dry-run

# Apply to one subject
python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py tuinalogy

# Apply to all 4 subjects
python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py all
```

## 10. Verification checklist

After running:
- `git diff --stat` — additions only in the envelope region, no Chinese content removed.
- Run twice — second run reports `changed=0`.
- Spot-check 3 files: envelope present, table filled, original content below.
- Every CU folder has `_assets/logos/jpk-logo.png` accessible via the `../_assets/logos/jpk-logo.png` relative path.

## 11. Open items / future work

- Extract JPW hours per CU into `subjects.json` so `TEMPOH` can be filled exactly (currently uses a placeholder pointing to JPW/RK).
- Populate `ALAT BANTUAN MENGAJAR` per lesson from each PM's existing teaching-aids table instead of using a generic default.
- Add a regeneration hook in `build/wim_consolidate_all.py` to consume the envelope when producing the final DOCX.
