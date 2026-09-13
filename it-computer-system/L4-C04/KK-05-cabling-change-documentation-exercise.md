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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C04 NETWORK CABLING MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. PLAN CABLING LAYOUT AND STANDARDS<br>2. MANAGE CABLE INSTALLATION AND LABELLING<br>3. MAINTAIN CABLE RECORDS AND DIAGRAMS<br>4. COORDINATE WITH FACILITIES AND CONTRACTORS<br>5. DOCUMENT CABLING CHANGES |
| NO. KOD | IT-020-4:2013-C04/KK(5/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-05-cabling-change-documentation-exercise

**TUJUAN:** Kertas rujukan untuk KK-05-cabling-change-documentation-exercise.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Process two cabling change requests end-to-end: complete change request forms, obtain approval, execute a minor physical change in the training lab (re-patch), update all records and the as-built drawing, and produce change completion reports.

---

## Tempoh / Duration

3 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Cabling Change Request Form template | 2 |
| 2 | Change Completion Report template | 2 |
| 3 | Existing cable schedule (from KK-03, or instructor-provided version) | 1 |
| 4 | As-built floor plan drawing (Rev B from KK-03, or instructor-provided) | 1 |
| 5 | Port assignment record | 1 |
| 6 | Change log (from KK-03 or fresh template) | 1 |
| 7 | Label printer with cable labels | 1 (shared) |
| 8 | Patch cords (Cat6A, 0.5 m) | 4 |
| 9 | Link tester (basic continuity tester) | 1 (shared) |
| 10 | Pen and drawing instruments | 1 set |

---

## Langkah Keselamatan / Safety Precautions

- When re-patching, confirm with the instructor that the simulated ports are not in live use before disconnecting any patch cord
- Do not force RJ-45 connectors — align correctly before inserting
- Velcro tie wraps only when dressing patch cords — do not use plastic cable ties in the patch area

---

## Senario / Scenario

You are managing the network cabling for Building A, Floor 1 (continuing from KK-03). Two change requests have been submitted this week:

**Change Request CCR-2026-002 (Move):** User Tan Wei Ming has moved from Room A1-101 (outlet WA-A1-101-A, patch panel PP01 port 01) to Room A1-106. A new outlet WA-A1-106-A (cable HC-A1-01-009, patch panel PP01 port 09) has already been installed by the contractor (test passed, length 29 m, today's date). The old outlet WA-A1-101-A cable (HC-A1-01-001) remains active for future use by another staff member.

**Change Request CCR-2026-003 (Add — Emergency):** The server room has requested one additional Cat6A outlet (WA-A1-SR-A) for a new NAS device. Cable HC-A1-01-010 has been pulled and terminated at patch panel PP01 port 10 (length 18 m). Verbal approval was given by the IT manager (Mr. Azlan) at 09:15 this morning. The physical work is already done; you must now formalise the documentation.

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **Complete Change Request Form for CCR-2026-002:** Fill in all fields of the Cabling Change Request Form: change type (Move), description, cables/outlets affected, impact assessment (user's network port will change; brief disconnection during re-patch), technical specification, estimated cost (labour only — cable already in place), priority (Routine). Mark the "Approved by" field with the IT manager's name and today's date (simulated approval). |
| 2 | **Complete Change Request Form for CCR-2026-003:** Fill in all fields for the emergency Add change. For the approval field, record: "Verbal approval — Mr. Azlan (IT Manager) — [today's date] 09:15. Written confirmation pending." Note this as an emergency change and state that full documentation must be completed by end of day. |
| 3 | **Update the cable schedule for both changes:** (a) CCR-2026-002: Add a new row for HC-A1-01-009 (Active; destination WA-A1-106-A; PP01 port 09; length 29 m; test passed). (b) CCR-2026-003: Add a new row for HC-A1-01-010 (Active; destination WA-A1-SR-A; PP01 port 10; length 18 m; test passed). For both rows, record the CCR number in the Notes column. |
| 4 | **Update the port assignment record:** Update port 09 (assigned to HC-A1-01-009; user Tan Wei Ming; Room A1-106) and port 10 (assigned to HC-A1-01-010; NAS device; Server Room). |
| 5 | **Execute the physical re-patch (CCR-2026-002):** In the training rack, disconnect the patch cord from PP01 port 01 (old position). Connect a new Cat6A patch cord from PP01 port 09 (new position representing Tan Wei Ming's new outlet) to the assigned switch port. Run a continuity test to confirm the link is active. Record the result. |
| 6 | **Print and apply updated labels:** For the new outlet WA-A1-106-A and patch panel port 09, print machine-generated labels. Apply them. Verify that the old outlet WA-A1-101-A still has its correct label (no change required — cable still active). |
| 7 | **Update the as-built floor plan:** (a) Add outlet symbol WA-A1-106-A in Room A1-106. (b) Draw the cable run HC-A1-01-009 from the outlet to TR-A1-01. (c) Add outlet symbol WA-A1-SR-A in the server room. (d) Draw cable run HC-A1-01-010 to TR-A1-01. (e) Increment revision to Rev C. Update revision table with today's date and descriptions of both changes. |
| 8 | **Update the change log:** Add entries for CCR-2026-002 and CCR-2026-003 with all required fields. |
| 9 | **Complete Change Completion Reports:** For each CCR, complete the Change Completion Report: summary of work, cables added/affected, test result, records updated confirmation, labels updated confirmation, completed by (your name), verified by (instructor's name — simulated). |
| 10 | Submit all documents to the instructor: two change request forms, updated cable schedule, updated port assignment record, revised as-built drawing (Rev C), change log, two change completion reports, and continuity test result note. |

---

## Hasil Jangkaan / Expected Outcome

- Two completed and approved Cabling Change Request Forms (routine and emergency)
- Updated cable schedule with 10 active cable entries; all fields complete
- Port assignment record updated for ports 09 and 10
- Physical re-patch completed and continuity tested (link confirmed active)
- New labels applied to WA-A1-106-A and PP01 port 09; WA-A1-SR-A and PP01 port 10
- As-built drawing revised to Rev C with two new outlets and updated revision table
- Change log with entries for CCR-2026-002 and CCR-2026-003
- Two Change Completion Reports completed and ready for filing

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | CCR-2026-002 Change Request Form completed with all fields | [ ] Yes  [ ] No |
| 2 | CCR-2026-003 Change Request Form completed; emergency verbal approval noted | [ ] Yes  [ ] No |
| 3 | Cable schedule updated with two new active cable entries | [ ] Yes  [ ] No |
| 4 | Port assignment record updated for ports 09 and 10 | [ ] Yes  [ ] No |
| 5 | Physical re-patch completed; continuity tested and confirmed | [ ] Yes  [ ] No |
| 6 | New labels printed and applied for both new outlets and panel ports | [ ] Yes  [ ] No |
| 7 | As-built drawing updated to Rev C with two new outlets and cable runs | [ ] Yes  [ ] No |
| 8 | Revision table updated with today's date and both change descriptions | [ ] Yes  [ ] No |
| 9 | Change log updated for both CCRs | [ ] Yes  [ ] No |
| 10 | Two Change Completion Reports completed and submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |