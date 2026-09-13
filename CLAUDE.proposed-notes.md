# CLAUDE.md Rewrite Rationale

## Best-practice sources used

1. **Anthropic official docs** (https://code.claude.com/docs/en/best-practices) — primary authority.
   Key rules applied: keep it concise; ask "would removing this cause a mistake?" for every line;
   bloated files cause Claude to ignore rules; `CLAUDE.md` loaded every session so only put things
   that apply broadly; volatile info belongs in a separate file referenced by path, not duplicated.

2. **Anthropic blog** (https://claude.com/blog/using-claude-md-files) — applied: reference
   external docs by path rather than duplicating them; iterate from actual friction, not
   theoretically complete upfront.

3. **redreamality.com deep-dive** (https://redreamality.com/blog/claude-md-agents-md-deep-dive/) —
   applied: "~150–200 instructions" is the reliable compliance ceiling; stable rules vs volatile
   status must be in separate files with independent lifecycles; imperative voice with MUST/NEVER;
   progressive disclosure via file paths; versioned status in dated-update files like `now.md`.

---

## What was cut and why

| Cut | Reason |
|-----|--------|
| "Agent Onboarding (read in order)" numbered list | Redundant — rule "read INDEX.md first" captures it in one line |
| "4 subjects" project description prose | Volatile and already stale; INDEX.md is the maintained single source |
| Full Key Paths table (12 rows) | 4 of 12 were broken or stale (see below); moved to indexed subject table which doubles as a path guide |
| `noss-to-wim\` as "Project root" | BROKEN — the path does not exist; actual root is the repo itself |
| IT source `noss-it020-textbook\` path | BROKEN — folder does not exist at that path; merged into this project |
| BEV and Aesthetic PDF paths in `Downloads\` | BROKEN — neither PDF found on disk; removed from stable CLAUDE.md, paths survive in `00-README.md` which is where they were used |
| "Reference Documents" section (4 URLs) | Moved to brief one-liner references; URLs still present but without prose. The `07-jpk-format-spec.md` URL was already correct — kept as inline spec ref. |
| "WIM Structure per CU" table | Fully covered in INDEX.md and wiki/02-wim-structure.md; duplicating it in CLAUDE.md wastes context on every session |
| "Use professional, government-standard language" rule | Self-evident; the official best-practice source says to cut "self-evident practices like write clean code" |
| "Include bilingual terms where appropriate" (generic) | Replaced with specific per-subject language rules that actually change agent behaviour |

---

## What was added and why

| Added | Source / Reason |
|-------|----------------|
| `wiki/now.md` pointer in the first section | Anthropic docs: volatile status (deadlines, focus) must not be in CLAUDE.md; point to where it lives instead |
| `ai-digital-marketing/` in the subject table | The workstream was entirely missing from CLAUDE.md despite being the most active in July 2026 |
| `multimedia-interactive-design/` and `creative-multimedia-development/` | Also missing; listed in INDEX.md but never in CLAUDE.md |
| `proposals/` workstream section | Entirely missing from CLAUDE.md; proposals/ folder exists on disk with 4 files |
| Dynamic subject-key note for JPK script | `enhance_wim_jpk.py` argparse now loads keys from `subjects.json`; the old hardcoded usage was misleading |
| Explicit "NEVER add content the NOSS CoCU does not support" framing | Changed from descriptive ("Do NOT add content…") to imperative NEVER per best-practice voice guidance |

---

## Broken paths found in current CLAUDE.md

| CLAUDE.md claim | Actual status | Correct value |
|-----------------|--------------|---------------|
| Project root `C:\...\noss-to-wim\` | Does NOT exist | The project root is the repo itself (`3u-pioneer-academy-noss/`) — a path table entry for "project root" is redundant |
| IT source `C:\...\noss-it020-textbook\` | Does NOT exist | Content merged into this repo under `content/`, `NOSS-IT-020-Textbook/`, `it-computer-system/` |
| BEV source PDF `Downloads\G452-010-3-2023…pdf` | File not on disk | Unknown — not found; remove from CLAUDE.md, keep in 00-README.md for reference |
| Aesthetic source PDF `Downloads\S960-002-3-2020…pdf` | File not on disk | Unknown — not found; same treatment |

---

## Line count

- Before: 94 lines
- After: 90 lines
- Deleted: ~35 lines of stale/redundant content
- Added: ~31 lines covering 3 missing workstreams + correcting paths

The net count is similar, but the information density is higher: every line removed was either
wrong, redundant with INDEX.md, or self-evident; every line added changes what an agent would do.

---

## Items left for Jay to decide

1. **Build commands verified as existing** (`build/wim_md_to_docx.py` and `build/wim_consolidate_all.py`
   both exist on disk). However, the `build/` directory is not in the Glob search path from git —
   Jay should confirm these scripts are tested and working before treating the build section as canonical.

2. **BEV and Aesthetic source PDFs** are not in Downloads. If they were moved or renamed, the
   correct paths should be added back. If they were never needed (content already extracted into
   `00-noss-extract.md`), no action needed.

3. **`multimedia-interactive-design/` and `creative-multimedia-development/`** appear in the
   subject table but CLAUDE.md currently says nothing about their NOSS codes or language. Added
   from INDEX.md — Jay should confirm J582-001-3:2019 and J582-001-4:2025 are correct, and
   whether `creative-multimedia-development/` is truly a stub or has work in progress.

4. **`proposals/` git tracking.** The git status at conversation start shows `proposals/` is
   untracked. Whether to git-add it is Jay's call; CLAUDE.md does not address git strategy.

5. The `wiki/story.md` file exists and is mentioned in `wiki/now.md` but is not referenced in
   the proposed CLAUDE.md — it is narrative context, not agent instruction, so it was left out.
   If Jay wants agents to read it before generating WIM content, add a pointer.
