# CLAUDE.md — 3U Pioneer Academy NOSS / JPK Project

## Start here

Read `INDEX.md` before walking the directory tree. It lists every subject, CU structure, and
external reference. Read `wiki/now.md` for current deadlines, focus, and blockers — do not ask
Jay about status; read it instead.

## What this project is

Two parallel workstreams, one client (3U Pioneer Academy), one JPK accreditation goal:

**Workstream A — WIM Generator** (the bulk of the work)
Convert NOSS standards into JPK-format Written Instructional Materials (WIM / Bahan Pengajaran
Bertulis). Seven document types per Competency Unit (CU): PM-teori, KP-XX, KT-XX, PM-amali,
KK-XX, KA, PA.

**Workstream B — PTPK / COPTPA Proposals**
Grant proposals for Skim TBT 2026 and COPTPA accreditation. Deadline-sensitive — check
`wiki/now.md` first.

## Subject folders (Workstream A)

| Folder | NOSS Code | Language |
|--------|-----------|----------|
| `tuinalogy-services/` | MP-031-3:2016 | Simplified Chinese + bilingual EN/BM terms |
| `aesthetic-services/` | S960-002-3:2020 | BM/EN |
| `bev-diagnostic-rectification/` | G452-010-3:2023 | BM/EN |
| `it-computer-system/` | IT-020-3/4/5:2013 | BM/EN |
| `ai-digital-marketing/` | DM-001-3:2026 | BM/EN — COPTPA, C01–C07 + E01/E02 |
| `multimedia-interactive-design/` | J582-001-3:2019 | BM/EN — COPTPA 2023, in progress |
| `creative-multimedia-development/` | J582-001-4:2025 | BM/EN — stub, awaiting NOSS PDF |

## Proposal folder (Workstream B)

`proposals/` — four PTPK Skim TBT 2026 proposals: `ai-dm-proposal.md`, `ai-admin-proposal.md`,
`ai-iso-proposal.md`, `ai-mfg-proposal.md`. Deployed as web apps; see `wiki/now.md` for live URLs
and deadline status.

## WIM coding format

`[NOSS Code]-[CU Code]/[Doc Code]([Seq]/[Total])`

- `G452-010-3:2023-C01/KP(1/4)` — BEV CU1 Info Sheet 1 of 4
- `MP-031-3:2016-C02/KP(1/3)(PUTIH)` — Tuinalogy CU2 Info Sheet 1 of 3

## Non-negotiable rules

**Content**
- Source of truth for every CU: that subject's `00-noss-extract.md`. NEVER add content the NOSS
  CoCU does not support.
- 30% Knowledge / 70% Performance split across all training hours.
- Every Related Knowledge item → one KP. Every Work Activity → one KK.
- Assessment must map directly to CoCU Assessment Criteria.
- Use bilingual terms: EN + BM for BEV/Aesthetic/IT/AI-DM; 中英马 for Tuinalogy.
- **Tuinalogy safety:** NEVER recommend 合谷 LI4, 三阴交 SP6, 肩井 GB21, 至阴 BL67, 昆仑 BL60
  on pregnant clients (孕期禁忌五穴). This rule must survive every edit.

**Formatting**
- **JPK envelope required on every WIM file:** every `.md` inside a CU folder MUST begin with
  the `<!-- JPK_ENVELOPE_v1 -->` block. Spec: `wiki/07-jpk-format-spec.md`.
- Regenerate envelopes (idempotent):
  `python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py <subject|all>`
  Valid subject keys are in `.claude/skills/wim-jpk-format/data/subjects.json`.

**Images**
- Every image in `_assets/` MUST have an entry in `tuinalogy-services/_assets/ATTRIBUTION.md`.
  CC BY / CC BY-SA / PD only — no arbitrary web scraping.

**Logging**
- Append every significant change to `LOG.md`. Never edit existing entries.

## Build commands

```bash
# Single .md → .docx
uv run python build/wim_md_to_docx.py <input.md> --style KP --output out.docx

# All subjects consolidated
uv run python build/wim_consolidate_all.py

# One subject only
uv run python build/wim_consolidate_all.py --subject tuina --output build/WIM-Tuinalogy.docx
```

After opening .docx in Word: right-click TOC → Update Field → Update entire table.

## Key references (external)

- Buku Panduan WIM Edisi 2020: https://anyflip.com/jpvdh/aagk/basic
- MySPIKE portal: https://www.myspike.my
- Jennifer Drive 1 (WIM panduan, local): `raw/folder-1-wim-panduan/`
- Jennifer Drive 2 (sample WIM, local): `raw/folder-2-sample-wim/`
- Jennifer Drive 3 (IT-020 approved sample, local): `raw/folder-3-jennifer-it020-2026-06-21/`
