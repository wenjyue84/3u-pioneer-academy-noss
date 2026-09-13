# WIM Build Pipeline

Converts the subject markdown sources into DOCX output that reads like a
textbook (publisher-style headings, running headers, banded tables, numbered
figures, safety / definition callouts) while preserving the JPK envelope on
every WIM.

## Files

| Path | Role |
|------|------|
| `wim_md_to_docx.py` | Single-file converter (one `.md` → one `.docx`) |
| `wim_consolidate_all.py` | Bundler that emits one `.docx` per subject or all-in-one |
| `_templates/reference-textbook.docx` | Pandoc reference template — source of truth for typography, colours, table styles |
| `_templates/build-reference-docx.py` | Deterministic generator for the reference template — re-run if it is lost or needs a design change |
| `_templates/fonts/README.md` | Font identity & Windows fallbacks |
| `filters/callouts.lua` | Pandoc Lua filter mapping `::: {.note}` / `.warning` / `.definition` / `.example` to Word callout styles |

## Quick start

```powershell
# (re)generate the reference template after editing build-reference-docx.py
uv run --with python-docx python build/_templates/build-reference-docx.py

# one subject
uv run --with python-docx python build/wim_consolidate_all.py --subject tuina --output build/WIM-Tuinalogy.docx

# all 4 subjects
uv run --with python-docx python build/wim_consolidate_all.py --output build/WIM-Consolidated-All.docx

# single file (used for quick preview)
uv run --with python-docx python build/wim_md_to_docx.py tuinalogy-services/C01/KP-01-consultation-area-reception.md --style KP --output build/_preview.docx
```

After opening in Word, **right-click the TOC → Update Field → Entire table**
so page numbers populate. The SEQ fields that number figures and tables also
update on field-refresh (Ctrl+A → F9).

## Callout markdown syntax

```markdown
::: {.note}
**NOTE:** 孕妇禁用合谷 LI4、三阴交 SP6。
:::

::: {.warning}
**WARNING:** Isolate the HV battery before removing any orange connector.
:::

::: {.definition}
**DEFINITION:** *Tuina* (推拿) is a Chinese manual therapy that…
:::

::: {.example}
**EXAMPLE:** Resetting a BMS fault code on a Hyundai Kona EV…
:::
```

The Lua filter wraps each block in the matching Word paragraph style
(`Callout Note / Warning / Definition / Example`). If the block does not
already start with a bold label, the filter prepends one automatically.

## Typography

- Body: Source Serif 4 10.5 pt, justified, 1.3 line spacing, 5 mm first-line indent
- Headings: Source Sans 3, navy `#1F3864`, small-caps for H2
- CJK fallback: Source Han Serif SC (Windows fallback: Microsoft YaHei)
- Monospace: JetBrains Mono (fallback: Consolas)

Install the preferred fonts for the full identity (see `_templates/fonts/README.md`).
Without them Word silently substitutes — the document stays legible, just with
a different personality.

## Post-processing (consolidator)

The consolidator runs Pandoc, then applies post-processing via `python-docx`:

1. Insert cover page
2. Re-colour H1/H2/H3 based on CU doc type (KP/KT/KK/PM/KA/PA colour map)
3. **Re-style tables** → horizontal rules only, repeating header row, banded rows. Skips the JPK envelope table (detected by matching the logo path or the Putrajaya address).
4. **Number figure / table captions** with Word SEQ fields scoped to Heading 1 (`\s 1`). Counter resets at every subject H1.
5. **Running header** via STYLEREF pulling the current H1 + H2 into the top of every page.
6. Footer "Page X of Y"
7. Margins: top/bottom 2.0 cm, inner/outer 2.2 cm (template contributes mirror-margin intent; consolidator overrides to flat margins because the post-processed document is one long section)

## Known limitations

- SVG images in the markdown need `rsvg-convert` in PATH; otherwise Pandoc drops the image with a warning (does not fail the build).
- Mirror margins are authored in the reference template but flattened by `set_margins()` during post-processing. If you want recto/verso binding, delete the `set_margins()` call in `wim_consolidate_all.py`.
- Drop caps, pull quotes, and front-matter Roman numerals are **not** implemented (Phase C of the styling plan — deferred).
- The single-file converter still inserts its legacy 3-column "NOSS / CU / Kod" box in addition to the JPK envelope; this duplicates data now present in the envelope. Safe to remove in a follow-up if desired.
