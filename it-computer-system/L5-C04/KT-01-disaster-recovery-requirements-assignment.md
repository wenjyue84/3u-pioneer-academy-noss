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

## KERTAS TUGASAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KT(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-01-disaster-recovery-requirements-assignment

**TUJUAN:** Kertas rujukan untuk KT-01-disaster-recovery-requirements-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Answer ALL questions. Refer to KP(1/4) for guidance. Write your answers in the space provided or on a separate answer sheet. This assignment is formative and does not count toward final assessment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

---

## Arahan / Instructions

Answer ALL questions. Refer to KP(1/4) for guidance. Write your answers in the space provided or on a separate answer sheet. This assignment is formative and does not count toward final assessment.

**Masa / Duration:** 1 hour 30 minutes

---

## Soalan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks — 2 marks each)

**A1.** Which of the following BEST describes the relationship between Business Continuity (BC) and Disaster Recovery (DR)?

- (a) BC and DR are identical — both focus only on IT systems
- (b) DR is a subset of BC; DR focuses on IT systems while BC covers the entire organisation
- (c) BC is a subset of DR; BC only applies to small businesses
- (d) DR replaces BC planning in modern organisations

**A2.** The Maximum Tolerable Downtime (MTD) is BEST defined as:

- (a) The time it takes to restore a system from backup
- (b) The maximum time an organisation can tolerate a critical function being unavailable before consequences become unacceptable
- (c) The average downtime experienced per month
- (d) The time between backup cycles

**A3.** An organisation's online payment gateway has an RTO of 2 hours. This means:

- (a) Backups must be taken every 2 hours
- (b) The payment gateway must be restored within 2 hours of a disaster declaration
- (c) The payment gateway can tolerate 2 hours of data loss
- (d) Recovery must begin within 2 hours of the incident being detected

**A4.** A system has an RPO of 30 minutes. Which backup strategy is MOST appropriate?

- (a) Weekly full backup stored on tape
- (b) Daily incremental backup to cloud
- (c) Continuous data protection (CDP) or log shipping every 30 minutes
- (d) Monthly full backup with no incrementals

**A5.** In a risk assessment matrix, a threat rated Likelihood=4 and Impact=4 produces a risk score of:

- (a) 4
- (b) 8
- (c) 16
- (d) 44

**A6.** Which international standard governs Business Continuity Management Systems (BCMS)?

- (a) ISO/IEC 27001:2022
- (b) ISO 22301:2019
- (c) NIST SP 800-53
- (d) ISO 9001:2015

**A7.** A gap analysis in the context of DR requirements analysis is used to:

- (a) Identify the financial cost of hardware purchases
- (b) Compare current DR controls against required controls and identify shortfalls
- (c) Calculate the number of backup tapes needed
- (d) Measure the speed of the internet connection at the DR site

**A8.** Which system would typically be classified as Tier 1 (Critical) in a hospital's BIA?

- (a) Staff canteen booking system
- (b) Patient records and clinical information system
- (c) Meeting room reservation portal
- (d) Employee training management system

**A9.** The "3-2-1 Rule" for data backup refers to:

- (a) 3 backups per day, 2 offsite, 1 in cloud
- (b) 3 copies of data, on 2 different media types, with 1 copy offsite
- (c) 3 full backups, 2 differentials, 1 incremental per week
- (d) 3 DR sites, 2 warm, 1 hot

**A10.** Which of the following is an example of a HUMAN-INDUCED threat to IT infrastructure?

- (a) Lightning strike causing power surge
- (b) Flash flood entering the data centre
- (c) Ransomware attack encrypting all file servers
- (d) Hardware failure due to manufacturing defect

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** Define Recovery Time Objective (RTO) and Recovery Point Objective (RPO). Explain why both values must be formally agreed upon by senior management, not decided unilaterally by the IT team. (8 marks)

**B2.** Describe the FIVE (5) steps of the Business Impact Analysis (BIA) methodology as outlined in KP(1/4). For each step, state its purpose. (10 marks)

**B3.** An IT manager states: "Our company makes daily backups, so our RPO is 24 hours." Evaluate this statement. Under what business circumstances would a 24-hour RPO be acceptable, and under what circumstances would it be unacceptable? Provide ONE example of each. (6 marks)

**B4.** Identify and briefly explain THREE (3) categories of threats that an organisation's IT infrastructure may face. Give ONE specific example for each category. (6 marks)

---

### Bahagian C: Soalan Esei / Essay (40 marks)

**C1.** You are engaged as an IT consultant by **Klinik Bestari Sdn. Bhd.**, a private clinic chain with 5 branches across Selangor. The clinic uses the following IT systems:
- Electronic Medical Records (EMR) system — used by all doctors and nurses
- Appointment booking system (web-based, patient-facing)
- Pharmacy management and stock system
- Payroll and HR system
- WiFi and network infrastructure across all branches

The current IT setup has no DR plan, no offsite backup, and a single server at the main branch.

(a) Conduct a Business Impact Analysis (BIA) for all five systems. For each system, state: the MTD, a justified RTO, a justified RPO, the impact category most affected by downtime, and the priority tier (Tier 1–4). Present your findings in a structured table. (20 marks)

(b) Identify FOUR (4) risks facing this clinic's IT infrastructure. For each risk, state: the threat, likelihood rating (1–5), impact rating (1–5), risk score, risk classification (High/Medium/Low), and ONE recommended control. (10 marks)

(c) Write the Gap Analysis section of a DR Requirements Report for this clinic. Identify at least THREE (3) gaps between the current state and an adequate DR posture. For each gap, state the current state, the required state, and the consequence of leaving the gap unaddressed. (10 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*