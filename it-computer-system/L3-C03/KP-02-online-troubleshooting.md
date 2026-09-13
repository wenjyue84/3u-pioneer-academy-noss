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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C03 COMPUTER SYSTEM REPAIR |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST<br>2. CARRY OUT ONLINE TROUBLESHOOTING<br>3. PERFORM ON-SITE REPAIR<br>4. PREPARE COMPUTER STATUS REPORT |
| NO. KOD | IT-020-3:2013-C03/KP(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-online-troubleshooting

**TUJUAN:** Kertas rujukan untuk KP-02-online-troubleshooting.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose, advantages, and limitations of online (remote) troubleshooting
2. Set up and use remote desktop tools to connect to and control a client's computer
3. Apply a structured troubleshooting methodology to diagnose software, driver, and configuration faults remotely
4. Use knowledge base resources and diagnostic scripts to identify and resolve common faults
5. Recognise when a remote session must be escalated to on-site repair
6. Document the outcome of a remote troubleshooting session accurately

---

## 1.0 Introduction to Online Troubleshooting

Online troubleshooting (Penyelesaian Masalah Dalam Talian) is the process of diagnosing and resolving computer faults remotely, without physical access to the unit. The technician connects to the client's computer over a network using remote access tools, then executes diagnostic and remediation steps as if seated in front of the machine.

Online troubleshooting is appropriate when:
- The fault is software-related (operating system errors, application crashes, driver conflicts, malware)
- The client is in a different location (branch office, work-from-home environment)
- The fault can be replicated in the current operating environment and does not require hardware inspection

Online troubleshooting is **not** appropriate when:
- The computer will not power on or cannot reach the network (no remote connection is possible)
- The fault is confirmed hardware (failed PSU, burnt motherboard, physically broken component)
- The user's connection speed or security policy prevents use of remote tools

---

## 2.0 Remote Access Tools

The following remote desktop and remote support tools are used in online troubleshooting:

| Tool | Type | Use Case |
|------|------|----------|
| Windows Remote Desktop (RDP) | Built-in (Windows Pro/Enterprise) | Full desktop control over LAN or VPN; requires RDP enabled on target |
| Microsoft Quick Assist | Built-in (Windows 10/11) | Screen sharing and control for same-organisation support |
| TeamViewer | Third-party | Cross-platform remote access; suitable for internet-based support |
| AnyDesk | Third-party | Lightweight remote desktop; low-bandwidth environments |
| SSH (Secure Shell) | Command-line protocol | Command-line access to Windows (via OpenSSH) or Linux systems |
| PowerShell Remoting | Built-in (Windows) | Remote execution of PowerShell scripts across the domain |

### 2.1 Enabling Windows Remote Desktop

Before a technician can connect via RDP, the following must be configured on the target computer:

1. Open **Settings → System → Remote Desktop** and toggle **Enable Remote Desktop** to On
2. Confirm the user account has Remote Desktop access rights (member of Remote Desktop Users group)
3. Ensure the firewall allows TCP port 3389 inbound
4. Note the computer's IP address or hostname for connection

### 2.2 Connecting via RDP

1. On the technician's computer, open **Remote Desktop Connection** (mstsc.exe)
2. Enter the IP address or hostname of the target computer
3. Click **Connect**, then enter the authorised credentials when prompted
4. The remote desktop session opens — the technician now has full control of the desktop

---

## 3.0 Structured Troubleshooting Methodology

Remote troubleshooting follows the same logical methodology as on-site troubleshooting. The CompTIA A+ six-step troubleshooting process is the industry-accepted standard:

| Step | Action |
|------|--------|
| 1. Identify the problem | Gather information from the user; identify symptoms; check error messages; review recent changes |
| 2. Establish a theory of probable cause | Consider the most likely causes based on symptoms; start with the simplest explanation |
| 3. Test the theory | Execute targeted checks (e.g. ping, Event Viewer, Device Manager) to confirm or eliminate the theory |
| 4. Establish a plan of action | Define the corrective steps to be taken; confirm with supervisor if changes carry risk |
| 5. Implement the solution | Execute the fix; where possible, take a system restore point before making changes |
| 6. Verify and document | Confirm the fault is resolved; test with the user; update the job order with full details |

---

## 4.0 Common Software and OS Faults — Remote Diagnosis

### 4.1 Operating System Faults

| Fault | Symptom | Remote Diagnostic Tool | Typical Resolution |
|-------|---------|------------------------|-------------------|
| Blue Screen of Death (BSOD) | System crashes with STOP error code | Event Viewer → Windows Logs → System; WinDbg for minidump analysis | Update drivers; run `sfc /scannow`; check for faulty Windows Update |
| Slow system performance | High CPU/RAM/disk usage | Task Manager (taskmgr.exe); Resource Monitor | Terminate runaway processes; disable start-up items; scan for malware |
| Windows Update failure | Update fails with error code | Settings → Update & Security; `WindowsUpdateLog` | Reset Windows Update components; use DISM to repair the component store |
| System File Corruption | Applications crash; missing DLL errors | Command Prompt (Admin): `sfc /scannow` | Run SFC; if SFC finds unfixable errors, run `DISM /Online /Cleanup-Image /RestoreHealth` |
| Profile corruption | User cannot log in; empty desktop | Event Viewer; Registry (HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList) | Create new user profile; migrate data |

### 4.2 Driver and Device Faults

| Fault | Symptom | Remote Diagnostic Tool | Typical Resolution |
|-------|---------|------------------------|-------------------|
| Unknown device | Yellow exclamation mark in Device Manager | Device Manager (devmgmt.msc) | Download and install correct driver from manufacturer website |
| Driver conflict | Device not functioning; system instability | Device Manager → View → Show hidden devices | Roll back driver; uninstall conflicting driver; reinstall in correct order |
| Network adapter issue | No network connectivity | `ipconfig /all`; `ping 127.0.0.1`; `ping gateway` | Disable/re-enable adapter; update driver; reset TCP/IP stack (`netsh int ip reset`) |

### 4.3 Application Faults

| Fault | Symptom | Diagnostic Approach | Typical Resolution |
|-------|---------|---------------------|--------------------|
| Application crash on launch | Error message or immediate closure | Event Viewer → Application log; check for .NET or Visual C++ runtime errors | Repair or reinstall application; install missing runtime |
| Licence or activation error | Application opens with activation prompt | Check system date/time; verify licence key; check internet connectivity to activation server | Re-enter licence; re-activate online; contact software vendor if persistent |
| Application performance issues | Application runs slowly or freezes | Task Manager; check available RAM and disk space | Close competing processes; increase virtual memory; check for application updates |

---

## 5.0 Diagnostic Tools and Commands

The following built-in Windows tools are used during remote troubleshooting sessions:

| Tool / Command | Purpose | How to Open |
|----------------|---------|-------------|
| `eventvwr.msc` — Event Viewer | Review system, application, and security event logs | Run → `eventvwr.msc` |
| `devmgmt.msc` — Device Manager | View device status; update, rollback, or uninstall drivers | Run → `devmgmt.msc` |
| `msconfig` — System Configuration | Manage start-up items; enable/disable services for clean-boot diagnosis | Run → `msconfig` |
| `taskmgr` — Task Manager | Monitor CPU, RAM, disk, and network usage; terminate processes | Ctrl+Shift+Esc |
| `sfc /scannow` | Scan and repair protected Windows system files | Command Prompt (Admin) |
| `DISM /Online /Cleanup-Image /RestoreHealth` | Repair the Windows component store using Windows Update | Command Prompt (Admin) |
| `ipconfig /all` | Display full TCP/IP configuration for all adapters | Command Prompt |
| `ping` / `tracert` | Test network connectivity; trace routing path | Command Prompt |
| `chkdsk C: /f /r` | Check and repair file system errors on a disk | Command Prompt (Admin); requires restart |
| `msinfo32` | Display full hardware and software system information | Run → `msinfo32` |
| `perfmon` — Performance Monitor | Capture and analyse detailed performance data over time | Run → `perfmon` |

---

## 6.0 Using the Knowledge Base

A knowledge base (Pangkalan Pengetahuan) is a structured repository of documented solutions to known problems. It is the technician's primary research resource during remote troubleshooting.

### 6.1 Types of Knowledge Base Resources

| Resource | Description |
|----------|-------------|
| Internal knowledge base | Organisation's own documented solutions from previous repair cases; accessed via helpdesk system |
| Microsoft Support (support.microsoft.com) | Official documentation for Windows error codes, BSOD analysis, and known issues |
| Vendor knowledge base | Manufacturer's support portal for product-specific driver, firmware, and fault information (e.g. Dell ProSupport, HP Support Assistant) |
| CompTIA and industry forums | Community knowledge for generic hardware and software issues |

### 6.2 Knowledge Base Search Strategy

1. **Use the exact error code or message** as the primary search term (e.g. "0x0000007E BSOD", "Error 0x80070005 Windows Update")
2. **Add the OS version** to narrow results (e.g. "Windows 11 22H2")
3. **Review multiple sources** — a single result may describe an older or unrelated scenario
4. **Verify the solution applies** to the specific hardware model and OS build before executing
5. **Record the knowledge base article reference** in the job order for audit traceability

---

## 7.0 Diagnostic Scripts

Diagnostic scripts automate repetitive information-gathering steps during remote troubleshooting. Common examples using PowerShell:

**Collect system information:**
```powershell
Get-ComputerInfo | Select-Object CsName, OsName, OsVersion, CsProcessors, CsTotalPhysicalMemory
```

**List services that have stopped unexpectedly:**
```powershell
Get-Service | Where-Object {$_.Status -eq 'Stopped' -and $_.StartType -eq 'Automatic'}
```

**Check disk health (SMART status):**
```powershell
Get-PhysicalDisk | Select-Object FriendlyName, MediaType, HealthStatus, OperationalStatus
```

**Export Event Viewer Application errors in the last 24 hours:**
```powershell
Get-EventLog -LogName Application -EntryType Error -Newest 50 | Export-Csv C:\Temp\AppErrors.csv -NoTypeInformation
```

Scripts must be run in an elevated (Administrator) PowerShell session. Results should be saved to a temporary folder and reviewed before closing the remote session.

---

## 8.0 Escalation from Online to On-Site

Online troubleshooting has clear boundaries. The technician must escalate to on-site repair when:

| Condition | Reason for Escalation |
|-----------|-----------------------|
| Computer cannot power on or reach the network | Remote connection is impossible |
| Fault is confirmed hardware (e.g. SMART failure, POST failure) | Physical component replacement required |
| Remote session is unstable due to network quality | Diagnosis cannot be completed reliably |
| Security policy prevents remote tool installation | Organisational restriction must be respected |
| Sensitive data environment (e.g. payment terminal, classified workstation) | Remote access may violate compliance requirements |

When escalating, the technician must record all remote steps taken and findings on the job order before closing the remote session. The on-site technician uses this information to avoid repeating steps.

---

## 9.0 Common Errors in Online Troubleshooting

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Making system changes without a restore point | Irreversible damage if the fix makes the fault worse | Always create a System Restore point before applying changes to OS or registry |
| Closing the remote session before verifying resolution | Fault persists; user calls back; wasted effort | Test the fix with the user before ending the session |
| Not documenting steps taken | No audit trail; the on-site technician has no history to work from | Log every action in the job order as it is performed |
| Using remote tools without user consent | Privacy and security breach | Obtain user acknowledgement before initiating remote control |
| Applying a knowledge base fix without verifying it matches the OS/hardware | New fault introduced | Cross-check OS version, build number, and hardware model before applying any fix |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 3: Computer System Repair
- CompTIA A+ Core 2 (220-1102) — Troubleshooting Operating Systems, Security, and Operational Procedures
- Microsoft Documentation: Windows Remote Desktop, Event Viewer, SFC and DISM tools
- Microsoft Support Knowledge Base: support.microsoft.com
- CompTIA A+ Troubleshooting Methodology (Six-Step Process)