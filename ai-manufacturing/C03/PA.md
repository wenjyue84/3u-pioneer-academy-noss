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

## KERTAS PENILAIAN PRESTASI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | MFG-AI-3:2026 AI FOR SMART MANUFACTURING SPECIALIST |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | MFG-AI-3:2026-C03 AI VISION QUALITY CONTROL AND DEFECT DETECTION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. DEPLOY AN AI VISION INSPECTION SYSTEM (SISTEM PEMERIKSAAN PENGLIHATAN AI) FOR PRODUCT DEFECT IDENTIFICATION<br>2. ANNOTATE A DATASET AND TRAIN A CUSTOM AI MODEL (MODEL AI TERSUAI) FOR A SPECIFIC PRODUCT CATEGORY<br>3. INTEGRATE AI VISION INSPECTION DATA WITH A MANUFACTURING EXECUTION SYSTEM (MES) FOR REAL-TIME QUALITY TRACEABILITY<br>4. EVALUATE AI VISION SYSTEM PERFORMANCE AGAINST MANUAL INSPECTION BENCHMARKS |
| NO. KOD | MFG-AI-3:2026-C03/PA(1/1) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU MUDA (Light Blue) |

**TAJUK:** Penilaian Prestasi — AI Vision Quality Control and Defect Detection

**TUJUAN:** Menilai pencapaian kompetensi amali pelatih merentasi keempat-empat Aktiviti Kerja CU C03, melalui pemerhatian langsung semasa pelaksanaan KK-01 dan KK-02, serta penilaian hasil kerja yang dihasilkan.

<!-- /JPK_ENVELOPE_v1 -->

---

## Maklumat Pelatih / Trainee Information

| Medan | Nilai |
|---|---|
| **Nama Pelatih** | |
| **No. IC / Passport** | |
| **Kumpulan / Batch** | |
| **Tarikh Penilaian** | |
| **Nama Penilai** | |
| **Lokasi Penilaian** | |

---

## Arahan kepada Penilai / Instructions to Assessor

1. Gunakan senarai semak ini untuk memerhatikan dan menilai prestasi pelatih semasa pelaksanaan KK-01 (Latihan Model AI Vision) dan KK-02 (Reka Bentuk Integrasi AI Vision–MES).
2. Tandakan **✓** (Kompeten) atau **✗** (Tidak Kompeten) untuk setiap elemen dalam Bahagian A.
3. Gunakan skala 1–4 dalam Bahagian B untuk menilai kualiti hasil kerja.
4. Pelatih dianggap KOMPETEN untuk CU ini jika mencapai markah agregat ≥ 70% DAN lulus semua elemen wajib (*) dalam Bahagian A.
5. Penilai tidak boleh memberi bimbingan teknikal semasa penilaian berlangsung.

---

## Bahagian A: Senarai Semak Pemerhatian (Observation Checklist)

### Aktiviti Kerja 1: DEPLOY AN AI VISION INSPECTION SYSTEM FOR PRODUCT DEFECT IDENTIFICATION

*(Diperhatikan semasa KK-01, Bahagian A dan B)*

| No. | Elemen Kompetensi | ✓ / ✗ | Wajib (*) | Pemerhatian |
|---|---|---|---|---|
| 1.1 | Pelatih menyenaraikan komponen fizikal sistem pemeriksaan sebelum memulakan (kamera, kanta, pencahayaan) | | * | |
| 1.2 | Pelatih memilih dan menyatakan justifikasi geometri pencahayaan yang sesuai untuk produk yang diberikan | | | |
| 1.3 | Pelatih mendefinisikan taksonomi kecacatan dengan minimum 3 kelas yang mempunyai nama, penerangan, dan gred | | * | |
| 1.4 | Pelatih membina taksonomi berdasarkan jenis kecacatan yang relevan kepada produk (bukan generik) | | | |
| 1.5 | Pelatih muat naik imej ke Roboflow dengan betul (projek dicipta, format betul) | | | |

**Subtotal AK1: _____ / 5**

---

### Aktiviti Kerja 2: ANNOTATE A DATASET AND TRAIN A CUSTOM AI MODEL FOR A SPECIFIC PRODUCT CATEGORY

*(Diperhatikan semasa KK-01, Bahagian B dan C)*

| No. | Elemen Kompetensi | ✓ / ✗ | Wajib (*) | Pemerhatian |
|---|---|---|---|---|
| 2.1 | Pelatih melukis bounding box dengan tepat merangkumi kawasan kecacatan (margin 2–3 piksel) | | * | |
| 2.2 | Pelatih menganotasi minimum 80 imej dalam masa yang diperuntukkan | | | |
| 2.3 | Pelatih memilih dan mengaktifkan minimum 3 teknik augmentasi data dalam Roboflow | | | |
| 2.4 | Pelatih menetapkan split dataset 70/20/10 (latihan/pengesahan/ujian) dengan betul | | * | |
| 2.5 | Pelatih melatih model YOLOv8 menggunakan kod Python yang betul tanpa ralat kritikal | | * | |
| 2.6 | Pelatih menyimpan model terbaik (best.pt) ke lokasi yang boleh diakses | | | |

