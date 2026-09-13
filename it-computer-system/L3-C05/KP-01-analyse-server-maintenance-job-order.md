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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C05 SERVER MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER MAINTENANCE JOB ORDER<br>2. CARRY OUT HARDWARE MAINTENANCE<br>3. PERFORM SERVER OPERATING SYSTEM MAINTENANCE<br>4. PREPARE SERVER MAINTENANCE RECORD |
| NO. KOD | IT-020-3:2013-C05/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-analyse-server-maintenance-job-order

**TUJUAN:** Kertas rujukan untuk KP-01-analyse-server-maintenance-job-order.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and structure of a server maintenance job order
2. Differentiate between preventive maintenance (PM) and corrective maintenance (CM) job orders
3. Identify the scope of work, priority level, and safety precautions from a job order
4. Verify resource availability (tools, spare parts, personnel) before commencing maintenance
5. Escalate or clarify ambiguous or incomplete job orders through the correct channel

---

## 1.0 Introduction to Server Maintenance Job Orders

A server maintenance job order (Perintah Kerja Penyelenggaraan Pelayan) is the authorised document that initiates and governs all maintenance activities on a server. It defines what must be done, who is responsible, when it must be completed, and what resources are required. No maintenance work should begin on a production server without a duly approved job order.

Servers are critical infrastructure. Unplanned or unauthorised maintenance can cause service outages, data loss, and security breaches. The job order system enforces accountability, traceability, and compliance with organisational IT policies.

---

## 2.0 Types of Server Maintenance

Server maintenance activities are classified into two broad categories:

| Type | Bahasa Malaysia | Description | Typical Trigger |
|------|-----------------|-------------|-----------------|
| Preventive Maintenance (PM) | Penyelenggaraan Pencegahan | Scheduled, routine tasks performed to prevent failures before they occur | Maintenance calendar, manufacturer schedule, SLA requirement |
| Corrective Maintenance (CM) | Penyelenggaraan Pembetulan | Reactive tasks performed to restore a server to normal operation after a fault or failure | Fault report, monitoring alert, user complaint |

**Preventive maintenance** examples: cleaning dust filters, replacing thermal paste, updating firmware, testing UPS, verifying RAID integrity, rotating backup media.

**Corrective maintenance** examples: replacing a failed hard disk drive, re-seating a loose RAM module, rebuilding a degraded RAID array, reinstalling a corrupted OS component.

---

## 3.0 Structure of a Server Maintenance Job Order

A well-formed server maintenance job order contains the following fields:

| Field | Medan | Description |
|-------|-------|-------------|
| Job order number | Nombor perintah kerja | Unique identifier for tracking and audit |
| Date issued | Tarikh dikeluarkan | Date the job order was created and approved |
| Issued by | Dikeluarkan oleh | Name and designation of the authorising officer |
| Assigned to | Ditugaskan kepada | Name(s) of the technician(s) responsible |
| Server details | Butiran pelayan | Hostname, IP address, model, location (rack, data centre) |
| Maintenance type | Jenis penyelenggaraan | Preventive (PM) or Corrective (CM) |
| Priority level | Tahap keutamaan | Critical / High / Medium / Low |
| Scope of work | Skop kerja | Detailed list of tasks to be performed |
| Required tools | Alatan diperlukan | List of tools and equipment needed |
| Required parts | Alat ganti diperlukan | Spare parts, firmware images, media |
| Scheduled start time | Masa mula dijadualkan | Planned commencement time (maintenance window) |
| Scheduled end time | Masa tamat dijadualkan | Planned completion time |
| Downtime approval | Kelulusan masa henti | Signature of service owner approving planned downtime |
| Safety precautions | Langkah keselamatan | ESD precautions, lockout/tagout, PPE requirements |
| Remarks | Catatan | Any special instructions or known risks |

---

## 4.0 Priority Levels

The priority level determines the response time and escalation path:

| Priority | Keutamaan | Typical Response Time | Example Scenario |
|----------|-----------|-----------------------|------------------|
| Critical (Kritikal) | Immediate — within 1 hour | Production server down; core services unavailable |
| High (Tinggi) | Within 4 hours | Degraded RAID array; one disk failed, rebuild needed |
| Medium (Sederhana) | Within 24 hours | Scheduled firmware update approaching deadline |
| Low (Rendah) | Within 72 hours | Routine cleaning, log archival, minor software patch |

Priority must be set by the issuing officer based on business impact, not by the attending technician. If a technician believes the assigned priority is incorrect, they must escalate to the supervisor before proceeding.

