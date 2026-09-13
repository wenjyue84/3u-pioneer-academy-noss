# `_engine/` — NOSS → PPA Assessment Engine

Graph-driven generator and validator for JPK **Penilaian Amali PPT-PPA** papers
(SOALAN + SKEMA + ANSWER SHEET + EQUIPMENT VERIFICATION).

Built 2026-08-25 in response to Jennifer's 2026-08-24 review. It exists because the
first generation round produced papers that were *plausible* but wrong in ways a
human reviewer had to catch by eye:

| Defect Jennifer found | Why it happened | What the engine does now |
|---|---|---|
| All 6 CU + E01 put into a 3-hour practical | The model picked CUs itself | `profile.cu_modes` is an **input**, never inferred |
| Office Admin: all 7 CU included | same | same |
| Mixed BM/EN in one sentence | No language contract | `V05_monolingual` fails the build |
| E01 declared but never scored | No coverage check | `V04_no_excluded_refs` + `V02/V03` coverage |
| Page-count declaration wrong | Written before render | `⟪PAGES⟫` backfill (build/ppa_integrate.py) |
| No JPK logo, no table borders | WIM textbook template reused | dedicated PPA renderer (round 2) |

## The graph

```
NOSS ──has──▶ CompetencyUnit (core | elective)
                   │
                   ├─has──▶ WorkActivity
                   │            └─has──▶ PerformanceCriterion
                   │
                   └─mode──▶ practical | oral | excluded      ← from the profile
Task      ──covers──▶ CompetencyUnit[]   ──consumes──▶ minutes
OralQuestion ──assesses──▶ CompetencyUnit
SkemaItem ──scores──▶ PerformanceCriterion  ──weight──▶ marks
```

Nothing about which CU to assess is a model decision. The profile states it; the
validator proves the document obeys it.

## Layout

| Path | What |
|---|---|
| `ppa/schema.py` | dataclasses + JSON (de)serialisation for the graph and profile |
| `ppa/validate.py` | V01–V09 validators; exit non-zero on any failure |
| `ppa/cli.py` | `graph`, `validate`, `plan` subcommands |
| `graph/<noss>.json` | one competency graph per NOSS — traceable to a `source_file` |
| `profiles/<noss>.json` | selection profile: CU modes, language, duration, sets, weights |
| `reports/` | validator output, one JSON + one markdown per run |

## Usage

```bash
# validate one paper against its profile + graph
uv run python -m _engine.ppa.cli validate \
    --profile _engine/profiles/fb-018-3.json \
    --paper output/jennifer-ppa-soalan/fb-018-3-set-a-soalan.md

# validate every paper that has a profile
uv run python -m _engine.ppa.cli validate --all

# print the assessment plan a profile implies (tasks, time budget, mark split)
uv run python -m _engine.ppa.cli plan --profile _engine/profiles/fb-018-3.json
```

## Rules that must survive every edit

- A CU marked `excluded` must not appear **anywhere** in the paper — not on the
  cover, not in the skema, not in an oral question.
- `language` is a contract. `bm` means Bahasa Malaysia only. Slash-joined
  bilingual phrases (`Tinjauan Pasaran / Market Survey`) are a validation failure,
  not a style preference.
- Practical duration must fit `duration_minutes.min..max` **including** setup and
  the oral session.
- Every `practical` CU needs at least one Task; every `oral` CU needs at least one
  oral question. Declared-but-unassessed is the exact defect that got the first
  round rejected.
