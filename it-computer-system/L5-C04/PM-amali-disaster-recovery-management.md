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

## PELAN MENGAJAR – AMALI

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/PM(AMALI) |
| Muka Surat | 1/1 |
| WARNA KERTAS | KUNING (Yellow) |

**TAJUK:** PM-amali-disaster-recovery-management

**TUJUAN:** Kertas rujukan untuk PM-amali-disaster-recovery-management.

**TEMPAT:** BILIK AMALI / MAKMAL

**TEMPOH:** Rujuk JPW/RK.

**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.

**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.

<!-- /JPK_ENVELOPE_v1 -->
## Agihan Masa Amali / Practical Time Allocation

Total practical hours for CoCU 4 = 350 × 70% = **245 hours**

| KK | Tajuk / Title | Aktiviti Kerja | Jam / Hours |
|----|--------------|---------------|-------------|
| KK(1/4) | Analysing Disaster Recovery Requirements | WA1: Analyse Disaster Recovery Requirements | 81.2 |
| KK(2/4) | Developing a Disaster Recovery Management Plan | WA2: Develop Disaster Recovery Management Plan | 36.4 |
| KK(3/4) | Implementing the Network Disaster Recovery Plan | WA3: Implement Computer Network Disaster Recovery Management Plan | 72.8 |
| KK(4/4) | Producing a Disaster Recovery Management Report | WA4: Produce Disaster Recovery Management Report | 54.6 |
| **Jumlah / Total** | | | **245.0** |

---

## Kaedah Pengajaran / Teaching Method (4-Step)

### 1. PERSEDIAAN (Preparation)

| Langkah / Step | Aktiviti / Activity | Masa / Duration |
|----------------|---------------------|-----------------|
| 1.1 | Welcome trainees; take attendance; confirm all trainees have completed the relevant KP and KT before the practical session | 5 min |
| 1.2 | State the practical learning objectives for the session; connect to the corresponding KP theory | 5 min |
| 1.3 | Review data confidentiality rules: all simulated organisation data is confidential; no real credentials to be used; documents stored in designated folders only | 5 min |
| 1.4 | Distribute the KK (Work Sheet) and explain the exercise structure, expected outputs, and assessment criteria | 5 min |
| 1.5 | Verify lab environment readiness: confirm VM snapshots loaded, backup files accessible, templates distributed | 10 min |

### 2. PENYAMPAIAN (Demonstration)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 2.1 | Demonstrate the practical task step-by-step as per the KK procedures using the instructor's workstation projected to the class |
| 2.2 | For KK(1/4) and KK(2/4) (document-based): show how to complete the BIA table, risk register, and DRP sections using the provided templates; highlight common errors (e.g. RTO > MTD; incorrect risk score calculation) |
| 2.3 | For KK(3/4) (lab-based): demonstrate the lab environment; show how to locate backup files; demonstrate the first database restore step; show correct DNS update syntax |
| 2.4 | For KK(4/4) (report-based): show the PIR template structure; demonstrate how to construct the timeline table and calculate RTO/RPO; show example Executive Summary style |
| 2.5 | Highlight critical decision points: when to escalate, how to justify RTO/RPO values, how to write for a CEO audience |
| 2.6 | Answer questions before trainees begin their own work |

### 3. PENGGUNAAN (Practice)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 3.1 | Trainees perform the practical task as per the KK procedures, individually or in pairs as specified |
| 3.2 | Instructor circulates to observe, guide technique, and ask probing questions to verify understanding (e.g. "Why did you set this RTO value?", "What would happen if you restored the logs out of order?") |
| 3.3 | For KK(3/4) lab sessions: monitor progress against the time allocation; prompt trainees who fall significantly behind to prioritise Sections A, B, and C before attempting D and E |
| 3.4 | Trainees complete the KK Assessment Checklist as they work and self-assess against each criterion |

### 4. PENGESAHAN (Confirmation)

| Langkah / Step | Aktiviti / Activity |
|----------------|---------------------|
| 4.1 | Instructor reviews each trainee's completed outputs against the KK Assessment Checklist; provide written sign-off |
| 4.2 | Verify technical outputs (database restored; application accessible; smoke tests passed) before signing off KK(3/4) |
| 4.3 | Conduct a group debrief: discuss common issues encountered; correct misconceptions; highlight best-practice examples from the class |
| 4.4 | Trainees save and submit all digital documents to the designated training folder; clear workstations |
| 4.5 | Record session completion and any outstanding items in the training register |

---

## Peralatan dan Bahan / Equipment and Materials

| Item | Quantity per Trainee | Notes |
|------|---------------------|-------|
| Computer workstation | 1 | Connected to lab network; VMware Workstation or Hyper-V installed |
| Lab VM set (DC-01, DB-01, APP-01, DR-DB-01, DR-APP-01, FW-01, FW-DR) | 1 set | Pre-configured by instructor; snapshots restored before each session |
| Simulated backup files (SQL Server .bak files, VM snapshots) | 1 set | Pre-loaded on lab backup share |
| BIA worksheet template | 1 | Excel or equivalent; pre-formatted |
| Risk Register template | 1 | Excel or equivalent; pre-formatted |
| DRP template document | 1 | Word or equivalent; section headers pre-formatted |
| DR Implementation Log template | 1 | Table format with timestamp, action, result, responsible columns |
| PIR template document | 1 | Word or equivalent; all 11 sections pre-formatted |
| CAP tracking spreadsheet | 1 | Excel; all fields pre-formatted |
| Organisation scenario brief | 1 | Printed; provided by instructor |
| ISO 22301:2019 one-page summary | 1 | Printed reference card |
| DR test report template | 1 | Word or equivalent |
| Projector / large screen | 1 (shared) | For instructor demonstration |

---

## Keselamatan / Safety Requirements

- All simulated organisation data (system names, IP addresses, credentials) must remain within the training environment — not to be copied to personal devices or shared outside class
- Lab VMs must not be connected to production or internet networks without explicit instructor authorisation
- Trainees must not attempt to access any system outside the designated lab scope
- All printed documents containing simulated sensitive information must be returned to the instructor or shredded at end of session
- Digital documents must be stored only in the designated training folder with appropriate access control — not on personal cloud storage (Google Drive, OneDrive personal) without encryption

---

## Penilaian Amali / Practical Assessment

Upon completion of all 4 KK sessions, trainees will sit for the Performance Assessment (PA):

- **Code:** IT-020-5:2013-C04/PA
- **Duration:** 8 hours (may be conducted over 2 assessment days)
- **Format:** Practical tasks covering all 4 Work Activities — BIA and risk analysis, DRP activation, lab-based technical recovery, and PIR production
- **Assessment criteria:** Process (30%), Output (30%), Attitude (15%), Safety (15%), Environmental (10%)
- **Pass mark:** 60% overall

---

## Nota Pengajar / Instructor Notes

- Pre-load all lab VM snapshots and backup files at least 24 hours before each KK(3/4) session to allow time for troubleshooting lab issues.
- For KK(1/4) and KK(2/4), ensure trainees use the provided templates — free-form documents are harder to assess consistently and may not align with industry-standard formats.
- The tabletop drill component of KK(3/4) works best with groups of 4–6. If class size exceeds 12, run multiple concurrent groups with different scenario complication cards.
- Level 5 trainees should demonstrate **management-level decision-making**, not just execution. During practical sessions, ask "why" questions frequently to push trainees beyond rote procedure following.
- Schedule KK(4/4) (PIR production) immediately after KK(3/4) while the recovery exercise data is fresh in trainees' minds — ideally the session immediately following.