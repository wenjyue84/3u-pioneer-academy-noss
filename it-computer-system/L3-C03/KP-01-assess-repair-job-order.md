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
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C03 COMPUTER SYSTEM REPAIR |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST<br>2. CARRY OUT ONLINE TROUBLESHOOTING<br>3. PERFORM ON-SITE REPAIR<br>4. PREPARE COMPUTER STATUS REPORT |
| NO. KOD | IT-020-3:2013-C03/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-assess-repair-job-order

**TUJUAN:** Kertas rujukan untuk KP-01-assess-repair-job-order.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify the key fields of a computer repair job order and explain their purpose
2. Distinguish between a new repair job order and a change request
3. Apply a systematic assessment process to determine job scope, priority, and escalation need
4. Describe the escalation criteria for repair tasks that exceed technician authority or skill level
5. Document job order assessment findings accurately before commencing repair work

---

## 1.0 Introduction to the Repair Job Order

A repair job order (Perintah Kerja Pembaikan) is a formal document that authorises a technician to carry out diagnostic and repair work on a computer system. It is issued by a supervisor, help desk, or client and defines the scope of the repair task. Without an authorised job order, the technician must not proceed — this protects both the organisation and the client from unauthorised modifications.

A change request (Permintaan Perubahan) is a modification to an existing repair engagement. It may expand scope (e.g. replace additional components discovered during diagnosis), change priority, or cancel part of the original instruction. Change requests must be approved before any additional work is performed.

---

## 2.0 Fields of a Repair Job Order

A standard computer repair job order contains the following fields:

| Field | Description |
|-------|-------------|
| Job order number (No. Perintah Kerja) | Unique identifier for tracking and audit purposes |
| Date issued (Tarikh Dikeluarkan) | Date the repair request was initiated |
| Reported by (Dilaporkan Oleh) | Name and department of the user or client reporting the fault |
| Asset tag / serial number | Identifier of the computer unit to be repaired |
| Fault description (Penerangan Kerosakan) | User's description of the problem in plain language |
| Symptom(s) observed (Gejala Diperhatikan) | Observable indicators (e.g. no display, fails to boot, overheating) |
| Priority level (Tahap Keutamaan) | Urgency of repair: Normal, High, or Critical |
| Assigned technician (Juruteknik Bertanggungjawab) | Name of the technician responsible for the task |
| Target completion date | Deadline for the repair to be completed |
| Parts authorised (Alat Ganti Diluluskan) | Components approved for replacement without further authorisation |
| Authorising officer (Pegawai Meluluskan) | Supervisor or manager who approved the job order |

---

## 3.0 Types of Repair Requests

Repair requests are classified by origin and nature:

| Type | Trigger | Example |
|------|---------|---------|
| Corrective repair (Pembaikan Pembetulan) | User-reported fault | PC fails to start after power surge |
| Emergency repair (Pembaikan Kecemasan) | Critical system failure | Server-class desktop supporting production stops working |
| Warranty repair (Pembaikan Waranti) | Hardware still under manufacturer warranty | HDD fails within warranty period — vendor RMA required |
| Change request (Permintaan Perubahan) | Scope change during an active repair | Technician discovers additional faulty RAM modules during approved HDD replacement |

---

## 4.0 Job Order Assessment Process

Before commencing any repair, the technician must systematically assess the job order using the following steps:

1. **Read the entire job order.** Do not begin work based on a verbal summary. Review every field.
2. **Verify the asset.** Confirm the asset tag or serial number on the physical unit matches the job order. Repair performed on the wrong unit is a serious procedural error.
3. **Review the fault description and symptoms.** The user's language may be non-technical (e.g. "the screen went black"). The technician must interpret the symptom and identify probable causes.
4. **Assess job scope.** Determine whether the repair is within the technician's authorisation level and skill set. Complex repairs (e.g. motherboard-level component replacement, data recovery from failed RAID) may require escalation.
5. **Check parts availability.** Identify any components likely to require replacement and verify stock availability before committing to a completion date.
6. **Confirm priority and deadline.** High-priority jobs must be logged and actioned promptly. Critical jobs may require immediate suspension of lower-priority work.
7. **Record the assessment.** Document findings on the job order form or in the helpdesk system before proceeding to diagnosis.

---

## 5.0 Priority Classification

Priority levels determine the order in which jobs are actioned and the acceptable response time:

| Priority | Definition | Target Response | Example |
|----------|-----------|----------------|---------|
| Normal (Biasa) | Non-urgent; user can continue working on alternative equipment | 2–3 working days | Optical drive not reading discs |
| High (Tinggi) | User cannot perform core work functions | Same day or next working day | PC boots to BSOD; user has no spare unit |
| Critical (Kritikal) | Business-critical system or multiple users affected | Immediate — within hours | Finance workstation failure at month-end closing |

---

## 6.0 Escalation Criteria

Not all repair tasks can or should be handled by the assigned technician. Escalation (Peningkatan) is required when:

- The fault is beyond the technician's authorisation level (e.g. server hardware, specialised industrial PCs)
- The repair requires specialist tools not available on-site (e.g. soldering station for component-level PCB repair)
- The unit is under active warranty — incorrect repair by the technician may void the warranty
- Data recovery is needed from a physically damaged storage device — this requires a specialist lab
- The technician's initial diagnosis is inconclusive after following standard diagnostic steps

When escalating, the technician must:
1. Record all steps already taken and findings to date on the job order
2. Notify the supervisor or help desk with a written escalation note
3. Ensure the unit is secured and correctly labelled pending handover to the next responsible party

---

## 7.0 Common Errors in Job Order Assessment

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Beginning work without a job order | Unauthorised repair; liability risk | Always obtain a signed job order before starting |
| Not verifying asset tag | Repair performed on wrong unit | Check asset tag physically against job order before touching the unit |
| Accepting vague fault descriptions without clarification | Wrong diagnostic path; wasted time | Ask the user for specific symptoms; note exact error messages |
| Ignoring priority level | High-priority job missed; SLA breach | Sort the day's job orders by priority at the start of each shift |
| Failing to escalate when required | Incomplete or incorrect repair; warranty voided | Know and apply the escalation criteria; when in doubt, escalate |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 3: Computer System Repair
- CompTIA A+ Core 1 (220-1101) and Core 2 (220-1102) — Chapter on Troubleshooting Methodology
- ISO/IEC 20000 IT Service Management — Incident and Change Management concepts
- Organisational IT helpdesk and asset management policy