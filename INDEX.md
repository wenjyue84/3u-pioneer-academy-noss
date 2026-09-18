# INDEX — 3U Pioneer Academy NOSS / JPK Umbrella

> **Purpose:** Navigation hub for the combined 3U Pioneer Academy skills-accreditation project. Read this first. Designed for LLMs: read this instead of walking the 16k-file tree.
>
> **What this is:** On 2026-06-22 four separate NOSS-related folders were merged into this one umbrella project. They share one client (3U Pioneer Academy), one goal (JPK accreditation), and one contact (Jennifer). See [wiki/00-umbrella-overview.md](wiki/00-umbrella-overview.md) for the full picture and [log.md](log.md) for merge provenance.

**Client:** 3U Pioneer Academy Sdn Bhd · **Lead:** Jay (Lew Wen Jyue) · **Contact:** Jennifer +60 12-611 1677 · **WhatsApp:** 商学院ADI IT Program
**Last updated:** 2026-06-22

---

## The 4 Sub-Efforts (merged here)

| # | Sub-effort | What it does | Lives in | Source folder (now archived) |
|---|-----------|--------------|----------|------------------------------|
| A | **WIM Generator** | Generate JPK-format Written Instructional Materials across 4 subjects (the active, biggest effort) | `aesthetic-services/` `bev-diagnostic-rectification/` `it-computer-system/` `tuinalogy-services/` `build/` `validators/` | `noss-to-wim` |
| B | **IT-020 Textbook** | Generate L3/L4/L5 textbook content for NOSS IT-020 | `content/IT-020-3,4,5/` `NOSS-IT-020-Textbook/` `scripts/` `templates/` | `noss-it020-textbook` (+ near-dup `NOSS`) |
| C | **Accreditation Application** | Business effort to apply for JPK accreditation of the IT-020 (ADI IT) programme | `From-WhatsApp/` + root notes (`NotebookLM - ADI*`, `WhatsApp-Group-Reference-*`) | `Apply NOSS IT-020 Computer System Management` |
| D | **Reference & Raw imports** | JPK panduan, sample WIMs, Jennifer's 2026-06-21 IT-020 sample | `raw/folder-1-wim-panduan/` `raw/folder-2-sample-wim/` `raw/folder-3-jennifer-it020-2026-06-21/` `_reference/` | (across all four) |

> **Relationship:** NOSS (the government *standard*) → feeds both the **textbook** (B) and the **WIM** (A); WIM is the mandatory teaching material that, once accepted by JPK, unlocks the **accreditation** (C). D is the benchmark/reference material that grounds A and B.

---

## Wiki Reading Order (concept knowledge)

| # | File | Topic |
|---|------|-------|
| — | [wiki/00-umbrella-overview.md](wiki/00-umbrella-overview.md) | **Combined-project overview — start here** |
| — | [wiki/story.md](wiki/story.md) | Narrative entry point (the WIM manufacturing story) |
| 01 | [wiki/01-noss-overview.md](wiki/01-noss-overview.md) | What is NOSS (Malaysian occupational skills standard) |
| 02 | [wiki/02-wim-structure.md](wiki/02-wim-structure.md) | WIM document structure (7 doc types per CU) |
| 03 | [wiki/03-wim-coding-system.md](wiki/03-wim-coding-system.md) | WIM coding `[NOSS]-[CU]/[Doc]([Seq]/[Total])` + paper colours |
| 04 | [wiki/04-wim-development-process.md](wiki/04-wim-development-process.md) | Step-by-step WIM authoring workflow |
| 05 | [wiki/05-noss-to-wim-mapping.md](wiki/05-noss-to-wim-mapping.md) | Mapping CoCU items to KP/KT/KK |
| 06 | [wiki/06-whatsapp-context.md](wiki/06-whatsapp-context.md) | Stakeholder messages and context |
| 07 | [wiki/07-jpk-format-spec.md](wiki/07-jpk-format-spec.md) | JPK envelope spec — logo + identification table |

---

## Sub-effort A — WIM Generator (subjects)

| Subject | NOSS Code | Level | Folder | Status |
|---------|-----------|-------|--------|--------|
| **Tuinalogy** 推拿疗法 | MP-031-3:2016 | 3 | `tuinalogy-services/` | Active — images + Chinese WIM |
| **Aesthetic Services** | S960-002-3:2020 | 3 | `aesthetic-services/` | Content complete |
| **BEV Diagnostic & Rectification** | G452-010-3:2023 | 3 | `bev-diagnostic-rectification/` | Content complete |
| **IT Computer System** | IT-020-3/4/5:2013 | 3,4,5 | `it-computer-system/` | Content complete (L3 primary) |
| **Multimedia Interactive Design** 互动多媒体设计 | J582-001-3:2019 | 3 | `multimedia-interactive-design/` | In progress — WIM generating (COPTPA 2023) |
| **Creative Multimedia Development** 创意多媒体开发 | J582-001-4:2025 | 4 | `creative-multimedia-development/` | Stub — awaiting J582-001-4:2025 NOSS PDF |
| **AI-Powered Digital Marketing Specialist** | DM-001-3:2026 | 3 | `ai-digital-marketing/` | New — COPTPA course, KP/KK in progress |
| **Video / Film (Editing)** 视频剪辑 | IT-072-3:2012 | 3 | `video-film-editing/` | New 2026-09-18 — ADI Pekerjaan (MPC/JPK) document set 00–10, see its README |
| **Preschool Teaching** 学前教育 | P851-002-4:2025 | **4 (DKM)** | `preschool-teaching/` | New 2026-09-18 — ADI Pekerjaan set 00–12 + `output/` (30 bulan, subjective assessment, LPKC); Core Abilities L1–L4 Phase 2; see its README |

