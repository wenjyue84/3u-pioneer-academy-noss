# Core Abilities Inventory — Z-009-4:2015 (Level 4)

Source dir: `raw/adi-mpc-template-2026-09/core-abilities/_txt/` — all 50 files with the
`Z-009-4-2015__` prefix. This inventory covers those 50 .txt files (extracted from the 50 PDFs
under `raw/adi-mpc-template-2026-09/core-abilities/Core Abilities Level 1_2_3_4_5/Z-009-4-2015/`
via `pypdf` this session; none were scanned/no-text-layer — all 50 yielded extractable text).

File-type breakdown: 1 CAPC (Core Abilities Profile Chart, whole-Level-4 overview) + 8 per-module
CPC/ability-statement header pages (the short `04CORE~1`/`04 CPC`/`04COMP~1`/`04. CORE ABILITIES
PROFILE CHART` files — these repeat the same CA-title/ability-statement block also printed atop
every KP file for that module, not a distinct content page) + 33 Kertas Penerangan (KP,
Information Sheet, prefix `07`/`08`) files + 4 files at prefix `09` (labelled KP by their own
header block, not a separate "Kertas Kerja" template — see note in §2) + 1 file at prefix `11`
(`11.L4-02-03` and `11.L4-04-05` — same KP template) + 8 Soalan Penilaian (assessment) papers, one
per module.

