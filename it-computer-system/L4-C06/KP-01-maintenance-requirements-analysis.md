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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C06 COMPUTER SYSTEM MAINTENANCE MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM MAINTENANCE REQUIREMENTS<br>2. DEVELOP COMPUTER SYSTEM MAINTENANCE PLAN<br>3. MANAGE COMPUTER SYSTEM MAINTENANCE WORK<br>4. MANAGE COMPUTER SYSTEM TROUBLESHOOTING ISSUES/FAILURES<br>5. PRODUCE COMPUTER SYSTEM MAINTENANCE MANAGEMENT REPORT |
| NO. KOD | IT-020-4:2013-C06/KP(1/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-maintenance-requirements-analysis

**TUJUAN:** Kertas rujukan untuk KP-01-maintenance-requirements-analysis.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify and classify the maintenance requirements of a computer system environment
2. Distinguish between corrective, preventive, predictive, and condition-based maintenance
3. Conduct a maintenance needs assessment using structured methodologies
4. Interpret Service Level Agreements (SLA) and translate them into maintenance obligations
5. Prioritise maintenance tasks based on criticality, risk, and operational impact

---

## 1.0 Introduction to Maintenance Requirements Analysis

At Level 4, the computer system administrator is responsible not merely for carrying out maintenance tasks, but for managing the entire maintenance function — planning, resourcing, scheduling, and overseeing a team of technicians. The foundation of this management role is a thorough analysis of maintenance requirements: understanding what systems exist, what condition they are in, what level of service is required, and what maintenance activities must be performed to sustain that service.

Maintenance requirements analysis (MRA) is the systematic process of identifying, classifying, and prioritising all maintenance needs for a computer system environment. It produces the inputs to the maintenance plan and forms the basis for resource allocation, SLA compliance, and KPI reporting.

---

## 2.0 Types of Maintenance

| Type | Bahasa Malaysia | Description | When Applied |
|------|-----------------|-------------|--------------|
| Corrective (CM) | Penyelenggaraan Pembetulan | Restore a failed system to operational status | After a fault or failure occurs |
| Preventive (PM) | Penyelenggaraan Pencegahan | Scheduled activities to prevent failures | At fixed time intervals |
| Predictive (PdM) | Penyelenggaraan Ramalan | Monitor system condition to predict failure | Based on condition indicators |
| Condition-Based (CBM) | Penyelenggaraan Berdasarkan Keadaan | Trigger maintenance when a threshold is crossed | When monitoring data exceeds threshold |
| Proactive | Penyelenggaraan Proaktif | Eliminate root causes of failure before they occur | During system design and change management |

For most enterprise computer system environments, a combination of preventive and predictive maintenance is the most cost-effective strategy. Corrective maintenance should be minimised through robust PM/PdM programmes.

---

## 3.0 Maintenance Needs Assessment Process

A maintenance manager conducts a needs assessment using the following structured steps:

### Step 1: Asset Inventory and Classification

Compile a complete inventory of all computer systems and infrastructure under management. Classify each asset by:

- **Criticality tier:** Mission-critical, business-critical, or standard
- **Asset type:** Server, desktop, laptop, networking device, storage, peripheral
- **Age and warranty status:** Under warranty, post-warranty, end-of-life
- **Current condition:** Good, degraded, at-risk

| Criticality Tier | Description | Maintenance Priority |
|------------------|-------------|----------------------|
| Tier 1 — Mission-Critical | Systems whose failure directly halts core business operations (e.g. ERP servers, domain controllers) | Highest — 24/7 monitoring, redundancy required |
| Tier 2 — Business-Critical | Systems whose failure significantly impairs operations (e.g. file servers, email servers) | High — scheduled preventive maintenance |
| Tier 3 — Standard | End-user workstations, non-critical peripherals | Normal — routine scheduled maintenance |

### Step 2: Failure History Analysis

Review the maintenance history and helpdesk records for each asset:

- Frequency of past failures (Mean Time Between Failures, MTBF)
- Types of failures (hardware, software, network, power)
- Average repair time (Mean Time To Repair, MTTR)
- Impact of past failures on operations

High failure frequency on a specific asset class signals a need for increased PM frequency or asset replacement.

### Step 3: SLA and Compliance Review

Review all Service Level Agreements relevant to the computer system environment:

- Uptime commitments (e.g. 99.5% availability = maximum 43.8 hours downtime per year)
- Response time obligations (e.g. critical fault: respond within 1 hour, resolve within 4 hours)
- Scheduled maintenance windows permitted
- Reporting and audit obligations

The maintenance requirements must be designed to ensure SLA compliance at all times.

### Step 4: Risk Assessment

Assess the risk of each identified maintenance gap:

| Risk Factor | Description |
|-------------|-------------|
| Likelihood | Probability of failure occurring if maintenance is not performed |
| Impact | Consequence of failure — financial, operational, reputational |
| Detectability | How quickly the failure can be detected and responded to |
| Risk Score | Likelihood × Impact (use a 1–5 scale for each) |

Prioritise maintenance tasks with the highest risk scores.

### Step 5: Maintenance Gap Analysis

Compare current maintenance activities against identified requirements:

- Identify activities that are currently not performed but should be
- Identify activities that are over-maintained (wasteful)
- Identify activities where frequency needs adjustment

---

## 4.0 Key Maintenance Metrics

| Metric | Formula / Definition | Significance |
|--------|----------------------|--------------|
| MTBF (Mean Time Between Failures) | Total operating time ÷ Number of failures | Higher is better; indicates reliability |
| MTTR (Mean Time To Repair) | Total repair time ÷ Number of repairs | Lower is better; indicates responsiveness |
| Availability | MTBF ÷ (MTBF + MTTR) × 100% | Must meet SLA uptime target |
| PM Compliance Rate | PM tasks completed on schedule ÷ PM tasks scheduled × 100% | Indicates discipline of maintenance programme |
| Maintenance Cost Ratio | Maintenance cost ÷ Asset replacement value × 100% | Industry benchmark: 2–5% per annum |

---

## 5.0 SLA Interpretation for Maintenance Planning

A Service Level Agreement (SLA / Perjanjian Tahap Perkhidmatan) is a formal contract or organisational policy that defines the required service levels for computer systems. The maintenance manager must translate SLA terms into specific maintenance obligations:

| SLA Term | Maintenance Implication |
|----------|-------------------------|
| 99.9% uptime (8.76 hrs downtime/year) | Mission-critical systems must have redundancy and 24/7 monitoring |
| P1 fault: resolve within 2 hours | Technician on-call roster must be active; spare parts must be on-hand |
| Planned maintenance window: Saturday 01:00–05:00 | All disruptive maintenance must be scheduled within this window |
| Monthly availability report to management | KPI data collection and reporting system must be in place |

---

## 6.0 Stakeholder Consultation

Maintenance requirements cannot be determined by the IT department alone. The maintenance manager must consult:

- **Business unit managers:** Understand operational schedules and critical business periods when maintenance downtime must be avoided
- **End users:** Identify recurring performance complaints that may indicate maintenance gaps
- **Senior management:** Confirm budget envelope and risk tolerance
- **Vendors and contractors:** Obtain manufacturer-recommended maintenance schedules and firmware update advisory

---

## 7.0 Documenting the Maintenance Requirements Analysis

The output of MRA is a formal document containing:

1. Asset inventory with criticality classification
2. Failure history summary per asset class
3. SLA obligations and derived maintenance requirements
4. Risk assessment matrix
5. Maintenance gap analysis
6. Prioritised list of required maintenance activities
7. Recommended maintenance strategy (PM/PdM/CBM mix)
8. Resource and budget implications

This document is reviewed and approved by the IT Manager and becomes the authoritative input to the Maintenance Plan.

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCU 6
- ISO 55001:2014 Asset Management — Requirements
- ITIL 4 Foundation — Service Management Practices (Service Level Management)
- CompTIA Server+ Study Guide — Maintenance and Troubleshooting
- Jabatan Perkhidmatan Awam Malaysia — Garis Panduan Pengurusan Aset ICT