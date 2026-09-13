# 00-CU-SPEC — AI for ISO Quality Management Specialist Programme
**Source of truth for 7 writing agents. Extract only. Gaps marked `[derived — not in proposal]`.**

---

## Programme Identity

| Field | Value | Source |
|-------|-------|--------|
| **Programme Code** | ISO-AI-3:2026 | Proposal header table |
| **Programme Name (English)** | AI for ISO Quality Management Specialist Programme | Proposal heading line 2 |
| **Programme Name (Chinese)** | AI 品质管理体系专才培训计划 | Proposal heading line 1 |
| **Programme Name (Malay)** | NOT STATED IN PROPOSAL — proposal gives no Malay programme name. The CU-level Malay names exist but the programme-level Malay title is absent. `[gap]` |
| **TAHAP (Level)** | 3 | Proposal section 7.3A: "Sijil Kemahiran Malaysia (SKM) 第3级" |
| **Scheme** | PTPK Skim TBT 2026 — Bidang Kecerdasan Buatan (AI Priority Field) | Proposal header table |
| **Total Hours** | 280 hours (7 CU × 40 hours) | Proposal header table |
| **Knowledge / Practical Split** | 30% theory / 70% practical (84 hrs / 196 hrs) | Proposal Appendix A |
| **Training Provider** | Character Academy Sdn Bhd (rep: Tan Siow Inn / Jennifer) | Proposal header table |
| **Content Partner** | 3U Pioneer Academy Sdn Bhd + Prisma Technology Sdn Bhd | Proposal header table |

> **Code discrepancy note:** The proposal states the programme code as `ISO-AI-3:2026` in the header table and in the LOI template. No other code variant appears in this document. The instruction note mentioned a possible discrepancy with a live website showing `ISO-AI-3:2026` — this is **the same code**, so no discrepancy is present within the proposal itself. If the live website shows a different code, that cannot be verified from this document; do not silently substitute.

---

## 30/70 Split Rule

Every CU must maintain exactly **12 hours theory / 28 hours practical / 40 hours total**.
This is a hard constraint from the JPK CBT framework. Do not deviate.

---

## Malaysian Grounding

The following Malaysian bodies, regulations, standards, and real-world contexts are **legitimately referenced in the proposal** and must appear where relevant across WIM content:

### Regulatory & Standards Bodies
- **SIRIM QAS International Sdn Bhd** — national ISO certification body; issues MS ISO 9001 certification; referenced throughout
- **Department of Standards Malaysia (STANDARDS MALAYSIA)** — custodian of Malaysian Standards (MS prefix); referenced implicitly via SIRIM
- **JPK (Jabatan Pembangunan Kemahiran)** — CBT framework authority; all WIM must comply with JPK structure
- **HRD Corp** — training subsidy body; SBL-Khas and Skim Bantuan Latihan applicable to employers of graduates

### Applicable Laws & Regulations
- **Personal Data Protection Act 2010 (PDPA, Act 709)** — cited in C02 for document retention rules
- **ISO 9001:2015** — the primary quality management standard; all 7 CU map to specific clauses
- **ISO 19011** — auditor competency guidelines; cited in C05
- **IATF 16949** — automotive QMS standard; referenced in employer profile (not a training objective)
- **ISO 13485** — medical device QMS; referenced in employer profile only
- **ISO 22000 / HACCP** — food safety; referenced in employer profile only

### Industry Policy Context
- **NIMP 2030** — National Investment Master Plan; each CU maps to a NIMP thrust (see Appendix A of proposal)
- **Industry4WRD** — national Industry 4.0 framework; AI-QMS skills align with CFF competency framework
- **MyDIGITAL Blueprint 2021–2030** — digital workforce target; this programme contributes to manufacturing digital talent
- **MIDA Capital Allowance for Automation (CA)** — graduate employers may qualify
- **FMM (Federation of Malaysian Manufacturers)** — [derived — not in proposal] relevant industry body for manufacturing sector; likely real-world context for Johor industrial belt

### Real-World Industry Context
- **Pasir Gudang Industrial Estate / Senai Industrial Park (Johor)** — primary placement zone; precision manufacturing
- **Shah Alam / Bukit Raja Industrial Area (Selangor)** — automotive and general manufacturing
- **Bayan Lepas Free Industrial Zone (Penang)** — E&E manufacturing
- **PROTON / PERODUA Tier-1 and Tier-2 supplier chain** — automotive QMS context
- **SME manufacturing sector** — AI tool adoption rate below 15% as cited in proposal (2025 survey; verify source before quoting in WIM)

### AI Tools Referenced in Proposal (use as practical tool references in WIM)
- AuditBoard AI, TeamMate AI (Wolters Kluwer) — audit tools (C05)
- M-Files AI, SharePoint AI, DocuWare — document management (C02)
- Power BI AI, Tableau AI, Google Looker — analytics/KPI (C07)
- Python data analytics, n8n, Make — automation platforms (general)

---

## CU Specifications

### C01 — AI FUNDAMENTALS FOR QUALITY MANAGEMENT

| Field | Value |
|-------|-------|
| **CU Code** | ISO-AI-3:2026-C01 |
| **CU Title (English)** | AI FUNDAMENTALS FOR QUALITY MANAGEMENT |
| **CU Title (Chinese)** | AI 品质管理基础 |
| **CU Title (Malay)** | Asas AI untuk Pengurusan Kualiti |
| **Hours** | 12 theory / 28 practical / 40 total |
| **NIMP 2030 Thrust** | Thrust 5: Technology Adoption & Innovation in Manufacturing |

**Work Activities (Aktiviti Kerja) — for JPK envelope `NO. DAN PERNYATAAN AKTIVITI KERJA`:**
1. ASSESS CURRENT QMS FOR AI INTEGRATION OPPORTUNITIES
2. MAP ISO 9001:2015 CLAUSES TO AI TOOLS
3. DEVELOP AI IMPLEMENTATION ROADMAP FOR QUALITY DEPARTMENT
4. EVALUATE AI TOOL SUITABILITY FOR QMS APPLICATIONS `[derived — not in proposal; proposal lists only 3 work activities for C01; 4th added to meet JPK 4-activity standard]`

**Knowledge Topics (KP files):**

**KP-01: ISO 9001:2015 Structure and AI Alignment**
Scope: Full clause-by-clause overview of ISO 9001:2015 (context, leadership, planning, support, operation, performance evaluation, improvement). Map each clause group to the AI capability that can automate or augment it. Establish the foundation all subsequent CUs build upon.

**KP-02: AI Types and Applications in Quality Management**
Scope: Computer Vision (visual inspection), Natural Language Processing (document review, NCR classification), Predictive Analytics (risk forecasting), and Machine Learning (pattern detection in production data). Real examples from Malaysian manufacturing context. How each AI type addresses specific ISO requirements.

**KP-03: SIRIM MS ISO Certification Process and Industry 4.0 Quality Pillars**
Scope: SIRIM QAS International certification pathway for MS ISO 9001 — application, document review, Stage 1 audit, Stage 2 audit, surveillance. Industry 4.0 four pillars for quality: digitalisation, connectivity, intelligence, automation. Malaysian SME context; why AI adoption lags and how this programme addresses the gap.

**Practical Tasks (KK files):**

**KK-01: QMS-AI Opportunity Assessment**
Scope: Trainees conduct a structured AI-readiness audit of a simulated or real manufacturing company's current QMS. Use a provided checklist to identify which ISO clauses are currently manual/paper-based, rate AI integration maturity (1–5 scale), and produce a written opportunity assessment report with prioritised recommendations.

**KK-02: ISO-AI Clause Mapping and Roadmap Development**
Scope: Trainees produce a completed ISO 9001:2015-to-AI-tools mapping table (all 10 clauses) and draft a 6-month AI implementation roadmap for the quality department of the simulated company. Roadmap includes tool selection rationale, phasing, and expected KPI improvement targets.

---

### C02 — AI DOCUMENT CONTROL AND MANAGEMENT SYSTEM

| Field | Value |
|-------|-------|
| **CU Code** | ISO-AI-3:2026-C02 |
| **CU Title (English)** | AI DOCUMENT CONTROL AND MANAGEMENT SYSTEM |
| **CU Title (Chinese)** | AI 文件控制与管理系统 |
| **CU Title (Malay)** | Kawalan Dokumen AI & Sistem Pengurusan |
| **Hours** | 12 theory / 28 practical / 40 total |
| **NIMP 2030 Thrust** | Thrust 3: Operational Excellence (Process Efficiency) |

**Work Activities:**
1. IMPLEMENT AI-POWERED DOCUMENT VERSION CONTROL SYSTEM
2. AUTOMATE DOCUMENT APPROVAL WORKFLOWS
3. USE AI TO ENSURE DOCUMENT COMPLIANCE WITH ISO REQUIREMENTS
4. MANAGE DOCUMENT RETENTION IN ACCORDANCE WITH PDPA 2010 `[derived — not in proposal; 4th activity inferred from PDPA knowledge requirement stated in proposal]`

**Knowledge Topics (KP files):**

**KP-01: ISO 9001 Clause 7.5 — Documented Information Requirements**
Scope: Full unpacking of ISO 9001:2015 Clause 7.5 (creation, update, control of documented information). Document types: mandatory procedures, records, work instructions, quality manual. Version control principles: review cycles, approval authority, obsolete document control. SIRIM auditor expectations for document systems.

**KP-02: AI Document Management Platforms and OCR Technology**
Scope: Overview of AI-enabled DMS platforms (SharePoint AI, M-Files AI, DocuWare). How NLP automates version conflict detection, expiry alerts, and compliance checking. OCR and AI text extraction for digitising legacy paper-based QMS documents. Electronic signature compliance under Malaysian law.

**KP-03: PDPA 2010 Document Retention and Electronic Record Compliance**
Scope: Personal Data Protection Act 2010 (Act 709) requirements for document retention periods, data subject access rights, and secure disposal. Electronic signature legal validity in Malaysia. Practical PDPA compliance checklist for QMS document controllers. Cross-reference with ISO 9001 Clause 7.5.3 (control of documented information).

**Practical Tasks (KK files):**

**KK-01: AI Document Version Control Setup**
Scope: Trainees configure a simulated AI document management environment (using available free tools or provided lab environment). Upload a set of sample ISO documents, apply version numbering, set approval workflows, and test automated expiry alerts. Produce a before/after comparison showing manual vs. AI-assisted document cycle time.

**KK-02: Document Compliance Audit Using AI Tools**
Scope: Given a set of 10 sample QMS documents (some compliant, some non-compliant with ISO 7.5 requirements), trainees use AI tools to identify compliance gaps, generate a corrective action list, and produce a document compliance report. Includes PDPA retention schedule for the simulated company's document types.

---

### C03 — NON-CONFORMANCE TRACKING AND ROOT CAUSE ANALYSIS WITH AI

| Field | Value |
|-------|-------|
| **CU Code** | ISO-AI-3:2026-C03 |
| **CU Title (English)** | NON-CONFORMANCE TRACKING AND ROOT CAUSE ANALYSIS WITH AI |
| **CU Title (Chinese)** | AI 不符合项追踪与根因分析 |
| **CU Title (Malay)** | Penjejakan NCR & RCA dengan AI |
| **Hours** | 12 theory / 28 practical / 40 total |
| **NIMP 2030 Thrust** | Thrust 4: Quality & Standards Competitiveness |

**Work Activities:**
1. LOG AND CATEGORIZE NON-CONFORMANCES USING AI CLASSIFICATION ENGINE
2. CONDUCT ROOT CAUSE ANALYSIS USING AI-ASSISTED 5-WHY AND FISHBONE METHODS
3. TRACK CORRECTIVE ACTIONS TO CLOSURE USING AI WORKFLOW
4. GENERATE CAPA CLOSURE REPORTS AND VERIFY EFFECTIVENESS `[derived — not in proposal; proposal lists 3 work activities; 4th derived from CAPA lifecycle knowledge requirement]`

**Knowledge Topics (KP files):**

**KP-01: ISO 9001 Clause 10.2 — Nonconformity and Corrective Action**
Scope: Full clause requirements: react to nonconformity, evaluate root cause, implement corrective action, review effectiveness. NCR lifecycle: raise → investigate → root cause → corrective action → verification → close. SIRIM expectations for NCR records. Difference between correction (immediate fix) and corrective action (root cause elimination).

**KP-02: AI-Powered Root Cause Analysis Tools and Methodologies**
Scope: 5-Why method with AI augmentation — how AI suggests additional "why" branches from historical data. Fishbone (Ishikawa) diagram categories (6M: Man, Machine, Method, Material, Measurement, Environment). 8D problem-solving methodology overview. AI classification engines: how they assign NCRs to root cause categories using ML trained on historical defect data.

**KP-03: CAPA System Architecture and NCR Management Platforms**
Scope: CAPA system structure — corrective action vs. preventive action. AI workflow platforms for CAPA: auto-assignment, escalation triggers, reminder notifications, closure verification. Integration with production data for trend analysis. Key KPIs: NCR close rate, repeat NCR rate, average resolution time. Malaysian manufacturing context: typical defect categories in E&E and automotive sectors.

**Practical Tasks (KK files):**

**KK-01: NCR Logging and AI Classification Exercise**
Scope: Trainees receive a set of 15 simulated production defect reports. Using provided AI classification tool or structured prompts, categorise each NCR by defect type, affected process, and root cause category. Complete a standard NCR form for 3 selected cases. Produce a summary table showing defect distribution by category.

**KK-02: Root Cause Analysis and CAPA Documentation**
Scope: For 2 assigned NCR cases, trainees conduct full AI-assisted RCA using 5-Why and Fishbone methods. Document findings, propose corrective and preventive actions, set target completion dates, and simulate workflow closure sign-off. Present one completed CAPA package including effectiveness verification criteria.

---

### C04 — AI RISK ASSESSMENT AND FMEA

| Field | Value |
|-------|-------|
| **CU Code** | ISO-AI-3:2026-C04 |
| **CU Title (English)** | AI RISK ASSESSMENT AND FMEA |
| **CU Title (Chinese)** | AI 风险评估与 FMEA |
| **CU Title (Malay)** | Penilaian Risiko AI & FMEA |
| **Hours** | 12 theory / 28 practical / 40 total |
| **NIMP 2030 Thrust** | Thrust 4: Quality & Standards Competitiveness |

**Work Activities:**
1. CONDUCT RISK ASSESSMENT USING AI RISK SCORING TOOLS
2. PERFORM FMEA WITH AI ASSISTANCE
3. UPDATE RISK REGISTER AUTOMATICALLY BASED ON PRODUCTION DATA
4. DEVELOP PREVENTIVE ACTION PLANS FROM AI-GENERATED RISK INSIGHTS `[derived — not in proposal; proposal lists 3 work activities; 4th derived from preventive action planning knowledge requirement]`

**Knowledge Topics (KP files):**

**KP-01: ISO 9001 Clause 6.1 — Risk and Opportunity Management**
Scope: Clause 6.1 requirements: determine risks and opportunities, plan actions, integrate into QMS. Risk thinking vs. preventive action (shift in ISO 9001:2015 vs. 2008). Risk register structure: risk description, likelihood, severity, detection, RPN, owner, action status. How AI pre-populates risk registers from historical production and NCR data.

