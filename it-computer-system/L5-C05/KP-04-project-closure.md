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
| NO. KOD | IT-020-5:2013-C05/KP(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-project-closure

**TUJUAN:** Kertas rujukan untuk KP-04-project-closure.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Execute a structured project closure process for computer system and network projects
2. Conduct formal client handover including system acceptance sign-off and warranty transfer
3. Prepare a comprehensive lessons learned register and project closure report
4. Perform administrative closure including document archiving and resource release
5. Transition the delivered system into operational support (BAU — Business As Usual)

---

## 1.0 Introduction to Project Closure

Project closure is the formal process of concluding all project activities and transitioning deliverables to the client or operational team. It is one of the most frequently underestimated phases in IT projects — teams are eager to move on, and closure activities are deferred or skipped. This leads to disputes over acceptance, unresolved defects inherited by operations, and lost knowledge that prevents future projects from learning from past experience.

**PRINCE2** defines closure as a mandatory stage, not optional. **PMBOK®** similarly treats closure as a distinct process group. A Level 5 project manager must ensure closure is completed properly regardless of schedule pressure.

**Dua Jenis Penutupan / Two Types of Closure:**

| Jenis / Type | Keadaan / Condition | Tindakan / Action |
|--------------|---------------------|-------------------|
| **Penutupan Normal / Normal Closure** | All deliverables accepted; project objectives met | Full closure process as described in this sheet |
| **Penutupan Awal / Early Closure** | Project cancelled or terminated before completion | Document reasons; close contracts; archive partial work; preserve lessons learned |

---

## 2.0 Closure Prerequisites — Final Acceptance Verification

Before initiating formal closure, the project manager must verify that all conditions for acceptance are met:

### 2.1 Final Acceptance Checklist

| Bil. | Kriteria Penerimaan / Acceptance Criterion | Status |
|------|--------------------------------------------|--------|
| 1 | All WBS deliverables completed and documented | [ ] Lengkap / Complete |
| 2 | All User Acceptance Test (UAT) cases passed (≥ 95% pass rate) | [ ] Lengkap / Complete |
| 3 | All Critical and High severity defects resolved and retested | [ ] Lengkap / Complete |
| 4 | Security penetration test completed — no unresolved Critical/High findings | [ ] Lengkap / Complete |
| 5 | All network devices configured and operational within SLA | [ ] Lengkap / Complete |
| 6 | All servers deployed, patched to current security baseline | [ ] Lengkap / Complete |
| 7 | IP address plan, VLAN register, and network diagram (as-built) finalised | [ ] Lengkap / Complete |
| 8 | All licences registered and licence certificates transferred to client | [ ] Lengkap / Complete |
| 9 | Warranty cards and vendor support contracts transferred to IT operations | [ ] Lengkap / Complete |
| 10 | All administrator and end-user training sessions completed | [ ] Lengkap / Complete |
| 11 | Operations team confirmed readiness to support the system (BAU handover) | [ ] Lengkap / Complete |
| 12 | All project invoices settled; final payment processed | [ ] Lengkap / Complete |

### 2.2 Outstanding Items Register

If any items remain incomplete at the point of closure initiation, they are logged as **outstanding items** and a resolution date is agreed with the client. Minor outstanding items do not prevent closure provided:
- The client formally acknowledges and accepts the outstanding items in writing
- A legally binding resolution schedule is agreed
- A financial retention or bond is held until outstanding items are resolved

---

## 3.0 Client Handover Process

### 3.1 System Acceptance Sign-Off

The formal acceptance of the project deliverables is executed through a structured sign-off process:

**Langkah Penerimaan Klien / Client Acceptance Steps:**

1. **Demonstration:** Project manager and lead engineer conduct a live demonstration of all system functions to the client and operations team
2. **Walkthrough:** Operations team performs hands-on walkthrough of all key management interfaces (network management system, server console, backup system)
3. **Acceptance Test Witness:** Client representative witnesses execution of final acceptance test cases
4. **Sign-Off:** Client authorised representative signs the **Project Acceptance Certificate**

**Sijil Penerimaan Projek / Project Acceptance Certificate:**

| Medan / Field | Butiran / Details |
|---------------|-------------------|
| Nama Projek / Project Name | |
| No. Projek / Project Number | |
| Tarikh Siap / Completion Date | |
| Pengurus Projek / Project Manager | |
| Wakil Klien / Client Representative | |
| **Kenyataan Penerimaan / Acceptance Statement** | *"I hereby confirm that all project deliverables have been received, tested, and accepted in accordance with the agreed acceptance criteria."* |
| Tandatangan Klien / Client Signature | |
| Tarikh / Date | |
| Tandatangan PM / PM Signature | |
| Tarikh / Date | |

### 3.2 As-Built Documentation Handover

Comprehensive as-built documentation must be transferred to the client at handover. This is the definitive record of the system as actually built — not the design documents which may have changed during implementation.

| Dokumen / Document | Kandungan / Content |
|--------------------|---------------------|
| **Pelan Rangkaian Terkini / As-Built Network Diagram** | Physical and logical topology; all device locations, IP addresses, VLAN assignments, port connections |
| **Inventori Peralatan / Equipment Inventory** | Serial numbers, model numbers, firmware/software versions, warranty expiry dates, vendor contact |
| **Pelan Pengalamatan IP / IP Address Plan** | Full IP address allocation table; subnet definitions; DHCP ranges; static assignments |
| **Konfigurasi Peranti / Device Configurations** | Exported configuration files for all network devices and servers (stored in encrypted archive) |
| **Prosedur Operasi Standard / Standard Operating Procedures (SOPs)** | Common administrative tasks: adding a user, configuring a new VLAN, replacing a failed drive |
| **Pelan Kesinambungan / Business Continuity Plan** | Backup schedules; recovery procedures; emergency contact list; escalation path |
| **Rekod Ujian / Test Records** | All UAT test cases, results, and defect resolution records |
| **Rekod Latihan / Training Records** | Attendance list and training materials for administrator and end-user training |

### 3.3 Warranty and Support Transition

The project manager must formally transfer all warranty and support responsibilities:

- Provide the IT operations team with the vendor support portal credentials, contract numbers, and SLA terms
- Introduce the operations team to vendor account managers (introductory email)
- Clarify the warranty claim process for each piece of equipment
- Define the escalation path for issues beyond the operations team's capability (vendor > project manager > system integrator)
- Establish a **post-implementation support window** (typically 30–60 days) during which the project team remains on call to assist operations

---

## 4.0 Lessons Learned Process

### 4.1 Purpose of Lessons Learned

Lessons learned capture the knowledge gained during the project — both positive practices to repeat and negative experiences to avoid. They are the primary mechanism by which an organisation improves its project management maturity over time.

**PRINCE2** calls this document the **End Project Report + Lessons Log**. **PMBOK®** terms it the **Lessons Learned Register**. Both are maintained throughout the project and formally compiled at closure.

### 4.2 Lessons Learned Workshop

A facilitated lessons learned workshop should be conducted with the full project team before the team is disbanded. The workshop typically takes 2–4 hours and covers:

| Soalan Panduan / Guiding Question | Contoh Dapatan / Example Finding |
|-----------------------------------|----------------------------------|
| What went well and should be repeated? | "Early involvement of the security officer in design review prevented three firewall redesigns" |
| What went poorly and should be avoided? | "Hardware procurement was initiated too late — delivery delays put the schedule at risk" |
| What would we do differently if we started again? | "We would conduct a VLAN compatibility test on the legacy switches before committing to the architecture" |
| What should be communicated to other project teams? | "The cabling contractor requires 3 weeks of advance notice — build this into future project schedules" |
| What process improvements should be recommended? | "Introduce a standard equipment inspection form — current process is inconsistent across projects" |

### 4.3 Lessons Learned Register Format

| ID | Kategori / Category | Keterangan / Description | Kesan / Impact | Cadangan / Recommendation | Pemilik / Owner |
|----|---------------------|--------------------------|----------------|---------------------------|-----------------|
| LL-001 | Perancangan / Planning | Procurement timeline underestimated by 2 weeks for imported equipment | Schedule delay; customer dissatisfaction | Add 2-week buffer for all imported hardware in future project schedules | PM |
| LL-002 | Teknikal / Technical | Firmware version conflict between legacy access switches and new core switch not identified until integration test | 5-day rework delay | Add firmware compatibility check to pre-project technical assessment checklist | Network Engineer |
| LL-003 | Komunikasi / Communication | Finance Department was not informed of maintenance window schedule — caused complaints during cutover | Stakeholder dissatisfaction | Include all affected departments in communication plan; send maintenance notice 2 weeks in advance | PM |
| LL-004 | Kualiti / Quality | UAT test plan prepared only 3 days before UAT — insufficient time for client review | Several UAT cases were unclear; required rework | Prepare UAT test plan at least 2 weeks before UAT commencement | QA Lead |
| LL-005 | Positif / Positive | Daily 15-minute team stand-up meetings improved issue resolution speed significantly | Issues resolved 40% faster than previous project | Adopt daily stand-ups as standard practice on all future projects | PM |

---

## 5.0 Project Closure Report

### 5.1 Structure of the Project Closure Report

The Project Closure Report is the formal summary document that records the project's outcome against its original objectives. It is submitted to the project sponsor for approval and archived in the organisation's project repository.

**Kandungan Laporan Penutupan / Project Closure Report Contents:**

| Bahagian / Section | Kandungan / Content |
|--------------------|---------------------|
| **1. Maklumat Projek / Project Information** | Project name, code, manager, sponsor, start date, actual end date |
| **2. Ringkasan Eksekutif / Executive Summary** | 1-page narrative: objectives achieved, overall assessment (success/partial/failure with reasons) |
| **3. Perbandingan Skop / Scope Comparison** | Original scope vs. delivered scope; approved changes; items deferred |
| **4. Perbandingan Jadual / Schedule Comparison** | Planned vs. actual milestone dates; total schedule variance; reasons for variance |
| **5. Perbandingan Kos / Cost Comparison** | Budget vs. actual cost breakdown; variance analysis; contingency utilised |
| **6. Prestasi Kualiti / Quality Performance** | UAT pass rate; defects found and resolved; quality gates passed |
| **7. Pengurusan Risiko / Risk Management Summary** | Risks that materialised; effectiveness of mitigation strategies |
| **8. Pelajaran Dipetik / Lessons Learned Summary** | Top 5 lessons; recommendations for future projects |
| **9. Penyerahan / Deliverables** | Checklist of all deliverables and acceptance status |
| **10. Tindakan Tertunggak / Outstanding Actions** | Any remaining items with resolution schedule and ownership |
| **11. Pengesahan / Approvals** | Signatures: Project Manager, Sponsor, Client Representative |

### 5.2 Budget vs. Actual Summary

| Kategori / Category | Belanjawan (RM) / Budget | Sebenar (RM) / Actual | Varians (RM) / Variance | % Varians |
|---------------------|--------------------------|----------------------|-------------------------|-----------|
| Hardware | 203,000 | 215,400 | +12,400 | +6.1% |
| Software licences | 45,000 | 45,000 | 0 | 0% |
| Cabling and civil works | 27,000 | 29,800 | +2,800 | +10.4% |
| Labour / Professional services | 61,000 | 63,500 | +2,500 | +4.1% |
| Project management | 25,000 | 25,000 | 0 | 0% |
| Training | 6,000 | 5,800 | −200 | −3.3% |
| **Subtotal** | **367,000** | **384,500** | **+17,500** | **+4.8%** |
| Contingency reserve (utilised) | 38,400 | 22,000 | −16,400 | — |
| **JUMLAH / TOTAL** | **405,400** | **406,500** | **+1,100** | **+0.3%** |

---

## 6.0 Administrative Closure

### 6.1 Document Archiving

All project documents must be archived in an organised, accessible manner for future reference, audit, and dispute resolution. Minimum retention period for government-related IT projects in Malaysia: **7 years**.

**Senarai Dokumen Arkib / Archive Document Checklist:**

- Project charter and stakeholder register
- Project management plan (all subsidiary plans)
- Requirements Traceability Matrix (RTM)
- Design documents and architecture diagrams
- As-built documentation set
- Procurement records (contracts, purchase orders, delivery orders, invoices)
- Change request log and all change request forms
- Risk register and issue log
- Quality records (UAT test plans, results, defect log)
- Training records
- Communications (meeting minutes, status reports, formal correspondence)
- Project Acceptance Certificate
- Project Closure Report
- Lessons Learned Register

**Format Arkib / Archive Format:** Digital archive in a named folder structure; encrypted backup on at least two media (e.g., organisational file server + cloud backup). Physical documents scanned to PDF/A format.

### 6.2 Resource Release

| Langkah / Step | Tindakan / Action |
|----------------|-------------------|
| Team members | Formally release from the project; notify their functional managers; complete performance evaluations |
| Contractors / Vendors | Issue formal completion certificates; process final payments; close purchase orders |
| Project tools and licences | Return or reassign project management software licences; close project codes in financial system |
| Physical resources | Return borrowed equipment; vacate project office space if applicable |
| Financial | Close project cost centre; confirm all invoices processed; release any retained amounts on vendor contracts |

### 6.3 Project Celebrations and Recognition

Recognising team contributions is part of professional closure practice. A Level 5 project manager should:
- Send a formal appreciation email to the full team and all key stakeholders
- Nominate exceptional contributors for recognition through the organisation's HR process
- Conduct a brief team celebration (team lunch, certificate of appreciation)
- Acknowledge vendor partners who performed above expectations

---

## 7.0 Transition to Business As Usual (BAU)

### 7.1 BAU Handover Plan

The transition from project to operations requires a structured handover plan:

| Aktiviti / Activity | Tanggungjawab / Responsibility | Tarikh Sasaran / Target Date |
|---------------------|-------------------------------|------------------------------|
| IT operations team trained on all systems | Project team / Vendor | Before go-live |
| NOC monitoring alerts configured and tested | Network Engineer / NOC team | Before go-live |
| Helpdesk scripts updated for new system | Project Manager / Helpdesk Lead | Before go-live |
| SLA for ongoing support agreed and signed | IT Manager / Vendor | Before go-live |
| First 30-day hypercare support period begins | Project team (on call) | Day 0 — go-live |
| First 30-day hypercare support period ends | Project team formally withdrawn | Day 30 post go-live |
| Post-implementation review conducted | Project Manager / IT Manager | Day 30 post go-live |

### 7.2 Post-Implementation Review (PIR)

The PIR is conducted 30–90 days after go-live to assess whether the delivered system is meeting its intended business objectives:

| Aspek / Aspect | Soalan Penilaian / Evaluation Question |
|----------------|----------------------------------------|
| **Pencapaian Teknikal / Technical Performance** | Are network uptime, latency, and throughput meeting the agreed SLAs? |
| **Kepuasan Pengguna / User Satisfaction** | Are end users satisfied with system performance? (survey) |
| **Nilai Perniagaan / Business Value** | Have the business objectives stated in the BRD been achieved? |
| **Kos Operasi / Operating Cost** | Is the actual monthly operating cost within the projected OPEX estimate? |
| **Isu Terbuka / Outstanding Issues** | Are there recurring issues that need to be addressed in a follow-up phase? |

The PIR findings are documented and shared with the project sponsor. Any significant gaps identified in the PIR may trigger a follow-on project or change request under the IT operations change management process.

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer System Management — CoCU 5
- PMI. (2021). *PMBOK® Guide*, 7th Edition. Project Management Institute.
- AXELOS. (2017). *Managing Successful Projects with PRINCE2*, 6th Edition.
- ISO 21502:2020 — Project, Programme and Portfolio Management — Guidance on Project Management
- National Archives of Malaysia — Records Management Guidelines for Government Agencies
- ITIL 4 Foundation — Transition, Release, and Deployment Management