**Structural difference from L1–3 (flagged, not carried over):** every Level-4 Soalan paper says
`SOALAN PENILAIAN PENGETAHUAN (SUBJEKTIF)` on its cover page — these are short-answer/essay papers
(2 questions, each split into lettered sub-parts a/b/c/d with per-part mark allocations, e.g.
"(6 Marks)"), NOT the 20-item MCQ format used throughout L1–3. Module 08's paper additionally
splits into "PART A: SHORT ANSWER QUESTIONS (4 questions, 20 marks)" + "PART B: ESSAY QUESTION (1
question, 20 marks)". Every paper ends with a model-answer section, labelled inconsistently across
files: `ANSWER`, `SCHEMA`, `SKEMA PEMARKAHAN`, or `SCHEME` (no single fixed term, confirmed by
direct read of the M01/M02/M08 papers — not assumed from L1–3's pattern).

## 1. Level 4 CAPC (Core Abilities Profile Chart)

From `Z-009-4-2015__MODULE 01 ORGANISATIONAL BEHAVIOUR__SUB MODULE 1-ORGANIZATION FRAMEWORK__04CORE~1.PDF.txt`
(job level FOUR, job area code Z-009-4:2015, sector/sub-sector/job-area all "ALL"): 8 Core
Abilities —
Z-009-4:2015-CA01 ORGANISATIONAL BEHAVIOUR AWARENESS,
CA02 HEALTH, SAFETY & ENVIRONMENT MONITORING,
CA03 RELATIONSHIP MANAGEMENT CAPABILITY,
CA04 ETIQUETTE PRACTICES,
CA05 STRATEGIC THINKING SKILL,
CA06 EFFECTIVE COMMUNICATION COLLABORATION,
CA07 CHANGE MANAGEMENT AWARENESS,
CA08 SYSTEM TECHNOLOGY APPLICATION.

Ability statements per CA (read verbatim from the header block repeated atop every module's KP
files — one module read per CA, cross-checked against every KP file in that module which all
repeat the identical block):

- **CA01 Organisational Behaviour Awareness** (7 statements): 01.01 Adhere to conceptual framework
  of the organization; 01.02 Enhance successful teamwork; 01.03 Demonstrate work delegation
  capability; 01.04 Ensure systematic documentation; 01.05 Encourage organization event
  coordination; 01.06 Comply with training requirement procedures; 01.07 Recognize staff vertical
  mobility potential.
- **CA02 Health, Safety and Environmental Monitoring** (3 statements): 02.01 Ensure health
  awareness program; 02.02 Ensure safety awareness program; 02.03 Ensure environment awareness
  program.
- **CA03 Relationship Management Capability** (6 statements): 03.01 Promote good networking; 03.02
  Enhance interpersonal conflict resolution; 03.03 Promote empathy; 03.04 Provide motivation;
  03.05 Demonstrate initiative behaviour; 03.06 Adhere to continuous effective learning.
- **CA04 Etiquette Practices** (5 statements): 04.01 Adhere to codes of ethical discipline; 04.02
  Comply cultural awareness; 04.03 Adhere to meticulous performance; 04.04 Adhere to result
  oriented practices; 04.05 Adhere protocol requirement.
- **CA05 Strategic Thinking Skill** (5 statements): 05.01 Advocate effective thinking; 05.02
  Comply with effective analysis; 05.03 Apply stress management techniques; 05.04 Apply budgetary
  control procedures; 05.05 Apply problem solving techniques.
- **CA06 Effective Communication Collaboration** (3 statements): 06.01 Apply effective
  communication; 06.02 Formulate constructive speech; 06.03 Adhere to effective presentation
  methodology. (Note: only 2 KP files exist for this CA — "Effective Communication Skill" and
  "Effective Presentation Methodology" — no distinct KP file was found for ability 06.02 in the
  source tree; it may be folded into one of the two existing KPs, not verified further.)
- **CA07 Change Management Awareness** (5 statements): 07.01 Adhere to change management
  objective; 07.02 Observe change management methodology; 07.03 Adhere to change management
  initiative; 07.04 Adhere to coaching & mentoring implementation; 07.05 Performance organisation
  branding.
- **CA08 System Technology Application** (4 statements): 08.01 Adopt appropriate software
  application; 08.02 Comply to system analysis application; 08.03 Update IT application; 08.04
  Adhere to IT rules & regulations.

## 2. Per-Module Detail (8 modules, CA01–CA08)

Each KP entry: title — verbatim numbered heading outline (top-level headings; sub-bullets omitted
for brevity except where structurally notable) — page count (from the `Drpd/of` running header,
cross-checked against the page-break count) — language (all English body text; header-table field
labels are bilingual EN/BM as in L1–3) — SOALAN/QUESTION count at the end of the KP where present.
File-prefix key observed in this Level: `04` = CPC/ability header (not separate content), `07`/`08`
= Kertas Penerangan, `09` = also a Kertas Penerangan by its own internal header (titled "KERTAS
PENERANGAN (INFORMATION SHEET)" — despite the `09` prefix suggesting Kertas Kerja in the CLAUDE.md
naming convention, the files themselves are Information Sheets), `11` = also Kertas Penerangan.
No distinct Kertas Kerja (KK) or Kertas Tugasan (KT) template was found among these 50 files — the
09/11-prefixed files are KP-format documents, not the assessment worksheets that prefix implies in
L1–3-style naming. This is a **file-type finding, not an assumption** — confirmed by opening each
09/11-prefixed file and reading its own header block.

### CA01 Organisational Behaviour Awareness (7 sub-modules, longest module by sub-module count)

- SM1 **"Organization Framework"** (Z-009-4:2015-M01/P(1/7), 15pg EN — header page 1 prints
  "Drpd/of: 14" but every subsequent page prints "15"; inconsistency noted, not resolved):
  `1. Definition`(1.1–1.4), `2. Types of Business Organizations`(2.1 Proprietorship, 2.2
  Partnership, mislabelled `3.3 Corporation`), `2. Company Size and Organizational Structure`
  (duplicate "2." numbering in source; 2.1 Size of the Organization and Information Requirements —
  i-Small/ii-Medium/iii-Large Organizations), `3. Mission and Vision Statements`(3.1–3.2), `4.
  Strategy execution as a process`(4.1 as a system, 4.2 as a step-by-step process — Steps 1–10),
  `5. How to Establish an Organization`(Steps 1–4). SOALAN: 4 Q (12 marks each).
- SM2 **"Workplace Teamwork"** (M01/P(2/7), 14pg EN): `1. Build an effective and cohesive team`
  (1.1–1.11), `2. Keys to Successful Teamwork`(2.1–2.10), `3. The secrets to successful teamwork:
  Trust and accountability`(3.1–3.12, plus "four things team members need"), `4. Description of
  the Multicultural Personality Questionnaire (MPQ)`(4.1 Cultural empathy, 4.2 Open-mindedness,
  4.3 Social Initiative, 4.4 Emotional stability, 4.5 Flexibility). SOALAN: 3 fill-in-the-blank Q.
- SM3 **"Work Delegation"** (M01/P(3/7), 19pg EN): `1. Defining Delegation`, `2. Learning To
  Delegate`, `3. Understanding Why Delegation Is Important`(3.1), `4. Knowing How To Delegate`
  (4.1 seven points i–vii, 4.2 Why people fail to delegate, 4.3 What should not be delegated), `5.
  Deciding What To Delegate`(5.1–5.2), `6. The Process Of Delegation`(6.1 Step 1 Choose What to
  Delegate…6.4 Step 4 Follow Up), `7. Monitoring System`(7.1 Contemporary Control System, 7.2
  Effective Reward Systems, 7.3 Effective Boundaries and Constraints), `8. Avoiding Pitfalls`.
  SOALAN: 3 Q (3 marks each).
- SM4 **"Systematic Documentation"** (M01/P(4/7), 15pg EN): `1. Overview`(1.1 Documentation
  Procedures, 1.2 Practice Proper and Systematic Filing, 1.3 Good and Systematic Filling Scheme,
  1.4 Filling System, 1.5 Filing Process), `2. Implement Proper Indexing`(2.1 Data Storage, 2.2
  Establish Proper Recording, 2.3 Electronic/2.4 Paper Based/2.5 Hybrid System, 2.6 Arrangement
  Scheme, 2.7 Filing Tips, 2.8 Adopt Proper Document Retrieval, 2.9 Hybrid or Electronic System,
  2.10 After Hours Retrieval), `3. Acquire And Sort Data`, `4. Periodically Review Document`(4.1
  Review Process, 4.2 Review Checklist), `5. Advantages`, `6. Update Document Accordingly`. SOALAN:
  6 Q with explicit mark allocations (Q1 15 marks, Q2 3 marks, Q3 10 marks, Q4 10 marks, Q5 12
  marks, Q6 10 marks) — answer marker present but the exact keyword wasn't captured verbatim in
  this pass; treat as unconfirmed wording, confirmed only that an answer section exists.
- SM5 **"Organization Event Coordination"** (M01/P(5/7), 19pg EN): `1. Overview`(1.1 Event
  Coordinator norms i–vi, 1.2 Encourage Organization Event Coordination — 11 tasks i–xi, 1.3
  Personal Requirements i–viii), `2. Organization Event Objective`(2.1–2.4, incl. the "5 Ws" plan
  i-WHO/ii-WHAT/iii-WHEN/iv-WHERE/v-WHY), `3. Event Rightful Team`(3.1 Event Team Management, 3.2
  Know Your Team — Maslow-style needs i-Physiological…vi-Self Actualization), `4. Group Event
  Coordination`(4.1 Develope Strength, 4.2 The Event Industry, 4.3 Event Planning, 4.4 Event
  Coordinator — 5 industry contexts i-Corporations…v-Independent Planners, 4.5 Right Event —
  Type A vs Type B events, event cooperation eligibility a–c). `5. Questions`: 10 Q, mixed mark
  values (4–10 marks each), with a printed answer key (SKEMA JAWAPAN-style, verified: answers for
  Q1–Q10 given, Q3/Q4/Q5/Q8 marked "in literature" meaning open-text answer not keyed).
- SM6 **"Training Compliance"** (M01/P(6/7), 9pg EN): `1. Overview`, `2. Training procedure
  requirements`(2.1 Training procedures for employee, 2.2 Trainer's identification, 2.3 Training
  assessment, 2.4 Training schedule), `3. Performance management`(3.1 Key Performance Indicators,
  3.2 Types of KPIs). SOALAN: 6 Q.
- SM7 **"Staff Vertical Mobility"** (M01/P(7/7), 5pg EN — shortest KP in the module): `1.
  Overview`, `2. Staff vertical mobility`, `3. Responsibility of staff vertical mobility`, `4.
  Selection criteria to facilitate staff vertical mobility`(4.1 Action plan, 4.2 Participate in
  promotional examinations, 4.3 Proficiency in-service training), `5. Recognition of staff
  vertical mobilisation`. SOALAN: 6 Q.
- **SOALAN PENILAIAN M01** (module-level, SUBJEKTIF, 2pp EN, KOD UNIT Z-009-4:2015 CA01): 2
  questions, Q1 has 4 lettered sub-parts (a–d, 6/2/6/6 marks) drawing on SM1 (establish
  organization), SM5 (KPI/staff mobility recognition), Q2 has 2 lettered sub-parts (a–b, 10/10
  marks) drawing on SM3 (delegation) and SM5 (event vendor criteria). Confirmed by full read:
  cross-CA drawing from multiple sub-modules within CA01, full worked-answer key follows headed
  `ANSWER`.

### CA02 Health, Safety and Environmental Monitoring (1 module-level, no sub-module folders)

- **"Health, Safety and Environmental Awareness"** (07-prefix, M02/P, 17pg EN): `1.0 Awareness
  Programme Objectives`, `2.0 Planning Awareness Programmes`, `3.0 Implement and Monitoring an
  Awareness Programmes`(3.1 Awareness Programme Activities), `4.0 Awareness Program Monitoring and
  Evaluation`(sub-numbered assessment criteria: gap analysis, priorities, solutions, social-needs
  assessment, logic/plausibility, comparison-with-research, preliminary-observation). SOALAN: 7 Q.
- **"Safety And Health Awareness Programme"** (09-prefix, longest KP-equivalent in this module at
  20pg EN): `1.0 Introduction`, `2.0 Developing A Safety And Health Programme`, `3.0 Factors
  Determining The Success Of A Safety And Health [Programme]`(3.1 Management Commitment and
  Employee Involvement, 3.2 Worksite Analysis, 3.3 Hazards Prevention and Control, 3.4 Safety and
  Health Training), `4.0 Safety Awareness Program In The Work Place`(4.1 OSHMS, 4.2 Safety and
  Health Audit, 4.3 Emergency Prevention/Preparedness/Response, 4.4 Promotions, 4.5 Tool Box Talk,
  4.6 Permit To Work System, 4.7 Lock-Out Tag-Out System, 4.8 Workplace Inspection, 4.9 Preventive
  Maintenance Programme, 4.10 Accident Investigation and Reporting Technique), `5.0 Health
  Awareness Program In The Work Place`(5.1 Chemical Control Programme, 5.2 Noise Control
  Management Programme, 5.3 Ergonomic Programme, 5.4 Confined Space Programme). SOALAN: answer
  marker "SCHEME" confirmed present at end; question count not independently re-verified beyond
  regex (10 numbered items detected) — treat as approximate.
- **"Environmental Awareness Program"** (11-prefix, 13pg EN): heading outline not fully captured
  by the automated heading scan in this pass (regex found no top-level numbered headings — the
  file uses a different heading style, e.g. bold run-in headers rather than "N. Title" lines); not
  independently re-read in full this session — flagged as an inventory gap rather than guessed.
  SOALAN: 6 Q detected by regex, not manually verified.
- **SOALAN PENILAIAN CA02** (module-level, SUBJEKTIF, 2pp EN): confirmed by full read — 2
  questions, each with 4 lettered sub-parts (a–d), covering HSE awareness programme benefits,
  management visibility/involvement, chemical exposure control methods, environmental problem
  types (Q1), and awareness-programme planning/health-programme content/programme evaluation (Q2).
  Answer key headed `SCHEMA`.

### CA03 Relationship Management Capability (3 sub-modules)

- SM1 **"Promote Good Networking"** (07-prefix, 19pg EN — note: this file's own printed TAJUK
  differs slightly by page, "Networking Methodology" also appears as a sub-heading): `1. Business
  Networking`(1.1–1.4), `2. Promote Good Networking`(2.1), `3. Networking Methodology`(3.1–3.2),
  `4. Networking Strategy Development`(4.1–4.2). Ends with 4 short-answer questions (regex found 0
  in the SOALAN-count pass because this file's question block sits before a literal "SOALAN"
  marker was detected — the 4 questions ["What is business networking?", "What is the most common
  subject item posed at networking function?", "Why does approachability so called a two way
  street?", "What do you understand by Common Point of Interest (CPI)?"] are visible directly in
  the extracted text).
- SM2 **"Personnel Developement"** [sic, source spelling] (07-prefix, 18pg EN): `1. Overview`(1.1
  Supplier Relationship Management (SRM) — note: SRM heading appears disconnected from the
  Personnel Development title, possible copy-paste artifact from another source document,
  consistent with the L1–3 inventory's observation of reused reference blocks), `2. Enhance
  Interpersonal Conflict Resolution`(2.2–2.5), `3. Promote Empathy`(3.1 What is Empathy, 3.2
  Components of Empathy), `4. Provide Motivation`(4.1 Three Motivation Theories, 4.2 Motivation
  Without Monetary Rewards), `5. Demonstrate Initiative Behavior`(5.1–5.2). Question block present
  but not captured cleanly by the automated scan; not independently re-verified.
- SM3 **"Adhere To Continuous Effective Learning"** (07-prefix, 22pg EN — longest KP in this
  module and one of the longest in L4): `1. Training Needs Analysis`(1.1–1.3), `2. Training Needs
  Analysis Process`(2.1–2.2), `3. Collecting And Analysing`(3.1–3.6, incl. KJ Analysis method),
  `4. Bridging The Analysis And Evaluation Through Learning`(4.1–4.12: Learning Objectives —
  Knowledge/Skill/Attitude objectives), `5. Training Outcome Evaluation`(5.1–5.7), `6. Managing
  The Evaluation Process`(6.1–6.12), `7. The Comparison Between The Learning Cycle And Training`
  (7.1–7.4), `8. Learning From The Training Outcome Evaluation`(8.1), `9. Terminology`. SOALAN: 6
  Q.
- **SOALAN PENILAIAN M3 INTERPERSONAL BEHAVIOUR** [sic — module-level paper's own title says
  "Interpersonal Behaviour" though CA03's title is "Relationship Management Capability", a
  source-labeling mismatch] (SUBJEKTIF, 2pp EN): 2 questions, Q1 has 4 lettered sub-parts (4/4/6/6
  marks), Q2 has 2 lettered sub-parts (10/10 marks). Answer marker: SCHEMA (confirmed by the
  earlier structural scan; content not independently re-read in full).

### CA04 Etiquette Practices (2 sub-modules)

- SM1 **"Codes of Ethical Discipline"** (07-prefix, 8pg EN): `1. Principles Of Ethical Discipline`
  (1.1 Decision making, 1.2 Good decisions are both ethical and effective), `2. Appearance`(2.1,
  2.2, 2.4 — 2.3 missing/skipped in source numbering), `3. Communication`(3.1–3.6), `4. Behaviour`
  (4.1), `5. Ethical Behaviour`(5.1, 5.2, 5.4, 5.5, 5.6 — 5.3 skipped in source numbering). SOALAN:
  4 Q.
  Also **"Cultural Awareness"** (09-prefix, 7pg EN, same SM1): `1. Behaviour Of Cultural
  Sensitivity`(1.1–1.5: Definition, Importance, Types of Skills, Implementation), `2. Social
  Isolation`(2.1 Definition, 2.2 Effects, 2.3–2.4), `3. Prejudice`(3.1 Risk Factors, 3.2 key
  considerations towards cultural awareness). SOALAN: 3 Q.
- SM2 **"Meticulous Performance"** [file's own TAJUK reads "Meticulous Work Performance" in body]
  (07-prefix, 6pg EN): `1. Meticulous Work Performance`(1.1 definition, 1.2 Planning, 1.3
  Monitoring, 1.4 Rewards), `2. Consequences Of Alternative Solutions To Meticulous Performance`,
  `3. Constructive Performance Feedback`(3.1–3.4), `4. Six Ways To Make Feedback Constructive`
  (4.1–4.2). SOALAN: 5 Q.
  Also **"Result Oriented Practices"** (09-prefix, 10pg EN, same SM2): `1. Result Oriented
  Practices`(1.1 Introduction, 1.2 Result Oriented Practices, 1.3 Advantages), `2. Demonstrate
  Established Work Certification Standard`(2.1–2.2), `3. Constructive Criticism And Suggestion
  Delivery`(3.1–3.3), `4. Work Performance Discussion Process`(4.1–4.2). SOALAN: 5 Q.
  Also **"Protocol Requirement"** (11-prefix, 7pg EN, same SM2): `1. Protocol Comprehension`
  (1.1–1.11), `2. Correspondence Language`(2.1–2.7), `3. Protocol Implementation`(3.1–3.8), `4.
  The Advantages Of Having A Protocol`(4.1–4.9). SOALAN: 3 Q.
- **SOALAN PENILAIAN M04** (SUBJEKTIF, 2pp EN): 2 questions, each with 2 lettered sub-parts
  (10 marks each part). Answer marker: SKEMA JAWAPAN (matches L1–3's most common term).

### CA05 Strategic Thinking Skill (5 sub-modules)

- SM1 **"Effective Thinking Skill"** (08-prefix, 11pg EN): `1. Introduction to Strategic Thinking`
  (1.1–1.2, 1.5 three basic principles, 1.6 "Six Thinking Hats", 1.7 Thinking Strategies and Its
  Application in Problem Solving — note 1.3/1.4 skipped in source numbering). SOALAN: answer
  marker SCHEMA confirmed; question count not independently re-verified (regex over-counted at 10
  due to matching non-question numbered lines).
- SM2 **"Effective Competency Analysis"** (08-prefix, 12pg EN): `1. Competency`(1.2–1.5,
  competency-based vs normal interviews), `2. Ideas`(2.2 Generating Idea, 2.3 Information, 2.4
  Language and Tone, 2.5 Ideas and Information Sources, 2.6 Analytical skills, 2.7 Effective
  Analysis — a 10-point checklist for information gathering, 2.8 Effective analysis strategies).
  SOALAN: not independently verified (regex noise from the 10-point checklist numbering).
- SM3 **"Stress Management Technique"** (08-prefix, 9pg EN): `1. Causes Lead To Stress`, `2.
  Effects of Stress on Your Health`, `3. Stress Identification`, `4. Stress Reduction Techniques`.
  SOALAN: 3 Q.
- SM4 **"Budgetary Allocation Procedures"** [file's own TAJUK differs from folder name "Apply
  Budgetary Control Procedures"] (08-prefix, 8pg EN): `1. Introduction To Budgetary Allocation
  Procedures`, `2. Budget Objectives`, `3. Budget Strategies`, `4. Budget Allocation`, `5. Budget
  Allocation Process`. SOALAN: 3 Q.
- SM5 **"Problem Solving Techniques"** (08-prefix, 8pg EN): `1. Definition Of Fact and Opinion`,
  `2. Relationship Principle`, `3. Problem Solving`, `4. Decision Making`(4.2–4.4), `5. Rational
  Strategies`(5.2). SOALAN: 4 Q.
- **SOALAN PENILAIAN M05 LEVEL 4** (SUBJEKTIF, 2pp EN): draws across multiple sub-modules
  (competency/analytical skill definitions, stress causes/reduction, problem-solving model),
  multiple lettered sub-parts with mark values from 2–10 marks; answer marker ANSWER SCHEME
  confirmed present. Full question-by-question breakdown not re-verified beyond the structural
  scan.

### CA06 Effective Communication Collaboration (2 sub-modules only, for 3 ability statements — see §1 note)

- "MODULE 1 - EFFECTIVE COMMUNICATION" folder → **"Effective Communication Skill"** (08-prefix,
  M06/P(1/2), 8pg EN): `1. Introduction To Effective Communication`(1.1–1.3), `2. Benefit Of
  Effective Communication In Workplace`(2.1 Reduces conflict + others), `3. Barriers To Effective
  Communication`, `4. Skill for Effective Communication`(4.1). SOALAN: 4 Q.
- "MODULE 2 - EFFECTIVE PRESENTATION" folder → **"Effective Presentation Methodology"** (07-prefix,
  8pg EN): `1. Presentation Structure, Knowledge and Audience`(1.2–1.3), `2. Information Sources`
  (2.1, 2.3 tips), `3. Graphic Standard Rules`(3.1–3.5). SOALAN: 5 Q.
- **SOALAN PENILAIAN M06 LEVEL 4** (SUBJEKTIF, 2pp EN): "Soalan 1 (20 Marks)" with multiple
  lettered sub-parts (5 marks each) plus further questions on graphic information / presentation
  method / communicator traits (10, 4, 3, 10 marks parts seen in the structural scan). Answer
  marker: ANSWER SCHEME.

### CA07 Change Management Awareness (3 sub-modules)

- SM1 **"Change Management Objective"** (07-prefix, 14pg EN): `1. The Nature And Complexity Of
  Work`(1.1–1.7), `2. Project Resources`(2.1–2.10: known-knowns/known-unknowns/unknown-unknowns),
  `3. Work Schedule`(3.1 Milestone, 3.2 Change Management Activities, 3.3 Change Management
  Process, 3.4 Deadline). SOALAN: 7 Q.
  Also **"Change Management Methodology"** (09-prefix, 17pg EN, same SM1 — longest KP-equivalent
  in this module): `1. Appropriate Change Management Methodology`(1.1–1.11: ADKAR, Kotter's
  8-Step Change Model, Lewin's 3-Stage Model, The Change Curve, Prosci's Methodology), `2. Staff
  Performance Guidelines And Procedures`(2.1–2.8), `3. Possible Risk Factors`(3.1–3.3, 3.5), `4.
  Risk Management`(4.2–4.4). SOALAN: 5 Q.
- SM2 **"Change Management Initiative"** (07-prefix, 8pg EN): `1. Positive Attitude Philosophy`
  (1.1–1.5: PMA), `2. Initiative Management Behaviour`(2.1), `3. Mitigation And Adaptation
  Procedures`(3.1–3.2), `4. Identification Of Instruction Problems Concerning Work Completion`
  (4.1–4.3). SOALAN: 4 Q, answer marker SCHEME confirmed.
  Also **"Coaching And Mentoring Implementation"** (09-prefix, 8pg EN, same SM2): `1. Counseling,
  Coaching And Mentoring During Change Management`(1.1–1.4: definitions, differences between
  coaching and mentoring), `2. Opportunity In Change Management`(2.1–2.2). SOALAN: 6 Q.
- SM3 **"Organisation Branding"** [KP's own TAJUK reads "Organisation Branding" for folder
  "Organisation Branding Enhancement"] (07-prefix, 9pg EN): `1. Organisation`(1.1–1.2, 1.4–1.5),
  `2. Branding`(2.1–2.3, 2.5–2.10), `3. Culture`(3.1–3.6), `4. Organisational Culture
  Multiplicities`(4.1–4.4), `5. Ideas of Branding`(5.1–5.10). SOALAN: 5 Q.
- **SOALAN PENILAIAN M07** (SUBJEKTIF, 2pp EN): 2 questions, each with 2 lettered sub-parts (10
  marks each). Answer marker: SKEMA JAWAPAN.

### CA08 System Technology Application (2 sub-modules)

- SM1 **"IT System Utilization"** — 3 KP-equivalent files:
  - **"Software Application Adoption"** (07-prefix, 8pg EN): `1. What is IT applications?`, `2.
    What are the 2 basic principle components of a computer?`(2.1 Hardware, 2.2 Software), `3.
    What is software applications?`(5.1–5.2 — note mismatched numbering in source, the "3."
    heading is followed by "5.1/5.2" sub-numbers, then `4. IT problems`(4.1–4.2), `5. What is
    document printing?`(5.1–5.4). SOALAN: 9 Q (source numbering irregularity noted, not
    corrected).
  - **"System Analysis Compliance"** (09-prefix, 11pg EN): `1. Backup and Restore`(1.2–1.3), `2.
    Authentication`(2.1–2.4), `3. Biometrics`(3.1), `4. Encryption`(4.1–4.2), `5. How to Identify
    Which Hardware Component is Failing in Your Computer`(5.1–5.7), `6. Managing Digital
    Documents`(6.1–6.8, with a numbering repeat of 6.7/6.8 in source). SOALAN: 2 Q (shortest
    detected question count in L4 corpus — not independently re-verified, may be an artifact of
    the extraction).
  - **"IT Application Update"** (11-prefix, 10pg EN): `1. What is System Software?`(1.1–1.5:
    operating systems, Open Source), `2. What is search engines?`(2.2–2.7), `3. Internet
    Facilities`(3.1–3.4). SOALAN: 8 Q, answer marker SCHEMA confirmed.
- SM2 **"IT Regulations Adherence"** — **"IT Rules & Regulations Adherence"** (07-prefix, 15pg EN,
  longest KP in this module): `1. Privacy & Security`(1.1–1.5), `2. Threats In Networks`(2.1–2.2),
  `3. Network Security Controls`. SOALAN: 3 Q.
- **Soalan penilaian L4 CA08** (SUBJEKTIF, split format unique among the 8 module papers,
  confirmed by full read, 2pp EN): "PART A: SHORT ANSWER QUESTIONS (4 QUESTIONS : 20 MARKS)" — Q1
  IT application classes (2), Q2 software application types (8), Q3 operating systems (5), Q4
  network security problem reasons (5) — plus "PART B: ESSAY QUESTION (1 QUESTION : 20 MARKS)" —
  a scenario question on setting up a new IT Section (hardware/software selection, networking/
  security considerations). Answer key headed `SKEMA PEMARKAHAN`.

## 3. Common KP Header Block (verbatim, from `Z-009-4-2015__MODULE 01 ORGANISATIONAL BEHAVIOUR__SUB MODULE 1-ORGANIZATION FRAMEWORK__08L4-C~1.PDF.txt`)

```
KOD DAN NAMA PROGRAM / PROGRAM'S CODE AND NAME: Z-009-4:2015 CORE ABILITIES
TAHAP / LEVEL: 4 (FOUR)
NO. DAN TAJUK KEBOLEHAN TERAS / CORE ABILITY NO. AND TITLE: CA01 ORGANISATIONAL BEHAVIOUR AWARENESS
NO. DAN PENYATAAN KEBOLEHAN / ABILITY NO. AND STATEMENT: 01.01 ADHERE TO CONCEPTUAL FRAMEWORK OF THE ORGANIZATION [+01.02 … 01.07]
NO. KOD / CODE NO.: Z-009-4:2015 M01/P(1/7)
Muka Surat / Page: 1   Drpd / of: 14 (later pages print 15 — inconsistent)
TAJUK/TITLE: ORGANIZATION FRAMEWORK
TUJUAN/PURPOSE: [1-paragraph objective statement naming the CA and what a competent person shall be able to do]
JABATAN PEMBANGUNAN KEMAHIRAN
KEMENTERIAN SUMBER MANUSIA
ARAS 7 & 8 BLOK D4, KOMPLEK D
PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN
62530 PUTRAJAYA
KERTAS PENERANGAN (INFORMATION SHEET)
```
Same running-header format as L1–3: `NO. KOD/CODE NO.` + `Mukasurat/Page` + `Drpd/of` repeat on
every page. Body ends with `SOALAN/QUESTION` (2–10 short-answer or fill-in-blank prompts,
sometimes with explicit marks, sometimes without) then `RUJUKAN/REFERENCE(S)` (numbered URL/book
list — mostly generic web sources, e.g. successfactors.com, entrepreneur.com, forbes.com,
snagajob.com — matching L1–3's pattern of citing general management/HR websites rather than
Malaysian-specific sources except where OSHA/FMA/EQA law is quoted directly, as in CA02).

## 4. Common Soalan (Question Paper) Header (verbatim, from `Z-009-4-2015__MODULE 01 ORGANISATIONAL BEHAVIOUR__SOALAN PENILAIAN M01 ORGANISATIONAL BEHAVIOUR Vol. 1.pdf.txt`)

```
KOD DAN NAMA PUSAT BERTAULIAH

SOALAN PENILAIAN PENGETAHUAN (SUBJEKTIF)
KOD UNIT CORE ABILITY: [blank field on the template]
NAMA UNIT ABILITY: [blank field on the template]
NAMA CALON: [blank]
NO.KAD PENGENALAN: [blank]
MASA: [blank]
TARIKH: [blank]
MARKAH: [blank]

Arahan kepada calon:
1. Tulis nama dan nombor kad pengenalan calon pada ruangan yang disediakan;
2. Calon tidak dibenarkan membuka kertas soalan sehingga dibenarkan;
3. Calon hendaklah menjawab semua soalan;
4. Calon dilarang membawa nota atau sebarang bahan rujukan kecuali yang dibenarkan.
5. Dilarang meniru semasa penilian; dan
6. Dilarang membawa keluar kertas soalan dari bilik peperiksaan

KERTAS PENILAIAN INI MENGANDUNGI ...02.... MUKA SURAT BERCETAK
  JABATAN PEMBANGUNAN KEMAHIRAN
  KEMENTERIAN SUMBER MANUSIA
  ARAS 7 and 8 BLOK D4, KOMPLEKS D
  PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN
  62530 PUTRAJAYA
```
Unlike L1–3 (20-item MCQ, header/instructions identical), every L4 Soalan paper is headed
`SOALAN PENILAIAN PENGETAHUAN (SUBJEKTIF)` — a structured short-answer/essay paper, always printed
as "...02.... MUKA SURAT BERCETAK" (2 printed pages) except CA08's paper which prints "...2...."
(same value, different padding) and internally splits into PART A/PART B. The `KOD UNIT CORE
ABILITY` and `NAMA UNIT ABILITY` fields are blank on the template itself (filled by hand, unlike
L1–3 where the KOD UNIT was pre-printed) — this is a further template difference from L1–3, worth
flagging for anyone drafting new L4-style WIM papers. Each paper is followed by a model-answer
section headed inconsistently: `ANSWER` (M01), `SCHEMA` (M02, M07 partial), `SKEMA JAWAPAN` (M04,
M07), `ANSWER SCHEME` (M05, M06), `SKEMA PEMARKAHAN` (M08) — five distinct terms across 8 papers,
more variation than the 4 terms noted in the L1–3 inventory.

## Files referenced

All 50 files under
`C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\raw\adi-mpc-template-2026-09\core-abilities\_txt\`
with the `Z-009-4-2015__` prefix — 1 whole-level CAPC chart, 8 per-module ability-statement header
pages, 33 KP files, 8 Soalan Penilaian papers (all SUBJEKTIF format, unlike L1–3's MCQ format).

**Known gaps in this pass** (flagged rather than guessed): the CA02 "Environmental Awareness
Program" KP's heading outline was not captured by the automated heading scan and was not
independently re-read in full; several SOALAN question counts for CA02/CA03/CA05/CA06 module-level
papers and a handful of sub-module KP SOALAN blocks were derived from a regex-based structural
scan rather than a full manual read, and are marked "not independently re-verified" above where
that applies. A follow-up pass reading those specific files in full would close these gaps.
