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
| NO. KOD | IT-020-3:2013-C03/KP(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-computer-status-report

**TUJUAN:** Kertas rujukan untuk KP-04-computer-status-report.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose of the computer status report and its role in IT service management
2. Identify the mandatory fields and sections of a computer status report
3. Write accurate technical descriptions of fault diagnosis findings, repair actions, and parts used
4. Record functionality test results in a clear and verifiable format
5. Submit a completed status report following organisational sign-off and filing procedures

---

## 1.0 Purpose of the Computer Status Report

The computer status report (Laporan Status Komputer) is the formal record of a completed repair engagement. It is written by the technician upon completion of all repair work and functionality testing, and it serves the following purposes:

- **Accountability:** Provides a clear record of what was found, what was done, and who authorised the work
- **Asset management:** Updates the organisation's IT asset register with the latest component configuration and repair history
- **Audit trail:** Provides evidence that the repair was carried out correctly should a dispute or warranty claim arise
- **Knowledge transfer:** Informs colleagues or future technicians of the repair history if the same unit fails again
- **Billing and cost tracking:** Supports internal cost recovery or external invoicing by recording parts used and labour hours

A report that is incomplete, inaccurate, or missing a signature is not a valid record — it must be completed before the unit is returned to the user.

---

## 2.0 Structure and Fields of the Computer Status Report

A standard computer status report contains the following sections:

### 2.1 Header Information

| Field | Description |
|-------|-------------|
| Report number (No. Laporan) | Unique identifier; may be linked to or identical to the job order number |
| Date of report (Tarikh Laporan) | Date the report was completed |
| Technician name and employee ID (Nama Juruteknik) | Full name and staff ID of the technician who performed the repair |
| Supervisor / Authorising officer | Name of the person who reviewed and approved the report |

### 2.2 Asset Information

| Field | Description |
|-------|-------------|
| Asset tag (Tag Aset) | Organisation's internal identifier for the computer unit |
| Serial number (No. Siri) | Manufacturer's serial number, found on the chassis label |
| Make and model (Jenama dan Model) | e.g. Dell OptiPlex 7090, HP EliteDesk 800 G6 |
| User / Department (Pengguna / Jabatan) | The person or department to whom the unit is assigned |
| Location (Lokasi) | Physical location of the unit within the premises |

### 2.3 Fault Description

This section records the fault as reported by the user, in the user's own words, followed by the technician's interpretation of the symptom.

**Example:**

> **User-reported fault:** "The computer suddenly switched off and would not turn on again."
>
> **Technician's interpretation:** System presents no power symptom — no LED indicators, no fan spin on pressing power button. Suspected PSU failure.

The fault description must be factual and specific. Vague entries such as "PC not working" are not acceptable.

### 2.4 Diagnosis Findings

This section documents the systematic diagnostic steps taken and the conclusion reached. Each step should include the tool used and the result observed.

**Example format:**

| Step | Tool / Method | Result / Finding |
|------|---------------|-----------------|
| 1 | Visual inspection of chassis interior | No physical damage, swollen capacitors, or burnt smell observed |
| 2 | Multimeter check of PSU 24-pin ATX connector | +12 V rail measured 9.8 V (below acceptable range of 11.4–12.6 V) — PSU confirmed faulty |
| 3 | RAM visual inspection and reseating | Two DDR4 modules correctly seated; no fault found |
| 4 | Boot test with replacement PSU | System POST completed successfully; OS loaded normally |

**Diagnosis conclusion:** PSU failure — +12 V rail under-voltage caused no-power condition.

### 2.5 Repair Actions Taken

This section lists every corrective action performed, in chronological order.

**Example:**

1. Powered off and unplugged unit; performed ESD precautions
2. Disconnected all power connectors from failed PSU
3. Removed failed PSU (Corsair CX450M, 450 W)
4. Installed replacement PSU (Corsair CX450M, 450 W — from workshop stock, batch no. WS-2024-11)
5. Reconnected all power connectors; cable management completed
6. Powered on; completed POST and OS boot verification

### 2.6 Parts Used

All components consumed during the repair must be documented for asset register and stock management purposes:

| Part Description | Part Number / Model | Serial Number | Source | Quantity |
|------------------|--------------------|--------------|----|----------|
| PSU, Corsair CX450M 450W | CP-9020102-UK | SN-CX450-00234 | Workshop stock | 1 |
| Thermal paste, Arctic MX-4 (2g) | ACTCP00002B | N/A | Workshop stock | 1 tube |

If no parts were replaced (e.g. the repair was a reseat or software fix), state: "No parts replaced."

### 2.7 Functionality Test Results

This section records the results of the post-repair functionality test. Every test performed must be listed with a clear Pass / Fail result.

| Test | Method | Result |
|------|--------|--------|
| POST and OS boot | Powered on; observed POST; OS loaded to login screen | Pass |
| RAM detection | BIOS hardware monitor — shows 16 GB DDR4 (2 × 8 GB) | Pass |
| Storage detection | BIOS storage list — Samsung 870 EVO 500 GB detected | Pass |
| Temperature at idle (10 min) | HWMonitor: CPU 38°C, System 34°C, HDD 32°C | Pass |
| Network connectivity | `ping 8.8.8.8` — 4 packets sent, 4 received, 0% loss | Pass |
| Application launch | MS Office, Chrome browser, company ERP — all opened without error | Pass |
| User sign-off | User tested unit and confirmed satisfactory operation | Pass |

### 2.8 Recommendations

If the technician identifies additional issues that were not part of the original repair scope, they must be recorded as recommendations for the supervisor's consideration — not actioned without a new job order.

**Example recommendations:**

- "HDD SMART data shows Reallocated Sector Count = 14. Recommend scheduling preventive HDD replacement within 3 months."
- "System has 8 GB RAM installed. User has reported slow performance during multitasking. Recommend upgrading to 16 GB if within budget."

### 2.9 Signatures

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Technician | | | |
| Supervisor | | | |
| User / Client (receiving the unit) | | | |

All three signatures are required before the report is filed. A report without the user's signature does not confirm the unit was returned and accepted.

---

## 3.0 Writing Standards for the Status Report

The computer status report is an official document. The following writing standards apply:

| Standard | Requirement |
|----------|-------------|
| Language | Professional English or Bahasa Malaysia; consistent throughout the report |
| Specificity | Use exact component names, model numbers, measured values, and error codes — not vague descriptions |
| Chronological order | Diagnosis steps and repair actions listed in the order they were performed |
| Objectivity | State facts only; do not assign blame or include personal opinions |
| Completeness | Every mandatory field must be filled; blank fields are not acceptable |
| Legibility | If handwritten, must be neat and legible; if typed, use consistent font and spacing |

---

## 4.0 Filing and Retention

Completed status reports must be filed according to organisational document management policy:

| Method | Requirement |
|--------|------------|
| Hardcopy filing | Filed by job order number in the IT helpdesk folder; retained for minimum 3 years (or as per organisational policy) |
| Digital filing | Scanned and uploaded to the helpdesk system linked to the asset record; filename format: `[Asset Tag]_[Report Number]_[Date].pdf` |
| Asset register update | The IT asset register must be updated to reflect any component changes (e.g. new PSU serial number, new HDD model) |

---

## 5.0 Common Errors in Status Report Preparation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Vague fault description ("PC not working") | Report is not useful for future reference; audit fails | Use specific, technical language with exact symptoms and error codes |
| Missing parts details (no model or serial number) | Asset register cannot be updated; stock management fails | Record every replaced part with full description, model, and serial number |
| Skipping the functionality test section | No evidence the repair was verified; unit may be returned with a fault | Complete the full functionality test checklist before writing the report |
| Missing user signature | No confirmation the unit was received and accepted | Obtain user signature at handover; do not close the job order without it |
| Not recording recommendations | Known latent faults go unaddressed until they cause another failure | Always record observed issues beyond the repair scope under Recommendations |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 3: Computer System Repair
- ISO/IEC 20000 IT Service Management — Incident Record and Change Record requirements
- CompTIA A+ Core 2 (220-1102) — Documentation, Change Management, and Ticketing Systems
- Organisational IT asset management and helpdesk policy