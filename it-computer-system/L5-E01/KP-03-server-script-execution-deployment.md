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

## KERTAS PENERANGAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Create a scheduled task to run DiskCheck.ps1 daily at 06:00

**TUJUAN:** $taskName    = "IT-DiskSpaceCheck-Daily" $taskDesc    = "Checks disk space on all servers and emails a report" $scriptPath  = "C:\Scripts\Check-DiskSpace.ps1" $logPath     = "C:\Logs\taskscheduler-diskcheck.log" $serviceAcct = "CONTOSO\svc-monitoring"   # Dedicated service account

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Configure scheduled execution of server scripts using Windows Task Scheduler and Linux cron
2. Deploy scripts across server environments using structured deployment procedures
3. Implement runtime monitoring, logging verification, and alerting for deployed scripts
4. Apply rollback procedures when a deployed script fails in production

---

## 1.0 Execution Environments

Before deployment, the practitioner must understand the execution environment in which the script will run. This differs from an interactive terminal session in important ways:

| Aspect | Interactive Session | Scheduled/Automated Execution |
|--------|--------------------|---------------------------------|
| Working directory | Current user's home or chosen directory | Defined by scheduler; often system root |
| Environment variables | Full user environment | Minimal system environment (no user PATH) |
| Credentials | Current logged-in user | Service account or stored credential |
| Output | Console (stdout/stderr) | Redirected to log file or discarded |
| Error visibility | Immediate | Visible only in logs or alerts |

**Consequence:** Scripts that work interactively often fail when scheduled because they rely on user environment variables or interactive prompts. All scripts must be tested in a non-interactive context before production deployment.

---

## 2.0 Scheduled Execution — Windows Task Scheduler

### 2.1 Creating a Scheduled Task via PowerShell

The preferred method for production environments is to create tasks programmatically so they are reproducible and version-controllable:

```powershell
# Create a scheduled task to run DiskCheck.ps1 daily at 06:00
# Run this once on the management server as Administrator

$taskName    = "IT-DiskSpaceCheck-Daily"
$taskDesc    = "Checks disk space on all servers and emails a report"
$scriptPath  = "C:\Scripts\Check-DiskSpace.ps1"
$logPath     = "C:\Logs\taskscheduler-diskcheck.log"
$serviceAcct = "CONTOSO\svc-monitoring"   # Dedicated service account

# Build the action — use pwsh.exe for PowerShell 7
$action  = New-ScheduledTaskAction `
    -Execute "C:\Program Files\PowerShell\7\pwsh.exe" `
    -Argument "-NonInteractive -ExecutionPolicy Bypass -File `"$scriptPath`" -SmtpServer smtp.contoso.com -ReportRecipient itmanager@contoso.com" `
    -WorkingDirectory "C:\Scripts"

# Daily trigger at 06:00
$trigger = New-ScheduledTaskTrigger -Daily -At "06:00"

# Run as service account; does not require user to be logged on
$principal = New-ScheduledTaskPrincipal `
    -UserId $serviceAcct `
    -LogonType Password `
    -RunLevel Highest

# Settings: restart on failure (3 attempts, 5 min apart); kill if runs > 30 min
$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 30) `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 5) `
    -StartWhenAvailable `
    -RunOnlyIfNetworkAvailable

$task = New-ScheduledTask -Action $action -Trigger $trigger `
            -Principal $principal -Settings $settings -Description $taskDesc

Register-ScheduledTask -TaskName $taskName -InputObject $task -Force

Write-Host "Scheduled task '$taskName' registered successfully."
```

### 2.2 Verifying and Testing a Scheduled Task

```powershell
# View the registered task
Get-ScheduledTask -TaskName "IT-DiskSpaceCheck-Daily" | Select-Object *

# Manually trigger the task to verify it works non-interactively
Start-ScheduledTask -TaskName "IT-DiskSpaceCheck-Daily"

# Wait and check last run result (0 = success; non-zero = failure)
Start-Sleep -Seconds 15
$taskInfo = Get-ScheduledTaskInfo -TaskName "IT-DiskSpaceCheck-Daily"
Write-Host "Last Run Time  : $($taskInfo.LastRunTime)"
Write-Host "Last Result    : $($taskInfo.LastTaskResult)"  # 0 = success

# Check the script's own log file to verify output
Get-Content "C:\Logs\DiskCheck_$(Get-Date -Format 'yyyyMMdd').log" -Tail 20
```

---

## 3.0 Scheduled Execution — Linux Cron

### 3.1 Cron Syntax

Cron schedules are defined by a five-field time expression:

```
┌─── minute (0–59)
│  ┌─── hour (0–23)
│  │  ┌─── day of month (1–31)
│  │  │  ┌─── month (1–12 or Jan–Dec)
│  │  │  │  ┌─── day of week (0–7; 0 and 7 = Sunday)
│  │  │  │  │
*  *  *  *  *  /path/to/command
```

**Common cron expressions:**

| Expression | Meaning |
|------------|---------|
| `0 6 * * *` | Every day at 06:00 |
| `0 0 * * 0` | Every Sunday at midnight |
| `*/15 * * * *` | Every 15 minutes |
| `0 2 1 * *` | First day of each month at 02:00 |
| `0 6,18 * * 1-5` | Weekdays at 06:00 and 18:00 |

### 3.2 Creating and Managing Cron Jobs

```bash
# View current user's crontab
crontab -l

# Edit crontab for the monitoring service account
# Always use 'sudo crontab -u <user> -e' for service accounts
sudo crontab -u svc-monitoring -e

# --- Contents to add inside the crontab editor ---
# Environment variables (set PATH explicitly — cron has minimal PATH)
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=""    # Suppress default mail; we handle logging ourselves

# Daily 06:00 — log backup
0 6 * * * /opt/scripts/backup_logs.sh /var/log/appserver /mnt/backup/logs >> /var/log/cron-backup.log 2>&1

# Every 5 minutes — service health check
*/5 * * * * /opt/scripts/service_health_check.sh >> /var/log/cron-health.log 2>&1

# Weekly Sunday 02:00 — full system report
0 2 * * 0 /opt/scripts/weekly_report.sh >> /var/log/cron-weekly.log 2>&1
```

### 3.3 Systemd Timers (Modern Alternative to Cron)

On modern Linux distributions (RHEL 8+, Ubuntu 20.04+), systemd timers are preferred over cron for production scripts because they integrate with journald logging, support dependency ordering, and restart failed services.

```ini
# /etc/systemd/system/disk-backup.service
[Unit]
Description=Daily disk backup service
After=network.target

[Service]
Type=oneshot
User=svc-monitoring
ExecStart=/opt/scripts/backup_logs.sh /var/log/appserver /mnt/backup/logs
StandardOutput=journal
StandardError=journal
SyslogIdentifier=disk-backup
```

```ini
# /etc/systemd/system/disk-backup.timer
[Unit]
Description=Daily disk backup timer
Requires=disk-backup.service

[Timer]
OnCalendar=*-*-* 06:00:00
Persistent=true     # Run immediately if last scheduled execution was missed
RandomizedDelaySec=300  # Randomise start within 5 minutes to avoid thundering herd

[Install]
WantedBy=timers.target
```

```bash
# Enable and start the timer
sudo systemctl daemon-reload
sudo systemctl enable --now disk-backup.timer

# Verify timer status
sudo systemctl list-timers disk-backup.timer

# Check service execution logs
sudo journalctl -u disk-backup.service --since "1 day ago"
```

---

## 4.0 Deployment Procedures

### 4.1 Deployment Environments

Scripts must pass through a staged deployment pipeline before reaching production:

| Environment | Purpose | Who Can Deploy |
|-------------|---------|----------------|
| Development (DEV) | Script author writes and unit tests | Script developer |
| User Acceptance Testing (UAT) | Testing on representative infrastructure | Senior IT staff |
| Production (PROD) | Live execution on production servers | Approved by Change Manager |

### 4.2 Pre-Deployment Checklist

Before deploying any script to production:

- [ ] Script tested successfully in DEV and UAT environments
- [ ] Dry-run (`-WhatIf` / `--dry-run`) executed without errors
- [ ] All hardcoded values replaced with parameters or configuration files
- [ ] Credentials stored in Credential Manager / vault (not in script)
- [ ] Git commit tagged with version number (e.g. `v1.0.0`)
- [ ] Peer review completed
- [ ] Change request approved by Change Advisory Board (CAB)
- [ ] Rollback procedure documented
- [ ] Deployment time window agreed (not during business-critical hours)

### 4.3 Deployment Script Example

```powershell
# Deploy-Script.ps1 — Deploys a PowerShell script to multiple target servers
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)][string]$ScriptName,
    [Parameter(Mandatory)][string[]]$TargetServers,
    [Parameter(Mandatory)][string]$SourcePath,
    [string]$DestinationPath = "C:\Scripts"
)

$ErrorActionPreference = 'Stop'
$results = @()

foreach ($server in $TargetServers) {
    try {
        $dest = "\\$server\C$\Scripts"

        if (-not (Test-Path $dest)) {
            if ($PSCmdlet.ShouldProcess($dest, 'Create directory')) {
                New-Item -Path $dest -ItemType Directory -Force | Out-Null
            }
        }

        $sourceFile = Join-Path $SourcePath $ScriptName
        $destFile   = Join-Path $dest $ScriptName

        if ($PSCmdlet.ShouldProcess($destFile, "Copy $sourceFile")) {
            Copy-Item -Path $sourceFile -Destination $destFile -Force
        }

        $results += [PSCustomObject]@{ Server = $server; Status = 'Deployed'; Error = $null }
        Write-Host "[OK] Deployed to $server"
    }
    catch {
        $results += [PSCustomObject]@{ Server = $server; Status = 'Failed'; Error = $_.Exception.Message }
        Write-Warning "[FAIL] $server`: $($_.Exception.Message)"
    }
}

$results | Format-Table -AutoSize
$failed = $results | Where-Object { $_.Status -eq 'Failed' }
if ($failed) { exit 1 } else { exit 0 }
```

---

## 5.0 Runtime Monitoring and Log Verification

After deployment, the practitioner must verify that scripts are executing correctly:

### 5.1 Log Monitoring — PowerShell

```powershell
# Monitor a log file in real-time (equivalent to 'tail -f' on Linux)
Get-Content "C:\Logs\DiskCheck_$(Get-Date -Format 'yyyyMMdd').log" -Wait -Tail 50

# Search for ERROR entries in all today's logs
Get-ChildItem "C:\Logs\*$(Get-Date -Format 'yyyyMMdd')*.log" |
    Select-String -Pattern 'ERROR|FATAL|WARN' |
    Format-Table Filename, LineNumber, Line -AutoSize

# Count success vs failure across multiple log files
$logFiles = Get-ChildItem "C:\Logs\DiskCheck_*.log"
$logFiles | ForEach-Object {
    $content = Get-Content $_.FullName
    [PSCustomObject]@{
        File    = $_.Name
        Success = ($content | Select-String 'Script started').Count
        Errors  = ($content | Select-String 'ERROR|FATAL').Count
    }
} | Format-Table -AutoSize
```

### 5.2 Log Monitoring — Bash

```bash
# Real-time log monitoring
tail -f /var/log/cron-backup.log

# Search for errors in last 7 days of logs
grep -r "ERROR\|FATAL\|WARN" /var/log/cron-*.log | \
    awk -F: '{print $1}' | sort | uniq -c | sort -rn

# Check last cron execution status via syslog
grep "svc-monitoring\|CRON" /var/log/syslog | tail -20
```

---

## 6.0 Rollback Procedures

If a deployed script causes issues in production, the rollback procedure must be executed promptly:

### 6.1 Rollback Steps

| Step | Action |
|------|--------|
| 1 | Immediately disable the scheduled task or cron job |
| 2 | Assess the impact — identify affected servers and data |
| 3 | Restore the previous script version from Git or backup |
| 4 | Re-test the previous version in UAT if time permits |
| 5 | Re-enable the scheduler with the previous version |
| 6 | Document the incident in the change log and incident register |

### 6.2 Rollback Commands

```powershell
# Windows — disable a scheduled task immediately
Disable-ScheduledTask -TaskName "IT-DiskSpaceCheck-Daily"

# Restore previous version from Git
git log --oneline scripts/windows/Check-DiskSpace.ps1
git checkout v0.9.0 -- scripts/windows/Check-DiskSpace.ps1
# Re-deploy the restored version
.\Deploy-Script.ps1 -ScriptName "Check-DiskSpace.ps1" -TargetServers @('Server01','Server02') -SourcePath ".\scripts\windows"

# Re-enable the task
Enable-ScheduledTask -TaskName "IT-DiskSpaceCheck-Daily"
```

```bash
# Linux — comment out the cron job immediately
sudo crontab -u svc-monitoring -l | \
    sed 's|^.*/opt/scripts/backup_logs.sh|#&|' | \
    sudo crontab -u svc-monitoring -

# Restore previous version from Git
git checkout v0.9.0 -- scripts/linux/backup_logs.sh
sudo cp scripts/linux/backup_logs.sh /opt/scripts/backup_logs.sh
sudo chmod 750 /opt/scripts/backup_logs.sh

# Re-enable by removing the comment from crontab
sudo crontab -u svc-monitoring -e
```

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCU E01 Server Scripting
- Microsoft Docs: Task Scheduler — https://learn.microsoft.com/en-us/windows/win32/taskschd/
- Linux `crontab` manual — `man 5 crontab`
- systemd.timer manual — `man 5 systemd.timer`
- Red Hat: Using systemd timers — https://access.redhat.com/documentation/
- ITIL Change Management Framework — Change Advisory Board (CAB) processes