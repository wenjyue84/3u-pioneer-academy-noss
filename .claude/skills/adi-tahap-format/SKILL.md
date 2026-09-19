---
name: adi-tahap-format
description: Verify that a Penilaian Pengetahuan file's question FORMAT (MCQ vs Struktur+Esei) matches what its own Tahap requires, per the ADI Pekerjaan rule (Tahap 3 = MCQ, Tahap 4/5 DKM = Subjektif). Use for video-film-editing and preschool-teaching only — not confirmed as a general JPK rule for other NOSS subjects in this repo.
---

# ADI Pekerjaan Tahap -> question format

## The rule (verified sources, quoted verbatim)

From `preschool-teaching/07-soalan-penilaian-pengetahuan/00-format-subjektif-tahap4.md:3-6`:

> "Panduan ADI Pekerjaan 552025, Jadual 8 (p.22): DKM (Tahap 4) → bentuk Subjektif, 2 soalan
> setiap CU, 1 jam, markah lulus 60%, boleh ulang sehingga lulus."
> "Templat pegawai `3.2 Format Soalan PENILAIAN PENGETAHUAN.xlsx`, sheet `JSU STD THP 4-5
> (SUBJEKTIF)`: ... JUMLAH SOALAN KESELURUHAN = 1 struktur + 1 esei; TEMPOH 1 JAM."
> "Buku Panduan Pembangunan Soalan Edisi 2024 §5.5.6 (p.32) & Jadual 15: soalan struktur =
> 3–4 sub-soalan (a–d), aras kesukaran struktur mesti merangkumi keseluruhan aras (R, S, T);
> ... struktur + esei mesti merangkumi SEMUA WA; esei = aras Tinggi."

From `preschool-teaching/README.md:59` (Tahap 3 vs Tahap 4/DKM comparison row):

> "理论考卷 | 20 MCQ / 30 分钟 | 主观题 2 题（1 Struktur + 1 Esei）/ 1 小时，60% 及格 |
> Panduan ADI Jadual 8 (p.22); 3.2 模板末 sheet; Buku Panduan Soalan 2024 §5.5.6"

**Summary:**

| Tahap | Format | Soalan | Tempoh | Markah Lulus |
|---|---|---|---|---|
| 3 (SKM) | Objektif (MCQ) | 20 soalan, 4 pilihan | 30 minit | (per file) |
| 4/5 (DKM) | Subjektif | 2 soalan/CU: 1 Struktur (3–4 sub a–d, spans R/S/T) + 1 Esei (aras Tinggi) | 1 jam | 60% |

## Scope — do not over-apply

This rule is verified **only for the ADI Pekerjaan pathway**: `video-film-editing` (Tahap 3) and
`preschool-teaching` (Tahap 4, DKM). `wiki/07-jpk-format-spec.md` — the standard WIM/JPK envelope
spec used by the other subjects (Tuinalogy, Aesthetic, BEV, IT, AI-DM, multimedia) — has **no**
mention of MCQ/objektif/Struktur/Esei at all. Do **not** run this checker against those subjects,
and do not assume they follow the same Tahap→format split without checking `Panduan ADI Pekerjaan
552025.pdf` or the standard JPK WIM guideline directly first.

## Workflow

Run after writing or editing any `07-soalan-penilaian-pengetahuan/*.md` file in video-film-editing
or preschool-teaching:

```bash
uv run .claude/skills/adi-tahap-format/scripts/check_tahap_format.py video-film-editing/07-soalan-penilaian-pengetahuan
uv run .claude/skills/adi-tahap-format/scripts/check_tahap_format.py preschool-teaching/07-soalan-penilaian-pengetahuan
```

- `ERROR` = the file's body/header format contradicts what its own Tahap requires (wrong format
  entirely, missing required section, wrong pilihan count, esei not aras Tinggi) — must fix.
- `WARN` = a softer deviation from Jadual 8 / §5.5.6 (duration, pass mark, sub-question count,
  aras spread) — read and use judgement; a WARN is not automatically wrong if the file has a
  documented, deliberate reason to differ.

This checker validates FORMAT ONLY (which type of paper, and its structural shape). It does not
check MCQ writing-style rules (punctuation, italics, distractor homogeneity) — use
`.claude/skills/soalan-format` for that, on the MCQ (Tahap 3) files.

## Known limits

- Tahap is read from the file's own `| TAHAP | ... |` row, falling back to the NOSS code suffix
  (`...-4:2025-...` → Tahap 4). A file with neither is reported `tahap_unknown` and skipped.
- The esei/struktur aras checks rely on the `· Aras · Konstruk` tagging convention already used in
  this project's files (e.g. `— WA4 · Tinggi · Prosedur`); a file that omits these tags will not be
  checked for R/S/T spread.
