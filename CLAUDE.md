# CLAUDE.md — NOSS to WIM Conversion Project

## Agent Onboarding (read in order)

1. **`INDEX.md`** — directory manifest; fastest way to locate any file or subject
2. **`LOG.md`** — dated activity log (Karpathy-style); reconstructs recent changes and intent
3. **This file** — rules, conventions, build commands

> **Always scan INDEX.md before walking the tree.** It lists every subject, CU structure, build output, and external reference. LOG.md gives the "why" behind recent work.

## Project

Convert NOSS documents into WIM (Written Instructional Materials / Bahan Pengajaran Bertulis) for **4 subjects**:

1. **Tuinalogy** — MP-031-3:2016 Tuinalogy Services 推拿疗法 (Level 3) — **Simplified Chinese**, with bilingual EN/BM clinical terms
2. **BEV** — G452-010-3:2023 Battery Electric Vehicle Diagnostic and Rectification (Level 3)
3. **Aesthetic** — S960-002-3:2020 Aesthetic Services (Level 3)
4. **IT** — IT-020-3/4/5:2013 Computer System Management (Levels 3, 4, 5)

## Key Paths

| What | Path |
|------|------|
| Project root | `C:\Users\Jyue\Documents\1-projects\noss-to-wim\` |
| Tuinalogy WIM | `tuinalogy-services/` |
| Aesthetic WIM | `aesthetic-services/` |
| BEV WIM | `bev-diagnostic-rectification/` |
| IT WIM | `it-computer-system/` |
| Reference docs | `_reference/` |
| Agent prompts | `_agents/` |
| Jennifer's sample WIM PDFs | `raw/folder-1-wim-panduan/`, `raw/folder-2-sample-wim/` |
| Tuinalogy images | `tuinalogy-services/_assets/{meridians,acupoints,anatomy,techniques,clinical}` |
| Tuinalogy attribution manifest | `tuinalogy-services/_assets/ATTRIBUTION.md` |
| BEV source PDF | `C:\Users\Jyue\Downloads\G452-010-3-2023 Battery Electric Vehicle (BEV) Diagnostic and Rectification.pdf` |
| Aesthetic source PDF | `C:\Users\Jyue\Downloads\S960-002-3-2020 AESTHETIC SERVICES.pdf` |
| IT source (existing) | `C:\Users\Jyue\Documents\1-projects\noss-it020-textbook\` |

## WIM Structure per CU

Each Competency Unit folder contains:
- `PM-teori.md` — Theory Lesson Plan (yellow paper)
- `KP-XX.md` — Information Sheets (white paper) — one per knowledge topic
- `KT-XX.md` — Assignment Sheets (pink paper) — one per KP
- `PM-amali.md` — Practical Lesson Plan (yellow paper)
- `KK-XX.md` — Work Sheets (blue paper) — one per work activity
- `KA.md` — Knowledge Assessment (pink paper)
- `PA.md` — Performance Assessment (light blue paper)

## WIM Coding Format

`[NOSS Code]-[CU Code]/[Doc Code]([Seq]/[Total])`

Examples:
- `G452-010-3:2023-C01/KP(1/4)` = Info Sheet 1 of 4 for BEV CU 1
- `MP-031-3:2016-C02/KP(1/3)(PUTIH)` = Tuinalogy CU 2 Info Sheet 1 of 3 (white paper)

## Rules

- Source of truth: NOSS PDF extractions in each subject's `00-noss-extract.md`
- 30% Knowledge / 70% Performance split for all training hours
- Every Related Knowledge item in CoCU must be covered by a KP
- Every Work Activity must be covered by a KK
- Use professional, government-standard language
- Include bilingual terms where appropriate (EN + BM for BEV/Aesthetic/IT; 中英马 for Tuinalogy)
- Do NOT add content not supported by the NOSS CoCU
- Assessment must align with CoCU Assessment Criteria
- **Tuinalogy safety:** always preserve 孕期禁忌五穴 (pregnancy contraindications: 合谷 LI4, 三阴交 SP6, 肩井 GB21, 至阴 BL67, 昆仑 BL60) — never recommend these on pregnant clients
- **Image licensing:** every image in `_assets/` must have an entry in `ATTRIBUTION.md` (CC BY / CC BY-SA / PD only — no arbitrary web scraping)
- **Log every significant change** to `LOG.md` — append a new dated entry, do not rewrite history
- **JPK envelope required on every WIM:** every `.md` in a CU folder must begin with the `<!-- JPK_ENVELOPE_v1 -->` block (logo + JPK address + Malay doc-type label + identification table). Spec: `07-jpk-format-spec.md`. Regenerate via `python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py <subject|all>` — idempotent.

## Build Commands

```bash
# Single .md → .docx (per-file, JPK-formatted with paper colour)
uv run python build/wim_md_to_docx.py <input.md> --style KP --output out.docx

# All 4 subjects into one consolidated .docx
uv run python build/wim_consolidate_all.py

# Tuinalogy only
uv run python build/wim_consolidate_all.py --subject tuina --output build/WIM-Tuinalogy.docx
```

After opening output .docx in Word, **right-click TOC → Update Field → Update entire table** to populate page numbers.

## Reference Documents

- Buku Panduan WIM Edisi 2020 (effective Jan 2021): https://anyflip.com/jpvdh/aagk/basic
- MySPIKE: https://www.myspike.my
- Jennifer's Drive folder 1 (WIM panduan samples): https://drive.google.com/drive/folders/1RqufqB60euIIm-pt_08S9v98rDLV8FCN
- Jennifer's Drive folder 2 (sample WIM): https://drive.google.com/drive/folders/1tu1dmkkI6H-pnX53qRQAWnzsgauTUc0f
- Both folders downloaded locally into `raw/` — use them as format-compliance references when drafting new WIM
