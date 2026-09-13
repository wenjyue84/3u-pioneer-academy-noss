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

## KERTAS KERJA

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C03 COMPUTER SYSTEM SECURITY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM SECURITY MANAGEMENT REQUIREMENTS<br>2. PLAN COMPUTER SYSTEM SECURITY MANAGEMENT<br>3. MANAGE COMPUTER SYSTEM SECURITY<br>4. PRODUCE COMPUTER SYSTEM SECURITY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C03/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-managing-security-operations-and-incidents

**TUJUAN:** Kertas rujukan untuk KK-03-managing-security-operations-and-incidents.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Direct and document the governance of key security management operations: Security Operations Centre (SOC) performance oversight, information security incident management, and identity and access management (IAM) governance.

---

## Tempoh / Duration

5 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Security incident simulation package (provided by instructor) | 1 set |
| 2 | SOC KPI dashboard template | 1 |
| 3 | Incident management log template | 1 |
| 4 | IAM access review template | 1 |
| 5 | Vulnerability report — simulated monthly scan results | 1 |
| 6 | Computer with word processing and spreadsheet software | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Incident simulation data is fictional — treat as confidential for the purposes of the exercise
- Do not use real personal data or real system credentials in any exercise response

---

## Senario / Scenario

Six months have passed since the Security Management Plan was approved at Prisma Teknologi Sdn Bhd. The ISMS is now partially implemented. You are managing the following operational situation this month:

**SOC Operations:** The SOC team has submitted their monthly operational report. Key figures: 1,240 alerts triaged; 18 escalated to incident status; MTTD average = 6.2 hours; MTTR average = 3.8 hours; false positive rate = 31%.

**Security Incident:** Yesterday at 14:35, the SOC detected unusual outbound traffic from the Finance department's file server. Investigation confirmed that an employee's account was used to access and copy 2,400 customer records to an external USB drive. The employee is currently on annual leave. The file server logs show the access occurred at 02:17 that morning.

**IAM Issue:** The quarterly privileged access review has returned results showing: 12 user accounts belonging to former employees are still active; 4 accounts have access to systems beyond their current role; 2 privileged (administrator) accounts have not been used in 90 days.

**Vulnerability Management:** The monthly vulnerability scan identified 3 critical CVSS 9.2 vulnerabilities on the public-facing web server. These have been open for 11 days without remediation. The IT team states the patch requires a planned maintenance window.

**Awareness Programme:** The quarterly phishing simulation returned a 22% click rate — significantly above the 5% target.

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | Review the SOC monthly KPI figures. Complete the SOC KPI Dashboard template: record each KPI, compare to target, assign a RAG (Red / Amber / Green) status, and write a brief management comment for each metric that is off-target. |
| 2 | Identify which SOC metrics require immediate management action. Write a brief directive memo (half page) to the SOC Lead specifying: the metrics that must improve, the root causes you suspect, and the actions you require — with deadlines. |
| 3 | Classify the data exfiltration incident using the organisation's severity classification (Critical/P1 through Low/P4). Justify your classification. |
| 4 | Complete the Incident Management Log for this incident covering all lifecycle phases: Identification, Containment, Eradication, Recovery (propose actions for each phase), Post-Incident Review (planned), and Improvement. For Containment and Eradication, specify what management decisions and approvals are needed. |
| 5 | Determine whether this incident triggers a regulatory notification obligation under PDPA 2010. State your legal reasoning and draft the notification letter to the Personal Data Protection Commissioner (PDPC) if required. |
| 6 | Address the IAM review findings. For each category of issue (former employee accounts, over-privileged accounts, unused privileged accounts), state the required management action, the urgency, and the role responsible for executing the action. |
| 7 | Address the vulnerability management issue. The 3 critical vulnerabilities have exceeded the 24-hour patching SLA by 10 days. Draft an escalation memo to the IT Manager: state the risk, the SLA breach, and the required action — including whether an emergency change request should be raised. |
| 8 | Analyse the phishing simulation result (22% click rate vs. 5% target). Propose a remediation plan for the awareness programme: identify likely root causes, propose 3 specific corrective actions, and set measurable targets and timelines. |
| 9 | Compile all outputs from Steps 1–8 into a Monthly Security Management Report suitable for the Information Security Steering Committee. Include: SOC KPI dashboard; incident summary; IAM review actions; vulnerability remediation status; awareness programme remediation plan. |

---

## Hasil Jangkaan / Expected Outcome

- SOC KPI Dashboard with RAG ratings and management commentary
- SOC Lead directive memo
- Incident classification with justification
- Completed Incident Management Log covering all lifecycle phases
- PDPC notification decision with legal justification (and draft letter if applicable)
- IAM remediation action list
- IT Manager escalation memo (vulnerability management)
- Awareness programme remediation plan
- Monthly Security Management Report (consolidated, suitable for Steering Committee)

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | SOC KPI Dashboard correctly identifies off-target metrics with justified RAG ratings | [ ] Yes [ ] No |
| 2 | Directive memo to SOC Lead is specific, actionable, and time-bound | [ ] Yes [ ] No |
| 3 | Incident severity classification is correctly applied and justified | [ ] Yes [ ] No |
| 4 | Incident Management Log covers all required lifecycle phases with appropriate management actions | [ ] Yes [ ] No |
| 5 | PDPA notification decision is legally sound and documented | [ ] Yes [ ] No |
| 6 | IAM remediation actions are appropriate, urgent, and role-assigned | [ ] Yes [ ] No |
| 7 | Vulnerability escalation memo is clear and references the SLA breach | [ ] Yes [ ] No |
| 8 | Awareness programme remediation plan is evidence-based with measurable targets | [ ] Yes [ ] No |
| 9 | Monthly Security Management Report is professionally structured and suitable for Steering Committee | [ ] Yes [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |