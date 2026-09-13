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
| NO. KOD | IT-020-5:2013-C05/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-project-management-execution

**TUJUAN:** Kertas rujukan untuk KP-03-project-management-execution.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Direct and manage project execution in accordance with the approved project management plan
2. Monitor and control project performance using Earned Value Management (EVM) and variance analysis
3. Apply integrated change control to evaluate, approve, and implement change requests
4. Manage project team performance through effective leadership, communication, and conflict resolution
5. Control quality, risk, and procurement throughout project execution
6. Produce and distribute project status reports to stakeholders

---

## 1.0 Introduction to Project Execution and Monitoring

Project execution is where the approved plan meets operational reality. The project manager's role during execution is not to perform the technical work personally but to *direct, coordinate, and control* the team and resources so that deliverables are produced on time, within budget, and to the required quality.

**Two concurrent process groups operate during execution:**

| Kumpulan Proses / Process Group | Fokus / Focus |
|--------------------------------|---------------|
| **Pelaksanaan / Executing** | Directing the team, managing vendors, producing deliverables, implementing approved changes |
| **Pemantauan dan Kawalan / Monitoring & Controlling** | Measuring performance against baseline, identifying variances, taking corrective action |

A Level 5 project manager must be proficient in both — failing to monitor while executing leads to problems discovered too late to correct.

---

## 2.0 Directing and Managing Project Work

### 2.1 Work Assignment and Team Direction

Effective work assignment requires the project manager to:

1. Issue work packages to team members based on the WBS and schedule
2. Confirm each team member understands the acceptance criteria and deadline for their tasks
3. Maintain a daily/weekly task tracker (Kanban board, Microsoft Project, or equivalent)
4. Remove obstacles (blocked resources, pending approvals, vendor delays) that prevent work from proceeding

**RACI Matrix for Project Execution:**

| Aktiviti / Activity | Project Manager | Network Engineer | System Administrator | Security Officer | Vendor | Sponsor |
|---------------------|-----------------|------------------|----------------------|------------------|--------|---------|
| Core switch configuration | A | R | I | C | C | I |
| Server OS deployment | A | C | R | C | I | I |
| Firewall policy implementation | A | C | C | R | C | I |
| UAT coordination | R/A | C | C | C | I | I |
| Change request approval | R | C | C | C | I | A |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

### 2.2 Information Distribution

The Communications Management Plan defines who receives what information. During execution, the project manager must:

- Send **weekly status reports** to all stakeholders (scope, schedule, cost, risk dashboard)
- Conduct **weekly team stand-up meetings** (15–30 minutes; focus on progress, blockers, next tasks)
- Conduct **monthly steering committee presentations** for sponsors (milestone status, major risks, decisions required)
- Maintain a **project issue log** visible to all team members

### 2.3 Issue Management

An *issue* is a current problem (not a future risk) that is affecting the project. Every issue must be:

1. Logged with a unique ID, date raised, description, and severity
2. Assigned an owner responsible for resolution
3. Given a target resolution date
4. Tracked until closed

| ID | Tarikh / Date | Keterangan Isu / Issue Description | Keterukan / Severity | Pemilik / Owner | Tarikh Selesai | Status |
|----|---------------|-------------------------------------|----------------------|-----------------|----------------|--------|
| I-001 | 2026-03-05 | Core switch firmware version incompatible with VLAN policy | High | Network Engineer | 2026-03-10 | Open |
| I-002 | 2026-03-12 | Server delivery delayed by 1 week (customs clearance) | High | Procurement Manager | 2026-03-19 | Open |
| I-003 | 2026-03-18 | Finance Dept UAT participation postponed — conflict with month-end | Medium | Project Manager | 2026-03-25 | Resolved |

---

## 3.0 Monitoring and Controlling Project Performance

### 3.1 Performance Measurement Using EVM

Earned Value Management (EVM) provides objective, quantitative performance data. The project manager must report EVM metrics at each status reporting cycle.

**Contoh EVM Status Report — Week 10 of 20:**

| Metrik | Formula | Nilai / Value | Tafsiran / Interpretation |
|--------|---------|---------------|---------------------------|
| Budget at Completion (BAC) | (given) | RM 358,400 | Total approved budget |
| Planned Value (PV) | % complete planned × BAC | RM 179,200 | 50% of work should be done by Week 10 |
| Earned Value (EV) | % complete actual × BAC | RM 161,280 | Only 45% of work actually completed |
| Actual Cost (AC) | Actual spend to date | RM 172,032 | Amount actually spent |
| Schedule Variance (SV) | EV − PV | −RM 17,920 | **Behind schedule** |
| Cost Variance (CV) | EV − AC | −RM 10,752 | **Over budget** |
| Schedule Performance Index (SPI) | EV / PV | 0.90 | Achieving 90% of planned work rate |
| Cost Performance Index (CPI) | EV / AC | 0.94 | Spending RM 1.06 for every RM 1.00 of work done |
| Estimate at Completion (EAC) | BAC / CPI | RM 381,277 | Projected final cost if CPI continues |
| Variance at Completion (VAC) | BAC − EAC | −RM 22,877 | Projected overspend |

**Tindakan Pembetulan / Corrective Action Required:**
- Investigate root cause of schedule delay (Week 8–9 cabling work behind due to contractor shortage)
- Engage secondary cabling contractor to recover 5 days of lost schedule
- Escalate projected cost overrun to sponsor; review contingency reserve utilisation

### 3.2 Schedule Variance Analysis and Recovery

When SPI < 0.95 (schedule deterioration > 5%), the project manager must:

1. Identify which activities are behind and by how many days
2. Determine whether delayed activities are on the critical path
3. Select a recovery strategy:
   - **Crashing:** Add resources to critical path activities (increases cost)
   - **Fast Tracking:** Overlap sequential activities (increases risk)
   - **Scope Reduction:** Remove lower-priority deliverables (requires sponsor approval)
4. Update the schedule baseline (requires formal change request if baseline revision)
5. Report the recovery plan to stakeholders

### 3.3 Change Control Process

Every computer system and network project will face change requests — from stakeholders wanting additional features, from technical discoveries during implementation, or from external regulatory changes.

**Integrated Change Control Process:**

```
1. Change Request Raised
   → Submitted by team member, stakeholder, or PM
   → Documented on Change Request Form (ID, date, description, requestor)

2. Impact Analysis
   → PM and technical lead assess impact on:
      - Scope (what additional work is required)
      - Schedule (how many days added/removed)
      - Cost (additional/reduced budget)
      - Risk (new risks introduced or existing risks changed)
      - Quality (impact on testing requirements)

3. Change Control Board (CCB) Review
   → CCB members: Project Sponsor, IT Manager, Project Manager, Lead Engineer
   → Decision: Approve / Reject / Defer / Approve with conditions

4. Implementation
   → Approved changes are incorporated into project plan
   → WBS, schedule, and budget baselines updated
   → RTM updated to reflect scope changes
   → All affected stakeholders notified

5. Verification
   → PM verifies approved change is implemented correctly
   → Close the change request record
```

**Change Request Log:**

| CR ID | Tarikh | Pemohon / Requestor | Keterangan / Description | Dampak Kos | Dampak Jadual | Keputusan CCB | Status |
|-------|--------|---------------------|--------------------------|------------|----------------|---------------|--------|
| CR-001 | 2026-03-10 | IT Manager | Add 10 additional WAPs for warehouse coverage | +RM 12,000 | +3 days | Approved | Implemented |
| CR-002 | 2026-03-22 | Finance Head | Include DLP software deployment in scope | +RM 18,500 | +7 days | Deferred to Phase 2 | Deferred |
| CR-003 | 2026-04-02 | Network Engineer | Upgrade firewall model due to throughput requirement | +RM 6,000 | 0 days | Approved | Pending |

---

## 4.0 Team Management and Leadership

### 4.1 Team Development Stages

Computer system and network project teams typically pass through Tuckman's stages of team development:

| Peringkat / Stage | Ciri-ciri / Characteristics | Peranan PM / PM Role |
|-------------------|-----------------------------|----------------------|
| **Forming** | Team members are polite, uncertain of roles | Clarify roles, set expectations, build rapport |
| **Storming** | Disagreements over approaches, roles, priorities | Mediate conflict, reinforce ground rules, provide direction |
| **Norming** | Team establishes working norms; collaboration improves | Reinforce positive behaviours; empower team |
| **Performing** | High productivity; team self-manages effectively | Delegate; focus on removing obstacles and strategic issues |
| **Adjourning** | Project ends; team disbands | Recognise contributions; capture lessons learned |

### 4.2 Conflict Management

Technical projects frequently experience conflict over design decisions, resource allocation, and schedule pressure. A Level 5 project manager applies five conflict resolution techniques, ordered by preference:

| Teknik / Technique | Kaedah / Method | Kesesuaian / Best Used When |
|--------------------|-----------------|-----------------------------|
| **Kolaborasi / Collaborate** | Both parties work together to find a mutually satisfying solution | Important issues; time available; both parties willing |
| **Kompromi / Compromise** | Each party gives up something to reach agreement | Moderate importance; time pressure |
| **Akomodasi / Accommodate** | One party concedes to preserve the relationship | Issue is more important to the other party; relationship matters more |
| **Paksa / Force** | PM uses authority to impose a solution | Emergency; safety issue; when other methods fail |
| **Elak / Withdraw** | Defer or avoid the conflict | Issue is minor; more information needed before deciding |

**Collaboration** is the preferred technique as it produces the most durable resolution.

### 4.3 Performance Management

The project manager monitors individual team member performance through:

- Regular one-on-one check-ins (weekly, 15 minutes)
- Review of task completion against schedule
- Quality of deliverables against acceptance criteria
- Peer feedback in team retrospectives

When performance issues are identified:
1. Discuss privately with the team member — understand root cause
2. Provide specific, actionable feedback
3. Agree on corrective actions and a review date
4. Escalate to functional manager if performance does not improve

---

## 5.0 Quality Control During Execution

### 5.1 Quality Assurance vs. Quality Control

| Aspek | Jaminan Kualiti / Quality Assurance (QA) | Kawalan Kualiti / Quality Control (QC) |
|-------|------------------------------------------|----------------------------------------|
| Fokus | Processes and methodology | Products and deliverables |
| Masa | Throughout the project | At completion of each deliverable |
| Tindakan | Process audits, checklist compliance | Inspection, testing, measurement |
| Siapa | PM, QA auditor | Technical team, independent tester |

### 5.2 Technical Quality Gates

For computer system and network projects, quality gates are established at key milestones:

| Pintu Kualiti / Quality Gate | Kriteria Lulus / Pass Criteria |
|------------------------------|-------------------------------|
| Design Review Gate | All design documents reviewed and signed off by security officer and IT manager |
| Pre-Implementation Gate | All hardware received and inspected; configurations peer-reviewed |
| Integration Test Gate | All components tested individually (unit test) before system integration |
| UAT Gate | User acceptance test cases ≥ 95% pass rate; all critical defects resolved |
| Security Gate | Penetration test completed; no Critical or High severity findings unresolved |
| Go-Live Gate | All above gates passed; rollback plan confirmed; cutover window approved by operations |

### 5.3 Configuration Management

All network device configurations, server build templates, and IP address plans must be under configuration management:

- Use a version control system (Git) or configuration management database (CMDB)
- Every configuration change must be documented with: who changed it, when, what was changed, and why
- Pre-change and post-change configurations must be captured
- Rollback procedures must be documented and tested before each configuration change

---

## 6.0 Risk Monitoring and Control

### 6.1 Risk Review Meetings

The Risk Register must be reviewed at every weekly team meeting. The project manager:

- Reviews all open risks for changes in probability or impact
- Checks whether triggers for any risk have occurred
- Verifies mitigation actions are being executed
- Identifies new risks as they emerge
- Closes risks that are no longer applicable

### 6.2 Risk Response Execution

When a risk event occurs (i.e., the risk materialises into an actual issue):

1. Activate the pre-planned risk response from the Risk Register
2. Log the risk as an issue in the Issue Log
3. Determine whether contingency reserve is required
4. Assess whether the risk event triggers additional risks
5. Report to stakeholders at next status report cycle

---

## 7.0 Procurement Management During Execution

### 7.1 Vendor Performance Monitoring

For computer system and network projects, procurement involves hardware vendors, software vendors, and implementation contractors. The project manager monitors vendor performance through:

| Aspek | Penilaian / Evaluation Method |
|-------|-------------------------------|
| Delivery timeliness | Compare actual delivery date vs. contracted date; track in Issue Log |
| Product quality | Incoming inspection; match purchase order specifications to actual goods received |
| Technical support responsiveness | SLA compliance; response time to support tickets |
| Documentation | Completeness of technical manuals, compliance certificates, warranty cards |

### 7.2 Contract Administration

- Keep all contracts, purchase orders, and delivery orders in the project document repository
- Record acceptance (or rejection with reasons) for every equipment delivery
- Process invoices only after formal acceptance of deliverables
- Document any contract disputes through formal written communication

---

## 8.0 Status Reporting

A well-structured project status report provides stakeholders with clear, factual information to make decisions. Standard format:

| Bahagian / Section | Kandungan / Content |
|--------------------|---------------------|
| **Ringkasan Eksekutif / Executive Summary** | 2–3 sentences: overall status (Green/Amber/Red), key achievement this period, key concern |
| **Status Pencapaian / Milestone Status** | Table of milestones: planned date, actual/forecast date, status (Completed/On Track/At Risk/Delayed) |
| **Prestasi EVM / EVM Performance** | PV, EV, AC, SV, CV, SPI, CPI, EAC — table and trend chart |
| **Risiko dan Isu Utama / Top Risks and Issues** | Top 5 risks and top 5 issues — status and owner |
| **Perubahan / Changes** | Change requests submitted, approved, rejected this period |
| **Aktiviti Akan Datang / Upcoming Activities** | Next 2-week look-ahead |
| **Keputusan Diperlukan / Decisions Required** | Explicit requests to stakeholders for decisions or approvals |

**Kod Isyarat Lampu / Traffic Light Status:**

| Warna / Colour | Maksud / Meaning |
|----------------|-----------------|
| Hijau / Green | On track — no significant issues |
| Amber / Amber | At risk — issues identified; corrective action in progress |
| Merah / Red | Off track — significant variance; sponsor intervention required |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer System Management — CoCU 5
- PMI. (2021). *PMBOK® Guide*, 7th Edition. Project Management Institute.
- AXELOS. (2017). *Managing Successful Projects with PRINCE2*, 6th Edition.
- Tuckman, B.W. (1965). Developmental sequence in small groups. *Psychological Bulletin*, 63(6), 384–399.
- ISO 21502:2020 — Project, Programme and Portfolio Management
- ITIL 4 Foundation — Service Value System and Change Management