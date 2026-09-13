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

## KERTAS KERJA

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C07 MOBILE DEVICE CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. CARRY OUT MOBILE DEVICE CONFIGURATION<br>3. PERFORM MOBILE DEVICE TROUBLESHOOT<br>4. CARRY OUT MOBILE DEVICE COMMISSIONING |
| NO. KOD | IT-020-3:2013-C07/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-mobile-device-troubleshoot

**TUJUAN:** Kertas rujukan untuk KK-03-mobile-device-troubleshoot.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

Pada akhir aktiviti ini, pelatih dapat:

1. Mengenal pasti gejala (symptoms) masalah yang dilaporkan pada mobile device.
2. Mendiagnosis punca masalah menggunakan kaedah troubleshoot yang sistematik.
3. Melaksanakan tindakan pembetulan (corrective action) yang sesuai untuk masalah yang dikenal pasti.
4. Mengesahkan bahawa masalah telah diselesaikan selepas tindakan pembetulan.
5. Mendokumentasikan proses dan keputusan troubleshoot dalam borang laporan.

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti (Peralatan : Pelatih) |
|-----|------|-------------------------------|
| 1 | Mobile device (Smartphone/Tablet) dengan masalah simulasi | 1:1 |
| 2 | Komputer / Laptop | 1:1 |
| 3 | Kabel USB / USB cable | 1:1 |
| 4 | Rangkaian WiFi (access point) yang aktif | 1:kumpulan |
| 5 | Borang Laporan Troubleshoot (simulasi) | 1:1 |
| 6 | Senarai gejala masalah yang disediakan pengajar | 1:1 |

---

## Langkah Keselamatan / Safety Precautions

- Jangan melakukan factory reset tanpa kebenaran bertulis daripada pengajar.
- Pastikan data pada peranti telah dibuat sandaran (backup) sebelum sebarang tindakan pembetulan yang berisiko.
- Jangan memasang atau membuang aplikasi sistem (system apps) tanpa kebenaran pengajar.
- Catat setiap langkah troubleshoot yang diambil untuk membolehkan proses diulang atau dibatalkan.
- Sekiranya masalah tidak dapat diselesaikan, lapor kepada pengajar dan jangan teruskan.

---

## Prosedur / Procedure

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | **Terima dan Semak Laporan Masalah:** Terima borang laporan masalah simulasi daripada pengajar. Baca dengan teliti gejala (symptoms) yang dilaporkan oleh "pelanggan". Tanya soalan penjelasan jika perlu (simulasi): bilakah masalah mula berlaku, adakah berlaku selepas kemaskini, adakah masalah berterusan atau berkala. |
| 2 | **Pengesahan Gejala (Symptom Verification):** Hidupkan mobile device dan cuba sendiri gejala yang dilaporkan. Sahkan sama ada gejala dapat direplikasi. Catat pemerhatian awal: mesej ralat (error message), kod ralat (error code), tingkah laku peranti yang tidak normal. |
| 3 | **Diagnosis Masalah Rangkaian:** Semak status sambungan WiFi: buka Settings > WiFi, pastikan WiFi ON dan disambungkan. Jika tidak dapat sambung: lupakan (forget) rangkaian dan sambung semula, semak kata laluan, semak sama ada IP address bertentangan (conflict). Lakukan ping test ke gateway untuk mengesahkan sambungan rangkaian. Semak tetapan APN jika melibatkan data selular. |
| 4 | **Diagnosis Masalah Aplikasi:** Buka Settings > Apps / Application Manager. Kenalpasti aplikasi yang bermasalah. Cuba langkah berikut mengikut urutan: (a) Force Stop aplikasi, (b) Clear Cache, (c) Clear Data (amaran: akan memadam data aplikasi), (d) Uninstall dan install semula aplikasi. Semak versi OS dan pastikan memenuhi keperluan minimum aplikasi. |
| 5 | **Diagnosis Masalah Prestasi Peranti:** Semak penggunaan RAM: Settings > About Phone > Memory / RAM. Semak storan (storage): Settings > Storage — pastikan storan dalaman tidak penuh (minimum 15% kosong). Semak aplikasi yang berjalan di latar belakang (background apps) dan tutup yang tidak diperlukan. Semak penggunaan bateri (battery usage) untuk mengenal pasti aplikasi yang membebankan. |
| 6 | **Diagnosis Masalah Pengesahan (Authentication):** Sekiranya peranti tidak dapat log masuk ke akaun korporat atau MDM: semak kelayakan (username/password) dengan pengguna, semak sambungan internet, semak tetapan server (server address, port, SSL), semak sama ada akaun dikunci atau tamat tempoh kata laluan. |
| 7 | **Laksanakan Tindakan Pembetulan:** Berdasarkan diagnosis, laksanakan tindakan pembetulan yang sesuai. Lakukan satu tindakan pada satu masa dan uji selepas setiap tindakan sebelum meneruskan ke langkah seterusnya. Jika masalah tidak selesai selepas tindakan pertama, cuba tindakan seterusnya mengikut hierarki penyelesaian. |
| 8 | **Pengesahan Penyelesaian:** Setelah tindakan pembetulan dilaksanakan, uji semula fungsi yang bermasalah untuk mengesahkan masalah telah diselesaikan. Uji semua fungsi berkaitan untuk memastikan tiada masalah baru ditimbulkan. Dapatkan pengesahan daripada pengajar bahawa peranti kini berfungsi dengan baik. |
| 9 | **Dokumentasi:** Lengkapkan Borang Laporan Troubleshoot dengan mencatat: gejala asal, diagnosis punca masalah, tindakan pembetulan yang dilaksanakan, keputusan selepas tindakan, dan status akhir (selesai/perlu tindakan lanjut). Serahkan borang kepada pengajar. |

---

## Hasil Dijangka / Expected Outcome

- Gejala masalah dikenal pasti dan disahkan dengan tepat.
- Punca masalah didiagnosis melalui kaedah yang sistematik.
- Tindakan pembetulan yang sesuai berjaya dilaksanakan.
- Masalah diselesaikan dan disahkan melalui ujian pasca-pembetulan.
- Borang Laporan Troubleshoot dilengkapkan dan diserahkan kepada pengajar.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Terima / Accept | Tidak Terima / Reject | Catatan |
|-----|---------------------|-----------------|-----------------------|---------|
| **A. PROSES KERJA** | | | | |
| 1 | Laporan masalah diterima dan gejala dikenal pasti dengan betul | [ ] | [ ] | |
| 2 | Gejala disahkan (direplikasi) pada peranti | [ ] | [ ] | |
| 3 | Diagnosis masalah rangkaian dijalankan dengan sistematik | [ ] | [ ] | |
| 4 | Diagnosis masalah aplikasi dijalankan mengikut hierarki (Force Stop > Clear Cache > Clear Data > Reinstall) | [ ] | [ ] | |
| 5 | Diagnosis masalah prestasi (RAM, storage, battery) dijalankan | [ ] | [ ] | |
| 6 | Tindakan pembetulan dilaksanakan satu persatu dan diuji | [ ] | [ ] | |
| 7 | Masalah disahkan selesai melalui ujian pasca-pembetulan | [ ] | [ ] | |
| **B. HASIL KERJA** | | | | |
| 8 | Peranti berfungsi normal selepas troubleshoot | [ ] | [ ] | |
| 9 | Borang Laporan Troubleshoot dilengkapkan dengan lengkap | [ ] | [ ] | |
| 10 | Proses kerja disiapkan dalam masa yang ditetapkan | [ ] | [ ] | |
| **C. SIKAP** | | | | |
| 11 | Bekerja secara metodikal dan tidak tergesa-gesa | [ ] | [ ] | |
| 12 | Menepati masa yang ditetapkan | [ ] | [ ] | |
| 13 | Persekitaran tempat kerja dibersih dan dikemas setelah selesai | [ ] | [ ] | |
| **D. KESELAMATAN & PERSEKITARAN** | | | | |
| 14 | Tiada tindakan berisiko (factory reset, hapus sistem) tanpa kebenaran | [ ] | [ ] | |
| 15 | Setiap langkah troubleshoot dicatat untuk traceability | [ ] | [ ] | |

---

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|------------------------|---------------|
| **Pelatih / Trainee** | | | |
| **Pengajar / Instructor** | | | |