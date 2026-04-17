---
name: wim-jpk-format
description: Apply Malaysian JPK (Jabatan Pembangunan Kemahiran) standard envelope format to WIM markdown files across all NOSS subjects. Prepends government logo, JPK address block, document-type label, and identification table to every .md.
---

# WIM JPK Format Skill

Enhance Written Instructional Materials (WIM) markdown files so they comply with the JPK (Jabatan Pembangunan Kemahiran) house style. Every WIM document in a NOSS project begins with a standard envelope: government logo, JPK Putrajaya address, Malay document-type label, and a structured identification table listing program/CU/work-activity metadata.

## When to use

Trigger this skill when the user asks to:
- "Apply JPK format to WIM"
- "Make WIM look like the reference samples"
- "Add government logo to WIMs"
- "Format WIMs to Malaysian JPK standard"

Applies to any subject folder under `noss-to-wim/` that has CU subfolders with `PM-teori.md`, `PM-amali.md`, `KP-*.md`, `KT-*.md`, `KK-*.md`, `KA.md`, `PA.md`.

## Architecture

| Path | Role |
|------|------|
| `SKILL.md` | This file — usage and spec |
| `scripts/extract_logo.py` | One-time: extract JPK crest from a reference PDF cover |
| `scripts/enhance_wim_jpk.py` | Main enhancer — idempotent, per subject or all |
| `data/subjects.json` | Per-subject metadata (NOSS code, CU titles, work activities) |

## Usage

```bash
# 1. Extract JPK logo (once, per subject root)
uv run --with pymupdf python .claude/skills/wim-jpk-format/scripts/extract_logo.py <subject>

# 2. Dry-run a single CU
python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py tuinalogy --cu C01 --dry-run

# 3. Apply to one subject
python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py tuinalogy

# 4. Apply to all subjects
python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py all
```

Subject keys: `tuinalogy`, `aesthetic`, `bev`, `it`, or `all`.

## JPK Envelope format

Every enhanced file begins with:

```markdown
<!-- JPK_ENVELOPE_v1 -->
![JPK Logo](../_assets/logos/jpk-logo.png)

**JABATAN PEMBANGUNAN KEMAHIRAN (JPK)**
TINGKAT 7-8, BLOK D4, KOMPLEKS D,
PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,
62530 PUTRAJAYA

## {DOCUMENT_TYPE_LABEL_IN_MALAY}

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | {NOSS_CODE} {PROGRAM_NAME_BM} |
| TAHAP | {LEVEL} |
| KOD DAN TAJUK UNIT KOMPETENSI | {NOSS}-{CU} {CU_TITLE_EN} |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. {WA1}<br>2. {WA2}<br>3. {WA3}<br>4. {WA4} |
| NO. KOD | {WIM_CODE} |
| Muka Surat | 1/1 |
| WARNA KERTAS | {COLOR_MALAY} ({COLOR_EN}) |

**TAJUK:** {title from existing H1 or filename}

**TUJUAN:** {first paragraph of existing intro / learning outcomes}
<!-- /JPK_ENVELOPE_v1 -->

---

{original content, untouched}
```

## Document types

| Doc ID | Malay Label | Paper Color | WIM code suffix |
|--------|-------------|-------------|-----------------|
| PM-teori | PELAN MENGAJAR – TEORI | KUNING (Yellow) | `/PM(TEORI)` |
| PM-amali | PELAN MENGAJAR – AMALI | KUNING (Yellow) | `/PM(AMALI)` |
| KP | KERTAS PENERANGAN | PUTIH (White) | `/KP({seq}/{total})` |
| KT | KERTAS TUGASAN | MERAH JAMBU (Pink) | `/KT({seq}/{total})` |
| KK | KERTAS KERJA | BIRU (Blue) | `/KK({seq}/{total})` |
| KA | KERTAS PENILAIAN PENGETAHUAN | MERAH JAMBU (Pink) | `/KA` |
| PA | KERTAS PENILAIAN PRESTASI | BIRU MUDA (Light Blue) | `/PA` |

## Idempotency

- Script detects `<!-- JPK_ENVELOPE_v1 -->` at top of file.
- If found, the envelope is replaced (content below `<!-- /JPK_ENVELOPE_v1 -->` preserved).
- If absent, envelope is prepended above the existing content.
- Legacy metadata block (lines starting with `**WIM 编码：**`, `**NOSS：**`, etc.) is stripped when prepending, since that data is now in the identification table.

## Verification

After run, check:
1. `git diff --stat` shows additions only for envelope region.
2. Run script twice — second run diff is empty.
3. Spot-check 3 files across subjects: envelope present, table filled, original content intact.

## Skipped files

- `00-cocu.md`, `00-noss-extract.md`, `00-README.md`, `01-jpw-distribution.md` — metadata/overview, not WIM deliverables.
- Files outside CU subfolders.
