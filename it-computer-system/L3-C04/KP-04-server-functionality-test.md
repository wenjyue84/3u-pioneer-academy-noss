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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/KP(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-server-functionality-test

**TUJUAN:** Kertas rujukan untuk KP-04-server-functionality-test.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and scope of server functionality testing after installation
2. Conduct hardware health verification using POST results, event logs, and vendor diagnostic tools
3. Verify OS stability, service status, and system resource availability
4. Test network connectivity and name resolution from and to the server
5. Validate installed server roles and services against the job order requirements
6. Record test results in a structured functionality test checklist

---

## 1.0 Purpose of Server Functionality Testing

Server functionality testing (ujian kefungsian pelayan) is the systematic process of verifying that every hardware component and software service installed on the server operates correctly and meets the specifications in the job order. Testing is conducted **before the server is handed over to production** to ensure that any faults are identified and resolved at the installation stage rather than during live operations.

A server that is not fully tested may exhibit failures that:
- Cause service outages affecting all users on the network
- Result in data loss if storage or RAID configuration is incorrect
- Produce intermittent errors that are difficult to diagnose after handover
- Violate the service level agreement (SLA / Perjanjian Tahap Perkhidmatan) between the IT team and the business

---

## 2.0 Hardware Health Verification

### 2.1 POST (Power-On Self-Test) Review

Every server performs a POST when powered on. The POST checks processor, memory, storage controllers, and other hardware before handing control to the OS boot loader.

| POST Indicator | Meaning | Action |
|----------------|---------|--------|
| All LEDs green; no beep codes | Hardware detected and healthy | Proceed to OS verification |
| Amber LED on front panel | Hardware fault detected | Check System Event Log (SEL) in BIOS or BMC |
| Beep codes (multiple beeps) | Specific hardware fault (varies by vendor) | Refer to vendor documentation for beep code meaning |
| POST stops at memory count | Memory error; DIMM not seated or faulty | Reseat DIMMs; replace faulty module |
| POST stops at RAID controller | RAID controller or drive fault | Check RAID controller BIOS for drive status |

### 2.2 System Event Log (SEL) Review

The **System Event Log (SEL)** is stored in the server's BMC and records hardware events (temperature, voltage, fan speed, drive failures) independent of the OS. Review the SEL after first boot:

- Access via BIOS/UEFI setup utility → Server Management → System Event Log
- Access via BMC web interface (iDRAC/iLO) → Server Health → System Event Log
- Access via IPMI command: `ipmitool sel list`

Clear any pre-existing log entries from factory testing, then run the server for at least 30 minutes and re-check the SEL for new events.

### 2.3 Memory Diagnostic

| Tool | Platform | Purpose |
|------|----------|---------|
| MemTest86+ | Bootable (cross-platform) | Comprehensive RAM test; detects bit errors, addressing errors; run overnight for thorough testing |
| Windows Memory Diagnostic | Windows Server | Built-in; run via `mdsched.exe`; basic pass; less thorough than MemTest86+ |
| Vendor memory test (e.g. Dell Diagnostics) | Boot from vendor utility | Vendor-validated memory test integrated with hardware reporting |

For production servers, run at least one full pass of MemTest86+ before OS installation, or run after OS installation if memory errors are suspected.

### 2.4 Storage and RAID Verification

| Check | Tool / Method |
|-------|--------------|
| All drives detected | RAID controller BIOS / UEFI storage management; vendor RAID utility |
| RAID array status is Optimal | RAID controller BIOS shows "Optimal" or equivalent; no degraded or failed drives |
| Drive health (S.M.A.R.T. data) | Vendor RAID utility; `smartctl -a /dev/sdX` (Linux); check Reallocated Sectors, Pending Sectors, Uncorrectable Errors — all should be 0 |
| RAID read/write test | Run a sequential and random I/O test using CrystalDiskMark (Windows) or `fio` (Linux) to verify expected throughput |
| BBU (Battery Backup Unit) status | RAID controller utility: BBU should show "Healthy" and charge level ≥ 80% |

**RAID Logical Drive Verification Checklist:**

| Item | Expected Value |
|------|---------------|
| Number of logical drives | As specified in job order |
| RAID level | As specified in job order (e.g. RAID 10) |
| Total logical drive capacity | Matches calculated usable capacity for the RAID level |
| Drive cache policy | Write-Back (when BBU healthy); Write-Through (when BBU absent or depleted) |
| Array status | Optimal |

### 2.5 Temperature and Cooling Verification

| Check | Acceptable Range | Tool |
|-------|-----------------|------|
| CPU temperature at idle | Typically 25–55°C (varies by CPU TDP and cooling) | BMC/iDRAC web interface → Sensors; `ipmitool sdr type Temperature` |
| CPU temperature under load | Below T_junction max (e.g. 95°C for Xeon Scalable) | Run a CPU stress test (Prime95, `stress-ng`) for 10 minutes; monitor via BMC |
| Inlet air temperature | Below 35°C (ASHRAE Class A1: 15–32°C recommended) | BMC temperature sensors (Inlet Temp) |
| Fan speeds | All fans spinning at or above minimum RPM threshold | BMC/iDRAC → Sensors → Fan |

---

## 3.0 Operating System Verification

### 3.1 System Event Log (Windows)

In Windows Server, the **Event Viewer (Pemapar Peristiwa)** records OS, application, and security events.

| Log | What to Check |
|-----|--------------|
| System log | Errors and warnings from OS components and drivers at startup; look for driver errors, disk errors (Event ID 7, 11, 51) |
| Application log | Application-level errors; verify no critical errors from installed services |
| Setup log | Errors during OS installation or role installation |
| Security log | Verify audit logging is active; check for any unexpected logon failures |

No **Error** or **Critical** entries should be present in the System log for a freshly installed server. Warnings are common for informational purposes but must be reviewed.

### 3.2 Services Status Verification (Windows)

Open **Services (services.msc)** or use PowerShell:
```powershell
Get-Service | Where-Object {$_.Status -eq 'Stopped' -and $_.StartType -eq 'Automatic'}
```
All services set to **Automatic** start type should be in **Running** state. Stopped automatic services indicate a configuration or dependency error.

### 3.3 System Resource Baseline (Windows)

Use **Task Manager** or **Performance Monitor (perfmon)** to record baseline resource utilisation immediately after installation (before production load):

| Resource | Expected Baseline (Idle) |
|----------|--------------------------|
| CPU utilisation | < 10% at idle |
| RAM utilisation | < 30% at idle (varies by roles installed) |
| Disk I/O | Low; no sustained 100% disk utilisation |
| Network utilisation | < 1% at idle |

### 3.4 Linux System Verification

| Check | Command |
|-------|---------|
| System uptime and load | `uptime` |
| Failed systemd services | `systemctl --failed` |
| Kernel messages (hardware errors) | `dmesg | grep -i error` |
| Disk and filesystem check | `df -h` (free space); `lsblk` (block devices); `cat /proc/mdstat` (software RAID status if applicable) |
| Memory usage | `free -h` |
| Running processes | `top` or `htop` |
| Network interfaces | `ip addr show`; `ip route show` |

---

## 4.0 Network Connectivity Testing

Network testing verifies that the server can communicate with the network and that required services are reachable.

### 4.1 Basic Connectivity Tests

| Test | Command (Windows) | Command (Linux) | Expected Result |
|------|-------------------|-----------------|----------------|
| Loopback test | `ping 127.0.0.1` | `ping 127.0.0.1` | Replies from local network stack; verifies TCP/IP is functional |
| Gateway reachability | `ping <gateway IP>` | `ping <gateway IP>` | Replies from default gateway; verifies Layer 3 connectivity |
| DNS server reachability | `ping <DNS server IP>` | `ping <DNS server IP>` | Replies from DNS server |
| Internet reachability | `ping 8.8.8.8` | `ping 8.8.8.8` | Replies from Google DNS (if internet access permitted) |
| Hostname resolution | `nslookup google.com` | `nslookup google.com` | Returns IP address; verifies DNS resolution |
| Reverse DNS lookup | `nslookup <server IP>` | `nslookup <server IP>` | Returns server FQDN; verifies reverse DNS record |

### 4.2 Network Port and Service Tests

| Test | Command | Purpose |
|------|---------|---------|
| Test TCP port connectivity | `Test-NetConnection <IP> -Port <port>` (PS) / `nc -zv <IP> <port>` (Linux) | Verify specific service ports are open and listening |
| View listening ports | `netstat -an` or `Get-NetTCPConnection` (PS) | Confirm server is listening on expected ports (e.g. 443 for HTTPS, 389 for LDAP) |
| Firewall rule verification | `Get-NetFirewallRule` (PS) / `ufw status verbose` (Linux) | Verify firewall permits required traffic and blocks unrequired ports |

### 4.3 NIC Teaming / Bonding Verification (if configured)

If the job order specifies NIC teaming (Windows) or bonding (Linux) for redundancy or load balancing:

| Check | Method |
|-------|--------|
| Team/bond interface created | Network Adapter settings (Windows) / `cat /proc/net/bonding/bond0` (Linux) |
| Both member NICs active | Team properties → Adapters tab; bonding status shows both slaves active |
| Failover test | Disconnect one NIC cable; verify network connectivity is maintained; reconnect and verify both NICs active again |

---

## 5.0 Server Role Functionality Testing

After verifying hardware, OS, and network, test each installed server role individually.

### 5.1 Active Directory Domain Services (AD DS) Test

| Test | Command / Tool | Expected Result |
|------|---------------|----------------|
| DCDIAG (DC Diagnostics) | `dcdiag /test:all /v` | All tests Pass; no Failures |
| Replication check | `repadmin /showrepl` | Replication successful to all DC partners; no errors |
| NETLOGON service | `Get-Service Netlogon` | Running |
| DNS SRV records | `nslookup -type=SRV _ldap._tcp.<domain>` | Returns DC IP address; confirms AD DNS records are registered |
| SYSVOL share accessible | `dir \\<domain>\SYSVOL` | SYSVOL contents visible; confirms SYSVOL replication is functional |
| User authentication test | Log in to a domain-joined test PC using a domain user account | Successful authentication; user profile loads |

### 5.2 DNS Test

| Test | Command | Expected Result |
|------|---------|----------------|
| Forward lookup | `nslookup <hostname>.<domain>` | Returns correct IP address |
| Reverse lookup | `nslookup <IP address>` | Returns correct FQDN |
| External resolution via forwarder | `nslookup google.com <DNS server IP>` | Returns IP for google.com; confirms forwarder is working |
| Zone transfer | DNS Manager → right-click zone → Reload | Zone reloads without error |

### 5.3 DHCP Test

| Test | Method | Expected Result |
|------|--------|----------------|
| Scope active | DHCP Manager → Scope status shows Active | Active |
| Client IP assignment | Connect a test device; set NIC to DHCP; check assigned IP | IP assigned within scope range; gateway and DNS populated correctly |
| DHCP lease visible | DHCP Manager → Address Leases | Test device lease visible with correct MAC address and lease expiry |

### 5.4 File Server Test

| Test | Method | Expected Result |
|------|--------|----------------|
| Share accessible | From a client PC: `\\<server name>\<share name>` | Share opens; correct files visible |
| Read/write permissions | Create a test file in the share; delete it | File created and deleted without permission errors (for authorised user) |
| Shadow Copies | Right-click a test file → Restore previous versions | Previous version available if shadow copies are configured |

### 5.5 Web Server (IIS / Apache) Test

| Test | Method | Expected Result |
|------|--------|----------------|
| Default website | Open browser → `http://<server IP>` | Default IIS or Apache page loads |
| HTTPS (if configured) | Open browser → `https://<server IP or FQDN>` | Page loads; SSL certificate valid; no browser warnings |
| Application pool status (IIS) | IIS Manager → Application Pools | All pools in Started state |

---

## 6.0 Functionality Test Checklist

Use this checklist to record the outcome of all tests. Each item must be signed off before the server is released to production.

| # | Test Category | Test Item | Expected Result | Actual Result | Pass/Fail | Technician Initials |
|---|--------------|-----------|----------------|---------------|-----------|-------------------|
| 1 | Hardware | POST completes without errors | No error codes | | | |
| 2 | Hardware | All processors detected in BIOS | Count matches job order | | | |
| 3 | Hardware | Total RAM detected | Matches job order (GB) | | | |
| 4 | Hardware | All drives detected by RAID controller | Count matches job order | | | |
| 5 | Hardware | RAID array status | Optimal | | | |
| 6 | Hardware | All fans operating | All fans spinning | | | |
| 7 | Hardware | CPU temperature at idle | < 55°C | | | |
| 8 | OS | OS boots to login screen | Login screen displayed | | | |
| 9 | OS | No Critical/Error events in System Event Log | No errors | | | |
| 10 | OS | All Automatic services running | 0 stopped Automatic services | | | |
| 11 | OS | Windows activation status | Activated | | | |
| 12 | Network | Ping gateway | Replies received | | | |
| 13 | Network | Ping DNS server | Replies received | | | |
| 14 | Network | DNS name resolution | Correct IP returned | | | |
| 15 | Role: AD DS | DCDIAG all tests pass | All Pass | | | |
| 16 | Role: DNS | Forward and reverse lookup correct | Correct results | | | |
| 17 | Role: DHCP | Client receives IP from scope | IP assigned correctly | | | |
| 18 | Role: File Server | Share accessible from client | Share opens | | | |
| 19 | Role: File Server | Read/write permissions correct | Files created/deleted | | | |
| 20 | BMC | BMC web interface accessible | Login page loads | | | |

---

## 7.0 Common Errors in Server Functionality Testing

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Skipping hardware health check before OS testing | OS-level symptoms attributed to software when root cause is hardware | Always verify hardware (POST, SEL, RAID, temperature) before OS tests |
| Not running DCDIAG after AD DS promotion | Undetected replication or DNS registration failures surface during production | Run DCDIAG /test:all immediately after promotion; resolve all failures |
| Testing only from the server itself | Network path from clients to server not verified | Always test from a separate client machine on the same subnet and from a different VLAN |
| Marking test as "Pass" without recording actual result | Incomplete audit trail; cannot reproduce issue if fault occurs later | Record actual observed result (not just tick Pass) in the test checklist |
| Not testing failover for RAID or NIC teaming | Redundancy assumed but not confirmed; silent failure discovered only during real fault | Simulate drive pull or NIC cable disconnect; verify recovery within test window |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 4: Server Installation
- Microsoft Learn — DCDIAG reference: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/dcdiag
- CompTIA Server+ Study Guide (SK0-005) — Chapter on Server Testing and Troubleshooting
- Dell EMC PowerEdge Server Diagnostics Guide
- ASHRAE Thermal Guidelines for Data Processing Environments (4th Edition)
- smartmontools documentation: https://www.smartmontools.org/