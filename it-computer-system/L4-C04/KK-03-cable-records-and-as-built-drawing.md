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
| NO. KOD | IT-020-4:2013-C04/KK(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-cable-records-and-as-built-drawing

**TUJUAN:** Kertas rujukan untuk KK-03-cable-records-and-as-built-drawing.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Complete a cable schedule, update a port assignment record, and produce a revised as-built drawing segment based on a simulated post-installation scenario.

---

## Tempoh / Duration

3 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Simulated cable schedule template (Excel or printed) | 1 |
| 2 | Simulated port assignment record template | 1 |
| 3 | As-built floor plan drawing (Rev A, with 6 cables installed — simulated scenario) | 1 |
| 4 | Drawing instruments (ruler, pencil, coloured pens) | 1 set |
| 5 | TIA-606-B label convention reference card | 1 |
| 6 | Change log template | 1 |
| 7 | Revision table template | 1 |
| 8 | Computer with spreadsheet software (if available) | 1 |

---

## Langkah Keselamatan / Safety Precautions

- This is a documentation exercise — no physical cabling tools are required
- Handle printed drawings carefully; do not fold or damage them
- Save all electronic work frequently to prevent data loss

---

## Senario / Scenario

You are the network cabling administrator for Building A, Floor 1. The initial installation (6 Cat6A horizontal cables, 6 outlets, patch panel PP01 in TR-A1-01) was completed and documented in Rev A of the as-built drawing and cable schedule.

The following changes have since occurred and need to be documented:

**Change 1 (Add):** Two new workstations have been installed in Room A1-105. Two new Cat6A cables (HC-A1-01-007 and HC-A1-01-008) have been pulled and terminated at patch panel PP01 ports 07 and 08. Outlets WA-A1-105-A and WA-A1-105-B have been installed. Cable lengths: 38 m and 41 m. Both cables passed Cat6A certification. Installation date: today's date.

**Change 2 (Decommission):** The outlet WA-A1-101-B (Cable HC-A1-01-002, PP01 port 02) is no longer in use. The workstation has been removed. The cable remains in place but is decommissioned.

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Review the existing cable schedule (Rev A). Identify the 6 existing cable entries. Verify that each entry has: Cable ID, type, origin (patch panel port), destination (outlet ID), length, installation date, test result, and status. |
| 2 | Add two new rows to the cable schedule for the cables installed under Change 1 (HC-A1-01-007 and HC-A1-01-008). Fill in all required fields. Status: Active. |
| 3 | Update the existing row for HC-A1-01-002 (Change 2 — decommission). Change the status field from "Active" to "Decommissioned". Add the decommission date and a note referencing the change request number (use CCR-2026-001 as the reference). |
| 4 | Open the port assignment record. Update port 07 and port 08 of PP01 to show the new cable IDs, outlet IDs, and user/device assignments (both assigned to new workstations in Room A1-105). Update port 02 status to "Decommissioned — no device". |
| 5 | On the as-built floor plan drawing (Rev A), add the two new outlet symbols at the correct positions in Room A1-105 (mark approximately 2 m from the south wall, 1.5 m apart). Draw the cable run lines from the outlets back to TR-A1-01 along the corridor pathway. Label each run with the cable ID. |
| 6 | Mark outlet WA-A1-101-B on the floor plan with a "decommissioned" notation (cross-hatch the outlet symbol or add a "D" suffix). |
| 7 | Increment the drawing revision from Rev A to Rev B. Update the revision table at the bottom of the drawing: add a new row with today's date, description ("Add 2 outlets Room A1-105; decommission WA-A1-101-B"), and your name. |
| 8 | Complete a change log entry for both changes: CCR number, date, change type, description, cables affected, drawing revision. |
| 9 | Conduct a self-check: verify that every cable in the cable schedule has a corresponding outlet on the floor plan; verify that the patch panel port assignment record matches the cable schedule. Record any discrepancies. |
| 10 | Submit the updated cable schedule, port assignment record, revised floor plan drawing (Rev B), and change log to the instructor. |

---

## Hasil Jangkaan / Expected Outcome

- Updated cable schedule with 8 active entries and 1 decommissioned entry — all fields complete
- Updated port assignment record reflecting current active and decommissioned ports
- As-built floor plan revised to Rev B showing new outlets, cable runs, and decommissioned outlet notation
- Revision table updated with date, description, and drafter name
- Change log completed for both changes
- Self-check completed and discrepancies recorded (none expected if procedure followed correctly)

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Two new cables added to cable schedule with all fields complete | [ ] Yes  [ ] No |
| 2 | Decommissioned cable status updated with date and CCR reference | [ ] Yes  [ ] No |
| 3 | Port assignment record updated for ports 02, 07, and 08 | [ ] Yes  [ ] No |
| 4 | Two new outlet symbols added to floor plan in correct location | [ ] Yes  [ ] No |
| 5 | Cable run lines drawn from new outlets to TR | [ ] Yes  [ ] No |
| 6 | Decommissioned outlet marked on floor plan | [ ] Yes  [ ] No |
| 7 | Drawing revision incremented to Rev B | [ ] Yes  [ ] No |
| 8 | Revision table updated with date, description, and drafter name | [ ] Yes  [ ] No |
| 9 | Change log completed for both changes | [ ] Yes  [ ] No |
| 10 | Self-check completed; discrepancies recorded | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |