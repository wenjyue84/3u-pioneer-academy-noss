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
| NO. KOD | IT-020-3:2013-C07/KK(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-mobile-device-configuration

**TUJUAN:** Kertas rujukan untuk KK-02-mobile-device-configuration.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

Pada akhir aktiviti ini, pelatih dapat:

1. Melaksanakan konfigurasi tetapan menu peranti mudah alih dengan betul.
2. Mengkonfigurasi tetapan rangkaian: WiFi, IP Address, dan pengesahan (authentication).
3. Memasang (install) dan mengkonfigurasi aplikasi yang diperlukan pada mobile device.
4. Melaksanakan pengujian konfigurasi untuk memastikan peranti berfungsi mengikut keperluan job order.
5. Mendokumentasikan semua langkah konfigurasi yang telah dilaksanakan.

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti (Peralatan : Pelatih) |
|-----|------|-------------------------------|
| 1 | Komputer / Laptop | 1:1 |
| 2 | Mobile device (Smartphone/Tablet) | 1:1 |
| 3 | Kabel USB / USB cable | 1:1 |
| 4 | Rangkaian WiFi (access point) yang aktif | 1:kumpulan |
| 5 | Borang Laporan Konfigurasi (simulasi) | 1:1 |
| 6 | LCD Projector | 1:bilik |

---

## Langkah Keselamatan / Safety Precautions

- Pastikan mobile device dicas sekurang-kurangnya 50% sebelum memulakan konfigurasi.
- Jangan memadam (delete) data sedia ada pada peranti tanpa kebenaran pengajar.
- Gunakan kelayakan (credentials) simulasi yang disediakan pengajar; jangan gunakan akaun peribadi.
- Sekiranya konfigurasi gagal, jangan cuba factory reset tanpa arahan pengajar.
- Catat setiap perubahan tetapan yang dilakukan untuk membolehkan rollback jika perlu.

---

## Prosedur / Procedure

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | **Konfigurasi Tetapan Menu Peranti:** Buka Settings pada mobile device. Semak dan konfigurasi tetapan asas: Display (brightness, screen timeout), Sound & notification, Date & time (set to automatic), Language & input. Catat sebarang perubahan yang dilakukan. |
| 2 | **Konfigurasi Rangkaian WiFi:** Buka Settings > Wireless & Network > WiFi. Hidupkan (ON) WiFi. Pilih SSID rangkaian yang ditetapkan dalam job order daripada senarai. Masukkan kata laluan (password) yang diberikan oleh pengajar. Sahkan peranti berjaya disambungkan dan peroleh IP address. |
| 3 | **Konfigurasi IP Address (jika statik diperlukan):** Setelah menyambung ke WiFi, ketik dan tahan nama rangkaian > Modify network. Tukar IP settings daripada DHCP kepada Static. Masukkan IP Address, Gateway, Subnet mask, dan DNS server seperti yang ditetapkan dalam job order. Simpan tetapan. |
| 4 | **Pengujian Rangkaian dan Pengesahan (Authentication):** Buka pelayar (browser) pada mobile device. Cuba akses laman web (contoh: www.google.com) untuk mengesahkan capaian internet. Jalankan ping test melalui aplikasi Network Tools jika tersedia. Catat keputusan ujian. |
| 5 | **Pemasangan Aplikasi:** Buka Google Play Store (Android) atau App Store (iOS). Cari dan pasang aplikasi yang ditetapkan dalam job order (contoh: aplikasi korporat, MDM agent, e-mel). Untuk setiap aplikasi: semak versi minimum OS, semak keserasian dengan peranti, muat turun dan pasang, sahkan aplikasi berjaya dipasang dan boleh dibuka. |
| 6 | **Prosedur Konfigurasi Aplikasi:** Buka setiap aplikasi yang dipasang. Masukkan tetapan konfigurasi yang diperlukan (contoh: server address untuk e-mel korporat, port number, SSL/TLS setting). Uji fungsi asas setiap aplikasi. Catat sebarang ralat (error) yang berlaku. |
| 7 | **Pengujian Konfigurasi Peranti:** Lakukan ujian pengesahan (authentication test): log masuk ke akaun korporat atau MDM. Lakukan ujian komunikasi rangkaian: hantar e-mel ujian, akses shared folder. Lakukan ujian aplikasi: jalankan setiap aplikasi yang dipasang dan sahkan fungsi utamanya. |
| 8 | **Dokumentasi:** Lengkapkan Borang Laporan Konfigurasi dengan mencatat: semua tetapan yang telah dikonfigurasi, aplikasi yang dipasang beserta versi, keputusan ujian (berjaya/gagal), dan sebarang isu yang dijumpai beserta tindakan yang diambil. Serahkan borang kepada pengajar. |

---

## Hasil Dijangka / Expected Outcome

- Tetapan menu peranti dikonfigurasi mengikut keperluan job order.
- Peranti berjaya disambungkan ke rangkaian WiFi dan memperoleh IP address yang betul.
- Semua aplikasi yang ditetapkan berjaya dipasang dan dikonfigurasi.
- Ujian konfigurasi (authentication, rangkaian, aplikasi) berjaya dijalankan.
- Borang Laporan Konfigurasi dilengkapkan dan diserahkan kepada pengajar.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Terima / Accept | Tidak Terima / Reject | Catatan |
|-----|---------------------|-----------------|-----------------------|---------|
| **A. PROSES KERJA** | | | | |
| 1 | Tetapan menu peranti dikonfigurasi dengan betul | [ ] | [ ] | |
| 2 | WiFi berjaya disambungkan dengan IP address yang betul | [ ] | [ ] | |
| 3 | IP Address (statik/DHCP) dikonfigurasi mengikut keperluan | [ ] | [ ] | |
| 4 | Aplikasi yang ditetapkan berjaya dipasang dan dikonfigurasi | [ ] | [ ] | |
| 5 | Ujian pengesahan (authentication) berjaya | [ ] | [ ] | |
| 6 | Ujian komunikasi rangkaian berjaya | [ ] | [ ] | |
| 7 | Ujian aplikasi berjaya dijalankan | [ ] | [ ] | |
| **B. HASIL KERJA** | | | | |
| 8 | Borang Laporan Konfigurasi dilengkapkan dengan tepat | [ ] | [ ] | |
| 9 | Proses kerja disiapkan dalam masa yang ditetapkan | [ ] | [ ] | |
| **C. SIKAP** | | | | |
| 10 | Bekerja secara sistematik mengikut prosedur | [ ] | [ ] | |
| 11 | Menepati masa yang ditetapkan | [ ] | [ ] | |
| 12 | Persekitaran tempat kerja dibersih dan dikemas setelah selesai | [ ] | [ ] | |
| **D. KESELAMATAN & PERSEKITARAN** | | | | |
| 13 | Prosedur keselamatan dipatuhi sepanjang aktiviti | [ ] | [ ] | |
| 14 | Tiada perubahan tidak dibenarkan dilakukan pada peranti | [ ] | [ ] | |

---

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|------------------------|---------------|
| **Pelatih / Trainee** | | | |
| **Pengajar / Instructor** | | | |