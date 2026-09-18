# INDEX — output/ (IT-072-3:2012 Video / Film (Editing), Tahap 3 · ADI Pekerjaan)

**242 fail** dalam format asal pegawai — 5 CU teras sahaja (elektif E01 diarkib di `_archive/`). Semua templat pegawai (`raw/adi-mpc-template-2026-09/`) diisi terus (formula/sheet/gaya dikekalkan); nama fail = nama asal + ` (IT-072)`. Logik pemilihan fail & urutan: `README.md`. Cari `[TBD:` untuk nilai yang perlu diisi (syarikat, Bakat, tarikh, personel, kod pusat).

| # | Folder | Fail | Templat pegawai | Sumber md |
|---|---|---|---|---|
| 01 | Lampiran 5 | `1. Borang Matriks … (IT-072).xlsx` — 26 WA × P1–P11, tanda `/`, 6 sheet, 2,523 formula | `1-panduan/lampiran-jpk/LAMPIRAN 5` | `02-`, `01-` |
| 02 | 4.2 | `4.2_Penjajaran Jam … (IT-072).xlsx` — 2880/576 j, CA 80, C01–C05 99.2 j, pundaran 12/12/13/12/13 = 62 hari, formula kekal | `2-fail-syarikat/4.2` | `03-` §A |
| 03 | 4.3 | `4.3_Jadual … (IT-072).xlsx` — Teori CA 1–10, C01 11–22, C02 23–34, C03 35–47, C04 48–59, C05 60–72; Kerja P01–P11 | `2-fail-syarikat/4.3` | `03-` §B–C |
| 04 | 3.3a | `3.3a-01 … -05 Rangka Nota Pembelajaran <CU> (IT-072).docx` — satu seksyen setiap WA, topik = Related Knowledge CoCU | `4-pelaksanaan-kompilasi/3.3a` | `04-rangka-…/` |
| 05 | 3.3b | `CU C01-C05/3.3b-01 … -26` (26, templat 3.3b; **21–26 muka setiap WA** — setiap Bab: Objektif → Pengenalan → konsep → sub-topik teknikal dengan jadual & contoh studio → prosedur → kesilapan biasa → senarai semak → kajian kes → Rumusan; Glosari + Peta minda + Latihan Pengukuhan; kepala jadual menyenaraikan **semua WA CU itu, WA semasa ditebalkan**) · `Core Abilities L1-L3 (format JPK)/KP-CA-01 … -47` (47 docx + 47 PDF, format Kertas Penerangan rasmi JPK dari zip: logo, alamat, jadual pengenalan 6 baris, header NO. KOD/Mukasurat) · `Core Abilities L1-L3/` (47, versi awal gaya 3.3b, simpanan) | `3.3b Template` / PDF rasmi zip | `05-nota-…/`, `11-core-abilities/` |
| 06 | 3.2 | `3.2 Format Soalan … (IT-072).xlsx` — 5 pasang sheet JSU/Prompt C01–C05, 20 soalan 10:6:4, SUM kekal | `3.2 Format Soalan` | `06-jsu.md` |
| 07 | 3.4b | `CU C01-C05/3.4b-01 … -05` (5, templat 3.4b) · `Core Abilities L1-L3 (format JPK)/SOALAN-CA-01 … -14` (14 docx + 14 PDF, templat rasmi `SOALAN PENILAIAN … .docx` dari zip, logo JPK, MENGANDUNGI n MUKA SURAT ikut PDF sebenar, SKEMA JAWAPAN) · `Core Abilities L1-L3/` (14, versi awal, simpanan) | `3.4b Template` / docx rasmi zip | `07-soalan-…/`, `11-…/Soalan-*` |
| 08 | 3.1 | `3.1_Bukti Penilaian Pengetahuan (IT-072).docx` — 5 CU + 14 CA baris markah | `3.1 Bukti Penilaian` | `09-` §C |
| 09 | 4 + Lampiran 4 | `4 Senarai Bukti Proses Kerja (IT-072).xlsx` (34 bukti, P01–P11) + `2_Borang Perakuan Pembimbing … (IT-072).docx` | `4 Senarai Bukti`, Lampiran 4 | `08-`, `09-` §B |
| 10 | Lampiran 6 | `1.1 Borang Laporan Penilaian Bukti Kekompetenan … (IT-072).docx` — 26 + 26 baris pra-isi | Lampiran 6 | `09-` §A |
| 11 | Fail Syarikat | `0_Isi Kandungan…`, `3.1a_Surat Tawaran…`, `5_Surat pelantikan…` (IT-072).docx | `2-fail-syarikat/` | `10-` §A |
| 12 | Fail Bakat | `1_Muka Hadapan…docx`, `2_Isi Kandungan…pptx`, `3_Fail Separator…docx` (P01–P11) | `3-persediaan-kompilasi/` | `10-` §B |
| 13 | **Buku Teks** | `Buku Teks IT-072-3-2012 … C01-C05 (IT-072).docx/.pdf` (726 muka, kulit + TOC berhalaman + 26 Nota, setiap Nota 21–26 muka) · 5 jilid per CU · `Buku Teks Core Abilities … L1-L3 (IT-072).docx/.pdf` (347 muka, 47 Nota) | kompilasi 3.3b (docxcompose + Word) | 05 |

Tidak dihasilkan (rujukan pegawai / bukan Tahap 3): `1. Panduan JPK/`, CPC (cetak NOSS p.14), MySpike manual, `4.1 Contoh Jadual`, `1.2 LPKC` (DKM/DLKM sahaja), `5.1/5.2 Tuntutan`, Slip MySPIKE.

Nota: setiap fail dibuka semula dengan openpyxl/python-docx dan dibaca balik; PDF dijana melalui Word (`_tools/Export-Pdf.ps1`, satu proses Word setiap fail). **Kebolehbacaan** (2026-09-18): semua docx/xlsx dipoles ikut `_tools/READABILITY-SPEC.md` (Arial 11, jarak baris 1.15, label tebal, jadual Table Grid berlorek, lebar lajur/wrap/freeze pada xlsx) — teks sebelum/selepas dibanding aksara demi aksara: 0 perbezaan; formula xlsx tidak berubah. Muka 1 fail (format JPK) disemak visual berbanding PDF rasmi. Skrip: `_tools/`.
