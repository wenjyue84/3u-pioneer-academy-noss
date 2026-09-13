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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C06 COMPUTER SYSTEM MAINTENANCE MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM MAINTENANCE REQUIREMENTS<br>2. DEVELOP COMPUTER SYSTEM MAINTENANCE PLAN<br>3. MANAGE COMPUTER SYSTEM MAINTENANCE WORK<br>4. MANAGE COMPUTER SYSTEM TROUBLESHOOTING ISSUES/FAILURES<br>5. PRODUCE COMPUTER SYSTEM MAINTENANCE MANAGEMENT REPORT |
| NO. KOD | IT-020-4:2013-C06/PA |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU MUDA (Light Blue) |

**TAJUK:** PA-maintenance-management

**TUJUAN:** Kertas rujukan untuk PA-maintenance-management.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. This is a MANAGEMENT PERFORMANCE examination. You will be assessed on your ability to manage the full computer system maintenance function — from requirements analysis through planning, work management, troubleshooting coordination, and reporting.
2. You will be given a scenario brief, simulated data packs, and access to a computer with office productivity software.
3. You will be assessed on: **Process** (how you manage the work), **Output** (the quality of your documents), **Attitude** (professionalism and communication), **Decision-making** (quality of judgements under simulated pressure), and **Documentation** (completeness and accuracy).
4. You must work independently. Consulting peers or external references is not permitted unless specified.
5. All outputs must be submitted as printed documents and/or computer files as directed by the assessor.

---

## Arahan kepada Penilai / Instructions to Assessor

- Provide each trainee with the scenario brief, data packs, and templates before the assessment begins.
- Allow a 10-minute reading period before the clock starts.
- Observe the trainee's decision-making process; record observations on the assessment rubric.
- Do NOT provide hints or guidance unless there is a safety concern.
- The assessor plays the role of the IT Manager. The trainee must escalate to the assessor when the scenario requires management escalation.
- Introduce the injected incidents (see below) at the specified times.
- Verify all submitted documents at the end of the assessment.

---

## Senario / Scenario Brief

**Organisation:** Agensi Pengurusan Maklumat Negeri (APMN) — a state government ICT agency

**IT Environment:**
- 3 application servers (Tier 1): core e-government portal, financial management system (FMS), email
- 1 domain controller (Tier 1)
- 60 staff workstations (Tier 3)
- 2 managed switches, 1 router, 1 firewall (Tier 2)
- 1 UPS system (server room)

**SLA Requirements:**
- Tier 1 servers: 99.5% availability; P1 response ≤ 30 minutes; P1 resolution ≤ 2 hours
- Tier 2 network devices: P2 response ≤ 1 hour; resolution ≤ 4 hours
- Planned maintenance window: every Saturday, 01:00–05:00

**Known Context:**
- The last full MRA was conducted 18 months ago
- The UPS battery is 3.5 years old (recommended replacement: 4 years)
- The FMS server has had 2 disk errors flagged in monitoring over the past 3 months (no action taken)
- PM compliance for the past quarter: 78% (below the 95% target)
- Budget remaining for the year: RM 22,000 (8 months elapsed of 12)

**Assessment Duration:** 4 hours

---

## Tugasan / Tasks

You must complete the following tasks in the order given. Allocate your time accordingly.

### Task 1 — Maintenance Requirements Analysis (WA1) — 45 minutes

Using the provided data pack (asset inventory, incident history, SLA document):

1. Classify all assets by criticality tier with justification
2. Calculate MTBF, MTTR, and Availability for the FMS server using the provided 12-month incident data
3. Complete a risk assessment matrix for the top 4 maintenance risks (Likelihood × Impact)
4. Produce a one-page MRA Gap Analysis identifying missing or inadequate maintenance activities

**Deliverable:** Completed MRA output (criticality table, MTBF/MTTR/Availability calculation, risk matrix, gap analysis)

---

### Task 2 — Maintenance Plan Development (WA2) — 45 minutes

1. Develop a 3-month maintenance calendar (next quarter) for all asset classes, scheduled within the approved maintenance window. Flag any scheduling conflicts.
2. Write a brief SOP outline (minimum 8 steps) for the FMS server quarterly PM. Include: purpose, prerequisites, two safety precautions, step-by-step procedure, acceptance criteria, and documentation requirement.
3. Prepare a resource plan for the quarter: staffing hours, tools, and spare parts required (include UPS battery replacement).

**Deliverable:** 3-month maintenance calendar, SOP outline, resource plan

---

### Task 3 — Maintenance Work Management (WA3) — 30 minutes

The assessor injects the following scenario at 60 minutes into the assessment:

**Injected Incident A:** "It is Saturday 02:15 during the planned maintenance window. Technician reports that during the FMS server quarterly PM, a SATA data cable was accidentally disconnected and the server failed to reboot. The server is currently offline."

1. Classify and log this as an incident (priority, scope, impact)
2. Raise an emergency work order
3. Assign the technician to restore the server (write the task instruction)
4. Draft an escalation message to the IT Manager (assessor)
5. Document the deviation and the action taken

**Deliverable:** Incident log, emergency work order, task instruction, escalation message, deviation record

---

### Task 4 — Troubleshooting and Failure Management (WA4) — 45 minutes

The assessor injects the following scenario at 90 minutes into the assessment:

**Injected Incident B:** "At 09:10 on Monday morning, the e-government portal is unreachable. 150 members of the public cannot submit applications. The portal server's monitoring dashboard shows CPU utilisation at 100% since 08:55. Investigation reveals a runaway process caused by a recent patch applied on Friday without following the change management procedure."

1. Classify this as P1. Complete the incident management form.
2. Describe the structured troubleshooting steps you would direct your team to take (minimum 5 steps).
3. Identify and document the workaround (restoring service while investigating root cause).
4. Conduct a 5 Whys RCA. Identify the root cause and at least 2 corrective and 2 preventive actions.
5. Write the Post-Incident Report.

**Deliverable:** Incident form, troubleshooting plan, workaround decision record, 5 Whys RCA, Post-Incident Report

---

### Task 5 — Maintenance Management Report (WA5) — 45 minutes

Using the simulated monthly data pack provided by the assessor:

1. Calculate all KPIs for the month (Availability, PM Compliance, MTTR-P1, Repeat Incident Rate, First-Time Fix Rate, Budget Utilisation)
2. Assign RAG status to each KPI; provide root cause explanation for Amber/Red items
3. Write the Recommendations section (minimum 3 recommendations)
4. Write the Executive Summary (maximum 1 page)
5. Present the Executive Summary verbally to the assessor (IT Manager) in 3–5 minutes

**Deliverable:** KPI table with RAG, recommendations, executive summary; verbal presentation

---

## Rubrik Penilaian / Assessment Rubric

### A. PROSES PENGURUSAN (Management Process) — 30 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| A1 | MRA conducted systematically using correct methodology (criticality classification, MTBF/MTTR, risk matrix, gap analysis) | 6 | |
| A2 | Maintenance plan developed with realistic schedule, valid SOP, and resourced plan | 6 | |
| A3 | Maintenance work managed correctly (incident logged, WO raised, technician assigned, escalation sent, deviation recorded) | 6 | |
| A4 | Troubleshooting managed systematically (P1 classified, structured steps, workaround implemented, RCA completed) | 6 | |
| A5 | Report compiled with correct KPI calculations, RAG status, and actionable recommendations | 6 | |
| | **Subtotal Process** | **30** | |

### B. HASIL KERJA (Output Quality) — 30 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| B1 | MRA output is complete, accurate, and professionally structured | 6 | |
| B2 | Maintenance plan (calendar, SOP, resource plan) is complete and operationally realistic | 6 | |
| B3 | Work management documents (incident log, WO, escalation, deviation record) are complete and accurate | 6 | |
| B4 | Troubleshooting documents (RCA, Post-Incident Report) are complete and correctly structured | 6 | |
| B5 | Monthly report (KPI table, RAG, recommendations, executive summary) is complete, accurate, and management-appropriate | 6 | |
| | **Subtotal Output** | **30** | |

### C. SIKAP DAN KOMUNIKASI (Attitude and Communication) — 15 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| C1 | Works independently and manages time effectively within the 4-hour assessment | 5 | |
| C2 | Demonstrates sound management judgement in responses to injected incidents (priority, escalation, workaround) | 5 | |
| C3 | Verbal presentation of executive summary is clear, structured, and targeted at a management audience | 5 | |
| | **Subtotal Attitude** | **15** | |

### D. KEPUTUSAN DAN TINDAKAN (Decision-Making and Action) — 15 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| D1 | Incident A managed with correct priority, escalation, and deviation documentation | 5 | |
| D2 | Incident B classified as P1; workaround implemented promptly; RCA reaches the true root cause | 5 | |
| D3 | Recommendations are specific, actionable, and directly supported by the report data | 5 | |
| | **Subtotal Decision-Making** | **15** | |

### E. DOKUMENTASI (Documentation) — 10 marks

| No. | Kriteria / Criteria | Markah / Marks | Penilaian / Score |
|-----|---------------------|----------------|-------------------|
| E1 | All documents use professional language; structured with headings, tables, and correct terminology | 5 | |
| E2 | All documents are complete (no missing sections) and submitted within the allocated time | 5 | |
| | **Subtotal Documentation** | **10** | |

---

## Ringkasan Markah / Score Summary

| Section | Maximum | Score |
|---------|---------|-------|
| A. Management Process | 30 | |
| B. Output Quality | 30 | |
| C. Attitude and Communication | 15 | |
| D. Decision-Making and Action | 15 | |
| E. Documentation | 10 | |
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

*(Assessor to provide feedback on management competency demonstrated, quality of decision-making under pressure, documentation quality, and any critical non-compliance observed.)*

|  |
|---|
|  |
|  |
|  |