# 13 — Urutan top-down: dari Jadual → bahan pembelajaran akhir (IT-072-3:2012, ADI Pekerjaan)

**Kaedah (Jay, 2026-09-18):** mula dari perancangan jadual pegawai, kemudian turun langkah demi langkah sampai bahan akhir (Nota/Kertas Penerangan, Soalan, bukti kerja). Setiap langkah di bawah menunjuk kepada **fail dalam format rujukan pegawai** yang boleh dimuat turun terus dari GitHub (`video-film-editing/output/`). Urutan ini ikut agenda Bengkel MPC 17–19 Sep 2026 (Topik 4 Matrik → Topik 5 Jadual → Topik 6 Bahan Pembelajaran → Topik 7/8 JSU & Soalan → Bukti & Verifikasi).

> Pautan muat turun: setiap fail di `output/` boleh diambil dari GitHub dengan butang **Download raw** — laluan penuh:
> `https://github.com/wenjyue84/3u-pioneer-academy-noss/tree/master/video-film-editing/output/`

## Langkah 0 — Standard (NOSS) → CU & WA

| Apa | Dari mana | Output rujukan |
|---|---|---|
| 5 CU teras, 26 WA (E01 elektif tidak dihantar) | NOSS IT-072-3:2012 CP p.15–34 | `CPC` = NOSS PDF p.14 (cetak terus); senarai WA = sheet **CU & WA** dalam Lampiran 5 |

## Langkah 1 — Proses Kerja syarikat ↔ NOSS (Topik 4)

| Output (format pegawai) | Fail | Kandungan |
|---|---|---|
| Lampiran 5 Borang Matriks [JPK/ADI/02-2024] | `output/01 Lampiran 5 …/1. Borang Matriks … (IT-072).xlsx` | 11 Proses Kerja (P1–P11) × 26 WA, tanda `/`; semua 6 sheet & formula templat dikekalkan |

Dokumen kerja dalaman: `01-proses-kerja.md` (langkah setiap P — ini "kertas kerja" pekerja).

## Langkah 2 — Jadual (Topik 5) — **menentukan urutan semua bahan di bawah**

| Output | Fail | Keputusan |
|---|---|---|
| 4.2 Penjajaran Jam CA/CU | `output/02 4.2 …/4.2_Penjajaran Jam … (IT-072).xlsx` | 18 bulan = 2880 j; teori 20 % = 576 j; CA 80 j; C01–C05 99.2 j setiap satu (12/12/13/12/13 hari = 62 hari); formula templat dikekalkan |
| 4.3 Jadual Teori & Jadual Kerja | `output/03 4.3 …/4.3_Jadual … (IT-072).xlsx` | **Teori:** CA minggu 1–10 → C01 11–22 → C02 23–34 → C03 35–47 → C04 48–59 → C05 60–72. **Kerja:** P01–P11 ikut `03-jadual-latihan.md` §C |

Urutan bahan = urutan blok teori: **CA → C01 → C02 → C03 → C04 → C05**, dan dalam setiap CU ikut WA1…WAn.

## Langkah 3 — Bahan pembelajaran setiap blok (Topik 6): Rangka → Nota/Kertas Penerangan

Templat pegawai: 3.3a (rangka, prompt) → **3.3b Nota Pembelajaran** (= Kertas Penerangan JPK; kepala KOD PROGRAM / TAHAP / CU / WA / NO. KOD / TAJUK / TUJUAN / PENERANGAN / SOALAN / RUJUKAN). Peraturan pegawai: 1 WA = 1 Nota.

| Minggu | Blok | Muat turun (folder `output/05 3.3b …/`) | Bil |
|---|---|---|---|
| 1–10 | Core Abilities L1+L2+L3 (Z-009-1/2/3:2015) | `Core Abilities L1-L3/3.3b-CA-01 … -47` | 47 |
| 11–22 | C01 Visual Editing Project Analysis | `CU C01-C05/3.3b-01 … -05` | 5 |
| 23–34 | C02 Visual Editing Preparation | `3.3b-06 … -09` | 4 |
| 35–47 | C03 Offline Visual Editing | `3.3b-10 … -14` | 5 |
| 48–59 | C04 Audio Sweetening | `3.3b-15 … -20` | 6 |
| 60–72 | C05 Online Visual Editing | `3.3b-21 … -26` | 6 |

Rangka (3.3a) format pegawai: `output/04 3.3a …/` (5 fail); sumber md `04-rangka-nota-pembelajaran/`. Sumber teks: `05-nota-pembelajaran/`, `11-core-abilities/`.

## Langkah 4 — Soalan setiap blok (Topik 7/8): JSU → Soalan → rekod markah

| Output | Fail | Nota |
|---|---|---|
| 3.2 JSU (Jadual Spesifikasi Ujian) | `output/06 3.2 JSU …/3.2 Format Soalan … (IT-072).xlsx` — sheet `JSU C01`…`JSU C05` + `Prompt Cxx` | 20 soalan/CU, 10:6:4 (R/S/T) & 10:6:4 (P/F/S); formula JUMLAH templat dikekalkan |
| 3.4b Soalan Penilaian Pengetahuan | `output/07 3.4b …/CU C01-C05/3.4b-01 … -05` dan `…/Core Abilities L1-L3/3.4b-CA-01 … -14` | kertas calon + SKEMA JAWAPAN di muka akhir; lulus 60 % |
| 3.1 Bukti Rekod Penilaian Pengetahuan (markah) | `output/08 3.1 …/3.1_Bukti Penilaian Pengetahuan (IT-072).docx` | 5 CU + 14 CA baris |

Diadakan pada minggu terakhir setiap blok teori (10, 22, 34, 47, 59, 72).

## Langkah 5 — Kemahiran kerja 80 % (kertas kerja / bukti) mengikut Jadual Kerja

Dalam ADI Pekerjaan **tiada ujian amali berasingan**: "kertas kerja" = bukti kerja sebenar setiap Proses Kerja, disahkan Pembimbing.

| Output | Fail | Nota |
|---|---|---|
| 4 Senarai Bukti Proses Kerja | `output/09 …/4 Senarai Bukti Proses Kerja (IT-072).xlsx` | 34 bukti untuk P01–P11, dipetakan ke CU-WA; sheet GARIS PANDUAN pegawai dikekalkan |
| Lampiran 4 Perakuan Pembimbing [JPK/ADI/01-2024] | `output/09 …/2_Borang Perakuan Pembimbing … (IT-072).docx` | grid P01–P11 |
| Borang dalaman syarikat (10 jenis: analisis projek, semakan rough cut, QC, dll.) | belum dibina — senarai di `09-penilaian-kekompetenan.md` §D | **jika Jay mahu "Kertas Kerja" format JPK WIM** (Buku Panduan WIM), boleh dijana dari `01-proses-kerja.md` dengan skill `wim-jpk-format` — templat pegawai ADI tidak ada Kertas Kerja |

## Langkah 6 — Verifikasi & pemasangan fail (bulan 18)

Produk akhir: **Buku Teks** = kompilasi semua 3.3b Nota (docx + PDF, per CU dan penuh) di `output/13 Buku Teks (kompilasi Nota)/`.


| Output | Fail |
|---|---|
| Lampiran 6 Laporan Penilaian Bukti Kekompetenan [JPK/ADI/03-2024] | `output/10 Lampiran 6 …/1.1 Borang Laporan … (IT-072).docx` (26 + 26 baris pra-isi) |
| Fail Pelaksanaan ADI (syarikat): Isi Kandungan, Surat Tawaran, Surat Lantikan | `output/11 Fail Pelaksanaan ADI (Syarikat)/` |
| Fail Kompilasi (Bakat): Muka Hadapan, Isi Kandungan (pptx), Separator P01–P11 | `output/12 Fail Kompilasi Kemahiran Kerja (Bakat)/` |

## Semakan urutan (jangan langkau)

1. Lampiran 5 lulus (semua 26 WA ada ✓) **sebelum** jadual — jadual kerja bergantung pada P-kod.
2. 4.2 dulu, baru 4.3 — jam teori setiap CU menentukan panjang blok minggu.
3. Nota disiapkan **sebelum** soalan — JSU/soalan mesti boleh dijawab dari nota (peraturan 3.4a).
4. Senarai Bukti disiapkan **sebelum** latihan bermula — Bakat perlu tahu bukti apa nak kumpul dari hari pertama.
5. Lampiran 6 & 4 hanya pada bulan 18.

Status semua fail & `[TBD]`: `output/INDEX-fail-pegawai.md`.
