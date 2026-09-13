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
| NO. KOD | IT-020-3:2013-C05/KP(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-server-maintenance-record

**TUJUAN:** Kertas rujukan untuk KP-04-server-maintenance-record.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and legal/organisational requirements for server maintenance records
2. Identify the mandatory fields of a server maintenance record
3. Prepare accurate and complete maintenance records for both preventive and corrective maintenance activities
4. Maintain a server maintenance logbook and history file
5. Describe the record retention, storage, and disposal requirements for maintenance documentation

---

## 1.0 Introduction to Server Maintenance Records

A server maintenance record (rekod penyelenggaraan pelayan) is the official written account of all maintenance activities performed on a server. It documents what was done, by whom, when, and what the outcome was. The maintenance record is created at the completion of each maintenance activity and is retained as part of the server's permanent history file.

Maintenance records serve multiple purposes:

| Purpose | Tujuan | Detail |
|---------|--------|--------|
| Accountability | Akauntabiliti | Identifies the technician responsible for each maintenance action |
| Traceability | Kebolehkesanan | Enables a future technician or auditor to reconstruct exactly what was done and when |
| Troubleshooting | Penyelesaian masalah | Recurring faults can be identified by reviewing the maintenance history |
| Compliance | Pematuhan | Regulatory frameworks (ISO 27001, PCI-DSS, ITSM standards) require documented maintenance records |
| Warranty and vendor support | Jaminan dan sokongan vendor | Vendors may require maintenance records to validate warranty claims |
| Capacity planning | Perancangan kapasiti | Trends in disk usage, CPU load, and component replacements inform hardware refresh decisions |

---

## 2.0 Types of Maintenance Records

| Record Type | Jenis Rekod | When Prepared | Content Summary |
|-------------|-------------|--------------|-----------------|
| Preventive Maintenance (PM) Report | Laporan Penyelenggaraan Pencegahan | After each scheduled PM activity | Tasks performed, inspection findings, measurements taken, parts consumed |
| Corrective Maintenance (CM) Report | Laporan Penyelenggaraan Pembetulan | After resolving a fault or incident | Fault description, root cause, corrective action taken, parts replaced, time to repair |
| Firmware/Patch Update Record | Rekod Kemaskini Perisian Tegar/Tampalan | After each firmware or OS patch update | Component updated, previous version, new version, update tool, result |
| Component Replacement Record | Rekod Penggantian Komponen | After replacing any hardware component | Replaced component details, replacement component details, reason for replacement |
| Server Maintenance Logbook | Buku Log Penyelenggaraan Pelayan | Running log — entry after every maintenance event | Date, activity type, brief summary, technician name |

---

## 3.0 Mandatory Fields of a Server Maintenance Record

All server maintenance records must contain the following mandatory fields:

| Field | Medan | Description |
|-------|-------|-------------|
| Record number | Nombor rekod | Unique sequential identifier for the record (linked to the job order number) |
| Server details | Butiran pelayan | Hostname, IP address, model and serial number, physical location (rack, data centre, room) |
| Maintenance type | Jenis penyelenggaraan | Preventive (PM) or Corrective (CM) |
| Date of maintenance | Tarikh penyelenggaraan | Date the maintenance activity was performed |
| Start time | Masa mula | Time the maintenance activity commenced |
| End time | Masa tamat | Time the maintenance activity was completed |
| Total downtime | Jumlah masa henti | Total duration the server or service was unavailable |
| Technician name | Nama juruteknik | Full name of the technician who performed the maintenance |
| Technician signature | Tandatangan juruteknik | Handwritten or electronic signature |
| Supervisor name | Nama penyelia | Full name of the supervisor who reviewed the record |
| Supervisor signature | Tandatangan penyelia | Handwritten or electronic signature |
| Work performed | Kerja yang dilakukan | Detailed description of all tasks performed |
| Parts used | Bahagian yang digunakan | Part name, part number, quantity, and serial number of any components installed or removed |
| Test results | Keputusan ujian | Results of post-maintenance functional tests |
| Remarks | Catatan | Any anomalies observed, deferred actions, or recommendations for follow-up |
| Next scheduled PM | PM yang dijadualkan seterusnya | Date of the next preventive maintenance activity for this server |

---

## 4.0 Preparing a Preventive Maintenance (PM) Record

A PM record documents the routine maintenance activities performed during a scheduled maintenance window. It must be prepared while the work is still fresh — ideally completed before leaving the maintenance site.

**Step-by-step procedure:**

1. **Retrieve the approved job order.** The job order number becomes the reference number for the maintenance record.
2. **Record the server details.** Confirm and record hostname, IP address, model, serial number, and physical location.
3. **Record start and end time.** Note the exact time work commenced and the time all maintenance tasks and post-maintenance tests were completed.
4. **List all tasks performed.** Use specific, technical language — avoid vague descriptions. Examples:
   - GOOD: "Cleaned dust from all intake/exhaust vents and CPU heatsink fins using ESD-safe compressed air. Replaced air filter (Filter P/N: HPE 867990-B21). Applied fresh thermal paste (Arctic MX-4) to CPU socket 1 after removing and cleaning heatsink."
   - POOR: "Cleaned server."
5. **Record all parts consumed.** For each part installed or replaced, note the part name, manufacturer part number, quantity, and serial number (if applicable).
6. **Record measurements and inspection findings.** Examples: CPU temperature before and after thermal paste replacement; RAID array status (Optimal/Degraded); PSU output voltage readings; fan RPM readings from IPMI.
7. **Record post-maintenance test results.** Confirm that the server passed all verification checks (POST, OS boot, service availability, RAID status, event log review).
8. **Sign and date the record.** Both the technician and the supervisor must sign the completed record.
9. **File the record** in the server's maintenance history file.

---

## 5.0 Preparing a Corrective Maintenance (CM) Record

A CM record documents a reactive maintenance event triggered by a fault or failure. It must also capture the fault investigation process, root cause, and corrective action.

**Additional fields for a CM record:**

| Field | Medan | Description |
|-------|-------|-------------|
| Fault/incident description | Penerangan kerosakan/insiden | How the fault was reported or detected; symptoms observed |
| Fault detection method | Kaedah pengesanan kerosakan | Monitoring alert, user complaint, physical inspection, IPMI/BMC alert |
| Root cause | Punca akar | The underlying cause of the fault (e.g. "HDD failed due to reallocated sector count exceeding threshold as shown in S.M.A.R.T. log") |
| Corrective action | Tindakan pembetulan | Specific steps taken to resolve the fault |
| Replaced components | Komponen yang diganti | Full details of removed (faulty) and installed (replacement) components |
| Time to repair (TTR) | Masa untuk membaiki | Total elapsed time from fault notification to service restoration |
| Impact | Kesan | Services affected and duration of impact |
| Preventive recommendation | Cadangan pencegahan | Recommendation to prevent recurrence (e.g. "Schedule quarterly S.M.A.R.T. checks for all HDDs") |

---

## 6.0 Component Replacement — Recording Requirements

Every component replacement must be documented with sufficient detail to create a complete audit trail:

| Field | Example Entry |
|-------|--------------|
| Component type | Hard Disk Drive (HDD) |
| Slot / Bay position | Drive Bay 3 (of 8) |
| Removed component — Part number | Seagate ST4000NM0035 |
| Removed component — Serial number | WBF0A12B |
| Removed component — Reason for removal | S.M.A.R.T. status: Reallocated Sector Count = 842 (threshold: 36); RAID status: Degraded |
| Installed component — Part number | Seagate ST4000NM0035 |
| Installed component — Serial number | WBF1C45D |
| Installed component — Source | Spare parts store (inventory tag: SPR-HDD-047) |
| RAID rebuild initiated | Yes — initiated 14:32, completed 23:15 (8 hrs 43 min) |
| Post-replacement RAID status | Optimal |

Removed faulty components must be:
1. Tagged with the date of removal, server hostname, and reason for removal
2. Stored in the designated defective parts area pending vendor return or disposal
3. Not discarded without written approval from the supervisor

---

## 7.0 Server Maintenance Logbook

The server maintenance logbook (buku log penyelenggaraan pelayan) is a running chronological record of all maintenance events for a specific server. It provides a quick-reference history without requiring retrieval of individual detailed reports.

**Logbook entry format:**

| Date | Time | Activity Type | Summary | Technician | Reference |
|------|------|--------------|---------|------------|-----------|
| 2026-01-15 | 09:00–11:30 | PM | Quarterly PM: cleaned dust, verified RAID (Optimal), checked temperatures (CPU1: 42°C, CPU2: 44°C), updated BMC firmware from 2.1.0 to 2.3.1 | Ahmad Razif | JO-2026-0042 |
| 2026-02-28 | 14:25–23:20 | CM | Drive Bay 3 HDD failed (S.M.A.R.T. error). Replaced with spare (S/N: WBF1C45D). RAID rebuilt — array Optimal at 23:15. | Nurul Ain | JO-2026-0081 |
| 2026-03-12 | 02:00–04:00 | OS Patch | Applied March 2026 cumulative update (KB5035845) and .NET Framework update (KB5034276). Server rebooted. All services restored. | Ahmad Razif | CHG-2026-0055 |

**Logbook maintenance rules:**
- One logbook per server (or per server cluster)
- Entries must be made in chronological order — do not insert entries out of sequence
- Corrections must be made by drawing a single line through the error and initialling the correction — do not use correction fluid (liquid paper)
- The logbook must be stored securely with the server's documentation set

---

## 8.0 Record Retention, Storage, and Disposal

### 8.1 Retention Requirements

Maintenance records must be retained for a minimum period to support audits, warranty claims, and incident investigations:

| Record Type | Minimum Retention Period |
|-------------|--------------------------|
| PM and CM maintenance reports | 3 years from date of maintenance |
| Component replacement records | Life of the server + 1 year |
| Firmware/patch update records | 3 years from date of update |
| Server maintenance logbook | Life of the server + 3 years |

Individual organisations may specify longer retention periods. Always follow the more stringent requirement.

### 8.2 Storage Requirements

| Storage Method | Requirements |
|----------------|-------------|
| Physical (paper) records | Filed in a labelled folder specific to each server; stored in a lockable filing cabinet in the IT office; protected from fire and water damage |
| Electronic records | Stored in the organisation's ITSM or document management system; access controlled (read access for technicians; write access for the record creator and supervisor only); backed up as part of the regular data backup cycle |

### 8.3 Disposal

When records reach the end of their retention period:
- **Paper records:** Cross-cut shredded or incinerated — do not place in general waste as they may contain server IP addresses, configuration details, or security-relevant information
- **Electronic records:** Deleted from the ITSM system by the IT manager with a disposal log entry noting the record numbers destroyed, date, and approver

---

## 9.0 Common Errors in Maintenance Record Preparation

| Error | Ralat | Consequence | Prevention |
|-------|-------|-------------|------------|
| Vague task descriptions | Penerangan tugasan yang tidak jelas | Record is useless for future reference or audit | Use specific technical language; record exact measurements and part numbers |
| Missing supervisor signature | Tandatangan penyelia tiada | Record is incomplete and not legally valid | Do not file a record until it is countersigned by the supervisor |
| Recording from memory after a delay | Merekod dari ingatan selepas kelewatan | Inaccurate times, tasks, or part numbers | Complete the record on-site immediately after finishing maintenance |
| Not recording replaced component serial numbers | Tidak merekod nombor siri komponen yang diganti | Cannot trace component history for warranty or audit | Record both removed and installed serial numbers for every replacement |
| Disposing of records before retention period ends | Melupuskan rekod sebelum tamat tempoh simpanan | Compliance violation; cannot support audit or legal claim | Implement a retention calendar; only dispose with written manager approval |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 5: Server Maintenance
- CompTIA Server+ Certification Study Guide — Chapter: Documentation and Change Management
- ITIL Foundation — Service Transition: Change Management and Configuration Management
- ISO/IEC 20000-1: Information Technology Service Management — Documentation requirements
- Organisational IT Maintenance Policy, Record Retention Policy, and Change Management Procedure