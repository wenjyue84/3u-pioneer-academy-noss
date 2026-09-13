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

## KERTAS PENERANGAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KP(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-disaster-recovery-report-production

**TUJUAN:** Kertas rujukan untuk KP-04-disaster-recovery-report-production.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify the mandatory components of a Disaster Recovery Management Report
2. Compile and present post-incident data including actual RTO/RPO achieved, system recovery timeline, and issues encountered
3. Conduct a structured post-incident review (PIR) and document root cause findings
4. Write executive-level DR summary reports for senior management and regulatory bodies
5. Develop and track corrective action plans (CAP) arising from DR incidents and tests

---

## 1.0 Types of DR Reports / Jenis-Jenis Laporan DR

DR reporting occurs at two primary stages: after a DR **test/drill** and after an **actual disaster event**. Both report types share a common structure but differ in scope and urgency.

| Report Type | Trigger | Primary Audience | Urgency |
|-------------|---------|-----------------|---------|
| **DR Test Report / Laporan Ujian DR** | Completion of any scheduled DR test or drill | IT management, DR Coordinator, Internal Audit | Within 5 business days of test |
| **Post-Incident Report (PIR) / Laporan Pasca-Insiden** | Resolution of an actual disaster event | Senior management, Board, regulators | Within 10 business days of recovery |
| **DR Annual Review Report** | Annual DRP review cycle | IT Director, CEO, Board Risk Committee | Annually |
| **Regulatory Report / Laporan Kawal Selia** | Mandatory notification to regulators (if applicable) | Regulators (e.g. Bank Negara, SC, MCMC) | Per regulatory timeline (often 24–72 hours initial notification) |

---

## 2.0 Post-Incident Report (PIR) Structure / Struktur Laporan Pasca-Insiden

### 2.1 Mandatory Sections / Bahagian Wajib

The PIR is the most comprehensive DR report. It must contain:

| Section | Title | Content |
|---------|-------|---------|
| 1 | Incident Summary / Ringkasan Insiden | Incident reference number, date and time of occurrence, date and time of recovery, brief description of disaster event |
| 2 | Scope of Impact / Skop Impak | Systems affected; users/departments affected; geographic scope |
| 3 | Timeline / Garis Masa | Chronological log of all actions from incident detection to recovery declaration |
| 4 | Root Cause Analysis / Analisis Punca Asas | Identified root cause(s); contributing factors; evidence |
| 5 | Recovery Performance / Prestasi Pemulihan | Actual RTO achieved vs. target; actual RPO achieved vs. target; data loss quantification |
| 6 | Effectiveness Assessment / Penilaian Keberkesanan | Assessment of DRP activation, team response, communication, and technical recovery steps |
| 7 | Issues and Gaps / Isu dan Jurang | Problems encountered during recovery; deviations from the DRP; near-misses |
| 8 | Corrective Action Plan (CAP) | Specific actions to prevent recurrence or improve response; owner; due date |
| 9 | Financial Impact / Impak Kewangan | Estimated cost of downtime; recovery costs; data loss value |
| 10 | Lessons Learnt / Pengajaran Dipelajari | Key insights for improving DR planning, training, and technology |
| 11 | Approval / Kelulusan | Signatures of DR Coordinator, IT Director, CEO |

### 2.2 Incident Timeline Format / Format Garis Masa Insiden

The timeline section is critical for accountability and future improvement. It must be precise:

| Timestamp | Event | Action Taken | By Whom |
|-----------|-------|-------------|---------|
| 08:14 | Power failure detected at primary data centre | Monitoring alert generated | Automated system |
| 08:16 | IT Operations alerted; initial investigation begins | Contacted facilities management | NOC Engineer |
| 08:30 | UPS battery estimated 15 minutes remaining; generator failed to start | Escalated to IT Manager | NOC Engineer |
| 08:45 | IT Manager declares Level 3 alert; DR Coordinator notified | DRP activated | IT Manager |
| 09:00 | DR team assembled at command centre | Conference bridge established | DR Coordinator |
| 09:15 | Network infrastructure at DR site verified online | DNS failover initiated | Network Engineer |
| 10:30 | Tier 1 systems (AD, ERP database) restored at DR site | Database recovery completed | DBA |
| 11:45 | All Tier 1 systems validated and operational | Recovery declaration issued | DR Coordinator |
| **RTO achieved:** 3 hours 31 minutes | **Target RTO:** 4 hours | **Status: PASS** | |

---

## 3.0 Root Cause Analysis (RCA) / Analisis Punca Asas

### 3.1 RCA Methodology

Root Cause Analysis is a structured investigation technique to identify the underlying cause(s) of an incident, not merely the immediate symptom. DR reports must include a formal RCA.

**Common RCA methods used in IT DR:**

| Method | Description |
|--------|-------------|
| **5 Whys / 5 Mengapa** | Ask "Why?" five times in succession to drill down from symptom to root cause |
| **Fishbone Diagram (Ishikawa)** | Visual tool mapping causes under categories: People, Process, Technology, Environment |
| **Fault Tree Analysis (FTA)** | Top-down deductive analysis mapping how top-level failures can result from combinations of lower-level events |

### 3.2 Example: 5 Whys Application

**Incident:** Tier 1 ERP system was unavailable for 3.5 hours.

| Why # | Question | Answer |
|-------|----------|--------|
| Why 1 | Why was the ERP system unavailable? | The primary server failed to start after a power interruption |
| Why 2 | Why did the server fail to start after power interruption? | The UPS did not maintain power long enough for a graceful shutdown |
| Why 3 | Why did the UPS not maintain sufficient power? | The UPS battery had degraded below 60% capacity |
| Why 4 | Why was the battery degraded? | The UPS had not been replaced within the recommended 3-year cycle |
| Why 5 | Why was it not replaced? | No preventive maintenance schedule existed for UPS units |
| **Root Cause** | No preventive maintenance schedule for UPS batteries | |
| **Corrective Action** | Implement quarterly UPS health checks; schedule battery replacement per manufacturer cycle | |

---

## 4.0 Recovery Performance Measurement / Pengukuran Prestasi Pemulihan

### 4.1 KPIs for DR Reporting / KPI Pelaporan DR

The following Key Performance Indicators (KPIs) must be reported after every incident and test:

| KPI | Definition | Measurement Method |
|-----|------------|-------------------|
| **Actual RTO / RTO Sebenar** | Time from disaster declaration to recovery declaration | Timestamp log: activation time to validation sign-off |
| **Actual RPO / RPO Sebenar** | Amount of data lost (measured in time) | Database log review; compare recovered data timestamp to incident timestamp |
| **Mean Time to Detect (MTTD)** | Average time from incident occurrence to detection | Monitoring alert timestamp vs. incident start time |
| **Mean Time to Respond (MTTR)** | Average time from detection to DR activation | Alert timestamp to DRP activation declaration |
| **Recovery Success Rate** | Percentage of systems recovered within target RTO | (Systems meeting RTO / Total systems) × 100% |
| **Data Loss Volume** | Actual volume of data lost (GB or transaction count) | Pre and post recovery data comparison |

### 4.2 RTO/RPO Variance Analysis

When actual RTO or RPO exceeds targets, a variance analysis must be documented:

| Variance Type | Example | Required Action |
|---------------|---------|----------------|
| Minor variance (< 10% over target) | Target RTO 4 hrs; achieved 4 hrs 20 min | Document; review contributing factors; no immediate DRP change required |
| Moderate variance (10–25% over) | Target RTO 4 hrs; achieved 5 hrs | Root cause analysis; update DRP; schedule remedial training |
| Major variance (> 25% over) | Target RTO 4 hrs; achieved 6 hrs | Formal corrective action plan; management review; possible strategy change (e.g. upgrade to hot site) |

---

## 5.0 Corrective Action Plan (CAP) / Pelan Tindakan Pembetulan

### 5.1 CAP Structure

Every issue identified in the DR report must have a corresponding corrective action:

| CAP Item | Issue Description | Root Cause | Corrective Action | Owner | Target Date | Status |
|----------|------------------|-----------|-------------------|-------|-------------|--------|
| CAP-001 | DNS failover took 45 min instead of 15 min | TTL values not pre-reduced | Reduce all critical DNS TTLs to 300 seconds; document in DRP | Network Engineer | 30 days | Open |
| CAP-002 | DBA contacted 20 min after activation | Contact list outdated | Update DR contact list; verify quarterly | DR Coordinator | 14 days | Open |
| CAP-003 | DR site firewall rules incomplete | Config backup was 6 months old | Automate firewall config backup weekly; store in cloud | Security Officer | 21 days | Open |

### 5.2 CAP Tracking and Closure

The DR Coordinator is responsible for tracking all CAP items:
- Monthly CAP status review meeting
- Each item closed only when remediation is verified (not merely when action is "taken")
- Closed CAP items documented with evidence (e.g. screenshot of updated contact list, configuration export)
- Outstanding CAPs reported to IT Director at the monthly IT governance meeting

---

## 6.0 Regulatory and Compliance Reporting / Pelaporan Kawal Selia dan Pematuhan

### 6.1 Regulatory Requirements in Malaysia

Organisations in regulated sectors must report significant IT incidents to the relevant authority:

| Sector | Regulator | Reporting Requirement |
|--------|-----------|----------------------|
| Banking and Finance | Bank Negara Malaysia (BNM) | BNM RMiT (Risk Management in Technology) — incidents must be reported within 1 hour; detailed report within 5 business days |
| Capital Markets | Securities Commission (SC) | Cyber incidents affecting market operations reported within 24 hours |
| Telecommunications | MCMC | Significant service outages reported per MCMC licensing conditions |
| Government Agencies | MAMPU / CyberSecurity Malaysia (CSM) | Major cyber incidents reported to MyCERT within 24 hours |
| Healthcare | Ministry of Health (KKM) | Patient data breaches under PDPA reported to JPDP |

### 6.2 Regulatory Report Content

Regulatory reports typically require:
- Incident date, time, duration
- Nature of incident and systems affected
- Number of users/customers affected
- Root cause (if determined)
- Actions taken to restore service
- Measures to prevent recurrence
- Contact person with full details

---

## 7.0 DR Annual Review Report / Laporan Semakan Tahunan DR

### 7.1 Purpose and Content

The Annual DR Review Report assesses the overall state of the DR programme for the year:

| Section | Content |
|---------|---------|
| DR tests conducted | Summary of all tests, dates, types, outcomes |
| Actual incidents | Summary of any real disaster events and response performance |
| DRP changes made | What was updated and why |
| Training completed | DR awareness and drill participation by team members |
| Infrastructure changes | New systems, cloud migrations, decommissions affecting DR |
| Budget vs. actual | DR spending vs. budget; investment recommendations for next year |
| Risk posture | Current risk register update; new threats identified |
| Next year plan | Proposed test schedule, investment, and improvement priorities |

### 7.2 Report Presentation to Management / Pembentangan kepada Pengurusan

The Annual DR Review is typically presented at the Board Risk Committee or equivalent governance body:
- Presented by the IT Director or CISO
- Supported by dashboards showing KPI trends (RTO/RPO over time, test pass rate)
- Management must formally acknowledge and approve the next year's DR plan and budget

---

## Rujukan / References

- ISO 22301:2019 — Business Continuity Management Systems — Requirements
- Bank Negara Malaysia — Risk Management in Technology (RMiT) Policy Document
- CyberSecurity Malaysia — Incident Reporting Guidelines
- NIST SP 800-61 Rev.2 — Computer Security Incident Handling Guide
- NOSS IT-020-5:2013 CoCU 4 — Disaster Recovery Management
- PDPA 2010 (Personal Data Protection Act) — Data Breach Obligations