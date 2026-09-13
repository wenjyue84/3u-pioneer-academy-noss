# CLAUDE.md — 3U Pioneer Academy NOSS / JPK Project

## Start here

Read `INDEX.md` before walking the directory tree — it lists every subject, CU structure, and
external reference. Read `wiki/now.md` for current deadlines, focus, and blockers. Do not ask Jay
for status; read `wiki/now.md` instead, and update it when status changes.

## What this project is

Two parallel workstreams, one client (3U Pioneer Academy), one JPK accreditation goal.

**Workstream A — WIM generation** (the bulk of the work)
Convert NOSS standards into JPK-format Written Instructional Materials (WIM / Bahan Pengajaran
Bertulis). Seven document types per Competency Unit (CU): PM-teori, KP-XX, KT-XX, PM-amali,
KK-XX, KA, PA.

**Workstream B — PTPK / COPTPA proposals**
Grant proposals for PTPK Skim TBT and COPTPA accreditation. Deadline-sensitive — check
`wiki/now.md` first.

## Subject folders (Workstream A)

| Folder | NOSS Code | Language |
|--------|-----------|----------|
| `tuinalogy-services/` | MP-031-3:2016 | Simplified Chinese + bilingual EN/BM terms |
| `aesthetic-services/` | S960-002-3:2020 | BM/EN |
| `bev-diagnostic-rectification/` | G452-010-3:2023 | BM/EN |
| `it-computer-system/` | IT-020-3/4/5:2013 | BM/EN |
| `ai-digital-marketing/` | DM-001-3:2026 | BM/EN — COPTPA, C01–C08 + E01/E02 |
| `multimedia-interactive-design/` | J582-001-3:2019 | BM/EN — COPTPA 2023, in progress |
| `creative-multimedia-development/` | J582-001-4:2025 | BM/EN — stub, awaiting NOSS PDF |

## Proposals (Workstream B)

`proposals/` — PTPK Skim TBT proposals: `ai-dm-proposal.md`, `ai-admin-proposal.md`,
`ai-mfg-proposal.md`, `ai-iso-proposal.md`. Baseline snapshots in
`_archive/proposals-baseline-<DDMMYY>/`.

**Eligibility rule that governs every proposal:** the applicant (Penyedia Latihan) MUST already
hold active JPK or MQA *pentauliahan*, and must attach a Sijil Akuan Pentauliahan plus a
per-programme Surat Kelulusan Pentauliahan. An entity without accreditation cannot be the
applicant — it can only be an industry partner signing a LOC/LOA/MOA. Never draft a proposal that
names an unaccredited entity as applicant. Source: Garis Panduan §4.8, §8.1, Lampiran 1 item 2.1.

## WIM coding format

`[NOSS Code]-[CU Code]/[Doc Code]([Seq]/[Total])`

- `G452-010-3:2023-C01/KP(1/4)` — BEV CU1 Info Sheet 1 of 4
- `MP-031-3:2016-C02/KP(1/3)(PUTIH)` — Tuinalogy CU2 Info Sheet 1 of 3

## Non-negotiable rules

**Citing a regulation to anyone outside this repo — three things, never fewer.** A claim about what
JPK or PTPK requires travels as: (1) a **cropped image of the actual clause**, (2) the **verbatim
Malay text**, (3) the **source URL and page number**. A paraphrase on its own is worthless to the
person who has to act on it.

**Read every crop back before sending it.** Render the page, crop it, then open the crop and confirm
it actually contains the sentence you are claiming. On 2026-07-29 three of twelve crops had cut the
decisive line in half — the closing date, the clause number of 4.8, and both items of 10.2. A crop
that omits the sentence proves nothing and is worse than sending nothing. Source PDFs and verified
crops live in `raw/ptpk/`.

**Never fabricate.** Company names, SSM numbers, addresses, phone numbers, certificate numbers,
IC numbers, statistics — every one traces to a source you actually read. An unknown fact becomes a
greppable placeholder, never a plausible guess:

```
⟪TBD: what is needed | who must supply it | needed-by date⟫
```

Audit the outstanding set with `rg "⟪TBD" proposals/`. Never leave bare `—`, `______`, `XXXX`,
or `（由 X 补充）` — normalise them to the form above.

**Content**
- Source of truth for every CU: that subject's `00-noss-extract.md`. NEVER add content the NOSS
  CoCU does not support.
- 30% Knowledge / 70% Performance split across all training hours. Any hour block that breaks the
  ratio (e.g. a capstone project) must sit explicitly OUTSIDE the CU total and say so — do not
  bend the ratio to absorb it.
- Every Related Knowledge item → one KP. Every Work Activity → one KK.
- Assessment must map directly to CoCU Assessment Criteria.
- Bilingual terms: EN + BM for BEV/Aesthetic/IT/AI-DM; 中英马 for Tuinalogy.
- **Tuinalogy safety:** NEVER recommend 合谷 LI4, 三阴交 SP6, 肩井 GB21, 至阴 BL67, 昆仑 BL60 on
  pregnant clients (孕期禁忌五穴). This rule must survive every edit.

**Formatting**
- **JPK envelope required on every WIM file:** every `.md` inside a CU folder MUST begin with the
  `<!-- JPK_ENVELOPE_v1 -->` block. Spec: `wiki/07-jpk-format-spec.md`.
- Regenerate envelopes (idempotent):
  `python .claude/skills/wim-jpk-format/scripts/enhance_wim_jpk.py <subject|all>`
  Valid subject keys live in `.claude/skills/wim-jpk-format/data/subjects.json`.

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

After opening the .docx in Word: right-click TOC → Update Field → Update entire table.

## Key references

- PTPK Skim TBT garis panduan (19 Mei 2025) — the binding eligibility document:
  https://smart.ptpk.gov.my/WebContent/doc/Garis%20Panduan%20Pembiayaan%20Program%20TVET%20Berimpak%20Tinggi%2019%20Mei%202025_latest.pdf
  Enquiries: tvetberimpaktinggi@ptpk.gov.my
- Buku Panduan WIM Edisi 2020: https://anyflip.com/jpvdh/aagk/basic
- MySPIKE portal (accredited-centre lookup): https://www.myspike.my
- Jennifer's sample WIM sets (local): `raw/folder-1-wim-panduan/`,
  `raw/folder-2-sample-wim/`, `raw/folder-3-jennifer-it020-2026-06-21/`
- Jennifer's 2026-07-24 voice notes, transcribed: `wiki/08-jennifer-voicenotes-20260724.md`
  (machine transcription — verify before relying on any specific figure)

## Tools

Use these before writing an ad-hoc script. Every path below existed on disk when this block was generated (2026-09-11, hub_lint.py HUB-010); regenerate with `uv run …/_tools/hub-lint/hub_lint.py --path <this folder> --fix --rules HUB-010`.

| Kind | Command (run from this folder) | Notes |
|---|---|---|
| scripts | `uv run _tools/accuracy_auditor.py`, `uv run _tools/assessment-time-validator.py`, `uv run _tools/coverage_validator.py` +6 more in `_tools/` | 9 file(s) |
| scripts | `uv run _tools/analyzers/question_type_analyzer.py` | 1 file(s) |
| scripts | `uv run _tools/classifiers/question_difficulty_classifier.py` | 1 file(s) |
| scripts | `uv run _tools/enforcer/header_box_enforcer.py` | 1 file(s) |
| scripts | `uv run bev-diagnostic-rectification/_tools/generate-scenarios.py` | 1 file(s) |
| scripts | `uv run raw/scripts/_add_image_stories.py`, `uv run raw/scripts/_add_stories.py`, `uv run raw/scripts/_get_token.py` +17 more in `raw/scripts/` | 20 file(s) |
| scripts | `uv run scripts/_add_image_stories.py`, `uv run scripts/_add_stories.py`, `uv run scripts/_get_token.py` +32 more in `scripts/` | 35 file(s) |
| scripts | `uv run tools/apply-pregnancy-warnings.py`, `uv run tools/audit-regulatory-compliance.py`, `uv run tools/check-pregnancy-safety.py` +7 more in `tools/` | 10 file(s) |
