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
| NO. KOD | IT-020-5:2013-C02/KK(4/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-evaluate-and-configure-asset-management-system

**TUJUAN:** Kertas rujukan untuk KK-04-evaluate-and-configure-asset-management-system.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Evaluate two ITAM software platforms against an organisation's requirements, configure the selected platform with a sample dataset, and demonstrate key ITAM workflows including asset creation, discovery import, licence tracking, and report generation.

---

## Tempoh / Duration

6 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Laptop or workstation with internet access | 1 |
| 2 | Snipe-IT (demo instance or local Docker install) | 1 |
| 3 | GLPI (demo instance or local install with FusionInventory) | 1 |
| 4 | Simulated organisational requirements document (provided by instructor) | 1 |
| 5 | Sample asset dataset — 20 records in CSV format (provided) | 1 |
| 6 | Sample software licence data — 5 products (provided) | 1 |
| 7 | ITAM System Evaluation Scoresheet (provided) | 1 |
| 8 | Network discovery scan result (simulated CSV, provided) | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Use only training/demo instances; do not enter real organisational data into public demo environments
- Do not modify system settings that could affect other trainees sharing the demo environment
- Log out of all systems at the end of the session

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Read the organisational requirements document. Extract the ten functional requirements listed and enter them into the ITAM System Evaluation Scoresheet. Assign a weighting to each requirement based on the organisation's stated priorities (total weightings must sum to 100%). |
| 2 | Log into the Snipe-IT demo instance. Explore the following modules: Asset List, Asset Categories, Asset Models, Licences, Users, Reports. Record your observations in the scoresheet for each of the ten requirements. Score each requirement 1–5 (1 = does not meet, 5 = fully meets). |
| 3 | Log into the GLPI demo instance. Explore the same functional areas: Computer inventory, Software, Licences, Contracts, Reports. Record and score against the same ten requirements. |
| 4 | Calculate the weighted score for each platform: multiply each criterion score by its weighting, then sum to produce a total out of 100. Determine the recommended platform based on the weighted scores. Document your recommendation with justification. |
| 5 | In the recommended platform (Snipe-IT or GLPI as determined in Step 4), configure the following: (a) Create 3 asset categories: Desktop PC, Laptop, Network Switch. (b) Create 2 asset statuses: Active, In Repair. (c) Create 3 user accounts with different roles: Admin, Asset Manager, Read-Only. (d) Import the 20-record sample dataset using the CSV import function. Resolve any import errors. |
| 6 | Manually create one asset record that represents a newly received laptop. Fill in all mandatory fields including: asset tag, serial number, model, category, status, assigned user, location, purchase date, and purchase cost. |
| 7 | Import the simulated network discovery scan result (CSV) into the platform. Identify any discovered devices that are not already in the asset register. Create asset records for two of them and flag the remainder for further investigation. |
| 8 | Add the five software licence records to the platform. For each licence, record: product name, manufacturer, licence type, number of seats, and expiry date. Assign at least two licences to assets in the register. Generate the licence compliance report and review the output. |
| 9 | Generate three standard reports: (a) Asset Status Summary; (b) Assets assigned to a specific department; (c) Assets with purchase date older than 4 years. Export each report as CSV or PDF. |
| 10 | Compile an ITAM System Evaluation Report summarising: the evaluation scores, the recommendation, configuration steps completed, and any limitations or issues encountered. |

---

## Hasil Jangkaan / Expected Outcome

1. **Completed Evaluation Scoresheet** — weighted scores for both platforms; recommendation with justification
2. **Configured ITAM platform** — categories, statuses, users, and 20 imported assets correctly set up
3. **Manually created asset record** — all mandatory fields complete
4. **Discovery reconciliation** — discovered devices matched or flagged
5. **Licence records** — five licences entered; compliance report generated
6. **Three exported reports** — as CSV or PDF
7. **ITAM System Evaluation Report** — summary of evaluation process and findings

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Evaluation scoresheet completed for both platforms with weighted scores | [ ] Yes  [ ] No |
| 2 | Platform recommendation justified with reference to scores and requirements | [ ] Yes  [ ] No |
| 3 | Asset categories, statuses, and user roles configured correctly | [ ] Yes  [ ] No |
| 4 | 20-record CSV imported successfully; import errors resolved | [ ] Yes  [ ] No |
| 5 | Manual asset record complete with all mandatory fields | [ ] Yes  [ ] No |
| 6 | Discovery results reconciled; new records created for unmatched devices | [ ] Yes  [ ] No |
| 7 | Software licences entered; compliance report generated | [ ] Yes  [ ] No |
| 8 | Three reports generated and exported | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |