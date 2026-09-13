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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C04 DISASTER RECOVERY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE DISASTER RECOVERY REQUIREMENTS<br>2. DEVELOP DISASTER RECOVERY MANAGEMENT PLAN<br>3. IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN<br>4. PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C04/KK(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-developing-disaster-recovery-plan

**TUJUAN:** Kertas rujukan untuk KK-02-developing-disaster-recovery-plan.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
**TUJUAN:** Develop a structured Disaster Recovery Plan (DRP) document for a given organisation, including DR strategy selection, backup plan, DR team structure, and recovery procedures.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

---

## Objektif / Objective

Produce a complete Disaster Recovery Plan document for the organisation introduced in KK(1/4), incorporating the BIA findings, appropriate DR strategy, backup and replication plan, DR team structure, and documented recovery procedures.

---

## Tempoh / Duration

4 hours (distributed across WA2 practical sessions)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Completed DR Requirements Report from KK(1/4) | 1 |
| 2 | DRP template document | 1 |
| 3 | DR strategy comparison reference card | 1 |
| 4 | Backup schedule planning worksheet | 1 |
| 5 | DR team role card set | 1 set |
| 6 | Computer with word processing software | 1 |

---

## Langkah Keselamatan / Safety Precautions

- All DRP documents contain sensitive infrastructure information — treat as confidential
- Do not use actual production credentials or real IP addresses in training documents; use simulated values
- All digital copies must be stored in the designated training folder with appropriate access control

---

## Senario / Scenario

Continuing from KK(1/4): **Syarikat Logistik Sejahtera Sdn. Bhd.**

Management has approved a DR investment budget of RM 350,000 for the first year, with an annual maintenance budget of RM 80,000. The company has obtained a contract for colocation space at a Tier 3 data centre in Cyberjaya. Management priorities:

- WMS and TMS must be recoverable within 4 hours (Tier 1)
- ERP must be recoverable within 24 hours (Tier 2)
- Email server within 48 hours (Tier 3)
- CCTV and HR portal within 1 week (Tier 4)

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Review the DR Requirements Report from KK(1/4). Confirm system tiers and RTO/RPO targets before proceeding. |
| 2 | Select the appropriate DR strategy (hot site, warm site, cold site, or cloud DR) for each system tier. Justify your selection referencing budget constraints and RTO/RPO targets. Document in Section 7 of the DRP template. |
| 3 | Design the backup and replication plan. For each Tier 1 and Tier 2 system, specify: backup type (full/incremental/differential), replication method (synchronous/asynchronous/log shipping), backup frequency, retention period, and offsite storage method. Use the GFS rotation scheme for at least one system. Document in Section 8 of the DRP template. |
| 4 | Define the DR team structure for Syarikat Logistik Sejahtera. Assign at least SIX (6) roles from the KP(2/4) reference. For each role, specify: name/position, primary responsibilities, and contact information (use simulated names). Create an escalation procedure with minimum 3 alert levels. Document in Section 4 of the DRP template. |
| 5 | Write the DRP Activation Procedure (Section 9). Define: who has authority to declare a disaster, what conditions trigger activation, and the first 10 actions after activation in chronological order. |
| 6 | Write Recovery Procedures (Section 10) for the WMS (Tier 1 system). The procedures must be in step-by-step format (numbered), technically specific, and achievable within the stated RTO of 4 hours. Minimum 12 steps. |
| 7 | Write the Communication Plan (Section 12). Define internal and external communication channels, message templates for staff notification and customer notification, and the designated spokesperson. |
| 8 | Complete the DRP cover page, version history table, and approval signature block. Submit the completed DRP document to the instructor. |

---

## Hasil Jangkaan / Expected Outcome

A completed DRP document (minimum 8 pages) containing:
- DR strategy selection with justification for each system tier
- Backup and replication plan covering all Tier 1 and Tier 2 systems
- DR team structure with minimum 6 defined roles
- Escalation procedure with minimum 3 alert levels
- DRP activation procedure (minimum 10 steps)
- Detailed recovery procedures for WMS (minimum 12 steps)
- Communication plan with staff and customer message templates
- Completed cover page, version history, and approval block

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | DR strategy selected and justified for each system tier within budget | [ ] Yes  [ ] No |
| 2 | Backup plan specifies type, frequency, retention, and offsite storage for all Tier 1 and 2 systems | [ ] Yes  [ ] No |
| 3 | Replication method appropriate to RPO requirements | [ ] Yes  [ ] No |
| 4 | DR team structure with minimum 6 roles; escalation procedure with 3 levels | [ ] Yes  [ ] No |
| 5 | DRP activation procedure: authority, trigger conditions, first 10 actions documented | [ ] Yes  [ ] No |
| 6 | WMS recovery procedures: step-by-step, minimum 12 steps, technically specific | [ ] Yes  [ ] No |
| 7 | Communication plan: internal and external channels; message templates present | [ ] Yes  [ ] No |
| 8 | DRP document properly formatted with cover page, version history, and approval block | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |