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
| NO. KOD | IT-020-5:2013-C03/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-security-requirements-analysis

**TUJUAN:** Kertas rujukan untuk KP-01-security-requirements-analysis.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the scope and purpose of an Information Security Management System (ISMS) at Level 5 management responsibility
2. Identify and interpret organisational security requirements from regulatory, contractual, and internal sources
3. Apply the ISO/IEC 27001:2022 framework structure to gap analysis against an existing security posture
4. Distinguish between strategic, tactical, and operational security management responsibilities
5. Produce a structured security requirements analysis document suitable for management review

---

## 1.0 Introduction to Security Management Requirements Analysis

At Level 5, the security professional does not merely configure or operate security controls — the role is to **manage** the organisation's information security as a whole, aligning it with business objectives, regulatory obligations, and risk tolerance. Requirements analysis is the first work activity in this process: before any plan can be made or any control implemented, management must understand **what is required** and **by whom**.

Security management requirements derive from multiple authoritative sources:

| Source Category | Examples |
|----------------|---------|
| Regulatory and legal obligations | Personal Data Protection Act 2010 (PDPA), Bank Negara Malaysia (BNM) Risk Management in Technology (RMiT) policy, Securities Commission Cybersecurity Guidelines |
| Industry standards and frameworks | ISO/IEC 27001:2022 (ISMS), NIST Cybersecurity Framework (CSF) 2.0, CIS Controls v8 |
| Contractual requirements | Customer agreements, service level agreements (SLAs), supply chain security clauses |
| Internal organisational mandates | Board-approved security policies, internal audit findings, prior incident lessons learned |
| Third-party assessments | Penetration test reports, vulnerability assessment findings, external audit reports |

---

## 2.0 The ISO/IEC 27001:2022 Framework as the Requirements Reference

ISO/IEC 27001:2022 is the internationally recognised standard for establishing, implementing, maintaining, and continually improving an ISMS. Understanding its structure is essential for requirements analysis at Level 5.

### 2.1 Clause Structure

| Clause | Title | Relevance to Requirements Analysis |
|--------|-------|-------------------------------------|
| Clause 4 | Context of the Organisation | Identifies internal/external issues, interested parties, and ISMS scope |
| Clause 5 | Leadership | Defines top management commitment and policy requirements |
| Clause 6 | Planning | Requires risk assessment, risk treatment, and security objectives |
| Clause 7 | Support | Resources, competence, awareness, communication, documented information |
| Clause 8 | Operation | Implementation and control of planned processes |
| Clause 9 | Performance Evaluation | Internal audit, management review, monitoring and measurement |
| Clause 10 | Improvement | Nonconformity, corrective action, continual improvement |

### 2.2 Annex A Controls (ISO/IEC 27002:2022)

ISO/IEC 27001:2022 Annex A references 93 controls grouped into four themes:

| Theme | No. of Controls | Examples |
|-------|----------------|---------|
| Organisational controls | 37 | Information security policies, roles and responsibilities, threat intelligence |
| People controls | 8 | Screening, information security awareness training, disciplinary process |
| Physical controls | 14 | Physical security perimeters, clear desk policy, equipment maintenance |
| Technological controls | 34 | Access control, malware protection, network security, cryptography |

---

## 3.0 Conducting an Organisational Context Analysis

Requirements analysis begins with understanding the **context of the organisation** (ISO/IEC 27001:2022 Clause 4).

### 3.1 Internal Context Factors

| Factor | Examples |
|--------|---------|
| Organisational structure | Number of departments, subsidiaries, remote offices |
| Business processes | Core workflows dependent on information systems |
| Existing IT infrastructure | On-premises servers, cloud services, BYOD policy |
| Current security controls | Existing firewalls, endpoint protection, IAM systems |
| Staffing and competency levels | IT team size, security awareness, training records |
| Risk culture and appetite | Board tolerance for operational disruption vs. data breach |

### 3.2 External Context Factors

| Factor | Examples |
|--------|---------|
| Regulatory environment | PDPA compliance requirements, sector-specific regulations |
| Threat landscape | Industry-specific threats (ransomware, insider threats, supply chain attacks) |
| Technology environment | Cloud adoption trends, IoT proliferation, software supply chain risks |
| Competitive environment | Intellectual property protection requirements |
| Customer and partner expectations | Security clauses in contracts, due diligence questionnaires |

---

## 4.0 Identifying Interested Parties and Their Security Requirements

ISO/IEC 27001:2022 Clause 4.2 requires the organisation to identify interested parties (stakeholders) and their relevant requirements.

| Interested Party | Typical Security Requirements |
|-----------------|-------------------------------|
| Senior Management / Board | Assurance that information assets are protected; regulatory compliance maintained |
| Customers / Clients | Confidentiality of their data; service availability; breach notification |
| Employees | Clear security policies; training; protection of personal data they submit |
| Regulators (BNM, MCMC, SC) | Timely incident reporting; evidence of controls; audit cooperation |
| External auditors | Access to ISMS documentation; evidence of compliance; management review records |
| IT and security operations team | Clear procedures; appropriate tools; escalation paths |
| Third-party suppliers / vendors | Security requirements in contracts; access control for third-party systems |

---

## 5.0 Gap Analysis Against the Current Security Posture

A gap analysis compares the **required** security controls against what is **currently in place**, identifying shortfalls that must be addressed in the security management plan.

### 5.1 Gap Analysis Process

1. **Define the scope** — which systems, processes, and organisational units are included in the ISMS scope (ISO/IEC 27001:2022 Clause 4.3)
2. **Inventory existing controls** — document all current technical, administrative, and physical security measures
3. **Map to requirements** — for each identified requirement (regulatory, standard, contractual), assess whether an existing control satisfies it
4. **Classify gaps** — categorise as: *fully met*, *partially met*, or *not met*
5. **Assess gap risk** — estimate the likelihood and impact if each gap is exploited
6. **Prioritise gaps** — rank by risk level to inform planning

### 5.2 Gap Analysis Output Document

| Section | Content |
|---------|---------|
| ISMS Scope Statement | Defines boundaries of the analysis |
| Requirements Inventory | All identified requirements by source category |
| Control Inventory | All existing controls with evidence reference |
| Gap Register | Each gap: requirement → current state → gap description → risk rating |
| Preliminary Recommendations | High-level actions required to close gaps |

---

## 6.0 Security Management Responsibilities at Level 5

Level 5 security management is **strategic and governance-oriented** — distinct from Level 4 hands-on security operations.

| Responsibility Level | Level 4 (Technical) | Level 5 (Management) |
|---------------------|--------------------|-----------------------|
| Focus | Configuring and operating security controls | Governing, planning, and oversight of the ISMS |
| Risk | Identifying and reporting technical vulnerabilities | Defining risk tolerance; approving risk treatment decisions |
| Policies | Following policies | Authoring and approving policies |
| Audit | Supporting audit activities | Commissioning and reviewing audit findings |
| Incident | Responding to incidents | Overseeing incident management; approving escalation |
| Reporting | Operational status reports | Executive and Board-level reporting |

---

## 7.0 Security Requirements Analysis Report

The output of Work Activity 1 is a formal **Security Requirements Analysis Report** submitted to senior management. It documents:

1. **ISMS scope** — systems and processes in scope
2. **Regulatory and standards requirements** — with specific clauses and obligations
3. **Interested parties register** — stakeholders and their security requirements
4. **Current security posture** — inventory of existing controls
5. **Gap analysis results** — gap register with risk ratings
6. **Preliminary recommendations** — prioritised list of actions for the planning phase

---

## Rujukan / References

- ISO/IEC 27001:2022 — Information Security Management Systems — Requirements
- ISO/IEC 27002:2022 — Information Security Controls
- Personal Data Protection Act 2010 (Malaysia) — Act 709
- Bank Negara Malaysia, Risk Management in Technology (RMiT) Policy Document, 2020
- NIST Cybersecurity Framework 2.0, February 2024
- NOSS IT-020-5:2013 Computer Systems Management — CoCU 3