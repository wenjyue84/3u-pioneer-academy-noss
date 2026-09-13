# LMS Fix Skill

Upload images and fix broken content references in the Frappe LMS for the NOSS-to-WIM project.

## When to use

Run this skill whenever you:
- Import new lessons into the LMS (to fix image paths and .md refs)
- Add new images to a subject's `_assets/` folder
- See broken images or confusing filename references in the LMS

## What it fixes

1. **Broken images** — Uploads all images from `tuinalogy-services/_assets/` to Frappe (`/files/`), then rewrites lesson body `(../_assets/category/image.jpg)` → `(/files/image.jpg)`
2. **Local .md file references** — Replaces references like `00-tuina-terminology.md` and `00-cocu.md` with human-readable labels (`Tuina Terminology Reference`, `NOSS CoCU Reference`)
3. **Cache** — Clears Frappe server cache so changes reflect immediately

## Run

Always run from the project root:

```bash
cd C:\Users\Jyue\Documents\1-projects\noss-to-wim

# Step 1: Upload images + fix image refs in lesson bodies
uv run scripts/lms_fix_images.py

# Step 2: Fix broken .md filename references
uv run scripts/lms_fix_md_refs.py

# Step 3: Clear Frappe cache
lms cache
```

Or run all three in sequence:

```bash
cd C:\Users\Jyue\Documents\1-projects\noss-to-wim && uv run scripts/lms_fix_images.py && uv run scripts/lms_fix_md_refs.py && lms cache
```

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/lms_fix_images.py` | Upload `_assets/` images → Frappe; patch lesson bodies |
| `scripts/lms_fix_md_refs.py` | Replace local `.md` refs with plain-text labels |
| `scripts/lms_link_quizzes.py` | Create interactive KA quiz lessons per chapter + wire quizzes |

All scripts are **idempotent** — safe to re-run. Already-fixed lessons are skipped automatically.

## Quiz setup (one-time per subject)

After importing a new subject, run the quiz linker to create interactive Knowledge Assessment lessons:

```bash
uv run scripts/lms_link_quizzes.py
```

Each chapter gets a `Knowledge Assessment` lesson with an embedded interactive quiz (MCQ, auto-scored). Student attempts and scores are tracked under **LMS → Quiz Submissions**.

## Scope

Both scripts operate **only on the active tuinalogy course** (`tuinalogy-services-level-3`) lessons. Orphaned lessons from old import runs are skipped.

## LMS URL

`http://100.88.116.94:8001` (also `http://localhost:8001` from this machine)

## Auth

Username: `Administrator` / Password: `admin` (configured inside each script)
