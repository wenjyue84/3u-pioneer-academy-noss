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
| NO. KOD | IT-020-4:2013-C02/KT(5/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-05-document-security-configuration-incidents

**TUJUAN:** Kertas rujukan untuk KT-05-document-security-configuration-incidents.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions in ALL sections. Refer to KP(5/5) for guidance. Write your answers clearly in the answer booklet provided. This assignment is formative.

**Masa / Duration:** 1 hour

---

## Bahagian A: Soalan Pelbagai Pilihan / Section A: Multiple Choice (20 marks — 4 marks each)

**A1.** A security configuration baseline document is used to:

- (a) Record only the network IP addresses of all servers
- (b) Document the minimum-security settings all systems of a given type must meet, as a reference for compliance and configuration management
- (c) List the names of all users in the Active Directory domain
- (d) Replace the need for an incident report

**A2.** According to the NIST SP 800-61 incident response lifecycle, the correct order of phases is:

- (a) Detection → Containment → Preparation → Eradication → Recovery
- (b) Preparation → Detection and Analysis → Containment → Eradication → Recovery → Post-Incident Activity
- (c) Containment → Detection → Eradication → Recovery → Preparation
- (d) Detection → Preparation → Recovery → Eradication → Post-Incident Activity

**A3.** Windows Security Event ID 4625 indicates:

- (a) A user account was created
- (b) A user account was locked out
- (c) A failed logon attempt
- (d) A successful logon

**A4.** Storing security logs ONLY on the affected local system is a risk because:

- (a) Local storage is slower than centralised storage
- (b) An attacker who compromises the system can delete or alter the logs, destroying evidence
- (c) Local logs are not compatible with SIEM systems
- (d) Event Viewer cannot store more than 100 events

**A5.** Under the Personal Data Protection Act 2010 (PDPA), when a security incident involves personal data, the organisation must:

- (a) Ignore it if fewer than 10 individuals are affected
- (b) Implement adequate security controls to protect personal data and be accountable for breaches
- (c) Only notify affected individuals if the data was sold
- (d) Delete all personal data immediately upon discovery of the incident

---

## Bahagian B: Soalan Jawapan Pendek / Section B: Short Answer (30 marks)

**B1.** List EIGHT (8) sections that must be included in a security configuration baseline record. For each section, give one example of the information it would contain. (16 marks)

**B2.** Describe the SIX (6) phases of the NIST incident response lifecycle. For each phase, state the key activity performed. (12 marks)

**B3.** State TWO (2) Windows Security Event IDs related to account management and explain what each event indicates. (2 marks)

---

## Bahagian C: Soalan Situasi / Section C: Situational Question (50 marks)

**C1.** Read the following incident scenario carefully, then answer all parts.

**Scenario:** At 14:35 on a Monday, the IT helpdesk receives a call from the Finance Manager reporting that her computer is behaving unusually — files in the Finance shared folder are being renamed with the extension `.encrypted` and a ransom note text file has appeared on her desktop. You check the SIEM and find the following events:

- **13:47** — Event ID 4624: Successful logon for account `fin.manager` from workstation `FIN-PC-05`
- **13:52** — Event ID 4648: Logon using explicit credentials for account `svc-backup` from `FIN-PC-05`
- **14:01** — Multiple Event ID 4663: Object access — Finance share files being accessed and modified by `svc-backup`
- **14:35** — Finance Manager calls helpdesk

(a) Classify this incident by type and severity (P1–P4). Justify your classification. (8 marks)

(b) Describe the immediate containment steps you would take within the first 30 minutes of confirming this incident. (12 marks)

(c) Based on the SIEM events provided, construct an incident timeline. Identify the likely attack vector and explain what each event in the timeline indicates about the attacker's actions. (15 marks)

(d) Complete the Lessons Learned section of the incident report for this scenario. Identify at least THREE (3) weaknesses revealed by this incident and for each, recommend a specific corrective action with a named owner and a realistic deadline. (15 marks)

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