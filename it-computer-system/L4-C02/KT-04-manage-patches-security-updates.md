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

## KERTAS TUGASAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/KT(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-04-manage-patches-security-updates

**TUJUAN:** Kertas rujukan untuk KT-04-manage-patches-security-updates.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions in ALL sections. Refer to KP(4/5) for guidance. Write your answers clearly in the answer booklet provided. This assignment is formative.

**Masa / Duration:** 1 hour

---

## Bahagian A: Soalan Pelbagai Pilihan / Section A: Multiple Choice (20 marks — 4 marks each)

**A1.** A security update with a CVSS score of 9.5 is classified as:

- (a) Low
- (b) Medium
- (c) High
- (d) Critical

**A2.** The PRIMARY purpose of Windows Server Update Services (WSUS) is to:

- (a) Automatically install all updates on all computers without administrator control
- (b) Centralise and control the approval and distribution of Microsoft updates across the organisation
- (c) Replace the need for antivirus software
- (d) Download updates directly from the internet to each workstation

**A3.** Before applying a Critical security patch to a production server, the administrator should FIRST:

- (a) Apply it immediately without delay as it is Critical severity
- (b) Test the patch in a staging environment and obtain change management approval
- (c) Notify all users to log off and apply directly
- (d) Wait for the next quarterly maintenance window regardless of severity

**A4.** Which PowerShell command verifies whether a specific KB patch is installed on a system?

- (a) `Get-Service -Name KB5034441`
- (b) `Get-HotFix -Id KB5034441`
- (c) `Install-WindowsFeature KB5034441`
- (d) `Get-WindowsUpdate -KB5034441`

**A5.** A rollback plan for a patch deployment is important because:

- (a) Patches always fail and must be reversed
- (b) It allows the administrator to restore the system to its pre-patch state if the patch causes problems
- (c) It is required by WSUS before any patch can be approved
- (d) It replaces the need for a staging environment test

---

## Bahagian B: Soalan Jawapan Pendek / Section B: Short Answer (30 marks)

**B1.** Describe the EIGHT (8) phases of the patch management lifecycle in order. For each phase, state the key activity and the output produced. (16 marks)

**B2.** Explain the difference between a Security Update, a Service Pack, and a Feature Update. State the typical response time for a Critical security update and justify why. (6 marks)

**B3.** Describe FOUR (4) fields that must be included in a patch register and explain the purpose of each field. (4 marks)

**B4.** State THREE (3) items that should be checked during patch testing in a staging environment before approving a patch for production deployment. (4 marks — 1 mark per item, plus 1 bonus for explanation)

---

## Bahagian C: Soalan Situasi / Section C: Situational Question (50 marks)

**C1.** You are managing the IT infrastructure for a logistics company with 5 Windows Server 2022 servers and 120 Windows 11 workstations spread across 3 branch offices. The company currently has no centralised patch management solution — each machine downloads updates independently from Microsoft Update. A recent audit found that 35% of workstations are missing Critical security patches that are more than 60 days old.

(a) Explain the security risks created by the current unmanaged patching approach. Identify at least THREE (3) specific risks. (12 marks)

(b) Propose a WSUS-based patch management architecture for this company. Include: the placement of the WSUS server(s), how client computers will be directed to WSUS via Group Policy, and how you would structure WSUS computer groups for staged deployment. (18 marks)

(c) You receive a Microsoft Security Advisory for a Critical vulnerability (CVSS 9.8) in Windows Server 2022 that allows unauthenticated remote code execution. There is no known public exploit yet, but CyberSecurity Malaysia has issued an alert. Describe step-by-step the complete patch management process you would follow from receipt of the advisory to verified deployment on all servers, including how you would document each step. (20 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*

---

## Kriteria Penilaian / Assessment Criteria

| Section | Marks | Passing Standard |
|---------|-------|-----------------|
| A — Multiple Choice | 20 | Minimum 12/20 |
| B — Short Answer | 30 | Minimum 18/30 |
| C — Situational | 50 | Minimum 30/50 |
| **Total** | **100** | **Minimum 60/100** |