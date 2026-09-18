# SPEC — preschool-teaching/output (P851-002-4:2025, Tahap 4/DKM)

Mirrors `video-film-editing/output/00-SPEC.md` rules: fill original officer templates
(`raw/adi-mpc-template-2026-09/`) with content sourced only from this subject's `.md` files,
never fabricate, `⟪TBD: …⟫` → `[TBD: …]`. Driver: `_tools/build_output.py`, config-driven via the
`SUBJECTS` dict (`--subject video-film-editing` for the IT-072 regression fixture, `--subject
preschool-teaching` for P851). Verify by reading each saved file back (each subcommand prints a
read-back).

## Built and run this pass

| Subcommand | Template | Source md | Output | Status |
|---|---|---|---|---|
| `rangka` | `4-pelaksanaan-kompilasi/3.3a Template Rangka Nota Pembelajaran (BM).docx` | `04-rangka-nota-pembelajaran/Cxx-rangka.md` (5) | `output/04 3.3a .../3.3a-0n Rangka Nota Pembelajaran Cxx <TITLE> (P851).docx` | **Done** — 5 files, 21 WA total |
| `nota` | `4-pelaksanaan-kompilasi/3.3b Template Nota Pembelajaran.docx` | `05-nota-pembelajaran/Cxx-Wnn.md` (21) | `output/05 3.3b .../CU C01-C05/3.3b-nn Nota Pembelajaran Cxx-Wnn <WA> (P851).docx` | **Done** — 21 files |
| `index` | — | walks `output/` | `output/INDEX-fail-pegawai.md` | **Done** — auto-generated, counts `[TBD:` occurrences per docx |
| `lpkc` | `4-pelaksanaan-kompilasi/1.2 LPKC.docx` (PPL-ADI scoring form) + fresh docx from `12-lpkc-template-outline.md` | `12-lpkc.md`, `12-lpkc-template-outline.md` | `output/10b 1.2 LPKC (DKM sahaja)/1.2 Borang Penilaian LPKC_JPK_ADI_04-2024 (P851).docx` + `.../Rangka Penulisan LPKC (P851).docx` | **Done** — header fields (KOD NOSS, TAJUK NOSS) filled on the scoring form; candidate name/no. pendaftaran/tajuk projek left as `[TBD: ...]` (not yet known); Rangka Penulisan LPKC built fresh per Jadual 10 format (Arial 12pt, 1.5 spacing, margins Atas/Bawah/Kanan 2.5cm, Kiri 4.0cm, page number bottom-right) |

**JAM PENGETAHUAN methodology:** equal-split 168 j/CU x NOSS WA weightage (per `00-noss-extract.md`
§10/§18 Competency Weightage, cross-verified against `02-borang-matriks-lampiran-5.md` 'Senarai CU
& WA' table — both agree). PROSES KERJA BERKAITAN is derived from the same matrix's ✓ marks
(`02-borang-matriks-lampiran-5.md` 'Matriks NOSS vs Proses Kerja'), cross-checked against
`01-proses-kerja.md` '## Ringkasan pemetaan'. Both are computed at generation time in
`build_wa_derivation_table()` (`build_output.py`) — never written back into the source `Cxx-Wnn.md`
files — and rendered as a "PROSES KERJA BERKAITAN:" / "JAM PENGETAHUAN:" block right after the
official header table in each generated nota docx (the officer's `3.3b Template Nota
Pembelajaran.docx` header table itself has no cells for these two fields). Full derived table:
`_tools/derived-wa-hours.md` (21 WA rows, audit trail).

CU titles used (from `00-noss-extract.md` §6): C01 Conduct Daily Routine Activities · C02 Perform
Preschool Teaching And Learning Activities · C03 Organise Preschool Classroom Environment · C04
Develop Pupil's Assessment · C05 Handle Parental-Community Activities.

`rangka` source-parsing note: unlike IT-072 (rangka derived from each WA's `III. PENERANGAN` Bab
headings in the nota md), P851's `Cxx-rangka.md` files already aggregate Bab/sub-topik per WA in
one file (`## WAn — <title> (<code>)` + numbered Bab list) — `build_output.py` has two parse modes
(`rangka_src_mode: "aggregate_md"` for P851, `"from_nota"` for IT-072) behind the same renderer.

## Not yet built (xlsx/pptx cell-layout reverse-engineering — flagged, not fabricated)

These require diffing each FINISHED IT-072 output against its BLANK template cell-by-cell
(openpyxl) before the same logic can be reproduced for P851 — that comparison pass (STEP 1.7 of the
task brief) was not completed this session. `build_output.py <cmd> --subject preschool-teaching`
prints `SKIPPED (not implemented this pass)` for every one of these rather than guessing cell
positions or fabricating numbers:

| Subcommand | Template | Source md | Known template quirk to solve |
|---|---|---|---|
| `lampiran5` | `1-panduan/lampiran-jpk/LAMPIRAN 5 …xlsx` (sheets *NOSS vs Proses Kerja*, *CU & WA*) | `01-proses-kerja.md`, `02-borang-matriks-lampiran-5.md` | 21 WA × P-column `/` marks — mechanical once cell map known |
| `jam42` | `2-fail-syarikat/4.2 Penjajaran Jam Latihan CA_CU_EU.xlsx` | `_progress.md` params: 30 bln / 4800 j total / 960 j CU / CA 120 j / 168 j × 5 CU | Template may **compute** CA from a level dropdown rather than take it as direct input — must find the input cell that forces CA=120 and document it here once found |
| `jadual43` | `2-fail-syarikat/4.3 Jadual Pengetahuan dan Proses Kerja.xlsx` | `03-jadual-latihan.md` §A/§B/§C | Template built for Tahap 3 has **72 week columns**; P851 needs **120** — must copy the last week column's style/width/merge pattern to extend to col 120 before filling |
| `jsu` | `4-pelaksanaan-kompilasi/3.2 Format Soalan PENILAIAN PENGETAHUAN.xlsx` | `07-soalan-penilaian-pengetahuan/Cxx.md` (format spec in `00-format-subjektif-tahap4.md`) | Use sheet ` JSU STD THP 4-5 (SUBJEKTIF)` (NOT the THP 1-3 sheets, which must stay untouched); 5 copies `JSU C01`…`JSU C05`; JUMLAH = 1 Struktur + 1 Esei, TEMPOH 1 jam |
| `soalan` | `4-pelaksanaan-kompilasi/3.4b Template Penilaian Pengetahuan.docx` | `07-soalan-penilaian-pengetahuan/Cxx.md` | Struktur 1 a–d + Esei 1 + SKEMA JAWAPAN on new page; PDF via `Export-Pdf.ps1` |
| `rekod31` | `4-pelaksanaan-kompilasi/3.1 Bukti Penilaian Pengetahuan.docx` | `09-penilaian-kekompetenan.md` + CA L4 inventory (`ca-l4-inventory` agent, in progress) | 5 CU rows (40 markah each) + 22 Core Ability rows |
| `bukti` | `4-pelaksanaan-kompilasi/4 Senarai Bukti Proses Kerja.xlsx` + `2 Borang Perakuan Pembimbing…docx` | `08-senarai-bukti-proses-kerja.md` | — |
| `lampiran6` | `1.1 Borang Laporan Penilaian Bukti Kekompetenan…docx` | `09-penilaian-kekompetenan.md` §A | 21 WA rows |
| `syarikat` | `2-fail-syarikat/*` | company name `⟪TBD: nama tadika/syarikat⟫` | — |
| `bakat` | `3-persediaan-kompilasi/*` | `10-susunan-fail-kompilasi.md` | — |
| `buku` | (compiled from `nota` outputs via docxcompose) | `output/05 .../*.docx` | Straightforward once `nota` is done (it is) — just not wired up this pass |

## Re-run commands

```bash
cd preschool-teaching/output/_tools
uv run --with python-docx --with openpyxl --with docxcompose python build_output.py rangka --subject preschool-teaching
uv run --with python-docx --with openpyxl --with docxcompose python build_output.py nota   --subject preschool-teaching
uv run --with python-docx --with openpyxl --with docxcompose python build_output.py lpkc   --subject preschool-teaching
uv run --with python-docx --with openpyxl --with docxcompose python build_output.py index  --subject preschool-teaching
# regression fixture (READ-ONLY check only — do NOT run against video-film-editing, it would overwrite committed output/)
```

`--subject video-film-editing` config exists in `build_output.py` for future regression testing but
was **not executed** this pass to honor "NEVER modify anything under `video-film-editing/`" — the
`nota`/`rangka` logic was ported line-for-line from the working `tmp_juno_regen/gen_nota.py` and
`gen_rangka.py` scripts that already produced the committed IT-072 output, so behavioural parity is
by construction, not by a fresh test run.
