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
| NO. KOD | IT-020-5:2013-C05/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-project-planning

**TUJUAN:** Kertas rujukan untuk KP-02-project-planning.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Develop a Work Breakdown Structure (WBS) for a computer system and network project
2. Construct a project schedule using Gantt chart and Critical Path Method (CPM)
3. Prepare a project budget incorporating direct costs, indirect costs, and contingency reserves
4. Develop a risk management plan using qualitative and quantitative risk analysis
5. Produce a project management plan integrating scope, schedule, cost, quality, risk, communication, procurement, and stakeholder management plans

---

## 1.0 Introduction to Project Planning

Project planning translates approved requirements into a detailed roadmap for execution. A comprehensive project plan is the single most important reference document for a project manager — it establishes the performance baseline against which actual progress is measured.

**PMBOK® Guide 7th Edition** identifies planning as a continuous activity, not a one-time event. For computer system and network projects, planning must account for technology dependencies, vendor procurement lead times, and the operational constraints of the live IT environment.

**Prinsip Perancangan Utama / Key Planning Principles:**

- Plan to the level of detail needed to manage the work effectively — neither too high-level nor excessively granular
- All planning outputs must be based on validated requirements (RTM from KP-01)
- The project sponsor must formally approve the baseline plan before execution begins
- Plans must include explicit change control provisions

---

## 2.0 Scope Planning and Work Breakdown Structure (WBS)

### 2.1 Project Scope Statement

The Project Scope Statement defines precisely what the project will and will not deliver. It contains:

| Komponen / Component | Kandungan / Content |
|----------------------|---------------------|
| **Perihalan Skop Produk / Product Scope Description** | Detailed description of the system and network solution to be delivered |
| **Kriteria Penerimaan / Acceptance Criteria** | Measurable conditions that deliverables must satisfy for client sign-off |
| **Penyerahan / Deliverables** | List of all tangible outputs (hardware installed, software configured, documentation) |
| **Pengecualian / Exclusions** | Explicitly named items that are NOT included in the project |
| **Andaian / Assumptions** | Conditions assumed to be true but not confirmed |
| **Kekangan / Constraints** | Limitations on budget, schedule, technology, or resources |

### 2.2 Work Breakdown Structure (WBS)

The WBS decomposes the total project scope into manageable work packages. It is a hierarchical decomposition — each lower level represents increasing detail. The WBS defines 100% of the project scope — nothing more and nothing less.

**Contoh WBS / Sample WBS — Network Upgrade Project:**

```
1.0  Network Infrastructure Upgrade Project
1.1  Project Management
     1.1.1  Project charter and stakeholder register
     1.1.2  Project management plan
     1.1.3  Status reporting and meeting management
     1.1.4  Project closure report
1.2  Requirements and Design
     1.2.1  Requirements elicitation and analysis
     1.2.2  Network architecture design
     1.2.3  Security architecture review
     1.2.4  Design approval and sign-off
1.3  Procurement
     1.3.1  Bill of materials (BOM) preparation
     1.3.2  Vendor evaluation and selection
     1.3.3  Purchase orders and contracts
     1.3.4  Equipment delivery and inspection
1.4  Implementation
     1.4.1  Core switch installation and configuration
     1.4.2  VLAN and routing configuration
     1.4.3  Firewall rules and security policy deployment
     1.4.4  Server rack installation and cabling
     1.4.5  Wireless access point deployment
1.5  Testing and Quality Assurance
     1.5.1  Unit testing (individual components)
     1.5.2  Integration testing (full system)
     1.5.3  User acceptance testing (UAT)
     1.5.4  Security penetration test
1.6  Training and Documentation
     1.6.1  Administrator training
     1.6.2  End-user training
     1.6.3  As-built documentation
1.7  Project Closure
     1.7.1  Final acceptance sign-off
     1.7.2  Lessons learned register
     1.7.3  Project archive
```

**WBS Dictionary:** Every work package in the WBS must have a corresponding WBS Dictionary entry containing: description, assigned owner, estimated effort (person-hours), estimated cost, acceptance criteria, and dependencies.

---

## 3.0 Schedule Planning

### 3.1 Activity Definition and Sequencing

From the WBS work packages, the project manager identifies individual activities, then sequences them by dependency type:

| Jenis Kebergantungan / Dependency Type | Definisi / Definition | Contoh / Example |
|----------------------------------------|-----------------------|------------------|
| **Finish-to-Start (FS)** | Activity B cannot start until Activity A finishes | Cabling must finish before switch configuration can start |
| **Start-to-Start (SS)** | Activity B cannot start until Activity A starts | Documentation can start when implementation starts |
| **Finish-to-Finish (FF)** | Activity B cannot finish until Activity A finishes | Testing finishes when defect fixing finishes |
| **Start-to-Finish (SF)** | Activity B cannot finish until Activity A starts | Rarely used in IT projects |

### 3.2 Critical Path Method (CPM)

CPM identifies the sequence of activities with zero float — the longest path through the network diagram. Any delay on the critical path directly delays the project end date.

**Steps to calculate the critical path:**

1. List all activities with estimated durations
2. Draw the network diagram (precedence diagram method)
3. Perform **Forward Pass** — calculate Early Start (ES) and Early Finish (EF) for each activity
4. Perform **Backward Pass** — calculate Late Start (LS) and Late Finish (LF)
5. Calculate **Total Float** = LS − ES (or LF − EF)
6. Activities with Total Float = 0 are on the critical path

**Contoh / Example:**

| Aktiviti | Tempoh (Hari) | Bergantung Kepada | ES | EF | LS | LF | Float | Kritikal? |
|----------|---------------|-------------------|----|----|----|----|-------|-----------|
| A: Requirements analysis | 5 | — | 0 | 5 | 0 | 5 | 0 | Ya |
| B: Network design | 7 | A | 5 | 12 | 5 | 12 | 0 | Ya |
| C: Procurement | 14 | B | 12 | 26 | 12 | 26 | 0 | Ya |
| D: Equipment delivery | 7 | C | 26 | 33 | 26 | 33 | 0 | Ya |
| E: Core switch install | 3 | D | 33 | 36 | 33 | 36 | 0 | Ya |
| F: Server rack install | 5 | D | 33 | 38 | 34 | 39 | 1 | Tidak |
| G: VLAN config | 4 | E | 36 | 40 | 36 | 40 | 0 | Ya |
| H: Integration test | 5 | F, G | 40 | 45 | 40 | 45 | 0 | Ya |

Critical path: A → B → C → D → E → G → H (total: 45 days)

### 3.3 Gantt Chart

A Gantt chart is the primary schedule communication tool. It shows each activity as a horizontal bar on a timeline, with dependencies shown as arrows. Key elements:

- Activity bars (planned vs. actual when tracking begins)
- Milestones (diamond symbols) for key approval points
- Baseline schedule line (for comparison during execution)
- Resource assignments on each bar

**Gantt chart software commonly used:** Microsoft Project, ProjectLibre, Smartsheet, or Jira (for Agile projects).

### 3.4 Schedule Compression Techniques

When the initial schedule exceeds the required deadline, two compression techniques are applied:

| Teknik / Technique | Kaedah / Method | Kesan / Effect |
|--------------------|-----------------|----------------|
| **Crashing** | Add resources to critical path activities | Reduces duration; increases cost |
| **Fast Tracking** | Perform critical path activities in parallel (overlap) | Reduces duration; increases risk |

---

## 4.0 Cost Planning and Budget

### 4.1 Cost Estimation Methods

| Kaedah / Method | Penerangan / Description | Ketelitian / Accuracy |
|-----------------|--------------------------|----------------------|
| **Analogous Estimating** | Use actual costs from similar completed projects | ±25–50% |
| **Parametric Estimating** | Use statistical model (cost per network port × number of ports) | ±10–25% |
| **Bottom-up Estimating** | Estimate each WBS work package individually and sum | ±5–10% |
| **Three-point Estimating (PERT)** | Expected cost = (Optimistic + 4 × Most Likely + Pessimistic) / 6 | ±5–15% |

### 4.2 Project Budget Structure

A complete project budget includes:

| Kategori / Category | Penerangan / Description | Contoh |
|---------------------|--------------------------|--------|
| **Kos Langsung / Direct Costs** | Costs directly attributable to the project | Hardware, software licences, contractor fees |
| **Kos Tidak Langsung / Indirect Costs** | Overhead shared with other projects | Office facilities, utilities, shared staff time |
| **Rizab Luar Jangka / Contingency Reserve** | Buffer for identified risks (typically 10–15%) | Risk register items with quantified impact |
| **Rizab Pengurusan / Management Reserve** | Buffer for unknown unknowns (typically 5–10%) | Controlled by sponsor; not in project manager's baseline |

**Contoh Anggaran Bajet / Sample Budget Estimate:**

| Item | Kuantiti | Harga Unit (RM) | Jumlah (RM) |
|------|----------|-----------------|-------------|
| Core switch (48-port PoE+) | 2 | 28,000 | 56,000 |
| Firewall (NGFW) | 1 | 35,000 | 35,000 |
| Server (rack-mount, 2U) | 3 | 22,000 | 66,000 |
| Wireless access points | 20 | 1,200 | 24,000 |
| Structured cabling (per point) | 150 | 180 | 27,000 |
| Software licences (3-year) | 1 lot | 45,000 | 45,000 |
| Installation labour | 300 hrs | 120/hr | 36,000 |
| Project management | 1 lot | 25,000 | 25,000 |
| Training | 2 sessions | 3,000 | 6,000 |
| **Subtotal** | | | **320,000** |
| Contingency Reserve (12%) | | | 38,400 |
| **JUMLAH KESELURUHAN / TOTAL** | | | **358,400** |

### 4.3 Earned Value Management (EVM)

EVM integrates scope, schedule, and cost performance into a single measurement framework. Key metrics:

| Metrik / Metric | Formula | Tafsiran / Interpretation |
|-----------------|---------|---------------------------|
| **Planned Value (PV)** | Budgeted cost of work scheduled | How much work should have been done by now? |
| **Earned Value (EV)** | Budgeted cost of work performed | How much work has actually been done (in budget terms)? |
| **Actual Cost (AC)** | Actual cost of work performed | How much did the work actually cost? |
| **Schedule Variance (SV)** | EV − PV | Negative = behind schedule |
| **Cost Variance (CV)** | EV − AC | Negative = over budget |
| **Schedule Performance Index (SPI)** | EV / PV | < 1.0 = behind schedule |
| **Cost Performance Index (CPI)** | EV / AC | < 1.0 = over budget |
| **Estimate at Completion (EAC)** | BAC / CPI | Projected total cost at current efficiency |

---

## 5.0 Risk Management Planning

### 5.1 Risk Identification

Risk identification is a continuous process. Common sources of risk in computer system and network projects:

**Risiko Teknikal / Technical Risks:**
- Hardware delivery delays (import restrictions, supply chain disruption)
- Software compatibility issues between new and legacy systems
- Network performance degrading below SLA thresholds
- Security vulnerabilities in newly deployed firmware

**Risiko Pengurusan / Management Risks:**
- Scope creep from undocumented stakeholder requests
- Key technical staff resignation during project execution
- Vendor failure to meet contractual obligations

**Risiko Luaran / External Risks:**
- Regulatory changes affecting data handling requirements
- Power infrastructure unreliability at deployment site
- Cyber-attack during migration window

### 5.2 Risk Assessment — Probability × Impact Matrix

Each identified risk is assessed on two dimensions:

| Kebarangkalian / Probability | Dampak / Impact | Tahap Risiko / Risk Level | Tindakan / Action |
|------------------------------|-----------------|---------------------------|-------------------|
| High (> 60%) | High | **Kritikal** | Immediate mitigation required |
| High (> 60%) | Medium | **Tinggi** | Mitigation plan required |
| Medium (30–60%) | High | **Tinggi** | Mitigation plan required |
| Medium (30–60%) | Medium | **Sederhana** | Monitor; contingency plan |
| Low (< 30%) | Any | **Rendah** | Monitor; accept |

### 5.3 Risk Response Strategies

| Strategi / Strategy | Penerangan / Description | Contoh |
|---------------------|--------------------------|--------|
| **Elak / Avoid** | Change plan to eliminate the risk | Use local stock components to avoid import delays |
| **Kurang / Mitigate** | Reduce probability or impact | Install redundant links to reduce single-point-of-failure impact |
| **Pindah / Transfer** | Shift risk to a third party | Procure hardware with vendor SLA and replacement guarantee |
| **Terima / Accept** | Acknowledge and proceed (with contingency) | Accept minor schedule slippage risk; hold contingency reserve |

### 5.4 Risk Register

The Risk Register is the living document that records all identified risks and their management plans:

| ID | Keterangan Risiko / Risk Description | Kebarangkalian | Dampak | Tahap | Strategi | Pemilik | Status |
|----|--------------------------------------|----------------|--------|-------|----------|---------|--------|
| R-001 | Hardware delivery delayed > 2 weeks | Medium | High | Tinggi | Mitigate — confirm stock with secondary vendor | Procurement Manager | Open |
| R-002 | Legacy system incompatible with new switches | Low | High | Sederhana | Mitigate — conduct compatibility test pre-deployment | Network Engineer | Open |
| R-003 | Key network engineer resigns during project | Low | High | Sederhana | Transfer — cross-train backup engineer | HR / PM | Open |
| R-004 | Configuration errors causing network outage during cutover | Medium | High | Kritikal | Avoid — perform cutover in maintenance window; rollback plan ready | Network Engineer | Open |

---

## 6.0 Subsidiary Plans

A complete project management plan integrates the following subsidiary plans:

| Pelan / Plan | Kandungan Utama / Key Content |
|--------------|-------------------------------|
| **Pengurusan Skop / Scope Management Plan** | How scope is defined, validated, and controlled |
| **Pengurusan Jadual / Schedule Management Plan** | Scheduling tool, update frequency, schedule baseline approval |
| **Pengurusan Kos / Cost Management Plan** | Estimation method, cost baseline, EVM reporting thresholds |
| **Pengurusan Kualiti / Quality Management Plan** | Quality standards, QA activities, QC inspection checklist |
| **Pengurusan Risiko / Risk Management Plan** | Risk process, probability/impact scales, risk register ownership |
| **Pengurusan Komunikasi / Communications Management Plan** | Who gets what information, in what format, how often |
| **Pengurusan Pengadaan / Procurement Management Plan** | Procurement strategy, contract types, vendor evaluation criteria |
| **Pengurusan Pihak Berkepentingan / Stakeholder Management Plan** | Engagement strategies for each stakeholder group |
| **Pengurusan Sumber Manusia / Human Resource Management Plan** | Team roles, responsibilities, RACI chart, training needs |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer System Management — CoCU 5
- PMI. (2021). *PMBOK® Guide*, 7th Edition. Project Management Institute.
- AXELOS. (2017). *Managing Successful Projects with PRINCE2*, 6th Edition.
- Kerzner, H. (2022). *Project Management: A Systems Approach to Planning, Scheduling, and Controlling*, 13th Edition. Wiley.
- Microsoft Project documentation — microsoft.com/project
- ISO 21502:2020 — Project, Programme and Portfolio Management — Guidance on Project Management