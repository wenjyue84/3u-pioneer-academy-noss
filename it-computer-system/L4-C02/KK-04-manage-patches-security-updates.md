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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/KK(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-manage-patches-security-updates

**TUJUAN:** Kertas rujukan untuk KK-04-manage-patches-security-updates.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Install and configure Windows Server Update Services (WSUS), approve patches for staged deployment, verify patch compliance on client systems, and maintain a patch register.

---

## Tempoh / Duration

4 hours

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Windows Server 2022 (WSUS server role to be installed) | 1 |
| 2 | Windows 11 workstation (WSUS client) | 1 |
| 3 | Group Policy Management Console (GPMC) | Pre-installed |
| 4 | Internet access (for WSUS synchronisation with Microsoft Update) | Available |
| 5 | Patch register template (blank) | 1 |
| 6 | Administrator credentials | Provided by instructor |

---

## Langkah Keselamatan / Safety Precautions

- Only approve patches in the designated training WSUS computer groups — do not modify production WSUS settings if shared infrastructure is used
- Take a VM snapshot of both server and workstation before applying any patches
- Ensure the workstation is not a critical shared resource before triggering patch installation
- Record the pre-patch state (current OS build number) before any updates are applied

---

## Prosedur / Procedures

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | **Record baseline.** On the Windows 11 workstation, open Settings → Windows Update → Update history. Record the current OS build number and the date of the last installed update. Run `Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10` in PowerShell and record the output. |
| 2 | **Install WSUS role.** On the Windows Server, open Server Manager → Add Roles and Features. Select Windows Server Update Services. Accept all dependencies. In the WSUS configuration wizard: choose to store updates locally at `C:\WSUS`; complete the post-installation task (configure WSUS). |
| 3 | **Configure WSUS synchronisation.** In the WSUS console, run the Configuration Wizard: sync from Microsoft Update (upstream server); select products: Windows 11 and Windows Server 2022; select classifications: Critical Updates, Security Updates, Definition Updates; set synchronisation schedule: daily at 03:00. Run an initial synchronisation manually and wait for it to complete (instructor may provide a pre-synced WSUS if bandwidth is limited). |
| 4 | **Create WSUS computer groups.** In the WSUS console under Computers → All Computers, create two groups: `Training-Test` and `Training-Production`. |
| 5 | **Configure Group Policy to point the workstation to WSUS.** Create a GPO named `Training-WSUS-Client` and link it to the Training OU. Configure: Specify intranet Microsoft update service location = `http://<wsus-server-hostname>:8530`; Configure Automatic Updates = 4 (auto download and schedule install); Scheduled install time = 03:00; Target Group = `Training-Test`. Apply the GPO to the workstation. Run `gpupdate /force` on the workstation to apply. |
| 6 | **Verify workstation reports to WSUS.** In the WSUS console, go to Computers → Training-Test. The workstation should appear within a few minutes (may require `wuauclt /detectnow` on the workstation). Confirm it is listed as a managed client. |
| 7 | **Approve updates for Testing group.** In WSUS, go to Updates → All Updates. Filter by: Approval = Unapproved, Status = Needed. Select three to five Critical or Important updates. Right-click → Approve → select Training-Test group → Approved for Install. |
| 8 | **Trigger update installation on the workstation.** On the Windows 11 workstation, run `wuauclt /detectnow /updatenow` or go to Settings → Windows Update → Check for updates. Monitor the WSUS console for the workstation's compliance status to change from Needed to Installed. |
| 9 | **Verify patch installation.** On the workstation, run `Get-HotFix -Id KB<number>` for each approved KB. Confirm all approved updates are listed as installed. Check Event Viewer → Windows Logs → System for any installation errors (Event ID 19 = update installed; Event ID 20 = installation failure). |
| 10 | **Complete the patch register.** For each approved and installed update, fill in the patch register: KB number, CVE reference (if applicable), severity, affected systems, date approved, date installed, verified by, status. Submit to instructor. |

---

## Hasil Jangkaan / Expected Outcome

- WSUS role installed and synchronised with Microsoft Update
- WSUS computer groups created; workstation successfully reporting to WSUS
- Updates approved for Training-Test group
- Updates installed on workstation and verified via PowerShell and WSUS reports
- No installation errors in Event Viewer
- Patch register completed for all approved updates

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Pre-patch baseline (build number, installed updates) recorded | [ ] Yes  [ ] No |
| 2 | WSUS role installed and post-installation task completed | [ ] Yes  [ ] No |
| 3 | WSUS synchronisation configured and initial sync completed | [ ] Yes  [ ] No |
| 4 | Computer groups created in WSUS console | [ ] Yes  [ ] No |
| 5 | GPO configured to point workstation to WSUS | [ ] Yes  [ ] No |
| 6 | Workstation visible in WSUS Training-Test group | [ ] Yes  [ ] No |
| 7 | Updates approved for Training-Test group | [ ] Yes  [ ] No |
| 8 | Updates installed and verified on workstation | [ ] Yes  [ ] No |
| 9 | Patch register completed with all required fields | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |