# 00-CU-SPEC — AI for Admin / Office Administration Programme
## Source of Truth for WIM Writing Agents (C01–C07)

> **Read this file first.** All 7 writing agents must extract their CU data from this file.
> Do NOT invent content not listed here. Where content is marked `[derived — not in proposal]`,
> agents may use professional judgment but must flag it in the WIM with a note.
>
> Last updated: 2026-07-29

---

## Programme Identity

| Field | Value |
|-------|-------|
| **Programme Code (Kod Program)** | `ADMIN-AI-3:2026` |
| **Programme Name (English)** | AI Workflow Automation & Digital Governance Specialist Programme |
| **Programme Name (Malay / Nama Program BM)** | Program Pakar Automasi Aliran Kerja AI & Tadbir Urus Digital |
| **Programme Name (Chinese / 计划名称)** | AI 工作流程自动化与数字治理专才培训计划 |
| **TAHAP (Level)** | 3 |
| **JPK NOSS Code** | `ADMIN-AI-3:2026` *(as stated in proposal; formal JPK registration pending — do NOT invent a NOSS-style code beyond what the proposal states)* |
| **Total Hours (C01–C07)** | 280 hours |
| **Theory : Practical Ratio (C01–C07)** | 30% : 70% — 84 hours theory : 196 hours practical |
| **Hours per CU** | 40 (12 theory + 28 practical) |
| **Capstone (C08)** | 80 hours industrial attachment — NOT included in WIM writing scope for this batch |
| **Submitting Institution** | Prisma Technology Sdn Bhd (Main Applicant) |
| **Curriculum Developer** | 3U Pioneer Academy Sdn Bhd |
| **Target Cohort** | 25 trainees per batch |
| **Scheme** | Skim Tabung Bakat Tempatan (TBT) 2026 — Train and Place |

---

## 30/70 Split Rule

> **Every CU must hold exactly 12 hours theory and 28 hours practical.**
> Summing across C01–C07: 7 × 12 = 84 hours theory, 7 × 28 = 196 hours practical = 280 hours total.
> This is a hard JPK compliance requirement. Do not adjust the split.

---

## Malaysian Grounding

The following Malaysian legal, regulatory, and market contexts are legitimately relevant to this programme. Writing agents must weave these in where the CU content naturally calls for it — do not force all items into every CU.

| Context | Relevant CUs | Notes |
|---------|-------------|-------|
| **PDPA 2010 (Akta Perlindungan Data Peribadi 2010 — Act 709)** | C02, C03, C04, C07 | Consent, notice, disclosure, security, retention, access principles; penalties (as amended by Act A1727, in force 1 Apr 2025) up to RM1,000,000 / 3 years imprisonment |
| **Employment Act 1955 (Akta Kerja 1955)** | C03 | Leave entitlement, overtime rules, termination provisions — governs what HR automation must comply with |
| **EPF (KWSP) / SOCSO (PERKESO) / EIS (SIP) statutory contributions** | C03, C04 | Calculation rules, monthly submission deadlines, e-Caruman portal |
| **SST — Sales and Service Tax (Cukai Jualan dan Perkhidmatan)** | C04 | Basic compliance; when to charge SST; SST-02 return basics |
| **LHDN e-Invoicing** | C04 | MyInvois system mandatory rollout; e-Invoice format requirements for SMEs |
| **SSM (Suruhanjaya Syarikat Malaysia)** | C04 | Business registration filings, annual return submission — admin staff role in documentation |
| **MCMC AI Usage Guidelines** | C07 | Malaysian Communications and Multimedia Commission guidance on responsible AI use |
| **Common Malaysian SME Accounting Software** | C04, C06 | AutoCount, SQL Accounting — most prevalent in Malaysian SMEs; integration with AI tools |
| **Microsoft 365 / Google Workspace** | C01, C02, C05 | Dominant office suites in Malaysia; Copilot and Gemini AI features specifically |
| **Bahasa Malaysia (BM) Business Correspondence** | C02 | Official government-standard BM letter format (Surat Rasmi); memo (memorandum); minutes (minit mesyuarat) |
| **n8n / Zapier / Microsoft Power Automate** | C01, C05 | Workflow automation platforms referenced in proposal |
| **Kakitangan.com** | C03 | Malaysian-built HR platform; widely used by SMEs for leave, payroll, attendance |

