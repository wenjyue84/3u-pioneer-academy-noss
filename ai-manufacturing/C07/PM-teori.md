<!-- JPK_ENVELOPE_v1 -->
<table border="0" cellspacing="0" cellpadding="8" width="100%">
<tr>
<td width="130" valign="top"><img src="../../_assets/logos/jpk-logo.png" alt="JPK Logo" width="110"></td>
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
| KOD DAN TAJUK UNIT KOMPETENSI | MFG-AI-3:2026-C07 SMART FACTORY INTEGRATION AND OT/IT CONVERGENCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. USE MIDDLEWARE TO INTEGRATE OPERATIONAL TECHNOLOGY (OT) DATA WITH ENTERPRISE IT SYSTEMS<br>2. LOAD AI ENHANCEMENT MODULES (MODUL PENINGKATAN AI) ONTO SCADA/HMI SYSTEMS FOR INTELLIGENT HUMAN-MACHINE INTERFACE<br>3. PLAN AND BUILD A FACTORY DATA LAKE (DATA LAKE KILANG) ARCHITECTURE TO SUPPORT FACTORY-WIDE DATA GOVERNANCE<br>4. CONDUCT AN OT/IT CYBERSECURITY RISK AUDIT AND APPLY IEC 62443 CONTROLS TO A SIMULATED FACTORY NETWORK |
| NO. KOD | MFG-AI-3:2026-C07/PM-T(1/1) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** Pelan Mengajar Teori — Integrasi Kilang Pintar dan Konvergensi OT/IT

**TUJUAN:** Merancang pengajaran teori secara sesi demi sesi untuk mencapai jumlah 12 jam teori yang ditetapkan, merangkumi ketiga-tiga KP dalam unit kompetensi C07.

<!-- /JPK_ENVELOPE_v1 -->

---

## Maklumat Pelan Mengajar / Lesson Plan Information

| Medan | Nilai |
|---|---|
| **Jumlah Jam Teori** | 12 jam (720 minit) |
| **Jumlah Sesi** | 6 sesi × 2 jam |
| **KP Diliputi** | KP-01, KP-02, KP-03 |
| **Nama Jurulatih** | *(biarkan kosong — untuk ditandatangani)* |
| **Tarikh Mula** | *(untuk diisi oleh jurulatih)* |

---

## Jadual Sesi Teori / Theory Session Schedule

### SESI 1 — KP-01 Bahagian 1 (2 jam / 120 minit)

**Masa:** 120 minit

**Tajuk:** Pengenalan Konvergensi OT/IT: Perbezaan, Risiko, dan Model Purdue

**Objektif Pembelajaran:**
Pada akhir sesi ini, pelatih akan dapat:
1. Membezakan sistem OT daripada sistem IT merentasi empat dimensi (keutamaan keselamatan, kitaran hayat, toleransi masa, keperluan kemas kini)
2. Menerangkan mengapa konvergensi OT/IT mewujudkan risiko baharu yang tidak wujud apabila kedua-dua rangkaian terpencil
3. Melabelkan Model Rujukan Purdue dengan lima lapisan dan menerangkan fungsi setiap lapisan

| Masa | Tajuk Slot | Aktiviti P&P | Bahan / ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:15 | Pembukaan dan Pengenalan | Jurulatih memperkenalkan CU07 dan kepentingannya dalam konteks NIMP 2030 Thrust 7. Soal-jawab: "Apakah OT?" untuk mentaksir pengetahuan sedia ada. | Slaid pembuka, papan putih | Pemerhatian respons lisan |
| 0:15–0:45 | OT vs. IT: Apakah bezanya? | Kuliah interaktif: jurulatih membentangkan perbandingan OT/IT menggunakan jadual. Perbincangan kes: insiden kilang apabila OT terhubung tanpa segmentasi. | Slaid perbandingan OT/IT, video kilang (pilihan) | Soalan kuiz lisan 2 soalan |
| 0:45–1:15 | Model Rujukan Purdue | Kuliah bergambar rajah: jurulatih melukis 5 lapisan Purdue di papan putih sambil menerangkan. Pelatih melengkapkan gambar rajah kosong. | Papan putih, kertas A4 (gambar rajah kosong) | Pelatih melengkapkan gambar rajah |
| 1:15–1:45 | DMZ dan kepentingan segmentasi | Perbincangan kumpulan: "Apakah yang berlaku jika tiada DMZ?" Jurulatih moderasi. | Papan putih, slaid DMZ | Perbincangan kumpulan |
| 1:45–2:00 | Rumusan dan Soal-Jawab | Jurulatih merumuskan poin utama. Pelatih menjawab 3 soalan ulangkaji secara lisan. Tugasan pra-sesi 2: baca KP-01 Seksyen 3 (protokol). | KP-01 (untuk rujukan) | 3 soalan ulangkaji lisan |

---

### SESI 2 — KP-01 Bahagian 2 (2 jam / 120 minit)

**Masa:** 120 minit

**Tajuk:** Protokol Komunikasi Industri: MQTT, OPC-UA, Modbus, PROFINET, dan Edge Computing

**Objektif Pembelajaran:**
Pada akhir sesi ini, pelatih akan dapat:
1. Membandingkan empat protokol industri utama dari segi model komunikasi, keselamatan lalai, dan kes penggunaan
2. Menerangkan mengapa MQTT memerlukan TLS dan OPC-UA mempunyai keselamatan terbina dalam
3. Menerangkan seni bina tiga lapisan (OT → Edge → Cloud) dan peranan edge computing

| Masa | Tajuk Slot | Aktiviti P&P | Bahan / ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:10 | Ulangkaji Sesi 1 | Kuiz 5 soalan pendek tentang OT vs. IT dan Model Purdue. Jurulatih menyemak jawapan bersama. | Kad kuiz | Kuiz 5 soalan |
| 0:10–0:50 | Empat Protokol Industri | Kuliah perbandingan: Modbus → PROFINET → OPC-UA → MQTT. Setiap protokol dijelaskan dengan animasi atau gambar rajah cara ia berfungsi. Tekankan: Modbus dan MQTT-tanpa-TLS TIDAK selamat secara lalai. | Slaid protokol, gambar rajah Modbus master-slave, gambar rajah MQTT broker | Pelatih menjawab: "Dalam situasi X, protokol mana yang anda pilih?" |
| 0:50–1:20 | Edge Computing dan Seni Bina Hybrid | Kuliah bergambar rajah: tiga lapisan OT → Edge → Cloud. Perbandingan fungsi di edge vs. di awan. Contoh: kilang Nusajaya Tech Park mengunakan Moxa UC-8100 sebagai edge gateway. | Slaid seni bina, gambar rajah edge computing | Pelatih melukis semula seni bina tiga lapisan |
| 1:20–1:50 | Latihan Pemilihan Protokol | Pelatih (dalam pasangan) diberi 3 senario kilang dan perlu memilih protokol yang sesuai untuk setiap senario beserta justifikasi. Jurulatih moderasi perbincangan. | Helaian latihan senario | Maklum balas serta-merta dari jurulatih |
| 1:50–2:00 | Rumusan | Jurulatih merumuskan poin utama. Pratonton KP-02 untuk sesi seterusnya. | KP-01, KP-02 | Pemerhatian |

---

### SESI 3 — KP-02 Bahagian 1 (2 jam / 120 minit)

**Masa:** 120 minit

**Tajuk:** SCADA Berteraskan AI: Dari Sistem Reaktif ke Sistem Ramalan

**Objektif Pembelajaran:**
Pada akhir sesi ini, pelatih akan dapat:
1. Menerangkan komponen utama sistem SCADA konvensional dan batasannya
2. Menerangkan keempat-empat modul AI yang boleh ditambah kepada SCADA: pengesanan anomali, ramalan proses, pengurusan penggera pintar, dan cadangan tindakan
3. Membandingkan platform SCADA dengan AI yang ada di pasaran

| Masa | Tajuk Slot | Aktiviti P&P | Bahan / ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:15 | Kuiz Ulangkaji Sesi 2 | Jurulatih bertanya: "Apakah perbezaan keselamatan antara Modbus dan OPC-UA?" dan 2 soalan lain. Perbincangan kelas. | Papan putih | Ulangkaji lisan |
| 0:15–0:50 | SCADA Konvensional: Fungsi dan Batasan | Kuliah dengan gambar rajah komponen SCADA (MTU, RTU, PLC, HMI, historian). Perbincangan: kes alarm fatigue — "Bayangkan 3,000 penggera sehari — apa yang berlaku?" | Slaid, gambar rajah SCADA, video demonstrasi SCADA (pilihan) | Perbincangan kelas |
| 0:50–1:20 | Empat Modul AI untuk SCADA | Kuliah interaktif: setiap modul AI dijelaskan dengan kes penggunaan kilang. Tekankan: AI dalam OT hanya **menyokong** keputusan manusia — tidak menggantikan operator untuk tindakan kawalan kritikal. | Slaid modul AI, gambar rajah aliran data | Soalan pemahaman |
| 1:20–1:50 | Platform SCADA dengan AI | Pembentangan ringkas 5 platform (Ignition, Siemens WinCC, Rockwell FactoryTalk, GE iFIX, Aveva). Pelatih membuat perbandingan ringkas dalam jadual. | Slaid perbandingan platform, jadual kosong | Pelatih lengkapkan jadual perbandingan |
| 1:50–2:00 | Rumusan dan Tugasan | Jurulatih merumuskan. Tugasan pra-sesi: baca KP-02 Seksyen 2 (HMI) dan Seksyen 3 (tadbir urus data). | KP-02 | Pemerhatian |

---

### SESI 4 — KP-02 Bahagian 2 (2 jam / 120 minit)

**Masa:** 120 minit

**Tajuk:** Intelligent HMI, Tadbir Urus Data Kilang, dan Seni Bina Data Lake

**Objektif Pembelajaran:**
Pada akhir sesi ini, pelatih akan dapat:
1. Menerangkan evolusi HMI dari Generasi 1 ke Generasi 4 (Intelligent HMI)
2. Menerangkan lima dimensi tadbir urus data kilang pintar
3. Mereka bentuk struktur tiga zon data lake kilang (raw, curated, analytics)

| Masa | Tajuk Slot | Aktiviti P&P | Bahan / ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:10 | Ulangkaji Sesi 3 | 3 soalan ringkas tentang SCADA dan modul AI. | Papan putih | Ulangkaji lisan |
| 0:10–0:40 | Evolusi HMI | Kuliah dengan gambar visual setiap generasi HMI. Tunjukkan video atau gambar HMI Gen 1 (analog panel) berbanding HMI Gen 4 (tablet AR). Perbincangan: "Ciri Intelligent HMI mana yang paling berguna dalam kilang berbahaya?" | Slaid, gambar HMI Gen 1–4, video AR HMI (pilihan) | Perbincangan kelas |
| 0:40–1:10 | Tadbir Urus Data Kilang | Kuliah interaktif: lima dimensi tadbir urus. Kes PDPA 2010 — data biometrik pekerja kilang. Latihan: pelatih mencadangkan pemilik dan tempoh simpanan untuk 3 jenis data kilang. | Slaid, helaian latihan | Latihan individu — disemak bersama |
| 1:10–1:45 | Seni Bina Data Lake | Kuliah dengan gambar rajah tiga zon. Perbincangan: perbezaan data lake vs. data warehouse. Latihan: pelatih melabel 5 dataset ke zon yang sesuai. | Slaid, gambar rajah data lake, helaian latihan | Latihan individu |
| 1:45–2:00 | Rumusan dan Pratonton KP-03 | Jurulatih merumuskan. Pratonton KP-03: "Sesi seterusnya — ancaman keselamatan siber OT yang nyata." | KP-02, KP-03 | Pemerhatian |

---

### SESI 5 — KP-03 Bahagian 1 (2 jam / 120 minit)

**Masa:** 120 minit

**Tajuk:** Ancaman Keselamatan Siber OT dan Piawaian IEC 62443: Zon dan Konduit

**Objektif Pembelajaran:**
Pada akhir sesi ini, pelatih akan dapat:
1. Mengenal pasti lima vektor ancaman keselamatan siber utama dalam persekitaran OT kilang
2. Menerangkan konsep zon keselamatan dan konduit dalam model IEC 62443
3. Menetapkan komponen kilang kepada zon keselamatan yang sesuai dengan Aras Keselamatan yang betul

| Masa | Tajuk Slot | Aktiviti P&P | Bahan / ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:10 | Ulangkaji Sesi 4 | Soalan: "Apakah tiga zon data lake dan apakah data yang sesuai untuk setiap zon?" | Papan putih | Ulangkaji lisan |
| 0:10–0:40 | Ancaman Keselamatan Siber OT | Kuliah: lima vektor ancaman (USB malware, supply chain, akses jauh tidak selamat, pergerakan lateral, DoS). Untuk setiap ancaman, satu contoh insiden industri yang telah didokumentasikan secara umum (Stuxnet, Ukraine grid). Tekankan: bahan ini adalah untuk memahami risiko dan merancang pertahanan — bukan untuk replikasi. | Slaid ancaman, gambar rajah vektor serangan | Perbincangan kelas |
| 0:40–1:10 | IEC 62443: Zon dan Konduit | Kuliah: konsep zon keselamatan, jenis konduit (firewall, DMZ, data diode, jump server). Aras Keselamatan SL 0–SL 4. Latihan: pelatih menetapkan 6 komponen kilang ke zon IEC 62443 yang sesuai. | Slaid IEC 62443, helaian latihan | Latihan individu |
| 1:10–1:50 | Latihan Pemetaan Zon | Jurulatih membentangkan topologi kilang sintetik (mirip AutoComp dalam KK-02). Pelatih dalam kumpulan kecil (3 orang) menetapkan zon dan mencadangkan konduit. Setiap kumpulan membentangkan dalam 2 minit. | Helaian topologi, papan putih | Pembentangan kumpulan |
| 1:50–2:00 | Rumusan | Jurulatih merumuskan poin utama IEC 62443. Tugasan: baca KP-03 Seksyen 3 dan 4 (Defence in Depth, NACSA, dasar Malaysia). | KP-03 | Pemerhatian |

---

### SESI 6 — KP-03 Bahagian 2 + Ulangkaji Menyeluruh (2 jam / 120 minit)

**Masa:** 120 minit

**Tajuk:** Pertahanan Berlapis, Dasar Keselamatan Siber Malaysia, dan Ulangkaji Menyeluruh CU07

**Objektif Pembelajaran:**
Pada akhir sesi ini, pelatih akan dapat:
1. Menerangkan lima lapisan Defence in Depth dengan contoh kawalan untuk setiap lapisan
2. Menerangkan peranan NACSA dan keperluan Dasar Keselamatan Siber Kebangsaan untuk industri
3. Mengulangkaji kesemua kandungan KP-01, KP-02, dan KP-03 melalui aktiviti ulangkaji interaktif

| Masa | Tajuk Slot | Aktiviti P&P | Bahan / ABBM | Penilaian |
|---|---|---|---|---|
| 0:00–0:15 | Kuiz Ulangkaji Sesi 5 | 5 soalan berkaitan vektor ancaman OT dan zon IEC 62443. Perbincangan jawapan. | Papan putih | Kuiz 5 soalan |
| 0:15–0:40 | Defence in Depth: Lima Lapisan | Kuliah bergambar rajah piramid pertahanan berlapis. Latihan: pelatih menyenaraikan satu kawalan konkrit untuk setiap lapisan dalam konteks kilang E&E Malaysia. | Slaid Defence in Depth, helaian latihan | Latihan individu |
| 0:40–1:00 | NACSA dan Dasar Kebangsaan | Kuliah ringkas: peranan umum NACSA, definisi CNII, hubungan dengan kilang pembuatan biasa. Tekankan: kilang biasa tidak secara automatik termasuk dalam CNII kecuali mereka membekalkan sektor CNII. Cara mendapatkan panduan terkini dari NACSA.gov.my. | Slaid dasar, KP-03 Seksyen 3 dan 4 | Soalan pemahaman |
| 1:00–1:40 | Ulangkaji Menyeluruh CU07 | Aktiviti "Jeopardy-style": 3 kategori (OT/IT, Data Lake, Keselamatan Siber) × 5 soalan. Pelatih dalam 3 pasukan berlumba menjawab soalan. Jurulatih moderasi dan membetulkan jawapan yang salah. | Soalan ulangkaji, papan putih skor | Kuiz berstruktur |
| 1:40–2:00 | Pratonton Amali dan Penutupan | Jurulatih menerangkan KK-01 dan KK-02 yang akan datang. Soal-jawab akhir. Pengesahan pelatih faham keperluan amali. | KK-01, KK-02 | Soal-jawab |

---

## Ringkasan Jam Teori / Theory Hours Summary

| Sesi | Tajuk Utama | Jam |
|---|---|---|
| Sesi 1 | OT vs. IT, Model Purdue, DMZ | 2 |
| Sesi 2 | Protokol Industri, Edge Computing | 2 |
| Sesi 3 | SCADA Berteraskan AI | 2 |
| Sesi 4 | Intelligent HMI, Tadbir Urus Data, Data Lake | 2 |
| Sesi 5 | Ancaman OT, IEC 62443 Zon dan Konduit | 2 |
| Sesi 6 | Defence in Depth, NACSA, Ulangkaji | 2 |
| **Jumlah** | | **12 jam** |

---

## Bahan Pengajaran yang Diperlukan / Required Teaching Materials

| Bahan | Kuantiti | Catatan |
|---|---|---|
| Slaid pembentangan (PowerPoint) | 1 set (6 fail) | Disediakan oleh jurulatih |
| Helaian gambar rajah kosong (Model Purdue) | 1 per pelatih | Dicetak sebelum sesi |
| Helaian latihan protokol (Sesi 2) | 1 per pelatih | Dicetak sebelum sesi |
| Helaian latihan data lake (Sesi 4) | 1 per pelatih | Dicetak sebelum sesi |
| Helaian topologi kilang sintetik (Sesi 5) | 1 per pelatih | Dicetak sebelum sesi |
| KP-01, KP-02, KP-03 (cetakan) | 1 set per pelatih | Boleh dijadikan rujukan dalam kelas |
| Komputer riba jurulatih dan projektor | 1 unit | Untuk persembahan slaid |
| Papan putih dan penanda | 1 set | Untuk gambar rajah interaktif |

---

## Tandatangan / Signatures

| | |
|---|---|
| **Nama Jurulatih:** | _____________________________ |
| **Kelayakan:** | _____________________________ |
| **Tandatangan:** | _____________________________ |
| **Tarikh Disediakan:** | _____________________________ |
| **Disahkan oleh (Ketua Jurulatih):** | _____________________________ |
| **Tarikh Disahkan:** | _____________________________ |
