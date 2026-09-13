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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C06 COMPUTER SYSTEM MAINTENANCE MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM MAINTENANCE REQUIREMENTS<br>2. DEVELOP COMPUTER SYSTEM MAINTENANCE PLAN<br>3. MANAGE COMPUTER SYSTEM MAINTENANCE WORK<br>4. MANAGE COMPUTER SYSTEM TROUBLESHOOTING ISSUES/FAILURES<br>5. PRODUCE COMPUTER SYSTEM MAINTENANCE MANAGEMENT REPORT |
| NO. KOD | IT-020-4:2013-C06/KK(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-managing-troubleshooting-failures

**TUJUAN:** Kertas rujukan untuk KK-04-managing-troubleshooting-failures.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Manage a simulated critical (P1) system failure from initial detection through structured troubleshooting, root cause analysis, corrective action, and KEDB documentation.

---

## Tempoh / Duration

4 hours (including role-play exercise and RCA workshop)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Incident scenario briefing document (provided by instructor) | 1 |
| 2 | Incident management form template | 1 |
| 3 | Escalation matrix (from KP-04) | 1 |
| 4 | RCA template (5 Whys + Fishbone) | 1 |
| 5 | KEDB entry template | 1 |
| 6 | Post-incident report template | 1 |
| 7 | Computer with word processing software | 1 |

---

## Langkah Keselamatan / Safety Precautions

- All incident information in this exercise is simulated — do not share outside the classroom
- During the role-play, the trainee acting as manager should not attempt to personally fix the technical issue — focus on coordination and documentation

---

## Senario / Scenario

It is Monday morning, 08:15. Users begin reporting that they cannot access the student information system (SIS). The monitoring alert system has not triggered (it was offline for maintenance). You receive a phone call from the Faculty of Engineering registrar: "The SIS is completely down. Final exam results cannot be submitted. The deadline is 09:00 today."

You investigate and find:
- The SIS application server (App Server 1) is unreachable via ping
- The server room monitoring system shows the server's CPU temperature alarm was triggered at 07:55
- A review of the maintenance log shows the cooling fan in App Server 1 was flagged as faulty during last Saturday's PM but was not yet replaced (Deviation 1 from KK-03)
- The server is unresponsive at the console — thermal shutdown has occurred

Your team consists of: Technician A (senior), Technician B (junior). The server vendor's hotline is available.

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Log the incident. Complete the incident management form: incident number, time logged, reported by, affected systems, number of users impacted, and initial priority classification. Justify the P1 classification. |
| 2 | Apply the escalation matrix. Identify who must be notified immediately (IT Manager, Faculty Dean, vendor). Draft and send a brief incident notification message to the IT Manager (written format). |
| 3 | Assign Technician A to the physical server. Define his immediate task: confirm thermal shutdown, power off safely, replace the faulty fan (spare part location confirmed), allow cooldown, power on, and verify boot. Establish a check-in protocol: report every 15 minutes. |
| 4 | Identify and apply a workaround while the server is being restored: determine if exam result submission can be rerouted (e.g. manual email submission to registrar) and communicate this to the Faculty Dean. Document the workaround decision. |
| 5 | Monitor progress. Record Technician A's 15-minute status reports. Note actual restoration time vs SLA target (P1: 2 hours). |
| 6 | Once service is restored, confirm with the registrar. Send a service restoration notification to all affected users. Record the actual downtime duration. |
| 7 | Conduct a 5 Whys RCA for this incident. Start from the immediate cause (thermal shutdown) and trace back to the root cause. Complete the RCA template. |
| 8 | Develop corrective and preventive actions from the RCA. Assign each action an owner and target completion date. |
| 9 | Create a KEDB entry for the known error pattern (delayed replacement of faulty cooling fan creates thermal shutdown risk on mission-critical server). |
| 10 | Write the Post-Incident Report using the template. Include: incident summary, timeline, root cause, business impact (estimated hours × number of affected users), corrective actions, preventive actions, and lessons learned. |

---

## Hasil Jangkaan / Expected Outcome

- Completed incident management form (P1, with priority justification)
- Escalation notification message to IT Manager
- Technician assignment with defined task and check-in protocol
- Documented workaround decision
- Status monitoring log (15-minute intervals)
- Service restoration notification
- Completed 5 Whys RCA with root cause identified
- Corrective and preventive action table (with owners and dates)
- KEDB entry
- Post-Incident Report (complete, management-ready)

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Incident logged with complete information and P1 justification | [ ] Yes  [ ] No |
| 2 | Escalation matrix applied correctly; IT Manager notified with appropriate message | [ ] Yes  [ ] No |
| 3 | Technician assigned with clear task scope and check-in protocol | [ ] Yes  [ ] No |
| 4 | Workaround identified, decided, and communicated to the business | [ ] Yes  [ ] No |
| 5 | 15-minute monitoring log maintained until service restored | [ ] Yes  [ ] No |
| 6 | Service restoration notification sent to affected users | [ ] Yes  [ ] No |
| 7 | 5 Whys RCA reaches the true root cause (not just the immediate trigger) | [ ] Yes  [ ] No |
| 8 | Corrective and preventive actions are specific, assigned, and time-bound | [ ] Yes  [ ] No |
| 9 | KEDB entry is complete and correctly structured | [ ] Yes  [ ] No |
| 10 | Post-Incident Report is complete and suitable for management review | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |