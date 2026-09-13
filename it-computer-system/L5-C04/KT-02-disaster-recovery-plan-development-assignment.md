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
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KT(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-02-disaster-recovery-plan-development-assignment

**TUJUAN:** Kertas rujukan untuk KT-02-disaster-recovery-plan-development-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Answer ALL questions. Refer to KP(2/4) for guidance. Write your answers in the space provided or on a separate answer sheet. This assignment is formative and does not count toward final assessment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

---

## Arahan / Instructions

Answer ALL questions. Refer to KP(2/4) for guidance. Write your answers in the space provided or on a separate answer sheet. This assignment is formative and does not count toward final assessment.

**Masa / Duration:** 1 hour 30 minutes

---

## Soalan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks — 2 marks each)

**A1.** A HOT SITE DR facility is characterised by:

- (a) A bare building with basic utilities only; systems must be brought in after a disaster
- (b) Pre-configured hardware with live synchronised systems enabling near-immediate failover
- (c) Hardware installed but no data replication; requires data restoration from backup
- (d) A cloud-hosted environment that is only provisioned when disaster is declared

**A2.** The Grandfather-Father-Son (GFS) backup rotation scheme uses which combination?

- (a) Hourly, daily, weekly backups
- (b) Daily, weekly, monthly backups
- (c) Weekly, monthly, yearly backups
- (d) Real-time, daily, weekly backups

**A3.** Synchronous data replication achieves an RPO of:

- (a) 24 hours
- (b) 1–4 hours
- (c) 15–30 minutes
- (d) Zero (0) — no data loss

**A4.** Which cloud DR model keeps a minimal "core" environment running in the cloud continuously and scales it up only when a disaster occurs?

- (a) Backup and Restore
- (b) Pilot Light
- (c) Warm Standby
- (d) Multi-site Active-Active

**A5.** A company's ERP system has an RTO of 24 hours and an RPO of 4 hours. Which DR site type is MOST cost-appropriate?

- (a) Hot site with real-time synchronous replication
- (b) Warm site with hourly log shipping
- (c) Cold site with weekly tape backup
- (d) No DR site needed

**A6.** The DRP document must be formally approved by which parties BEFORE it can be considered operational?

- (a) Only the IT helpdesk team
- (b) IT Director and CEO (at minimum); Internal Auditor for compliance verification
- (c) All staff who have read the document
- (d) The software vendor providing backup tools

**A7.** Which DRP section documents who has authority to declare a disaster and the conditions that trigger plan activation?

- (a) Section 6 — System Inventory
- (b) Section 8 — Backup and Replication Plan
- (c) Section 9 — Activation Procedures
- (d) Section 13 — Testing Schedule

**A8.** A Level 3 alert in an escalation procedure typically means:

- (a) A single workstation has failed
- (b) MTD is breached or imminent; DR Coordinator declares disaster and activates DRP
- (c) A department printer is offline
- (d) The backup job completed with warnings

**A9.** The "3-2-1" backup rule requires offsite storage of backups primarily to protect against:

- (a) Accidental file deletion by a single user
- (b) Site-wide disasters that destroy all on-site copies
- (c) Ransomware targeting only the production servers
- (d) Hard drive read errors on the backup media

**A10.** Differential backup saves:

- (a) Only files changed since the last backup of any type
- (b) All files changed since the last FULL backup
- (c) All files in the system, every time
- (d) Only newly created files since last full backup

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** Compare HOT SITE, WARM SITE, and COLD SITE DR facilities. For each, state: the typical RTO achievable, the relative cost, and ONE scenario where it would be the appropriate choice. Present your answer in a structured table. (9 marks)

**B2.** Explain the difference between INCREMENTAL and DIFFERENTIAL backup. Illustrate your answer with a weekly backup scenario (Monday full backup; Tuesday to Friday daily backup). Show what data is captured each day for both methods. (8 marks)

**B3.** Describe the role of the DR Coordinator and the Database Administrator (DBA) in a DR team. Explain why both roles are essential and what would happen if either role was absent during a DR activation. (7 marks)

**B4.** A company's DRP has not been reviewed for 3 years. The company has since migrated its email system to Microsoft 365 (cloud) and hired a new IT Director. Identify THREE (3) specific reasons why this DRP must be updated, and describe the update action required for each reason. (6 marks)

---

### Bahagian C: Soalan Esei / Essay (40 marks)

**C1.** You are the IT Manager of **Syarikat Perabot Maju Sdn. Bhd.**, a furniture manufacturer with 200 employees. The company's critical systems are:

| System | Current Backup | RTO Target | RPO Target |
|--------|---------------|------------|------------|
| ERP (production & inventory) | Weekly tape; stored on-site | 8 hours | 2 hours |
| CAD design server (product designs) | No backup | 24 hours | 4 hours |
| E-commerce website | Hosted externally by vendor | 2 hours | 30 minutes |
| Email (internal Exchange server) | Daily backup; stored on-site | 24 hours | 24 hours |

The company has approved a DR budget of RM 200,000 for initial setup and RM 60,000 annually.

(a) For each system, recommend and justify the appropriate DR strategy (site type and replication method) to meet the stated RTO and RPO targets within the budget. Explain any trade-offs you must make due to budget constraints. (16 marks)

(b) Design a complete backup and replication plan for the ERP system. Include: backup type and schedule (using GFS rotation), replication method, retention period, and offsite storage solution. Justify each decision. (12 marks)

(c) The company's CEO asks: "What is the minimum set of sections our DRP must contain to be ISO 22301-compliant?" Write a structured response identifying at least EIGHT (8) mandatory DRP sections and explaining the purpose of each in non-technical language suitable for a CEO. (12 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*