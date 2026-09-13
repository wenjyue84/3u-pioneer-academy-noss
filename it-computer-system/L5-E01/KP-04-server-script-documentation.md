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
| NO. KOD | IT-020-5:2013-E01/KP(4/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Use List<T> instead of array += for performance on large server counts.

**TUJUAN:** $results = [System.Collections.Generic.List[PSCustomObject]]::new()

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Produce complete inline code documentation using standard comment conventions for PowerShell, Bash, and Python
2. Write a Script Technical Reference document covering purpose, parameters, dependencies, and examples
3. Maintain a Change Log and version history using Git and structured commit messages
4. Prepare a handover package for operational handover of scripts to the IT Operations team

---

## 1.0 Why Documentation Is Critical for Server Scripts

Server scripts are operational assets. Unlike application code maintained by a development team, scripts are often written by individual administrators and may be maintained by different staff over time. Undocumented scripts are a significant operational risk:

| Risk | Consequence |
|------|-------------|
| No explanation of purpose | New administrator cannot determine if the script is still needed |
| Undocumented parameters | Script called with wrong arguments, producing incorrect or destructive output |
| No known dependencies | Script fails after a server upgrade because a required module was removed |
| No change history | Impossible to identify when a regression was introduced |
| No runbook | Operations team cannot respond to failures at 3 AM without the original author |

**Documentation is not optional at Level 5.** All scripts deployed to production must be accompanied by complete documentation.

---

## 2.0 Inline Code Documentation

Inline documentation is embedded within the script itself. It is the first line of defence for any reader opening the file.

### 2.1 PowerShell — Comment-Based Help

PowerShell has a structured comment-based help system that integrates with `Get-Help`:

```powershell
<#
.SYNOPSIS
    Brief one-line description of what the script does.

.DESCRIPTION
    Full description. Explain the purpose, what problem it solves,
    and any important behaviour the operator should understand.
    May span multiple lines.

.PARAMETER ServerList
    Path to a text file containing one server FQDN per line.
    Default: C:\Config\servers.txt

.PARAMETER Threshold
    Disk utilisation percentage above which a drive is flagged.
    Acceptable range: 50–99. Default: 85.

.PARAMETER SmtpServer
    FQDN or IP of the SMTP relay server. Must be reachable from the
    management server. Mandatory parameter.

.PARAMETER WhatIf
    If specified, the script describes what it would do without making
    any changes or sending any emails. Use for testing.

.EXAMPLE
    .\Check-DiskSpace.ps1 -SmtpServer smtp.contoso.com -ReportRecipient itm@contoso.com
    Runs with default threshold (85%) and default server list.

.EXAMPLE
    .\Check-DiskSpace.ps1 -Threshold 90 -SmtpServer smtp.contoso.com -ReportRecipient itm@contoso.com -WhatIf
    Dry run with 90% threshold — shows what would be flagged without sending email.

.INPUTS
    Text file (ServerList parameter): one server FQDN per line.

.OUTPUTS
    HTML email to ReportRecipient.
    Log file: C:\Logs\DiskCheck_YYYYMMDD.log

.NOTES
    Author     : Ahmad Razif bin Ismail
    Department : IT Operations, Contoso Berhad
    Version    : 1.2
    Date       : 2026-06-01
    Requires   : PowerShell 7.0+; WMI read access on target servers;
                 SMTP relay permission from management server.
    Tested on  : Windows Server 2022; PowerShell 7.4
    Repository : https://git.contoso.com/it-ops/server-scripts

    CHANGE LOG:
    v1.2 (2026-06-01) — Added HTML report body; replaced Write-Host with logging function
    v1.1 (2026-04-15) — Added per-server error handling for unreachable nodes
    v1.0 (2026-03-01) — Initial release
#>
```

**In-body comments** explain non-obvious logic — not what the code does, but why:

```powershell
# Use List<T> instead of array += for performance on large server counts.
# Array concatenation in PowerShell creates a new array on each iteration — O(n²).
$results = [System.Collections.Generic.List[PSCustomObject]]::new()

# Filter DriveType=3 to include only local fixed disks.
# DriveType 2 = removable, 4 = network, 5 = CD-ROM.
$disks = Get-CimInstance -ClassName Win32_LogicalDisk -Filter "DriveType=3"
```

### 2.2 Bash — Comment Conventions

```bash
#!/usr/bin/env bash
# =============================================================================
# Script      : backup_logs.sh
# Purpose     : Compress and archive application logs older than RETENTION_DAYS
# Usage       : ./backup_logs.sh [LOG_DIR] [ARCHIVE_DIR]
# Parameters  :
#   LOG_DIR     — Source log directory (default: /var/log/appserver)
#   ARCHIVE_DIR — Archive destination  (default: /mnt/backup/logs)
# Output      : Compressed .tar.gz archive in ARCHIVE_DIR
#               Log file: /var/log/backup_logs_YYYYMMDD.log
# Dependencies: tar, find (GNU coreutils — standard on all target Linux distros)
# Author      : Siti Norzahra binti Kamarudin
# Department  : IT Infrastructure, Contoso Berhad
# Version     : 1.1 (2026-06-01)
# Tested on   : Ubuntu 22.04 LTS, RHEL 8.6
# Repository  : https://git.contoso.com/it-ops/server-scripts
#
# CHANGE LOG:
# v1.1 (2026-06-01) — Added archive integrity verification before deleting originals
# v1.0 (2026-04-20) — Initial release
# =============================================================================

set -euo pipefail

# Retention period in days. Files older than this will be archived.
readonly RETENTION_DAYS=7

# Use mapfile (bash 4.0+) to safely handle filenames with spaces.
mapfile -t old_logs < <(find "$LOG_DIR" -name "*.log" -mtime +"$RETENTION_DAYS" -type f)
```

### 2.3 Python — Docstrings (PEP 257)

```python
"""
Script  : service_health_check.py
Purpose : Check status of critical systemd services on multiple Linux servers
          via SSH and produce a JSON report.
Usage   : python service_health_check.py --hosts hosts.txt --services services.txt
          python service_health_check.py --hosts hosts.txt --services services.txt --user monitor
Output  : JSON report file; log file.
Author  : Ahmad Razif bin Ismail
Version : 1.0 (2026-06-01)
Requires: Python 3.10+; SSH key-based authentication to target servers;
          'monitor' user with systemctl read privilege on all target hosts.
Tested  : Ubuntu 22.04 LTS target servers; Python 3.12 on management host.
"""


def check_service_on_host(host: str, service: str, ssh_user: str) -> dict:
    """
    Check whether a systemd service is active on a remote host via SSH.

    Uses key-based SSH authentication in non-interactive (BatchMode) mode.
    If the SSH connection times out or fails, returns a result dict with
    status='timeout' or status='error' rather than raising an exception,
    so the caller can continue checking remaining hosts.

    Args:
        host:     FQDN or IP address of the target server.
        service:  Name of the systemd service to check (e.g. 'nginx', 'postgresql').
        ssh_user: SSH username (must have key-based auth configured on target).

    Returns:
        dict with keys:
            host     (str)  — target host
            service  (str)  — service name checked
            status   (str)  — 'active', 'inactive', 'failed', 'timeout', or 'error'
            ok       (bool) — True only when status == 'active'
            error    (str|None) — error message if status is not 'active', else None

    Raises:
        Does not raise. All exceptions are caught and returned in the result dict.
    """
```

---

## 3.0 Script Technical Reference Document

Every production script must be accompanied by a **Script Technical Reference (STR)** document — a standalone document that can be read without opening the script file.

### 3.1 STR Template

```markdown
# Script Technical Reference

## Identification

| Field | Value |
|-------|-------|
| Script Name | Check-DiskSpace.ps1 |
| Script Code | IT-OPS-SCR-001 |
| Version | 1.2 |
| Date | 2026-06-01 |
| Author | Ahmad Razif bin Ismail |
| Owner | IT Operations Team |
| Repository | https://git.contoso.com/it-ops/server-scripts |
| Related Change Request | CHG-2026-0045 |

## Purpose

Checks disk space utilisation on all Windows Server nodes listed in the
configuration file. If any drive exceeds the configured threshold, sends
an HTML email report to the designated recipient.

## Target Environment

| Item | Detail |
|------|--------|
| OS | Windows Server 2019 / 2022 |
| Runtime | PowerShell 7.4+ |
| Execution host | Management server (MGMT-01) |
| Target servers | All production Windows servers (see C:\Config\servers.txt) |
| Network access | WMI (TCP/135 + dynamic RPC) from MGMT-01 to all target servers |
| SMTP access | TCP/25 from MGMT-01 to smtp.contoso.com |

## Dependencies

| Dependency | Type | Purpose |
|------------|------|---------|
| PowerShell 7.4 | Runtime | Script interpreter |
| CimCmdlets module | Built-in module | WMI/CIM queries |
| CONTOSO\svc-monitoring | Service account | Execution identity; WMI read access |
| C:\Config\servers.txt | Configuration file | List of target server FQDNs |
| smtp.contoso.com | Infrastructure | SMTP relay for email report |

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| Threshold | int | No | 85 | Disk usage % above which a drive is flagged |
| SmtpServer | string | Yes | — | FQDN of SMTP relay server |
| ReportRecipient | string | Yes | — | Email address of report recipient |
| ComputerList | string[] | No | From servers.txt | Override server list for ad-hoc runs |

## Input / Output

**Input:** List of server FQDNs (C:\Config\servers.txt); WMI query results from each server.

**Output:**
- HTML email to ReportRecipient when flagged drives found
- Log file: C:\Logs\DiskCheck_YYYYMMDD.log (retained 30 days)
- Exit code 0 (success) or 1 (fatal error)

## Execution Schedule

| Scheduler | Task Name | Schedule | Execution Account |
|-----------|-----------|----------|-------------------|
| Windows Task Scheduler | IT-DiskSpaceCheck-Daily | Daily 06:00 | CONTOSO\svc-monitoring |

## Error Handling

| Condition | Behaviour |
|-----------|-----------|
| Target server unreachable | Logged as UNREACHABLE; included in report; script continues |
| SMTP send failure | Logged as ERROR; script exits with code 1 |
| Log directory not found | Script exits immediately with code 1 |

## Security Considerations

- Execution account (svc-monitoring) has WMI read access only — no admin rights
- No credentials stored in the script; Windows Credential Manager used
- ExecutionPolicy Bypass scoped to this scheduled task only (not system-wide)
- Log files accessible only to svc-monitoring and IT Administrators

## Known Limitations

- WMI queries time out after 30 seconds per server; very slow servers may be marked unreachable
- Does not support servers in untrusted domains without explicit WMI credentials

## Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2026-03-01 | A.R. Ismail | Initial release |
| 1.1 | 2026-04-15 | A.R. Ismail | Added per-server error handling |
| 1.2 | 2026-06-01 | A.R. Ismail | HTML report body; replaced Write-Host with logging function |
```

---

## 4.0 Operational Runbook

The **Operational Runbook** is a procedure document used by the IT Operations team to respond to failures without involving the original script author.

### 4.1 Runbook Template

```markdown
# Operational Runbook: Disk Space Monitoring

## Alert Condition
The scheduled task IT-DiskSpaceCheck-Daily fails or no email is received by 07:00.

## Initial Response (Level 1 — Operations)

1. Check Task Scheduler on MGMT-01:
   - Start > Task Scheduler > Task Scheduler Library > IT-DiskSpaceCheck-Daily
   - Verify Last Run Time and Last Result (0 = OK; 2147942401 = file not found)

2. Check log file: C:\Logs\DiskCheck_YYYYMMDD.log
   - Look for ERROR or FATAL entries
   - Note the last successful line before the error

3. Common quick fixes:
   - Task shows "Last Result: 0x1" → Check if svc-monitoring password has expired
   - Log shows "SMTP error" → Confirm smtp.contoso.com is reachable from MGMT-01
   - Log shows "Access denied" on a server → WMI access may have been revoked; escalate

## Escalation (Level 2 — Senior IT)

If Level 1 steps do not resolve:
- Contact script owner: Ahmad Razif bin Ismail (ext. 4512 / ahmad.razif@contoso.com)
- Provide: full log file, Task Scheduler history, last successful run date

## Manual Execution

To run the script manually as a test:
```powershell
cd C:\Scripts
.\Check-DiskSpace.ps1 -SmtpServer smtp.contoso.com -ReportRecipient itmanager@contoso.com -Verbose
```

To test without sending email:
```powershell
.\Check-DiskSpace.ps1 -SmtpServer smtp.contoso.com -ReportRecipient itmanager@contoso.com -WhatIf
```
```

---

## 5.0 Version Control Documentation

Git provides the authoritative change history for all scripts. In addition to commit messages, the following practices apply:

### 5.1 CHANGELOG.md

Maintain a human-readable `CHANGELOG.md` at the repository root following the Keep a Changelog format:

```markdown
# Changelog

All notable changes to the IT Operations server scripts are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

## [1.2.0] — 2026-06-01
### Changed
- Check-DiskSpace.ps1: Replaced Write-Host with structured Write-Log function
- Check-DiskSpace.ps1: Report body changed to HTML for better readability

## [1.1.0] — 2026-04-15
### Added
- Check-DiskSpace.ps1: Per-server error handling for unreachable nodes
- backup_logs.sh: Archive integrity verification step before deletion

### Fixed
- backup_logs.sh: Script now exits with code 1 when archive creation fails

## [1.0.0] — 2026-03-01
### Added
- Initial release: Check-DiskSpace.ps1, backup_logs.sh, service_health_check.py
```

### 5.2 Git Tags for Releases

```bash
# Tag the current HEAD as a production release
git tag -a v1.2.0 -m "Release v1.2.0 — HTML report and structured logging improvements"
git push origin v1.2.0

# List all release tags
git tag -l "v*"

# View changes between two releases
git log v1.1.0..v1.2.0 --oneline
```

---

## 6.0 Documentation Handover Package

When handing over scripts to the IT Operations team, prepare a complete handover package:

| Document | Description | Format |
|----------|-------------|--------|
| Script Technical Reference (STR) | Full technical specification | Markdown / PDF |
| Operational Runbook | Step-by-step failure response | Markdown / Word |
| CHANGELOG.md | Version history | Markdown |
| Deployment instructions | How to install on a new server | Markdown |
| Test plan | How to verify correct operation | Markdown |
| Access request record | Service account permissions granted | Email/ITSM ticket |
| Change request | CAB approval record | ITSM ticket number |

**Handover sign-off:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Script Author | | | |
| Receiving IT Operations Lead | | | |
| IT Manager | | | |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCU E01 Server Scripting
- PEP 257 — Docstring Conventions — https://peps.python.org/pep-0257/
- PowerShell Comment-Based Help — https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comment_based_help
- Keep a Changelog — https://keepachangelog.com/en/1.0.0/
- Google Developer Documentation Style Guide — https://developers.google.com/style
- ITIL 4 — Service Configuration Management; Change Enablement practices