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
| KOD DAN TAJUK UNIT KOMPETENSI | MFG-AI-3:2026-C03 AI VISION QUALITY CONTROL AND DEFECT DETECTION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. DEPLOY AN AI VISION INSPECTION SYSTEM (SISTEM PEMERIKSAAN PENGLIHATAN AI) FOR PRODUCT DEFECT IDENTIFICATION<br>2. ANNOTATE A DATASET AND TRAIN A CUSTOM AI MODEL (MODEL AI TERSUAI) FOR A SPECIFIC PRODUCT CATEGORY<br>3. INTEGRATE AI VISION INSPECTION DATA WITH A MANUFACTURING EXECUTION SYSTEM (MES) FOR REAL-TIME QUALITY TRACEABILITY<br>4. EVALUATE AI VISION SYSTEM PERFORMANCE AGAINST MANUAL INSPECTION BENCHMARKS |
| NO. KOD | MFG-AI-3:2026-C03/PM-A(1/1) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** Pelan Mengajar Amali — AI Vision Quality Control and Defect Detection

**TUJUAN:** Panduan pelaksanaan sesi amali sepanjang 28 jam untuk unit kompetensi C03, berstruktur mengikut keempat-empat Aktiviti Kerja, daripada penyediaan dataset dan latihan model AI (KK-01) hingga reka bentuk integrasi MES dan penilaian prestasi (KK-02).

<!-- /JPK_ENVELOPE_v1 -->

---

## Maklumat Pengajaran

| Medan | Nilai |
|---|---|
| **Nama Pengajar** | *(Kosong — diisi oleh pusat latihan)* |
| **Jumlah Jam Amali** | **28 jam** |
| **Nisbah T/P** | 30% Teori (12 jam) / 70% Amali (28 jam) |
| **Saiz Kelas** | Maksimum 20 pelatih (boleh bekerja secara individu atau berpasangan) |
| **Mod Penyampaian** | Amali berasaskan komputer; bimbingan pengajar; kerja projek individu |
| **Keperluan Perkakasan** | PC/laptop per pelatih; akses internet; akaun Google Colab/Roboflow |

---

## Pelan Sesi Amali / Practical Session Plan

| Sesi | Masa (jam) | Masa Kumulatif | Tajuk Sesi | Aktiviti Kerja (AK) | Objektif Pembelajaran | Aktiviti Amali | Bahan / ABBM | Penilaian / Pemerhatian |
|---|---|---|---|---|---|---|---|---|
| **P1** | 2.0 j | 2.0 j | **Orientasi Lab dan Persediaan Persekitaran** | AK1 (persediaan) | Pelatih berjaya menyediakan persekitaran Python dengan `ultralytics` dan Roboflow terinstal; akaun dibuat | Pasang pakej: `pip install ultralytics roboflow -q` dalam virtual env; uji import; daftar akaun Roboflow dan Google Colab; pengesahan GPU dalam Colab | Komputer lab; internet; slaid arahan persediaan; Google Colab | Pengajar semak setiap pelatih — pastikan GPU tersedia dalam Colab dan `from ultralytics import YOLO` berjalan tanpa ralat |
| **P2** | 2.0 j | 4.0 j | **Pemilihan Senario Produk dan Pembinaan Taksonomi Kecacatan** | AK1 | Pelatih membina taksonomi kecacatan yang lengkap dengan minimum 3 kelas bermakna untuk produk yang diberikan | Pelatih terima senario (A/B/C/D dari KK-01); kumpulan berkaitan produk yang sama duduk bersama dan berbincang tentang kecacatan yang mungkin; setiap pelatih tulis taksonominya sendiri (individu); pengajar semak dan beri maklum balas | Senarai senario (KK-01 Bahagian A); kertas kerja taksonomi; rujukan imej kecacatan produk | Pengajar menilai taksonomi mengikut kriteria KK-01 Jadual T1; maklum balas individu sebelum meneruskan |
| **P3** | 3.0 j | 7.0 j | **Pengumpulan Imej dan Anotasi Bounding Box — Bahagian 1** | AK2 | Pelatih menganotasi minimum 50 imej dengan bounding box yang tepat | Muat naik imej ke Roboflow; buat projek baru; mula proses anotasi — pengajar berjalan dan semak ketepatan kotak pembatas pelatih pertama 10 imej setiap pelatih; perbetulkan sebelum meneruskan | Akaun Roboflow; imej dataset (disediakan pengajar atau diambil sendiri); panduan anotasi bercetak (KK-01) | Pengajar periksa 10 imej anotasi pertama setiap pelatih — ketepatan bounding box dan konsistensi nama kelas |
| **P4** | 3.0 j | 10.0 j | **Pengumpulan Imej dan Anotasi Bounding Box — Bahagian 2 + Augmentasi** | AK2 | Pelatih menyelesaikan minimum 100 imej dianotasi; augmentasi dataset dikonfigurasi | Teruskan anotasi sehingga mencapai minimum 100 imej; konfigurasi augmentasi (minimum 3 teknik); jana dataset dalam format YOLOv8 | Roboflow; panduan augmentasi (KK-01 Langkah B4) | Semakan pengajar: bilangan imej dan saiz fail dataset yang dijana; pastikan split 70/20/10 betul |
| **P5** | 2.0 j | 12.0 j | **Latihan Model YOLOv8 — Persiapan dan Permulaan** | AK2 | Pelatih berjaya memuat turun dataset dari Roboflow dan memulakan latihan model YOLOv8 | Tulis dan jalankan kod Python muat turun dataset; mulakan latihan YOLOv8n atau YOLOv8s; pastikan GPU aktif; pantau loss dalam log Colab | Google Colab; akaun Roboflow; kod Python dari KK-01 Langkah C2 & C3 | Pengajar semak kod setiap pelatih sebelum jalankan latihan — elak ralat kod yang menyebabkan sesi GPU terbuang |
| **P6** | 2.0 j | 14.0 j | **Latihan Model YOLOv8 — Pemantauan dan Penyimpanan Model** | AK2 | Pelatih memahami cara membaca loss curves; model terbaik disimpan dengan betul | Pantau log latihan semasa epoch berjalan; baca dan tafsir training loss, validation loss; apabila latihan selesai, salin model ke Google Drive; jalankan kod penilaian `model.val()` | Google Colab; Google Drive; kod Python dari KK-01 Langkah C4 | Pengajar semak bahawa model best.pt tersimpan dan kod val() menghasilkan output metrik |
| **P7** | 2.0 j | 16.0 j | **Inferens pada Imej Ujian dan Confusion Matrix Manual** | AK4 | Pelatih menjalankan inferens pada set ujian; melengkapkan Confusion Matrix dengan nilai TP, FP, FN, TN yang betul | Jalankan inferens pada 30+ imej ujian; semak setiap imej secara visual dan bandingkan dengan label sebenar; isi Confusion Matrix manual dalam KK-01 Jadual T4 | Google Colab; imej ujian; helaian Confusion Matrix (KK-01 Jadual T4) | Pengajar semak Confusion Matrix — pastikan pelatih faham perbezaan TP vs. FP dan FN vs. TN dengan betul |
| **P8** | 2.0 j | 18.0 j | **Pengiraan Metrik dan Penilaian Prestasi** | AK4 | Pelatih mengira Precision, Recall, F1 dengan betul dan mentafsir implikasi perniagaan | Kira Precision, Recall, F1 secara manual dari Confusion Matrix; bandingkan dengan nilai dari `model.val()`; tafsir — adakah model cukup baik untuk barisan pengeluaran sebenar?; jawab soalan refleksi KK-01 | Helaian pengiraan (KK-01); kalkulator | Pengajar semak pengiraan pelatih — pastikan formula betul dan tafsiran relevan dengan konteks industri |
| **P9** | 2.0 j | 20.0 j | **Reka Bentuk Rajah Seni Bina Integrasi AI–MES** | AK3 | Pelatih melukis rajah seni bina integrasi yang lengkap dan berlabel dengan semua lapisan | Buka draw.io; reka bentuk rajah mengikut spesifikasi KK-02 Langkah A1; pastikan semua komponen hadir; eksport sebagai PNG | draw.io (diagrams.net); panduan komponen rajah (KK-02); contoh rajah (KP-03) | Pengajar semak rajah: adakah semua lapisan ada? Adakah protokol dilabel pada setiap sambungan? |
| **P10** | 2.0 j | 22.0 j | **Reka Bentuk Skema Rekod MES dan Peraturan Amaran** | AK3 | Pelatih mendefinisikan skema rekod kualiti minimum 9 medan; mereka bentuk minimum 4 peraturan amaran yang boleh diukur | Isi Jadual B1 dan B2 dalam KK-02; gunakan data KTPJ (KK-02 Data Senario) sebagai rujukan | Helaian KK-02 Bahagian B; data senario KTPJ | Pengajar semak: adakah semua medan ada? Adakah peraturan amaran mempunyai keadaan boleh diukur dan tindakan konkrit? |
| **P11** | 2.0 j | 24.0 j | **Pengiraan Keperluan Sistem dan Perbandingan Prestasi** | AK3 & AK4 | Pelatih mengira keperluan bandwidth, storan, dan masa nyata dengan betul; mengira ROI perbandingan AI vs. manual | Isi Jadual C1 dan D1 dalam KK-02; pengiraan storan imej dan bandwidth; pengiraan ROI; jawab soalan refleksi | Helaian KK-02; kalkulator; data senario KTPJ | Pengajar semak aritmetik: formula betul? Hasil masuk akal? |
| **P12** | 2.0 j | 26.0 j | **Penyediaan Dokumen Spesifikasi Integrasi** | AK3 | Pelatih menyediakan dokumen spesifikasi integrasi 1–2 muka surat yang profesional | Tulis dokumen dalam Word/Google Docs menggunakan template KK-02 Langkah E1; pastikan semua 7 bahagian hadir; API spec ditulis dengan betul | Word / Google Docs; template spesifikasi (KK-02); KP-03 untuk rujukan API spec | Pengajar semak dokumen: adakah semua bahagian ada? Adakah API spec boleh digunakan untuk handoff sebenar? |
| **P13** | 1.0 j | 27.0 j | **Pembentangan dan Semakan Rakan (Peer Review)** | AK3 & AK4 | Pelatih membentangkan keputusan model dan spesifikasi integrasi; menerima maklum balas membina | Setiap pelatih membentangkan dalam 5 minit: (1) prestasi model (Precision/Recall/F1), (2) rajah seni bina, (3) satu cabaran yang dihadapi. Pelatih lain beri satu soalan atau cadangan | Rajah dan dokumen pelatih; projektor atau skrin bersama | Pengajar menilai kejelasan pembentangan dan keupayaan menjawab soalan |
| **P14** | 1.0 j | 28.0 j | **Finalisasi Kerja dan Persediaan PA** | AK1–4 | Pelatih menyiapkan semua dokumen; bersedia untuk penilaian prestasi (PA) | Semak dan siapkan semua bahagian KK-01 dan KK-02; muat naik semua fail ke platform yang ditetapkan; pengajar terangkan prosedur penilaian prestasi (PA) | Semua hasil kerja KK-01 dan KK-02; platform submit (Google Drive, portal latihan, dsb.) | Pengajar sahkan penerimaan semua hasil kerja; taklimat PA |