**Subtotal AK2: _____ / 6**

---

### Aktiviti Kerja 3: INTEGRATE AI VISION INSPECTION DATA WITH MES FOR REAL-TIME QUALITY TRACEABILITY

*(Diperhatikan semasa KK-02)*

| No. | Elemen Kompetensi | ✓ / ✗ | Wajib (*) | Pemerhatian |
|---|---|---|---|---|
| 3.1 | Pelatih melukis rajah seni bina yang mengandungi semua lapisan: kamera, Edge PC, MES, dan lapisan tindakan | | * | |
| 3.2 | Rajah menunjukkan arah aliran data dengan label protokol yang betul | | | |
| 3.3 | Pelatih mendefinisikan skema rekod kualiti MES dengan minimum 7 medan yang betul | | * | |
| 3.4 | Pelatih mereka bentuk minimum 3 peraturan pencetus amaran yang mempunyai keadaan boleh diukur dan tindakan konkrit | | | |
| 3.5 | Pelatih mengira keperluan storan imej dengan betul menggunakan formula yang ditunjukkan | | | |
| 3.6 | Pelatih menyediakan dokumen spesifikasi integrasi yang mengandungi minimum 5 bahagian | | | |

**Subtotal AK3: _____ / 6**

---

### Aktiviti Kerja 4: EVALUATE AI VISION SYSTEM PERFORMANCE AGAINST MANUAL INSPECTION BENCHMARKS

*(Diperhatikan semasa KK-01 Bahagian D dan KK-02 Bahagian D)*

| No. | Elemen Kompetensi | ✓ / ✗ | Wajib (*) | Pemerhatian |
|---|---|---|---|---|
| 4.1 | Pelatih melengkapkan Confusion Matrix dengan nilai TP, FP, FN, TN yang betul | | * | |
| 4.2 | Pelatih mengira Precision dengan formula yang betul dan menunjukkan langkah pengiraan | | * | |
| 4.3 | Pelatih mengira Recall dengan formula yang betul dan menunjukkan langkah pengiraan | | * | |
| 4.4 | Pelatih mengira F1-Score dengan formula yang betul | | | |
| 4.5 | Pelatih membuat perbandingan prestasi AI vs. pemeriksaan manual yang bermakna dengan data yang disediakan | | | |
| 4.6 | Pelatih mentafsir implikasi perniagaan FN vs. FP dengan tepat (yang mana lebih berbahaya dan mengapa) | | | |

**Subtotal AK4: _____ / 6**

---

**Jumlah Elemen Kompeten (Bahagian A): _____ / 23**

---

## Bahagian B: Penilaian Kualiti Hasil Kerja (Quality of Work Output)

Gunakan skala berikut:
- **4 — Cemerlang:** Melebihi standard; boleh menjadi rujukan
- **3 — Baik:** Memenuhi standard sepenuhnya; sedikit ruang untuk penambahbaikan
- **2 — Memuaskan:** Memenuhi standard minimum; penambahbaikan diperlukan
- **1 — Perlu Usaha:** Tidak mencapai standard minimum; latihan tambahan diperlukan

| No. | Kriteria Hasil Kerja | Skor (1–4) | Ulasan Penilai |
|---|---|---|---|
| B1 | **Taksonomi Kecacatan:** Definisi kelas tepat, gred sesuai untuk konteks industri produk yang diberikan | | |
| B2 | **Kualiti Anotasi Dataset:** Kotak pembatas tepat; anotasi konsisten merentasi semua imej; kepelbagaian data ada | | |
| B3 | **Prestasi Latihan Model:** Latihan berjalan tanpa ralat; epoch selesai; model tersimpan dengan betul | | |
| B4 | **Ketepatan Pengiraan Metrik:** Confusion Matrix, Precision, Recall, F1 dikira dengan aritmetik yang betul | | |
| B5 | **Kualiti Rajah Seni Bina:** Lengkap, berlabel jelas, protokol tepat, tata letak profesional | | |
| B6 | **Skema Rekod MES:** Medan lengkap; jenis data tepat; contoh nilai realistik dan konsisten | | |
| B7 | **Dokumen Spesifikasi Integrasi:** Profesional; semua bahagian ada; API spec tepat; boleh digunakan untuk handoff sebenar | | |
| B8 | **Analisis Perbandingan AI vs. Manual:** Data digunakan dengan betul; pengiraan ROI tepat; tafsiran bermakna | | |

**Jumlah Skor B: _____ / 32**

**Skor B sebagai peratus: _____ %** *(Jumlah Skor B ÷ 32 × 100)*

---

## Bahagian C: Penilaian Komunikasi dan Refleksi

*(Dinilai melalui jawapan soalan refleksi dalam KK-01 dan KK-02)*

| No. | Kriteria | Skor (1–4) | Ulasan |
|---|---|---|---|
| C1 | Pelatih boleh menjelaskan pilihan teknikalnya (kamera, pencahayaan, augmentasi) dengan justifikasi yang tepat | | |
| C2 | Pelatih memahami implikasi perniagaan Precision vs. Recall dan boleh memberi nasihat kepada pengurus kilang | | |
| C3 | Pelatih mengenal pasti kelemahan sistemnya sendiri dan mencadangkan penambahbaikan yang praktikal | | |

**Jumlah Skor C: _____ / 12**

---

## Pengiraan Markah Keseluruhan

| Bahagian | Skor | Wajaran | Skor Wajaran |
|---|---|---|---|
| A: Senarai Semak Pemerhatian | _____ / 23 elemen | 40% (berdasarkan peratusan kompeten) | |
| B: Kualiti Hasil Kerja | _____ / 32 | 45% | |
| C: Komunikasi dan Refleksi | _____ / 12 | 15% | |
| **JUMLAH TERTIMBANG** | | | **_____ %** |

**Formula pengiraan:**

```
Skor A (%) = (Bilangan elemen kompeten ÷ 23) × 100
Skor B (%) = (Jumlah skor B ÷ 32) × 100
Skor C (%) = (Jumlah skor C ÷ 12) × 100

Skor Keseluruhan = (Skor A × 0.40) + (Skor B × 0.45) + (Skor C × 0.15)
```

---

## Rubruk Prestasi / Performance Rubric

### Rubruk untuk Bahagian B1 — Kualiti Taksonomi Kecacatan

| Skor | Penerangan |
|---|---|
| **4** | ≥4 kelas kecacatan yang relevan dengan produk; nama dalam format betul (underscore, lowercase); penerangan tepat; gred sesuai dengan risiko industri; terdapat kelas `no_defect` |
| **3** | 3 kelas yang relevan; nama dan penerangan betul; gred ada tetapi mungkin tidak tepat untuk semua kelas |
| **2** | 3 kelas; nama atau penerangan generik; gred ada |
| **1** | <3 kelas atau kelas tidak relevan dengan produk; atau tiada gred |

### Rubruk untuk Bahagian B4 — Ketepatan Pengiraan Metrik

| Skor | Penerangan |
|---|---|
| **4** | Confusion Matrix betul; Precision, Recall, F1 dikira dengan formula yang tepat; aritmetik betul; nilai ditunjukkan sebagai peratusan; tafsiran kontekstual diberikan |
| **3** | Formula betul; aritmetik betul; hasil dalam peratusan; tafsiran ringkas ada |
| **2** | Formula betul; satu kesilapan aritmetik minor; hasil ada |
| **1** | Formula salah atau tidak lengkap |

### Rubruk untuk Bahagian B5 — Kualiti Rajah Seni Bina

| Skor | Penerangan |
|---|---|
| **4** | Semua lapisan ada (Level 0 hingga Level 3); semua komponen berlabel; protokol pada setiap sambungan; warna atau gaya berbeza untuk lapisan; tata letak professional dan mudah dibaca |
| **3** | Semua lapisan ada; kebanyakan komponen berlabel; protokol pada kebanyakan sambungan |
| **2** | Komponen utama ada; sebahagian tidak berlabel atau protokol tidak jelas |
| **1** | Rajah tidak lengkap atau tidak dapat difahami tanpa penjelasan lisan |

### Rubruk untuk Bahagian B7 — Dokumen Spesifikasi Integrasi

| Skor | Penerangan |
|---|---|
| **4** | Semua bahagian ada (gambaran, komponen, API spec, prestasi, simpanan, amaran, UAT); bahasa teknikal tepat; boleh digunakan untuk handoff kepada pasukan IT sebenar tanpa pindaan major |
| **3** | 5–6 bahagian; bahasa teknikal sebahagian betul; API spec ada tetapi tidak lengkap |
| **2** | 4 bahagian; asas ada; tidak profesional untuk handoff sebenar |
| **1** | <4 bahagian atau dokumen sangat umum tanpa kandungan teknikal |

---

## Keputusan Penilaian / Assessment Decision

**Syarat lulus:**
1. Semua elemen bertanda (*) dalam Bahagian A mestilah KOMPETEN (✓)
2. Skor Keseluruhan Tertimbang ≥ 70%

| Kriteria | Status |
|---|---|
| Semua elemen wajib (*) kompeten? | Ya / Tidak |
| Skor Keseluruhan ≥ 70%? | Ya / Tidak |
| **Keputusan Akhir** | **KOMPETEN / BELUM KOMPETEN** |

---

## Ruang Maklum Balas Penilai / Assessor Feedback

**Kekuatan yang diperhatikan:**

______________________________________________________________________
______________________________________________________________________
______________________________________________________________________

**Bidang yang memerlukan penambahbaikan:**

______________________________________________________________________
______________________________________________________________________
______________________________________________________________________

**Cadangan latihan lanjutan (jika BELUM KOMPETEN):**

______________________________________________________________________
______________________________________________________________________

---

## Pengesahan / Confirmation

| | Penilai | Pelatih |
|---|---|---|
| **Nama** | | |
| **Tandatangan** | | |
| **Tarikh** | | |

---

> **NOTA:** Pelatih yang didapati BELUM KOMPETEN berhak mendapat peluang penilaian semula (re-assessment) selepas menjalani latihan pemulihan yang dikenalpasti. Tarikh penilaian semula ditetapkan oleh pusat latihan.
