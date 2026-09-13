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
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C05 SERVER MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER MAINTENANCE JOB ORDER<br>2. CARRY OUT HARDWARE MAINTENANCE<br>3. PERFORM SERVER OPERATING SYSTEM MAINTENANCE<br>4. PREPARE SERVER MAINTENANCE RECORD |
| NO. KOD | IT-020-3:2013-C05/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Check available updates

**TUJUAN:** sudo dnf check-update

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the importance of server operating system maintenance for security and stability
2. Describe the OS patching and update cycle, including testing and rollback procedures
3. Perform server backup and restoration procedures for Windows Server and Linux server environments
4. Configure and interpret server monitoring tools and system logs to detect service degradation
5. Maintain server storage by managing disk space, file system health, and temporary files
6. Apply user account and access control maintenance practices on a server OS
7. Document all OS maintenance activities in accordance with organisational change management requirements

---

## 1.0 Introduction to Server OS Maintenance

The server operating system (OS) is the software layer that manages hardware resources and provides services to applications and users. A well-maintained server OS is essential for:

- **Security (Keselamatan):** Unpatched OS vulnerabilities are the primary vector for ransomware, malware, and unauthorised access.
- **Stability (Kestabilan):** Accumulated disk clutter, fragmented logs, and outdated drivers can degrade server performance over time.
- **Compliance (Pematuhan):** Regulatory frameworks (e.g. ISO 27001, PCI-DSS) require documented patch management and audit trails.
- **Availability (Ketersediaan):** Proactive monitoring and maintenance reduces unplanned downtime.

Common server OS platforms in Malaysian enterprise environments:

| Platform | Common Versions | Typical Use Case |
|----------|----------------|-----------------|
| Windows Server | 2016, 2019, 2022 | Active Directory, file server, IIS web server, SQL Server |
| Linux (RHEL / CentOS / Rocky Linux) | 7, 8, 9 | Web server (Apache/Nginx), database (MySQL/PostgreSQL), containerised workloads |
| Linux (Ubuntu Server) | 20.04 LTS, 22.04 LTS | Cloud-adjacent workloads, development servers |

The procedures in this information sheet apply to both Windows Server and Linux server environments unless stated otherwise.

---

## 2.0 OS Patching and Update Management

### 2.1 Why Patching is Critical

Software vulnerabilities (kelemahan perisian) are discovered continuously. Vendors release patches (tampalan) to fix these vulnerabilities. An unpatched server is exposed to known exploits that attackers can use to gain unauthorised access, steal data, or disrupt services.

The patch management cycle (kitaran pengurusan tampalan):

```
Identify available patches
        ↓
Assess risk and relevance
        ↓
Test in a non-production environment
        ↓
Schedule maintenance window
        ↓
Apply patches to production server
        ↓
Verify system stability after patching
        ↓
Document and close the change request
```

### 2.2 Patch Classification

| Classification | Description | Typical Response Time |
|----------------|-------------|----------------------|
| Critical (Kritikal) | Remotely exploitable vulnerability; no user interaction required | Apply within 72 hours; emergency change if actively exploited |
| Important (Penting) | Vulnerability that can be exploited with user interaction or local access | Apply within 14 days |
| Moderate (Sederhana) | Limited impact; requires significant conditions to exploit | Apply in next scheduled maintenance cycle |
| Low (Rendah) | Minimal impact; defence-in-depth improvement | Apply at next quarterly maintenance |

### 2.3 Windows Server Patching Procedure

**Method 1: Windows Server Update Services (WSUS)**

WSUS is the recommended method in organisational environments. It allows the IT administrator to approve, test, and deploy patches to multiple servers in a controlled manner.

1. On the WSUS server, review and approve updates for the target server group.
2. On the target server, open **Windows Update** settings and trigger a check for updates from the WSUS server.
3. Review the list of approved updates; note any updates that require a restart.
4. Schedule the update installation during an approved maintenance window.
5. After installation, review the update history to confirm all patches were applied successfully.
6. Restart the server if required; verify all services start correctly after restart.

**Method 2: Manual patch application (standalone servers)**

1. Open **Windows Update** (Settings → Windows Update) or **sconfig** (Server Core).
2. Click "Check for updates."
3. Review available updates; defer optional updates that are not security-related unless tested.
4. Install selected updates; restart as required.
5. Confirm update status shows "You're up to date."

