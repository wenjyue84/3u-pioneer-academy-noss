# INDEX — noss-to-wim Project Directory Manifest

> **Purpose:** Fast lookup table for every directory and key file. Designed for LLMs: read this instead of walking the tree. Keep lines short, paths absolute when useful, descriptions one-sentence.

**Last updated:** 2026-04-17

---

## Subjects (4)

| Subject | NOSS Code | Level | Folder | Status |
|---------|-----------|-------|--------|--------|
| **Tuinalogy** 推拿疗法 | MP-031-3:2016 | 3 | `tuinalogy-services/` | Active — enriched with images + Chinese WIM |
| **Aesthetic Services** | S960-002-3:2020 | 3 | `aesthetic-services/` | Content complete |
| **BEV Diagnostic & Rectification** | G452-010-3:2023 | 3 | `bev-diagnostic-rectification/` | Content complete |
| **IT Computer System** | IT-020-3/4/5:2013 | 3, 4, 5 | `it-computer-system/` | Content complete (L3 primary) |

## Top-level Reading Order

Follow `00-` through `06-` for project context:

| # | File | Topic |
|---|------|-------|
| 00 | `00-README.md` | Project overview — start here |
| 01 | `01-noss-overview.md` | What is NOSS (Malaysian occupational skills standard) |
| 02 | `02-wim-structure.md` | How WIM documents are organised (7 document types per CU) |
| 03 | `03-wim-coding-system.md` | WIM coding convention `[NOSS]-[CU]/[Doc]([Seq]/[Total])` |
| 04 | `04-wim-development-process.md` | Step-by-step WIM authoring workflow |
| 05 | `05-noss-to-wim-mapping.md` | How to map CoCU items to KP/KT/KK |
| 06 | `06-whatsapp-context.md` | Messages and context from stakeholders |
| — | `CLAUDE.md` | Agent onboarding instructions |
| — | `INDEX.md` (this file) | Directory manifest |
| — | `LOG.md` | Append-only project activity log |
| — | `10us.md` | Every-10-story Spiral milestone digest (Chinese) |

## Subject Structure (identical across all 4)

Each subject folder contains:
- `00-README.md` — subject entry point
- `00-noss-extract.md` — raw CoCU extraction from NOSS PDF (source of truth)
- `01-jpw-distribution.md` — 30/70 knowledge/performance hours
- `C01/`, `C02/`, ... — one folder per Competency Unit (core)
- `E01/`, `E02/`, ... — elective CUs (tuinalogy/aesthetic only)
- `_assets/`, `_reference/`, `_docs/` — supporting material

Each CU folder contains 7 WIM document types:

| File | Type | Paper colour | Purpose |
|------|------|--------------|---------|
| `PM-teori.md` | Lesson Plan | Yellow | Theory class plan |
| `KP-XX.md` | Information Sheet | White | Knowledge topic (one per Related Knowledge item) |
| `KT-XX.md` | Assignment Sheet | Pink | Exercises mirroring each KP |
| `PM-amali.md` | Lesson Plan | Yellow | Practical class plan |
| `KK-XX.md` | Work Sheet | Blue | Step-by-step practical activity |
| `KA.md` | Knowledge Assessment | Pink | Written exam paper |
| `PA.md` | Performance Assessment | Light blue | Practical skill evaluation |

## Tuinalogy-specific Additions

| Path | Description |
|------|-------------|
| `tuinalogy-services/_assets/` | 27 CC-licensed Wikimedia Commons images (5 categories) |
| `tuinalogy-services/_assets/meridians/` | 7 meridian charts (Wellcome Collection) |
| `tuinalogy-services/_assets/acupoints/` | 2 acupoint reference figures |
| `tuinalogy-services/_assets/anatomy/` | 6 skeletal/muscular/anatomical images |
| `tuinalogy-services/_assets/techniques/` | 5 historical massage / reflexology images |
| `tuinalogy-services/_assets/clinical/` | 7 tongue-diagnosis + clinical scene images |
| `tuinalogy-services/_assets/ATTRIBUTION.md` | **Legal manifest** — CC BY 4.0 / CC BY-SA 4.0 / PD attribution |
| `tuinalogy-services/_reference/pregnancy-safety-reference.md` | 禁忌五穴 (孕期五大禁忌穴位) safety doc |
| `tuinalogy-services/_reference/regulatory-compliance-matrix.md` | Malaysian T&CM Act 2013 / OSHA / PDPA compliance |
| `tuinalogy-services/_reference/tcm-terminology-index.md` | Trilingual 中英马 TCM terminology (经络/八纲/四诊) |

All Tuinalogy WIM markdown is written in **Simplified Chinese (简体中文)** with bilingual EN/BM terms for clinical vocabulary.

## Top-level Utility Folders

| Path | Contents |
|------|----------|
| `_agents/` | Agent prompts and templates |
| `_data/` | Data files (extracted JSON, CSVs) |
| `_reference/` | Cross-subject reference (coverage matrix, industry standards) |
| `_tools/` | Project-specific tool scripts |
| `build/` | Docx builders + outputs |
| `scripts/` | Helper scripts |
| `tests/`, `tools/` | Test suites and tooling |
| `validators/` | Content validators (CoCU coverage, pregnancy check, terminology consistency) |
| `test-reports/` | Latest validator output reports |
| `raw/` | **Jennifer's reference WIM samples** — sample JPK-format PDFs from Google Drive |

## Spiral State (autonomous enhancement loop)

| Path | Purpose |
|------|---------|
| `.spiral/` | Spiral runtime state — checkpoints, worker logs, iteration summaries |
| `.spiral/prd-backups/` | Auto-backups of prd.json before each iteration |
| `.spiral/crashes/` | Crash log — `index.json` for exit codes |
| `.spiral/test-suites/` | Smoke / regression / security / performance suites |
| `prd.json` | Product Requirements Document — all user stories (pass/pending) |
| `spiral.config.sh` | Spiral configuration (focus area, validation, cost controls) |
| `calibration.jsonl` | Story cost calibration data |
| `progress.txt` | Running progress log |

## Build Outputs

| File | Description |
|------|-------------|
| `build/WIM-Consolidated-All.docx` | All 4 subjects merged into single .docx (8.4 MB, ~433 md files) |
| `build/WIM-Tuinalogy.docx` | Tuinalogy-only .docx with embedded images (7.8 MB) |
| `build/wim_md_to_docx.py` | Single-file converter (read-only per project convention) |
| `build/wim_consolidate_all.py` | Batch consolidator with cover page + TOC + page numbers |

## Key External References

- **Buku Panduan WIM Edisi 2020**: https://anyflip.com/jpvdh/aagk/basic
- **MySPIKE**: https://www.myspike.my
- **Jennifer's Drive folder 1** (WIM panduan samples): https://drive.google.com/drive/folders/1RqufqB60euIIm-pt_08S9v98rDLV8FCN → `raw/folder-1-wim-panduan/`
- **Jennifer's Drive folder 2** (sample WIM): https://drive.google.com/drive/folders/1tu1dmkkI6H-pnX53qRQAWnzsgauTUc0f → `raw/folder-2-sample-wim/`

## Source PDFs (outside project)

| Subject | Path |
|---------|------|
| BEV | `C:\Users\Jyue\Downloads\G452-010-3-2023 Battery Electric Vehicle (BEV) Diagnostic and Rectification.pdf` |
| Aesthetic | `C:\Users\Jyue\Downloads\S960-002-3-2020 AESTHETIC SERVICES.pdf` |
| Tuinalogy | NOSS MP-031-3:2016 (extracted to `tuinalogy-services/00-noss-extract.md`) |
| IT | `C:\Users\Jyue\Documents\1-projects\noss-it020-textbook\` (pre-existing) |
