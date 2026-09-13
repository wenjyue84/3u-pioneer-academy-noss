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

## PELAN MENGAJAR – AMALI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C06 COMPUTER NETWORK CONNECTIVITY SET-UP |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER NETWORK CONFIGURATION SPECIFICATION<br>2. CARRY OUT COMPUTER NETWORK CONFIGURATION<br>3. PERFORM COMPUTER NETWORK CONNECTIVITY TEST<br>4. CARRY OUT COMPUTER NETWORK TROUBLESHOOT<br>5. PREPARE COMPUTER NETWORK CONNECTIVITY REPORT |
| NO. KOD | IT-020-3:2013-C06/PM(AMALI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-amali-network-connectivity-setup

**TUJUAN:** Kertas rujukan untuk PM-amali-network-connectivity-setup.

**TEMPAT:** BILIK AMALI / MAKMAL

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Setelah menamatkan semua 5 sesi KK, pelatih akan menduduki Penilaian Prestasi (PA).

**TEMPAT:** BILIK AMALI / MAKMAL RANGKAIAN

**TEMPOH:** Rujuk JPW/RK. (Jumlah amali: 84 jam)

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat melaksanakan persediaan sambungan rangkaian komputer secara praktikal, termasuk analisis spesifikasi, konfigurasi, pengujian, penyelesaian masalah, dan pelaporan.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, peralatan rangkaian sebenar, bahan tunjuk-cara.

---

## Agihan Masa Amali / Practical Time Allocation

| KK | Tajuk / Title | Jam / Hours |
|----|--------------|-------------|
| KK(1/5) | Analysing Network Configuration Specification and Preparing Installation Checklist | 16.8 |
| KK(2/5) | Carrying Out Network Configuration — Cabling, Device Setup, and IP Assignment | 21.0 |
| KK(3/5) | Performing Network Connectivity Testing | 16.8 |
| KK(4/5) | Carrying Out Network Troubleshooting | 21.0 |
| KK(5/5) | Preparing the Network Connectivity Report | 8.4 |
| **Jumlah / Total** | | **84.0** |

---

## Huraian Kandungan Amali / Practical Content Description

### KK(1/5) — Analysing Network Configuration Specification and Preparing Installation Checklist (16.8 jam)

| Langkah Kerja | Huraian |
|---------------|---------|
| 1.1 | Receive and read a simulated network configuration specification document |
| 1.2 | Identify all required network hardware: switches, routers, patch panels, access points |
| 1.3 | Extract and record the IP addressing scheme, subnet mask, default gateway, and DNS details |
| 1.4 | Identify cabling requirements: cable type, estimated lengths, quantity of RJ-45 connectors |
| 1.5 | Produce a complete installation checklist including equipment, tools, and configuration parameters |
| 1.6 | Draw a physical network topology diagram based on the specification |
| 1.7 | Submit checklist and diagram to instructor for review before proceeding |

### KK(2/5) — Carrying Out Network Configuration — Cabling, Device Setup, and IP Assignment (21.0 jam)

| Langkah Kerja | Huraian |
|---------------|---------|
| 2.1 | Gather and organise all required tools and materials at the workstation |
| 2.2 | Crimp UTP Cat 6 patch cables to T568B standard; test each cable with a cable continuity tester |
| 2.3 | Connect all devices to the managed switch according to the topology diagram |
| 2.4 | Configure the managed switch: port assignment, VLAN setup (where required), port labelling |
| 2.5 | Configure DHCP scope on the router/server: IP range, subnet mask, gateway, DNS, exclusions |
| 2.6 | Assign static IP addresses to fixed devices (printers, servers) as per specification |
| 2.7 | Configure each workstation's network adapter: verify DHCP lease or set static IP as required |
| 2.8 | Label all cables and ports systematically; perform cable management |

### KK(3/5) — Performing Network Connectivity Testing (16.8 jam)

| Langkah Kerja | Huraian |
|---------------|---------|
| 3.1 | Run `ipconfig /all` on each workstation; verify correct IP address, subnet mask, gateway, and DNS |
| 3.2 | Ping the default gateway from each workstation; record response times and packet loss |
| 3.3 | Ping each static-IP device (printers, servers) from a workstation; verify successful response |
| 3.4 | Ping between workstations to verify Layer 3 connectivity across the network |
| 3.5 | Run `tracert` to an external destination; verify correct routing path through the gateway |
| 3.6 | Test internet connectivity from at least two workstations using a browser |
| 3.7 | Use `nslookup` to verify DNS resolution for at least one external domain |
| 3.8 | Record all test commands and outputs in the connectivity test log sheet |

### KK(4/5) — Carrying Out Network Troubleshooting (21.0 jam)

| Langkah Kerja | Huraian |
|---------------|---------|
| 4.1 | Receive a simulated fault scenario from the instructor (e.g. APIPA address, ping failure, VLAN mismatch) |
| 4.2 | Identify and document the symptoms observed using systematic diagnostic commands |
| 4.3 | Apply bottom-up OSI troubleshooting: verify physical layer (cable, link light) first, then Layer 3 (IP config) |
| 4.4 | Use appropriate diagnostic tools: cable tester, ping, tracert, ipconfig, Event Viewer |
| 4.5 | Identify the root cause and apply the corrective action (recrimp cable, fix IP config, correct VLAN port) |
| 4.6 | Verify the fix by re-running connectivity tests and confirming expected results |
| 4.7 | Document each fault: symptom, diagnostic steps, root cause, corrective action, and verification result |

### KK(5/5) — Preparing the Network Connectivity Report (8.4 jam)

| Langkah Kerja | Huraian |
|---------------|---------|
| 5.1 | Compile all documentation collected during KK(1/5) to KK(4/5) |
| 5.2 | Complete the network connectivity report using the standard template: cover page, IP address table, equipment list, test results, fault log, remarks |
| 5.3 | Attach or transcribe actual command outputs (ipconfig, ping, tracert) as evidence |
| 5.4 | Review report for accuracy, completeness, and professional presentation |
| 5.5 | Present the completed report to the instructor/assessor; explain findings and any corrective actions taken |
| 5.6 | Obtain instructor sign-off on the completed report |

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Sambut pelatih; ambil kehadiran dan semak kehadiran PPE | 5 minit |
| 1.2 | Nyatakan objektif pembelajaran amali untuk sesi tersebut | 5 minit |
| 1.3 | Ulangkaji peraturan keselamatan: pengendalian kabel, kawasan kerja selamat, elektrik | 5 minit |
| 1.4 | Edarkan KK (Lembaran Kerja) dan terangkan struktur latihan | 5 minit |
| 1.5 | Sahkan semua peralatan dan bahan tersedia di setiap stesen kerja | 5 minit |

### 2. PENYAMPAIAN (Demonstration)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Demonstrasikan tugas amali langkah demi langkah mengikut prosedur KK |
| 2.2 | Tunjukkan teknik crimping kabel UTP yang betul dan penggunaan cable tester |
| 2.3 | Demonstrasikan konfigurasi IP pada Windows: tetapan DHCP dan IP statik |
| 2.4 | Jalankan arahan diagnostik secara langsung (ping, tracert, ipconfig) dan terangkan output |
| 2.5 | Tunjukkan teknik yang betul dan salah; terangkan akibat kesilapan |
| 2.6 | Jawab soalan sebelum pelatih memulakan kerja sendiri |

### 3. PENGGUNAAN (Practice)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Pelatih melaksanakan tugas amali di stesen kerja individu mereka |
| 3.2 | Pengajar mengelilingi untuk memerhati, membimbing, dan membetulkan teknik |
| 3.3 | Soal selidik lisan ringkas semasa amali untuk mengesahkan kefahaman |
| 3.4 | Pelatih melengkapkan senarai semak penilaian KK semasa bekerja |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Pengajar memeriksa kerja setiap pelatih yang telah disiapkan berdasarkan senarai semak penilaian |
| 4.2 | Sahkan hasil yang dijangkakan dicapai (sambungan berfungsi, laporan lengkap, ujian ping berjaya) |
| 4.3 | Berikan maklum balas tentang proses, hasil, sikap, keselamatan, dan kebersihan kawasan kerja |
| 4.4 | Pelatih membersihkan dan memulangkan peralatan dan bahan ke storan |
| 4.5 | Rekod penyelesaian sesi dan sebarang isu |

---

## Peralatan dan Bahan / Equipment and Materials

| Item | Kuantiti per Pelatih | Nota |
|------|---------------------|------|
| Managed switch (8-port atau lebih) | 1 | Untuk konfigurasi VLAN dan port |
| Router / DHCP server (fizikal atau VM) | 1 (dikongsi) | Untuk konfigurasi DHCP |
| Stesen kerja (PC atau laptop) | 2–3 | Untuk ujian sambungan antara peranti |
| Gulung kabel UTP Cat 6 | 1 (dikongsi) | Untuk pengkabelan patch |
| Konektor RJ-45 | 10 | Untuk latihan crimping |
| Crimping tool | 1 | Untuk memasang konektor RJ-45 |
| Cable continuity tester | 1 (dikongsi) | Untuk mengesahkan sambungan kabel |
| Patch panel (opsyenal) | 1 (dikongsi) | Untuk amali pemasangan kabinet rangkaian |
| Label maker atau tag kabel | 1 (dikongsi) | Untuk pelabelan kabel dan port |
| Pencetak rangkaian (atau simulasi) | 1 (dikongsi) | Untuk amali IP statik |
| Toner and probe kit | 1 (dikongsi) | Untuk mengesan kabel di panel |
| Borang laporan sambungan rangkaian | 1 | Borang bercetak |
| Dokumen NOSS | 1 | Rujukan IT-020-3:2013 CoCu 6 |

---

## Keselamatan / Safety Requirements

- Pastikan semua stesen kerja dalam keadaan selamat sebelum memulakan kerja kabel
- Elakkan membengkokkan kabel UTP melebihi jejari lenturan minimum (jangan lebih dari 4x diameter kabel)
- Pastikan kabel tidak menjadi halangan laluan atau bahaya tersandung
- Gunakan alat crimping dengan betul untuk mengelakkan kecederaan tangan
- Pastikan semua peralatan rangkaian (switch, router) dihidupkan mengikut urutan yang betul
- Sisa kabel dan pembungkusan mesti dilupuskan melalui saluran kitar semula yang diluluskan
- Jangan menyambung atau memutuskan kabel rangkaian aktif tanpa makluman kepada pengajar

---

## Penilaian Amali / Practical Assessment

Setelah menamatkan semua 5 sesi KK, pelatih akan menduduki Penilaian Prestasi (PA):

- **Kod:** IT-020-3:2013-C06/PA
- **Tempoh minimum:** 3 jam
- **Format:** Tugas praktikal (persediaan sambungan rangkaian lengkap daripada spesifikasi hingga laporan handover)
- **Kriteria penilaian:** Proses, hasil, sikap, keselamatan, pematuhan alam sekitar
- **Markah lulus:** Kompeten (C) — markah keseluruhan ≥ 60% dan semua kriteria kritikal dipenuhi