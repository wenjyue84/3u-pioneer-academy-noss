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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/KK(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-executing-deploying-server-scripts

**TUJUAN:** Kertas rujukan untuk KK-03-executing-deploying-server-scripts.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Configure scheduled execution for the scripts developed in KK(2/4), deploy them to the training server environment, verify correct operation through log inspection, and demonstrate a complete rollback procedure.

---

## Tempoh / Duration

8 hours (spread across sessions as directed by instructor)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Windows training server (Windows Server 2022, PowerShell 7 installed) | 1 (shared or VM) |
| 2 | Linux training server (Ubuntu 22.04 LTS) | 1 (shared or VM) |
| 3 | Management workstation with network access to both training servers | 1 per trainee |
| 4 | Git client with training repository cloned | 1 per trainee |
| 5 | Pre-deployment checklist form (from KP(3/4)) | 1 |
| 6 | Simulated SMTP test relay (Mailtrap or local Postfix) | 1 (shared) |

---

## Langkah Keselamatan / Safety Precautions

- Only use the designated training servers — do not run scripts on production systems
- Confirm all scripts have a dry-run mode tested before live execution
- Do not register scheduled tasks or cron jobs as the Administrator/root account — use the designated training service account
- Revert all changes at the end of the session as directed by the instructor

---

## Bahagian A — Windows: Schedule and Deploy with Task Scheduler

### Scenario
Deploy `Get-LocalUserAudit.ps1` to the Windows training server and configure it to run daily at 07:00 as the training service account.

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| A1 | On the management workstation, complete the **pre-deployment checklist** from KP(3/4) Section 4.2 for `Get-LocalUserAudit.ps1`. Obtain instructor sign-off before proceeding. |
| A2 | Copy the script to the Windows training server using the deployment script pattern from KP(3/4) Section 4.3: `Copy-Item -Path .\scripts\windows\Get-LocalUserAudit.ps1 -Destination "\\TrainingServer01\C$\Scripts\"`. Verify the file exists on the target. |
| A3 | Verify the script runs correctly in an **interactive non-admin session** first: `pwsh -NonInteractive -ExecutionPolicy Bypass -File "C:\Scripts\Get-LocalUserAudit.ps1" -ComputerList @('localhost') -OutputPath "C:\Temp\audit_test.csv" -Verbose`. Inspect the CSV output and log file. |
| A4 | Register the scheduled task using the PowerShell code from KP(3/4) Section 2.1. Substitute `Get-LocalUserAudit.ps1` for the disk check script. Set trigger to daily 07:00. Record the full `Register-ScheduledTask` command used in your work log. |
| A5 | Manually trigger the task immediately: `Start-ScheduledTask -TaskName "IT-UserAudit-Daily"`. Wait 30 seconds. |
| A6 | Verify execution: `Get-ScheduledTaskInfo -TaskName "IT-UserAudit-Daily"`. Record `LastRunTime` and `LastTaskResult`. A result of 0 indicates success. |
| A7 | Inspect the log file: `Get-Content "C:\Logs\UserAudit_$(Get-Date -Format 'yyyyMMdd').log"`. Confirm log entries are present and no ERROR lines appear. |
| A8 | **Simulate a failure scenario**: temporarily rename the output directory so it does not exist. Trigger the task again. Observe that exit code is 1 and the failure is logged. Restore the directory. |
| A9 | **Practise rollback**: disable the task, restore the previous script version from Git tag `v1.0.0` (instructor will provide the tag), redeploy, and re-enable the task. Record all commands used. |

---

## Bahagian B — Linux: Schedule and Deploy with Cron and systemd Timer

### Scenario
Deploy `cleanup_tmp.sh` to the Linux training server. Configure it to run via cron and also as a systemd timer. Compare the two approaches.

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| B1 | Connect to the Linux training server via SSH as the training user. Verify the script directory exists: `ls /opt/scripts/`. |
| B2 | Copy the script from your repository to the server: `scp scripts/linux/cleanup_tmp.sh trainee@linuxserver01:/opt/scripts/`. Set correct permissions: `sudo chmod 750 /opt/scripts/cleanup_tmp.sh && sudo chown svc-monitoring:svc-monitoring /opt/scripts/cleanup_tmp.sh`. |
| B3 | Test the script manually as the service account: `sudo -u svc-monitoring /opt/scripts/cleanup_tmp.sh /tmp/app-test 5 1 monitor@training.local`. Create some test files first: `for i in {1..10}; do dd if=/dev/zero of=/tmp/app-test/testfile$i.tmp bs=1M count=100; done`. |
| B4 | Inspect the log: `cat /var/log/cleanup_tmp_$(date +%Y%m%d).log`. Verify deleted file entries and correct size totals. |
| B5 | Add a **cron job** for the service account to run the script nightly at 23:00: `sudo crontab -u svc-monitoring -e`. Add the entry: `0 23 * * * /opt/scripts/cleanup_tmp.sh /var/app/tmp 120 5 infra@prisma.com >> /var/log/cron-cleanup.log 2>&1`. |
| B6 | Verify the crontab was saved correctly: `sudo crontab -u svc-monitoring -l`. |
| B7 | Create the **systemd service and timer files** from the templates in KP(3/4) Section 3.3 (adapted for `cleanup_tmp.sh`). Write `/etc/systemd/system/cleanup-tmp.service` and `/etc/systemd/system/cleanup-tmp.timer`. |
| B8 | Enable and start the systemd timer: `sudo systemctl daemon-reload && sudo systemctl enable --now cleanup-tmp.timer`. Verify: `sudo systemctl list-timers cleanup-tmp.timer`. |
| B9 | Trigger the systemd service manually for testing: `sudo systemctl start cleanup-tmp.service`. Check result: `sudo journalctl -u cleanup-tmp.service --since "5 minutes ago"`. |
| B10 | **Compare** the cron and systemd approaches in your work log: note at least THREE (3) differences regarding logging, dependency handling, and failure notification. |
| B11 | **Practise rollback** for the cron job: comment out the cron entry, restore the previous script version from Git, redeploy, and re-enable. |

---

## Bahagian C — Multi-Server Deployment

### Scenario
Deploy `disk_report.py` to the management workstation and configure it to run against the training Linux servers, producing a daily JSON report.

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| C1 | Ensure SSH key-based authentication is configured from the management workstation to both training Linux servers for the `monitor` user. Test: `ssh monitor@linuxserver01 "echo OK"`. |
| C2 | Create a hosts file `config/training_hosts.txt` with the training server FQDNs (one per line). Commit to repository. |
| C3 | Run `disk_report.py` in test mode: `python3 scripts/python/disk_report.py --hosts config/training_hosts.txt --output /tmp/disk_report_test.json --threshold 80 --log /tmp/disk_report.log`. Inspect the JSON output. |
| C4 | Verify the JSON structure is correct: `python3 -m json.tool /tmp/disk_report_test.json`. Confirm `generated_at`, `total_filesystems`, `flagged`, and `results` fields are present. |
| C5 | Configure a cron job on the management workstation to run the disk report daily at 06:30: `crontab -e`. Add: `30 6 * * * python3 /opt/scripts/disk_report.py --hosts /opt/config/training_hosts.txt --output /var/reports/disk_$(date +\%Y\%m\%d).json --log /var/log/disk_report.log`. |
| C6 | Simulate a server failure: stop the SSH service on one training server. Run the script again. Verify the unreachable server appears in the JSON report with `"status": "unreachable"` and the script does not crash. |
| C7 | Record the total deployment procedure as a numbered list in your work log (suitable for inclusion in an Operational Runbook). |

---

## Hasil Jangkaan / Expected Outcome

- `Get-LocalUserAudit.ps1` scheduled and verified running on Windows training server; rollback demonstrated
- `cleanup_tmp.sh` deployed via both cron and systemd timer; cron vs systemd comparison written
- `disk_report.py` running against multiple training Linux servers; partial-failure handling demonstrated
- All deployment steps recorded in work log

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Pre-deployment checklist completed and signed off before Windows deployment | [ ] Yes  [ ] No |
| 2 | Scheduled task registered on Windows server with correct trigger and service account | [ ] Yes  [ ] No |
| 3 | Task manually triggered; LastTaskResult verified as 0 | [ ] Yes  [ ] No |
| 4 | Failure scenario simulated and logged; exit code 1 confirmed | [ ] Yes  [ ] No |
| 5 | Windows rollback demonstrated from Git tag | [ ] Yes  [ ] No |
| 6 | Linux script deployed with correct permissions (750, owned by svc-monitoring) | [ ] Yes  [ ] No |
| 7 | Cron job entry correct (time, command, redirect) | [ ] Yes  [ ] No |
| 8 | systemd service and timer files created and enabled | [ ] Yes  [ ] No |
| 9 | Cron vs systemd comparison written (at least 3 differences) | [ ] Yes  [ ] No |
| 10 | Python disk report run against multiple hosts; JSON output valid | [ ] Yes  [ ] No |
| 11 | Unreachable server handled gracefully in JSON output | [ ] Yes  [ ] No |
| 12 | Deployment procedure recorded as Runbook-ready numbered list | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |