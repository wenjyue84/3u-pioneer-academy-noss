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
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C05 SERVER MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER MAINTENANCE JOB ORDER<br>2. CARRY OUT HARDWARE MAINTENANCE<br>3. PERFORM SERVER OPERATING SYSTEM MAINTENANCE<br>4. PREPARE SERVER MAINTENANCE RECORD |
| NO. KOD | IT-020-3:2013-C05/KK(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-prepare-server-maintenance-record

**TUJUAN:** Kertas rujukan untuk KK-04-prepare-server-maintenance-record.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

By the end of this activity, the trainee will be able to:
1. Compile all maintenance actions performed on a server into a structured maintenance record.
2. Record component replacements with full part identification (model, serial number, supplier).
3. Document pre- and post-maintenance system status to demonstrate improvement or resolution.
4. Identify any outstanding issues or follow-up actions and assign responsibility.
5. Obtain required signatures and file the completed record according to organisational procedure.

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Completed hardware maintenance checklist (from KK-02) | 1 |
| 2 | Completed OS maintenance checklist (from KK-03) | 1 |
| 3 | Signed maintenance job order (from KK-01) | 1 |
| 4 | Server maintenance record template (provided by instructor) | 1 |
| 5 | Computer workstation with word processor or CMMS/ticketing system access | 1 |
| 6 | Pen | 1 |

---

## Langkah Keselamatan / Safety Precautions

- The maintenance record is an official document. Entries must be factual and accurate — do not estimate or guess values; refer to source checklists.
- Do not omit any action taken, even if the outcome was unsuccessful. Transparency is required for audit and troubleshooting purposes.
- Treat server asset information (hostnames, IP addresses, serial numbers) as sensitive. Do not display or share the completed record outside the authorised filing location.
- Once signed, the record must not be altered. If a correction is required, draw a single line through the incorrect entry, write the correction beside it, initial the correction, and note the date.

---

## Prosedur / Procedure

| Langkah / Step | Arahan / Instruction |
|----------------|----------------------|
| 1 | Gather all source documents: the signed job order from KK-01, the hardware maintenance checklist from KK-02, and the OS maintenance checklist from KK-03. Verify that all three documents relate to the same job order number before proceeding. |
| 2 | Open the server maintenance record template. Complete the header section: Job Order Number, Server Hostname, Server IP Address, Server Model and Serial Number, Location (rack/room), Date and Time maintenance started, Date and Time maintenance ended, Performed by (trainee name and staff ID). |
| 3 | **Section A — Hardware Maintenance Summary:** Transfer all hardware actions from the KK-02 checklist into this section. For each action, record: component affected (e.g., "Cooling Fan — Bay 2"), pre-maintenance condition (e.g., "Failed — fault LED active"), action taken (e.g., "Replaced with spare unit"), and post-maintenance condition (e.g., "Operational — fault LED cleared"). |
| 4 | **Section B — Replacement Parts Record:** For every component that was physically replaced, complete one row in the parts table: Part Type, Manufacturer, Model Number, Old Unit Serial Number (removed), New Unit Serial Number (installed), Supplier/Source, and Warranty Expiry Date (if known). If no parts were replaced, write "NIL — no components replaced during this maintenance cycle." |
| 5 | **Section C — OS Maintenance Summary:** Transfer all OS actions from the KK-03 checklist into this section. Record: OS patch level before maintenance, OS patch level after maintenance, list of updates applied (count and type), services restarted (name, previous state, new state), disk usage before and after cleanup (per volume, in GB), and a summary of critical event log entries found and resolved. |
| 6 | **Section D — System Status Comparison:** Complete the pre/post comparison table. For each metric, enter the value recorded before maintenance and the value recorded after maintenance. Metrics to include: overall hardware health status (iDRAC/iLO), RAID array status, CPU temperature (if logged), OS patch level, system drive free space, and number of critical event log errors. |
| 7 | **Section E — Outstanding Issues and Follow-Up Actions:** List any items that could not be resolved during this maintenance cycle (e.g., "Replacement NIC ordered — ETA 5 working days", "Memory module sent for RMA — awaiting replacement"). For each item, specify: Issue description, Action required, Person responsible, Target completion date. If there are no outstanding issues, write "NIL." |
| 8 | **Section F — Recommendations:** Record any recommendations for preventing recurrence or improving server reliability (e.g., "Increase preventive maintenance frequency from quarterly to bi-monthly due to high dust accumulation", "Schedule OS patching for next maintenance window"). Keep recommendations specific and actionable. |
| 9 | Review the entire completed record. Verify that every field is filled, all dates and times are consistent, all part serial numbers are correct, and the job order number matches throughout. Correct any discrepancies now — do not sign an inaccurate record. |
| 10 | Obtain signatures in the sign-off section: Trainee (performed by), Instructor/Supervisor (verified by), and (if applicable) Customer/Requestor (acknowledged by). Date all signatures. |
| 11 | File the completed maintenance record according to the filing procedure demonstrated by the instructor (e.g., upload to the CMMS system, place in the server's physical log binder, or save to the designated network share). Record the filing location on the checklist. |
| 12 | Return all source documents (job order, hardware checklist, OS checklist) to the instructor. Confirm that no documents remain on the trainee's personal workstation. |

---

## Hasil Dijangka / Expected Outcome

Upon completing this activity, the trainee will have produced a fully completed server maintenance record containing:
- A verified header with accurate asset identification.
- A hardware maintenance summary with pre/post conditions for each action.
- A complete parts replacement log with serial numbers and supplier information.
- An OS maintenance summary including patch levels and disk space metrics.
- A pre/post system status comparison table.
- All outstanding issues documented with assigned responsible persons and target dates.
- Required signatures obtained and the record filed in the designated location.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | All three source documents (job order, hardware checklist, OS checklist) match the same job order number | [ ] Yes  [ ] No |
| 2 | Record header completed: hostname, IP, model, serial, location, start/end times, performer | [ ] Yes  [ ] No |
| 3 | Section A: all hardware actions recorded with pre and post conditions | [ ] Yes  [ ] No |
| 4 | Section B: all replaced parts recorded with model and serial numbers (or "NIL" if none) | [ ] Yes  [ ] No |
| 5 | Section C: OS patch levels (before and after), updates applied, services and disk space recorded | [ ] Yes  [ ] No |
| 6 | Section D: pre/post comparison table completed for all required metrics | [ ] Yes  [ ] No |
| 7 | Section E: outstanding issues documented with responsible person and target date (or "NIL") | [ ] Yes  [ ] No |
| 8 | Section F: at least one actionable recommendation recorded | [ ] Yes  [ ] No |
| 9 | Record reviewed for completeness and accuracy before signing | [ ] Yes  [ ] No |
| 10 | All required signatures obtained (trainee, instructor, requestor) | [ ] Yes  [ ] No |
| 11 | Completed record filed in designated location; filing location noted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |