---
name: noss-ppa-generator
description: Generate and validate JPK Penilaian Amali PPT-PPA assessment papers (SOALAN, SKEMA, ANSWER SHEET, EQUIPMENT VERIFICATION) from a NOSS standard. Trigger when asked to create, fix, or check exam papers / soalan / skema / 考题 for a NOSS, when a new NOSS PDF arrives and papers are needed, or when Jennifer sends feedback on an existing paper.
---

# NOSS → PPT-PPA assessment paper generator

Jennifer, 2026-08-25 00:08:

> 我希望有一个方式可以记录我们这个 PPT-PPA 考题制作的方式，之后我们要创立考题，只需要上传
> NOSS，然后告诉它我们要选的 CU，他就自动帮我们做对的 soalan 和 Skema 出来，有这种可能吗

Yes. This is it. The engine lives in `_engine/`; this skill is the procedure for
driving it.

## Two ideas, both learned the hard way

**1. Which competency units get assessed is an input, never an inference.**

**2. The format benchmark is whichever file the *client* owns.**

Both of Jennifer's Drive folders hold files with near-identical names; only the
Drive `owner` field separates hers from ours. Ours cannot be their own benchmark.
Check it before treating any file as a reference — `gog drive ls` does not return
owner, so use the MCP:

```
mcp__claude_ai_Google_Drive__get_file_metadata { "fileId": "…" }   → "owner": "…"
```

On 2026-08-25 that check overturned a conclusion reached the same morning: her
papers are **Malay frame + English body**, not Malay throughout. Her complaint
"only one language" meant *no bilingual pair inside one sentence* — which her own
approved paper never has. See `_engine/FORMAT-jpk-ppa.md` §1.

It also found the CU selection had been in her file all along, **encoded as bold**
(C01, C04, C05 in `Arial-BoldMT`; the other three not). Text extraction drops
formatting, so the generator saw six identical units. A decision carried only by
visual formatting does not survive a pipeline — carry it as data.

**Confirmed 2026-08-25: bold on the cover *is* her exam CU selection.** So before
asking her anything, read the bold spans off any paper she owns — the answer may
already be in the file. `_engine/FORMAT-jpk-ppa.md` §3 has the extraction snippet.

**And check every source she has, not just the one you were handed.** The
FB-018-45 CU codes were reported as "unattested — the CoCU has a blank code
column" and a question went to the client. The codes were printed in that NOSS's
own `Training Hours Summary`, one folder away in the same Drive. Similarly, her
Drive holds the **full official NOSS PDFs** for N821, M731 and G471 (100, 112 and
70 pages) — far better than the CoCU extracts, and they confirmed all three
graphs' codes and titles verbatim. Enumerate her Drive by owner first:
`mcp__claude_ai_Google_Drive__search_files` with `owner = '<her address>'`.

The first generation round failed review because the model chose the units itself:
it put all six core units plus an elective into a three-hour practical, declared an
elective on the cover that nothing scored, and mixed two languages in one sentence.
None of that was a writing problem. It was a missing decision.

So the flow is: NOSS → graph (mechanical) → **worksheet → human decides** →
profile (machine-readable contract) → papers → validator proves the papers obey
the contract.

## Procedure

### 1. New NOSS arrives

Put the PDF under `raw/noss-character/`, extract text to
`raw/noss-character/txt/<key>.txt`, then transcribe the Competency Profile Chart
and CoCU tables into `_engine/graph/<key>.json`.

Transcribe; do not correct. Where the standard misnumbers, skips or contradicts
itself, reproduce what is printed and record it in `source_notes`. Across the six
NOSS transcribed so far, thirteen such defects were found — including N821, whose
section 6 calls C07 *Staff* Administration Supervision while its own CPC chart says
*Office* Administration Supervision. A transcription that quietly picks one stops
being evidence.

Verify it loads:

```bash
uv run python -c "from _engine.ppa.schema import NossGraph; g=NossGraph.load('_engine/graph/<key>.json'); print(g.noss_code, len(g.competency_units))"
```

### 2. Ask which units to assess

```bash
uv run python -m _engine.ppa.cli worksheet --graph _engine/graph/<key>.json
```

Send `_engine/worksheets/borang-pemilihan-cu-<key>.md` to the course owner. It
lists every unit with its work-activity and criterion counts — the honest proxy for
how much exam time a unit consumes — and states the capacity: a three-hour practical
holds roughly **two units assessed practically**, at ~48 minutes a station plus a
30-minute oral session and 10 minutes for handover.

That number is the answer to "why can't we just include all seven CUs". It is not
that the model is lazy; the clock does not fit.

**Do not proceed without the completed sheet.** Guessing here is precisely the
failure being engineered out.

### 3. Write the profile

Transcribe the completed worksheet into `_engine/profiles/<key>.json`. See
`_engine/profiles/fb-018-3.json` for a worked example. Every unit in the graph must
be given a mode: `practical`, `oral` or `excluded`.

`excluded` means **absent**, not "listed but unassessed". An elective printed on the
cover with no questions behind it is the defect that got the reference sample
flagged.

Record *why* in `notes`, with the date and the person who decided. A profile whose
provenance is lost gets re-litigated.

### 4. Write the spec, then the papers

Write `_engine/SPEC-<key>-set-<x>.md` — the prose form of the profile, aimed at
whoever writes the paper. `_engine/SPEC-fb-018-3-set-b.md` is the model.

Then generate the four documents into `output/jennifer-ppa-soalan/`:

| File | What |
|---|---|
| `<key>-set-<x>-soalan.md` | the question paper |
| `<key>-set-<x>-skema.md` | the marking scheme |
| `<key>-set-<x>-answer-sheet.md` | candidate answer sheet |
| `<key>-set-<x>-equipment-verification.md` | equipment verification |

Hard rules, all of them enforced by the validator:

- **One language.** `language: bm` means Bahasa Malaysia throughout. No
  `Melayu / English` slash pairs, no bracketed glosses. NOSS codes, official
  English unit titles on the cover block, and established abbreviations (KPI, FAQ,
  PPL-PPT) are the only exceptions.
- **Page count is a placeholder.** Write `⟪PAGES⟫`; step 6 backfills the real
  number. Both of the client's own reference papers declared the wrong count.
- **Marks add up.** Section criterion weights sum to the section heading; section
  totals equal the sum of criterion maxima; the paper totals 100%.
- **Set A and Set B are parallel forms.** Same units, same time budget, same mark
  split — different scenario.
- **Avoid a scenario industry that has its own NOSS.** Vehicle sales is not a valid
  scenario for a general sales NOSS; there is a separate standard for it.

### 5. Validate

```bash
uv run python -m _engine.ppa.cli validate --profile _engine/profiles/<key>.json
```

Zero errors before anything is sent. `V08 warn` about a hardcoded page count is
expected until step 6 runs.

Triage a paper that has no profile yet — language, marks and page declaration only:

```bash
uv run python -m _engine.ppa.cli lint
```

### 6. Render

```bash
# soalan, skema, answer sheet — default 10pt tables, 2.5 cm margins
uv run --with pywin32 --with python-docx python -m _engine.render.integrate \
    output/jennifer-ppa-soalan/<key>-set-<x>-{soalan,skema,answer-sheet}.md

# the JPK equipment form is one page by design and needs the tighter settings
uv run --with pywin32 --with python-docx python -m _engine.render.integrate \
    output/jennifer-ppa-soalan/<key>-set-<x>-equipment-verification.md \
    --table-font-pt 9 --margin-cm 1.8
```

Authoring tokens the renderer resolves (`_engine/FORMAT-jpk-ppa.md` §2):
`⟪LOGO⟫` → the Jata Negara crest inside that table cell · `⏎` → a real Word line
break (never `<br>`; pandoc drops it silently and welds words together) ·
`⟪SPAN⟫` → merge that row across all columns and centre it · `⟪PAGES⟫` → the real
printed page count, backfilled here.

Renders the docx, counts real pages, backfills `⟪PAGES⟫`, re-renders until the count
is stable, exports the PDF and verifies the PDF was written this run.

Then re-run `validate`: the declared page count must equal the PDF's page count.

**Never render with `build/wim_md_to_docx.py`.** That is the WIM textbook pipeline;
its template sets Source Serif 4 and full justification, which on a Mac substitutes
to a typewriter face with ragged word gaps, and it leaves tables unruled. That
combination is what got the first round rejected on sight.

### 7. Look at it

Render two pages to PNG and actually look:

```bash
uv run --with pymupdf python -c "
import pymupdf; d=pymupdf.open('output/jennifer-ppa-soalan/pdf/<name>.pdf')
[d[i].get_pixmap(dpi=120).save(f'/tmp/p{i}.png') for i in (0,3)]"
```

Two defects in the last round were invisible to every validator and obvious to the
eye: a competency-unit list collapsed into one run-on paragraph, and a candidate's
`NAMA CALON` field shaded as if it were a column heading. Validators check what
they were told to check.

## Validators

| | Checks |
|---|---|
| V01 | every unit in the graph has a mode in the profile |
| V02 | every `practical` unit appears in the TUGASAN section |
| V03 | every `oral` unit has a question; count matches the profile |
| V04 | no `excluded` unit appears anywhere — cover included |
| V05 | one language only |
| V06 | the cover's unit list equals the assessed set, exactly |
| V07 | declared TEMPOH sits inside the profile window, in JAM |
| V08 | page declaration is a real number, not `⟪PAGES⟫` |
| V09 | practical + oral weights total 100% |
| V10 | section weights, section totals and the paper total all reconcile |
| V11 | the six Malay section headings are present and in order |
| V12 | the reference code exists and its SET letter matches the filename |
| V13 | the SKEMA carries the examiner-only, AMARAN and marking-scale blocks |
| V14 | forbidden strings (`VIZTECH`, `Terlibut`, `DOCUMEN`) appear nowhere |
| V15 | summary tables reconcile with the raw data the candidate is handed |

Each exists because something got past a human review:

- **V10** — a writer reported "totals reconcile" over a table showing 54%; the
  paper totalled 94%, so no candidate could score full marks.
- **V12** — a re-lettered Set B kept `/A/` in its reference code.
- **V15** — the Set B paper's "verified summary" claimed 7 respondents preferred
  an air-conditioner, 10 were married with children and 15 intended to buy; the
  twenty raw rows said 6, 11 and 16. The answer sheet followed the summary and the
  skema followed the answer sheet, so the chain was internally consistent
  *everywhere except against the table the candidate actually analyses*. A
  candidate who counted correctly would have been marked wrong.

**Do not accept a writer's arithmetic — including your own.** And when you add a
validator, prove it fires: re-introduce the defect on a copy and check it reports.
A validator that passes because it never triggers is worse than none, because it
buys false confidence.

## Files

| Path | What |
|---|---|
| `_engine/README.md` | design rationale, defect-to-control mapping |
| `_engine/ppa/schema.py` | graph and profile dataclasses |
| `_engine/ppa/validate.py` | V01–V10 |
| `_engine/ppa/worksheet.py` | the CU-selection form generator |
| `_engine/ppa/cli.py` | `validate` · `plan` · `lint` · `worksheet` |
| `_engine/render/ppa_docx.py` | JPK docx renderer — logo, ruled tables, Arial |
| `_engine/render/integrate.py` | render → count → backfill → PDF |
| `_engine/graph/*.json` | one competency graph per NOSS |
| `_engine/profiles/*.json` | one selection profile per NOSS |
| `_engine/worksheets/*.md` | blank CU-selection forms |

## Graphs already transcribed

| NOSS | Level | CU | WA | PC | Note |
|---|---|---|---|---|---|
| FB-018-3:2012 Sales & Marketing Operation | 3 | 7 | 36 | 124 | profile complete |
| FB-018-4:2012 Sales & Marketing Administration | 4 | 8 | 41 | 127 | awaiting CU selection |
| FB-018-5 Sales & Marketing Management | 5 | 8 | 49 | 130 | awaiting CU selection |
| G471-001-3:2018 Retail Outlet Operations | 3 | 5 | 30 | 159 | no elective units exist |
| M731-001-3:2021 Digital Marketing Operation | 3 | 6 | 25 | 95 | no elective units exist |
| N821-001-3:2020 Office Administration | 3 | 7 | 36 | 115 | awaiting CU selection |