---

## Pengesahan Jumlah Jam Amali

| Sesi | Jam |
|---|---|
| P1 | 2.0 |
| P2 | 2.0 |
| P3 | 3.0 |
| P4 | 3.0 |
| P5 | 2.0 |
| P6 | 2.0 |
| P7 | 2.0 |
| P8 | 2.0 |
| P9 | 2.0 |
| P10 | 2.0 |
| P11 | 2.0 |
| P12 | 2.0 |
| P13 | 1.0 |
| P14 | 1.0 |
| **JUMLAH** | **28.0 jam ✓** |

---

## Pemetaan Sesi ke Aktiviti Kerja

| Aktiviti Kerja | Sesi yang Relevan | Jam |
|---|---|---|
| AK1: Deploy AI Vision Inspection System | P1, P2 | 4.0 j |
| AK2: Annotate Dataset and Train Custom AI Model | P3, P4, P5, P6 | 10.0 j |
| AK3: Integrate AI Vision Data with MES | P9, P10, P11, P12, P13 | 9.0 j |
| AK4: Evaluate AI Vision Performance vs. Manual | P7, P8, P11, P13 | 5.0 j |
| **JUMLAH** | | **28.0 j ✓** |

> **Nota:** Sesi P11 dan P13 merangkumi dua Aktiviti Kerja secara serentak kerana kerja pengiraan dan pembentangan melibatkan kedua-dua AK3 dan AK4 secara semula jadi.