**KP-02: FMEA Methodology — DFMEA and PFMEA with AI Assistance**
Scope: Design FMEA (DFMEA) vs. Process FMEA (PFMEA) — scope, inputs, outputs. RPN calculation: Severity (S) × Occurrence (O) × Detection (D), scale 1–10. Threshold RPN for mandatory action. How AI tools suggest failure modes from similar process databases. AIAG-VDA FMEA 2019 alignment `[derived — not in proposal; AIAG-VDA is the current industry standard referenced implicitly through IATF 16949 employer context]`. Malaysian automotive sector PFMEA examples.

**KP-03: AI Risk Assessment Platforms and Supply Chain Risk**
Scope: Overview of AI risk assessment platforms. Predictive analytics: how real-time sensor and production data feeds risk scoring updates. Supply chain risk categories: single-source supplier dependency, geopolitical risk, lead time variability. How AI dashboards provide early warning signals. Integration with risk register auto-update workflow.

**Practical Tasks (KK files):**

**KK-01: Risk Register Development and AI Risk Scoring**
Scope: Trainees complete a risk register for a simulated manufacturing process (provided scenario). Identify minimum 10 risks across ISO 9001 clause areas. Use AI risk scoring prompts to rate S/O/D, calculate RPN, and prioritise top 5 risks. Produce a formatted risk register document suitable for SIRIM audit evidence.

**KK-02: PFMEA for a Simulated Production Process**
Scope: Trainees conduct a Process FMEA for a defined 5-step production process (provided). Using AI assistance to suggest failure modes, complete the FMEA table: process step, potential failure mode, potential effect, S rating, potential cause, O rating, current controls, D rating, RPN, recommended action. Identify and document preventive actions for top 3 high-RPN items.

---

### C05 — AI INTERNAL AUDIT PLANNING AND MANAGEMENT

| Field | Value |
|-------|-------|
| **CU Code** | ISO-AI-3:2026-C05 |
| **CU Title (English)** | AI INTERNAL AUDIT PLANNING AND MANAGEMENT |
| **CU Title (Chinese)** | AI 内审规划与管理 |
| **CU Title (Malay)** | Perancangan & Pengurusan Audit Dalaman AI |
| **Hours** | 12 theory / 28 practical / 40 total |
| **NIMP 2030 Thrust** | Thrust 3: Operational Excellence (Audit Efficiency) |

**Work Activities:**
1. DEVELOP AI-ASSISTED ANNUAL AUDIT SCHEDULE
2. CONDUCT PAPERLESS INTERNAL AUDITS USING DIGITAL TOOLS
3. GENERATE AUDIT FINDINGS REPORTS AUTOMATICALLY
4. EVALUATE AUDITOR COMPETENCY REQUIREMENTS PER ISO 19011 `[derived — not in proposal; proposal lists 3 work activities; 4th derived from ISO 19011 auditor competency knowledge requirement stated in proposal]`

**Knowledge Topics (KP files):**

**KP-01: ISO 9001 Clause 9.2 — Internal Audit Requirements and ISO 19011 Guidelines**
Scope: Clause 9.2 requirements: audit programme, criteria, scope, frequency, method, reporting, corrective action. ISO 19011:2018 guidelines for auditing management systems — auditor competency attributes (knowledge, skills, personal attributes), audit principles (integrity, fair presentation, due professional care, confidentiality, independence, evidence-based approach, risk-based approach). SIRIM expectations for internal audit records.

**KP-02: AI Audit Tools and Digital Audit Execution**
Scope: AuditBoard AI and TeamMate AI (Wolters Kluwer) — feature overview, how AI suggests audit sampling strategy, flags high-risk areas based on NCR history and risk register data. Paperless audit workflow: mobile data collection, photo evidence capture, real-time finding entry. Audit checklist development: translating ISO clauses into verifiable audit questions. Evidence collection methods: interview, observation, document review.

**KP-03: Audit Report Generation and Audit Programme Management**
Scope: Automated audit report structure: executive summary, scope, criteria, findings (major NC / minor NC / observation / opportunity for improvement), conclusion, corrective action requirements. AI auto-generation of report from field entries. Audit programme management: scheduling by risk level, tracking closure of previous findings, trend analysis across audit cycles. Handling audit findings that escalate to NCR/CAPA.

**Practical Tasks (KK files):**

**KK-01: AI-Assisted Audit Schedule and Checklist Development**
Scope: Trainees develop a 12-month internal audit schedule for a simulated 8-department manufacturing company. Use AI tools to risk-rank departments and allocate audit frequency accordingly. Develop a clause-by-clause audit checklist for ISO 9001 Clause 8 (Operation) for one assigned department. Checklist must include minimum 20 audit questions with evidence type specified.

**KK-02: Simulated Internal Audit and Report Generation**
Scope: Trainees conduct a role-play internal audit using the checklist developed in KK-01. One trainee acts as auditee (using provided scenario information cards), one as auditor. Record findings using digital form. Use AI to draft the audit findings report. Review and finalise report for submission. Includes one major NC, one minor NC, and one observation minimum.

---

### C06 — SUPPLIER QUALITY MANAGEMENT WITH AI

| Field | Value |
|-------|-------|
| **CU Code** | ISO-AI-3:2026-C06 |
| **CU Title (English)** | SUPPLIER QUALITY MANAGEMENT WITH AI |
| **CU Title (Chinese)** | AI 供应商质量管理 |
| **CU Title (Malay)** | Pengurusan Kualiti Pembekal dengan AI |
| **Hours** | 12 theory / 28 practical / 40 total |
| **NIMP 2030 Thrust** | Thrust 2: Supply Chain Resilience & Efficiency |

**Work Activities:**
1. EVALUATE AND QUALIFY SUPPLIERS USING AI SCORING SYSTEMS
2. MONITOR SUPPLIER PERFORMANCE WITH AI DASHBOARDS
3. MANAGE SUPPLIER NON-CONFORMANCES
4. CONDUCT INCOMING INSPECTION USING AI VISION SYSTEMS `[derived — not in proposal; proposal lists 3 work activities but explicitly mentions AI Vision Systems for incoming inspection in knowledge requirements; this legitimately extends to a 4th work activity]`

**Knowledge Topics (KP files):**

**KP-01: ISO 9001 Clause 8.4 — Control of Externally Provided Processes, Products and Services**
Scope: Clause 8.4 requirements: type and extent of control, information for external providers, supplier evaluation, monitoring and re-evaluation. Supplier evaluation criteria: quality performance (defect rate, NCR history), delivery reliability, responsiveness, financial stability, certifications held. Approved Vendor List (AVL) management. SIRIM audit expectations for supplier control records.

**KP-02: AI Supplier Management Platforms and Vendor Scorecard Automation**
Scope: AI-enabled supplier management platforms — how they aggregate delivery, quality, and cost data into automated scorecards. Vendor scorecard metrics: on-time delivery rate, incoming defect rate, NCR response time, corrective action close rate. Supplier development programmes: escalation tiers, improvement plans, disqualification triggers. AI anomaly detection for supply chain risk signals (demand spikes, single-source dependency).

**KP-03: AI Vision Systems for Incoming Inspection and Supplier NCR Management**
Scope: AI visual inspection systems for incoming goods: how computer vision detects dimensional defects, surface flaws, labelling errors. Implementation considerations for Malaysian SME context (cost, infrastructure). Supplier NCR process: raise supplier NCR → 8D response requirement → containment action → root cause → corrective action → re-audit. Supplier development vs. disqualification decision framework.

**Practical Tasks (KK files):**

