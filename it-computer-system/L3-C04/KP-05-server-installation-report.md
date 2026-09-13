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
| NO. KOD | IT-020-3:2013-C04/KP(5/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-05-server-installation-report

**TUJUAN:** Kertas rujukan untuk KP-05-server-installation-report.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and importance of a server installation set-up report
2. Identify the mandatory sections of a server installation report
3. Record hardware inventory, software configuration, and network settings accurately
4. Compile test results and outstanding issues into the report
5. Prepare the report for formal handover and obtain client or supervisor sign-off

---

## 1.0 Purpose of the Server Installation Report

The **server installation set-up report (laporan pemasangan pelayan)** is the formal written record that documents everything that was installed, configured, and tested during the server installation project. It is produced at the completion of the installation and submitted to the client, IT manager, or supervisor as the official deliverable of the work.

The report serves three purposes:

| Purpose | Description |
|---------|-------------|
| Accountability (Akauntabiliti) | Provides an auditable record of who did what, when, and with what result — protects both the technician and the organisation |
| Reference (Rujukan) | Becomes the definitive record for future maintenance, upgrades, or troubleshooting. Without it, the next technician has no knowledge of what was installed |
| Handover (Serah terima) | Formally transfers responsibility for the server from the installation team to the operations team or client. The client's signature acknowledges acceptance |

A server installation without a completed and signed report is considered **incomplete**, regardless of how well the physical work was done.

---

## 2.0 Structure of the Server Installation Report

A complete server installation report contains the following sections:

| Section | Content |
|---------|---------|
| 1. Cover page | Report title, server name/hostname, job order number, date, prepared by, reviewed by |
| 2. Job order reference | Original job order number, description, requestor, approver, and any approved change requests |
| 3. Hardware inventory | Full list of installed hardware components with model numbers, serial numbers, and firmware versions |
| 4. Software and OS configuration | OS name, version, edition, activation status, installed roles and features, patch level |
| 5. Network configuration | Hostname, IP address, subnet mask, gateway, DNS servers, NIC details, VLAN |
| 6. Storage and RAID configuration | Drive details, RAID level, logical drive size, controller details |
| 7. Server roles and services configuration | Details of each installed role — domain name, DHCP scope, share names, etc. |
| 8. Functionality test results | Completed functionality test checklist (from KP-04) with pass/fail results |
| 9. Outstanding issues | Any items not completed, known issues, or deferred actions |
| 10. Recommendations | Suggested follow-up actions (e.g. firmware update scheduled, capacity monitoring) |
| 11. Sign-off | Technician signature, supervisor signature, client/requestor acceptance signature, and dates |

---

## 3.0 Section-by-Section Guidance

### 3.1 Cover Page

The cover page must be professional and clearly identify the document:

| Field | Example |
|-------|---------|
| Report title | Server Installation Set-Up Report |
| Server hostname | SRV-AD-01 |
| Job order number | JO-2024-0042 |
| Location / rack position | DC-1, Rack R-05, U12–U13 |
| Date of installation | 18–20 March 2024 |
| Date of report | 20 March 2024 |
| Prepared by | Technician name, designation |
| Reviewed by | Supervisor name, designation |
| Report reference number | RPT-2024-SRV-0042 |

### 3.2 Hardware Inventory

Record every hardware component installed. This inventory becomes the server's asset record.

| Component | Details to Record |
|-----------|-----------------|
| Server chassis | Vendor, model, serial number, asset tag |
| Processor(s) | Model, socket, core count, clock speed, quantity |
| Memory (RAM) | Type (RDIMM/LRDIMM), capacity per DIMM, speed, quantity, slot positions populated |
| Storage drives | Vendor, model, capacity, interface (SAS/SATA/NVMe), serial number, bay position — for each drive |
| RAID controller | Vendor, model, firmware version, BBU status |
| Network interface cards | Vendor, model, port count, speed, PCIe slot position — for each NIC |
| Power supply units | Vendor, model, rated wattage, quantity |
| Additional expansion cards | Any other PCIe cards (HBA, GPU, etc.) |
| Rail kit / CMA | Vendor and model |
| Firmware versions | BIOS/UEFI version, BMC firmware version, RAID controller firmware, NIC firmware |

**Example hardware inventory table:**

| Component | Vendor | Model | Serial No. | Firmware/Version | Qty |
|-----------|--------|-------|------------|-----------------|-----|
| Server chassis | Dell | PowerEdge R750 | DELL-SN-001 | BIOS 1.8.2 | 1 |
| Processor | Intel | Xeon Silver 4314 | — | Microcode 0xD0003A5 | 2 |
| RAM | Samsung | 32 GB DDR4 ECC RDIMM 3200 | — | — | 8 |
| SAS SSD | Seagate | 1.92 TB SAS 12 Gb/s | SSN-0001 to SSN-0004 | SSD-FW 2.01 | 4 |
| RAID controller | Dell | PERC H755 | — | FW 52.20.0-4516 | 1 |
| NIC (onboard) | Broadcom | 2 × 1GbE | — | FW 22.62.x | 1 |
| NIC (PCIe) | Intel | X710 2 × 10GbE | — | FW 9.2.x | 1 |
| PSU | Dell | 800 W Platinum | — | — | 2 |

### 3.3 Software and OS Configuration

| Item | Details to Record |
|------|-----------------|
| Operating system | Full name, version, build number, edition (e.g. Windows Server 2022 Datacenter, Build 20348) |
| Activation status | Activated / Volume Licence (KMS) / MAK — include activation ID if applicable |
| Service Pack / Patch level | Latest cumulative update installed (KB number and date) |
| Installed roles and features | List all Windows Server roles and features installed (e.g. AD DS, DNS, DHCP, File and Storage Services) |
| Installed applications | Any additional software installed (e.g. vendor management agent, antivirus, backup agent) with version numbers |
| Local user accounts | Names of local administrator accounts created (do not record passwords in the report) |

### 3.4 Network Configuration

| Item | Value |
|------|-------|
| Hostname (FQDN) | SRV-AD-01.company.local |
| IP address | 192.168.10.10 |
| Subnet mask | 255.255.255.0 (/24) |
| Default gateway | 192.168.10.1 |
| Primary DNS server | 192.168.10.10 (self, after AD DS promotion) |
| Secondary DNS server | 192.168.10.11 (secondary DC) |
| NIC 1 (onboard, management) | Port 1 — connected to management VLAN; MAC address: XX:XX:XX:XX:XX:01 |
| NIC 2 (PCIe 10GbE) | Ports 1 & 2 — LACP team "TeamProd"; connected to production VLAN 10; switch ports SW1:Gi0/1 and SW1:Gi0/2 |
| BMC/iDRAC IP address | 192.168.1.10 (management network) |
| VLAN | Production: VLAN 10; Management: VLAN 100 |

### 3.5 Storage and RAID Configuration

| Item | Details |
|------|---------|
| RAID controller | Dell PERC H755, firmware 52.20.0-4516 |
| Physical drives | 4 × Seagate 1.92 TB SAS SSD (Bays 0–3) |
| RAID level | RAID 10 |
| Logical drive size | 3.84 TB usable |
| Logical drive name | "OS+Data" |
| Drive cache policy | Write-Back (BBU present and healthy) |
| BBU status | Healthy, charge 100% |
| Stripe size | 256 KB |

### 3.6 Server Roles and Services Configuration

Document the key configuration parameters of each installed role:

**Active Directory Domain Services:**

| Item | Value |
|------|-------|
| Domain name (FQDN) | company.local |
| NetBIOS domain name | COMPANY |
| Forest functional level | Windows Server 2016 |
| Domain functional level | Windows Server 2016 |
| FSMO roles held | PDC Emulator, RID Master, Infrastructure Master, Schema Master, Domain Naming Master (first DC) |
| SYSVOL replication | DFSR |

**DHCP Server:**

| Item | Value |
|------|-------|
| Scope name | LAN_Scope_VLAN10 |
| IP address range | 192.168.10.50 – 192.168.10.200 |
| Subnet mask | 255.255.255.0 |
| Default gateway | 192.168.10.1 |
| DNS server | 192.168.10.10 |
| Lease duration | 8 hours |
| Exclusions | 192.168.10.1 – 192.168.10.49 (static devices) |

### 3.7 Functionality Test Results Summary

Attach the completed functionality test checklist (from KP-04) as an appendix and provide a summary:

| Category | Tests Conducted | Passed | Failed | Remarks |
|----------|----------------|--------|--------|---------|
| Hardware health | 7 | 7 | 0 | All hardware tests passed |
| Operating system | 4 | 4 | 0 | No errors in event log; all services running |
| Network connectivity | 5 | 5 | 0 | All connectivity tests passed |
| AD DS role | 3 | 3 | 0 | DCDIAG all pass; replication healthy |
| DNS role | 3 | 3 | 0 | Forward and reverse lookup correct |
| DHCP role | 2 | 2 | 0 | Test client received IP correctly |
| **Total** | **24** | **24** | **0** | **Server ready for production** |

### 3.8 Outstanding Issues and Deferred Actions

Record any items that were not completed during the installation, known limitations, or actions deferred for a later date:

| # | Issue / Deferred Action | Impact | Target Date | Owner |
|---|------------------------|--------|-------------|-------|
| 1 | RAID controller firmware update pending — latest version not available during installation window | Low — current firmware is stable | 30 March 2024 | IT Infrastructure Team |
| 2 | SSL certificate for IIS not yet provisioned — awaiting CA approval | Medium — HTTPS not functional | 25 March 2024 | IT Security Team |

If there are no outstanding issues, state: **"No outstanding issues. Server is fully operational as per job order requirements."**

### 3.9 Recommendations

Provide forward-looking recommendations for the operations team:

1. **Monitoring:** Enrol the server in the centralised monitoring system (e.g. Zabbix, Nagios, PRTG) within 7 days of handover to enable real-time alerting for CPU, RAM, disk, and network thresholds.
2. **Backup:** Configure the server backup job in the backup solution (e.g. Veeam, Windows Server Backup) with a daily full backup and hourly incremental. Verify the first backup job completes successfully.
3. **Firmware updates:** Schedule a maintenance window within 30 days to apply the pending RAID controller firmware update (see Outstanding Issues).
4. **Capacity planning:** Review RAM and storage utilisation after 30 days of production operation to confirm the specification meets actual workload demands.
5. **AD DS:** Add a second domain controller within 30 days for fault tolerance. A single DC is a single point of failure for all authentication and directory services.

---

## 4.0 Handover and Sign-Off

The handover process formally transfers the server from the installation team to the client or operations team.

### 4.1 Handover Procedure

| Step | Action |
|------|--------|
| 1 | Present the completed server installation report to the client or supervisor |
| 2 | Walk through each section of the report, explaining the configuration and test results |
| 3 | Demonstrate key functions (login, network share access, domain join of a test PC) in the client's presence |
| 4 | Address any questions or concerns raised by the client |
| 5 | Obtain signatures on the sign-off section of the report |
| 6 | Provide the client with a copy of the signed report (physical or electronic) |
| 7 | File the original signed report in the job management system |

### 4.2 Sign-Off Section

The sign-off section must be included at the end of the report:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Technician (Juruteknik) | | | |
| Supervisor (Penyelia) | | | |
| Client / Requestor (Pelanggan / Pemohon) | | | |

**Client acceptance statement:**

> *"I confirm that the server installation described in this report has been completed to my satisfaction and in accordance with the job order requirements. I accept the server for production use."*

---

## 5.0 Report Filing and Records Management

| Requirement | Detail |
|-------------|--------|
| Filing format | Physical (printed, signed, filed in job folder) AND electronic (PDF, stored in the IT asset management system) |
| Retention period | Minimum 3 years from date of installation (or as specified by organisational policy) |
| Version control | If the report is revised after sign-off, issue a new version (v1.1, v1.2) with a change log |
| Confidentiality | Server configuration reports contain sensitive network and security information — treat as **Confidential (Sulit)**; restrict access to authorised IT staff |

---

## 6.0 Common Errors in Server Installation Report Preparation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Recording incorrect serial numbers | Asset register mismatch; difficulty tracking warranty claims | Verify serial numbers from physical server labels, not from documentation |
| Omitting firmware versions | Cannot determine if firmware was current at installation; complicates future troubleshooting | Record firmware versions from BIOS/UEFI and vendor utility immediately after installation |
| Leaving outstanding issues section blank when issues exist | Client unaware of incomplete items; disputes at handover | Document all outstanding issues honestly, even minor ones |
| Signing off without performing the handover walkthrough | Client has not understood what was installed; disputes later | Conduct the walkthrough; document that it was done |
| Not filing the report electronically | Physical copy lost; no record available for future reference | Always scan and file in the IT asset management system on the day of handover |
| Recording passwords in the report | Security breach if report is accessed by unauthorised persons | Never record passwords in reports; use a separate, secured password manager |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 4: Server Installation
- CompTIA Server+ Study Guide (SK0-005) — Chapter on Documentation
- ISO/IEC 27001:2022 Information Security Management — documentation requirements
- MS-900 Microsoft 365 Fundamentals — cloud and hybrid server documentation best practices
- Organisational IT asset management and records retention policy