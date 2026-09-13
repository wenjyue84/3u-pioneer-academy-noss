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
| NO. KOD | IT-020-5:2013-C03/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-security-management-planning

**TUJUAN:** Kertas rujukan untuk KP-02-security-management-planning.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Conduct a formal information security risk assessment using a structured methodology
2. Select and justify risk treatment options appropriate to organisational risk appetite
3. Develop a Statement of Applicability (SoA) aligned with ISO/IEC 27001:2022 Annex A
4. Formulate a security governance framework including policy hierarchy and management roles
5. Produce a Security Management Plan with measurable objectives and a prioritised implementation roadmap

---

## 1.0 Information Security Risk Assessment

Risk assessment is the foundation of security management planning (ISO/IEC 27001:2022 Clause 6.1.2). It converts the gap analysis findings from Work Activity 1 into quantified risks that management can evaluate and act upon.

### 1.1 Risk Assessment Methodology

The organisation must define and apply a consistent risk assessment methodology. A common approach is:

**Risk = Likelihood × Impact**

| Parameter | Definition | Scale |
|-----------|-----------|-------|
| Likelihood | Probability that a threat will exploit a vulnerability within a given period | 1 (Rare) – 5 (Almost Certain) |
| Impact | Business consequence if the event occurs (financial, operational, reputational, legal) | 1 (Negligible) – 5 (Catastrophic) |
| Risk Score | Likelihood × Impact | 1–25 |

### 1.2 Risk Rating Matrix

| | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---|---|---|---|---|
| **Likelihood 5** | 5 | 10 | 15 | 20 | **25** |
| **Likelihood 4** | 4 | 8 | 12 | **16** | **20** |
| **Likelihood 3** | 3 | 6 | 9 | **12** | **15** |
| **Likelihood 2** | 2 | 4 | 6 | 8 | 10 |
| **Likelihood 1** | 1 | 2 | 3 | 4 | 5 |

**Risk Categories:** 1–5 = Low | 6–11 = Medium | 12–17 = High | 18–25 = Critical

### 1.3 Information Asset Inventory

Before risks can be assessed, information assets must be catalogued:

| Asset Category | Examples |
|----------------|---------|
| Data assets | Customer records, financial data, intellectual property, personnel files |
| Software assets | Business applications, operating systems, security software, databases |
| Hardware assets | Servers, workstations, network devices, storage systems |
| Service assets | Cloud services, internet connectivity, third-party managed services |
| People assets | Key personnel with privileged access or specialised security knowledge |

### 1.4 Threat and Vulnerability Identification

| Common Threat | Associated Vulnerability | Example Scenario |
|--------------|--------------------------|-----------------|
| Ransomware / Malware | Unpatched systems, absence of endpoint detection and response (EDR) | Attacker encrypts file server; production halts |
| Phishing / Social Engineering | Insufficient user awareness training | Employee credentials stolen; unauthorised access to ERP |
| Insider Threat | Excessive access privileges, lack of activity monitoring | Disgruntled employee exfiltrates customer database |
| Supply Chain Attack | Insufficient third-party security vetting | Compromised software update deploys backdoor |
| DDoS Attack | Absence of traffic scrubbing or failover | Public-facing portal unavailable for 8 hours |
| Data Leakage | No Data Loss Prevention (DLP) controls | Sensitive data sent to personal email account |
| Physical Theft | Inadequate physical access controls | Laptop stolen from unlocked office; unencrypted data exposed |

---

## 2.0 Risk Treatment

After risks are assessed, management must decide on the treatment approach for each risk (ISO/IEC 27001:2022 Clause 6.1.3).

### 2.1 Risk Treatment Options

| Option | Description | When to Apply |
|--------|-------------|---------------|
| **Modify (Treat)** | Implement controls to reduce likelihood or impact to an acceptable level | Risk score exceeds organisational risk appetite; cost of control is proportionate |
| **Accept** | Formally acknowledge and accept the residual risk | Risk score is within acceptable limits; cost of control exceeds risk impact |
| **Avoid** | Cease the activity that creates the risk | Risk is unacceptably high and cannot be mitigated cost-effectively |
| **Transfer** | Share the risk (e.g. cyber insurance, outsourcing to a managed security service provider) | Residual risk remains but is better managed by a third party |

### 2.2 Risk Treatment Plan

For each risk selected for modification, the Risk Treatment Plan specifies:

| Field | Description |
|-------|-------------|
| Risk ID | Unique reference from the risk register |
| Risk Description | Asset, threat, and vulnerability |
| Risk Score (Inherent) | Score before controls |
| Selected Controls | ISO/IEC 27001:2022 Annex A control(s) to be applied |
| Control Owner | Person or role responsible for implementing the control |
| Implementation Deadline | Target completion date |
| Risk Score (Residual) | Expected score after controls are implemented |
| Acceptance Threshold | Organisational risk appetite level |

---

## 3.0 Statement of Applicability (SoA)

The Statement of Applicability (SoA) is a required ISMS document (ISO/IEC 27001:2022 Clause 6.1.3d) that lists all 93 Annex A controls and, for each:

- States whether it is **applicable** or **not applicable**
- Provides **justification** for the inclusion or exclusion
- Indicates whether the control is **currently implemented**
- References the relevant requirement (risk, regulation, or contractual obligation) that necessitates the control

| SoA Column | Description |
|------------|-------------|
| Control reference (e.g. A.5.1) | ISO/IEC 27002:2022 control identifier |
| Control title | Short description of the control |
| Applicable (Y/N) | Whether the control applies to this organisation |
| Justification | Reason for inclusion/exclusion (risk, regulation, contractual) |
| Implementation status | Implemented / Partially Implemented / Not Yet Implemented |
| Evidence reference | Document, system, or record providing evidence of implementation |

---

## 4.0 Security Governance Framework

Governance defines **who is accountable** for information security, **how decisions are made**, and **how performance is monitored**.

### 4.1 Security Policy Hierarchy

| Level | Document | Purpose |
|-------|----------|---------|
| Level 1 | Information Security Policy (ISP) | Top-level statement of management intent; approved by Board or CEO |
| Level 2 | Topic-specific policies | Acceptable use policy, access control policy, incident response policy, data classification policy |
| Level 3 | Standards and guidelines | Technical standards, configuration baselines, security procedures |
| Level 4 | Work instructions and procedures | Step-by-step operational instructions for specific tasks |

### 4.2 Security Roles and Responsibilities

| Role | Responsibilities |
|------|----------------|
| Chief Information Security Officer (CISO) / Security Manager | Owns the ISMS; accountable to Board/senior management; oversees all security activities |
| Risk Owner | Senior manager responsible for accepting or treating a specific risk |
| Information Asset Owner | Responsible for an information asset's classification, access, and protection |
| Security Operations Centre (SOC) Lead | Manages day-to-day monitoring, detection, and first-response activities |
| Internal Auditor | Conducts ISMS internal audits; reports findings to CISO |
| IT Manager / System Administrator | Implements technical controls as directed by security policies |

### 4.3 Security Committee Structure

Effective governance requires structured oversight forums:

| Forum | Membership | Frequency | Purpose |
|-------|-----------|-----------|---------|
| Information Security Steering Committee | CISO, CIO, CFO, Legal, Business Unit Heads | Quarterly | Strategic decisions, risk acceptance, policy approval |
| Security Operations Review | SOC Lead, IT Manager, Security Team | Monthly | Operational metrics, incident trends, control effectiveness |
| Management Review (ISO 27001 Clause 9.3) | Top management + CISO | Annual (minimum) | Formal ISMS review; continual improvement decisions |

---

## 5.0 Security Objectives and Implementation Roadmap

ISO/IEC 27001:2022 Clause 6.2 requires the organisation to establish **measurable security objectives**.

### 5.1 Characteristics of Good Security Objectives (SMART)

| Criterion | Example |
|-----------|---------|
| Specific | "Reduce mean time to detect (MTTD) security incidents" |
| Measurable | "From current baseline of 72 hours to ≤ 4 hours within 12 months" |
| Achievable | Supported by SOC staffing and SIEM deployment budget |
| Relevant | Directly tied to incident management risk identified in risk assessment |
| Time-bound | Target achievement date: Q4 of current financial year |

### 5.2 Security Management Plan — Structure

The Security Management Plan is the primary output of Work Activity 2:

| Section | Content |
|---------|---------|
| 1. Executive Summary | Purpose, scope, and management approval |
| 2. Risk Assessment Results | Summary of critical and high risks |
| 3. Risk Treatment Plan | Controls selected, owners, and timelines |
| 4. Statement of Applicability | Annex A control applicability and status |
| 5. Security Governance Framework | Policy hierarchy, roles, committee structure |
| 6. Security Objectives | SMART objectives with KPIs and targets |
| 7. Implementation Roadmap | Phased plan: immediate (0–3 months), short-term (3–12 months), medium-term (1–3 years) |
| 8. Resource Requirements | Budget estimate, staffing, training needs |
| 9. Review and Update Schedule | Annual review cycle and trigger events |

### 5.3 Implementation Roadmap — Phasing

| Phase | Timeframe | Focus |
|-------|-----------|-------|
| Phase 1 — Immediate | 0–3 months | Critical risks; mandatory regulatory compliance; quick wins |
| Phase 2 — Short-term | 3–12 months | High-risk controls; governance framework establishment; SOC capability |
| Phase 3 — Medium-term | 1–3 years | ISMS maturity improvement; certification readiness; continuous monitoring |

---

## Rujukan / References

- ISO/IEC 27001:2022 — Information Security Management Systems — Requirements
- ISO/IEC 27005:2022 — Information Security Risk Management
- ISO/IEC 27002:2022 — Information Security Controls (Annex A reference)
- NIST SP 800-30 Rev.1 — Guide for Conducting Risk Assessments
- Bank Negara Malaysia, RMiT Policy Document, 2020
- NOSS IT-020-5:2013 Computer Systems Management — CoCU 3