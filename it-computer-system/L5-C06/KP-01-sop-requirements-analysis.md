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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C06 COMPUTER SYSTEM & NETWORK SOP DEVELOPMENT AND IMPLEMENTATION MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM & NETWORK SOP DEVELOPMENT AND IMPLEMENTATION REQUIREMENTS<br>2. PREPARE COMPUTER SYSTEM & NETWORK SOP DOCUMENT<br>3. MANAGE SOP IMPLEMENTATION<br>4. PRODUCE SOP DEVELOPMENT AND IMPLEMENTATION REPORT |
| NO. KOD | IT-020-5:2013-C06/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-sop-requirements-analysis

**TUJUAN:** Kertas rujukan untuk KP-01-sop-requirements-analysis.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Define Standard Operating Procedure (SOP) / Prosedur Operasi Piawai (POP) and explain its purpose in ICT governance
2. Identify the stakeholders, scope boundaries, and regulatory drivers for SOP development
3. Conduct a requirements gap analysis against existing policies, standards, and operational baselines
4. Classify SOP requirements by priority, complexity, and applicable compliance framework
5. Prepare a formal SOP Development and Implementation Requirements Report

---

## 1.0 Introduction to SOP / POP in Computer System & Network Management

A Standard Operating Procedure (SOP) — termed **Prosedur Operasi Piawai (POP)** in Bahasa Malaysia — is a formalised, step-by-step document that prescribes how a recurring operational task must be performed to achieve a consistent, compliant, and auditable outcome. In computer system and network management, SOPs govern activities ranging from user account provisioning and patch deployment to incident response and disaster recovery.

At Level 5, the competency moves beyond following SOPs to **managing their development and implementation lifecycle**: scoping, drafting, validating, deploying, training staff, monitoring compliance, and reporting outcomes to senior management.

**Key regulatory and standards context:**

| Standard / Framework | Relevance to IT SOP |
|---|---|
| MS ISO 9001:2015 | Documented information control; process approach; continual improvement |
| MS ISO/IEC 27001:2022 | Information security controls; operational procedures for ISMS |
| MAMPU ICT Security Policy (GPICT) | Malaysian Public Sector ICT security SOP requirements |
| NIST SP 800-53 | Control families requiring documented operating procedures |
| ITIL 4 | Service management practices; change, incident, and problem procedures |

---

## 2.0 Stakeholder Identification and Engagement

Effective SOP development begins with identifying every party whose work is affected by or who influences the SOP.

### 2.1 Stakeholder Categories

| Category | Examples | Role in SOP Development |
|---|---|---|
| Executive / Management | CIO, IT Director, Department Head | Approve scope, provide mandate, sign off final SOP |
| Process Owners | Network Manager, Systems Administrator, Security Officer | Supply subject-matter expertise; validate draft SOP |
| End Users / Operators | Helpdesk staff, IT technicians, network engineers | Validate practicality; identify workflow gaps |
| Compliance / Audit | Internal Audit, Information Security, Risk Management | Ensure regulatory alignment; review control coverage |
| External Parties | Vendors, contractors, auditors (where applicable) | Provide external perspective or contractual requirements |
| Human Resources | HR Department | Align SOP with personnel policies; training obligations |

### 2.2 Stakeholder Engagement Methods

- Structured interviews and focus group discussions (FGD)
- Review of existing job descriptions, organisational charts, and process maps
- Workshops: requirements elicitation, prioritisation, and consensus building
- Document review: current procedures, incident logs, audit findings, and complaints

---

## 3.0 Scope Definition

Scope definition establishes what the SOP set will cover and what it explicitly excludes.

### 3.1 Scope Dimensions

| Dimension | Questions to Answer |
|---|---|
| **Functional scope** | Which IT processes and sub-processes are in scope? (e.g. server management, network configuration, user account lifecycle) |
| **Organisational scope** | Which departments, sites, or entities must comply with the SOP? |
| **Technical scope** | Which systems, platforms, and infrastructure components are covered? (e.g. Windows Server, Cisco network equipment, cloud IaaS) |
| **Regulatory scope** | Which laws, standards, or contracts mandate the SOP? |
| **Time scope** | What is the target effective date and review cycle? |

### 3.2 Scope Statement Template

A scope statement should include:
1. **Background** — why the SOP is needed (trigger event, audit finding, new system, regulatory requirement)
2. **Objectives** — what the SOP set aims to achieve
3. **In-scope items** — explicit list of processes, systems, and organisational units
4. **Out-of-scope items** — explicit exclusions with rationale
5. **Assumptions and constraints** — e.g. resource availability, technology limitations

---

## 4.0 Requirements Gap Analysis

A gap analysis compares the current state (as-is) against the desired state (to-be) to identify what new or revised SOPs are needed.

### 4.1 Gap Analysis Process

```
Step 1: Inventory existing SOPs / procedures
         ↓
Step 2: Map existing SOPs to process areas
         ↓
Step 3: Identify process areas with no SOP, outdated SOP, or non-compliant SOP
         ↓
Step 4: Assess risk and impact of each gap
         ↓
Step 5: Prioritise gaps for SOP development
         ↓
Step 6: Document findings in the Requirements Report
```

### 4.2 Gap Classification

| Gap Type | Description | Example |
|---|---|---|
| Missing SOP | Process area has no documented procedure | No SOP for network firewall rule change |
| Outdated SOP | Existing SOP references obsolete technology or superseded policy | SOP still references Windows Server 2008 procedures |
| Non-compliant SOP | Existing SOP does not satisfy current regulatory or audit requirements | SOP lacks mandatory two-person authorisation required by ISO 27001 |
| Incomplete SOP | SOP covers the main task but omits exception handling, escalation, or rollback | Server patching SOP has no rollback procedure |
| Unapproved SOP | Procedure exists informally but has never been formally reviewed and approved | Network engineers follow undocumented tribal knowledge |

### 4.3 Gap Analysis Scoring Matrix

| Gap | Compliance Risk (1–5) | Operational Risk (1–5) | Priority Score (sum) |
|---|---|---|---|
| [Process Area] | | | |

Priority Score ≥ 8 = High Priority (develop first); 5–7 = Medium; ≤ 4 = Low.

---

## 5.0 Requirements Classification and Categorisation

After gap analysis, requirements are classified to guide the development plan.

### 5.1 Classification by Type

| Requirement Type | Definition |
|---|---|
| **Mandatory** | Required by law, regulation, contract, or certification standard. Non-negotiable. |
| **Best Practice** | Recommended by authoritative bodies (NIST, ISO, ITIL) but not legally mandated. |
| **Operational** | Needed for operational efficiency or consistency; driven by internal management decision. |

### 5.2 Classification by Document Type

| SOP Document | Purpose |
|---|---|
| **Master SOP** (POP Utama) | High-level procedure; applies organisation-wide |
| **Work Instruction** (Arahan Kerja) | Detailed step-by-step task guide; task-specific |
| **Policy** (Polisi) | Management directive; states what must be done |
| **Form / Template** (Borang / Templat) | Supporting document; captures evidence of SOP execution |
| **Checklist** (Senarai Semak) | Verification tool; ensures all steps are completed |

### 5.3 SOP Requirements Register

A Requirements Register documents each identified requirement:

| Ref | Process Area | Gap Type | Requirement Statement | Priority | Owner | Target Date |
|---|---|---|---|---|---|---|
| REQ-001 | Firewall rule management | Missing | Develop SOP for firewall rule addition, modification, and deletion, incorporating four-eyes authorisation | High | Network Manager | [Date] |
| REQ-002 | Server patch management | Outdated | Update patch management SOP to cover Windows Server 2022 and Linux patching via Ansible | High | Systems Administrator | [Date] |
| REQ-003 | User account provisioning | Incomplete | Add offboarding and dormant account review procedures to existing User Account SOP | Medium | IT Security Officer | [Date] |

---

## 6.0 Regulatory and Standards Alignment

### 6.1 Mapping Requirements to Standards

Each SOP requirement must be mapped to the applicable regulatory or standards clause:

| Requirement | ISO 27001 Clause | ISO 9001 Clause | GPICT Section |
|---|---|---|---|
| Incident response SOP | A.5.24, A.5.25 | 8.2 | Chapter 6 |
| Change management SOP | A.8.32 | 8.3 | Chapter 8 |
| Access control SOP | A.5.15, A.8.2 | — | Chapter 4 |
| Backup and recovery SOP | A.8.13 | — | Chapter 7 |

### 6.2 Compliance Documentation Requirements

Every SOP must include or reference:
- **Document control information**: document number, version, effective date, review date, owner, approver
- **Revision history**: all changes with date, change description, and authoriser
- **Distribution list**: who has received or has access to the document
- **Related documents**: cross-references to policies, other SOPs, forms, and standards

---

## 7.0 SOP Development and Implementation Requirements Report

The output of the requirements analysis phase is a formal **Requirements Report** that is presented to management for approval before development begins.

### 7.1 Report Structure

| Section | Content |
|---|---|
| 1. Executive Summary | Purpose, scope, key findings, and recommendations in one page |
| 2. Background and Trigger | Why the SOP development programme is needed |
| 3. Stakeholder List | All identified stakeholders and their roles |
| 4. Scope Statement | Functional, organisational, and technical scope |
| 5. Gap Analysis Results | Summary table of all identified gaps with risk ratings |
| 6. Requirements Register | Full register of all identified SOP requirements |
| 7. Regulatory Mapping | Crosswalk between requirements and applicable standards |
| 8. Development Plan (Preliminary) | Proposed timeline, resource requirements, and milestone schedule |
| 9. Approval and Sign-Off | Management signature(s) authorising commencement of development |

### 7.2 Presentation and Approval Process

1. Draft report circulated to process owners for factual verification
2. Requirements review workshop held to resolve disagreements
3. Final report submitted to IT steering committee or management for approval
4. Approval recorded with signature and date; report archived as a controlled document
5. Approved requirements register forms the baseline for the SOP development phase

---

## Rujukan / References

- NOSS IT-020-5:2013 — CoCU 6: Computer System & Network SOP Development and Implementation Management
- MS ISO 9001:2015 — Quality Management Systems: Requirements
- MS ISO/IEC 27001:2022 — Information Security Management Systems: Requirements
- MAMPU — Garis Panduan Keselamatan ICT (GPICT) Sektor Awam Malaysia
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organisations
- ITIL 4 Foundation — Service Management Practices (Axelos, 2019)
- Buku Panduan WIM JPK Edisi 2020