**Key Windows Server update components:**

| Component | Update Method |
|-----------|--------------|
| Windows OS (cumulative updates) | Windows Update / WSUS |
| .NET Framework | Windows Update / WSUS |
| Windows Defender definitions | Windows Update / WSUS (automatic recommended) |
| Drivers and firmware | Vendor utilities (do not use Windows Update for server firmware) |
| Server roles (IIS, AD DS, etc.) | Windows Update / WSUS |

### 2.4 Linux Server Patching Procedure

**RHEL / CentOS / Rocky Linux (using `yum` / `dnf`):**

```bash
# Check available updates
sudo dnf check-update

# Apply security updates only
sudo dnf update --security

# Apply all updates
sudo dnf update

# Check for kernel updates specifically
sudo dnf update kernel

# List installed kernel versions
sudo rpm -q kernel

# Reboot to activate a new kernel
sudo reboot
```

**Ubuntu Server (using `apt`):**

```bash
# Refresh package lists
sudo apt update

# Show available upgrades
sudo apt list --upgradable

# Apply security updates only (unattended-upgrades)
sudo unattended-upgrade --dry-run   # preview
sudo unattended-upgrade             # apply

# Apply all updates
sudo apt upgrade

# Apply distribution-level upgrades (use with caution on production)
sudo apt full-upgrade
```

**Important:** After a kernel update on Linux, the server must be rebooted for the new kernel to take effect. Verify the active kernel version after reboot:

```bash
uname -r
```

### 2.5 Testing Before Production Deployment

Patches should be tested in a non-production environment (staging server or test VM) before deployment to production servers, particularly for:

- Cumulative updates that include changes to core OS components
- Updates to server roles actively in use (e.g. IIS, Active Directory, DNS)
- Updates to database engines (SQL Server, MySQL)

Testing checklist:
- [ ] Apply patch to test server
- [ ] Verify server boots normally
- [ ] Verify all installed applications function correctly
- [ ] Check event logs for new error or warning events introduced by the patch
- [ ] Test key services (web, database, authentication)
- [ ] If all pass: proceed to production deployment

### 2.6 Rollback Procedures

If a patch causes instability in production:

**Windows Server rollback:**
- Open **Settings → Windows Update → Update History → Uninstall Updates**
- Select the problematic update and uninstall
- Restart the server
- Re-add the update to the WSUS decline list pending investigation

**Linux rollback (RPM-based):**
```bash
# List installed packages by date to identify recently installed packages
sudo rpm -qa --last | head -20

# Downgrade a specific package
sudo dnf downgrade <package-name>

# Roll back to a previous kernel
# Edit GRUB and select the previous kernel at boot, then:
sudo grubby --set-default /boot/vmlinuz-<previous-version>
```

**Linux rollback (APT-based):**
```bash
# Install a specific older version
sudo apt install <package-name>=<version>

# Hold a package at current version (prevent future auto-update)
sudo apt-mark hold <package-name>
```

---

## 3.0 Server Backup and Restoration

### 3.1 Importance of Server Backup

A server backup (sandaran pelayan) is a copy of the server's data, configuration, and system state stored in a separate location. Backups are the last line of defence against data loss caused by hardware failure, ransomware, accidental deletion, or a failed software update.

The backup strategy must address three questions:
- **What** is being backed up? (data files, OS system state, database, full image)
- **Where** is the backup stored? (local tape, NAS, remote site, cloud)
- **When** is it restored from? (how recent is the backup — Recovery Point Objective / RPO)

### 3.2 Backup Types

| Type | Jenis | Description | Storage Use | Restore Time |
|------|-------|-------------|-------------|--------------|
| Full backup | Sandaran penuh | Complete copy of all selected data | High | Fast (single set) |
| Incremental backup | Sandaran tambahan | Only data changed since the last backup (full or incremental) | Low | Slower (requires full + all incrementals) |
| Differential backup | Sandaran perbezaan | Only data changed since the last full backup | Medium | Medium (requires full + latest differential) |
| System state backup | Sandaran keadaan sistem | OS configuration, registry, Active Directory, boot files | Low–Medium | Fast for config recovery |
| Bare metal backup | Sandaran logam bogel | Full disk image including OS, applications, and data | Very high | Fastest full restore |

### 3.3 Backup Schedule — Recommended Practice

| Backup Type | Frequency | Retention |
|-------------|-----------|-----------|
| Full | Weekly (Sunday, off-hours) | 4 weeks |
| Incremental or Differential | Daily (Monday–Saturday, off-hours) | 2 weeks |
| System state (Windows Server) | Daily | 2 weeks |
| Database transaction log | Every 15–60 minutes (for critical databases) | 48–72 hours |

### 3.4 Windows Server Backup Procedure

**Using Windows Server Backup (wbadmin):**

```batch
:: Full server backup to network share
wbadmin start backup -backuptarget:\\NAS01\Backups\SRV01 -include:C: -allCritical -quiet

:: System state backup only
wbadmin start systemstatebackup -backuptarget:D: -quiet

:: Check backup status
wbadmin get status
```

**Verifying a Windows Server Backup:**
- Open Windows Server Backup console
- Review "Last backup" — confirm status shows "Successful"
- Check "Backup items" — confirm all volumes and system state are included
- Periodically perform a test restore to a separate location to confirm backup integrity

### 3.5 Linux Server Backup Procedure

**Using rsync (file-level backup):**

```bash
# Incremental backup of /var/www and /etc to a remote NAS
rsync -avz --delete /var/www/ backup-user@NAS01:/backups/srv01/www/
rsync -avz --delete /etc/ backup-user@NAS01:/backups/srv01/etc/

# With SSH key authentication (recommended for automated scripts)
rsync -avz -e "ssh -i /root/.ssh/backup_key" /data/ backup-user@NAS01:/backups/srv01/data/
```

**Using tar (archive backup):**

```bash
# Create compressed archive of /etc
tar -czf /mnt/backup/etc-$(date +%Y%m%d).tar.gz /etc

# Restore from tar archive
tar -xzf /mnt/backup/etc-20260101.tar.gz -C /
```

**Verifying a Linux backup:**
- Confirm the backup file exists and is non-zero size: `ls -lh /mnt/backup/`
- Test restore of a sample file to a temporary location to confirm archive integrity
- For rsync: compare file counts between source and destination: `find /var/www | wc -l`

### 3.6 Backup Verification — The 3-2-1 Rule

The 3-2-1 backup rule (Peraturan 3-2-1) is the industry standard for backup resilience:

| Rule | Meaning |
|------|---------|
| **3** copies of data | The original plus 2 backups |
| **2** different storage media | e.g. internal disk + NAS, or NAS + tape |
| **1** offsite copy | A copy stored in a physically separate location (remote site or cloud) |

A backup that has never been tested is not a backup — it is an assumption. Schedule periodic restore tests (at minimum quarterly) to verify backup integrity.

---

## 4.0 Server Monitoring

### 4.1 Purpose of Server Monitoring

Server monitoring (pemantauan pelayan) is the continuous observation of server performance metrics and service availability to detect problems before they cause outages. Monitoring enables:

- Early detection of resource exhaustion (disk full, RAM saturation, CPU spike)
- Alerting when a service stops responding
- Trending analysis to plan capacity upgrades
- Evidence collection for incident investigation

### 4.2 Key Metrics to Monitor

| Metric | Threshold for Alert | Monitoring Tool |
|--------|---------------------|-----------------|
| CPU utilisation | > 85% sustained for > 5 minutes | Windows Task Manager / Performance Monitor, Linux `top`/`htop`, Zabbix, Nagios |
| RAM utilisation | > 90% of total RAM | Same as above |
| Disk space | < 15% free on any volume | Windows Event Log, Linux `df -h`, Zabbix |
| Disk I/O latency | > 20 ms average read/write latency | Windows perfmon, Linux `iostat` |
| Network throughput | > 80% of interface capacity | SNMP-based monitoring, `iftop` (Linux) |
| Service availability | Any monitored service not responding | Nagios, Zabbix, Windows Service Monitor |
| Event log errors | New Critical or Error events | Windows Event Viewer, `/var/log/syslog`, SIEM |
| RAID status | Array not "Optimal/Online" | RAID vendor utility, mdadm (Linux) |
| Temperature | CPU > 80°C; ambient > 35°C | IPMI/BMC console |

### 4.3 Windows Server Monitoring Tools

**Performance Monitor (perfmon):**
- Open: `Win + R → perfmon`
- Add counters: Processor (_Total) % Processor Time, Memory Available MBytes, LogicalDisk % Free Space
- Create Data Collector Sets for long-term trending

**Windows Event Viewer:**
- Open: `Win + R → eventvwr`
- Key logs to review:
  - **System** — hardware and OS errors
  - **Application** — application-level errors
  - **Security** — logon events, policy changes, audit events
  - **Setup** — update and role installation events

**Resource Monitor:**
- Open: `Win + R → resmon`
- Real-time view of CPU, Memory, Disk, and Network per-process

**Server Manager — Dashboard:**
- Shows role-specific health summaries and event alerts for installed server roles

### 4.4 Linux Server Monitoring Tools

| Tool | Command / Usage | What It Shows |
|------|----------------|---------------|
| `top` | `top` | Real-time CPU and RAM usage by process |
| `htop` | `htop` | Enhanced interactive process viewer |
| `vmstat` | `vmstat 5` (refresh every 5 sec) | CPU, memory, swap, I/O, and process statistics |
| `iostat` | `iostat -xz 5` | Per-device disk I/O statistics |
| `df` | `df -h` | Disk space usage per filesystem |
| `free` | `free -h` | RAM and swap usage |
| `netstat` / `ss` | `ss -tuln` | Active network connections and listening ports |
| `journalctl` | `journalctl -p err -since "1 hour ago"` | Systemd journal — filter by priority |
| `tail` | `tail -f /var/log/syslog` | Real-time log monitoring |
| `sar` | `sar -u 1 10` | Historical performance data (requires `sysstat` package) |

### 4.5 System Log Management

Logs are the primary evidence source for diagnosing server problems. Log management tasks include:

| Task | Windows Server | Linux Server |
|------|---------------|-------------|
| Review error events | Event Viewer → Filter by Level: Critical/Error | `journalctl -p err` or `grep -i error /var/log/syslog` |
| Archive old logs | Configure Event Log maximum size and retention policy (overwrite as needed, or archive to .evtx) | Configure `logrotate` — rotate, compress, and retain logs |
| Clear application logs | Application-specific log rotation settings | `logrotate` configuration in `/etc/logrotate.d/` |
| Forward logs to SIEM | Windows Event Forwarding (WEF) or Syslog agent | `rsyslog` or `syslog-ng` forwarding to central log server |

**Log rotation example (`/etc/logrotate.d/nginx`):**
```
/var/log/nginx/*.log {
    weekly
    missingok
    rotate 12
    compress
    delaycompress
    notifempty
    sharedscripts
    postrotate
        nginx -s reopen
    endscript
}
```

---

## 5.0 Storage Maintenance

### 5.1 Disk Space Management

A server volume that fills to 100% capacity will cause the OS and applications to fail — write operations will return errors, databases may corrupt, and the OS may become unstable or unbootable.

**Windows Server — Disk Space Maintenance:**

```powershell
# Check disk space on all volumes
Get-PSDrive -PSProvider FileSystem | Select-Object Name, Used, Free

# Run Disk Cleanup (includes temporary files, Windows Update cache)
cleanmgr /sagerun:1

# Identify large files (PowerShell — find files > 1 GB)
Get-ChildItem -Path C:\ -Recurse -ErrorAction SilentlyContinue |
  Where-Object { $_.Length -gt 1GB } |
  Sort-Object Length -Descending |
  Select-Object FullName, @{Name="Size(GB)";Expression={[math]::Round($_.Length/1GB,2)}}
```

Common space consumers to clean on Windows Server:
- `C:\Windows\Temp` — temporary files
- `C:\Windows\SoftwareDistribution\Download` — Windows Update cache (clear after confirming updates are installed)
- Application log files that have not been rotated
- Shadow copies (VSS) — review and delete old snapshots if disk space is critical

**Linux — Disk Space Maintenance:**

```bash
# Check disk usage
df -h

# Find top 10 largest directories under /var
du -sh /var/* 2>/dev/null | sort -rh | head -10

# Find files larger than 500 MB
find / -xdev -size +500M -type f 2>/dev/null

# Clear package manager cache
sudo dnf clean all         # RHEL/CentOS/Rocky
sudo apt clean             # Ubuntu/Debian

# Remove old kernel packages (RHEL/CentOS — keep last 2)
sudo dnf remove --oldinstallonly --setopt installonly_limit=2 kernel
```

### 5.2 File System Health Check

| File System | Check Tool | When to Run |
|-------------|-----------|-------------|
| NTFS (Windows) | `chkdsk C: /f /r` (schedule for next boot) | When disk errors are reported in Event Viewer; annually as PM |
| ext4 (Linux) | `e2fsck -f /dev/sda1` (must be unmounted) | When filesystem errors appear in syslog; annually as PM |
| XFS (Linux) | `xfs_repair /dev/sda1` (must be unmounted) | When XFS errors appear in syslog |

### 5.3 Temporary File and Cache Cleanup

| Item | Location | Cleanup Method |
|------|----------|----------------|
| Windows Temp files | `%TEMP%`, `C:\Windows\Temp` | Disk Cleanup or manual delete |
| Windows Update cache | `C:\Windows\SoftwareDistribution\Download` | Manual delete after confirming updates applied |
| IIS logs | `C:\inetpub\logs\LogFiles\` | Compress and archive; delete logs older than retention period |
| Linux /tmp | `/tmp` | `tmpwatch` or `systemd-tmpfiles --clean` |
| Linux old kernels | `/boot` (GRUB entries) | `dnf remove --oldinstallonly` |
| Application logs | Varies by application | Configure log rotation |

---

## 6.0 User Account and Access Control Maintenance

### 6.1 Principle of Least Privilege

The principle of least privilege (prinsip keistimewaan minimum) states that every user account should have only the minimum permissions needed to perform its function. Regular access reviews enforce this principle and reduce the attack surface.

### 6.2 User Account Maintenance Tasks

| Task | Windows Server | Linux Server |
|------|---------------|-------------|
| List local user accounts | `net user` or `Get-LocalUser` | `cat /etc/passwd` or `getent passwd` |
| Disable inactive accounts | `Disable-LocalUser -Name <username>` | `usermod -L <username>` |
| Remove unnecessary accounts | `Remove-LocalUser -Name <username>` | `userdel -r <username>` |
| Review group memberships | `Get-LocalGroupMember -Group Administrators` | `groups <username>` or `id <username>` |
| Enforce password policy | Group Policy → Account Policies | `/etc/security/pwquality.conf`, `/etc/login.defs` |
| Audit privileged accounts | Review members of Administrators group | Review `/etc/sudoers` and `sudo` group membership |

### 6.3 Service Account Maintenance

Service accounts (akaun perkhidmatan) are dedicated accounts used by applications and services to run under a specific identity. They must be reviewed during OS maintenance:

- Confirm service accounts are still required (decommission if the service has been removed)
- Verify service accounts use strong passwords and that passwords are rotated per policy
- Ensure service accounts do not have interactive logon rights (they should not be able to log on to the console)
- Review service account permissions — they should only have access to the resources they need

---

## 7.0 Common Errors in Server OS Maintenance

| Error | Ralat | Consequence | Prevention |
|-------|-------|-------------|------------|
| Applying patches without testing | Menggunakan tampalan tanpa ujian | Production service disruption; application incompatibility | Always test in staging environment first |
| Not verifying backup before patching | Tidak mengesahkan sandaran sebelum tampalan | No recovery path if patch causes failure | Confirm backup is current and verified before every maintenance window |
| Ignoring disk space alerts | Mengabaikan amaran ruang cakera | Server crashes when disk fills to 100% | Monitor disk space; act when free space drops below 20% |
| Not reviewing event logs | Tidak menyemak log peristiwa | Silent failures accumulate until a major outage occurs | Review event logs at every PM cycle |
| Deleting required system files during cleanup | Memadam fail sistem yang diperlukan semasa pembersihan | OS instability or service failure | Only clean known safe locations; use built-in tools (Disk Cleanup, dnf clean) |
| Not documenting OS changes | Tidak mendokumentasikan perubahan OS | Audit failures; inability to trace root cause | Record every patch, configuration change, and account modification |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 5: Server Maintenance
- CompTIA Server+ Certification Study Guide — Chapters: OS Maintenance, Monitoring, Backup and Recovery
- Microsoft Documentation — Windows Server Update Services (WSUS), Windows Server Backup
- Red Hat Documentation — Managing and Monitoring a RHEL Server
- Ubuntu Server Guide — Security, Updates, and Backup
- NIST SP 800-40 Rev. 4 — Guide to Enterprise Patch Management Planning
- Organisational IT Maintenance Policy, Backup Policy, and Change Management Procedure