---

## 5.0 Analysing the Scope of Work

Before accepting a job order, the technician must thoroughly analyse the scope of work:

1. **Read the entire job order.** Do not begin work based on the title or summary alone. Hidden requirements often appear in the remarks section.
2. **Identify all tasks.** List every discrete action required (e.g. replace HDD, update BIOS, test RAID, document results).
3. **Assess the maintenance window.** Confirm whether the scheduled downtime window is sufficient to complete all tasks. Flag if it is not.
4. **Confirm access permissions.** Verify that the technician has the necessary system access (server room keycard, administrator credentials, remote management access).
5. **Identify dependencies.** Some tasks cannot begin until others are complete (e.g. data backup must complete before a disk replacement).
6. **Assess risk.** Identify any activities that carry a risk of data loss or extended downtime and note the mitigation steps.

---

## 6.0 Resource Verification

Before commencing work, the technician must verify that all required resources are available:

| Resource Category | Items to Verify |
|-------------------|-----------------|
| Tools (Alatan) | Anti-static wrist strap (gelang anti-statik), screwdrivers, torque driver, cable management tools, label maker, flashlight |
| Test equipment (Peralatan ujian) | Multimeter, network cable tester, POST diagnostic card |
| Spare parts (Alat ganti) | Correct HDD/SSD model and capacity, RAM module (correct type/speed), power supply unit (correct wattage and form factor) |
| Software/media (Perisian/media) | Firmware image, OS installation media, driver packages, backup restoration files |
| Documentation (Dokumentasi) | Server manual, network diagram, current configuration backup |
| Personnel (Kakitangan) | Sufficient qualified technicians; second person required for heavy equipment or high-voltage work |

If any resource is unavailable, the technician must inform the supervisor and update the job order before proceeding. Do not substitute parts or tools without written approval.

---

## 7.0 Safety and Compliance Requirements

Server maintenance activities carry specific safety requirements that must be identified from the job order before work begins:

| Requirement | Details |
|-------------|---------|
| ESD protection (Perlindungan ESD) | Anti-static wrist strap must be worn when handling circuit boards, RAM, CPUs, and drives |
| Lockout/Tagout (LOTO) | Power must be isolated and tagged before working on power supply units or UPS systems |
| Personal Protective Equipment (PPE) | Safety glasses when cleaning with compressed air; gloves when handling sharp rack edges |
| Data backup (Sandaran data) | Current backup must be confirmed before any hardware replacement or OS-level maintenance |
| Change management (Pengurusan perubahan) | All changes must be logged in the organisation's change management system (e.g. ITSM ticketing system) |
| Two-person rule | High-risk operations (e.g. physical server removal from rack) require two technicians present |

---

## 8.0 Escalation and Clarification

A technician must not proceed with maintenance if the job order contains any of the following issues:

- Missing or illegible fields (e.g. no server hostname, no approval signature)
- Scope of work that exceeds the technician's skill level or authorisation
- Required parts or tools that are unavailable
- Maintenance window that is insufficient for the stated tasks
- Conflicting instructions (e.g. "replace HDD" but the backup status is unknown)

In these cases, the technician must:
1. Note the specific issue on the job order
2. Contact the issuing officer or supervisor immediately
3. Do not commence any work until a revised or clarified job order is received

---

## 9.0 Common Errors in Job Order Analysis

| Error | Ralat | Consequence | Prevention |
|-------|-------|-------------|------------|
| Starting work without reading the full job order | Memulakan kerja tanpa membaca keseluruhan perintah kerja | Tasks missed; wrong parts used | Read every field; use an analysis checklist |
| Accepting an incomplete job order | Menerima perintah kerja yang tidak lengkap | Ambiguous scope leads to wrong actions | Verify all mandatory fields before signing acceptance |
| Ignoring the maintenance window | Mengabaikan tetingkap penyelenggaraan | Service disruption outside approved hours | Confirm window with service owner before scheduling |
| Not verifying backup status | Tidak mengesahkan status sandaran | Data loss if maintenance causes a fault | Check backup log and confirm last successful backup date |
| Wrong priority assessment | Penilaian keutamaan yang salah | Delayed response to critical fault | Escalate disagreements to supervisor; do not self-adjust |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 5: Server Maintenance
- CompTIA Server+ Certification Study Guide — Chapter: Preventive and Corrective Maintenance
- ITIL Foundation — Change Management and Incident Management processes
- Organisational IT Maintenance Policy and Change Management Procedure