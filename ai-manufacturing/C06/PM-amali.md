<!-- JPK_ENVELOPE_v1 -->
<table border="0" cellspacing="0" cellpadding="8" width="100%">
<tr>
<td width="130" valign="top"><img src="../_assets/logos/jpk-logo.png" alt="JPK Logo" width="110"></td>
<td valign="middle">
<b>JABATAN PEMBANGUNAN KEMAHIRAN (JPK)</b><br>
TINGKAT 7-8, BLOK D4, KOMPLEKS D,<br>
PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,<br>
62530 PUTRAJAYA
</td>
</tr>
</table>

## PELAN MENGAJAR (AMALI)

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | MFG-AI-3:2026 AI FOR SMART MANUFACTURING SPECIALIST |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | MFG-AI-3:2026-C06 ENERGY MANAGEMENT AND SUSTAINABILITY WITH AI |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. DEPLOY AN AI ENERGY MONITORING DASHBOARD TO TRACK FACTORY ENERGY CONSUMPTION IN REAL TIME<br>2. USE AI ANALYSIS TOOLS TO IDENTIFY ENERGY WASTE PATTERNS AND GENERATE OPTIMISATION RECOMMENDATIONS<br>3. IMPLEMENT AI-DRIVEN ENERGY OPTIMISATION STRATEGIES TO REDUCE MANUFACTURING COSTS<br>4. CALCULATE CARBON FOOTPRINT REDUCTION AND PREPARE ESG REPORTING DATA FOR STAKEHOLDERS |
| NO. KOD | MFG-AI-3:2026-C06/PM-A(1/1) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** Pelan Mengajar Amali — Pengurusan Tenaga dan Keberlanjutan dengan AI

**TUJUAN:** Menyusun 28 sesi pengajaran amali (28 jam) merangkumi keempat-empat Aktiviti Kerja C06 melalui KK-01 dan KK-02, selaras dengan nisbah 30% teori / 70% amali bagi CU C06.

<!-- /JPK_ENVELOPE_v1 -->
---

## Maklumat Pelan Mengajar

| Item | Butiran |
|---|---|
| Jumlah Jam Amali | 28 jam |
| Jumlah Sesi | 28 sesi (@ 1 jam setiap sesi) |
| Nisbah Teori:Amali | 12 jam : 28 jam = 30% : 70% ✓ |
| Nama Jurulatih | *(kosong untuk tandatangan)* |
| Tandatangan Jurulatih | |
| Tarikh Disediakan | |

> **NOTA:** Nama jurulatih dan tandatangan dikosongkan untuk diisi secara tulisan tangan. Jadual sesi boleh disesuaikan dengan keperluan kelas.

---

## Peta Aktiviti Kerja ke Sesi Amali

| Aktiviti Kerja | Sesi Amali | Kertas Kerja |
|---|---|---|
| AK 1: Deploy AI Energy Monitoring Dashboard | A-01 hingga A-07 (7 jam) | KK-01 Fasa 1 + 2 |
| AK 2: Identify Energy Waste Patterns | A-08 hingga A-14 (7 jam) | KK-01 Fasa 3, 4, 5, 6 |
| AK 3: Implement AI Optimisation Strategies | A-15 hingga A-21 (7 jam) | KK-02 Fasa 1, 2, 3 |
| AK 4: Calculate Carbon Footprint & ESG | A-22 hingga A-28 (7 jam) | KK-02 Fasa 3 (Scope 2), 4, 5, 6 |

---

## Jadual Pelan Mengajar Amali

| Sesi | Masa (jam) | Tajuk Sesi | Objektif Pembelajaran | Aktiviti P&P | Bahan / ABBM | Penilaian |
|---|---|---|---|---|---|---|
| **A-01** | 1 jam | **Persediaan Persekitaran Kerja dan Pengenalan Dataset** | Pelatih dapat memasang Power BI Desktop, mengesahkan sambungan internet, dan memahami struktur dataset kilang sintetik | Setup Power BI Desktop; muat turun dataset `kilang_ceria_tenaga_2025.csv` dari jurulatih; terang struktur lajur; semak integrity data pertama kali | Komputer pelatih; Power BI Desktop (muat turun percuma); dataset CSV; panduan setup | Jurulatih semak: Power BI terbuka + CSV diimport dengan betul |
| **A-02** | 1 jam | **Data Import dan Data Cleaning** | Pelatih dapat mengimport data ke Power BI dan melakukan data cleaning asas | Import CSV ke Power BI Power Query; kenal pasti dan tangani null values; tambah lajur `hari_minggu` dan `waktu_kategori` | Power BI Desktop; dataset CSV; KK-01 (Langkah 1.1–1.3) | Semak: Bilangan null values direkodkan dalam borang KK-01 Bahagian A |
| **A-03** | 1 jam | **Pembinaan Visualisasi Pertama: Line Chart dan Bar Chart** | Pelatih dapat membina line chart penggunaan kWh harian dan stacked bar chart agihan per zona | Ikut langkah KK-01 Fasa 2 — bina 2 visual pertama (Line chart + Stacked bar); konfigurasikan paksi, tajuk, dan warna | Power BI Desktop; data bersih | Semak: 2 visual terbina dengan tajuk dan paksi berlabel |
| **A-04** | 1 jam | **Pembinaan Visualisasi: Profil Harian dan KPI Card** | Pelatih dapat membina profil penggunaan jam-jam dan kad EnPI yang berfungsi | Bina profil penggunaan purata jam 0–23; cipta KPI card EnPI dengan DAX formula; konfigurasikan format nombor | Power BI Desktop | Semak: KPI card menunjukkan nilai EnPI yang betul |
| **A-05** | 1 jam | **Penambahan Penapis (Slicers) dan Ujian Dashboard** | Pelatih dapat menambah slicer bulan, zona, dan waktu; menguji fungsi dashboard secara menyeluruh | Tambah 3 slicer; uji interaksi antara slicer dan setiap visual; perbaiki sebarang isu paparan | Power BI Desktop | Semak: 3 slicer berfungsi; visual bertindak balas kepada penapis |
| **A-06** | 1 jam | **Mendapatkan Kadar Tarif TNB dari Sumber Rasmi** | Pelatih dapat menavigasi laman web TNB, mengenal pasti jadual tarif industri yang betul, dan mencatat kadar yang relevan | Lawati www.tnb.com.my; cari "Jadual Tarif"; kenal pasti tarif industri; catat kadar puncak, luar puncak, dan MD; rekod dalam borang KK-01 Bahagian B | Komputer + internet; borang KK-01 Bahagian B | Semak: Borang B dilengkap dengan URL sumber dan tarikh |
| **A-07** | 1 jam | **Pengiraan EnPI dan Kos Tenaga Baseline + Eksport Dashboard** | Pelatih dapat mengira EnPI dan anggaran kos tenaga baseline dan mengeksport dashboard sebagai PDF | Kira EnPI Januari (KK-01 Langkah 5.3); kira anggaran kos tenaga Januari (KK-01 Langkah 5.2); eksport dashboard sebagai PDF; simpan semua fail | Power BI Desktop; kalkulator/spreadsheet; KK-01 Bahagian D | Semak: Dashboard PDF dieksport; Bahagian D borang dilengkap |
| **A-08** | 1 jam | **Pembinaan Formula Anomali: Statistical Baseline** | Pelatih dapat mengira purata dan standard deviasi penggunaan jam-jam dan membina formula pengesan anomali | Kira mean dan StdDev kWh per jam (hari bekerja dan hujung minggu); bina formula anomali dalam Power BI DAX atau kolum kiraan Excel | Power BI Desktop atau Excel; KK-01 Langkah 3.1 | Semak: Formula anomali mengeluarkan output "ANOMALI" atau "Normal" untuk setiap baris |
| **A-09** | 1 jam | **Visualisasi Anomali dan Ujian Sensitiviti** | Pelatih dapat menambah conditional formatting pada line chart untuk menanda anomali dan menyenaraikan semua titik anomali | Tambah conditional formatting (merah untuk anomali); cipta jadual senarai anomali; uji dengan menukar threshold (±1.5 SD vs ±2 SD) | Power BI Desktop | Semak: Titik anomali dipaparkan dalam warna berbeza; jadual anomali wujud |
| **A-10** | 1 jam | **Analisis Corak 1: Penggunaan Luar Waktu Operasi** | Pelatih dapat mengira jumlah kWh yang digunakan semasa kilang tidak beroperasi dan menyatakan implikasi kos | Kira kWh semasa bukan operasi (Ahad + 11pm–7am) menggunakan Power BI atau Excel; kira % daripada jumlah; anggaran kos | Power BI / Excel; KK-01 Langkah 4.1 | Semak: Angka kWh bukan operasi dikira dan direkodkan |
| **A-11** | 1 jam | **Analisis Corak 2: Variasi Bulanan dan Korelasi Output** | Pelatih dapat mengenal pasti bulan dengan penggunaan kWh tertinggi/terendah dan menganalisis korelasi dengan output produksi | Kira EnPI setiap bulan; plot scatter (kWh vs unit produksi); kenal pasti bulan luar trend | Power BI / Excel; KK-01 Langkah 4.2 | Semak: 3 bulan tertinggi dan 3 terendah dikenal pasti dengan justifikasi |
| **A-12** | 1 jam | **Analisis Corak 3: Kenal Pasti Corak Pembaziran Ketiga** | Pelatih dapat mengenal pasti corak pembaziran ketiga yang unik berdasarkan eksplorasi data bebas | Penerokaan bebas data oleh pelatih; jurulatih beri panduan minimal; cadangkan corak ketiga yang berbeza dari dua yang pertama | Power BI / Excel; KK-01 Langkah 4.3 | Semak: Corak ketiga dikenal pasti dengan bukti data dalam jadual KK-01 |
| **A-13** | 1 jam | **Penyediaan Laporan Ringkasan Pemantauan Tenaga** | Pelatih dapat menyediakan laporan ringkasan 2-halaman dengan dapatan yang komprehensif | Tulis laporan menggunakan Word/Docs: 4 bahagian (ringkasan eksekutif, corak pembaziran, kos baseline, EnPI vs baseline) | Word / Google Docs; KK-01 Langkah 6.2 | Semak: Laporan 2 halaman disiapkan; semua 4 bahagian ada |
| **A-14** | 1 jam | **Pembentangan KK-01 dan Maklum Balas Rakan Sebaya** | Pelatih dapat membentangkan dapatan analisis tenaga dengan jelas dalam 5 minit | Pembentangan 5 minit per pelatih; maklum balas rakan sebaya; jurulatih menilai menggunakan senarai semak KK-01 | Dashboard PDF; laporan ringkasan; senarai semak KK-01 | Penilai mengisi senarai semak KK-01; penilaian PA Aktiviti Kerja 1 dan 2 |
| **A-15** | 1 jam | **Pelan Tindakan Pengoptimuman: Semak Semula Corak dan Peta Strategi AI** | Pelatih dapat memetakan strategi AI yang sesuai kepada setiap corak pembaziran yang dikenal pasti dalam KK-01 | Semak dapatan KK-01; perbincangan kelas tentang strategi AI (demand staggering, anomaly detection, AI scheduling); isi jadual peta strategi KK-02 | KK-02 Langkah 1.1–1.2; KP-02 (rujukan) | Semak: Jadual peta strategi AI dilengkap dengan justifikasi |
| **A-16** | 1 jam | **Anggaran Unjuran Penjimatan kWh per Strategi** | Pelatih dapat membuat anggaran penjimatan kWh yang munasabah dengan andaian yang jelas | Tentukan andaian penjimatan (% pengurang) bagi setiap strategi; kira kWh jimat per bulan dan per tahun; rekod dalam jadual KK-02 | KK-02 Langkah 1.3–1.4; kalkulator | Semak: Setiap strategi ada anggaran kWh dengan andaian yang dinyatakan |
| **A-17** | 1 jam | **Pengiraan Penjimatan Kos menggunakan Tarif TNB Rasmi** | Pelatih dapat mengira penjimatan kos (RM) menggunakan kadar tarif TNB yang diperoleh dari sumber rasmi | Masukkan kWh jimat ke dalam formula kos; hitung penjimatan puncak, luar puncak, dan MD secara berasingan; jumlah penjimatan RM/tahun | KK-02 Langkah 2.2; kadar tarif TNB dari A-06; Excel | Semak: Pengiraan kos menggunakan kadar dari sumber rasmi (bukan nilai direka) |
| **A-18** | 1 jam | **Pengiraan ROI dan Tempoh Pulang Modal** | Pelatih dapat mengira ROI dan payback period dengan betul | Kira penjimatan bersih tahunan (selepas kos operasi); kira ROI (%); kira payback period; rekod dalam KK-02 Bahagian A | KK-02 Langkah 2.3; kalkulator/Excel | Semak: Formula ROI dan payback digunakan dengan betul; angka masuk akal |
| **A-19** | 1 jam | **Mendapatkan GEF Malaysia dan Pengiraan Pelepasan Scope 2 Baseline** | Pelatih dapat menavigasi laman web ST untuk mendapatkan nilai GEF dan mengira pelepasan Scope 2 baseline | Lawati www.st.gov.my; cari Grid Emission Factor terkini; rekod nilai dan sumber; kira Scope 2 baseline kilang sintetik | KK-02 Langkah 3.1–3.2; komputer + internet; borang KK-02 Bahagian B | Semak: GEF dicatat dengan URL dan tarikh; pengiraan Scope 2 betul |
| **A-20** | 1 jam | **Pengiraan Pengurangan CO₂ dan Intensiti Karbon** | Pelatih dapat mengira pengurangan CO₂ sepadan dengan penjimatan kWh dan membandingkan intensiti karbon sebelum/selepas | Kira pengurangan CO₂ = kWh jimat × GEF ÷ 1,000; kira % pengurangan; kira intensiti karbon (kg CO₂e/unit) untuk baseline dan selepas | KK-02 Langkah 3.3–3.4; kalkulator/Excel | Semak: Semua empat angka (pengurangan CO₂, %, intensiti sebelum, selepas) dikira dengan betul |
| **A-21** | 1 jam | **Semakan Insentif MIDA Green Lane dan GITA** | Pelatih dapat menavigasi laman web MIDA dan GreenTech Malaysia dan menjawab soalan kelayakan spesifik | Lawati www.mida.gov.my (Green Lane) dan www.greentechmalaysia.my (GITA); isi soal selidik KK-02 Langkah 5.1–5.2 | Komputer + internet; KK-02 Langkah 5; borang KK-02 Bahagian C | Semak: Borang C diisi dengan maklumat dari laman web rasmi (bukan reka cipta) |
| **A-22** | 1 jam | **Penyediaan Ringkasan ESG Tenaga 1-Halaman (Draf)** | Pelatih dapat menyediakan draf ringkasan ESG mengikut struktur yang ditetapkan dalam KK-02 | Buka template ESG dari KK-02 Langkah 4.1; lengkapkan setiap bahagian dengan data dari sesi sebelumnya; biarkan bahagian TBD ditanda dengan jelas | KK-02 Langkah 4.1–4.2; Word / Google Docs | Semak: Draf ringkasan ESG mengandungi semua 6 elemen mandatori |
| **A-23** | 1 jam | **Semakan dan Penambahbaikan Ringkasan ESG** | Pelatih dapat mengenal pasti kekurangan dalam ringkasan ESG draf dan memperbaikinya | Pertukaran ringkasan ESG dengan rakan sebaya untuk semakan berpasangan; gunakan senarai semak 6 elemen KK-02; buat penambahbaikan | Senarai semak 6 elemen; Word / Google Docs | Semak: Rakan sebaya tandatangan pengesahan semakan |
| **A-24** | 1 jam | **Kompilasi Laporan Pengoptimuman Tenaga (Final)** | Pelatih dapat mengkompilasi semua dokumen KK-02 ke dalam fail yang tersusun | Susun folder: laporan pengoptimuman, ringkasan ESG, spreadsheet pengiraan CO₂; semak semula semua angka konsisten merentasi dokumen | KK-02 Langkah 6.1; semua fail kerja | Semak: Folder mengandungi 3 fail yang diperlukan dengan nama betul |
| **A-25** | 1 jam | **Persiapan Pembentangan KK-02** | Pelatih dapat menyediakan pembentangan 10 minit yang terstruktur merangkumi dapatan utama | Sediakan slaid pembentangan (5–8 slaid): strategi AI, penjimatan kWh+kos, pengurangan CO₂, ringkasan ESG, insentif | PowerPoint / Google Slides | Semak: Slaid siap dengan 4 kandungan utama |
| **A-26** | 1 jam | **Pembentangan KK-02: Kumpulan Pertama** | Pelatih dapat membentangkan dapatan dengan jelas dalam 10 minit dan menjawab soalan | Pembentangan 10 minit (kumpulan pertama); soal jawab 3 minit; maklum balas jurulatih | Slaid; projektor; senarai semak PA | Penilai mengisi PA Aktiviti Kerja 3 dan 4 (kumpulan pertama) |
| **A-27** | 1 jam | **Pembentangan KK-02: Kumpulan Kedua** | Pelatih dapat membentangkan dapatan dengan jelas dalam 10 minit dan menjawab soalan | Pembentangan 10 minit (kumpulan kedua); soal jawab 3 minit; maklum balas jurulatih | Slaid; projektor; senarai semak PA | Penilai mengisi PA Aktiviti Kerja 3 dan 4 (kumpulan kedua) |
| **A-28** | 1 jam | **Penutup: Refleksi, Maklum Balas dan Penyerahan Dokumen Akhir** | Pelatih dapat merefleksi pembelajaran dan menyerahkan semua dokumen dengan lengkap | Sesi refleksi berkumpulan: "Apa yang paling bermanfaat? Apa yang sukar?"; penyerahan dokumen akhir; jurulatih kongsi maklum balas keseluruhan; pengumuman keputusan PA | Borang refleksi; senarai semak penyerahan | Semua dokumen KK-01 dan KK-02 diserahkan; PA dikembalikan kepada pelatih |

---

## Ringkasan Jam / Hours Summary

| Aktiviti Kerja | Sesi | Jam |
|---|---|---|
| AK 1: Deploy AI Energy Dashboard (KK-01 Fasa 1+2) | A-01 hingga A-07 | 7 jam |
| AK 2: Identify Energy Waste Patterns (KK-01 Fasa 3–6) | A-08 hingga A-14 | 7 jam |
| AK 3: Implement AI Optimisation Strategies (KK-02 Fasa 1–3) | A-15 hingga A-21 | 7 jam |
| AK 4: Calculate Carbon Footprint & ESG (KK-02 Fasa 3–6) | A-22 hingga A-28 | 7 jam |
| **JUMLAH AMALI** | | **28 jam** |
| **Jumlah Teori (PM-teori)** | | **12 jam** |
| **JUMLAH KESELURUHAN C06** | | **40 jam ✓** |

---

## Keperluan Makmal dan Perkakasan

| Item | Kuantiti | Nota |
|---|---|---|
| Komputer riba/PC untuk pelatih | 1 per pelatih | Windows 10/11 atau macOS; RAM min 8 GB |
| Projektor + skrin | 1 set | Untuk demonstrasi jurulatih |
| Sambungan internet | Untuk semua stesen | Diperlukan untuk akses laman web TNB, ST, MIDA, GreenTech Malaysia |
| Power BI Desktop | Dipasang pada semua PC | Muat turun percuma dari powerbi.microsoft.com |
| Microsoft Office / Google Workspace | Dipasang/akses | Untuk Word/Excel/Docs/Sheets |
| Dataset sintetik `kilang_ceria_tenaga_2025.csv` | 1 fail per pelatih | Disediakan oleh jurulatih; 8,760 baris data |

---

## Catatan Jurulatih / Instructor Notes

- **Sesi A-06 dan A-19:** Ini adalah sesi kritikal. Pelatih perlu akses internet yang stabil. Jika sambungan bermasalah, sediakan tangkapan skrin (screenshot) laman web TNB (jadual tarif) dan ST (GEF) sebagai sandaran. Rekod tarikh tangkapan skrin — nilai yang lapuk tidak boleh digunakan tanpa pengesahan semula.
- **Sesi A-26 dan A-27:** Jika kelas mempunyai lebih daripada 8 pelatih, agihkan pembentangan merentasi kedua-dua sesi. Setiap pelatih diberi masa 10 minit + 3 minit soal jawab. Jurulatih mengurus masa dengan ketat.
- **Sesi A-28:** Pastikan semua borang PA dikumpulkan dan dilengkap sebelum pelatih meninggalkan kelas.
- **Akomodasi tambahan:** Pelatih yang memerlukan masa tambahan untuk pengiraan (atas sebab keperluan khas) boleh diberikan masa sambungan tidak melebihi 20% masa sesi dengan kelulusan jurulatih.
