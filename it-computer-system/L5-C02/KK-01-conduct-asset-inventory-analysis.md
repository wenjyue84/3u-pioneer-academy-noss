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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C02 COMPUTER SYSTEM ASSET MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM ASSET INVENTORY<br>2. DEFINE OPERATIONAL STATUS OF ASSETS<br>3. ESTIMATE COSTS AND SPACE REQUIREMENTS<br>4. DETERMINE ASSET MANAGEMENT SYSTEMS<br>5. MONITOR ASSET TAGGING AND LABELLING<br>6. EXECUTE ASSET DISPOSAL<br>7. PREPARE ASSET MANAGEMENT REPORTS |
| NO. KOD | IT-020-5:2013-C02/KK(1/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-01-conduct-asset-inventory-analysis

**TUJUAN:** Kertas rujukan untuk KK-01-conduct-asset-inventory-analysis.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Conduct a systematic physical and logical asset inventory for an assigned department, reconcile findings against the existing asset register, and produce a reconciled inventory report.

---

## Tempoh / Duration

6 hours (including preparation, physical survey, automated scan, reconciliation, and report writing)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Laptop or workstation with ITAM system access | 1 |
| 2 | Barcode/QR scanner (handheld) | 1 |
| 3 | Printed asset inventory checklist (simulated) | 1 set |
| 4 | Network discovery tool (Advanced IP Scanner or equivalent) installed | 1 |
| 5 | ITAM software account (Snipe-IT or GLPI training instance) | 1 |
| 6 | Simulated asset register (CSV or printed) | 1 |
| 7 | Stationery (pen, clipboard, sticky notes) | 1 set |
| 8 | Simulated office environment with tagged assets | As available |

---

## Langkah Keselamatan / Safety Precautions

- Do not move, disconnect, or power off any equipment during the inventory unless explicitly instructed
- Handle all assets carefully; do not touch internal components
- Obtain access permission from the department supervisor before entering work areas
- Treat all asset data as confidential; do not share outside the exercise

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Obtain the simulated asset register from the instructor. Review the register to understand the expected number and types of assets in the assigned area. Note any assets already flagged as Idle, In Repair, or Pending Disposal. |
| 2 | Divide the assigned area into zones (by room or desk row). Create a zone map on paper or in a spreadsheet. This ensures complete coverage and prevents double-counting. |
| 3 | Enter each zone and physically locate every asset. Use the barcode/QR scanner to scan each asset tag. Record the tag number, asset type, and physical location on the inventory checklist. If a tag is missing or unreadable, record the serial number manually. |
| 4 | Run the network discovery tool (e.g. Advanced IP Scanner) on the subnet assigned to the area. Export the results as a CSV file. Note each discovered device's IP address, MAC address, hostname, and device type. |
| 5 | Open the ITAM system. Cross-reference the physical scan results (Step 3) with the asset register and the network discovery results (Step 4). Identify: (a) assets found physically but not in the register (ghost assets); (b) assets in the register but not found physically (phantom assets); (c) assets found but with incorrect attributes (wrong location, serial number mismatch). |
| 6 | Document every discrepancy in the Reconciliation Log (use the provided template). For each discrepancy, record the asset ID (if known), the type of discrepancy, and the recommended action. |
| 7 | Update asset records in the ITAM system for discrepancies that can be resolved with certainty (e.g. update a location that has clearly changed). Flag records requiring further investigation for escalation. |
| 8 | Compile the Inventory Analysis Report using the structure in the Expected Outcome section. Present findings to the instructor and answer questions on your reconciliation decisions. |

---

## Hasil Jangkaan / Expected Outcome

A completed Inventory Analysis Report containing:

1. **Inventory Summary Table** — total assets found vs total in register, by category
2. **Reconciliation Log** — all discrepancies with type, description, and recommended action
3. **Ghost Asset List** — assets found but not in register, with recommended action (add to register / investigate)
4. **Phantom Asset List** — assets in register but not found, with recommended action (further search / write-off / lost report)
5. **Status Update Summary** — list of records updated in the ITAM system during the exercise
6. **Recommendations** — at least three process improvements to prevent future discrepancies

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Physical inventory conducted systematically using zone-based approach | [ ] Yes  [ ] No |
| 2 | All asset tags scanned or manually recorded | [ ] Yes  [ ] No |
| 3 | Network discovery tool used and results exported | [ ] Yes  [ ] No |
| 4 | Ghost and phantom assets correctly identified and documented | [ ] Yes  [ ] No |
| 5 | ITAM system records updated for resolvable discrepancies | [ ] Yes  [ ] No |
| 6 | Inventory Analysis Report complete with all six required sections | [ ] Yes  [ ] No |
| 7 | Recommendations are specific and evidence-based | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |