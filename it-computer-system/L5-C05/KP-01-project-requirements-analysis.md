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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C05 COMPUTER SYSTEM & NETWORK PROJECT MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM & NETWORK PROJECT REQUIREMENTS<br>2. PLAN COMPUTER SYSTEM & NETWORK PROJECT<br>3. MANAGE COMPUTER SYSTEM & NETWORK PROJECT<br>4. CARRY OUT COMPUTER SYSTEM & NETWORK PROJECT CLOSURE |
| NO. KOD | IT-020-5:2013-C05/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-project-requirements-analysis

**TUJUAN:** Kertas rujukan untuk KP-01-project-requirements-analysis.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and components of a project requirements analysis in computer system and network projects
2. Identify and classify functional, non-functional, technical, and business requirements from project briefs and stakeholder inputs
3. Apply structured elicitation techniques (interviews, questionnaires, workshops, observation) to gather complete requirements
4. Construct a Requirements Traceability Matrix (RTM) to link requirements to project deliverables
5. Evaluate requirements for completeness, feasibility, and alignment with organisational IT policies

---

## 1.0 Introduction to Project Requirements Analysis

Requirements analysis is the foundational activity of every computer system and network project. It determines *what* must be built, *why* it is needed, and *for whom* it will be delivered. At NOSS Level 5, a project manager must move beyond simply collecting user wishlists — the role demands structured analysis that links each requirement to a business objective, assigns ownership, and establishes criteria for acceptance.

**Definisi / Definition:**

A *project requirement* is a condition or capability that a system or network solution must satisfy to meet the needs of stakeholders and to comply with contractual, regulatory, or organisational standards.

**Kepentingan analisis keperluan / Importance of requirements analysis:**

- Prevents scope creep by establishing a baseline before design begins
- Reduces rework costs — errors caught at requirements stage cost 10–100× less to fix than errors found during testing or deployment
- Forms the legal and contractual basis for acceptance testing
- Enables accurate estimation of project budget, schedule, and resources

---

## 2.0 Types of Requirements

Computer system and network projects typically involve four categories of requirements:

| Jenis Keperluan / Requirement Type | Definisi / Definition | Contoh / Example |
|------------------------------------|-----------------------|------------------|
| **Fungsional / Functional** | What the system must do — specific behaviours, functions, or processes | "The network must support a minimum of 500 concurrent client connections via VLAN segmentation" |
| **Bukan Fungsional / Non-Functional** | Quality attributes — how well the system performs | "System uptime must be ≥ 99.9% per month (excluding scheduled maintenance)" |
| **Teknikal / Technical** | Hardware, software, and infrastructure specifications | "Servers must run Ubuntu Server 22.04 LTS with SELinux enforcing mode" |
| **Perniagaan / Business** | Organisational policies, budget, compliance, and strategic alignment | "The solution must comply with PDPA 2010 and ISO/IEC 27001 data classification requirements" |

### 2.1 Functional Requirements

Functional requirements define the system's intended behaviour. For computer system and network projects, they include:

- **Connectivity:** VPN access, WAN/LAN topology, inter-VLAN routing rules
- **Services:** Active Directory / LDAP authentication, DNS, DHCP, email, file sharing
- **Performance targets:** Bandwidth per user, latency thresholds, throughput SLAs
- **Security functions:** Firewall rule sets, IDS/IPS policies, patch management schedule
- **Backup and recovery:** RTO (Recovery Time Objective) and RPO (Recovery Point Objective)

### 2.2 Non-Functional Requirements

Non-functional requirements constrain system design and are often measurable quality attributes:

| Atribut / Attribute | Pengukuran / Measurement Example |
|---------------------|----------------------------------|
| Ketersediaan / Availability | ≥ 99.9% monthly uptime (≤ 8.76 hours downtime/year) |
| Prestasi / Performance | End-to-end latency ≤ 5 ms within the LAN |
| Skalabiliti / Scalability | Must scale from 100 to 500 users without hardware replacement |
| Keselamatan / Security | All data in transit encrypted with TLS 1.3 or higher |
| Kebolehselenggaraan / Maintainability | System must allow in-place OS patching with zero service interruption |

### 2.3 Technical Requirements

Technical requirements specify the hardware and software environment. They translate business and functional needs into implementable specifications:

- Server specifications (CPU cores, RAM, storage IOPS, RAID level)
- Network equipment (switch capacity, router throughput, firewall NGFW rating)
- Operating system and software versions (with EOL/EOS dates)
- Integration requirements (APIs, protocols, data formats)
- Physical environment (rack space, power redundancy, cooling capacity in kW)

### 2.4 Business Requirements

Business requirements anchor the project in organisational context. A Level 5 project manager must identify:

- **Strategic alignment:** How does this project support the organisation's IT roadmap?
- **Compliance obligations:** PDPA 2010, ISO/IEC 27001, NIST CSF, or sector-specific regulations
- **Budget constraints:** Approved capital expenditure (CAPEX) and operating expenditure (OPEX) limits
- **Stakeholder expectations:** Key performance indicators (KPIs) that define project success for each sponsor

---

## 3.0 Requirements Elicitation Techniques

Elicitation is the structured process of discovering requirements from stakeholders. A single technique is rarely sufficient — professional project managers use a combination:

| Teknik / Technique | Kesesuaian / Best Used When | Kelebihan / Advantage | Keterbatasan / Limitation |
|--------------------|-----------------------------|-----------------------|---------------------------|
| **Temu bual / Interview** | Detailed exploration of individual stakeholder needs | In-depth, builds rapport | Time-consuming; relies on stakeholder availability |
| **Soal selidik / Questionnaire** | Large, geographically dispersed user base | Efficient, scalable | Cannot probe follow-up answers |
| **Bengkel / Workshop (JAD)** | Cross-functional alignment and conflict resolution | Fast consensus, reveals conflicts early | Requires skilled facilitator |
| **Pemerhatian / Observation** | Understanding actual workflows vs. stated processes | Captures undocumented procedures | Can alter behaviour (Hawthorne effect) |
| **Analisis dokumen / Document analysis** | Reviewing existing system documentation, SLAs, policies | Objective, does not rely on memory | Documents may be outdated |
| **Prototaip / Prototyping** | Unclear or ambiguous UI/UX requirements | Makes abstract requirements concrete | Risk of prototype becoming the final design prematurely |

**JAD (Joint Application Development)** workshops are particularly effective for network and system projects because they bring IT architects, network engineers, end users, security officers, and sponsors into a facilitated session to resolve conflicting requirements before design begins.

---

## 4.0 Requirements Documentation

Well-documented requirements prevent ambiguity during design, development, and testing. The primary documents produced during requirements analysis are:

### 4.1 Business Requirements Document (BRD)

The BRD captures the high-level business need and the proposed solution scope. It is written for business stakeholders and contains:
- Project background and problem statement
- Business objectives and success criteria
- Stakeholder list with roles and authority levels
- High-level scope boundary (in-scope and out-of-scope items)
- Assumptions and constraints

### 4.2 System Requirements Specification (SRS)

The SRS translates BRD content into technical language for the project team. Structure follows IEEE 830:

1. Introduction (purpose, scope, definitions, overview)
2. Overall description (product perspective, functions, user characteristics, constraints)
3. Specific requirements (functional, non-functional, external interface requirements)
4. Appendices (data models, interface specifications)

### 4.3 Requirements Traceability Matrix (RTM)

The RTM links each requirement to its source, associated design element, test case, and deliverable. It is the primary tool for controlling scope and demonstrating requirement coverage during audit:

| ID Keperluan / Req ID | Kenyataan Keperluan / Requirement Statement | Sumber / Source | Komponen Reka Bentuk / Design Component | Kes Ujian / Test Case | Status |
|----------------------|----------------------------------------------|-----------------|------------------------------------------|----------------------|--------|
| REQ-F-001 | System shall support VLAN segmentation for Finance, HR, and Operations | CIO Briefing, 2026-01-10 | Layer 3 Switch Config — VLAN 10, 20, 30 | TC-NET-001 | Approved |
| REQ-NF-001 | Network uptime ≥ 99.9% monthly | SLA Document v2.1 | Redundant core switches, failover routing | TC-HA-001 | Approved |
| REQ-T-001 | Core switches: 48-port PoE+, minimum 960W PoE budget | Technical Spec Sheet | Procurement BOM — Cisco Catalyst 9300 | TC-POE-001 | Under Review |
| REQ-B-001 | Total project cost must not exceed RM 450,000 CAPEX | Budget Approval Memo | Cost baseline in project budget plan | N/A | Approved |

---

## 5.0 Requirements Validation and Prioritisation

### 5.1 Validation Criteria

Every requirement must pass four validation checks before it is baselined:

| Kriteria / Criterion | Penerangan / Description |
|----------------------|--------------------------|
| **Lengkap / Complete** | The requirement is fully described with no missing information |
| **Konsisten / Consistent** | The requirement does not contradict other requirements |
| **Boleh Diuji / Testable** | Acceptance criteria can be defined and measured |
| **Boleh Dicapai / Achievable** | The requirement can be implemented within project constraints |

### 5.2 MoSCoW Prioritisation

At Level 5, the project manager must prioritise requirements to manage scope and budget risk. The MoSCoW method classifies each requirement:

| Kelas / Class | Makna / Meaning | Tindakan / Action |
|---------------|-----------------|-------------------|
| **Must Have** | Project fails without this | Implement in all scenarios |
| **Should Have** | High value; include if possible | Implement unless resource-constrained |
| **Could Have** | Nice-to-have; low risk if omitted | Defer to Phase 2 if needed |
| **Won't Have (this time)** | Explicitly excluded from current scope | Document for future consideration |

### 5.3 Baseline and Change Control

Once requirements are validated and approved by all stakeholders, they are **baselined**. Any change to a baselined requirement must follow the formal Change Control Process:

1. Change request raised using Change Request Form
2. Impact analysis performed (scope, schedule, cost, risk)
3. Change Control Board (CCB) review and decision (approve / reject / defer)
4. RTM updated to reflect approved changes
5. Project plan and budget revised accordingly

---

## 6.0 Stakeholder Analysis

A structured stakeholder analysis ensures that all parties with influence over or interest in the project are identified and engaged appropriately. The RACI model is commonly used:

| Pihak Berkepentingan / Stakeholder | Peranan / Role | Kepentingan / Interest | Pengaruh / Influence | Strategi Penglibatan / Engagement Strategy |
|------------------------------------|----------------|------------------------|----------------------|--------------------------------------------|
| Chief Information Officer (CIO) | Sponsor | High | High | Formal steering committee updates monthly |
| IT Infrastructure Manager | Owner | High | High | Weekly project status meetings |
| Finance Department Head | User | Medium | Medium | Requirements workshop; SLA review sign-off |
| Network Security Officer | Reviewer | High | High | Security gate review at design and test phases |
| End Users | Consumer | High | Low | Questionnaire; UAT participation |
| Vendor / Contractor | Supplier | Medium | Medium | Scope-of-work briefing; contractual SLA |

---

## 7.0 Feasibility Assessment

Before requirements are baselined, a feasibility assessment evaluates whether the project is viable:

| Dimensi / Dimension | Soalan Utama / Key Question | Pertimbangan / Consideration |
|---------------------|-----------------------------|-----------------------------|
| **Teknikal / Technical** | Can the technology support the requirements? | Bandwidth, hardware EOL, vendor support, skill availability |
| **Kewangan / Financial** | Is the total cost of ownership within budget? | CAPEX, OPEX, licensing, training, maintenance |
| **Jadual / Schedule** | Can requirements be delivered within the deadline? | Resource availability, procurement lead times, dependencies |
| **Operasi / Operational** | Will the solution integrate with existing operations? | Staff training needs, change management impact |
| **Undang-undang / Legal** | Are there regulatory or compliance constraints? | PDPA, sector regulations, import/export controls on equipment |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer System Management — CoCU 5
- PMI. (2021). *A Guide to the Project Management Body of Knowledge (PMBOK® Guide)*, 7th Edition. Project Management Institute.
- IEEE Std 830-1998. *IEEE Recommended Practice for Software Requirements Specifications*
- AXELOS. (2017). *Managing Successful Projects with PRINCE2*, 6th Edition.
- Personal Data Protection Act (PDPA) 2010 — Malaysia
- ISO/IEC 27001:2022 — Information Security Management Systems