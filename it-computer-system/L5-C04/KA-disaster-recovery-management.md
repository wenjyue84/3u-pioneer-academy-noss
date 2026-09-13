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

## KERTAS PENILAIAN PENGETAHUAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KA |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KA-disaster-recovery-management

**TUJUAN:** Kertas rujukan untuk KA-disaster-recovery-management.

**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan kepada Pelatih / Instructions to Trainee

1. This paper consists of THREE (3) sections: A, B, and C.
2. Answer ALL questions in ALL sections.
3. Write your answers clearly in the answer booklet provided.
4. This is a CLOSED BOOK examination. No reference materials are permitted.
5. Duration: **2 hours**
6. Total marks: **100**
7. Pass mark: **60%**

---

## Arahan kepada Pengajar / Instructions to Instructor

- Distribute the question paper and answer booklet to each trainee.
- Allow exactly 2 hours for the examination.
- Collect all papers at the end of the allocated time.
- Mark using the answer scheme provided (separate document).
- This KA covers all four Work Activities of CoCU 4.

---

## BAHAGIAN A: SOALAN PELBAGAI PILIHAN / SECTION A: MULTIPLE CHOICE (30 marks — 2 marks each)

Answer all 15 questions. Circle the correct answer.

**1.** The international standard for Business Continuity Management Systems that Malaysian organisations use for DR compliance is:

- (a) ISO/IEC 27001:2022
- (b) ISO 22301:2019
- (c) NIST SP 800-34
- (d) BS 25999

**2.** Recovery Point Objective (RPO) defines:

- (a) The maximum time to restore a system after disaster declaration
- (b) The maximum acceptable amount of data loss measured in time
- (c) The point at which the DRP is activated
- (d) The minimum number of backup copies required

**3.** A Tier 1 Critical system with an RTO of 2 hours is BEST served by which DR strategy?

- (a) Cold site with weekly tape backup
- (b) Hot site or cloud DR with real-time replication
- (c) Warm site with daily differential backup
- (d) Reciprocal agreement with a partner organisation

**4.** In the GFS backup rotation scheme, which backup set is retained for 12 months?

- (a) Son (daily)
- (b) Father (weekly)
- (c) Grandfather (monthly)
- (d) All three are retained for 12 months

**5.** Synchronous data replication differs from asynchronous replication in that:

- (a) Synchronous replication is always cheaper
- (b) Synchronous replication acknowledges a write only after BOTH primary and replica have committed it, achieving RPO = 0
- (c) Asynchronous replication achieves faster write performance at the primary site with no trade-off
- (d) Synchronous replication can only be used with cloud storage

**6.** The FIRST step in the network recovery sequence during a DR activation is:

- (a) Restore the ERP application server
- (b) Apply pending transaction log backups to the database
- (c) Restore physical connectivity, switches, and core network services (DHCP, DNS)
- (d) Redirect application connection strings to the DR site

**7.** A tabletop exercise is BEST described as:

- (a) A live failover test where production systems are shut down
- (b) A discussion-based walkthrough of the DRP with key stakeholders; no systems are activated
- (c) A functional test of selected isolated systems
- (d) An unannounced drill conducted without prior notification to the DR team

**8.** DBCC CHECKDB is run after database restoration to:

- (a) Apply the latest Windows security patches
- (b) Verify database integrity and detect corruption introduced during the restore process
- (c) Rebuild all database indexes for performance
- (d) Create an encrypted backup of the restored database

**9.** The DR Corrective Action Plan (CAP) item status can be changed to CLOSED when:

- (a) The target date has passed
- (b) The owner sends an email stating it is done
- (c) Remediation is verified with documented evidence
- (d) The DR Coordinator approves verbally

**10.** Under Bank Negara Malaysia's RMiT policy, a significant IT incident must be reported to BNM:

- (a) Within 30 calendar days
- (b) In the next annual audit report
- (c) Within 1 hour of detection; detailed report within 5 business days
- (d) Only if the incident results in customer data loss

**11.** The "Pilot Light" cloud DR model is characterised by:

- (a) Full production running simultaneously in cloud and on-premises
- (b) Minimal core infrastructure pre-provisioned in cloud, scaled up only when disaster occurs
- (c) Complete backup restoration from cold storage at time of disaster
- (d) A warm standby running at full scale continuously in the cloud

**12.** Mean Time to Detect (MTTD) measures the time between:

- (a) DR activation and system recovery
- (b) System restoration and user acceptance
- (c) Incident occurrence and detection/alert generation
- (d) Last backup and the disaster event

**13.** The 5 Whys root cause analysis technique is used to:

- (a) Identify five people responsible for the disaster
- (b) Drill down from the visible symptom to the underlying root cause by asking "Why?" in succession
- (c) Produce exactly five corrective actions for every incident
- (d) Satisfy the five clauses of ISO 22301 related to incidents

**14.** Which section of a Post-Incident Report is written for CEO-level readership in non-technical language?

- (a) Technical Recovery Procedures
- (b) Database Restore Log
- (c) Executive Summary
- (d) Network Diagram Appendix

**15.** Failback refers to:

- (a) A second disaster occurring at the DR site
- (b) The process of returning operations from the DR site to the restored primary site
- (c) The failure of the backup system during DR activation
- (d) Backing up data at the DR site after recovery

---

## BAHAGIAN B: SOALAN JAWAPAN PENDEK / SECTION B: SHORT ANSWER (30 marks)

Answer all 6 questions.

**16.** Define Business Impact Analysis (BIA) and explain FOUR (4) pieces of information it produces that are essential inputs to the Disaster Recovery Plan. (5 marks)

**17.** Compare a HOT SITE and a COLD SITE. For each, state: (a) typical RTO achievable, (b) cost relative to the other, and (c) one business type for which it is the most appropriate choice. (6 marks)

**18.** Describe the four types of DR backup (Full, Incremental, Differential, Continuous Data Protection). For each, state its main advantage and its main disadvantage. (8 marks)

**19.** Identify FOUR (4) mandatory sections of a Post-Incident Report (PIR) and explain the purpose of each section in one sentence. (4 marks)

**20.** A disaster occurs at 10:00. The DR Coordinator declares disaster at 10:20. Database restoration is completed at 13:45. The latest applied backup was taken at 09:15. The RTO target is 3 hours from declaration; the RPO target is 2 hours.

Calculate: (a) actual RTO, (b) actual RPO, (c) MTTD. State whether each target was met. (5 marks)

**21.** State THREE (3) conditions that trigger a mandatory DRP review and update. For each, describe the specific part of the DRP most likely to need updating. (2 marks)

---

## BAHAGIAN C: SOALAN ESEI / SECTION C: ESSAY (40 marks)

Answer all 2 questions.

**22.** **Scenario:** You are the IT Manager of **Universiti Teknologi Bestari (UTB)**, a private university with 8,000 students and 500 staff. The university's critical IT systems include:

- Student Information System (SIS): enrolment, results, fees
- Learning Management System (LMS): online lectures, assignments, assessments
- Finance system: payroll, accounts payable/receivable
- Email and collaboration (Microsoft 365, cloud-hosted)
- Library management system
- Network infrastructure (campus-wide)

A flash flood inundates the university's server room at 02:00 on a Sunday night. All on-premises systems go offline. The university has a DRP but it was last tested 18 months ago. The DR site is a warm site at a colocation facility 15 km away.

(a) Describe how you would determine the order in which systems are recovered. What information from the BIA would guide your decision? Assign a recovery priority tier to each of the six systems listed and justify each assignment. (10 marks)

(b) Walk through the first four hours of DR activation in chronological detail. Identify which DR team roles are involved at each stage, what technical actions are taken, and what communication should occur with students, staff, and the public. (15 marks)

(c) After full recovery is achieved, you must write the PIR. Describe: (i) the timeline data you would collect, (ii) how you would conduct the root cause analysis, and (iii) the three most critical corrective actions you would recommend, given that the DRP had not been tested for 18 months and the flood was not anticipated. (15 marks)

---

## TAMAT / END OF PAPER

---

*Answer scheme is provided as a separate instructor document.*