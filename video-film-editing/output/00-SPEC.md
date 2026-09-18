# 12 — Fail untuk semakan Pegawai (format asal MPC/JPK: .xlsx / .docx / .pptx)

**Kenapa:** Pegawai MPC/JPK menyemak dalam Excel/Word mengikut templat mereka sendiri. Fail `.md` dalam `video-film-editing/00–11` adalah rekod dalaman kita; folder ini ialah **produk yang dihantar** — templat pegawai yang **diisi**, bukan dokumen baharu.

**Peraturan mutlak**
1. **Isi templat asal, jangan bina semula.** Buka fail templat pegawai dalam `raw/adi-mpc-template-2026-09/` dengan openpyxl / python-docx / python-pptx, isi sel/perenggan, simpan sebagai fail baharu di sini. Kekalkan sheet, lajur, gaya, logo, header/footer, susunan jadual. Jangan padam sheet/lajur templat (sheet rujukan besar dalam Lampiran 5 dikekalkan).
2. **Nama fail = nama asal pegawai + akhiran ` (IT-072)`** sebelum sambungan. Bila satu templat menghasilkan banyak fail (Nota, Soalan), tambah nombor jujukan dua digit selepas kod templat: `3.3b-01 …`, `3.3b-02 …`. Struktur subfolder = struktur folder pegawai (`2. Persediaan Fail Pelaksanaan ADI_Syarikat/`, `3. Persediaan Kompilasi Kemahiran Kerja_Bakat/`, `4. Pelaksanaan Kompilasi Kemahiran Kerja_Bakat/`).
3. **Kandungan hanya dari `.md` kita** (fail sumber dinyatakan di jadual bawah). Jangan cipta kandungan baharu; jangan ubah angka. `⟪TBD: …⟫` dalam md → dalam Excel/Word tulis `[TBD: …]` (kurungan segi empat, supaya boleh dicari) — jangan kosongkan senyap.
4. **Sahkan selepas simpan:** buka semula fail yang disimpan, baca balik sel/perenggan utama, dan laporkan nilainya. Fail yang tidak boleh dibuka semula = gagal.
5. Program: `IT-072-3:2012 VIDEO / FILM (EDITING)`, Tahap 3. Pusat Latihan: `3U Pioneer Academy Sdn Bhd`. Syarikat: `[TBD: nama syarikat]`.

## Jadual pemetaan templat → sumber → output

| Templat pegawai (raw/adi-mpc-template-2026-09/…) | Sumber kandungan (video-film-editing/…) | Output (output/…) |
|---|---|---|
| `2-fail-syarikat/0_Isi Kandungan Fail Pelaksanaan ADI Pekerjaan.docx` | `10-susunan-fail-kompilasi.md` §A | `2. …/0_Isi Kandungan Fail Pelaksanaan ADI Pekerjaan (IT-072).docx` |
| `1-panduan/lampiran-jpk/LAMPIRAN 5 Borang Matriks Pemetaan Aktiviti Proses Kerja.xlsx` (sheet *NOSS vs Proses Kerja*, juga *CU & WA*) | `02-borang-matriks-lampiran-5.md`, `01-proses-kerja.md` | `2. …/1. Borang Matriks Pemetaan Aktiviti Proses Kerja Syarikat Berdasarkan NOSS_JPK_ADI_02-2024 (IT-072).xlsx` |
| `2-fail-syarikat/3.1a Surat Tawaran Kerja BAKAT.docx` | program/TBD sahaja | `2. …/3.1a_Surat Tawaran Kerja_BAKAT (IT-072).docx` |
| `2-fail-syarikat/4.2 Penjajaran Jam Latihan CA_CU_EU.xlsx` | `03-jadual-latihan.md` §A | `2. …/4.2_Penjajaran Jam Latihan CA_CU_EU Program ADI Pekerjaan (IT-072).xlsx` |
| `2-fail-syarikat/4.3 Jadual Pengetahuan dan Proses Kerja.xlsx` (sheet *Jadual Teori*, *Jadual Kerja*) | `03-jadual-latihan.md` §B, §C | `2. …/4.3_Jadual Pengetahuan dan Proses Kerja ADI Pekerjaan (IT-072).xlsx` |
| `2-fail-syarikat/5 Contoh surat pelantikan personel ADI.docx` | program/TBD sahaja | `2. …/5_Surat pelantikan personel ADI (IT-072).docx` |
| `3-persediaan-kompilasi/1_Muka Hadapan Kompilasi.docx` | program | `3. …/1_Muka Hadapan Kompilasi Kemahiran Kerja (IT-072).docx` |
| `3-persediaan-kompilasi/2_Isi Kandungan.pptx` | `10-…` §B | `3. …/2_Isi Kandungan (IT-072).pptx` |
| `3-persediaan-kompilasi/3_Fail Separator.docx` | `01-proses-kerja.md` (P01–P12 tajuk) | `3. …/3_Fail Separator (Color Paper) (IT-072).docx` |
| `4-pelaksanaan-kompilasi/1.1 Borang Laporan Penilaian Bukti Kekompetenan.docx` | `09-penilaian-kekompetenan.md` §A | `4. …/1.1 Borang Laporan Penilaian Bukti Kekompetenan Calon Melalui Kaedah ADI Pekerjaan_JPK_ADI_03-2024 (IT-072).docx` |
| `4-pelaksanaan-kompilasi/2 Borang Perakuan Pembimbing.docx` | `09-…` §B | `4. …/2_Borang Perakuan Pembimbing ADI Pekerjaan_JPK_ADI_01-2024 (IT-072).docx` |
| `4-pelaksanaan-kompilasi/3.1 Bukti Penilaian Pengetahuan.docx` | `09-…` §C | `4. …/3.1_Bukti Penilaian Pengetahuan (IT-072).docx` |
| `4-pelaksanaan-kompilasi/3.2 Format Soalan PENILAIAN PENGETAHUAN.xlsx` (sheet *JSU STD THP 1-3 (n WA)* + *Prompt nWA*) | `06-jsu.md` | `4. …/3.2_Format Soalan PENILAIAN PENGETAHUAN (IT-072).xlsx` — 6 pasang sheet, satu setiap CU |
| `4-pelaksanaan-kompilasi/3.3b Template Nota Pembelajaran.docx` | `05-nota-pembelajaran/*.md` (31) | `4. …/3.3b Nota Pembelajaran/3.3b-01 … 3.3b-31 Nota Pembelajaran <CU-Wnn> <tajuk WA> (IT-072).docx` |
| sama | `11-core-abilities/*/KP-*.md` (47) | `4. …/3.3b Nota Pembelajaran Core Abilities/3.3b-CA-01 … -47 Nota Pembelajaran <Lx-CAxx> KP-<n> (IT-072).docx` |
| `4-pelaksanaan-kompilasi/3.4b Template Penilaian Pengetahuan.docx` | `07-soalan-penilaian-pengetahuan/*.md` (6) | `4. …/3.4b Penilaian Pengetahuan/3.4b-01 … -06 Penilaian Pengetahuan <CU> (IT-072).docx` |
| sama | `11-core-abilities/*/Soalan-*.md` (14) | `4. …/3.4b Penilaian Pengetahuan Core Abilities/3.4b-CA-01 … -14 Penilaian Pengetahuan <Lx-CAxx> (IT-072).docx` |
| `4-pelaksanaan-kompilasi/4 Senarai Bukti Proses Kerja.xlsx` (sheet *SENARAI BUKTI PROSES KERJA*, *Susunan Semula PK ke CU-WA*) | `08-senarai-bukti-proses-kerja.md` | `4. …/4_Senarai Bukti Proses Kerja (IT-072).xlsx` |

Tidak diisi (rujukan pegawai / bukan milik kita): `1. Panduan JPK/`, `3.0 Carta Aliran`, `3.2/3.3 Panduan MySpike`, `2_Competency Profil Chart.pdf` (gunakan CPC dari NOSS PDF p.14), `4.1 Contoh Jadual` (contoh), `5.1/5.2 Tuntutan`.

Selepas semua siap: `INDEX-fail-pegawai.md` di folder ini menyenaraikan setiap fail output, templat asalnya, sumber md, dan status `[TBD]` yang masih ada.
