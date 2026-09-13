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

## PELAN MENGAJAR (TEORI)

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | MFG-AI-3:2026 AI FOR SMART MANUFACTURING SPECIALIST |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | MFG-AI-3:2026-C03 AI VISION QUALITY CONTROL AND DEFECT DETECTION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. DEPLOY AN AI VISION INSPECTION SYSTEM (SISTEM PEMERIKSAAN PENGLIHATAN AI) FOR PRODUCT DEFECT IDENTIFICATION<br>2. ANNOTATE A DATASET AND TRAIN A CUSTOM AI MODEL (MODEL AI TERSUAI) FOR A SPECIFIC PRODUCT CATEGORY<br>3. INTEGRATE AI VISION INSPECTION DATA WITH A MANUFACTURING EXECUTION SYSTEM (MES) FOR REAL-TIME QUALITY TRACEABILITY<br>4. EVALUATE AI VISION SYSTEM PERFORMANCE AGAINST MANUAL INSPECTION BENCHMARKS |
| NO. KOD | MFG-AI-3:2026-C03/PM-T(1/1) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** Pelan Mengajar Teori — AI Vision Quality Control and Defect Detection

**TUJUAN:** Panduan pelaksanaan sesi pengajaran teori sepanjang 12 jam untuk unit kompetensi C03, merangkumi tiga topik pengetahuan (KP-01, KP-02, KP-03) dan penilaian pengetahuan.

<!-- /JPK_ENVELOPE_v1 -->

---

## Maklumat Pengajaran

| Medan | Nilai |
|---|---|
| **Nama Pengajar** | *(Kosong — diisi oleh pusat latihan)* |
| **Jumlah Jam Teori** | **12 jam** |
| **Nisbah T/P** | 30% Teori / 70% Amali (12 jam / 28 jam) |
| **Saiz Kelas** | Maksimum 20 pelatih |
| **Mod Penyampaian** | Penyampaian bersemuka + demonstrasi langsung + perbincangan kumpulan |

---

## Pelan Sesi / Session Plan