**KK-01: Supplier Evaluation and Scorecard Development**
Scope: Trainees receive performance data for 5 simulated suppliers (delivery records, defect rates, NCR history, certifications). Using a provided AI-assisted scoring template, calculate weighted supplier scores, rank suppliers, update the Approved Vendor List, and flag one supplier for development programme. Produce a completed vendor scorecard for each supplier.

**KK-02: Supplier NCR Management and Incoming Inspection Simulation**
Scope: Trainees process 3 simulated supplier NCR cases: complete supplier NCR forms, issue 8D request letters to suppliers, evaluate submitted 8D responses for adequacy, and decide disposition (accept / hold / return). Includes a simulated incoming inspection exercise using a provided defect image set, applying AI-vision decision criteria.

---

### C07 — CONTINUOUS IMPROVEMENT AND KPI ANALYTICS WITH AI

| Field | Value |
|-------|-------|
| **CU Code** | ISO-AI-3:2026-C07 |
| **CU Title (English)** | CONTINUOUS IMPROVEMENT AND KPI ANALYTICS WITH AI |
| **CU Title (Chinese)** | AI 持续改进与 KPI 分析 |
| **CU Title (Malay)** | Penambahbaikan Berterusan & Analitik KPI dengan AI |
| **Hours** | 12 theory / 28 practical / 40 total |
| **NIMP 2030 Thrust** | Thrust 5: Technology Adoption & Innovation in Manufacturing |

**Work Activities:**
1. ANALYZE QUALITY KPIS USING AI-POWERED DASHBOARDS
2. IDENTIFY IMPROVEMENT OPPORTUNITIES USING AI PATTERN RECOGNITION
3. IMPLEMENT KAIZEN INITIATIVES WITH AI TRACKING SYSTEM
4. PREPARE MANAGEMENT REVIEW INPUTS USING AI-GENERATED QUALITY REPORTS `[derived — not in proposal; proposal lists 3 work activities; 4th derived from ISO 9001 Clause 9.3 Management Review knowledge requirement stated in proposal]`

**Knowledge Topics (KP files):**

**KP-01: ISO 9001 Clause 10.3 and Quality KPI Framework**
Scope: Clause 10.3 (Continual Improvement) requirements: react to opportunities, improve processes, products, services, and QMS. Quality KPI definitions and calculation: OEE (Availability × Performance × Quality), Yield Rate (good units / total units), PPM Defects (defects per million opportunities), First Pass Yield, Cost of Poor Quality (COPQ). Setting KPI targets: benchmarking against Malaysian manufacturing sector norms. ISO 9001 Clause 9.3 Management Review inputs and outputs.

**KP-02: AI Analytics Tools for Quality — Power BI, Tableau, and Statistical Process Control**
Scope: Power BI AI and Tableau AI: building quality dashboards, setting automated alerts, using Q&A natural language queries. Google Looker for shared reporting. AI-enabled Statistical Process Control (SPC): control charts (X-bar/R, P-chart, C-chart), how AI detects out-of-control signals and triggers alerts. Difference between common cause and special cause variation. Real-time production data integration.

**KP-03: Lean Six Sigma, Kaizen, and AI-Assisted DMAIC**
Scope: Lean Six Sigma DMAIC methodology: Define, Measure, Analyse, Improve, Control. How AI accelerates each DMAIC phase: AI-assisted data collection (Measure), pattern recognition (Analyse), simulation (Improve). Kaizen event structure: scope, team, 5-day rapid improvement event, A3 report. AI tracking of Kaizen action items to closure. Management Review preparation: compiling AI-generated dashboard outputs into Management Review input report per ISO 9001 Clause 9.3.

**Practical Tasks (KK files):**

**KK-01: AI Quality Dashboard Design and KPI Analysis**
Scope: Trainees build a quality dashboard using Power BI (or equivalent provided tool) from a supplied dataset (12 months of simulated production quality data). Dashboard must display: OEE trend, monthly NCR count by category, Yield Rate trend, top 5 defect types (Pareto), and one SPC control chart. Trainees identify 2 out-of-control signals and recommend corrective actions.

