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
| KOD DAN TAJUK UNIT KOMPETENSI | MFG-AI-3:2026-C02 AI PREDICTIVE MAINTENANCE AND EQUIPMENT HEALTH MONITORING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. INSTALL IOT SENSORS ON CRITICAL EQUIPMENT AND ESTABLISH AN EQUIPMENT HEALTH MONITORING DATA STREAM<br>2. CONFIGURE AN AI PREDICTIVE MAINTENANCE ALERT SYSTEM (SISTEM AMARAN PENYELENGGARAAN RAMALAN AI)<br>3. ANALYSE EQUIPMENT FAILURE PATTERNS USING MACHINE LEARNING MODELS AND PRODUCE A MAINTENANCE RECOMMENDATION REPORT<br>4. CALCULATE AND PRESENT PREDICTIVE MAINTENANCE ROI TO JUSTIFY IMPLEMENTATION |
| NO. KOD | MFG-AI-3:2026-C02/PM-A(1/1) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** Pelan Mengajar Amali — AI Predictive Maintenance and Equipment Health Monitoring

**TUJUAN:** Merancang pelaksanaan sesi amali selama 28 jam merangkumi empat Aktiviti Kerja C02 — dari pemasangan sensor IoT simulasi dan konfigurasi dashboard, kepada analisis anomali ML, penulisan laporan penyelenggaraan, pengiraan ROI, dan pembentangan akhir.

<!-- /JPK_ENVELOPE_v1 -->

---

## Maklumat Pelan Mengajar

| Medan | Nilai |
|---|---|
| Nama Pensyarah | *(tandatangan dan nama semasa pengajaran)* |
| Kumpulan Pelatih | |
| Bilangan Pelatih | Maksimum 20 orang |
| Jumlah Jam Amali | **28 jam** |
| Nisbah Teori:Amali | 30% : 70% (12 jam teori / 28 jam amali) |
| Persediaan Pelatih | Akaun Azure (percuma) atau AWS diwujudkan sebelum Sesi A-1; Python 3.10+ dengan pip dipasang |
| Saiz Kumpulan | 2 orang per kumpulan (kerja berpasangan untuk KK-01 dan KK-02) |

---

## Pelan Sesi — Jadual Amali (28 Jam)

> **SEMAKAN JAM:** Sesi A-1 (8 jam) + A-2 (8 jam) + A-3 (7 jam) + A-4 (5 jam) = **28 jam amali** ✓

---

### Sesi A-1: KK-01 Bahagian 1 — Persediaan IoT dan Aliran Data Sensor (8 Jam)
**Merangkumi AK 1 dan sebahagian AK 2**

| Komponen | Butiran |
|---|---|
| **Masa** | 8 jam (480 minit) |
| **Tajuk Sesi** | Pemasangan Sensor IoT Simulasi dan Penubuhan Aliran Data Pemantauan Peralatan |

#### Objektif Pembelajaran Sesi A-1

Pada akhir sesi ini, pelatih akan berjaya:
1. Mencipta dan mengkonfigurasi Azure IoT Hub (atau AWS IoT Core) untuk menerima data sensor
2. Mendaftarkan peranti IoT simulasi dan mendapatkan connection string
3. Menjalankan skrip Python untuk menghantar data sensor simulasi ke platform cloud
4. Mengesahkan bahawa data sensor diterima dan dipaparkan dalam platform

#### Jadual Aktiviti P&P Sesi A-1

| Masa | Tajuk | Aktiviti P&P | Bahan/ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:15 (15 min) | Taklimat Keselamatan dan Orientasi Sesi | Pensyarah menerangkan peraturan keselamatan digital. Maklumkan: dalam sesi ini kita menggunakan persekitaran simulasi — tiada data kilang sebenar. Bahagi pelatih kepada pasangan. Semak persediaan: Python, pip, akaun Azure. | Senarai semak persediaan | — |
| 0:15–1:15 (60 min) | Persediaan Azure IoT Hub — Panduan Berpandu | Pensyarah membimbing seluruh kelas langkah demi langkah untuk mencipta IoT Hub (ikut KK-01 Langkah 2). **Pensyarah menunjukkan** pada projektor; pelatih mengikut pada komputer masing-masing. Hentikan setiap langkah untuk memastikan semua pelatih berjaya sebelum meneruskan. | Komputer lab, projektor, tutorial Azure | Semak: Adakah IoT Hub berjaya dicipta? |
| 1:15–1:45 (30 min) | Pendaftaran Peranti IoT | Pelatih mendaftarkan peranti IoT simulasi mereka (KK-01 Langkah 2c). Salin connection string. Pensyarah membantu pelatih yang menghadapi masalah. | Komputer lab | Semak: Connection string disalin? |
| 1:45–1:55 (10 min) | **REHAT** | | | |
| 1:55–2:25 (30 min) | Pasang Keperluan Python dan Semak Skrip | Pelatih memasang `azure-iot-device` library. Pensyarah menerangkan skrip `simulate_sensor.py` (KK-01 Langkah 3) — bukan menjalankannya lagi, tetapi memahami setiap bahagian: fungsi penjanaan data, parameter yang boleh diubah. | KK-01 (cetakan), komputer | Soalan pemahaman skrip |
| 2:25–3:25 (60 min) | Jalankan Skrip Simulasi Sensor | Pelatih memasukkan connection string mereka ke dalam skrip dan menjalankannya (KK-01 Langkah 3b–3c). Pantau output di terminal. Sahkan mesej diterima oleh Azure IoT Hub. Pensyarah berjalan dari komputer ke komputer untuk membantu. | Komputer lab | Semak: Bilangan mesej diterima dalam 5 minit |
| 3:25–3:35 (10 min) | **REHAT** | | | |
| 3:35–5:05 (90 min) | Bina Dashboard Pemantauan (Pilihan A atau B) | Pelatih membina dashboard dalam Azure Data Explorer atau Power BI (KK-01 Langkah 4). **Panel minimum yang diperlukan:** (1) suhu masa nyata, (2) getaran masa nyata, (3) status semasa. Pensyarah berjalan dan membantu. Kumpulkan tangkapan skrin "Normal" status semasa data simulasi normal (timestamp < 120). | Komputer lab, KK-01 (cetakan) | Tangkapan skrin dashboard Normal |
| 5:05–5:15 (10 min) | **REHAT** | | | |
| 5:15–6:45 (90 min) | Konfigurasi Ambang Amaran dan Ujian | Pelatih mengkonfigurasi tiga tahap amaran (Normal/Amaran/Kritikal) dalam dashboard (KK-01 Langkah 4a). Kemudian ubah `DEGRADATION_RATE = 0.15` dan jalankan semula skrip untuk mencetuskan amaran (Langkah 5). Kumpulkan tangkapan skrin "Amaran/Kritikal" status. | Komputer lab | Tangkapan skrin Amaran/Kritikal |
| 6:45–7:45 (60 min) | Penyediaan Dokumen Konfigurasi | Pelatih menyediakan dokumen konfigurasi sistem untuk handover (KK-01 Langkah 6). Pastikan semua maklumat yang diperlukan disertakan. | Microsoft Word/Google Docs | Semak dokumen konfigurasi |
| 7:45–8:00 (15 min) | Rumusan dan Simpan Kerja | Pastikan semua fail disimpan. Ambil tangkapan skrin akhir. Pastikan Azure IoT Hub sumber dipadam atau dimatikan untuk mengelak caj. Pensyarah mengumpulkan Answer Sheet Bahagian 1–4. | — | Tanda tangan kehadiran |

---

### Sesi A-2: KK-01 Bahagian 2 dan Mula KK-02 — Analisis Data Awal (8 Jam)
**Merangkumi baki AK 2 dan permulaan AK 3**

| Komponen | Butiran |
|---|---|
| **Masa** | 8 jam (480 minit) |
| **Tajuk Sesi** | Penyelesaian Konfigurasi Amaran, Muatkan Dataset, dan Analisis Data Awal |

#### Objektif Pembelajaran Sesi A-2

Pada akhir sesi ini, pelatih akan berjaya:
1. Melengkapkan semua bahagian KK-01 termasuk dokumen konfigurasi
2. Memuatkan dataset sensor C02-KK02 dan menjalankan pemeriksaan kualiti data
3. Menghasilkan visualisasi trend semua sensor dan mengenal pasti corak awal
4. Menjalankan model Isolation Forest dan menghasilkan visualisasi anomali

#### Jadual Aktiviti P&P Sesi A-2

| Masa | Tajuk | Aktiviti P&P | Bahan/ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:20 (20 min) | Taklimat Sesi dan Selesaikan Tunggakan KK-01 | Pensyarah mengulas keputusan KK-01 — sorot masalah biasa yang dihadapi (masalah Azure, skrip). Pelatih yang belum selesai KK-01 diberi masa 20 minit pertama untuk melengkapkan. | Maklum balas pensyarah | — |
| 0:20–0:30 (10 min) | Agihkan Dataset C02-KK02 | Pensyarah edarkan fail CSV kepada pelatih (USB atau folder bersama). Terangkan struktur dataset dan peristiwa yang dikodkan (hari 1–15 normal, 16–21 kemerosotan, hari ke-21 kegagalan). | CSV dataset, KK-02 (cetakan) | — |
| 0:30–1:15 (45 min) | KK-02 Langkah 1 — Muatkan dan Periksa Dataset | Pelatih membuka Jupyter Notebook baharu. Jalankan kod Langkah 1 dari KK-02. Isi Answer Sheet Bahagian 1: bilangan rekod, nilai hilang, statistik deskriptif. Pensyarah berjalan untuk membantu. | Jupyter Notebook, komputer | Semak Answer Sheet Bahagian 1 |
| 1:15–1:25 (10 min) | **REHAT** | | | |
| 1:25–2:55 (90 min) | KK-02 Langkah 2 — Visualisasi Trend Sensor | Pelatih menjalankan kod Langkah 2 dari KK-02 untuk menghasilkan grafik trend 4 sensor. **Perbincangan berpasangan (15 minit):** Setiap pasangan menghuraikan corak yang mereka lihat — pada hari ke-berapa kemerosotan bermula? Adakah suhu atau getaran yang berubah lebih awal? Isi Answer Sheet Bahagian 2. | Jupyter Notebook, grafik dihasilkan | Semak tangkapan skrin trend; Answer Sheet Bahagian 2 |
| 2:55–3:05 (10 min) | **REHAT** | | | |
| 3:05–4:35 (90 min) | KK-02 Langkah 3 — Isolation Forest (Bahagian 1) | Pelatih menjalankan kod Isolation Forest dari KK-02 Langkah 3. Hasilkan visualisasi anomali. Isi Answer Sheet Bahagian 3: bilangan anomali, kadar bertindih dengan kegagalan sebenar, false positives. Pensyarah menjelaskan output kepada kumpulan yang memerlukan bantuan. | Jupyter Notebook, KK-02 (cetakan) | Semak visual anomali; Answer Sheet Bahagian 3 |
| 4:35–4:45 (10 min) | **REHAT** | | | |
| 4:45–5:45 (60 min) | Perbincangan dan Interpretasi Anomali | **Perbincangan kelas (30 minit):** Pensyarah meminta 3–4 pasangan membentangkan temuan mereka — berapa anomali yang dikesan, adakah model berjaya mengesan kemerosotan sebelum kegagalan hari ke-21? Bincang perbezaan keputusan antara pasangan dan sebab-sebabnya. | Projektor (pasangan terpilih paparkan notebook) | Penilaian lisan |
| 5:45–6:45 (60 min) | KK-02 Langkah 4 — Pengiraan OEE (Bahagian 1: Availability dan Performance) | Pelatih menjalankan pengiraan OEE secara manual (KK-02 Langkah 4a–4d). Pensyarah berjalan dan menyemak setiap langkah. Pelatih mesti menunjukkan semua langkah dalam Answer Sheet. | Answer Sheet KK-02 Bahagian 4, kalkulator | Semak pengiraan Availability dan Performance |
| 6:45–7:45 (60 min) | KK-02 Langkah 4 — Pengiraan OEE (Bahagian 2: Quality, OEE, dan OEE selepas PdM) | Pelatih melengkapkan pengiraan Quality, OEE, dan anggaran OEE selepas PdM (4e–4g). Semak aritmetik dilakukan bersama pensyarah bagi setiap pasangan. | Answer Sheet KK-02, kalkulator | Semak pengiraan Quality, OEE, OEE selepas PdM |
| 7:45–8:00 (15 min) | Simpan Kerja dan Rumusan | Pelatih menyimpan notebook. Pensyarah merumuskan sesi dan maklumkan tentang Sesi A-3. | — | — |

---

### Sesi A-3: KK-02 Penyelesaian — ROI dan Laporan Penyelenggaraan (7 Jam)
**Merangkumi baki AK 3 dan AK 4 (pengiraan ROI)**

| Komponen | Butiran |
|---|---|
| **Masa** | 7 jam (420 minit) |
| **Tajuk Sesi** | Pengiraan ROI, Penyusunan Laporan Cadangan Penyelenggaraan, dan Persiapan Pembentangan |

#### Objektif Pembelajaran Sesi A-3

Pada akhir sesi ini, pelatih akan berjaya:
1. Mengira ROI penyelenggaraan ramalan dengan lengkap menggunakan dataset KK-02
2. Menyusun laporan cadangan penyelenggaraan yang profesional dalam format yang ditetapkan
3. Menyediakan pembentangan ringkas temuan analisis untuk sesi A-4

#### Jadual Aktiviti P&P Sesi A-3

| Masa | Tajuk | Aktiviti P&P | Bahan/ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:15 (15 min) | Ulasan dan Sambungan dari Sesi A-2 | Pensyarah mengulas jawapan OEE dari sesi sebelumnya. Kenal pasti kesilapan pengiraan yang biasa. | Slaid ringkasan OEE | — |
| 0:15–1:30 (75 min) | KK-02 Langkah 5 — Pengiraan ROI | Pelatih menjalankan pengiraan ROI langkah demi langkah (KK-02 Langkah 5a–5e). Pensyarah berjalan menyemak. **Semakan kelas (15 minit):** Pensyarah memilih 2–3 pasangan secara rawak untuk menunjukkan pengiraan mereka di depan kelas. Kelas menyemak bersama. | Answer Sheet KK-02 Bahagian 5, kalkulator | Semak pengiraan ROI; Payback Period |
| 1:30–1:40 (10 min) | **REHAT** | | | |
| 1:40–3:40 (120 min) | KK-02 Langkah 6 — Laporan Cadangan Penyelenggaraan | Pelatih menyusun laporan cadangan penyelenggaraan menggunakan struktur dari KK-02 Langkah 6 dalam Microsoft Word atau Google Docs. Pensyarah memberikan bimbingan: (a) kepentingan membezakan anggaran dari fakta, (b) cara menulis cadangan yang spesifik dan boleh dilaksanakan, (c) format profesional laporan. | Microsoft Word / Google Docs, KK-02 (cetakan), laptop | Semak draf laporan |
| 3:40–3:50 (10 min) | **REHAT** | | | |
| 3:50–4:50 (60 min) | Semakan Rakan Sejawat (Peer Review) Laporan | Setiap pasangan bertukar laporan dengan pasangan lain. Semak menggunakan senarai semak yang disediakan: (1) Adakah semua 5 bahagian ada? (2) Adakah cadangan spesifik? (3) Adakah ROI dikira dengan betul? (4) Adakah anggaran dibezakan dari fakta? Beri maklum balas bertulis. | Senarai semak peer review (disediakan pensyarah) | Penilaian rakan sejawat |
| 4:50–5:50 (60 min) | Penambahbaikan Laporan Berdasarkan Maklum Balas | Pelatih menambah baik laporan mereka berdasarkan maklum balas rakan sejawat. | Microsoft Word, maklum balas peer review | — |
| 5:50–6:20 (30 min) | Persiapan Pembentangan Akhir | Setiap pasangan menyediakan pembentangan ringkas (5 minit): (1) Temuan utama analisis anomali, (2) OEE sebelum dan selepas PdM, (3) ROI dan Payback Period, (4) Satu cadangan tindakan paling kritikal. | PowerPoint atau lakaran nota | — |
| 6:20–7:00 (40 min) | Semakan Dokumen Akhir dan Serahan | Semak semua dokumen yang perlu diserahkan: Answer Sheet (lengkap), Notebook Jupyter (berjalan), Laporan (PDF atau Word), tangkapan skrin. Perbaiki sebarang kekurangan sebelum sesi A-4. | Senarai semak penghantaran | Senarai semak penghantaran |

