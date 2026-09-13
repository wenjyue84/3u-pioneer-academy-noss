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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C03 COMPUTER SYSTEM SECURITY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM SECURITY MANAGEMENT REQUIREMENTS<br>2. PLAN COMPUTER SYSTEM SECURITY MANAGEMENT<br>3. MANAGE COMPUTER SYSTEM SECURITY<br>4. PRODUCE COMPUTER SYSTEM SECURITY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C03/KP(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-security-management-reporting

**TUJUAN:** Kertas rujukan untuk KP-04-security-management-reporting.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and audience hierarchy of security management reporting
2. Identify and calculate key security performance metrics and KPIs for management reporting
3. Produce an ISMS Internal Audit Report with findings, nonconformities, and recommendations
4. Prepare a Management Review Report meeting ISO/IEC 27001:2022 Clause 9.3 requirements
5. Construct an executive security dashboard suitable for Board and senior management consumption
6. Apply continual improvement principles to close audit and review findings

---

## 1.0 Purpose and Hierarchy of Security Management Reporting

Security management reporting serves to communicate the **state, effectiveness, and performance** of the ISMS to decision-makers at appropriate levels of detail. Different audiences require different report formats, depth, and frequency.

### 1.1 Reporting Audience Hierarchy

| Audience | Report Type | Frequency | Detail Level | Primary Purpose |
|---------|------------|-----------|--------------|----------------|
| Board of Directors / CEO | Executive Security Brief | Quarterly / As required | Strategic; visual dashboard; 1–2 pages | Risk exposure; regulatory compliance status; major incidents |
| Information Security Steering Committee | Security Steering Report | Quarterly | Management; metrics + narrative; 5–10 pages | KPI performance; risk treatment progress; resource decisions |
| CISO / Security Manager | ISMS Performance Report | Monthly | Operational; full metrics; detailed | Programme tracking; SOC performance; control effectiveness |
| Internal Auditor | Internal Audit Report | Annually (minimum) | Technical; findings-based | Nonconformities; observations; corrective actions |
| Regulator (BNM, MCMC) | Regulatory Compliance Report | As required by regulation | Formal; evidence-based | Demonstrating compliance; incident notification |

---

## 2.0 Key Security Metrics and KPIs for Management Reporting

Management reports must be grounded in measurable data. The following metrics are commonly reported at management level:

### 2.1 Risk Management Metrics

| Metric | Description | Calculation |
|--------|-------------|-------------|
| Risk Register Size | Total number of identified information security risks | Count of risks in risk register |
| Risk Distribution | Breakdown of risks by category (Critical / High / Medium / Low) | Count per category |
| Risk Treatment Progress | % of risks in the Risk Treatment Plan that have been addressed | Risks treated / Total risks × 100 |
| Residual Risk Acceptance Rate | % of risks accepted by management (not treated) | Accepted risks / Total risks × 100 |
| Risk Reduction Trend | Change in average risk score over reporting periods | Average risk score (current) vs. previous period |

### 2.2 Incident Management Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Total Security Incidents | Number of confirmed incidents in the reporting period | Trending downward |
| Incidents by Severity | P1/P2/P3/P4 breakdown | Minimise P1 and P2 |
| Mean Time to Detect (MTTD) | Average detection time | ≤ 4 hours |
| Mean Time to Respond (MTTR) | Average containment time | ≤ 2 hours |
| Mean Time to Recover (MTTR-R) | Average recovery time | Per business continuity objectives |
| Regulatory Notifications | Number of incidents requiring regulatory notification | Track; target 0 preventable breaches |
| Recurring Incident Rate | % of incidents caused by a previously known and unresolved vulnerability | < 5% |

### 2.3 Control Effectiveness Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Control Implementation Rate | % of planned controls fully implemented | ≥ 90% by target date |
| Patch Compliance Rate | % of systems patched within SLA | ≥ 98% for critical; ≥ 95% for high |
| Vulnerability Age | Average age of open vulnerabilities by severity | Critical: ≤ 24 hrs; High: ≤ 7 days |
| Privileged Account Review Completion | % of privileged accounts reviewed on schedule | 100% |
| Security Training Completion | % of staff completing mandatory annual training | ≥ 95% |
| Phishing Click Rate | % of staff clicking simulated phishing | < 5% |

---

## 3.0 ISMS Internal Audit

ISO/IEC 27001:2022 Clause 9.2 requires the organisation to conduct internal audits at planned intervals to determine whether the ISMS conforms to its own requirements and the requirements of the standard.

### 3.1 Internal Audit Programme

| Stage | Activity |
|-------|----------|
| Audit programme planning | Define audit scope, criteria, frequency, and responsible auditors for the year |
| Individual audit planning | Prepare audit plan: scope, objectives, methods, schedule, and checklists |
| Audit execution | Document review, interviews, and observation; collect objective evidence |
| Findings documentation | Record conformities, nonconformities (major/minor), and observations |
| Audit report | Formal written report with findings, conclusions, and recommendations |
| Corrective action | Auditee responds with root cause analysis and corrective action plan |
| Follow-up | Auditor verifies corrective actions are implemented and effective |

### 3.2 Audit Finding Classifications

| Classification | Definition | Required Response |
|---------------|-----------|-------------------|
| Major Nonconformity | Absence of a required control; complete breakdown of a process; ISMS objective not met | Immediate root cause analysis; corrective action within 30 days; re-audit required |
| Minor Nonconformity | Isolated lapse; partial implementation; single instance of non-compliance | Corrective action within 60–90 days; follow-up at next scheduled audit |
| Observation / Opportunity for Improvement | Not yet a nonconformity but a potential risk if not addressed | Management considers and decides on action; documented |
| Conformity | Control is implemented and operating effectively | Documented as positive evidence |

### 3.3 Internal Audit Report Structure

| Section | Content |
|---------|---------|
| 1. Audit Scope and Objectives | What was audited; what criteria were applied |
| 2. Audit Methodology | Documentary review, interviews, observation, sampling |
| 3. Audit Team | Names and roles of auditors; independence declaration |
| 4. Findings Summary | Count of major NCs, minor NCs, observations, conformities |
| 5. Detailed Findings | Each finding: clause reference, evidence, description, classification |
| 6. Conclusions | Overall ISMS conformity and effectiveness assessment |
| 7. Recommendations | Prioritised list of recommended improvements |
| 8. Distribution | Recipients (CISO, Management Review, external auditor if applicable) |
| 9. Corrective Action Plan | Auditee's response to each finding (completed separately) |

---

## 4.0 Management Review

ISO/IEC 27001:2022 Clause 9.3 requires top management to review the ISMS at planned intervals. The Management Review is the **highest-level formal review** of the ISMS and must produce documented outputs.

### 4.1 Required Management Review Inputs (Clause 9.3.2)

| Input | Description |
|-------|-------------|
| Status of actions from previous reviews | Were previously agreed actions completed? |
| Changes in external and internal issues | New regulatory requirements, organisational changes, threat landscape changes |
| Information security performance and effectiveness | KPI results; audit findings; incident trends |
| Feedback from interested parties | Customer complaints; regulatory feedback; supplier audit results |
| Risk assessment results and risk treatment plan status | Current risk register status; treatment progress |
| Opportunities for continual improvement | Identified improvements not yet actioned |

### 4.2 Required Management Review Outputs (Clause 9.3.3)

| Output | Description |
|--------|-------------|
| Decisions on continual improvement opportunities | Which improvements will be pursued; resource allocation |
| Changes to the ISMS | Scope changes; policy updates; structural changes |
| Resource needs | Budget, staffing, or training requirements approved |
| Revised security objectives | Updated or new SMART objectives for the next period |

### 4.3 Management Review Report Structure

| Section | Content |
|---------|---------|
| 1. Meeting details | Date, participants, chair (CISO or senior manager) |
| 2. ISMS Performance Summary | Dashboard of KPIs vs. targets |
| 3. Internal Audit Findings | Summary of most recent audit; NC closure status |
| 4. Incident Summary | Significant incidents in the review period |
| 5. Risk Register Review | Top risks; changes in risk landscape |
| 6. Compliance Status | Regulatory and contractual compliance position |
| 7. Interested Party Feedback | Stakeholder concerns and requirements |
| 8. Continual Improvement Decisions | Agreed improvements with owners and deadlines |
| 9. Changes to ISMS | Approved changes to scope, policy, or processes |
| 10. Resource Decisions | Budget and staffing decisions |
| 11. Revised Objectives | Updated security objectives for next period |
| 12. Action Register | All agreed actions with owner, deadline, and status |

---

## 5.0 Executive Security Dashboard

The executive security dashboard provides Board and senior management with a concise, visual summary of the organisation's security posture. It must communicate complex information clearly and without technical jargon.

### 5.1 Dashboard Components

| Component | Format | Content |
|-----------|--------|---------|
| Overall Security Posture | RAG (Red / Amber / Green) indicator | Single status indicator with brief narrative |
| Risk Exposure | Bar chart | Count of Critical / High / Medium / Low risks |
| Incident Trend | Line chart | Monthly incident count for last 12 months |
| Control Implementation | Progress bar | % of planned controls implemented |
| Top 3 Risks | Text summary | Brief description of the 3 highest-rated current risks |
| Regulatory Compliance | RAG per regulation | Compliance status for each applicable regulation |
| Training Completion | Percentage | % of staff with current mandatory training |
| Open Audit Findings | Count | Number of open NCs by severity |

### 5.2 Writing for Executive Audiences

When preparing reports for Board or senior management, the security manager must:

- **Lead with risk and business impact** — not technical detail
- **Use business language** — "customer data exposure risk" not "SQL injection vulnerability"
- **Provide context** — compare metrics to targets, industry benchmarks, or prior periods
- **Be concise** — executive summary on page 1; detail in annexes for those who need it
- **Recommend decisions** — present options with risk and cost trade-offs; ask for a specific decision

---

## 6.0 Continual Improvement

ISO/IEC 27001:2022 Clause 10 requires the organisation to continually improve the suitability, adequacy, and effectiveness of the ISMS. Security management reports are the primary input to this process.

### 6.1 Nonconformity and Corrective Action (Clause 10.1)

When a nonconformity is identified (from audit, incident, or monitoring), the organisation must:

1. **React** — take action to control and correct it; address consequences
2. **Investigate** — determine the root cause using structured methods (e.g. 5-Why analysis, fishbone diagram)
3. **Evaluate need for action** — determine if similar nonconformities could occur elsewhere
4. **Implement corrective action** — change the process, control, or procedure that allowed the nonconformity
5. **Review effectiveness** — verify that the corrective action has resolved the root cause
6. **Update the ISMS** — if the change affects documented information, update policies, procedures, or risk register

### 6.2 Improvement Action Register

All improvement actions arising from management reviews, audits, incidents, and monitoring activities must be tracked in a central register:

| Field | Description |
|-------|-------------|
| Action ID | Unique reference |
| Source | Audit finding / Management review / Incident / Risk assessment |
| Description | What needs to be done |
| Root Cause | Why the issue arose (for corrective actions) |
| Action Owner | Person responsible for completing the action |
| Due Date | Target completion date |
| Status | Open / In Progress / Completed / Verified |
| Evidence | Reference to evidence that the action has been effectively completed |
| Close Date | Date the action was verified as complete |

---

## Rujukan / References

- ISO/IEC 27001:2022 — Clauses 9.2 (Internal Audit), 9.3 (Management Review), 10.1 (Continual Improvement)
- ISO 19011:2018 — Guidelines for Auditing Management Systems
- ISO/IEC 27004:2016 — Information Security Measurements
- CISA, Cybersecurity Performance Goals, 2023
- Bank Negara Malaysia, RMiT Policy Document, 2020
- NOSS IT-020-5:2013 Computer Systems Management — CoCU 3