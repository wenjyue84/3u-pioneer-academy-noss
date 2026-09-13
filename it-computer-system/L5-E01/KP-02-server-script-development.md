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
| NO. KOD | IT-020-5:2013-E01/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** --- Logging Setup ---

**TUJUAN:** $LogPath = "C:\Logs\DiskCheck_$(Get-Date -Format 'yyyyMMdd').log"

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Apply structured script design principles including modularisation, parameterisation, and coding standards
2. Implement error handling, input validation, and logging in PowerShell, Bash, and Python scripts
3. Write scripts for common server administration tasks using real-world patterns
4. Apply version control practices using Git for server scripts

---

## 1.0 Script Design Principles

Well-designed server scripts share five characteristics regardless of language:

| Principle | Description |
|-----------|-------------|
| **Single responsibility** | Each script or function performs one clearly defined task |
| **Parameterisation** | Inputs are passed as parameters, not hardcoded in the script body |
| **Idempotency** | Running the script multiple times produces the same result as running it once |
| **Fail-safe defaults** | Scripts default to safe actions; destructive operations require explicit confirmation |
| **Observability** | Scripts produce logs and meaningful exit codes so failures can be diagnosed |

---

## 2.0 Script Structure and Coding Standards

### 2.1 PowerShell Script Structure

A production-quality PowerShell script follows this canonical structure:

```powershell
#Requires -Version 7.0
#Requires -Modules ActiveDirectory

<#
.SYNOPSIS
    Checks disk space on all servers and emails a report.
.DESCRIPTION
    Queries all Windows Server nodes for disk utilisation.
    Sends an HTML email report to the IT Manager if any drive exceeds the threshold.
.PARAMETER Threshold
    Disk utilisation percentage above which a drive is flagged. Default: 85.
.PARAMETER SmtpServer
    FQDN of the SMTP relay server.
.PARAMETER ReportRecipient
    Email address of the report recipient.
.EXAMPLE
    .\Check-DiskSpace.ps1 -Threshold 80 -SmtpServer smtp.contoso.com -ReportRecipient itmanager@contoso.com
.NOTES
    Author  : IT Operations Team
    Version : 1.2
    Date    : 2026-06-01
    Requires: WMI read access on target servers; SMTP relay permission
#>

[CmdletBinding(SupportsShouldProcess)]
param (
    [Parameter()]
    [ValidateRange(50, 99)]
    [int]$Threshold = 85,

    [Parameter(Mandatory)]
    [string]$SmtpServer,

    [Parameter(Mandatory)]
    [string]$ReportRecipient,

    [Parameter()]
    [string[]]$ComputerList = @('Server01', 'Server02', 'Server03')
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# --- Logging Setup ---
$LogPath = "C:\Logs\DiskCheck_$(Get-Date -Format 'yyyyMMdd').log"

function Write-Log {
    param([string]$Message, [string]$Level = 'INFO')
    $entry = "[{0}] [{1}] {2}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Level, $Message
    Add-Content -Path $LogPath -Value $entry
    Write-Verbose $entry
}

# --- Main Logic ---
function Get-DiskReport {
    [OutputType([PSCustomObject[]])]
    param([string[]]$Computers, [int]$ThresholdPct)

    $results = [System.Collections.Generic.List[PSCustomObject]]::new()

    foreach ($computer in $Computers) {
        try {
            Write-Log "Querying $computer"
            $disks = Get-CimInstance -ClassName Win32_LogicalDisk `
                        -ComputerName $computer `
                        -Filter "DriveType=3" `
                        -ErrorAction Stop |
                    Select-Object DeviceID,
                        @{N='SizeGB';  E={[math]::Round($_.Size / 1GB, 1)}},
                        @{N='FreeGB';  E={[math]::Round($_.FreeSpace / 1GB, 1)}},
                        @{N='UsedPct'; E={[math]::Round((1 - $_.FreeSpace / $_.Size) * 100, 1)}}

            foreach ($disk in $disks) {
                $results.Add([PSCustomObject]@{
                    ComputerName = $computer
                    Drive        = $disk.DeviceID
                    SizeGB       = $disk.SizeGB
                    FreeGB       = $disk.FreeGB
                    UsedPct      = $disk.UsedPct
                    Flagged      = $disk.UsedPct -ge $ThresholdPct
                    Status       = 'OK'
                })
            }
        }
        catch {
            Write-Log "ERROR querying $computer`: $($_.Exception.Message)" 'ERROR'
            $results.Add([PSCustomObject]@{
                ComputerName = $computer
                Drive        = 'N/A'
                SizeGB       = 0
                FreeGB       = 0
                UsedPct      = 0
                Flagged      = $false
                Status       = "UNREACHABLE: $($_.Exception.Message)"
            })
        }
    }
    return $results.ToArray()
}

try {
    Write-Log "Script started. Threshold: $Threshold%"
    $report = Get-DiskReport -Computers $ComputerList -ThresholdPct $Threshold
    $flaggedCount = ($report | Where-Object { $_.Flagged }).Count

    Write-Log "Query complete. $flaggedCount drive(s) above threshold."

    # Build HTML body
    $htmlRows = $report | ForEach-Object {
        $colour = if ($_.Flagged) { '#FFDDC1' } elseif ($_.Status -ne 'OK') { '#FFB3B3' } else { '#FFFFFF' }
        "<tr style='background:$colour'><td>$($_.ComputerName)</td><td>$($_.Drive)</td>" +
        "<td>$($_.SizeGB)</td><td>$($_.FreeGB)</td><td>$($_.UsedPct)%</td><td>$($_.Status)</td></tr>"
    }
    $htmlBody = @"
<html><body>
<h2>Disk Space Report — $(Get-Date -Format 'yyyy-MM-dd')</h2>
<p>Threshold: $Threshold% | Flagged: $flaggedCount drive(s)</p>
<table border='1' cellpadding='5' style='border-collapse:collapse;font-family:Arial'>
<tr style='background:#4472C4;color:white'><th>Server</th><th>Drive</th><th>Size (GB)</th><th>Free (GB)</th><th>Used %</th><th>Status</th></tr>
$($htmlRows -join "`n")
</table></body></html>
"@

    if ($PSCmdlet.ShouldProcess($ReportRecipient, 'Send disk space report email')) {
        Send-MailMessage -From 'monitoring@contoso.com' -To $ReportRecipient `
            -Subject "Disk Space Report $(Get-Date -Format 'yyyy-MM-dd') — $flaggedCount flagged" `
            -Body $htmlBody -BodyAsHtml -SmtpServer $SmtpServer
        Write-Log "Report email sent to $ReportRecipient"
    }

    exit 0
}
catch {
    Write-Log "FATAL: $($_.Exception.Message)" 'ERROR'
    exit 1
}
```

### 2.2 Bash Script Structure

```bash
#!/usr/bin/env bash
# =============================================================================
# Script  : backup_logs.sh
# Purpose : Compress and archive application logs older than 7 days
# Usage   : ./backup_logs.sh [LOG_DIR] [ARCHIVE_DIR]
# Author  : IT Operations Team
# Version : 1.1 (2026-06-01)
# =============================================================================

set -euo pipefail          # Exit on error; treat unset vars as error; propagate pipe failures
IFS=$'\n\t'               # Safer word splitting

# --- Configuration (overridable via environment or positional arguments) ---
readonly LOG_DIR="${1:-/var/log/appserver}"
readonly ARCHIVE_DIR="${2:-/mnt/backup/logs}"
readonly RETENTION_DAYS=7
readonly LOG_FILE="/var/log/backup_logs_$(date +%Y%m%d).log"
readonly SCRIPT_NAME="$(basename "$0")"

# --- Helper Functions ---
log() {
    local level="$1"; shift
    printf '[%s] [%s] [%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$SCRIPT_NAME" "$level" "$*" \
        | tee -a "$LOG_FILE"
}

die() {
    log "ERROR" "$*"
    exit 1
}

validate_directories() {
    [[ -d "$LOG_DIR" ]]     || die "Log directory not found: $LOG_DIR"
    [[ -d "$ARCHIVE_DIR" ]] || die "Archive directory not found: $ARCHIVE_DIR"
    [[ -w "$ARCHIVE_DIR" ]] || die "Archive directory not writable: $ARCHIVE_DIR"
}

# --- Main Logic ---
main() {
    log "INFO" "Starting log backup. Source: $LOG_DIR | Archive: $ARCHIVE_DIR"

    validate_directories

    local archive_name
    archive_name="${ARCHIVE_DIR}/logs_$(date +%Y%m%d_%H%M%S).tar.gz"

    # Find and compress log files older than retention period
    local -a old_logs
    mapfile -t old_logs < <(find "$LOG_DIR" -name "*.log" -mtime +"$RETENTION_DAYS" -type f)

    if [[ ${#old_logs[@]} -eq 0 ]]; then
        log "INFO" "No log files older than $RETENTION_DAYS days found. Nothing to archive."
        exit 0
    fi

    log "INFO" "Found ${#old_logs[@]} file(s) to archive."

    # Create compressed archive
    if tar -czf "$archive_name" "${old_logs[@]}"; then
        log "INFO" "Archive created: $archive_name"
    else
        die "Failed to create archive: $archive_name"
    fi

    # Verify archive integrity before deleting originals
    if tar -tzf "$archive_name" > /dev/null 2>&1; then
        log "INFO" "Archive integrity verified."
        rm -f "${old_logs[@]}"
        log "INFO" "Removed ${#old_logs[@]} original log file(s)."
    else
        die "Archive integrity check failed. Original files preserved."
    fi

    log "INFO" "Backup complete. Archive: $archive_name"
    exit 0
}

main "$@"
```

### 2.3 Python Script Structure

```python
#!/usr/bin/env python3
"""
Script  : service_health_check.py
Purpose : Check status of critical services on multiple Linux servers via SSH
          and produce a JSON/HTML report.
Usage   : python service_health_check.py --hosts hosts.txt --services services.txt
Author  : IT Operations Team
Version : 1.0 (2026-06-01)
"""

import argparse
import json
import logging
import subprocess
import sys
from datetime import datetime
from pathlib import Path


# ---------------------------------------------------------------------------
# Logging Configuration
# ---------------------------------------------------------------------------
def configure_logging(log_file: Path) -> logging.Logger:
    logger = logging.getLogger("service_health")
    logger.setLevel(logging.DEBUG)

    fmt = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # File handler
    fh = logging.FileHandler(log_file)
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    # Console handler (INFO and above only)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    return logger


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------
def load_list_from_file(file_path: Path) -> list[str]:
    """Read a newline-delimited text file and return non-empty stripped lines."""
    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    return [line.strip() for line in file_path.read_text().splitlines() if line.strip()]


def check_service_on_host(host: str, service: str, ssh_user: str) -> dict:
    """
    SSH into host and check if systemd service is active.
    Returns a result dict with host, service, status, and any error message.
    """
    cmd = [
        "ssh",
        "-o", "ConnectTimeout=10",
        "-o", "BatchMode=yes",           # Non-interactive; fail if key auth not available
        "-o", "StrictHostKeyChecking=no",
        f"{ssh_user}@{host}",
        f"systemctl is-active {service}"
    ]
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=15,
        )
        status = result.stdout.strip()   # 'active', 'inactive', 'failed', etc.
        return {
            "host": host,
            "service": service,
            "status": status,
            "ok": status == "active",
            "error": result.stderr.strip() if result.returncode != 0 else None,
        }
    except subprocess.TimeoutExpired:
        return {"host": host, "service": service, "status": "timeout", "ok": False,
                "error": "SSH connection timed out"}
    except Exception as exc:
        return {"host": host, "service": service, "status": "error", "ok": False,
                "error": str(exc)}


def run_checks(hosts: list[str], services: list[str], ssh_user: str,
               logger: logging.Logger) -> list[dict]:
    """Run service checks for all host/service combinations."""
    results = []
    for host in hosts:
        for service in services:
            logger.debug("Checking %s on %s", service, host)
            result = check_service_on_host(host, service, ssh_user)
            results.append(result)
            level = logging.INFO if result["ok"] else logging.WARNING
            logger.log(level, "%-20s %-30s %s", host, service, result["status"])
    return results


def write_json_report(results: list[dict], output_path: Path) -> None:
    report = {
        "generated_at": datetime.now().isoformat(),
        "total": len(results),
        "passed": sum(1 for r in results if r["ok"]),
        "failed": sum(1 for r in results if not r["ok"]),
        "results": results,
    }
    output_path.write_text(json.dumps(report, indent=2))


# ---------------------------------------------------------------------------
# Entry Point
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Server service health checker")
    parser.add_argument("--hosts",    required=True, type=Path, help="Path to hosts list file")
    parser.add_argument("--services", required=True, type=Path, help="Path to services list file")
    parser.add_argument("--user",     default="monitor", help="SSH username (default: monitor)")
    parser.add_argument("--output",   default="health_report.json", type=Path,
                        help="Output JSON report path")
    parser.add_argument("--log",      default=Path(f"health_check_{datetime.now():%Y%m%d}.log"),
                        type=Path, help="Log file path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logger = configure_logging(args.log)

    try:
        hosts    = load_list_from_file(args.hosts)
        services = load_list_from_file(args.services)
    except FileNotFoundError as exc:
        logger.error("Input file error: %s", exc)
        return 1

    logger.info("Starting health check: %d host(s), %d service(s)", len(hosts), len(services))
    results = run_checks(hosts, services, args.user, logger)

    write_json_report(results, args.output)
    failed = sum(1 for r in results if not r["ok"])
    logger.info("Complete. Report: %s | Failed checks: %d", args.output, failed)

    return 1 if failed > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
```

---

## 3.0 Error Handling Patterns

Robust error handling is a mandatory requirement for production server scripts. The following patterns apply across all three languages:

### 3.1 Error Handling Comparison Table

| Pattern | PowerShell | Bash | Python |
|---------|-----------|------|--------|
| Terminate on error | `$ErrorActionPreference = 'Stop'` | `set -e` | Exception propagation |
| Try/catch block | `try { } catch { }` | `command || handle_error` | `try: except Exception:` |
| Exit codes | `exit 0` / `exit 1` | `exit 0` / `exit 1` | `sys.exit(0)` / `sys.exit(1)` |
| Unset variable protection | `Set-StrictMode -Version Latest` | `set -u` | Always strict in Python |
| Pipe failure detection | N/A (object pipeline) | `set -o pipefail` | Exception on subprocess failure |

### 3.2 Exit Code Convention

Scripts must return meaningful exit codes so schedulers and monitoring tools can detect failures:

| Exit Code | Meaning |
|-----------|---------|
| 0 | Success — script completed without errors |
| 1 | General error — an unhandled exception or fatal condition occurred |
| 2 | Input/argument error — invalid parameters supplied |
| 3 | Partial success — script completed but some operations failed (use for multi-server scripts) |

---

## 4.0 Input Validation

All scripts must validate inputs before processing to prevent runtime failures and security vulnerabilities:

```powershell
# PowerShell — Parameter validation using built-in validators
param (
    [Parameter(Mandatory)]
    [ValidateNotNullOrEmpty()]
    [string]$ServerName,

    [Parameter()]
    [ValidateSet('Start', 'Stop', 'Restart')]
    [string]$Action = 'Restart',

    [Parameter()]
    [ValidateRange(1, 65535)]
    [int]$Port = 443
)
```

```bash
# Bash — manual validation with die helper
validate_input() {
    local server="$1"
    local action="$2"

    [[ -n "$server" ]] || die "Server name cannot be empty"
    [[ "$server" =~ ^[a-zA-Z0-9._-]+$ ]] || die "Invalid server name: $server"

    case "$action" in
        start|stop|restart) ;;
        *) die "Invalid action '$action'. Must be: start, stop, restart" ;;
    esac
}
```

---

## 5.0 Version Control with Git

All server scripts must be managed in a Git repository. The minimum Git workflow for server scripts:

```bash
# Initialise repository
git init server-scripts
cd server-scripts

# Standard project structure
mkdir -p scripts/{windows,linux,python} tests docs

# Add a new script
git add scripts/windows/Check-DiskSpace.ps1
git commit -m "feat: add disk space monitoring script for Windows Server fleet"

# Feature branch for development
git checkout -b feature/add-service-health-check
# ... develop and test ...
git add scripts/python/service_health_check.py
git commit -m "feat: add cross-platform service health checker with JSON output"
git checkout main
git merge feature/add-service-health-check

# Tag production-ready versions
git tag -a v1.0.0 -m "Release v1.0.0 — disk check and service health scripts"
```

**Commit message conventions (Conventional Commits):**

| Prefix | Use |
|--------|-----|
| `feat:` | New script or new feature added to existing script |
| `fix:` | Bug fix |
| `refactor:` | Code restructured without changing functionality |
| `docs:` | Documentation only changes |
| `test:` | Test scripts added or updated |
| `chore:` | Maintenance (dependency updates, config) |

**Files that must NEVER be committed:**

- Password files, API keys, or private keys
- `.env` files containing credentials
- Scripts with hardcoded connection strings to production systems

Use a `.gitignore` file and a `credentials/` folder excluded from tracking.

---

## 6.0 Modularisation and Reusability

Large scripts must be split into reusable modules or libraries:

```powershell
# PowerShell module file: ITOps.Utilities.psm1
function Write-Log {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Message,
        [ValidateSet('INFO','WARNING','ERROR')][string]$Level = 'INFO',
        [string]$LogPath = "C:\Logs\itops.log"
    )
    $entry = "[{0}] [{1}] {2}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Level, $Message
    Add-Content -Path $LogPath -Value $entry
}

function Test-ServerConnectivity {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string[]]$ComputerNames)
    foreach ($name in $ComputerNames) {
        [PSCustomObject]@{
            ComputerName = $name
            Reachable    = (Test-Connection -ComputerName $name -Count 1 -Quiet)
        }
    }
}

Export-ModuleMember -Function Write-Log, Test-ServerConnectivity
```

Import in other scripts with:
```powershell
Import-Module "\\scripts-share\Modules\ITOps.Utilities.psm1"
```

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCU E01 Server Scripting
- Microsoft PowerShell Documentation — https://learn.microsoft.com/en-us/powershell/
- Advanced Bash-Scripting Guide — https://tldp.org/LDP/abs/html/
- Python Logging HOWTO — https://docs.python.org/3/howto/logging.html
- Conventional Commits Specification — https://www.conventionalcommits.org/
- Pro Git (Scott Chacon & Ben Straub) — https://git-scm.com/book/en/v2