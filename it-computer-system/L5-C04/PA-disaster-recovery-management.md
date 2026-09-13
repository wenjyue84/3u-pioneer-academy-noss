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
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/PA |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU MUDA (Light Blue) |

**TAJUK:** PA-disaster-recovery-management

**TUJUAN:** Kertas rujukan untuk PA-disaster-recovery-management.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. This is a PRACTICAL examination covering all four Work Activities of CoCU 4.
2. You will be given a disaster scenario, access to a virtualised lab environment, document templates, and reference materials.
3. You will be assessed on: **Process** (how you perform the work), **Output** (quality of documents and technical results), **Attitude** (professionalism, decision-making), **Safety** (data security and documentation standards), and **Environmental** compliance (workspace management).
4. All documentation must be completed using the provided templates.
5. You may NOT use completed assignments from KK sessions — all work must be original for this assessment.
6. Total duration: **8 hours** (may be conducted over 2 days as per institutional schedule)

---

## Arahan kepada Penilai / Instructions to Assessor

- Provide each trainee with the scenario brief, lab access credentials, and all required templates.
- Observe each trainee continuously or at regular intervals; do NOT provide guidance or hints.
- Mark each criterion on the rubric as the trainee works and upon submission of final documents.
- Verify all technical outputs (database restored, application accessible, validation checklist signed) before scoring the Output section.
- A minimum score of 60% overall is required to pass.

---

## Senario Penilaian / Assessment Scenario

**Organisasi:** Syarikat Pengurusan Hartanah Jaya Sdn. Bhd. — a property management company with 150 staff, managing 5,000 residential units across 3 states.

**Sistem IT kritikal:**

| System | Role | Priority Tier | RTO Target | RPO Target |
|--------|------|--------------|------------|------------|
| Property Management System (PMS) | Tenancy records, rental collection, maintenance requests | Tier 1 | 4 hours | 1 hour |
| Financial System | Accounts, payroll, owner disbursements | Tier 2 | 12 hours | 4 hours |
| Document Management System (DMS) | Tenancy agreements, legal documents | Tier 2 | 24 hours | 8 hours |
| Email Server | Internal communication | Tier 3 | 48 hours | 24 hours |

**Kejadian / Incident:** At 06:30 on a Monday, an electrical surge caused by a lightning strike destroys the primary server rack at the company's head office data room. The UPS failed to hold power. All four systems are offline. The DR Coordinator (you) has been notified at 06:50.

**Lab environment:** The virtualised lab simulates the DR site (Cyberjaya colocation). Pre-loaded backups and VM snapshots are available at the designated lab share. The lab network simulates DR site connectivity.

**Masa yang diperuntukkan / Time Allocation:**

| Task | Allocated Time |
|------|---------------|
| WA1: BIA and Risk Assessment | 1.5 hours |
| WA2: DRP Activation and Strategy Confirmation | 1 hour |
| WA3: Technical Recovery (Lab) | 3 hours |
| WA4: Post-Incident Report Production | 2.5 hours |
| **Total** | **8 hours** |

---

## Tugasan / Tasks

### WA1: Analyse Disaster Recovery Requirements (1.5 hours)

Using the scenario information provided:

1. Complete a BIA table for all four systems: MTD, justified RTO, justified RPO, impact category, and priority tier
2. Complete a Risk Register with minimum FOUR (4) threats relevant to this scenario; include likelihood, impact, risk score, and classification
3. Identify THREE (3) gaps in the described IT infrastructure's DR posture; document each gap and its consequence
4. Write a 150-word BIA Executive Summary suitable for the CEO

### WA2: DRP Activation and Strategy (1 hour)

Using the completed DRP template provided (partially pre-filled with company details):

1. Complete the DRP Activation section: confirm the disaster declaration authority, state the conditions that were met to justify activation, and document the first 10 activation steps with timestamps (use 06:50 as T=0)
2. Confirm or revise the DR strategy for each system tier based on the scenario; justify any revisions
3. Define the DR team for this scenario: assign minimum SIX (6) roles; create a simplified escalation procedure with 3 levels

### WA3: Technical Recovery Implementation (3 hours — Lab)

In the virtualised lab environment:

1. Verify DR site network connectivity (ping tests; document results with timestamps)
2. Restore the PMS database from the provided backup files; apply all available transaction logs; run integrity check; calculate actual RPO
3. Update PMS application configuration to connect to DR database; start application service; perform smoke tests (login, view a tenancy record, generate a report)
4. Calculate actual RTO for PMS (from 06:50 to application validated)
5. Document all steps in the DR Implementation Log (provided template) with timestamps and observations

### WA4: Post-Incident Report (2.5 hours)

Produce a complete Post-Incident Report (PIR) using the provided PIR template:

1. Section 1 — Executive Summary (200–250 words, CEO-level language)
2. Section 3 — Incident Timeline (minimum 15 entries from 06:30 to PMS recovery declaration)
3. Section 4 — Root Cause Analysis (5 Whys for the primary cause: electrical surge → server failure)
4. Section 5 — Recovery Performance (actual vs. target RTO/RPO; MTTD; MTTR; variance classification)
5. Section 7 — Issues and Gaps (minimum 3 issues encountered or identified)
6. Section 8 — Corrective Action Plan (minimum 5 CAP items; all fields completed; prioritised)
7. Section 10 — Lessons Learnt (minimum 3 lessons with improvement recommendations)

---

## Rubrik Penilaian / Assessment Rubric

### A. PROSES (Process) — 30 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| A1 | BIA completed systematically: all systems covered; MTD, RTO, RPO values justified; tiers correctly assigned | 6 | |
| A2 | Risk Register: minimum 4 threats; likelihood, impact, and risk scores correctly calculated; classification accurate | 6 | |
| A3 | DRP activation procedure: disaster declaration documented; first 10 steps in correct chronological order with timestamps | 6 | |
| A4 | Technical recovery executed in correct sequence: network → database → application; each step documented with timestamp | 6 | |
| A5 | PIR produced in correct format: all 7 required sections present; professional language; consistent formatting | 6 | |
| | **Subtotal Process** | **30** | |

### B. HASIL (Output) — 30 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| B1 | PMS database successfully restored; DBCC CHECKDB passed; RPO calculated correctly | 6 | |
| B2 | PMS application operational at DR site; smoke tests passed; RTO calculated correctly | 6 | |
| B3 | DR Implementation Log complete and accurate with timestamps for all key steps | 4 | |
| B4 | PIR Executive Summary: 200–250 words; CEO-appropriate language; covers all required elements | 5 | |
| B5 | CAP table: minimum 5 items; all fields completed; items correctly prioritised | 5 | |
| B6 | RTO/RPO variance analysis: correctly calculated; correctly classified; appropriate management response stated | 4 | |
| | **Subtotal Output** | **30** | |

### C. SIKAP (Attitude) — 15 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| C1 | Works independently; makes decisions without unnecessary prompting from assessor | 5 | |
| C2 | Demonstrates analytical thinking: justifies RTO/RPO values, strategy choices, and risk ratings | 5 | |
| C3 | Presents findings professionally: explains decisions clearly and concisely during debrief | 5 | |
| | **Subtotal Attitude** | **15** | |

### D. KESELAMATAN (Safety) — 15 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| D1 | All documents handled as confidential: not left unattended; stored in designated folder only | 5 | |
| D2 | No real credentials, real IP addresses, or real personal data used in any training documents | 5 | |
| D3 | Lab environment accessed only within authorised scope; no unauthorised changes to lab infrastructure | 5 | |
| | **Subtotal Safety** | **15** | |

### E. ALAM SEKITAR (Environmental) — 10 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| E1 | Workstation (physical and digital) kept organised throughout assessment; files named correctly | 5 | |
| E2 | All templates and printed materials returned or properly stored/disposed of at end of assessment | 5 | |
| | **Subtotal Environmental** | **10** | |

---

## Ringkasan Markah / Score Summary

| Section | Maximum | Score |
|---------|---------|-------|
| A. Process | 30 | |
| B. Output | 30 | |
| C. Attitude | 15 | |
| D. Safety | 15 | |
| E. Environmental | 10 | |
| **TOTAL** | **100** | |

---

## Keputusan / Result

| | |
|---|---|
| **Lulus / Pass** (≥ 60 marks) | [ ] |
| **Gagal / Fail** (< 60 marks) | [ ] |

---

## Pengesahan / Verification

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Assessor 1 | | | |
| Assessor 2 (if applicable) | | | |
| Internal Verifier | | | |

---

## Ulasan / Comments

*(Assessor to provide specific feedback on strengths, areas for improvement, and any critical non-compliance observed. Comments must be written, not verbal only.)*

|  |
|---|
|  |
|  |
|  |
|  |