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
| NO. KOD | IT-020-3:2013-C05/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-server-os-maintenance

**TUJUAN:** Kertas rujukan untuk KK-03-server-os-maintenance.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

By the end of this activity, the trainee will be able to:
1. Verify the current OS version, patch level, and installed services on a server.
2. Apply OS security patches and updates using the appropriate update mechanism.
3. Manage server services — identify unnecessary or stopped services, disable or restart as appropriate.
4. Perform disk maintenance including volume health checks, disk cleanup, and log file management.
5. Verify system event logs for critical errors and document findings.

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Server running Windows Server 2019/2022 or Linux (RHEL/Ubuntu Server) — lab unit | 1 |
| 2 | Administrator / root account credentials | 1 set |
| 3 | Network connection to update repository (Windows Update / yum / apt mirror) | 1 |
| 4 | OS maintenance checklist form | 1 |
| 5 | Snapshot / backup confirmation record | 1 |
| 6 | Computer workstation for remote access (RDP / SSH client) | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Always take a VM snapshot or full backup before applying patches. If the server is physical and not virtualised, confirm that a recent backup exists and is restorable before proceeding.
- Apply patches only during the approved maintenance window. Patching a production server outside the approved window may violate organisational change control policy.
- Do not reboot a server during a maintenance window unless it has been pre-approved; confirm with the instructor before issuing any reboot command.
- Do not disable services without identifying their dependencies. Disabling a dependent service may cause other applications to fail.
- Use the principle of least privilege — do not perform routine maintenance tasks as root/Administrator unless required; escalate only when necessary.
- Keep a record of every change made so that actions can be reversed if an issue arises.

---

## Prosedur / Procedure

| Langkah / Step | Arahan / Instruction |
|----------------|----------------------|
| 1 | Connect to the server via Remote Desktop Protocol (RDP) for Windows Server, or SSH for Linux. Confirm you are on the correct server by verifying the hostname and IP address against the job order. |
| 2 | **Verify OS details:** On Windows Server, open PowerShell and run `Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber`. On Linux, run `cat /etc/os-release` and `uname -r`. Record the OS name, version, and current kernel/build number. |
| 3 | **Check current patch level:** On Windows Server, run `Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10` to list the 10 most recently applied patches. On Linux (RHEL/CentOS), run `rpm -qa --last | head -20`; on Ubuntu, run `grep " install " /var/log/dpkg.log | tail -20`. Record the date of the last applied patch. |
| 4 | **Take a backup/snapshot:** Confirm with the instructor that a VM snapshot or backup has been taken. Record the snapshot name and timestamp on the maintenance checklist before proceeding with any changes. |
| 5 | **Apply OS updates (Windows Server):** Open PowerShell as Administrator and run `Install-WindowsUpdate -AcceptAll -AutoReboot:$false` (requires PSWindowsUpdate module), or open Windows Update via Server Manager and click "Check for updates". Install all critical and security updates. Do NOT reboot yet — note updates that require a reboot. |
| 5a | **Apply OS updates (Linux — RHEL/CentOS):** Run `sudo yum check-update` to list available updates. Apply security updates with `sudo yum update --security -y`. For Ubuntu, run `sudo apt update && sudo apt upgrade -y`. Record the number and nature of packages updated. |
| 6 | **Service audit:** On Windows Server, open PowerShell and run `Get-Service | Where-Object {$_.Status -eq "Stopped"} | Select-Object Name, DisplayName, StartType`. Review stopped services and identify any that should be running (e.g., Windows Time, Print Spooler if required). On Linux, run `systemctl list-units --type=service --state=failed` to list failed services. |
| 7 | **Restart a stopped critical service:** If a required service is found stopped, restart it using `Start-Service -Name <ServiceName>` (Windows) or `sudo systemctl start <service-name>` (Linux). Verify the service is now running. Record the service name, previous state, and action taken. |
| 8 | **Disk health and space check:** On Windows Server, open PowerShell and run `Get-PSDrive -PSProvider FileSystem` to review disk usage. Flag any volume above 80% utilisation. On Linux, run `df -h` and flag any filesystem above 80% usage. |
| 9 | **Disk cleanup (Windows Server):** Open Disk Cleanup (`cleanmgr.exe`), select the system drive, and remove temporary files, Windows Update cache, and recycle bin contents. Alternatively, use PowerShell: `Remove-Item -Path "C:\Windows\Temp\*" -Recurse -Force -ErrorAction SilentlyContinue`. On Linux, clear old journal logs with `sudo journalctl --vacuum-time=30d` and remove old package cache with `sudo yum clean all` / `sudo apt clean`. |
| 10 | **Log file review:** On Windows Server, open Event Viewer (`eventvwr.msc`). Navigate to Windows Logs > System and Windows Logs > Application. Filter for events with Level = Critical or Error from the past 7 days. Record each unique Event ID, source, and description. On Linux, run `sudo grep -i "error\|critical\|fail" /var/log/messages | tail -50` (RHEL) or `sudo journalctl -p err -n 50` (Ubuntu). |
| 11 | **Reboot (if required and approved):** If patches require a reboot and the reboot has been pre-approved in the maintenance window, reboot the server now. On Windows Server: `Restart-Computer -Force`. On Linux: `sudo reboot`. Monitor the console until the server completes the boot cycle and OS login is available. |
| 12 | After reboot (or after completing all tasks without reboot), re-verify OS version and patch level to confirm updates were applied successfully. Re-run the disk space check to confirm cleanup was effective. |
| 13 | Complete the OS maintenance checklist form: record the pre- and post-patch levels, services restarted, disk space before and after cleanup, and any critical event log entries found. Submit to the instructor. |

---

## Hasil Dijangka / Expected Outcome

Upon completing this activity, the trainee will have:
- Confirmed and documented the server's OS version and patch level before and after maintenance.
- Applied all available security and critical OS updates.
- Identified and restarted any stopped critical services.
- Freed disk space through targeted cleanup of temporary and cached files.
- Reviewed event logs and documented all critical/error events found.
- Produced a completed OS maintenance checklist.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Correct server verified (hostname and IP match job order) | [ ] Yes  [ ] No |
| 2 | OS version and current patch level recorded before making changes | [ ] Yes  [ ] No |
| 3 | Backup / snapshot confirmed and recorded before applying updates | [ ] Yes  [ ] No |
| 4 | OS updates applied; number and type of updates recorded | [ ] Yes  [ ] No |
| 5 | Stopped/failed services identified and appropriate action taken | [ ] Yes  [ ] No |
| 6 | Disk utilisation checked; volumes above 80% flagged | [ ] Yes  [ ] No |
| 7 | Disk cleanup performed; space freed is recorded | [ ] Yes  [ ] No |
| 8 | Event logs reviewed; critical/error events documented | [ ] Yes  [ ] No |
| 9 | Post-update patch level verified to confirm successful application | [ ] Yes  [ ] No |
| 10 | OS maintenance checklist completed and submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |