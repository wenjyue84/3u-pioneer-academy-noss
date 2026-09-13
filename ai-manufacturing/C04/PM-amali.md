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
| KOD DAN TAJUK UNIT KOMPETENSI | MFG-AI-3:2026-C04 AI PRODUCTION PLANNING AND SCHEDULING OPTIMISATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. USE AI SIMULATION TOOLS TO IDENTIFY PRODUCTION BOTTLENECKS (KESESAKAN PENGELUARAN) AND QUANTIFY CAPACITY LOSS<br>2. IMPLEMENT AI-OPTIMISED PRODUCTION SCHEDULING BALANCING ORDER PRIORITY, CAPACITY CONSTRAINTS, AND MATERIAL AVAILABILITY<br>3. APPLY AI DEMAND FORECASTING MODELS (MODEL RAMALAN PERMINTAAN) TO DYNAMICALLY ADJUST PRODUCTION PLANS<br>4. VALIDATE AI SCHEDULING OUTCOMES AGAINST JIT BENCHMARKS AND PRESENT EFFICIENCY GAINS |
| NO. KOD | MFG-AI-3:2026-C04/PM-A(1/1) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** Pelan Mengajar Amali — AI Production Planning and Scheduling Optimisation

**TUJUAN:** Merancang penyampaian 28 jam kandungan amali CU04 merentasi 14 sesi (2 jam setiap sesi) yang merangkumi KK-01 (Analisis Bottleneck) dan KK-02 (Ramalan AI dan Jadual Pengeluaran) berstrukturkan kepada keempat-empat Aktiviti Kerja.

<!-- /JPK_ENVELOPE_v1 -->
---

## Maklumat Am / General Information

| Medan | Nilai |
|-------|-------|
| **Jumlah Jam Amali** | 28 jam |
| **Bilangan Sesi** | 14 sesi × 2 jam |
| **Kaedah Penyampaian** | Amali komputer, latihan berkumpulan, pembentangan hasil |
| **Bahasa Pengajaran** | Bahasa Malaysia (istilah teknikal dalam Bahasa Inggeris) |
| **Nama Instruktur** | *(Dikosongkan — diisi semasa penjadualan)* |
| **Tandatangan Instruktur** | *(Kosong — untuk tandatangan)* |
| **Nisbah Pelatih: Fasilitator** | Maksimum 20:1 |

---

## Gambaran Keseluruhan Amali / Practical Overview

| Fasa | Sesi | Aktiviti Kerja | Kandungan |
|------|------|---------------|-----------|
| **KK-01** | 1–7 | AK1 + AK2 | Analisis Bottleneck dan Penjadualan AI |
| **KK-02** | 8–12 | AK3 | Ramalan Permintaan AI (Prophet) + Jadual Pengeluaran |
| **KK-02 lanjutan + Validasi** | 13–14 | AK4 | Validasi vs. JIT + Pembentangan Akhir |

---

## FASA KK-01: ANALISIS BOTTLENECK DAN PENJADUALAN AI
### Sesi 1–7 (14 jam) — Aktiviti Kerja 1 dan 2

---

### SESI A1 (2 jam) — Persediaan dan Pengenalan Dataset

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Persediaan Persekitaran dan Pemahaman Dataset Kilang |
| **Objektif Pembelajaran** | 1. Memasang dan mengesahkan persekitaran Python dengan pakej pandas, numpy, matplotlib. 2. Memuat dan memeriksa dataset kapasiti kilang PCB simulasi. 3. Memahami struktur dan medan data kapasiti kilang. |
| **Aktiviti P&P** | (0:00–0:20) Fasilitator verifikasi semua pelatih mempunyai Python/Anaconda yang berfungsi. Bantu pelatih yang menghadapi masalah teknikal. (0:20–0:50) Pelatih muat fail `kilang_pcb_kapasiti_data.csv`, semak data menggunakan `pd.read_csv()` dan `df.describe()`. Fasilitator tunjukkan cara membaca dan mengesahkan data. (0:50–1:30) Syarahan ringkas oleh fasilitator: Makna setiap medan (ID stesen, masa proses, kapasiti nominal, OEE, permintaan MPS). Hubungkan kepada teori KP-01 yang dipelajari. (1:30–2:00) Pelatih melengkapkan Borang Rekod E1 (KK-01) dengan pemerhatian awal tentang data. |
| **Bahan / ABBM** | Komputer dengan Python/Anaconda; Fail `kilang_pcb_kapasiti_data.csv`; KK-01 (Langkah 1); KP-01 |
| **Penilaian** | Semak: Adakah pelatih berjaya memuat data? Adakah mereka dapat menerangkan makna setiap medan? |

---

### SESI A2 (2 jam) — Pengiraan Nisbah Penggunaan Kapasiti

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Pengiraan Kapasiti Efektif dan Nisbah Penggunaan Kapasiti |
| **Objektif Pembelajaran** | 1. Mengira Kapasiti Efektif untuk setiap stesen kerja (Kapasiti Nominal × OEE). 2. Mengira Nisbah Penggunaan Kapasiti untuk setiap stesen. 3. Mengkelaskan stesen kepada OK / RISIKO / BOTTLENECK menggunakan Python. |
| **Aktiviti P&P** | (0:00–0:30) Fasilitator tunjukkan cara mengira Kapasiti Efektif dalam Python/pandas menggunakan dataset. Pelatih ikuti serentak. (0:30–1:00) Pelatih menulis kod sendiri untuk mengira Nisbah Penggunaan Kapasiti dan menambah lajur status (OK/RISIKO/BOTTLENECK). (1:00–1:30) Fasilitator menunjukkan cara membuat carta bar (bar chart) Nisbah Penggunaan menggunakan matplotlib. Pelatih hasilkan visual yang sama. (1:30–2:00) Pelatih melengkapkan jadual E1 (KK-01) dengan keputusan pengiraan. Fasilitator semak kumpulan secara bergilir. |
| **Bahan / ABBM** | Komputer; Dataset; KK-01 (Langkah 2 dan 3); KP-01 (Seksyen 2.2) |
| **Penilaian** | Ketepatan pengiraan Kapasiti Efektif dan Nisbah Penggunaan semua 6 stesen. |

---

### SESI A3 (2 jam) — Pengiraan Kehilangan Kapasiti dan Nilai

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Kuantifikasi Kehilangan Kapasiti dalam Unit dan Nilai Ringgit |
| **Objektif Pembelajaran** | 1. Mengira kehilangan kapasiti dalam unit/syif dan unit/minggu untuk stesen bottleneck. 2. Mengira kehilangan nilai kapasiti dalam Ringgit Malaysia. 3. Merekod keputusan dalam Borang E3 (KK-01). |
| **Aktiviti P&P** | (0:00–0:30) Fasilitator semak keputusan Sesi A2 dan betulkan kesilapan biasa. Perbincangan: mengapa OEE penting dalam pengiraan kapasiti sebenar? (0:30–1:00) Pelatih mengira kehilangan kapasiti (unit/syif dan unit/minggu) menggunakan Python atau Excel. Fasilitator bimbing formula. (1:00–1:30) Pelatih mengira kehilangan nilai (RM/minggu) menggunakan nilai sumbangan RM22.75/unit. Fasilitator semak pengiraan beberapa pelatih. (1:30–2:00) Pelatih melengkapkan jadual E3 (KK-01). Fasilitator meminta beberapa pelatih berkongsi keputusan untuk semakan kelas. |
| **Bahan / ABBM** | Komputer; Dataset; KK-01 (Langkah 4 dan 5); Kalkulator |
| **Penilaian** | Ketepatan pengiraan kehilangan unit/minggu dan nilai RM (toleransi ±5%). |

---

### SESI A4 (2 jam) — Analisis TOC dan Cadangan Pemulihan

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Penerapan Theory of Constraints dan Penggubalan Cadangan Pemulihan |
| **Objektif Pembelajaran** | 1. Menerapkan Lima Langkah Fokus TOC kepada data kilang simulasi. 2. Mengemukakan sekurang-kurangnya tiga cadangan pemulihan yang realistik dan berprioritibelaskan. 3. Menyusun cadangan dalam Matriks Kesan × Kos. |
| **Aktiviti P&P** | (0:00–0:30) Perbincangan berkumpulan (4–5 pelatih): Gunakan Lima Langkah TOC untuk menganalisis bottleneck yang dikenal pasti. Setiap kumpulan menjawab: (i) Bottleneck mana yang paling kritikal? (ii) Apa dua tindakan eksploitasi yang tidak memerlukan kos modal? (0:30–1:00) Kumpulan mengemukakan cadangan. Fasilitator bimbing diskusi — kriteria cadangan yang baik: spesifik, realistik, anggaran kesan. (1:00–1:30) Pelatih mengisi Borang E4 (KK-01) — tiga cadangan berprioritibelaskan secara individu. (1:30–2:00) Perbincangan matriks Kesan × Kos. Fasilitator membimbing cara mengkategorikan cadangan mengikut potensi kesan dan kos pelaksanaan. |
| **Bahan / ABBM** | KK-01 (Langkah 6 dan 7); KP-01 (Seksyen 2.1–2.2); Whiteboard untuk matriks |
| **Penilaian** | Kualiti dan kebolehrealisasian cadangan yang dikemukakan. Fasilitator menilai secara langsung. |

---

### SESI A5 (2 jam) — Penyediaan Laporan Analisis Bottleneck

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Penulisan Laporan Analisis Bottleneck yang Berstruktur |
| **Objektif Pembelajaran** | 1. Menyusun laporan analisis bottleneck yang lengkap menggunakan templat yang diberikan. 2. Memasukkan ringkasan eksekutif, jadual data, peta proses, dan cadangan berprioritibelaskan. 3. Memastikan semua angka dalam laporan tepat dan konsisten. |
| **Aktiviti P&P** | (0:00–0:20) Fasilitator terangkan struktur laporan bottleneck yang baik menggunakan contoh (laporan dummy satu halaman). (0:20–1:30) Pelatih mengisi templat laporan menggunakan dapatan dari Sesi A2–A4. Fasilitator beredar membantu. (1:30–2:00) Semakan rakan sebaya (peer review): Pelatih bertukar laporan dengan rakan dan semak konsistensi angka (adakah angka dalam jadual sepadan dengan cadangan?). Berikan maklum balas bertulis. |
| **Bahan / ABBM** | Templat laporan `templat_laporan_bottleneck.docx`; Komputer; KK-01 (Langkah 8) |
| **Penilaian** | Kelengkapan laporan, ketepatan angka, dan kualiti cadangan. |

---

### SESI A6 (2 jam) — Penjadualan AI: Konsep dan Latihan Job Sequencing

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Penjadualan AI dalam Konteks Kilang: Latihan SPT dan EDD Hands-On |
| **Objektif Pembelajaran** | 1. Menyelesaikan masalah job sequencing menggunakan SPT dan EDD dengan data yang diberikan. 2. Mengesahkan kesahihan jadual yang dihasilkan. 3. Membandingkan metrik prestasi SPT vs. EDD. |
| **Aktiviti P&P** | (0:00–0:20) Ulangkaji teori SPT dan EDD (Sesi 6 teori). Tekankan semakan kesahihan. (0:20–1:10) Latihan individu: Selesaikan masalah job sequencing KP-03 Seksyen 4 menggunakan data kilang PCB Pasir Gudang (5 pesanan). Hasilkan jadual SPT dan EDD secara bertulis. Fasilitator beredar memeriksa kerja. (1:10–1:40) Perbincangan jawapan kelas. Fasilitator tunjukkan semakan kesahihan untuk jadual EDD — setiap Masa Siap Kumulatif disahkan. (1:40–2:00) Latihan tambahan: Fasilitator berikan 4 pesanan baharu (berbeza dari KP-03) untuk latihan kendiri. Periksa sendiri menggunakan kaedah semakan kesahihan yang diajar. |
| **Bahan / ABBM** | KP-03 (Seksyen 4); Kertas A4 untuk pengiraan; KK-01 (Langkah 9) |
| **Penilaian** | Kesahihan jadual SPT dan EDD yang dihasilkan. Fasilitator semak sekurang-kurangnya 5 pelatih secara langsung. |

---

### SESI A7 (2 jam) — Pembentangan KK-01 dan Penilaian Prestasi

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Pembentangan Hasil Analisis Bottleneck (KK-01) |
| **Objektif Pembelajaran** | 1. Membentangkan hasil analisis bottleneck, cadangan, dan laporan kepada fasilitator dan rakan sekumpulan. 2. Menjawab soalan tentang metodologi dan dapatan. 3. Menerima maklum balas dan mengenalpasti peluang penambahbaikan. |
| **Aktiviti P&P** | (0:00–1:40) Pembentangan kumpulan (4–5 pelatih per kumpulan, 8 minit per kumpulan). Setiap kumpulan bentangkan: (i) Bottleneck yang dikenal pasti; (ii) Kehilangan kapasiti dalam unit dan RM; (iii) Tiga cadangan berprioritibelaskan. (1:40–1:55) Fasilitator berikan maklum balas merangkumi kelas. (1:55–2:00) Transisi: Perkenalkan KK-02 — Ramalan AI dan Jadual Pengeluaran. |
| **Bahan / ABBM** | Laporan KK-01 (siap); Projektor untuk pembentangan; Borang Penilaian PA (AK1 dan AK2) |
| **Penilaian** | PA — AK1 (Bottleneck Analysis) dan AK2 (AI Scheduling) dinilai secara langsung semasa pembentangan menggunakan Kertas PA. |

---

## FASA KK-02: RAMALAN AI DAN JADUAL PENGELUARAN
### Sesi 8–14 (14 jam) — Aktiviti Kerja 3 dan 4

---

### SESI B1 (2 jam) — Persediaan Prophet dan Pemahaman Dataset Permintaan

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Pemasangan Prophet dan Pemahaman Data Permintaan Sejarah 12 Bulan |
| **Objektif Pembelajaran** | 1. Memasang pakej Prophet menggunakan pip. 2. Memuat dataset permintaan sejarah 12 bulan ke dalam Python. 3. Memahami format data yang diperlukan oleh Prophet (lajur `ds` dan `y`). |
| **Aktiviti P&P** | (0:00–0:30) Fasilitator panduan pemasangan Prophet: `pip install prophet`. Sahkan pemasangan berjaya. Bantu pelatih yang menghadapi masalah versi. (0:30–1:00) Pelatih memuat dataset `data_permintaan_pcb_12bulan.csv` dan mencipta DataFrame Prophet yang betul (lajur `ds` dalam format datetime, lajur `y` dalam integer). (1:00–1:30) Fasilitator menerangkan makna setiap titik data dalam konteks kilang — kenapa Jan 2026 lebih rendah (CNY), kenapa Nov/Dis 2025 lebih tinggi (akhir tahun). (1:30–2:00) Pelatih melengkapkan Borang D (KK-02) bahagian awal — merekod 3 pemerhatian awal tentang pola permintaan. |
| **Bahan / ABBM** | Komputer dengan Python; Fail dataset 12 bulan; KK-02 (Langkah 1 dan 2) |
| **Penilaian** | Pengesahan: Adakah DataFrame Prophet berjaya dicipta dengan format yang betul? |

---

### SESI B2 (2 jam) — Latihan Model Prophet dengan Konfigurasi Hari Cuti

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Melatih Model Prophet dengan Hari Cuti Malaysia |
| **Objektif Pembelajaran** | 1. Mengkonfigurasi hari cuti Malaysia (Hari Raya, Chinese New Year) dalam Prophet. 2. Memahami parameter `lower_window` dan `upper_window`. 3. Melatih model Prophet menggunakan `model.fit()`. |
| **Aktiviti P&P** | (0:00–0:30) Fasilitator jelaskan kepentingan mengkonfigurasi hari cuti untuk kilang Malaysia. Demo langsung: pembinaan DataFrame hari cuti dan maknanya. (0:30–1:00) Pelatih menulis kod konfigurasi hari cuti mereka sendiri. Fasilitator beredar memeriksa konfigurasi `lower_window` dan `upper_window`. (1:00–1:40) Pelatih menjalankan `model.fit(df)` dan memeriksa bahawa model dilatih tanpa ralat. Fasilitator menerangkan maksud mesej amaran Python yang biasa muncul (bukan ralat). (1:40–2:00) Perbincangan: Mengapa konfigurasi hari cuti yang tidak betul boleh menghasilkan ramalan yang kurang tepat? |
| **Bahan / ABBM** | Komputer; KK-02 (Langkah 3); KP-02 (Seksyen 2.3) |
| **Penilaian** | Semak: Adakah hari cuti dikonfigurasi dengan betul? Adakah model dilatih tanpa ralat fatal? |

---

### SESI B3 (2 jam) — Penjanaan Ramalan dan Visualisasi

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Menjana Ramalan 3 Bulan dan Menganalisis Plot Komponen |
| **Objektif Pembelajaran** | 1. Menggunakan `model.predict()` untuk menjana ramalan 3 bulan hadapan. 2. Menghasilkan dan menyimpan plot ramalan dan plot komponen. 3. Mentafsirkan output ramalan (yhat, yhat_lower, yhat_upper) dan komponen (trend, musiman, cuti). |
| **Aktiviti P&P** | (0:00–0:30) Fasilitator demo cara menjana future dataframe dan menjalankan `model.predict()`. Tunjukkan format output. (0:30–1:00) Pelatih jalankan ramalan dan paparkan output 3 bulan terakhir. Rekod nilai `yhat`, `yhat_lower`, `yhat_upper` dalam Borang D1 (KK-02). (1:00–1:30) Pelatih hasilkan plot ramalan dan plot komponen, simpan sebagai fail PNG. (1:30–2:00) Analisis plot komponen: Fasilitator tanya kepada kelas — "Bulan mana permintaan paling rendah berdasarkan komponen musiman?" Pelatih menjawab berdasarkan plot masing-masing. |
| **Bahan / ABBM** | Komputer; KK-02 (Langkah 4 dan 5); KP-02 (Seksyen 2.3) |
| **Penilaian** | Semak: Adakah ramalan 3 bulan dihasilkan? Plot disimpan? Penafsiran komponen betul? |

---

### SESI B4 (2 jam) — Penyusunan Jadual Pengeluaran AI

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Penyusunan Jadual Pengeluaran Berdasarkan Ramalan Prophet |
| **Objektif Pembelajaran** | 1. Menggunakan output ramalan Prophet untuk menyusun jadual pengeluaran mingguan. 2. Memastikan jadual yang disusun sah (jumlah unit ≈ ramalan permintaan). 3. Merekod jadual dalam Borang D2 (KK-02). |
| **Aktiviti P&P** | (0:00–0:30) Fasilitator terangkan cara menukar ramalan bulanan kepada mingguan dengan andaian distribusi seragam. Kaitkan dengan kapasiti stesen kerja yang tersedia. (0:30–1:00) Pelatih menyusun jadual pengeluaran 4 minggu menggunakan ramalan Prophet mereka. Fasilitator beredar menyemak: adakah jumlah unit dijadualkan ≈ ramalan? (1:00–1:30) Pelatih melengkapkan Jadual D2 dalam KK-02. Fasilitator minta beberapa pelatih berkongsi jadual mereka. (1:30–2:00) Semakan kelas: Fasilitator tunjukkan cara menyemak kesahihan jadual pengeluaran — jumlah mesti konsisten, kapasiti tidak boleh melebihi kapasiti efektif yang tersedia. |
| **Bahan / ABBM** | Komputer; KK-02 (Langkah 6 dan 7); KP-03 (Seksyen 1.1) |
| **Penilaian** | Ketepatan jadual pengeluaran (toleransi ±2% berbanding ramalan). Kesahihan disemak. |

---

### SESI B5 (2 jam) — Jadual JIT Manual dan Pengiraan Keuntungan Kecekapan

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Perbandingan Jadual JIT vs. AI dan Pengiraan Keuntungan Kecekapan |
| **Objektif Pembelajaran** | 1. Menyusun jadual JIT manual menggunakan permintaan sejarah bulan lalu + stok keselamatan 5%. 2. Membandingkan jadual AI dan jadual JIT menggunakan sekurang-kurangnya 3 parameter. 3. Mengira keuntungan kecekapan: penjimatan stok berlebihan (RM), OTD dijangka, masa penyediaan. |
| **Aktiviti P&P** | (0:00–0:30) Fasilitator terangkan cara menyusun jadual JIT manual menggunakan formula permintaan sejarah + 5%. Pelatih kira sendiri. (0:30–1:00) Pelatih melengkapkan Jadual Perbandingan D3 (KK-02) dengan sekurang-kurangnya 5 parameter: kuantiti, lebihan, nilai lebihan, OTD, masa jadual. (1:00–1:30) Pelatih mengira penjimatan nilai stok berlebihan menggunakan data sintetik KK-02. Fasilitator semak pengiraan. (1:30–2:00) Perbincangan kelas: Adakah penjimatan RM ini cukup untuk membenarkan kos langganan platform AI scheduling? Ini adalah soalan terbuka untuk pemikiran kritis. |
| **Bahan / ABBM** | KK-02 (Langkah 7, 8, dan 9); Kalkulator; KP-03 (Seksyen 5.1 dan 5.2) |
| **Penilaian** | Ketepatan pengiraan penjimatan nilai stok berlebihan. Kualiti perbandingan dalam Jadual D3. |

---

### SESI B6 (2 jam) — Penyediaan Laporan Akhir dan Refleksi

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Penyediaan Dokumen Akhir KK-02 dan Refleksi Pembelajaran |
| **Objektif Pembelajaran** | 1. Melengkapkan semua borang rekod KK-02 (D1–D5). 2. Menyediakan dokumen akhir yang merangkumi ramalan Prophet, jadual pengeluaran AI, perbandingan JIT, dan keuntungan kecekapan. 3. Melengkapkan refleksi pembelajaran (D5). |
| **Aktiviti P&P** | (0:00–1:00) Pelatih melengkapkan semua borang KK-02 yang belum siap. Fasilitator beredar membantu. Penekanan pada D5 (Refleksi) — pelatih mesti menulis dalam kata-kata sendiri, bukan terjemahan nota. (1:00–1:30) Semakan rakan sebaya: Pelatih bertukar dokumen dan semak kelengkapan (adakah semua medan diisi? Adakah angka konsisten?). (1:30–2:00) Perbincangan kelas: Fasilitator mengulas kesilapan biasa yang ditemui semasa rounnd beredar — contoh: ramalan direkod tetapi jadual tidak menggunakannya; stok berlebihan dikira dengan formula yang salah. |
| **Bahan / ABBM** | KK-02 (semua bahagian); Komputer |
| **Penilaian** | Kelengkapan dokumen KK-02. Kualiti refleksi (D5). |

---

### SESI B7 (2 jam) — Pembentangan Akhir dan Penilaian Prestasi

| Komponen | Butiran |
|----------|---------|
| **Tajuk** | Pembentangan Akhir CU04: Validasi AI Scheduling vs. JIT dan Keuntungan Kecekapan |
| **Objektif Pembelajaran** | 1. Membentangkan keseluruhan hasil kerja CU04 — analisis bottleneck, ramalan AI, jadual pengeluaran, dan perbandingan keuntungan. 2. Menjustifikasikan pilihan metodologi dan menjawab soalan secara kritikal. 3. Menerima penilaian prestasi akhir (PA). |
| **Aktiviti P&P** | (0:00–1:40) Pembentangan individu atau kumpulan (8–10 minit per persembahan). Setiap pelatih/kumpulan mesti mencakupi: (i) Bottleneck yang dikenal pasti dan cadangan; (ii) Output ramalan Prophet (trend, musiman, 3 bulan ramalan); (iii) Jadual AI vs. JIT dan keuntungan kecekapan; (iv) Satu had model Prophet yang mereka temui. (1:40–1:55) Fasilitator berikan ulasan keseluruhan dan kelas. Penekanan: ketepatan pengiraan adalah kritikal — ramalan yang tidak digunakan dalam jadual adalah tanda asas yang lemah. (1:55–2:00) Penutupan CU04: Kaitan kepada CU05 (AI Inventory and Supply Chain). |
| **Bahan / ABBM** | Dokumen KK-01 dan KK-02 (siap); Projektor; Borang Penilaian PA (AK3 dan AK4) |
| **Penilaian** | PA — AK3 (Demand Forecasting) dan AK4 (Validation & Presentation) dinilai semasa pembentangan menggunakan Kertas PA. |

---

## Ringkasan Jam Amali / Practical Hours Summary

| Sesi | Tajuk Ringkas | Jam | AK |
|------|--------------|-----|-----|
| A1 | Persediaan dan Dataset Kapasiti | 2 | AK1 |
| A2 | Nisbah Penggunaan Kapasiti | 2 | AK1 |
| A3 | Kehilangan Kapasiti dan Nilai | 2 | AK1 |
| A4 | TOC dan Cadangan | 2 | AK1 |
| A5 | Laporan Bottleneck | 2 | AK2 |
| A6 | Job Sequencing SPT/EDD | 2 | AK2 |
| A7 | Pembentangan KK-01 | 2 | AK1+AK2 |
| B1 | Persediaan Prophet | 2 | AK3 |
| B2 | Latihan Prophet dan Hari Cuti | 2 | AK3 |
| B3 | Ramalan dan Visualisasi | 2 | AK3 |
| B4 | Jadual Pengeluaran AI | 2 | AK3 |
| B5 | JIT vs. AI dan Keuntungan | 2 | AK4 |
| B6 | Laporan Akhir dan Refleksi | 2 | AK4 |
| B7 | Pembentangan Akhir | 2 | AK3+AK4 |
| **JUMLAH** | | **28 jam** | |

> **Pengesahan:** Jumlah jam amali = 28 jam. Ini mematuhi keperluan 70% amali dalam nisbah 12 jam teori / 28 jam amali / 40 jam jumlah per CU. Jumlah keseluruhan CU04 = **12 + 28 = 40 jam**. ✓

---

## Nota kepada Instruktur / Instructor Notes

1. **Sokongan teknikal Prophet:** Masalah pemasangan Prophet sangat biasa — sediakan prosedur penyelesaian masalah (troubleshooting guide) yang dicetak untuk Sesi B1. Isu versi `pystan` dan `cmdstanpy` adalah yang paling kerap berlaku.
2. **Domain caution — ketepatan aritmetik:** Dalam sesi job sequencing (A6), tekankan kepada pelatih bahawa jadual yang tidak sah adalah kesilapan yang paling mudah dikesan oleh jurulatih dan penilai JPK. Sentiasa sahkan bahawa Masa Siap Kumulatif = jumlah semua masa proses sebelumnya.
3. **KK-01 vs. KK-02 aliran:** KK-01 boleh dijalankan tanpa sambungan internet (data sintetik disediakan). KK-02 memerlukan pemasangan Prophet yang berfungsi. Sediakan alternatif (Excel dengan pengiraan ramalan manual sederhana) untuk pelatih yang menghadapi masalah teknikal berterusan.
4. **Pengurusan masa sesi A7 dan B7:** Jika lebih dari 5 kumpulan, pertimbangkan untuk mempersingkatkan pembentangan kepada 6 minit atau jalankan beberapa pembentangan secara serentak (parallel track).
5. **Hubungan NIMP 2030:** Kaitkan setiap sesi kepada NIMP 2030 Thrust 2 (Supply Chain Resilience & Efficiency). Kilang-kilang Malaysia yang mengurangkan bottleneck dan menggunakan AI scheduling menyumbang kepada matlamat daya saing pembuatan negara.