| Sesi | Masa (jam) | Masa Kumulatif | Tajuk Sesi | Objektif Pembelajaran | Aktiviti P&P | Bahan / ABBM | Penilaian |
|---|---|---|---|---|---|---|---|
| **1** | 1.5 j | 1.5 j | **Pengenalan AI Vision Inspection dan Had Pemeriksaan Manual** (KP-01 Seksyen 1) | Pelatih berupaya menyatakan 5 had utama pemeriksaan manual dan menerangkan komponen sistem penglihatan mesin industri | Pembentangan + Perbincangan: "Berapa banyak kecacatan yang boleh manusia kesan dalam 8 jam berterusan?" Tayangan video barisan pengeluaran berhenti kerana kesilapan pemeriksaan | Slaid PowerPoint; video YouTube barisan pembuatan (sumber terbuka); whiteboard | Soal jawab lisan: namakan 4 komponen sistem penglihatan mesin |
| **2** | 1.5 j | 3.0 j | **Pemilihan Kamera dan Pengiraan Resolusi** (KP-01 Seksyen 2) | Pelatih berupaya mengira GSD dan resolusi minimum yang diperlukan untuk mengesan kecacatan bersaiz tertentu | Pengajaran langsung formula GSD; pengiraan bersama di whiteboard; latihan cepat: 3 senario pengiraan berbeza (tekstil, PCB, makanan) | Slaid dengan formula; whiteboard; kalkulator; handout jadual jenis kamera | Latihan pengiraan dalam kelas — 2 soalan (5 minit); pengajar semak secara lisan |
| **3** | 1.5 j | 4.5 j | **Geometri Pencahayaan: Brightfield, Darkfield, Backlight, Dome** (KP-01 Seksyen 3) | Pelatih berupaya memilih geometri pencahayaan yang sesuai berdasarkan jenis kecacatan | Pembentangan visual setiap geometri; demonstrasi interaktif: tayangkan gambar kecacatan yang sama dengan pencahayaan berbeza — pelatih kenal pasti perbezaan; perbincangan "mengapa darkfield mendedahkan calar?" | Slaid dengan imej perbandingan pencahayaan berkualiti tinggi; contoh imej kecacatan sebenar (dicapai dari sumber terbuka berlesenkan CC); kertas latihan pemilihan pencahayaan | Kad aktiviti: beri 6 senario kecacatan; pelatih pilih pencahayaan betul (3 minit) — perbincangan bersama selepas itu |
| **4** | 1.5 j | 6.0 j | **Tiga Tugas CV dan Mekanisme CNN** (KP-01 Seksyen 4 & 5) | Pelatih berupaya membezakan pengelasan imej, pengesanan objek, dan segmentasi; menerangkan aliran data dalam CNN (conv → ReLU → pool → FC) | Tayangan animasi CNN (3Blue1Brown atau serupa); perbandingan output tiga tugas pada imej PCB yang sama; perbincangan: "senario mana memerlukan tugas apa?" | Slaid animasi CNN; kertas perbandingan tiga tugas; whiteboard untuk lakaran senibina CNN | Soal jawab: pelatih diberi senario → pilih tugas CV yang sesuai dengan justifikasi lisan |
| **5** | 1.0 j | 7.0 j | **Taksonomi Kecacatan dan Transfer Learning** (KP-01 Seksyen 6 + ulangkaji) | Pelatih berupaya membina taksonomi kecacatan bermakna dan menerangkan manfaat transfer learning | Kerja kumpulan: kumpulan 4 orang bina taksonomi kecacatan untuk industri yang diberikan (PCB / sarung tangan / makanan); pembentangan ringkas setiap kumpulan | Kertas kerja kumpulan; contoh taksonomi dari industri (KP-01); whiteboard | Pembentangan ringkas kumpulan (3 minit/kumpulan); maklum balas dari pengajar dan rakan |
| **6** | 1.5 j | 8.5 j | **Platform AI Vision dan Keperluan Dataset** (KP-02 Seksyen 1 & 2) | Pelatih berupaya membandingkan platform Cognex, Landing AI, Roboflow, Google Vision AI; menerangkan keperluan kepelbagaian dataset | Demonstrasi langsung Roboflow pada komputer pengajar (projek sebenar dipaparkan); perbincangan "Kenapa 50 imej tidak cukup?"; demo singkat antara muka Landing AI (jika akses ada) | Komputer pengajar dengan penyampai; Akaun demo Roboflow; jadual perbandingan platform (KP-02); handout keperluan dataset | Soal jawab: "Kilang SME Malaysia dengan bajet terhad — platform mana yang anda pilih dan mengapa?" |
| **7** | 1.5 j | 10.0 j | **Matriks Penilaian Model: TP, FP, FN, TN, Precision, Recall, F1** (KP-02 Seksyen 3) | Pelatih berupaya mendefinisikan keempat-empat sel confusion matrix; mengira dan mentafsir Precision, Recall, F1 | Pengajaran langsung dengan analogi: "bayangkan doktor yang mendiagnosis barah" untuk menerangkan FN vs. FP; tiga senario pengiraan berbeza dari data sintetik; pelatih kira sendiri lalu semak bersama | Slaid Confusion Matrix dengan warna; handout dataset sintetik 3 senario; kalkulator | Pengiraan dalam kelas: data diberikan → pelatih kira Precision, Recall, F1 → semak bersama selepas 5 minit |
| **8** | 1.0 j | 11.0 j | **Seni Bina MES, Corak Integrasi, dan Traceability ISO 9001** (KP-03 Seksyen 1–4) | Pelatih berupaya menerangkan lapisan ISA-95, empat corak integrasi, dan keperluan Klausa 8.5.2 | Pembentangan rajah hierarki ISA-95; perbandingan REST API vs. OPC-UA vs. MQTT; perbincangan senario traceability (kes carian rekod produk cacat selepas aduan pelanggan) | Slaid hierarki ISA-95; jadual perbandingan corak integrasi (KP-03); contoh rekod MES (jadual) | Soal jawab: "Kilang dengan MES SAP dan SCADA OPC-UA — corak mana paling sesuai?" |
| **9** | 1.0 j | 12.0 j | **Ulangkaji, Soal Jawab, dan Persediaan KA** | Pelatih bersedia untuk penilaian pengetahuan (KA); kejelasan semua konsep dikukuhkan | Ulangkaji dengan "Quick Quiz" 10 soalan aneka pilihan dari KA (bukan soalan peperiksaan sebenar — soalan latihan yang berbeza); soal jawab terbuka; pelatih boleh tanya mana-mana konsep yang tidak jelas | Soalan ulangkaji bercetak; whiteboard untuk penyelesaian masalah pengiraan; | Penilaian formatif: 10 soalan MCQ latihan — pelatih nilai sendiri; pengajar terangkan jawapan |