---

## CU Specifications

---

### C01 — PLAN AI AUTOMATION STRATEGY FOR OFFICE OPERATIONS

| Field | Value |
|-------|-------|
| **CU Code** | `ADMIN-AI-3:2026-C01` |
| **CU Title (English — uppercase)** | PLAN AI AUTOMATION STRATEGY FOR OFFICE OPERATIONS |
| **CU Title (Chinese)** | 办公室 AI 自动化策略规划 |
| **CU Title (Malay)** | Perancangan Strategi Automasi Pejabat AI |
| **Hours** | 12 theory + 28 practical = 40 total |

#### Work Activities (NO. DAN PERNYATAAN AKTIVITI KERJA)

These 4 items are the exact text used in the JPK envelope `NO. DAN PERNYATAAN AKTIVITI KERJA` field for every KP and KK file in C01.

1. ASSESS CURRENT OFFICE WORKFLOWS AND IDENTIFY AUTOMATION OPPORTUNITIES
2. DESIGN AN AI IMPLEMENTATION ROADMAP WITH TOOL SELECTION AND BUDGET PLAN
3. DEVELOP A CHANGE MANAGEMENT PLAN FOR AI ADOPTION IN THE WORKPLACE
4. EVALUATE AI AUTOMATION ROI AND PRESENT FINDINGS TO MANAGEMENT [derived — not in proposal; proposal lists only 3 work activities for C01; a 4th is required for JPK 4-activity standard]

#### Knowledge Topics (KP files)

**KP-01: Office Workflow Analysis and AI Readiness Assessment**
Scope: Methods for mapping existing office workflows using flowcharts (Carta Alir); identifying repetitive, rule-based tasks suitable for automation; conducting an AI readiness gap analysis; quantifying current time costs to build the ROI baseline. Tools: Microsoft Visio, Lucidchart, process mapping templates.

**KP-02: AI Tool Landscape for Office Automation**
Scope: Overview of the major AI office automation platforms — Microsoft 365 Copilot, Google Workspace Gemini, n8n (open-source), Zapier, Microsoft Power Automate; RPA (Robotic Process Automation) concepts; tool selection criteria (cost, integration, data residency, PDPA compliance); pricing models and SME budget considerations.

**KP-03: AI Adoption Strategy, Change Management, and ROI Calculation**
Scope: Designing an AI implementation roadmap (Pelan Hala Tuju AI) with phased rollout; change management frameworks for employee resistance; training path design; ROI calculation methodology for AI projects (time saved × headcount cost × frequency); presenting the business case to management.

#### Practical Tasks (KK files)

**KK-01: Map an Office Workflow and Identify Three Automation Opportunities**
Scope: Trainees select a real or simulated Malaysian SME scenario; document the existing process using a flowchart; identify at least 3 repetitive tasks with automation potential; quantify time cost per task per month; produce a written automation opportunity report (Laporan Peluang Automasi).

**KK-02: Build a 90-Day AI Implementation Roadmap**
Scope: Trainees draft a phased AI roadmap for the same SME scenario: tool selection rationale, estimated subscription costs (in MYR), training requirements, risk register, and a simple ROI projection table. Present findings in a 5-minute management briefing format.

---

### C02 — CREATE AND MANAGE BUSINESS DOCUMENTS WITH AI

| Field | Value |
|-------|-------|
| **CU Code** | `ADMIN-AI-3:2026-C02` |
| **CU Title (English — uppercase)** | CREATE AND MANAGE BUSINESS DOCUMENTS WITH AI |
| **CU Title (Chinese)** | 以 AI 进行文件创建与管理 |
| **CU Title (Malay)** | Pengurusan & Penciptaan Dokumen dengan AI |
| **Hours** | 12 theory + 28 practical = 40 total |

#### Work Activities (NO. DAN PERNYATAAN AKTIVITI KERJA)

1. DRAFT BUSINESS CORRESPONDENCE IN MULTIPLE LANGUAGES USING AI WRITING TOOLS
2. CREATE REPORTS AND PRESENTATIONS WITH AI-ASSISTED DATA VISUALISATION
3. BUILD AN AI-POWERED DOCUMENT MANAGEMENT AND RETRIEVAL SYSTEM
4. APPLY PDPA 2010 COMPLIANCE STANDARDS TO DOCUMENT HANDLING PROCEDURES

#### Knowledge Topics (KP files)

**KP-01: AI Writing Tools and Business Correspondence Standards**
Scope: Prompt engineering for business writing using ChatGPT and Claude; generating formal BM surat rasmi, English business letters, memos, and quotations; Microsoft Word Copilot and Google Docs AI (Help me write); multilingual drafting (BM / English / Chinese); quality-checking AI-generated text for accuracy and tone.

**KP-02: AI-Assisted Report Creation, Presentation Design, and Data Visualisation**
Scope: Microsoft PowerPoint Copilot for slide generation; Google Slides AI features; Notion AI for knowledge base management; automated chart and infographic generation from data; structuring executive reports with AI-suggested outlines; verifying AI-generated statistics against source data.

**KP-03: Document Management Systems and PDPA 2010 Compliance**
Scope: Principles of a Document Management System (DMS / Sistem Pengurusan Dokumen); AI-powered search and retrieval; electronic signature tools (DocuSign, SignNow) and their legal standing under Malaysian Electronic Commerce Act 2006; PDPA 2010 document compliance requirements — retention periods, access control, secure disposal; naming conventions and version control.

#### Practical Tasks (KK files)

**KK-01: Draft a Set of Three Business Documents Using AI**
Scope: Trainees use AI tools to produce: (1) a formal BM surat rasmi to a government body, (2) an English quotation letter to a client, and (3) a complaint-response memo. Each draft must be reviewed, edited for accuracy, and submitted with a prompt log documenting the AI instructions used.

**KK-02: Set Up a Simple Document Management System for a Simulated SME**
Scope: Trainees design a folder structure and naming convention for a simulated SME, configure a cloud-based DMS (Google Drive or SharePoint), set access permissions, and create a PDPA-compliant data retention schedule. Deliverable: a one-page DMS Policy document (Polisi Pengurusan Dokumen).

---

### C03 — APPLY AI TOOLS FOR HR ADMINISTRATION

| Field | Value |
|-------|-------|
| **CU Code** | `ADMIN-AI-3:2026-C03` |
| **CU Title (English — uppercase)** | APPLY AI TOOLS FOR HR ADMINISTRATION |
| **CU Title (Chinese)** | 人力资源 AI 辅助工具应用 |
| **CU Title (Malay)** | Alatan AI HR untuk Pentadbiran |
| **Hours** | 12 theory + 28 practical = 40 total |

#### Work Activities (NO. DAN PERNYATAAN AKTIVITI KERJA)

1. USE AI TO PUBLISH JOB ADVERTISEMENTS AND SCREEN CANDIDATE APPLICATIONS
2. AUTOMATE EMPLOYEE ONBOARDING DOCUMENTATION USING AI TOOLS
3. IMPLEMENT AI-ASSISTED ATTENDANCE AND LEAVE TRACKING WITH AUTOMATED REPORTING
4. PROCESS STATUTORY PAYROLL CONTRIBUTIONS (EPF / SOCSO / EIS) USING HR MANAGEMENT SOFTWARE [derived — not in proposal; proposal lists 3 work activities; statutory payroll is a major knowledge item in the proposal that warrants a 4th work activity]

#### Knowledge Topics (KP files)

**KP-01: AI Recruitment Tools and Candidate Screening**
Scope: AI job advertisement generation using ChatGPT and LinkedIn AI; resume screening platforms (Workday AI, Hiredly AI); bias awareness in AI screening; structured interview question generation; Malaysian job portal landscape (Hiredly, Jobstreet, LinkedIn Malaysia).

**KP-02: Onboarding Automation and HR Platform Management**
Scope: Employee onboarding document workflows — offer letter, contract, EPF Form KWSP 3, SOCSO Form 2, IC copy, bank details; automating document generation with AI templates; Kakitangan.com and BambooHR features for Malaysian SMEs; leave entitlement rules under Employment Act 1955 (annual leave, sick leave, maternity leave).

**KP-03: Payroll Compliance — EPF, SOCSO, EIS, and Automated Reporting**
Scope: EPF (KWSP) contribution rates and monthly submission via i-Akaun Majikan; SOCSO (PERKESO) contribution schedule and EIS (SIP) deduction; generating payslips with AI-assisted templates; payroll data security and PDPA 2010 obligations; auto-generating monthly HR summary reports.

#### Practical Tasks (KK files)

**KK-01: Run an AI-Assisted Recruitment Cycle for a Simulated Job Opening**
Scope: Trainees write a job advertisement using AI, screen 5 sample resumes using an AI-scoring rubric, shortlist 2 candidates with justification, and generate an interview question set. Deliverable: complete recruitment folder (ad, screening log, shortlist memo, interview guide).

**KK-02: Process Simulated Monthly Payroll and Generate Statutory Contribution Reports**
Scope: Given a simulated employee list (5 employees, varied salary levels), trainees calculate EPF, SOCSO, and EIS contributions for one month, generate payslips using an AI-assisted template, and produce an e-Caruman-format contribution summary. Submission includes a payroll checklist and data-handling declaration aligned with PDPA 2010.

---

### C04 — MANAGE FINANCE ADMINISTRATION WITH AI

| Field | Value |
|-------|-------|
| **CU Code** | `ADMIN-AI-3:2026-C04` |
| **CU Title (English — uppercase)** | MANAGE FINANCE ADMINISTRATION WITH AI |
| **CU Title (Chinese)** | 财务行政 AI 辅助 |
| **CU Title (Malay)** | Pentadbiran Kewangan dengan AI |
| **Hours** | 12 theory + 28 practical = 40 total |

#### Work Activities (NO. DAN PERNYATAAN AKTIVITI KERJA)

1. AUTOMATE EXPENSE CATEGORISATION AND TRACKING USING AI AND ACCOUNTING SOFTWARE
2. GENERATE AI-ASSISTED FINANCIAL SUMMARY REPORTS FOR MANAGEMENT DECISION-MAKING
3. IMPLEMENT AI INVOICE PROCESSING AND VERIFICATION WORKFLOWS
4. APPLY SST AND LHDN E-INVOICING COMPLIANCE REQUIREMENTS TO FINANCIAL RECORDS

#### Knowledge Topics (KP files)

**KP-01: AI in Accounting Software — AutoCount, SQL Accounting, and Cloud Tools**
Scope: AutoCount Accounting and SQL Accounting as dominant Malaysian SME platforms; integration of AI add-ons (Dext / Hubdoc OCR for invoice recognition); cloud alternatives (Xero AI, QuickBooks Online); expense categorisation rules; bank reconciliation automation; data export formats for audit trail.

**KP-02: AI Financial Reporting and Business Intelligence for SMEs**
Scope: Generating monthly P&L and cash flow summaries using AI prompts (Excel Copilot, ChatGPT with CSV upload); financial KPI dashboards for SMEs (gross margin, accounts receivable days, burn rate); chart interpretation; data cleaning before AI analysis; confidentiality obligations for financial data under PDPA 2010.

**KP-03: SST Compliance, LHDN e-Invoicing, and SSM Administrative Obligations**
Scope: Sales and Service Tax (SST / Cukai Jualan dan Perkhidmatan) — who must register, taxable goods/services, SST-02 return filing; LHDN MyInvois e-Invoice system — mandatory rollout timeline, e-Invoice XML format, admin staff responsibilities; SSM annual return and business particulars filing; financial document retention requirements.

#### Practical Tasks (KK files)

**KK-01: Set Up an AI-Assisted Expense Tracking and Invoice Processing System**
Scope: Trainees use Dext (or equivalent OCR tool) to process 10 simulated invoices, categorise expenses in a spreadsheet, reconcile against a bank statement extract, and flag any SST-chargeable items. Deliverable: categorised expense report and a 3-item discrepancy resolution log.

**KK-02: Produce a Monthly Financial Summary Report Using AI Tools**
Scope: Given a simulated SME dataset, trainees use Excel Copilot or ChatGPT to generate a management-ready financial summary covering revenue, expenses, and net profit for one month. Report must include an LHDN e-Invoice compliance checklist and a note on any SST obligations identified.

---

### C05 — IMPLEMENT AI SCHEDULING AND PROJECT MANAGEMENT

| Field | Value |
|-------|-------|
| **CU Code** | `ADMIN-AI-3:2026-C05` |
| **CU Title (English — uppercase)** | IMPLEMENT AI SCHEDULING AND PROJECT MANAGEMENT |
| **CU Title (Chinese)** | AI 排程与项目管理 |
| **CU Title (Malay)** | Penjadualan AI & Pengurusan Projek |
| **Hours** | 12 theory + 28 practical = 40 total |

#### Work Activities (NO. DAN PERNYATAAN AKTIVITI KERJA)

1. CONFIGURE AN AI CALENDAR MANAGEMENT SYSTEM FOR MULTI-STAKEHOLDER SCHEDULING
2. AUTOMATE MEETING SCHEDULING WORKFLOWS WITH CRM AND EMAIL SYSTEM INTEGRATION
3. TRACK PROJECT TASKS, DEADLINES, AND RESOURCE ALLOCATION USING AI PROJECT TOOLS
4. CALCULATE MEETING COST ROI AND OPTIMISE ORGANISATIONAL TIME USAGE

#### Knowledge Topics (KP files)

**KP-01: AI Calendar and Scheduling Tools**
Scope: Reclaim.ai and Motion AI for intelligent schedule prioritisation; Calendly and Cal.com for automated appointment booking; Microsoft Outlook AI scheduling assistant and Google Calendar Smart Scheduling; multi-timezone scheduling for cross-border teams; integrating scheduling tools with email and CRM platforms.

**KP-02: AI Project Management — Tools, Frameworks, and Tracking**
Scope: Microsoft Project Copilot for Gantt chart generation; Notion AI for kanban and project wikis; Asana and Monday.com AI features; task dependency mapping; resource allocation tracking; deadline alert automation; differences between Gantt (sequential) and Kanban (flow) approaches and when to use each.

**KP-03: Meeting ROI, Time Blocking, and Deep Work Principles**
Scope: Meeting cost formula (attendees × average hourly rate × duration); ROI threshold for recurring meetings; time blocking (Pengehadan Masa) strategy for administrative staff; deep work scheduling principles; producing a meeting minutes template with AI auto-summary; action item tracking workflows post-meeting.

#### Practical Tasks (KK files)

**KK-01: Configure a Weekly AI-Managed Calendar for a Simulated Executive**
Scope: Trainees use Reclaim.ai (or equivalent) to set up a week's schedule for a simulated executive: recurring commitments, focus blocks, 3 external appointments auto-scheduled via Calendly link, and 1 multi-timezone team call. Deliverable: annotated calendar screenshot and a setup guide (Panduan Persediaan Sistem Penjadualan).

**KK-02: Build a Project Tracker for a 4-Week Office AI Rollout Project**
Scope: Using Notion AI or Microsoft Project, trainees create a 4-week project plan for rolling out one AI tool in a simulated SME: task list, owners, deadlines, Gantt chart, risk register (2 risks minimum), and a meeting cost ROI calculation for the weekly progress meeting. Deliverable: complete project file plus a 1-page project brief.

---

### C06 — PRODUCE BUSINESS INTELLIGENCE REPORTS WITH AI

| Field | Value |
|-------|-------|
| **CU Code** | `ADMIN-AI-3:2026-C06` |
| **CU Title (English — uppercase)** | PRODUCE BUSINESS INTELLIGENCE REPORTS WITH AI |
| **CU Title (Chinese)** | AI 商业智能与报告 |
| **CU Title (Malay)** | Perisikan Perniagaan & Pelaporan AI |
| **Hours** | 12 theory + 28 practical = 40 total |

#### Work Activities (NO. DAN PERNYATAAN AKTIVITI KERJA)

1. BUILD AN AUTOMATED DATA DASHBOARD FOR REAL-TIME BUSINESS PERFORMANCE MONITORING
2. GENERATE MONTHLY AND QUARTERLY BUSINESS PERFORMANCE REPORTS USING AI TOOLS
3. ANALYSE OPERATIONAL KPIs WITH AI AND PRODUCE IMPROVEMENT RECOMMENDATIONS
4. CLEAN AND VALIDATE DATA BEFORE AI ANALYSIS TO ENSURE REPORT ACCURACY

#### Knowledge Topics (KP files)

**KP-01: Business Intelligence Tools — Power BI and Google Looker Studio**
Scope: Microsoft Power BI AI features (Quick Insights, Copilot for Power BI, Q&A natural language queries); Google Looker Studio data connectors and report sharing; connecting BI tools to common Malaysian SME data sources (AutoCount export, Google Sheets, SQL Accounting); dashboard design principles (clarity, hierarchy, colour).

**KP-02: AI-Assisted Data Analysis — ChatGPT, Excel Copilot, and Python Basics**
Scope: Uploading CSV data to ChatGPT for analysis; Excel Copilot for chart generation and trend identification; Python Pandas and Matplotlib for trainees with coding exposure (no-code alternative provided for each step); data cleaning concepts — handling missing values, duplicates, inconsistent formats; verifying AI-generated figures against source data.

**KP-03: SME KPI Frameworks and Performance Reporting**
Scope: Core Malaysian SME KPIs — revenue growth rate, customer acquisition cost, employee productivity index, gross profit margin, accounts receivable days; writing an executive performance narrative with AI assistance; anomaly detection and early warning indicators; quarterly report structure for management presentation; visualising KPI trends for non-technical audiences.

#### Practical Tasks (KK files)

**KK-01: Build a Live Business Dashboard Using Power BI or Looker Studio**
Scope: Trainees connect a provided simulated SME dataset (monthly sales, expenses, headcount) to Power BI or Looker Studio and build a dashboard with at least 4 visual components: revenue trend line, expense breakdown pie chart, KPI scorecard, and one anomaly flag. Deliverable: shareable dashboard link or exported PDF with a 1-page interpretation memo.

**KK-02: Produce a Quarterly Business Performance Report Using AI**
Scope: Given 3 months of simulated business data, trainees use AI tools to generate a formal management report covering revenue vs. target, top 3 expense categories, KPI achievement summary, and 2 improvement recommendations. Report must include a data source declaration and an AI-usage disclosure note.

---

### C07 — IMPLEMENT AI GOVERNANCE AND DATA PRIVACY PRACTICES

| Field | Value |
|-------|-------|
| **CU Code** | `ADMIN-AI-3:2026-C07` |
| **CU Title (English — uppercase)** | IMPLEMENT AI GOVERNANCE AND DATA PRIVACY PRACTICES |
| **CU Title (Chinese)** | AI 治理与数据安全 |
| **CU Title (Malay)** | Tadbir Urus AI & Privasi Data |
| **Hours** | 12 theory + 28 practical = 40 total |

#### Work Activities (NO. DAN PERNYATAAN AKTIVITI KERJA)

1. DRAFT AN AI USAGE POLICY WITH ACCEPTABLE USE TERMS AND PROHIBITED BEHAVIOURS LIST
2. CONDUCT A DATA PRIVACY RISK ASSESSMENT FOR AI TOOLS INTRODUCED IN THE WORKPLACE
3. DELIVER RESPONSIBLE AI USAGE TRAINING TO BUILD AN INTERNAL AI ETHICS CULTURE
4. RESPOND TO A DATA BREACH INCIDENT FOLLOWING PDPA 2010 NOTIFICATION REQUIREMENTS

#### Knowledge Topics (KP files)

**KP-01: PDPA 2010 and Malaysian AI Regulatory Framework**
Scope: Full PDPA 2010 (Act 709) principles — consent, notice, disclosure, security, retention, access, data integrity; penalties as amended by Act A1727 (RM1,000,000 fine / 3-year imprisonment, in force 1 Apr 2025); MCMC AI Usage Guidelines; obligations of data processors vs. data controllers; rights of data subjects; sector-specific obligations (health, finance, HR data); comparison of data storage policies across ChatGPT, Microsoft Copilot, and Claude.

**KP-02: Responsible AI Principles and Workplace AI Ethics**
Scope: Core responsible AI pillars — fairness, transparency, accountability, privacy protection, human oversight; AI hallucination risks and verification protocols; bias in AI recruitment and document screening; intellectual property considerations when using AI-generated content; building an AI ethics culture — acceptable use policy (Polisi Penggunaan AI), staff communications, governance committee structure.

**KP-03: Cybersecurity Basics and Data Breach Incident Response**
Scope: Phishing attack identification and prevention; password management (passphrases, 2FA); VPN usage for remote work; data classification levels (public, internal, confidential, restricted); incident response procedure — detect, contain, assess, notify (PDPA breach notification to Personal Data Protection Commissioner "as soon as practicable" — see pdp.gov.my for operative guideline); post-incident review and corrective action documentation.

#### Practical Tasks (KK files)

**KK-01: Draft an AI Usage Policy for a Simulated Malaysian SME**
Scope: Trainees produce a 2-page AI Usage Policy (Polisi Penggunaan AI) document covering: approved AI tools list, prohibited uses (no uploading of client PII to public AI, no AI-generated content published without human review), data handling rules aligned with PDPA 2010, consequences of policy breach, and a staff acknowledgement signature block. Policy must reference PDPA 2010 and MCMC guidance.

**KK-02: Conduct a Data Privacy Risk Assessment and Simulate Breach Response**
Scope: Trainees complete a Privacy Impact Assessment (PIA) template for one AI tool (ChatGPT or equivalent) evaluating 5 risk dimensions (data sent to tool, data retention by provider, access controls, employee training, contractual safeguards). Then, given a simulated data breach scenario (employee accidentally uploads client list to a public AI tool), trainees draft the PDPA breach notification letter to the Personal Data Protection Commissioner (notification must be made "as soon as practicable" per the Act; refer to pdp.gov.my for the operative guideline).

---

## Content Coverage Summary

| CU | English Title | KP Count | KK Count | Theory (hrs) | Practical (hrs) |
|----|---------------|----------|----------|--------------|-----------------|
| C01 | PLAN AI AUTOMATION STRATEGY FOR OFFICE OPERATIONS | 3 | 2 | 12 | 28 |
| C02 | CREATE AND MANAGE BUSINESS DOCUMENTS WITH AI | 3 | 2 | 12 | 28 |
| C03 | APPLY AI TOOLS FOR HR ADMINISTRATION | 3 | 2 | 12 | 28 |
| C04 | MANAGE FINANCE ADMINISTRATION WITH AI | 3 | 2 | 12 | 28 |
| C05 | IMPLEMENT AI SCHEDULING AND PROJECT MANAGEMENT | 3 | 2 | 12 | 28 |
| C06 | PRODUCE BUSINESS INTELLIGENCE REPORTS WITH AI | 3 | 2 | 12 | 28 |
| C07 | IMPLEMENT AI GOVERNANCE AND DATA PRIVACY PRACTICES | 3 | 2 | 12 | 28 |
| **TOTAL** | | **21** | **14** | **84** | **196** |

---

## Notes for Writing Agents

1. **JPK Envelope required on every file.** Every `.md` produced in a CU folder must begin with the `<!-- JPK_ENVELOPE_v1 -->` block. Use the programme code `ADMIN-AI-3:2026` and the CU code for that folder.
2. **File naming convention.** Follow the existing project pattern: `KP-01.md`, `KP-02.md`, `KP-03.md`, `KK-01.md`, `KK-02.md`, plus `KA.md` (knowledge assessment), `PA.md` (performance assessment), `PM-teori.md`, `PM-amali.md`.
3. **NO. KOD pattern.** `ADMIN-AI-3:2026-C0n/KP(x/3)` for information sheets; `ADMIN-AI-3:2026-C0n/KK(x/2)` for work sheets.
4. **Paper colours.** KP = PUTIH (White) | KK = BIRU (Blue) | KA = MERAH JAMBU (Pink) | PA = BIRU MUDA (Light Blue) | PM = KUNING (Yellow).
5. **Language.** Body text in English; bilingual terminology table (English / BM / Chinese) at the end of each KP; work activity names in UPPERCASE English in the JPK envelope; Malay labels for envelope fields.
6. **Assessment alignment.** KA questions must test KP knowledge. PA tasks must mirror KK work activities. Do not add assessment items not covered by the KP/KK content.
7. **No fabricated figures.** Do not invent company names, registration numbers, statistics, or legal provisions beyond what is listed in this spec or can be verified from Malaysian legislation.
8. **`[derived]` items.** Four work activities for C01 and C03 (item 4 in each) were derived because the proposal provided only 3. Writing agents must note this in a comment at the top of those CU's KP/KK files.