---

## Keperluan Teknikal Lab / Technical Lab Requirements

| Item | Spesifikasi Minimum | Keperluan Bilangan |
|---|---|---|
| Komputer / laptop | Windows 10/11 atau macOS; RAM 8 GB minimum (16 GB disyorkan); Python 3.10+ | 1 per pelatih |
| GPU (pilihan terbaik) | NVIDIA GPU dengan CUDA support | 1 per pelatih atau akses Colab |
| Akses internet | Minimum 10 Mbps per pelatih (untuk Roboflow + Colab) | 1 sambungan berkapasiti tinggi untuk kelas |
| Akaun Google | Untuk Google Colab dan Google Drive | 1 per pelatih (pelatih sedia terlebih dahulu) |
| Akaun Roboflow | Percuma — tier Roboflow Free | 1 per pelatih (daftar sebelum P1) |
| Webcam (jika ada) | Sebarang kamera 720p untuk mengambil imej sendiri | 1 per stesen atau berkongsi |

---

## Nota Pengajar / Instructor Notes

1. **Sesi P3–P4 (Anotasi):** Ini adalah bahagian paling membosankan dan paling mudah dilangkau kualiti. Pengajar mesti berjalan sekitar dan secara aktif semak 10 imej pertama setiap pelatih sebelum mereka meneruskan. Anotasi yang tidak konsisten atau tidak tepat akan merosakkan kualiti model dalam P5–P6.

2. **Sesi P5–P6 (Latihan):** Sesi GPU Colab percuma boleh berakhir tidak dijangka. Suruh pelatih simpan model ke Google Drive sebaik sahaja latihan selesai (Langkah C4). Sebagai langkah berjaga-jaga, simpan juga kod Python dalam fail .py berasingan supaya latihan boleh disambung semula.

3. **Masa Latihan:** Latihan YOLOv8n pada GPU T4 dengan 100 imej dan 50 epoch mengambil masa kira-kira 20–40 minit. Ini bermakna P5 boleh diisi dengan penjelasan kod dan P6 adalah semasa latihan berjalan. Manfaatkan masa latihan untuk perbincangan tentang interpretasi loss curve.

4. **Sesi P9 (draw.io):** Sesetengah pelatih mungkin pertama kali menggunakan draw.io. Berikan 10 minit orientasi ringkas alat ini sebelum memulakan aktiviti reka bentuk.

5. **Sesi P13 (Pembentangan):** Hadkan setiap pembentangan kepada 5 minit dengan ketat. 20 pelatih × 5 minit = 100 minit — melebihi masa sesi 60 minit. Pilihan: setiap dua pelatih membentangkan bersama, atau pilih 10 pelatih secara rawak untuk membentangkan.

6. **DOSH/OSHA 1994 reminder:** Walaupun amali ini adalah berasaskan perisian, ingatkan pelatih bahawa dalam persekitaran kilang sebenar, pemasangan kamera dan pendawaian sistem memerlukan pematuhan DOSH/OSHA 1994 — kerja elektrik mesti dilakukan oleh juruteknik berkelayakan.

---

## Tandatangan Pengajar

| | |
|---|---|
| **Nama Pengajar:** | *(Kosong untuk ditandatangani)* |
| **Tandatangan:** | |
| **Tarikh:** | |
