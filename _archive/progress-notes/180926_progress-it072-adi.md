# _progress.md — IT-072 Video/Film Editing ADI module build (started 2026-09-18 08:31)

Task: replicate the MPC/JPK ADI Pekerjaan folder (govt officer's Drive 1lzKA3Bg…) for NOSS IT-072-3:2012, sequentially numbered, with README. Output folder: `video-film-editing/`.

## Done
- raw downloads: `raw/adi-mpc-template-2026-09/` (34 files + `_md/` conversions + slide text) and `raw/it-072-video-editing/L3|L4|L5`
- `00-noss-extract.md` (noss-extract agent, 1112 lines, 1960 h total) — spot-checked OK
- `01-proses-kerja.md` (P01–P12, mine)
- `02-borang-matriks-lampiran-5.md/.xlsx` (script `scratchpad/build_matrix.py`)
- `06-jsu.md` (script `scratchpad/build_jsu.py`, distributions verbatim from JPK 3.2 xlsx)
- `08-senarai-bukti-proses-kerja.md` (mine, 39 bukti)

## In flight (agents)
- scout-sample (Z Sample Kompilasi structure) → feeds 09 + 10 + README
- scout-slides (186-slide text) → feeds 03 jadual rules
- nota-C01…E01 (6 × Sonnet) → `04-rangka-nota-pembelajaran/`, `05-nota-pembelajaran/` (31 WA)

## Next
- 03-jadual-latihan.md (+xlsx like 4.2/4.3) after scout-slides
- 07-soalan-penilaian-pengetahuan/<CU>.md — wave 2, per CU, after nota; follow 06-jsu labels
- 09-penilaian-kekompetenan.md (Lampiran 4/6 + company forms) after scout-sample
- 10-kompilasi-fail-susunan.md (Isi Kandungan / separators)
- README.md, LOG.md entry, INDEX.md + CLAUDE.md subject table row, wiki/now.md

## Facts that differ from CLAUDE.md
- pdftoppm not installed → PDF Read of image-only PDFs fails; use pypdf text layer (`scratchpad/pdftext.py`)
- Company (ADI applicant) unknown → ⟪TBD⟫ everywhere
