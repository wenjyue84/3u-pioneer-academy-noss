---
name: wim-docx-build
description: Build a consolidated, WPS-Office-friendly DOCX from WIM markdown files for one or all NOSS subjects. Handles the full md → pandoc → python-docx pipeline including static TOC / LOF / LOT (no dynamic Word fields), bilingual (EN / 中文 / BM) cover with JPK government logo, and page breaks before every CU and every .md file. Triggered when the user asks to "build WIM DOCX", "consolidate into .docx", "export WIM", or "generate WIM textbook".
---

# WIM DOCX Build Skill

Builds the final publishable DOCX from the WIM markdown sources. Output is designed to **open ready-to-read in WPS Office, LibreOffice, and Microsoft Word without any field update** (no right-click → Update Field, no Ctrl+A → F9).

## When to use

Trigger when the user asks to:
- "Build the WIM DOCX"
- "Consolidate Tuinalogy / BEV / Aesthetic / IT into one .docx"
- "Export the WIM textbook"
- "Regenerate the WPS-friendly output"
- "Make a printable version of the WIM"

Do **not** trigger for single-file preview (use `build/wim_md_to_docx.py` directly for that). This skill is for the consolidated pipeline only.

## Prerequisites

- `pandoc` on PATH
- `uv` for Python invocation (per project CLAUDE.md rule)
- JPK envelope already applied to every `.md` — if not, run `wim-jpk-format` first
- (optional) `rsvg-convert` on PATH for SVG image embedding; without it pandoc warns + drops SVGs

## Architecture

| Path | Role |
|------|------|
| `build/wim_consolidate_all.py` | Orchestrator: concatenate md → pandoc → post-process |
| `build/wim_md_to_docx.py` | Single-file converter (not used by this skill) |
| `build/_templates/reference-textbook.docx` | Pandoc reference template (typography + callout styles) |
| `build/_templates/build-reference-docx.py` | Deterministic template regenerator |
| `build/filters/callouts.lua` | Pandoc Lua filter for `::: {.note/.warning/.definition/.example/.pullquote}` blocks |
| `tuinalogy-services/_assets/logos/jpk-logo.png` | Government crest used on cover page |

## Pipeline stages (in order)

1. Concatenate every subject's CU `.md` files into one master markdown (image paths — both `![](md)` and `<img src="">` HTML — rewritten to absolute)
2. Pandoc → DOCX (with reference template + Lua callout filter, **no** `--toc`)
3. `insert_cover_page` — JPK logo + tri-lingual (EN / 中文 / BM) cover
4. `inject_envelope_logos` — **rebuilds the JPK envelope as a 2-column table** (logo left, address right) because pandoc collapses the source HTML envelope into one inline paragraph and drops the logo (see Gotchas §1)
5. `colorize_headings` — H1/H2/H3 coloured by doc type (KP/KT/KK/PM/KA/PA)
6. `apply_table_style` — banded rows, horizontal rules; skips JPK envelope tables
7. `promote_italic_captions` — reclassifies italic figure/table lines as Caption
8. `number_figure_captions` — literal `Figure 1.3  ·  图 1.3` numbering + bookmarks
9. `add_drop_caps` — initial-letter drop cap per subject opening paragraph
10. `build_static_toc` — hyperlinked TOC (no TOC field — static entries)
11. `insert_list_of_figures_tables` — static LOF + LOT tied to bookmarks
12. `add_page_breaks_per_document` — page break before each CU (H2) and each `.md` (H3)
13. `front_matter_roman_numerals` — Roman numerals for cover/TOC, Arabic thereafter
14. `add_running_header` — literal book title header (no STYLEREF)
15. `add_page_numbers` — `PAGE / NUMPAGES` footer (universally rendered)
16. `disable_even_odd_headers` — **strips `<w:evenAndOddHeaders/>` from settings.xml** so the single default footer renders on every page, not just odd ones (see Gotchas §2)
17. `set_margins` — 2.0 cm top/bottom, 2.2 cm left/right

## Usage

```bash
# Single subject
uv run --with python-docx python build/wim_consolidate_all.py \
  --subject tuina \
  --output build/WIM-Tuinalogy.docx

# All four subjects
uv run --with python-docx python build/wim_consolidate_all.py \
  --output build/WIM-Consolidated-All.docx
```

Subjects accepted: `tuina`, `aesthetic`, `bev`, `it`, `all`.

### Windows + Chinese text

Set `PYTHONIOENCODING=utf-8` before invoking so `print()` statements containing CJK don't crash in `cp1252` terminals:

```bash
PYTHONIOENCODING=utf-8 uv run --with python-docx python build/wim_consolidate_all.py --subject tuina --output build/WIM-Tuinalogy.docx
```

### File-locked error (Permission denied)

If the user has the target DOCX open in Word / WPS, pandoc returns `permission denied`. Write to a versioned filename instead (`WIM-Tuinalogy-v2.docx`, `-v3.docx`, …) — never overwrite a file you can't verify is closed.

## Verification

After build, run this one-shot check to confirm every house-style invariant landed:

```bash
PYTHONIOENCODING=utf-8 uv run --with python-docx python -c "
from docx import Document
import zipfile
p = 'build/WIM-Tuinalogy.docx'
d = Document(p)
xml = d.element.body.xml
z = zipfile.ZipFile(p)
settings = z.read('word/settings.xml').decode('utf-8')

print('--- Bilingual labels ---')
for n in ('书面教材','目录','插图目录','表格目录','技能发展局','合订本'):
    print(f'  {n!r:20s} -> {xml.count(n)}')

print('--- Page breaks ---')
print(f'  w:pageBreakBefore/  -> {xml.count(chr(60)+\"w:pageBreakBefore/\"+chr(62))}')

print('--- Drawings (cover logo + 1 per envelope + figure images) ---')
print(f'  w:drawing           -> {xml.count(chr(60)+\"w:drawing\"+chr(62))}')

print('--- Footer applies to every page (MUST be 0) ---')
print(f'  evenAndOddHeaders   -> {settings.count(\"evenAndOddHeaders\")}')

print('--- No dynamic fields (all MUST be 0) ---')
for n in ('SEQ Figure','SEQ Table','STYLEREF','<w:sdt>'):
    print(f'  {n!r:15s} -> {xml.count(n)}')
"
```

**Expected:**
- Bilingual labels: all > 0 (except `表格目录` which can be 0 if the subject has no tables)
- `w:pageBreakBefore/`: roughly `(H2 count − subjects) + (H3 count − CUs)` — e.g. Tuinalogy 1-subject / 7 CUs / 103 md files ≈ 102
- `w:drawing`: **`1 (cover) + N (.md envelopes) + figure images`**. For Tuinalogy this is `1 + 103 + figures ≈ 104+`. If you only see `1`, the envelope table rebuild broke — inspect `inject_envelope_logos`.
- `evenAndOddHeaders`: must be **0** after post-processing. If `1`, even pages lose their page number — inspect `disable_even_odd_headers`.
- Dynamic fields (`SEQ`, `STYLEREF`, `w:sdt`): all 0. Non-zero ⇒ post-processor regressed; check `number_figure_captions`, `build_static_toc`, `insert_list_of_figures_tables`, `add_running_header`.

## Gotchas learned (must-know for future edits)

### §1. Pandoc drops the JPK logo and flattens the envelope table

**Symptom:** Every information sheet renders with only the Putrajaya address — no JPK crest beside it — even though the source `.md` has `<img src="../_assets/logos/jpk-logo.png">`.

**Two overlapping causes:**

1. **HTML image paths are not rewritten by markdown-only regex.** The resolver must rewrite BOTH:
   - markdown `![alt](path)`
   - HTML `<img src="path">` (used inside the JPK envelope table)

   Even with the path fixed, pandoc's docx writer **still drops `<img>` tags that live inside an HTML `<table>`** — they never become native Image nodes. So path rewriting alone is insufficient.

2. **Pandoc collapses the entire HTML envelope table into a single Body-Text paragraph.** The source `<table><tr><td>[logo]</td><td>[address lines]</td></tr></table>` arrives in the DOCX as one run-together paragraph: `"JABATAN PEMBANGUNAN KEMAHIRAN (JPK) TINGKAT 7-8, BLOK D4 …"`. There is no `w:tbl` to inject into.

**Fix (authoritative — must live in post-processing, not in the `.md` source):** `inject_envelope_logos()` detects each collapsed envelope paragraph by its `"JABATAN PEMBANGUNAN KEMAHIRAN (JPK) TINGKAT"` signature, splits the run-together address back into 4 lines (`_split_jpk_address()`), synthesizes a borderless 2-column `w:tbl` — logo (`Cm(3.2)` picture, 4 cm cell) on the left, bold first-line address + 3 plain lines on the right — and replaces the paragraph in place.

**Do not try to fix this by editing the `.md` sources or the `wim-jpk-format` skill** — the envelope format is correct at source; the loss happens in pandoc. Keep the rebuild in post-processing so the envelopes stay consistent regardless of `.md` authoring changes.

### §2. Even-page numbers disappear

**Symptom:** Page numbers show only on odd pages (1, 3, 5…); even pages (2, 4, 6…) are blank at the bottom.

**Cause:** `build/_templates/reference-textbook.docx` sets `<w:evenAndOddHeaders/>` in `word/settings.xml` (intended for a future mirror-margins book layout). This flag tells Word/WPS to use **separate** header/footer parts for odd and even pages. The consolidator only adds a `default` (odd) footer reference, so even pages look up a non-existent even-footer part and render blank.

**Fix:** `disable_even_odd_headers()` strips the `<w:evenAndOddHeaders/>` node from `doc.settings.element` and removes any per-section `w:footerReference w:type="even"` / `w:headerReference w:type="even"` nodes.

**Why not just fix the template?** The template is used for single-file previews too, where the book layout may one day come back. Strip at consolidation time rather than at template generation time.

### §3. Windows PowerShell + CJK print crash

**Symptom:** `UnicodeEncodeError: 'charmap' codec can't encode character '\u4e66'` when post-processor prints Chinese.

**Fix:** Always prefix the build with `PYTHONIOENCODING=utf-8`. Make it the first token of the command, before `uv run`.

### §4. `permission denied` when rebuilding

**Symptom:** `withBinaryFile: permission denied` mid-pandoc.

**Cause:** The target DOCX is open in Word or WPS Office. Windows locks it for writing.

**Fix:** Write to a versioned filename (`-v2.docx`, `-v3.docx`, …). Never assume you can overwrite the last build.

### §5. Source filename drift

**Symptom:** `FileNotFoundError: .../KP-01.md`.

**Cause:** Files are periodically renamed from bare codes (`KP-01.md`) to descriptive variants (`KP-01-consultation-area-reception.md`) by a content linter. The consolidator's `classify_doc()` handles both forms — but ad-hoc scripts that hard-code `KP-01.md` will break.

**Fix:** When scripting against a specific .md, glob for `KP-01*.md` rather than hard-coding the full name.

## Post-build guidance for the user

Tell the user:

> The DOCX opens ready to read in **WPS Office, LibreOffice, and Microsoft Word** — no right-click → Update Field needed. TOC entries are Ctrl+Click hyperlinks. Figure / Table numbers, the running header, and the cover logo are all baked in at build time.

## Changing the design

- **Typography / colour / callout styles** → edit `build/_templates/build-reference-docx.py`, re-run it, then rebuild.
- **Cover page text / logo size** → edit `insert_cover_page()` in `build/wim_consolidate_all.py`. The cover logo uses `LOGO_PATH` (`tuinalogy-services/_assets/logos/jpk-logo.png`).
- **Envelope layout (per-document logo + address)** → edit `inject_envelope_logos()` and `_split_jpk_address()`. Current layout: 4 cm logo cell on left, bold first line + 3 plain lines on right, borderless.
- **Page-break policy** → edit `add_page_breaks_per_document()`. Current rule: break before every H2 except first-in-subject, every H3 except first-in-CU.
- **Bilingual labels** → edit the `LBL_*` constants (`LBL_CONTENTS`, `LBL_LIST_FIGURES`, `LBL_LIST_TABLES`, `LBL_FIGURE_BI`, `LBL_TABLE_BI`, `LBL_BOOK_HEADER`) in `build/wim_consolidate_all.py`.
- **Page-number behaviour** → `add_page_numbers()` writes `PAGE / NUMPAGES`; `disable_even_odd_headers()` ensures the footer renders on every page. Do not remove the latter — see Gotchas §2.

## Known limitations

- SVG images need `rsvg-convert` on PATH — otherwise pandoc drops them with a warning (build still succeeds).
- The static TOC has **no page numbers** (would need a DOCX→PDF render pass). Internal hyperlinks substitute.
- Running header is subject-granular only (not per-CU) because nested sections render inconsistently in WPS.
- Drop caps + Roman-numeral front matter depend on the reference template's Heading 1 / Title styles existing — regenerate the template if they're missing.
