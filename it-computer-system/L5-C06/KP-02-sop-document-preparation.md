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
| NO. KOD | IT-020-5:2013-C06/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-sop-document-preparation

**TUJUAN:** Kertas rujukan untuk KP-02-sop-document-preparation.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Apply document control principles to structure an SOP document correctly
2. Write SOP content using government-standard language, appropriate technical depth, and bilingual conventions
3. Incorporate process flow diagrams, decision trees, and supporting forms into the SOP
4. Conduct structured review and validation of SOP drafts with subject-matter experts
5. Manage document versioning, controlled distribution, and document register maintenance

---

## 1.0 SOP Document Structure and Standards

### 1.1 Mandatory Document Control Header

Every SOP document in a Malaysian government or government-linked ICT environment must carry a standardised document control header:

| Field | Description |
|---|---|
| Document Title | Full title of the SOP in Bahasa Malaysia and English |
| Document Number | Unique code from the document register (e.g. ICT-NET-SOP-001) |
| Version Number | Format: v1.0, v1.1, v2.0 (major version = substantive revision; minor = editorial) |
| Effective Date | Date from which the SOP is officially in force |
| Review Date | Date by which the SOP must be reviewed (typically 1–2 years from effective date) |
| Document Owner | Job title (not personal name) of the officer responsible for the SOP |
| Approver | Job title of the officer who has authority to approve the SOP |
| Classification | Document sensitivity level (e.g. TERHAD, SULIT, TERBUKA) |
| Revision History | Table of all changes: version, date, change description, authorised by |

### 1.2 Standard SOP Body Structure

| Section | Purpose |
|---|---|
| 1. Purpose (Tujuan) | States what the SOP achieves and why it exists |
| 2. Scope (Skop) | Defines what processes, systems, and personnel the SOP covers |
| 3. Definitions (Definisi) | Defines key terms, abbreviations, and acronyms |
| 4. Roles and Responsibilities (Peranan dan Tanggungjawab) | Lists who does what; use RACI matrix where appropriate |
| 5. Prerequisites (Prasyarat) | Conditions, tools, access, or approvals needed before starting |
| 6. Procedure Steps (Langkah Prosedur) | Numbered, sequential steps with decision points |
| 7. Exception Handling (Pengendalian Pengecualian) | How to handle deviations, errors, and escalation |
| 8. Records and Evidence (Rekod dan Bukti) | What must be documented, where, and for how long |
| 9. Related Documents (Dokumen Berkaitan) | Cross-references to policies, other SOPs, forms, and standards |
| 10. References (Rujukan) | External standards and regulations |

---

## 2.0 Writing SOP Content

### 2.1 Language and Style Guidelines

- **Bilingual requirement**: All SOPs for Malaysian government and public-sector entities must have titles, section headings, and key terms in both Bahasa Malaysia and English
- **Active voice and imperative mood**: Write steps as instructions, e.g. "Verify that the firewall rule set has been reviewed by the Network Security Officer before applying to the production environment" — not "The firewall rule set should be reviewed..."
- **Precision**: Avoid ambiguous words such as "appropriate", "sufficient", "as needed" — specify exact thresholds, quantities, or timeframes
- **Level-appropriate depth**: Level 5 SOPs must include governance, exception handling, escalation paths, and evidence requirements — not just the basic technical steps

### 2.2 Writing the Purpose Statement

The Purpose section must answer three questions:
1. **What** does this SOP govern? (the process)
2. **Why** does this SOP exist? (the business or compliance rationale)
3. **What outcome** does compliance with this SOP produce?

**Example — Firewall Rule Change SOP:**
> *Tujuan / Purpose: This SOP governs the request, review, authorisation, implementation, and verification of all changes to firewall rule sets on the organisation's computer network infrastructure. It exists to ensure that firewall changes are made in a controlled manner, with appropriate authorisation and documentation, to protect network security and maintain compliance with MS ISO/IEC 27001:2022 control A.8.22 (Segregation of networks) and A.8.32 (Change management).*

### 2.3 Writing Procedure Steps

Each procedural step must be:
- **Numbered sequentially** (1, 2, 3…; sub-steps as 1.1, 1.2…)
- **Assigned to a specific role** (not a person's name — always use the job title)
- **Specific about inputs, actions, and outputs**
- **Linked to a form or checklist** where evidence must be recorded

**Step format template:**

| Step | Responsible Role | Action | Input | Output / Evidence |
|---|---|---|---|---|
| 1 | Requestor | Submit firewall change request via the IT Service Desk portal, completing Form ICT-FW-001 | Business justification, source/destination IP, port, protocol | Submitted Form ICT-FW-001 with ticket number |
| 2 | Network Security Officer | Review the request for technical feasibility, security impact, and policy compliance within 2 working days | Form ICT-FW-001, current firewall rule set | Review comments on Form ICT-FW-001; approved or returned for revision |

---

## 3.0 Process Flow Diagrams and Decision Trees

### 3.1 Purpose of Visual Elements

Complex SOPs require visual representations alongside the textual procedure to:
- Show the overall flow and sequence of activities at a glance
- Clarify decision points where different paths are taken
- Communicate the SOP to non-technical stakeholders

### 3.2 Standard Flowchart Symbols

| Symbol | Name | Use |
|---|---|---|
| Rectangle | Process / Activity | A task or action step |
| Diamond | Decision | A yes/no or branch point |
| Parallelogram | Input / Output | Data input or document output |
| Rounded rectangle | Start / End | Beginning or end of the process |
| Arrow | Flow | Direction of process flow |

### 3.3 Swimlane Diagrams

For SOPs involving multiple roles, a swimlane (cross-functional flowchart) diagram is used. Each lane represents one role; process steps are placed in the appropriate lane to show who performs each action.

**Example structure for a 3-role SOP (Patch Management):**

```
| IT Security Officer | Systems Administrator | Change Advisory Board |
|---------------------|-----------------------|-----------------------|
| Identify patch      |                       |                       |
|        ↓            |                       |                       |
| Assess risk         |                       |                       |
|        ↓            |                       |                       |
| Submit RFC -------->| Review RFC            |                       |
|                     |        ↓              |                       |
|                     |                ------->| Approve/Reject        |
|                     |                       |        ↓              |
|                     | Apply patch <---------|                       |
|                     |        ↓              |                       |
|                     | Verify & report       |                       |
```

---

## 4.0 Supporting Forms and Checklists

### 4.1 Form Design Principles

Every form that accompanies an SOP must:
- Carry the document number of the parent SOP in its header
- Have a unique form number (e.g. Form ICT-NET-001/F1)
- Include fields for date, person completing the form, and authorising officer
- Be version-controlled alongside the parent SOP

### 4.2 Common SOP Supporting Documents

| Document Type | Example |
|---|---|
| Request Form | Firewall change request form, user access request form |
| Authorisation / Approval Form | Two-person authorisation record for critical changes |
| Checklist | Pre-change checklist, post-change verification checklist |
| Log Template | Incident log, maintenance log, patch log |
| Report Template | Monthly SOP compliance report, quarterly review report |
| Risk Assessment Template | Change risk assessment, vulnerability assessment |

---

## 5.0 Review and Validation Process

### 5.1 Review Stages

| Stage | Reviewer | Purpose |
|---|---|---|
| Technical Review | Subject-matter expert (e.g. Network Engineer, Systems Administrator) | Verify technical accuracy and completeness of steps |
| Operational Review | Process owner and end users | Verify practicality; identify workflow gaps or impractical steps |
| Compliance Review | Internal Audit, Information Security, Legal (if applicable) | Verify regulatory alignment and control coverage |
| Management Review | Department Head / CIO | Final authority check; confirm alignment with organisational strategy |

### 5.2 Review Documentation

All review comments must be captured in a **Review Comment Register**:

| Ref | Reviewer | Section | Comment | Action Taken | Status |
|---|---|---|---|---|---|
| RC-001 | Network Engineer | Step 3.2 | Step does not specify timeout value for firewall rule activation | Added: "activate within 10 seconds of rule push confirmation" | Resolved |

### 5.3 Validation Testing

Before an SOP is formally approved, it must be **tested** (desk-walked or live-tested):
1. A trained operator follows the SOP step-by-step in a test environment
2. Any step that cannot be executed as written is flagged for revision
3. Validation results are documented; revised SOP is re-tested if substantive changes are made
4. Validation sign-off is recorded before submitting for management approval

---

## 6.0 Document Versioning and Register

### 6.1 Version Control Rules

| Version Type | When Applied | Example |
|---|---|---|
| Major revision (v2.0) | Substantive change to scope, process steps, or roles; triggered by audit, system upgrade, or regulatory change | Change from manual patch process to automated patch management tool |
| Minor revision (v1.1) | Editorial corrections, clarification of wording, minor additions that do not change the process | Updated terminology to align with new system name |
| Draft | During development; not yet approved | Draft v0.1, Draft v0.2 |

### 6.2 Document Register

A Document Register (Daftar Dokumen) is maintained by the document controller and tracks every controlled SOP:

| Doc No. | Title | Version | Effective Date | Review Date | Owner | Status |
|---|---|---|---|---|---|---|
| ICT-NET-SOP-001 | Firewall Rule Change Procedure | v2.1 | 01/01/2026 | 31/12/2026 | Network Manager | Active |
| ICT-SYS-SOP-003 | Server Patch Management Procedure | v1.0 | 15/03/2026 | 14/03/2027 | Systems Administrator | Active |

### 6.3 Controlled Distribution

- Only controlled copies of approved SOPs may be distributed for operational use
- Controlled copies are stamped or watermarked with "SALINAN TERKAWAL / CONTROLLED COPY" and the copy number
- Uncontrolled copies (e.g. printed for reference only) must be marked "SALINAN TIDAK TERKAWAL / UNCONTROLLED COPY — verify currency before use"
- When an SOP is revised, the document controller must retrieve or invalidate all superseded controlled copies

---

## Rujukan / References

- NOSS IT-020-5:2013 — CoCU 6: Computer System & Network SOP Development and Implementation Management
- MS ISO 9001:2015 — Clause 7.5: Documented Information
- MS ISO/IEC 27001:2022 — Clause 7.5 & Annex A controls
- MAMPU — Panduan Pengurusan Dokumen ICT Sektor Awam
- National Archives of Malaysia — Records Management Guidelines
- ITIL 4 — Service Configuration Management Practice