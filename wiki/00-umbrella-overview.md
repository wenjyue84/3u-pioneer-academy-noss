# 3U Pioneer Academy NOSS / JPK — Umbrella Overview

> **Client:** 3U Pioneer Academy Sdn Bhd
> **Lead:** Jay (Lew Wen Jyue) · **Contact:** Jennifer +60 12-611 1677 · **WhatsApp:** 商学院ADI IT Program
> **Status:** Active — WIM generation 3/4 subjects content-complete; IT-020 application in progress
> **See also:** [[story]] | [[01-noss-overview]] | [[02-wim-structure]] | [[07-jpk-format-spec]]

This project is the single home for all of 3U Pioneer Academy's work toward **JPK (Jabatan Pembangunan Kemahiran) skills-training accreditation**. On 2026-06-22 four separate folders — each a slice of the same goal — were merged into one umbrella so a future session has one place to look. The academy wants to run nationally-recognised SKM (Sijil Kemahiran Malaysia) programmes; to do that it must (1) hold the right NOSS standards, (2) produce JPK-format teaching materials, and (3) pass JPK's accreditation review.

---

## The chain: NOSS → Textbook / WIM → Accreditation

| Layer | What it is | Who writes it | In this project |
|-------|-----------|---------------|-----------------|
| **NOSS** | The government *standard* — what a Level-3 graduate must be able to do | JPK | The input; extracted into each subject's `00-noss-extract.md` |
| **Textbook** | Student-facing course content for IT-020 | 3U / Jay | Sub-effort B (`content/`, `NOSS-IT-020-Textbook/`) |
| **WIM** | The *mandatory* JPK teaching package (7 doc types × every CU, colour-coded) | Accredited centre | Sub-effort A (4 subject folders) |
| **Accreditation** | JPK accepts the centre + materials → centre may issue SKM | JPK reviews | Sub-effort C (application notes, WhatsApp) |

A key clarification Jay and Jennifer worked through (April 2026): **NOSS = the syllabus/standard; WIM = the courseware**. They are not the same document. WIM is built *from* NOSS.

---

## The 4 merged sub-efforts

| # | Sub-effort | Scope | Status |
|---|-----------|-------|--------|
| **A** | **WIM Generator** (`noss-to-wim`) | Automate WIM manufacturing across Tuinalogy, Aesthetic, BEV, IT — the largest, active effort | 3/4 content-complete; Tuinalogy active |
| **B** | **IT-020 Textbook** (`noss-it020-textbook` + dup `NOSS`) | L3/L4/L5 textbook content for NOSS IT-020 Computer System | Content generated (SPIRAL-built) |
| **C** | **Accreditation Application** (`Apply NOSS IT-020…`) | Business effort to get the IT-020 (ADI IT) programme accredited | In progress |
| **D** | **Reference & Raw** | JPK panduan, sample WIMs, Jennifer's approved IT-020 sample | Reference (benchmark) |

### Subject coverage (Sub-effort A)

| Subject | NOSS Code | Level | Status |
|---------|-----------|-------|--------|
| Tuinalogy 推拿疗法 | MP-031-3:2016 | 3 | Active — Chinese WIM + 27 CC-licensed images |
| Aesthetic Services | S960-002-3:2020 | 3 | Content complete |
| BEV Diagnostic & Rectification | G452-010-3:2023 | 3 | Content complete |
| IT Computer System | IT-020-3/4/5:2013 | 3,4,5 | Content complete (L3 primary) |

---

## Current focus & open threads

- **Jennifer's 2026-06-21 IT-020 sample** (`raw/folder-3-jennifer-it020-2026-06-21/`) — a JPK-*approved* WIM she asked Jay to validate as the format template. Verdict: conforms as a format reference, but uses the older 2013 `P/T/K` coding (vs current 2020 `KP/KT/KK`), is only the Teori-KP + Amali-KK slice (not the full 7-type package), and is IT-specific. Use for layout, not content.
- **WIM QA last mile** — every generated doc must pass the JPK format validators; Tuinalogy's bilingual content must match the English subjects' standard.
- **IT-020 accreditation application** — the business/submission track (Sub-effort C) is the path to actually running the programme.

---

## Merge provenance (2026-06-22)

Combined per Jay's instruction (flat merge, keep everything). Mechanics:

- All four source folders flat-merged into `3u-pioneer-academy-noss/`; **every file-path collision was preserved as a numbered backup** (`*.~1~`, ≈3,028 files) — nothing overwritten silently.
- `cp` stalled on a Windows **junction** inside `noss-to-wim` (`.git`/cache reparse points); finished with `robocopy /XJ`, which correctly skipped 304 junction reparse points (not real data).
- The three source `.git` repos were flat-merged into one **non-functional** `.git` — re-init if version control is needed.
- The 4 originals were **archived** (not deleted) to `4-archive/old-projects/noss-merge-originals-2026-06-22/`.

*Sources: merged `00-README.md`, `index.md`, `log.md`, `wiki/story.md`; Jennifer WhatsApp 2026-04 to 2026-06-21; merge session 2026-06-22.*
