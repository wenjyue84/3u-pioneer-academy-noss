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
| NO. KOD | IT-020-5:2013-C02/KK(6/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-06-execute-secure-asset-disposal

**TUJUAN:** Kertas rujukan untuk KK-06-execute-secure-asset-disposal.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Process a set of end-of-life assets through the complete disposal workflow: classify disposal candidates, perform data destruction using approved software tools, prepare disposal documentation, and update the asset register to reflect completed disposals.

---

## Tempoh / Duration

6 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Laptop or workstation with ITAM system access | 1 |
| 2 | 3 training hard drives (HDDs — used, non-critical data) for data destruction practice | 3 |
| 3 | DBAN bootable USB or Blancco trial (for HDD wipe) | 1 |
| 4 | 1 training SSD for ATA Secure Erase practice | 1 |
| 5 | Simulated asset register with 8 disposal candidate records (provided by instructor) | 1 |
| 6 | Simulated repair quotations and technical assessment reports for the candidates | 1 set |
| 7 | Disposal Approval Form template (provided) | 1 |
| 8 | Data Destruction Certificate template (provided) | 1 |
| 9 | Simulated e-waste contractor licence (provided) | 1 |
| 10 | ITAM system access for record updates | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Handle all storage media with care; do not subject to physical shock or static discharge
- DBAN and secure erase tools permanently destroy all data — verify the correct drive is selected before initiating
- Do not perform physical destruction (shredding, disassembly) without explicit instructor approval and supervision
- Wear anti-static wrist strap when handling internal components
- Treat all simulated asset data as confidential

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Review the eight simulated disposal candidate records. For each asset, review the available evidence (age, repair quotation, technical assessment report). Apply the disposal trigger criteria from KP-06 Section 3 and confirm which assets qualify for disposal. Document your classification decision and the criteria met for each. |
| 2 | For assets that qualify, determine the data sensitivity classification for any storage media present (use the classification guide in KP-06 Section 5.1). Record the required destruction method for each: Clear, Purge, or Destroy. |
| 3 | Perform data destruction on the 3 training HDDs using DBAN (bootable USB): (a) Boot from the DBAN USB on the training workstation. (b) Select the target drive — verify the drive serial number matches the training drive before proceeding. (c) Select the "DoD Short" (3-pass) wipe method. (d) Initiate the wipe and wait for completion. (e) Record the completion time, drive serial number, and method used in the Data Destruction Certificate template. |
| 4 | Perform ATA Secure Erase on the 1 training SSD using the hdparm command (Linux live USB) or the manufacturer's secure erase tool: (a) Verify the drive is not frozen (hdparm -I /dev/sdX | grep frozen). (b) Set a temporary password (hdparm --security-set-pass p /dev/sdX). (c) Execute secure erase (hdparm --security-erase p /dev/sdX). (d) Verify completion; record in the Data Destruction Certificate. |
| 5 | Complete the Data Destruction Certificate for all destroyed media. Include: organisation name, asset ID, serial number, destruction method, standard applied, your name and signature, date, and instructor's witness signature. |
| 6 | Prepare the Disposal Approval Form for the confirmed disposal candidates. List all assets, their current book value (calculate from the depreciation schedule provided), the proposed disposal method for each (auction, donation, e-waste recycling, or destruction), and the estimated proceeds (if any). |
| 7 | Present the Disposal Approval Form to the instructor (acting as the approving authority). Answer any questions. Obtain the instructor's signature to simulate management approval. |
| 8 | Update the ITAM system for all approved disposed assets: change status to "Disposed", enter the disposal date, disposal method, and proceeds (if any). Remove the assets from the active register. |
| 9 | Compile the Disposal Report using the structure in the Expected Outcome section. Include confirmation that data destruction certificates are on file and that e-waste disposal (simulated) was conducted through a licensed contractor. |

---

## Hasil Jangkaan / Expected Outcome

1. **Disposal Candidate Classification Log** — criteria met documented for each of the 8 assets; confirm/reject disposal for each
2. **Data destruction completed** — 3 HDDs wiped (DBAN DoD Short); 1 SSD ATA Secure Erased
3. **Data Destruction Certificates** — completed for all 4 media items; signed by trainee and witnessed by instructor
4. **Disposal Approval Form** — all approved assets listed with disposal method, book value, and proposed proceeds; signed
5. **ITAM records updated** — all disposed assets show "Disposed" status with date and method
6. **Disposal Report** — complete summary for management review

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Disposal criteria applied correctly for all 8 candidates; decisions documented | [ ] Yes  [ ] No |
| 2 | Correct destruction method selected based on data sensitivity classification | [ ] Yes  [ ] No |
| 3 | DBAN wipe completed on 3 HDDs; drive serial numbers verified before wipe | [ ] Yes  [ ] No |
| 4 | ATA Secure Erase completed on SSD; completion verified | [ ] Yes  [ ] No |
| 5 | Data Destruction Certificates complete, signed, and witnessed | [ ] Yes  [ ] No |
| 6 | Disposal Approval Form complete and signed by instructor | [ ] Yes  [ ] No |
| 7 | ITAM records updated to "Disposed" with all required fields | [ ] Yes  [ ] No |
| 8 | Disposal Report compiled and complete | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |