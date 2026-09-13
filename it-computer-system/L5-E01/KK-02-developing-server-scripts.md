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
| NO. KOD | IT-020-5:2013-E01/KK(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** [Complete the comment-based help block]

**TUJUAN:** [CmdletBinding(SupportsShouldProcess)] param ( [Parameter(Mandatory)] [string[]]$ComputerList,

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objective

Develop three server scripts — one in each of PowerShell, Bash, and Python — for the tasks specified below, applying all production-quality practices from KP(2/4).

---

## Tempoh / Duration

8 hours (spread across multiple sessions as directed by instructor)

---

## Peralatan dan Bahan / Equipment and Materials

| No. | Item | Quantity |
|-----|------|----------|
| 1 | Workstation with PowerShell 7, Bash (WSL or Linux VM), Python 3.10+ | 1 per trainee |
| 2 | VS Code or equivalent editor with PowerShell and Python extensions | 1 |
| 3 | Git client (configured with trainee's name and email) | 1 |
| 4 | Training Git repository (provided by instructor) | 1 |
| 5 | SMTP test server (e.g. Mailtrap or local Postfix relay) | 1 (shared) |
| 6 | KP(2/4) Information Sheet for reference | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Test all scripts in the designated training environment only — never on production servers
- Do not store real passwords or credentials in scripts or in the Git repository
- Use the instructor-provided test SMTP relay only; do not configure external mail servers
- Ensure all scripts include a dry-run (`-WhatIf` / `--dry-run`) flag before any destructive operation

---

## Tugasan 1 — PowerShell: User Account Audit Script

### Scenario
Write a PowerShell 7 script named `Get-LocalUserAudit.ps1` that audits local user accounts on a list of Windows servers and produces a CSV report.

### Requirements
- Accept parameters: `ComputerList` (string array), `OutputPath` (string), `InactiveDays` (int, default 90)
- Query local user accounts on each server using `Get-LocalUser` or `Invoke-Command`
- Flag accounts that are: disabled, password never expires, or have not logged in for more than `InactiveDays`
- Write output to CSV at `OutputPath`
- Log each server query to a daily log file `C:\Logs\UserAudit_YYYYMMDD.log`
- Handle unreachable servers gracefully — log the failure, continue to next server
- Exit with code 0 on full success, 3 on partial success (some servers failed), 1 on fatal error

### Starter Structure
```powershell
#Requires -Version 7.0

<#
.SYNOPSIS
    Audits local user accounts on Windows servers for security compliance.
# [Complete the comment-based help block]
#>

[CmdletBinding(SupportsShouldProcess)]
param (
    [Parameter(Mandatory)]
    [string[]]$ComputerList,

    [Parameter(Mandatory)]
    [string]$OutputPath,

    [Parameter()]
    [ValidateRange(1, 365)]
    [int]$InactiveDays = 90
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# TODO: Implement Write-Log function
# TODO: Implement Get-UserAuditData function with try/catch per server
# TODO: Implement main logic: loop servers, collect results, export CSV
# TODO: Return correct exit code based on partial/full success
```

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Create the file `scripts/windows/Get-LocalUserAudit.ps1` in your training repository. |
| 2 | Write the complete comment-based help block (`.SYNOPSIS`, `.DESCRIPTION`, `.PARAMETER` for each, `.EXAMPLE` ×2, `.NOTES` with version and author). |
| 3 | Implement the `Write-Log` function accepting `Message` and `Level` parameters; append timestamped entries to the daily log file. |
| 4 | Implement `Get-UserAuditData` using `Invoke-Command` to query each server's local users. Handle unreachable servers with try/catch. |
| 5 | In the main block, loop through `ComputerList`, call `Get-UserAuditData`, collect results into a generic List. |
| 6 | Export the collected results to CSV using `Export-Csv`. |
| 7 | Add `-WhatIf` support: when specified, display what would be written to CSV without creating the file. |
| 8 | Implement exit code logic: exit 0 if all servers succeeded, exit 3 if some failed, exit 1 if the script crashed. |
| 9 | Test with: `.\Get-LocalUserAudit.ps1 -ComputerList @('localhost') -OutputPath "C:\Temp\audit.csv" -Verbose` |
| 10 | Commit with message: `feat: add Windows local user audit script with CSV output` |

---

## Tugasan 2 — Bash: Temporary File Cleanup Script

### Scenario
Write a Bash script named `cleanup_tmp.sh` that deletes temporary files from a specified directory on a Linux server, skipping files created within the last 2 hours, logging what was deleted, and sending a summary email if the total cleared space exceeds a threshold.

### Requirements
- Accept arguments: `TARGET_DIR`, `MIN_AGE_MINUTES` (default 120), `ALERT_GB` (default 5), `SMTP_TO`
- Use `find` to locate files older than `MIN_AGE_MINUTES`
- Calculate total size before deletion using `du`
- Delete matching files; log each deleted file with its size
- If total cleared size ≥ `ALERT_GB` GB, send a summary email via `sendmail` or `mail`
- Use `set -euo pipefail`; implement a `die()` function for fatal errors
- Exit code 0 on success, 1 on fatal error

### Starter Structure
```bash
#!/usr/bin/env bash
# cleanup_tmp.sh — Remove stale temporary files and alert on large cleanups
# Usage: ./cleanup_tmp.sh TARGET_DIR [MIN_AGE_MINUTES] [ALERT_GB] [SMTP_TO]
# Author: [Your name]
# Version: 1.0

set -euo pipefail
IFS=$'\n\t'

readonly TARGET_DIR="${1:?Usage: $0 TARGET_DIR [MIN_AGE_MIN] [ALERT_GB] [SMTP_TO]}"
readonly MIN_AGE_MINUTES="${2:-120}"
readonly ALERT_GB="${3:-5}"
readonly SMTP_TO="${4:-}"
readonly LOG_FILE="/var/log/cleanup_tmp_$(date +%Y%m%d).log"

# TODO: Implement log() function
# TODO: Implement die() function
# TODO: Implement validate_inputs() — check TARGET_DIR exists and is writable
# TODO: Implement calculate_size_gb() using du
# TODO: Implement send_alert_email() using mail command
# TODO: Implement main cleanup loop using find + rm
```

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Create `scripts/linux/cleanup_tmp.sh` in your training repository. |
| 2 | Implement `log()` to write timestamped entries to `$LOG_FILE` and stdout simultaneously using `tee`. |
| 3 | Implement `die()` to call `log ERROR` and exit 1. |
| 4 | Implement `validate_inputs()` — verify `TARGET_DIR` exists, is a directory, and is writable. |
| 5 | Use `find "$TARGET_DIR" -type f -mmin +"$MIN_AGE_MINUTES"` to locate candidate files. Store results with `mapfile`. |
| 6 | Calculate total size of candidate files in GB before deletion. |
| 7 | Delete each file with `rm`; log the filename and size. Accumulate total bytes deleted. |
| 8 | After deletion, check if total GB cleared ≥ `ALERT_GB`. If so, call `send_alert_email()`. |
| 9 | Make the script executable: `chmod 750 cleanup_tmp.sh`. Test with a temp directory containing dummy files. |
| 10 | Commit with message: `feat: add Linux tmp cleanup script with threshold alerting` |

---

## Tugasan 3 — Python: Disk Space Report Generator

### Scenario
Write a Python script named `disk_report.py` that queries disk utilisation on multiple Linux servers via SSH and generates a JSON report with summary statistics.

### Requirements
- Accept `--hosts` (path to hosts file), `--threshold` (int, default 80), `--output` (JSON path), `--log` (log file)
- SSH to each host and run `df -h --output=source,size,used,avail,pcent,target` to get disk info
- Parse the `df` output; flag filesystems where `pcent` ≥ threshold
- Write a JSON report: `generated_at`, `total_filesystems`, `flagged`, `results` array
- Use structured logging (file + console) from `logging` module
- Handle SSH failures gracefully — record in results as `status: "unreachable"`
- Return exit code 0 (no flagged), 3 (some flagged), 1 (fatal)

### Starter Structure
```python
#!/usr/bin/env python3
"""
disk_report.py — Query disk usage on remote Linux servers via SSH.
[Complete the full module docstring as per KP(4/4)]
"""

import argparse
import json
import logging
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def configure_logging(log_file: Path) -> logging.Logger:
    # TODO: Implement file + console logging as per KP(2/4) Section 2.3
    ...


def load_hosts(hosts_file: Path) -> list[str]:
    # TODO: Read newline-delimited host file; strip blank lines and comments (#)
    ...


def query_disk_usage(host: str, user: str) -> dict:
    """
    SSH to host and parse 'df' output.
    Returns dict with host, filesystems list, status, error.
    # TODO: Complete docstring per PEP 257
    """
    # TODO: Run: ssh -o BatchMode=yes -o ConnectTimeout=10 user@host
    #            "df -h --output=source,size,used,avail,pcent,target"
    # TODO: Parse output: skip header line; split each line into fields
    # TODO: Return structured result dict
    ...


def write_report(results: list[dict], output_path: Path, threshold: int) -> None:
    # TODO: Build report dict; write to output_path as formatted JSON
    ...


def parse_args() -> argparse.Namespace:
    # TODO: Define all arguments with help strings and defaults
    ...


def main() -> int:
    # TODO: Orchestrate: parse args → configure logging → load hosts
    #       → run queries → write report → return exit code
    ...


if __name__ == "__main__":
    sys.exit(main())
```

### Procedure

| Langkah | Arahan / Instruction |
|---------|---------------------|
| 1 | Create `scripts/python/disk_report.py` in your training repository. |
| 2 | Complete the module-level docstring with all required fields from KP(4/4). |
| 3 | Implement `configure_logging()` with file (DEBUG level) and console (INFO level) handlers. |
| 4 | Implement `load_hosts()` — read the file, strip blank lines and lines starting with `#`. |
| 5 | Implement `query_disk_usage()` — SSH to the host, run `df`, parse each data line into a dict with fields: `source`, `size`, `used`, `avail`, `pcent` (int), `target`. |
| 6 | Add threshold comparison: set `flagged=True` on any filesystem where `pcent >= threshold`. |
| 7 | Implement `write_report()` — create the JSON structure and write to `output_path` with `indent=2`. |
| 8 | Implement `parse_args()` with `--hosts`, `--threshold`, `--output`, `--user`, `--log`. |
| 9 | Implement `main()` — orchestrate all functions; return exit code 3 if any filesystems are flagged, 1 if fatal error, 0 if clean. |
| 10 | Test on localhost or a training VM. Commit: `feat: add SSH disk usage reporter with JSON output` |

---

## Hasil Jangkaan / Expected Outcome

Three committed, tested scripts:
1. `Get-LocalUserAudit.ps1` — working PowerShell script with full help, logging, error handling, exit codes
2. `cleanup_tmp.sh` — working Bash script with logging, size calculation, alert email
3. `disk_report.py` — working Python script with SSH querying, JSON output, structured logging

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | PowerShell: Complete comment-based help block present | [ ] Yes  [ ] No |
| 2 | PowerShell: Write-Log function implemented with timestamp and level | [ ] Yes  [ ] No |
| 3 | PowerShell: Error handling with try/catch per server | [ ] Yes  [ ] No |
| 4 | PowerShell: Correct exit codes (0/3/1) implemented | [ ] Yes  [ ] No |
| 5 | Bash: `set -euo pipefail` present; `die()` function implemented | [ ] Yes  [ ] No |
| 6 | Bash: `find` with correct `-mmin` flag for age filter | [ ] Yes  [ ] No |
| 7 | Bash: Alert email triggered only when threshold exceeded | [ ] Yes  [ ] No |
| 8 | Python: Module docstring complete per PEP 257 | [ ] Yes  [ ] No |
| 9 | Python: Structured logging with file and console handlers | [ ] Yes  [ ] No |
| 10 | Python: JSON report written with correct structure | [ ] Yes  [ ] No |
| 11 | All three scripts committed to Git with meaningful commit messages | [ ] Yes  [ ] No |
| 12 | No hardcoded credentials in any script or in Git history | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Name | Signature | Date |
|---|------|-----------|------|
| Trainee | | | |
| Instructor | | | |