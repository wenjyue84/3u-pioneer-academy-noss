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
| NO. KOD | IT-020-4:2013-C04/KK(1/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-01-cabling-layout-planning-exercise

**TUJUAN:** Kertas rujukan untuk KK-01-cabling-layout-planning-exercise.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Produce a compliant cabling layout plan for a given floor scenario, including cable count, outlet placement, TR location, and labelling scheme.

---

## Tempoh / Duration

3 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Floor plan drawing (A3, simulated building floor) | 1 per trainee |
| 2 | Drawing instruments (ruler, pencil, eraser, coloured pens) | 1 set |
| 3 | Cable count calculation worksheet | 1 |
| 4 | TIA-606-B label convention reference card | 1 |
| 5 | ANSI/TIA-568 distance limit reference card | 1 |
| 6 | Standard cabling symbols legend sheet | 1 |
| 7 | Calculator | 1 |

---

## Langkah Keselamatan / Safety Precautions

- This is a planning exercise — no physical cabling tools are used
- Handle drawing instruments carefully; store safely after use
- Return all reference materials to the instructor at the end of the session

---

## Senario / Scenario

You are the network cabling administrator for a company relocating to a new office. You have been given a floor plan for **Floor 2 of Building A** with the following details:

- Total floor area: approximately 800 m²
- 15 individual workstations (2 outlets each)
- 1 conference room (4 outlets)
- 1 printer alcove (2 outlets)
- 1 reception desk (2 outlets)
- Furthest workstation from the proposed TR is approximately 72 m (measured along walls and ceiling void pathway)
- The building uses a **star topology** horizontal cabling structure
- Standard to comply with: **ANSI/TIA-568.2-D**, cable category **Cat6A UTP**
- Labelling standard: **TIA-606-B**
- TR room available: room A2-TR01 (near the lift lobby, approximately in the centre of the floor)

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Study the floor plan carefully. Identify all work areas (workstations, conference room, printer alcove, reception). Mark each work area with a pencil circle. |
| 2 | Mark the TR location (room A2-TR01) on the floor plan. Verify that no outlet exceeds 90 m from the TR — measure the longest run along the pathway (not straight line). Record the measurement. |
| 3 | Mark the proposed outlet positions at each work area. Each workstation receives 2 outlets; conference room 4 outlets; printer alcove 2 outlets; reception 2 outlets. |
| 4 | Calculate the total number of outlets and add 15% spare capacity. Round up to the nearest 12 (to match patch panel organisation). Record your calculation on the worksheet. |
| 5 | Draw the cable run routes from each outlet back to the TR. Use dashed lines for cable runs; solid lines for walls. Label each route with an approximate pathway length (measure along the drawn route using the plan scale). |
| 6 | Calculate the total cable required: for each outlet, add the measured pathway length + 6 m slack (3 m at each end). Sum all cables. Add 8% waste allowance. Record total cable quantity in metres. |
| 7 | Assign TIA-606-B compliant identifiers to: (a) the TR room, (b) the patch panel, (c) five representative outlets (choose one per work area type). Use the label convention: WA-A2-[RoomNo]-[Port] for outlets; TR-A2-01-PP01 for the patch panel. Record your labels on the worksheet. |
| 8 | Produce a TR layout sketch (elevation view) showing: patch panel position in rack, horizontal cable manager, distribution switch, and PDU. Label each item. |
| 9 | Complete the cable count summary table on the worksheet: total outlets, spare capacity, total cable (m), patch panel port count required, switch port count required. |
| 10 | Review your plan for compliance: confirm all outlet-to-TR distances ≤ 90 m; confirm TR room location is central; confirm labels follow TIA-606-B. Submit the floor plan and worksheet to the instructor. |

---

## Hasil Jangkaan / Expected Outcome

- Annotated floor plan showing all outlet positions, cable runs, TR location, and approximate dimensions
- Completed cable count calculation worksheet with totals and spare capacity
- TIA-606-B compliant label list for TR, patch panel, and five representative outlets
- TR elevation sketch with rack components identified
- All outlet-to-TR distances confirmed ≤ 90 m

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | All work area outlets correctly marked on floor plan | [ ] Yes  [ ] No |
| 2 | TR location identified and all outlets confirmed within 90 m | [ ] Yes  [ ] No |
| 3 | Outlet count calculated correctly with 15% spare capacity | [ ] Yes  [ ] No |
| 4 | Total cable quantity calculated with 8% waste allowance | [ ] Yes  [ ] No |
| 5 | TIA-606-B labels correctly assigned (TR, panel, 5 outlets) | [ ] Yes  [ ] No |
| 6 | TR elevation sketch complete with all components labelled | [ ] Yes  [ ] No |
| 7 | Cable runs drawn on floor plan for all outlet positions | [ ] Yes  [ ] No |
| 8 | Plan reviewed for standard compliance before submission | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |