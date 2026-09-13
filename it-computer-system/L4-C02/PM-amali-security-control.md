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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/PM(AMALI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-amali-security-control

**TUJUAN:** Kertas rujukan untuk PM-amali-security-control.

**TEMPAT:** BILIK AMALI / MAKMAL

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
## Agihan Masa Amali / Practical Time Allocation

| KK | Tajuk / Title | Aktiviti Kerja | Jam / Hours |
|----|--------------|----------------|-------------|
| KK(1/5) | Conducting a Security Requirements Analysis | WA 1 | 21.0 |
| KK(2/5) | Configuring User Accounts, Groups, and Authentication Policies | WA 2 | 35.0 |
| KK(3/5) | Configuring Windows Defender Firewall and Reducing the Attack Surface | WA 3 | 35.0 |
| KK(4/5) | Implementing a Patch Management Cycle Using WSUS | WA 4 | 35.0 |
| KK(5/5) | Producing a Security Configuration Record and Incident Report | WA 5 | 14.0 |
| **Jumlah / Total** | | | **140.0** |

---

## Kaedah Pengajaran Amali / Practical Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Brief trainees on the session objective, the specific KK task, and expected output | 10 min |
| 1.2 | Verify that all workstations and lab infrastructure are operational; reset lab VMs to baseline snapshot if required | 10 min |
| 1.3 | Distribute scenario briefs, blank templates, and reference materials | 5 min |
| 1.4 | Demonstrate the first one or two steps of the KK procedure as a worked example (instructor-led walkthrough) | 15 min |
| 1.5 | Remind trainees of safety precautions: lab isolation, no changes to production-scope settings, log off when done | 5 min |

### 2. PENYAMPAIAN (Presentation / Demonstration)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Instructor demonstrates the complete procedure on the main projection system before trainees attempt independently |
| 2.2 | Key decision points highlighted: e.g. why PoLP matters when assigning permissions; why staging is required before production patching |
| 2.3 | Show common errors and their consequences during demonstration (e.g. what happens when Everyone group is not removed from a shared folder) |
| 2.4 | Allow trainees to observe and take notes during demonstration |

### 3. PENGGUNAAN (Application)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Trainees perform the KK procedures independently on their assigned lab workstations/VMs |
| 3.2 | Instructor circulates to observe, provide guidance only when genuinely stuck (do not perform steps for trainees) |
| 3.3 | Trainees complete the Assessment Checklist in the KK as they go; self-assess against each criterion |
| 3.4 | Trainees who complete early may attempt the extension task (if provided) or review their configuration documentation |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Instructor verifies each trainee's completed work against the KK Assessment Checklist |
| 4.2 | Trainees present their configuration record or output to the instructor (2–3 minutes per trainee) |
| 4.3 | Instructor signs and dates the KK Assessment Checklist for each trainee who meets all criteria |
| 4.4 | Debrief with class: common mistakes observed, correct approaches, key lessons |
| 4.5 | Trainees who do not meet all criteria must repeat the session in remediation time |
| 4.6 | Record session completion and attendance in training register |

---

## Perincian Sesi Amali / Session-by-Session Detail

### KK(1/5): Security Requirements Analysis — 21 jam

| Sesi | Aktiviti | Masa |
|------|---------|------|
| A1.1 | Introduction to lab environment; asset inventory exercise using provided scenario | 3 jam |
| A1.2 | Threat identification and risk rating workshop; complete threat register for scenario | 3 jam |
| A1.3 | Vulnerability assessment simulation using provided vulnerability scan output; interpret results | 3 jam |
| A1.4 | Control selection and justification; map controls to risks | 3 jam |
| A1.5 | SRS document production; trainees draft complete SRS for scenario | 3 jam |
| A1.6 | SRS peer review and presentation; instructor feedback; re-draft if required | 3 jam |
| A1.7 | Remediation / consolidation session; catch-up for trainees requiring additional time | 3 jam |

### KK(2/5): Access Control and Authentication — 35 jam

| Sesi | Aktiviti | Masa |
|------|---------|------|
| A2.1 | Active Directory lab setup: create OUs, user accounts, and security groups | 5 jam |
| A2.2 | NTFS permissions configuration; access control verification by role login test | 5 jam |
| A2.3 | GPO — password policy and account lockout configuration; gpresult verification | 5 jam |
| A2.4 | GPO — logon restrictions and software restriction policies | 5 jam |
| A2.5 | Account lockout trigger and unlock procedure; privileged account management practice | 5 jam |
| A2.6 | Linux user management: useradd, chmod, setfacl; equivalent RBAC on Linux | 5 jam |
| A2.7 | Consolidation and configuration record completion; instructor sign-off | 5 jam |

### KK(3/5): Firewall and Network Security — 35 jam

| Sesi | Aktiviti | Masa |
|------|---------|------|
| A3.1 | Pre-hardening Nmap scan; baseline documentation | 5 jam |
| A3.2 | Services review: identify and disable unnecessary services via services.msc and PowerShell | 5 jam |
| A3.3 | Windows Defender Firewall — create inbound rules (RDP restriction, block Telnet, allow HTTPS, allow DNS) | 5 jam |
| A3.4 | Windows Defender Firewall — create outbound rules; export firewall policy backup | 5 jam |
| A3.5 | Post-hardening Nmap scan; compare with baseline; verify attack surface reduction | 5 jam |
| A3.6 | VLAN and DMZ design exercise (paper-based or simulation tool) | 5 jam |
| A3.7 | Firewall rule register completion; consolidation and instructor sign-off | 5 jam |

### KK(4/5): Patch Management — 35 jam

| Sesi | Aktiviti | Masa |
|------|---------|------|
| A4.1 | WSUS role installation and configuration wizard | 5 jam |
| A4.2 | WSUS synchronisation setup; product and classification selection; initial sync | 5 jam |
| A4.3 | Computer group creation in WSUS; GPO client configuration | 5 jam |
| A4.4 | Workstation registration in WSUS; update detection verification | 5 jam |
| A4.5 | Update approval workflow; approve for Test group; monitor installation | 5 jam |
| A4.6 | Patch compliance verification: Get-HotFix, WSUS reports, Event Viewer | 5 jam |
| A4.7 | Patch register completion; rollback procedure demonstration; consolidation and sign-off | 5 jam |

### KK(5/5): Security Documentation and Incident Response — 14 jam

| Sesi | Aktiviti | Masa |
|------|---------|------|
| A5.1 | Security configuration baseline record: system identification, OS and services enumeration using PowerShell | 4 jam |
| A5.2 | Audit policy configuration (AuditPol); test event generation; Event Viewer log analysis | 3 jam |
| A5.3 | Simulated incident scenario: read scenario brief, analyse SIEM log excerpts, determine severity | 3 jam |
| A5.4 | Incident report completion; verbal presentation to instructor; lessons learned discussion | 4 jam |

---

## Peraturan Makmal / Lab Rules

| Peraturan / Rule | Penerangan / Detail |
|-----------------|---------------------|
| Rangkaian terpencil | Semua aktiviti amali mesti dijalankan pada rangkaian makmal terpencil sahaja. Dilarang menjalankan Nmap atau pengujian keselamatan pada rangkaian pengeluaran. |
| Snapshot VM | Ambil snapshot VM sebelum setiap sesi dimulakan. Pulihkan kepada snapshot jika konfigurasi rosak. |
| Kelayakan pentadbir | Kelayakan pentadbir yang diberikan untuk makmal adalah sulit. Jangan kongsi dengan pelatih lain. |
| Log keluar | Log keluar daripada semua sesi selepas setiap sesi amali. |
| Perubahan skop | Jangan ubah suai tetapan di luar OU latihan atau skop yang ditetapkan oleh pengajar. |
| Dokumentasi | Setiap perubahan konfigurasi mesti didokumentasikan sebelum dan selepas. |

---

## Penilaian Prestasi / Performance Assessment

Setelah semua 5 KK diselesaikan dan ditandatangani oleh pengajar, pelatih akan menjalani Penilaian Prestasi (PA):

- **Kod:** IT-020-4:2013-C02/PA
- **Tempoh:** 5 jam
- **Format:** Amali menyeluruh — melaksanakan semua 5 kawalan keselamatan dalam satu sesi penilaian bersepadu
- **Markah lulus:** 70/100
- **Syarat:** Semua KK mesti diselesaikan dan ditandatangani sebelum pelatih dibenarkan menduduki PA
- **Penilai:** Minimum 2 penilai bertauliah; satu pengesah dalaman