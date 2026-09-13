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
| NO. KOD | IT-020-4:2013-C06/KP(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-troubleshooting-issues-failures-management

**TUJUAN:** Kertas rujukan untuk KP-04-troubleshooting-issues-failures-management.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Distinguish between incident management and problem management in a computer system environment
2. Apply a structured troubleshooting methodology at the management level
3. Coordinate a team response to major system failures, including escalation and communication
4. Manage root cause analysis (RCA) processes and implement corrective actions
5. Maintain a known-error database (KEDB) and monitor recurring failure patterns

---

## 1.0 Incident vs Problem Management

At Level 3, a technician troubleshoots individual faults. At Level 4, the maintenance manager manages the system-wide response to failures and ensures that the underlying causes are permanently resolved. This distinction is captured in the ITIL framework:

| Concept | Definition | Focus |
|---------|------------|-------|
| Incident (Insiden) | Any unplanned interruption or degradation of a computer system or service | Restore service as quickly as possible |
| Problem (Masalah) | The underlying cause of one or more incidents | Identify and eliminate the root cause |
| Known Error (Ralat Diketahui) | A problem for which the root cause and a workaround are documented | Manage and monitor until permanently resolved |

The maintenance manager is responsible for both incident coordination (managing the immediate response) and problem management (ensuring root causes are found and fixed).

---

## 2.0 Incident Priority and Escalation Framework

Every incoming fault report must be assigned a priority level based on its impact and urgency:

| Priority | Classification | Impact | Target Response | Target Resolution |
|----------|---------------|--------|-----------------|-------------------|
| P1 | Critical | Core business systems down; multiple users affected | 15 minutes | 2 hours |
| P2 | High | Significant function impaired; workaround available | 30 minutes | 4 hours |
| P3 | Medium | Single user or non-critical system affected | 2 hours | 1 business day |
| P4 | Low | Minor issue; cosmetic or intermittent | 4 hours | 3 business days |

### Escalation Matrix

| Trigger | Escalation To | Action |
|---------|--------------|--------|
| P1 incident not resolved within 1 hour | IT Manager | Authorise additional resources; vendor escalation |
| P1 incident not resolved within 2 hours | Senior Management | Business impact communication; crisis management |
| P2 incident becoming P1 (scope expanding) | IT Manager | Re-prioritise and resource |
| Contractor/vendor not responding | IT Manager → Procurement | Activate SLA penalty clause |
| Safety risk identified | Safety Officer | Stop work; initiate safety protocol |

---

## 3.0 Structured Troubleshooting Methodology

The maintenance manager leads the team through a structured troubleshooting process to ensure faults are resolved systematically rather than through trial and error:

### Step 1: Identify and Define the Problem

- Gather symptoms from the user, helpdesk ticket, and monitoring alerts
- Confirm the scope: which systems, how many users, since when?
- Distinguish between symptoms and the probable cause

### Step 2: Establish a Theory of Probable Cause

- Consult the maintenance history for the affected asset
- Review recent changes (patching, hardware replacement, configuration changes)
- Apply the OSI model layering approach for network-related faults (Physical → Data Link → Network → Transport → Session → Presentation → Application)
- Consult the Known Error Database (KEDB) for matching entries

### Step 3: Test the Theory

- Assign the most competent available technician to test the theory
- Test one change at a time to isolate variables
- Document the result of each test step

### Step 4: Establish a Plan of Action

- Once the root cause is confirmed, develop a remediation plan
- Confirm whether a temporary workaround is needed to restore service while the permanent fix is prepared
- Estimate the time and resources required
- Obtain manager/IT Manager approval if the fix is disruptive (requires downtime)

### Step 5: Implement the Solution and Verify

- Execute the fix as per the approved plan
- Test the system after fixing to confirm the fault is resolved
- Verify that no new faults were introduced by the fix
- Obtain user confirmation that service is restored

### Step 6: Document and Close

- Record all findings, actions, and test results in the incident/work order record
- If a new problem root cause was identified, raise a Problem Record
- Update the KEDB if applicable
- Close the incident and notify the user

---

## 4.0 Root Cause Analysis (RCA)

Root Cause Analysis (Analisis Punca Asal) is conducted after a major incident (P1/P2) or when a fault recurs repeatedly. The purpose is to identify the fundamental cause — not just the immediate trigger.

### 4.1 RCA Techniques

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| 5 Whys (5 Kenapa) | Ask "why" repeatedly until the root cause is reached | Simple to moderate complexity incidents |
| Fishbone (Ishikawa) Diagram | Map causes across categories (People, Process, Technology, Environment) | Complex incidents with multiple potential causes |
| Fault Tree Analysis | Logical diagram of failure pathways | Safety-critical or mission-critical incidents |
| Change Analysis | Review all changes made before the incident | When a recent change is suspected as the cause |

### 4.2 RCA Process

1. Assemble an RCA team: maintenance manager + relevant technicians + vendor (if applicable)
2. Establish a timeline of events leading to the incident
3. Apply selected RCA technique to identify the root cause
4. Distinguish the root cause from contributing factors and symptoms
5. Develop corrective actions to eliminate the root cause
6. Develop preventive actions to reduce the likelihood of similar incidents
7. Assign owners and target dates for each action
8. Produce a written RCA report for management review

### 4.3 RCA Report Structure

| Section | Content |
|---------|---------|
| Incident summary | What happened, when, how long, impact |
| Timeline | Chronological sequence of events |
| Root cause | The fundamental cause identified |
| Contributing factors | Factors that worsened the incident but are not the root cause |
| Corrective actions | Specific actions to fix the root cause (with owner and date) |
| Preventive actions | Actions to prevent recurrence (with owner and date) |
| Lessons learned | Insights for improving maintenance and operations |

---

## 5.0 Known Error Database (KEDB)

The KEDB (Pangkalan Data Ralat Diketahui) is a structured record of problems for which the root cause is known but a permanent fix has not yet been implemented. It contains:

| Field | Description |
|-------|-------------|
| Known Error ID | Unique reference |
| Problem description | Symptoms and affected systems |
| Root cause | Identified root cause |
| Workaround | Temporary fix to restore service when the error occurs |
| Permanent fix status | Planned, in progress, or deferred |
| Impact | What is affected and by how much |
| Frequency | How often this error is encountered |

The KEDB enables faster incident resolution: when a matching known error is found, the technician applies the workaround immediately rather than spending time investigating.

---

## 6.0 Recurring Failure Pattern Monitoring

The maintenance manager monitors failure patterns to detect systemic problems:

- Track incidents by asset type, location, and failure category over time
- Generate monthly trend reports from the CMMS/ITSM system
- Flag asset classes where incident frequency exceeds the MTBF baseline
- Trigger a problem investigation when the same fault recurs more than three times in a 90-day period
- Present trend data in the monthly IT management report

---

## 7.0 Post-Incident Communication

After a P1 or P2 incident is resolved, the maintenance manager communicates to stakeholders:

| Communication | Audience | Content | Timing |
|---------------|----------|---------|--------|
| Incident closure notification | Affected users | Service restored; reference number | Immediately upon resolution |
| Incident report | IT Manager / Management | Root cause, resolution, impact, lessons learned | Within 24 hours |
| SLA impact update | Service management | Downtime duration; SLA compliance status | In monthly report |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCU 6
- ITIL 4 Foundation — Incident Management and Problem Management practices
- CompTIA Server+ Certification — Troubleshooting Methodology
- ISO/IEC 20000-1:2018 IT Service Management — Requirements
- Microsoft Docs — Windows Server Troubleshooting Guide