---
name: soalan-format
description: Enforce JPK "Contoh Format Penulisan Soalan" (MCQ writing rules) on every question file in this project — punctuation, capitalisation, italics for non-Malay terms, four-choice count, distractor homogeneity. Use whenever writing NEW MCQ soalan (07-soalan-penilaian-pengetahuan, Soalan-CAxx) or refining existing ones. Run the checker script before declaring any question file done.
---

# Soalan Format — JPK MCQ writing rules

Source of truth: `raw/soalan-format/contoh-format-penulisan-soalan.jpeg` (official JPK slide,
"CONTOH FORMAT PENULISAN SOALAN"). Ten rules, all binding for every MCQ file in this repo
(`**/07-soalan-penilaian-pengetahuan/*.md`, `**/Soalan-CA*.md`, and any other 4-choice objective
question file).

## The ten rules

1. **Question mark** — `?` at the end of a question stem, hard against the last word (no space:
   `...ini?` not `...ini ?`).
2. **Italics for non-Malay words** — any English/loan technical term inside Malay text (stem or
   option) must be wrapped `*like this*`.
3. **Trailing full stop on every option**, EXCEPT when the option is purely numeric, a bare common
   noun, or a bare proper noun (single word/name with nothing else).
4. **Every option starts with a capital letter.**
5. **A/B/C/D and I/II/III/IV must be uppercase.**
6. **Exactly four options** (A–D) — never three, never five.
7. **Image/diagram-stimulus questions must contain the word "Berdasarkan"** ("Berdasarkan rajah
   di atas...", "Berdasarkan gambar...").
8. **Options must be structurally homogeneous** — same grammatical shape/register, not a mix of a
   full sentence and a single word.
9. **Options ordered short → long / small → large.**
10. **Distractors must be homogeneous with the correct answer** — same category/unit (don't mix a
    time distractor with three technique distractors).

## Workflow

1. **Before writing new questions**, read this file and the source image once.
2. **Write questions** following the ten rules directly — don't rely on the checker to catch
   everything; rules 2, 7, 8, 9, 10 are semantic and the script only flags them as WARN heuristics.
3. **Run the checker** on the file(s) you touched:
   ```bash
   uv run .claude/skills/soalan-format/scripts/check_format.py <path-to-file-or-dir>
   ```
   - `ERROR` = objectively violates rules 1/3/4/5/6 — must fix before moving on.
   - `WARN` = heuristic hit on rules 2/7/8/9/10 — read the flagged line and use judgement; not
     every WARN is a real violation (the EN_TERMS wordlist in the script is not exhaustive and the
     length-based homogeneity check is a rough proxy).
4. **Never declare a question set "done" without a clean (or judged-clean) checker run** — paste
   the command output, not just "looks fine".
5. When a new recurring English/loan term shows up un-italicised across a subject (e.g. a
   subject-specific piece of jargon the wordlist doesn't know), add it to `EN_TERMS` in
   `scripts/check_format.py` rather than fixing it ad hoc every time.

## Known limits (don't over-trust the script)

- Rule 2 (italics) is a wordlist match — it will miss terms not in `EN_TERMS` and can false-positive
  on a Malay word that happens to contain an English substring. Skim the WARNs, don't blind-fix them.
- Rules 8–10 (homogeneity, ordering) are approximated by option string length only. A genuine
  semantic mismatch (e.g. three procedural steps + one attitude statement) will not be caught —
  read the four options yourself.
- The script does not touch subjective/structured question formats (e.g. preschool-teaching's
  Tahap 4 Struktur/Esei paper) — those aren't 4-choice MCQ and rules 3/4/5/6/9/10 don't apply to
  them. Rules 1 (question mark) and 2 (italics) still apply to any question stem regardless of type.