---

### Sesi A-4: Pembentangan Akhir dan Penilaian Prestasi (5 Jam)
**Merangkumi penilaian keseluruhan AK 1–4**

| Komponen | Butiran |
|---|---|
| **Masa** | 5 jam (300 minit) |
| **Tajuk Sesi** | Pembentangan Akhir, Penilaian Prestasi, dan Refleksi Program |

#### Objektif Pembelajaran Sesi A-4

Pada akhir sesi ini, pelatih akan berjaya:
1. Menyampaikan temuan analisis PdM secara profesional kepada pensyarah (bertindak sebagai "pengurus kilang")
2. Menjawab soalan teknikal tentang pilihan metodologi dan keputusan ROI
3. Menerima maklum balas penilaian dan refleksi pembelajaran

#### Jadual Aktiviti P&P Sesi A-4

| Masa | Tajuk | Aktiviti P&P | Bahan/ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:20 (20 min) | Taklimat Penilaian dan Persediaan Akhir | Pensyarah menerangkan format penilaian: setiap pasangan membentangkan 5 minit + soalan jawab 5 minit. Pelatih diberi masa 20 minit terakhir untuk persediaan. | Jadual pembentangan | — |
| 0:20–3:20 (180 min) | Pembentangan dan Soalan Jawab — 10 Pasangan | Setiap pasangan diberi 10 minit: (5 minit pembentangan + 5 minit soalan dari pensyarah). **Soalan yang akan ditanya:** (1) "Mengapa anda memilih parameter ambang ini?" (2) "Apa yang model AI anda kesan — dan adakah anda percaya hasilnya?" (3) "Jika pengurangan downtime sebenar hanya 20%, bagaimana ROI anda berubah?" (4) "Apakah risiko jika kilang tidak melaksanakan PdM ini?" | Slaid pembentangan, laptop, projektor | PA (Kertas Penilaian Prestasi) — semua 4 Aktiviti Kerja |
| 3:20–3:30 (10 min) | **REHAT** | | | |
| 3:30–4:00 (30 min) | Sesi Maklum Balas Penilaian | Pensyarah berkongsi maklum balas umum untuk kelas — kelemahan umum yang diperhatikan, kekuatan yang menonjol. Kekalkan nama pelatih sebagai umum. | — | — |
| 4:00–4:30 (30 min) | Refleksi Pembelajaran Individu | Setiap pelatih mengisi borang refleksi pembelajaran: (1) 3 perkara paling berharga yang dipelajari, (2) 1 kelemahan yang ingin diperbaiki, (3) bagaimana C02 berkaitan dengan kerja mereka di kilang/akan datang, (4) soalan yang masih tidak terjawab. | Borang refleksi pembelajaran (disediakan pensyarah) | Borang refleksi dikumpulkan |
| 4:30–5:00 (30 min) | Penutup C02 dan Pengenalan C03 | Pensyarah merumuskan keseluruhan C02 — hubungkan OEE, sensor, AI platform, model ML, dan ROI sebagai satu sistem yang saling berkaitan. Pratonton C03: AI Vision Quality Control (unit kompetensi seterusnya). Ucapan terima kasih kepada pelatih. | Slaid penutup, pratonton C03 | — |

---

## Ringkasan Jam Amali

| Sesi | Tajuk | Jam |
|---|---|---|
| A-1 | KK-01: Persediaan IoT Hub, Skrip Sensor, dan Dashboard Pemantauan | 8 jam |
| A-2 | KK-01 (selesai) + KK-02 Awal: Muatkan Data, Trend, Isolation Forest, OEE | 8 jam |
| A-3 | KK-02: Pengiraan ROI, Laporan Penyelenggaraan, Peer Review, Persiapan Pembentangan | 7 jam |
| A-4 | Pembentangan Akhir, Penilaian Prestasi (PA), dan Refleksi | 5 jam |
| **JUMLAH** | | **28 jam** |

> **SEMAKAN:** 8 + 8 + 7 + 5 = **28 jam amali** ✓ (70% daripada 40 jam per CU)

---

## Ringkasan Keseluruhan CU C02

| Komponen | Jam |
|---|---|
| Teori (PM-teori: 4 sesi × 3 jam) | 12 jam |
| Amali (PM-amali: 4 sesi) | 28 jam |
| **JUMLAH** | **40 jam** |

> **SEMAKAN AKHIR:** 12 jam teori + 28 jam amali = **40 jam per CU** ✓
> Nisbah Teori : Amali = 12 : 28 = **30% : 70%** ✓ (memenuhi keperluan JPK)

---

## Keperluan Peralatan dan Prasarana

| Keperluan | Spesifikasi | Catatan |
|---|---|---|
| Komputer lab | 1 per pelatih (atau 1 per 2 pelatih untuk kerja berpasangan) | Dengan akses internet, Python 3.10+, Jupyter Notebook |
| Internet | Stabil, sekurang-kurangnya 10 Mbps per pelatih | Untuk akses Azure portal dan senaran data ke cloud |
| Projektor | 1 unit untuk bilik amali | Untuk demo pensyarah dan pembentangan |
| Penyimpanan storan | Folder kongsi atau USB | Untuk agihan dataset C02-KK02-sensor-data.csv |
| Microsoft Word / Google Docs | Berlesen atau akses percuma | Untuk penyusunan laporan |

## Persediaan Pensyarah Sebelum Sesi

- [ ] Wujudkan akaun Azure percubaan (trial) untuk demo pensyarah
- [ ] Muat naik dataset C02-KK02-sensor-data.csv ke folder kongsi / USB
- [ ] Uji skrip `simulate_sensor.py` dengan akaun Azure pensyarah sendiri
- [ ] Sediakan soalan latihan ROI (berbeza daripada contoh KP-03 dan KT-03)
- [ ] Cetak KK-01 dan KK-02 (1 set per pelatih)
- [ ] Sediakan borang peer review dan borang refleksi
- [ ] Sediakan jadual pembentangan Sesi A-4

---

## Catatan Pensyarah

*(Ruang untuk catatan semasa pengajaran amali — pengubahsuaian yang dibuat, isu teknikal yang timbul, pelatih yang memerlukan perhatian tambahan)*

_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