Each subject folder: `00-README.md`, `00-noss-extract.md` (CoCU source of truth), `01-jpw-distribution.md` (30/70 split), then `C01/`, `C02/`… (core CUs) and `E01/`… (electives). Each CU folder holds the 7 WIM doc types:

| File | Type | Paper | Purpose |
|------|------|-------|---------|
| `PM-teori.md` | Lesson Plan | Yellow | Theory class plan |
| `KP-XX.md` | Information Sheet | White | Knowledge topic (one per Related Knowledge item) |
| `KT-XX.md` | Assignment Sheet | Pink | Exercises mirroring each KP |
| `PM-amali.md` | Lesson Plan | Yellow | Practical class plan |
| `KK-XX.md` | Work Sheet | Blue | Step-by-step practical activity |
| `KA.md` | Knowledge Assessment | Pink | Written exam paper |
| `PA.md` | Performance Assessment | Light blue | Practical skill evaluation |

**Build outputs:** `build/WIM-Consolidated-All.docx` (8.4 MB, all 4 subjects), `build/WIM-Tuinalogy.docx` (7.8 MB, with images). **JPK skill:** `.claude/skills/wim-jpk-format/`.

**AI Digital Marketing proposal:** `proposal-ai-digital-marketing.pptx` (root folder) — course proposal presentation for the COPTPA accreditation application.

---

## Sub-effort B — IT-020 Textbook

| Path | Contents |
|------|----------|
| `content/IT-020-3/`, `IT-020-4/`, `IT-020-5/` | Generated textbook content per level |
| `content/images/` | Textbook figures |
| `NOSS-IT-020-Textbook/` | Per-level textbook source tree (IT-020-3/4/5) |
| `_reference/course-originals/`, `_reference/noss-framework/`, `_reference/kitchen-template/` | Reference material the textbook was built from |
| `scripts/agent_prompts/` | Generation prompts |
| `output/`, `logs/` | Build outputs and run logs |

> **Note:** Two near-identical source folders (`NOSS` and `noss-it020-textbook`) were merged; `noss-it020-textbook` was the superset. Colliding files were preserved as numbered backups (`*.~1~`) rather than overwritten — see "Merge artifacts" below.

---

## Sub-effort C — Accreditation Application (ADI IT Program)

| Path | Contents |
|------|----------|
| `From-WhatsApp/` | WhatsApp exports from the 商学院ADI IT Program group |
| `01 Main - Apply NOSS IT-020 Computer System Management.md` | Application working notes |
| `NotebookLM - ADI IT Program.md`, `NotebookLM - Adi training.md` | NotebookLM research notes |
| `WhatsApp-Group-Reference-商学院ADI-IT-Program.md` | Group reference |

---

## Sub-effort D — Reference & Raw imports

| Path | Contents |
|------|----------|
| `raw/folder-1-wim-panduan/` | JPK **Buku Panduan WIM** samples (from Jennifer's Drive) |
| `raw/folder-2-sample-wim/` | Sample JPK-format WIM PDFs (benchmark) |
| `raw/folder-3-jennifer-it020-2026-06-21/` | Jennifer's JPK-approved IT-020-3:2013 sample WIM (C01/C02/C07; Teori-KP + Amali-KK) |
| `raw/md/` | Markdown extractions of source PDFs |

---

## Tooling, Spiral & Merge artifacts

| Path | Purpose |
|------|---------|
| `_tools/`, `tools/`, `tests/`, `validators/` | Validators (CoCU coverage, pregnancy-safety, terminology), test suites |
| `.spiral/`, `prd.json`, `spiral.config.sh`, `progress.txt`, `10us.md` | SPIRAL autonomous-enhancement runtime + Chinese 10-story milestone digests |
| `.git/` | ⚠️ **Frankenstein** — 3 source repos' `.git` were flat-merged; **not a valid single repo.** Re-init if git is needed (`rm -rf .git && git init`). |
| `*.~1~`, `*.~2~`, `*.~3~` (≈3,028 files) | **Collision backups** from the flat merge — the losing copy of every same-path file. Safe to prune once the canonical versions are confirmed good. |
| `.venv/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `__pycache__/` | Regenerable caches/venv (carried over; not on the reading path) |

---

## Key External References

- **Buku Panduan WIM Edisi 2020:** https://anyflip.com/jpvdh/aagk/basic
- **MySPIKE:** https://www.myspike.my
- **Jennifer Drive 1** (WIM panduan): https://drive.google.com/drive/folders/1RqufqB60euIIm-pt_08S9v98rDLV8FCN → `raw/folder-1-wim-panduan/`
- **Jennifer Drive 2** (sample WIM): https://drive.google.com/drive/folders/1tu1dmkkI6H-pnX53qRQAWnzsgauTUc0f → `raw/folder-2-sample-wim/`
- **Jennifer Drive 3** (IT-020 approved sample, 2026-06-21): https://drive.google.com/drive/folders/14wjOaK1DujM2jCSHAoREcsqbL4qquyGr → `raw/folder-3-jennifer-it020-2026-06-21/`

## Source NOSS PDFs (outside project)

| Subject | Path |
|---------|------|
| BEV | `C:\Users\Jyue\Downloads\G452-010-3-2023 Battery Electric Vehicle (BEV) Diagnostic and Rectification.pdf` |
| Aesthetic | `C:\Users\Jyue\Downloads\S960-002-3-2020 AESTHETIC SERVICES.pdf` |
| Tuinalogy | NOSS MP-031-3:2016 → `tuinalogy-services/00-noss-extract.md` |
| IT | merged into this project (`content/`, `NOSS-IT-020-Textbook/`) |

---

*Originals archived 2026-06-22 to `4-archive/old-projects/noss-merge-originals-2026-06-22/` (fully recoverable).*
