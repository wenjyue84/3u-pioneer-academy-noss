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
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KK(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-producing-disaster-recovery-management-report

**TUJUAN:** Kertas rujukan untuk KK-04-producing-disaster-recovery-management-report.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Compile a complete Post-Incident Report (PIR) and management summary based on a simulated disaster recovery event, including timeline reconstruction, root cause analysis, RTO/RPO variance analysis, and corrective action plan.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

---

## Objektif / Objective

Produce a professional, management-ready Disaster Recovery Management Report (Post-Incident Report) using data from the simulated disaster recovery exercise conducted in KK(3/4), supplemented by a provided incident data set.

---

## Tempoh / Duration

4 hours (distributed across WA4 practical sessions)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | DR Test Report and implementation log from KK(3/4) | 1 |
| 2 | Supplementary incident data sheet (provided by instructor) | 1 |
| 3 | PIR template document | 1 |
| 4 | CAP tracking spreadsheet template | 1 |
| 5 | RTO/RPO performance calculation worksheet | 1 |
| 6 | Computer with word processing and spreadsheet software | 1 |

---

## Langkah Keselamatan / Safety Precautions

- All report content references simulated data only — do not include any real organisational or personal data
- Final report documents must be stored in the designated training folder; remove from personal devices after assessment
- Spell-check and review all content before submission — professional language is required at Level 5

---

## Senario / Scenario

**Incident Reference: INC-2026-047**

Based on the simulated disaster exercise from KK(3/4), you are now the DR Coordinator of Syarikat Logistik Sejahtera. You must produce the formal Post-Incident Report for submission to the company's CEO and IT Director.

**Supplementary incident data provided by instructor:**

| Data Point | Value |
|-----------|-------|
| Incident start (primary site power failure) | 09:00 |
| Monitoring alert generated | 09:03 |
| IT Operations notified | 09:07 |
| DR Coordinator declares Level 3 disaster | 09:45 |
| DR team assembled | 10:00 |
| Network failover completed | 10:28 |
| Database restoration completed | 11:15 |
| WMS application confirmed operational | 11:52 |
| Recovery declaration issued | 12:10 |
| Target RTO for WMS | 4 hours |
| Target RPO for WMS | 1 hour |
| Latest backup applied timestamp | 08:00 (same day) |
| Root cause (preliminary) | UPS batteries degraded; generator auto-start failure |
| Estimated revenue impact | RM 85,000 (3+ hours of operations affected) |

---

## Prosedur / Procedures

### Bahagian A: Timeline Reconstruction / Pembinaan Semula Garis Masa (30 min)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| A1 | Using the supplementary incident data and your implementation log from KK(3/4), reconstruct a complete incident timeline table. Include: timestamp, event description, action taken, and responsible party. Minimum 12 timeline entries. |
| A2 | Calculate: (a) Actual RTO achieved; (b) Actual RPO achieved; (c) MTTD (Mean Time to Detect); (d) MTTR (Mean Time to Respond). Show your calculations clearly. |
| A3 | Classify each metric as: PASS (within target) / MINOR VARIANCE (< 25% over) / MAJOR VARIANCE (> 25% over). |

### Bahagian B: Root Cause Analysis / Analisis Punca Asas (45 min)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| B1 | Apply the 5 Whys method to the primary root cause (UPS battery failure leading to uncontrolled shutdown). Document all 5 Why levels with answers. |
| B2 | Identify at least TWO (2) contributing factors that worsened the impact (e.g. no DR plan; backup stored on-site only). |
| B3 | State the verified root cause in one clear sentence. |

### Bahagian C: PIR Sections — Scope, Impact, and Effectiveness (45 min)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| C1 | Write Section 2 (Scope of Impact): list all systems affected, number of users affected (estimate based on company scenario), and financial impact based on the provided data. |
| C2 | Write Section 6 (Effectiveness Assessment): assess each of the following — DRP activation process, DR team communication, technical recovery steps, and user communication. Rate each as Effective / Partially Effective / Ineffective and provide a brief justification (2–3 sentences each). |
| C3 | Write Section 10 (Lessons Learnt): document minimum FOUR (4) specific lessons, each with a corresponding improvement recommendation. |

### Bahagian D: Corrective Action Plan / Pelan Tindakan Pembetulan (45 min)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| D1 | Identify minimum FIVE (5) corrective actions arising from the incident and tabletop findings. |
| D2 | For each corrective action, complete all fields in the CAP table: Item ID, Issue Description, Root Cause, Corrective Action, Owner (role), Target Date, Priority (High/Medium/Low), Status (Open). |
| D3 | Prioritise the CAP items: rank from most urgent to least urgent. Justify the top 2 priorities. |

### Bahagian E: Executive Summary and Report Finalisation (45 min)

| Langkah | Arahan / Instruction |
|---------|---------------------|
| E1 | Write the Executive Summary (Section 1): 200–300 words, suitable for CEO-level readership. Include: what happened, when, systems affected, recovery performance vs. targets, financial impact, and the 2 most important corrective actions. Use professional, non-technical language. |
| E2 | Complete the PIR cover page: incident reference number, date of incident, date of report, classification (Confidential), and author details. |
| E3 | Compile all sections into the final PIR document. Ensure consistent formatting, professional language, and correct section numbering. |
| E4 | Prepare a 10-minute management presentation (PowerPoint or equivalent): 5–6 slides covering incident summary, recovery performance, root cause, top 3 corrective actions. |
| E5 | Submit the completed PIR and presentation to the instructor. |

---

## Hasil Jangkaan / Expected Outcome

A completed Post-Incident Report containing:
- Incident timeline (minimum 12 entries) with calculated RTO, RPO, MTTD, and MTTR
- 5 Whys root cause analysis with verified root cause statement
- Scope, impact, and effectiveness assessment (Sections 2 and 6)
- Minimum 4 lessons learnt with improvement recommendations
- CAP table with minimum 5 items, all fields completed, prioritised
- Executive Summary (200–300 words, CEO-level language)
- Management presentation (5–6 slides)

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Timeline complete (minimum 12 entries); RTO, RPO, MTTD, MTTR calculated correctly | [ ] Yes  [ ] No |
| 2 | 5 Whys RCA completed; root cause clearly stated | [ ] Yes  [ ] No |
| 3 | Scope and impact documented; financial impact included | [ ] Yes  [ ] No |
| 4 | Effectiveness assessment covers all 4 areas with justification | [ ] Yes  [ ] No |
| 5 | Minimum 4 lessons learnt with specific improvement recommendations | [ ] Yes  [ ] No |
| 6 | CAP table: minimum 5 items; all fields complete; items prioritised | [ ] Yes  [ ] No |
| 7 | Executive Summary: 200–300 words; professional language; CEO-appropriate | [ ] Yes  [ ] No |
| 8 | Management presentation prepared (5–6 slides); submitted with PIR | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |