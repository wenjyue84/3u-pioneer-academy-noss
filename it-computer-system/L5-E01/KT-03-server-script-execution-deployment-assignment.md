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

## KERTAS TUGASAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/KT(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-03-server-script-execution-deployment-assignment

**TUJUAN:** Kertas rujukan untuk KT-03-server-script-execution-deployment-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(3/4) for guidance. This assignment is formative.

**Masa / Duration:** 1 hour 30 minutes

---

## Soalan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks)

**A1.** A PowerShell script works correctly when run interactively but fails when executed by Task Scheduler. The MOST LIKELY cause is:

- (a) The script contains syntax errors
- (b) The scheduled task is using a service account with a minimal environment, missing the user PATH or profile-loaded modules
- (c) Task Scheduler does not support PowerShell 7
- (d) The script is too long to run unattended

**A2.** The cron expression `0 2 1 * *` executes:

- (a) Every day at 02:01
- (b) At 02:00 on the first day of each month
- (c) Every 2 hours on day 1 of the week
- (d) At midnight every 2nd day of the month

**A3.** In Windows Task Scheduler, a `LastTaskResult` of **0** indicates:

- (a) The task has never run
- (b) The task is currently running
- (c) The task completed successfully
- (d) The task was disabled

**A4.** The systemd timer directive `Persistent=true` ensures that:

- (a) The timer runs continuously without stopping
- (b) If the scheduled execution was missed (e.g. server was offline), it runs as soon as the server comes back online
- (c) The service cannot be stopped manually
- (d) The timer logs all output permanently

**A5.** Before deploying a script to production, the pre-deployment checklist requires that:

- (a) The script has been tested only in the developer's local environment
- (b) The script has been tested in DEV and UAT; a change request has been approved; rollback procedure is documented
- (c) The script has been reviewed by the finance department
- (d) The script runs without parameters

**A6.** The FIRST step in a script rollback procedure is:

- (a) Restore the previous version from Git
- (b) Immediately disable the scheduled task or cron job to stop further executions
- (c) Delete the current script file from all servers
- (d) Contact the script author

**A7.** The PowerShell command to immediately trigger a scheduled task named `IT-DiskCheck` without waiting for its next scheduled time is:

- (a) `Invoke-ScheduledTask -Name "IT-DiskCheck"`
- (b) `Start-ScheduledTask -TaskName "IT-DiskCheck"`
- (c) `Run-ScheduledTask -TaskName "IT-DiskCheck"`
- (d) `Execute-ScheduledTask "IT-DiskCheck"`

**A8.** A deployment pipeline has THREE environments in order. What is the correct sequence?

- (a) Production → UAT → Development
- (b) UAT → Development → Production
- (c) Development → UAT → Production
- (d) Development → Production → UAT

**A9.** When adding a cron job for a service account named `svc-ops`, the CORRECT approach is:

- (a) Add the cron job to the root crontab for elevated access
- (b) Use `sudo crontab -u svc-ops -e` to edit the service account's crontab
- (c) Add the cron job to `/etc/cron.daily/` as any user
- (d) Create the cron job in the current user's crontab and use `sudo` in the command

**A10.** The `RandomizedDelaySec=300` directive in a systemd timer unit:

- (a) Delays the first run by exactly 5 minutes
- (b) Randomises the start time within a 5-minute window to prevent multiple timers triggering simultaneously
- (c) Adds 5 minutes to the execution time limit
- (d) Pauses the timer for 5 minutes after each run

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** Explain THREE (3) reasons why a script that works correctly in an interactive terminal session may fail when executed by a scheduler (Task Scheduler or cron). For each reason, describe a specific symptom and how it is resolved. (12 marks)

**B2.** Compare cron and systemd timers for scheduling server scripts on Linux. State at least THREE (3) differences relevant to production use, covering logging, dependency handling, and recovery from missed executions. (9 marks)

**B3.** State FIVE (5) items from the pre-deployment checklist that must be completed before a script is deployed to production. For each item, explain why it is required. (9 marks)

---

### Bahagian C: Soalan Esei / Essay (30 marks)

**C1.** At 08:15 on a Monday morning, the IT Operations team reports that no disk space report email was received this morning. The scheduled task `IT-DiskSpaceCheck-Daily` should have run at 06:00.

(a) Describe the complete Level 1 troubleshooting procedure you would follow to diagnose the failure. Include the exact PowerShell commands you would run and what specific output you would look for at each step. (15 marks)

(b) The investigation reveals that the script failed because the service account `CONTOSO\svc-monitoring` password expired over the weekend, causing the scheduled task to fail with error code `0x8007052E` (logon failure). Describe step by step how you would resolve this issue and prevent it recurring, including any long-term configuration changes. (8 marks)

(c) After resolving the issue, you are asked to improve the monitoring so that future failures are detected within 15 minutes rather than the next morning. Describe TWO (2) complementary monitoring approaches that would achieve this, and explain how they would be implemented. (7 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*