**KK-02: Kaizen Project and Management Review Report**
Scope: Trainees select one improvement opportunity identified in KK-01 and complete a Kaizen A3 report: problem statement, current state analysis (using AI-generated data), target state, root cause (5-Why), countermeasures, implementation plan, and follow-up. Additionally, compile a 1-page Management Review Input Report from the dashboard data, formatted per ISO 9001 Clause 9.3 requirements. Present findings to trainer panel (simulated Management Review).

---

## Content Thinness Warnings for Writing Agents

The following CUs have areas where the proposal is vague and agents must derive content rather than extract it:

| CU | Issue | Severity |
|----|-------|----------|
| **C01** | Only 3 work activities in proposal; 4th is derived. | Low — 4th activity is logically coherent |
| **C02** | Only 3 work activities; 4th (PDPA retention) is derived from knowledge requirement. | Low — well-grounded in cited regulation |
| **C03** | Only 3 work activities; 4th (CAPA closure/verification) is derived from CAPA knowledge requirement. | Low — standard CAPA lifecycle step |
| **C04** | Only 3 work activities; 4th (preventive action planning) is derived. Also: AIAG-VDA 2019 reference is derived from automotive employer context, not directly cited. | Medium — FMEA methodology details need subject matter accuracy check |
| **C05** | Only 3 work activities; 4th (ISO 19011 competency evaluation) is derived from knowledge requirement. | Low — proposal explicitly cites ISO 19011 |
| **C06** | Only 3 work activities; 4th (AI Vision incoming inspection) is partially derived — proposal mentions it in knowledge but not as a work activity. | Low — legitimately supported |
| **C07** | Only 3 work activities; 4th (management review report) is derived from Clause 9.3 knowledge requirement. | Low — well-grounded |
| **ALL CU** | Practical task details (step counts, tool scenarios, assessment rubrics) are entirely absent from proposal — all KK scope notes are derived from best practice. | High — agents have full creative latitude for KK content within the stated work activity scope |
| **ALL CU** | No sample assessment questions, marking schemes, or PA criteria are in the proposal. KA and PA files will need to be derived by agents from CoCU assessment criteria conventions. | High |
| **Programme** | No Malay programme-level name in proposal. | Low for WIM purposes — CU-level Malay names are provided |

---

## JPK Envelope Template for This Programme

All WIM files in C01–C07 must open with the JPK envelope block. Use this identification table template:

```
| KOD DAN NAMA PROGRAM        | ISO-AI-3:2026 AI FOR ISO QUALITY MANAGEMENT SPECIALIST PROGRAMME |
| TAHAP                       | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | ISO-AI-3:2026-C0n <CU TITLE IN UPPERCASE> |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. <WORK ACTIVITY 1><br>2. <WORK ACTIVITY 2><br>3. <WORK ACTIVITY 3><br>4. <WORK ACTIVITY 4> |
| NO. KOD                     | ISO-AI-3:2026-C0n/<DOC TYPE>(<seq>/<total>) |
| Muka Surat                  | 1/1 |
| WARNA KERTAS                | <colour per doc type> |
```

Paper colour by document type (per JPK standard):
- KP (Information Sheet / Kertas Penerangan): PUTIH (White)
- KK (Work Sheet / Kertas Kerja): BIRU (Blue)
- KA (Knowledge Assessment): MERAH JAMBU (Pink)
- PA (Performance Assessment): BIRU MUDA (Light Blue)
- PM-Teori / PM-Amali (Lesson Plans): KUNING (Yellow)
- KT (Assignment Sheet): MERAH JAMBU (Pink)

Logo path: `../_assets/logos/jpk-logo.png` (relative from CU subfolder)

---

*Spec version: 1.0 | Compiled: 2026-07-29 | Source: ai-iso-proposal.md V2.0 (2026-07-25)*