---

## Pengesahan Jumlah Jam

| Sesi | Jam |
|---|---|
| Sesi 1 | 1.5 |
| Sesi 2 | 1.5 |
| Sesi 3 | 1.5 |
| Sesi 4 | 1.5 |
| Sesi 5 | 1.0 |
| Sesi 6 | 1.5 |
| Sesi 7 | 1.5 |
| Sesi 8 | 1.0 |
| Sesi 9 | 1.0 |
| **JUMLAH** | **12.0 jam ✓** |

---

## Bahan Pengajaran dan Pembelajaran (ABBM) yang Diperlukan

| Bahan | Tujuan | Sumber / Nota |
|---|---|---|
| Komputer pengajar dengan projektor | Paparan slaid dan demonstrasi langsung | Penyediaan pusat latihan |
| Akses internet (kelajuan mencukupi) | Demo Roboflow, tayangan video YouTube | WiFi kelas |
| Slaid PowerPoint C03 (disediakan berasingan) | Penyampaian teori berstruktur | Pengajar sediakan |
| Handout KP-01, KP-02, KP-03 (dicetak) | Rujukan pelatih semasa sesi | Pusat latihan cetak sebelum kelas |
| Imej kecacatan industri (sumber terbuka) | Demonstrasi visual perbezaan pencahayaan | Cari gambar berlesen CC BY/CC0 |
| Video barisan pengeluaran (YouTube/vimeo) | Konteksualisasi keperluan pemeriksaan | Pastikan ketersediaan offline jika WiFi tidak stabil |
| Kalkulator (saintifik atau telefon) | Pengiraan GSD, Precision, Recall | Pelatih bawa sendiri atau disediakan |
| Kertas kerja kumpulan (dicetak) | Aktiviti taksonomi kecacatan | Cetak 5 set (4 orang/kumpulan) |
| Akaun demo Roboflow | Demonstrasi langsung antara muka | Pengajar daftar akaun percuma |
| Whiteboard dan marker | Penulisan formula, rajah, pengiraan bersama | Penyediaan pusat latihan |

---

## Nota Pengajar / Instructor Notes

1. **Sesi 2 (Pengiraan GSD):** Gunakan contoh kilang Malaysia yang nyata (Penang PCB, Muar sarung tangan getah) untuk menjadikan pengiraan lebih relevan. Minta pelatih teka dahulu sebelum menunjukkan formula — ini mengaktifkan pemikiran kritis.

2. **Sesi 3 (Pencahayaan):** Jika boleh, bawa sampel fizikal: kepingan aluminium berkilat, kertas putih, dan sumber cahaya sudut rendah (lampu suluh dari sudut). Demonstrasi langsung lebih berkesan daripada slaid sahaja.

3. **Sesi 7 (Matriks Penilaian):** Ini adalah sesi paling kritikal dari segi konseptual. Berikan masa cukup untuk pengiraan. Pastikan pelatih memahami *mengapa* FN lebih bahaya daripada FP dalam konteks keselamatan produk — bukan hanya hafal formula.

4. **Sesi 8 (MES/Integrasi):** Jika ada pelatih yang sudah berpengalaman dengan sistem SCADA atau MES, minta mereka berkongsi pengalaman — ini memperkaya perbincangan.

5. **Pengiraan dalam Kelas:** Beri masa realistik untuk pengiraan (minimum 5 minit per soalan). Jangan tergesa-gesa — pemahaman lebih penting daripada kecepatan pada peringkat ini.

---

## Tandatangan Pengajar

| | |
|---|---|
| **Nama Pengajar:** | *(Kosong untuk ditandatangani)* |
| **Tandatangan:** | |
| **Tarikh:** | |
