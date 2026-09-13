# CLAUDE.md — NOSS to WIM Conversion Project

## Project

Convert NOSS documents into WIM (Written Instructional Materials / Bahan Pengajaran Bertulis) for 3 subjects:
1. **BEV** — G452-010-3:2023 Battery Electric Vehicle Diagnostic and Rectification (Level 3)
2. **Aesthetic** — S960-002-3:2020 Aesthetic Services (Level 3)
3. **IT** — IT-020-3/4/5:2013 Computer System Management (Levels 3, 4, 5)

## Key Paths

| What | Path |
|------|------|
| Project root | `C:\Users\Jyue\Documents\1-projects\noss-to-wim\` |
| BEV WIM | `bev-diagnostic-rectification/` |
| Aesthetic WIM | `aesthetic-services/` |
| IT WIM | `it-computer-system/` |
| Reference docs | `_reference/` |
| Agent prompts | `_agents/` |
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

Example: `G452-010-3:2023-C01/KP(1/4)` = Info Sheet 1 of 4 for CU 1

## Rules

- Source of truth: NOSS PDF extractions in each subject's `00-noss-extract.md`
- 30% Knowledge / 70% Performance split for all training hours
- Every Related Knowledge item in CoCU must be covered by a KP
- Every Work Activity must be covered by a KK
- Use professional, government-standard language
- Include bilingual terms where appropriate (EN + BM)
- Do NOT add content not supported by the NOSS CoCU
- Assessment must align with CoCU Assessment Criteria

## Build Commands

```bash
# Future: Generate .docx from .md content
# Will be implemented after .md content is confirmed
```

## Reference Documents

- Buku Panduan WIM Edisi 2020 (effective Jan 2021): https://anyflip.com/jpvdh/aagk/basic
- MySPIKE: https://www.myspike.my
- Google Drive refs: https://drive.google.com/drive/folders/1RqufqB60euIIm-pt_08S9v98rDLV8FCN
