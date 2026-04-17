# LOG — noss-to-wim Project Activity Log

> **Concept:** Append-only narrative of what was done, when, and why — inspired by Andrej Karpathy's "LLM wiki" / dated-micro-essay approach. Each entry is a small self-contained chunk so any LLM reading the log can reconstruct context quickly. Newest entries at the top.
>
> **Rules:**
> - One entry per working session (or per meaningful milestone)
> - ISO dates (`YYYY-MM-DD`)
> - Lead with **what changed** then **why** then **what's next**
> - Keep entries scannable — bullets over prose
> - Do not edit old entries (append corrections as new entries)

---

## 2026-04-17 — Jennifer's reference WIMs archived; docs + log + index introduced

**What changed**
- Downloaded two Google Drive folders of sample WIMs (provided by Jennifer as reference): `raw/folder-1-wim-panduan/` and `raw/folder-2-sample-wim/`
- Created `INDEX.md` — directory manifest for fast LLM navigation
- Created `LOG.md` (this file) — append-only activity log, Karpathy-style
- Updated `CLAUDE.md` to list Tuinalogy as the 4th subject and to instruct agents to read INDEX.md first
- Built consolidated DOCX outputs:
  - `build/WIM-Consolidated-All.docx` (8.4 MB, all 4 subjects, 433 md files)
  - `build/WIM-Tuinalogy.docx` (7.8 MB, Tuinalogy only with embedded images)
- Consolidation script `build/wim_consolidate_all.py` written (cover page, TOC, page numbers, colour-coded headings by doc type)

**Why**
- Jennifer's reference PDFs are the "what a JPK-compliant WIM should look like" benchmark — storing them locally so offline comparisons are possible
- Project now has 4 subjects (was 3) — CLAUDE.md needed updating so new agents don't miss Tuinalogy
- Karpathy's dated-log concept: LLMs that land in the project benefit from a narrative of what-and-why rather than only state; INDEX gives the map, LOG gives the journey

**What's next**
- Finalize pending Spiral stories (3 remaining as of last check)
- Review Jennifer's reference WIMs — compare format against current output, iterate if gaps
- **Neutralise Spiral's commit-clobbering bug** — its git-stash / reset cycle has wiped uncommitted work three times today

---

## 2026-04-17 — Tuinalogy image enrichment committed

**What changed**
- 27 CC-licensed images downloaded from Wikimedia Commons + Wellcome Collection
- Categorised into `_assets/{meridians,acupoints,anatomy,techniques,clinical}`
- `_assets/ATTRIBUTION.md` created — full legal manifest (CC BY 4.0, CC BY-SA 4.0, PD)
- 19 of 22 Tuinalogy KP files now reference images (11 commits on master)
- Skipped: all 6 C05 KPs (administrative topics — records, HR, hygiene supervision, accounting, marketing, complaints have no good Wikimedia match)

**Why**
- Tuinalogy teaches anatomy, meridians, acupoints, tongue diagnosis — text-only was insufficient
- CC-licensed sources avoid copyright issues for government training material

**Operational note**
- Spiral autonomous runner kept resetting `master` to `05cafb3` during the session, wiping enrichment commits twice
- Root cause: a respawner outside the normal `NOSS-Textbook-Refresh` Task Scheduler entry (which is disabled) keeps starting `python.exe` + `claude-code` + `ralph`. Respawner not yet identified — **investigate before next Spiral restart**

---

## 2026-04-17 — Tuinalogy subject launched (4th subject)

**What changed**
- Created `tuinalogy-services/` folder tree (C01–C05, E01, E02 — 7 CUs)
- Extracted NOSS MP-031-3:2016 CoCU into `tuinalogy-services/00-noss-extract.md`
- Generated Chinese (简体中文) WIM documents across all CUs (PM-teori, KP, KT, PM-amali, KK, KA, PA)
- Set Spiral focus to Tuinalogy only — pivoted away from BEV/Aesthetic/IT

**Why**
- Jennifer added Tuinalogy as a new scope (推拿疗法 MP-031-3:2016)
- Required Simplified Chinese with bilingual EN/BM for clinical vocabulary — different style from first three subjects

**What's next**
- Add images (done — see above entry)
- Run Spiral for ~50 user stories of content enhancement

---

## 2026-04-16 — BEV / Aesthetic / IT content enhancement via Spiral

**What changed**
- Ran Spiral autonomous loop to enhance existing BEV / Aesthetic / IT content
- First 30 user stories completed (captured in `10us.md` milestones 10, 20, 30)
- Major gains:
  - BEV C03 Thermal System scenario-based Knowledge Assessment
  - Aesthetic C03 manual body massage anatomy deepening
  - Aesthetic C04 six electrotherapy modality safety notes
  - Bilingual (EN+BM) Aesthetic terminology glossary with consistency validator

**Why**
- Baseline NOSS→WIM conversion produced competent-but-thin content
- Spiral iteratively adds depth, humanises language, adds scenario-based assessments, validates CoCU coverage

---

## 2026-04-16 — Project scaffolding

**What changed**
- Created project root at `C:\Users\Jyue\Documents\1-projects\noss-to-wim\`
- Top-level reading guides (`00-README.md` → `06-whatsapp-context.md`)
- Three subject folders created: BEV, Aesthetic, IT
- `CLAUDE.md` written with agent instructions (WIM structure, coding format, rules)
- Spiral skill configured (`spiral.config.sh`) for autonomous enhancement

**Why**
- Convert 3 NOSS occupational skill standards into Malaysian JPK-format Written Instructional Materials
- Target: government-standard training material ready for instructors

---

## Template for new entries

```markdown
## YYYY-MM-DD — one-line headline

**What changed**
- bullet
- bullet

**Why**
- bullet

**What's next** (optional)
- bullet
```
