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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C06 COMPUTER NETWORK CONNECTIVITY SET-UP |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER NETWORK CONFIGURATION SPECIFICATION<br>2. CARRY OUT COMPUTER NETWORK CONFIGURATION<br>3. PERFORM COMPUTER NETWORK CONNECTIVITY TEST<br>4. CARRY OUT COMPUTER NETWORK TROUBLESHOOT<br>5. PREPARE COMPUTER NETWORK CONNECTIVITY REPORT |
| NO. KOD | IT-020-3:2013-C06/KP(5/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-05-network-connectivity-report

**TUJUAN:** Kertas rujukan untuk KP-05-network-connectivity-report.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and audience of a network connectivity report.
2. Identify the required sections of a formal network connectivity report.
3. Record configuration parameters, test results, and fault findings accurately.
4. Prepare a network as-built diagram and an IP address register as supporting appendices.
5. Write clear, professional, and government-standard report language suitable for submission and handover.

---

## 1.0 Introduction to Network Connectivity Reports

A **network connectivity report** is the formal written record that documents what was planned, what was configured, what was tested, and what problems were found and resolved during a computer network connectivity set-up project. It is the primary deliverable at the end of CoCu 6 work activities.

The report serves multiple purposes:

| Purpose | Audience |
|---------|----------|
| Evidence of completed work | Client, supervisor, or JPK assessor |
| Handover document | IT administrator who will manage the network after installation |
| Baseline record | Future troubleshooting reference — "what the network looked like when it was working" |
| Compliance record | Confirms the installation meets the approved specification and organisational standards |
| Audit trail | Documents all faults found and resolved, including who performed each action |

A report that is incomplete, inaccurate, or unprofessional reflects poorly on the technician and the organisation. Every parameter must be verified against the physical configuration — reports are not written from memory.

---

## 2.0 Report Structure

A complete network connectivity report contains the following sections:

| Section | Content |
|---------|---------|
| 1. Cover Page | Project name, site name, date, technician name and ID, supervisor name, organisation |
| 2. Table of Contents | Numbered sections with page references |
| 3. Project Overview | Purpose of the network installation, scope of work, site address, number of users |
| 4. Network Summary | Topology used, number of devices configured, VLANs created, services deployed |
| 5. Device Configuration Record | For each device: hostname, IP, role, VLAN membership, services enabled, firmware version |
| 6. IP Address Register | Complete table of all assigned IP addresses — verified against actual device configuration |
| 7. Connectivity Test Results | Structured test record showing each test, command, expected result, actual result, and pass/fail |
| 8. Fault and Resolution Log | Each fault found during testing: description, root cause, resolution, verification |
| 9. As-Built Network Diagram | Final diagram reflecting the actual installed configuration (may differ from the original spec) |
| 10. Recommendations | Any items that deviate from best practice or that require follow-up action |
| 11. Conclusion | Summary statement that the installation meets the specification (or states what does not) |
| 12. Appendices | Supporting data: cable schedule, VLAN plan, DHCP scope details, original specification |
| 13. Sign-Off Page | Technician declaration, supervisor verification, client acceptance |

---

## 3.0 Cover Page

The cover page is the first impression of the report. It must contain:

- **Report title:** Computer Network Connectivity Report
- **Project / site name:** (e.g., Pejabat Daerah Seremban — LAN Set-up)
- **Prepared by:** Full name and IC/staff number of the technician
- **Designation:** (e.g., ICT Technician / Pelatih Tahap 3)
- **Date of submission:** (DD/MM/YYYY)
- **Reviewed by:** Supervisor name and signature
- **Organisation logo** (if applicable)
- **Document version:** (e.g., v1.0)
- **Status:** Final / Draft

---

## 4.0 Project Overview

The project overview provides context so that a reader with no prior knowledge of the project can understand the scope of work without reading the specification.

Write in full sentences. Include:

1. **Background:** Why the network was installed or upgraded (e.g., new office premises, increased headcount, replacement of obsolete equipment).
2. **Scope of work:** What was included — cabling, switch configuration, router configuration, wireless AP, DHCP/DNS, testing, and reporting.
3. **Out of scope:** What was explicitly excluded (e.g., WAN provisioning by ISP, server operating system installation).
4. **Site details:** Building name, floor, number of rooms or workstations.
5. **Key dates:** Date specification received, date work commenced, date testing completed, date report submitted.
6. **Technician(s):** Name and role of each person involved.

---

## 5.0 Device Configuration Record

For each network device configured, record the following:

### 5.1 Router

| Parameter | Value |
|-----------|-------|
| Hostname | GW-ROUTER-01 |
| Model | Cisco ISR 4321 |
| Firmware version | IOS XE 17.6.1 |
| LAN interface | GigabitEthernet0/0 — IP: 192.168.10.1/24 |
| WAN interface | GigabitEthernet0/1 — DHCP (ISP-assigned) |
| DHCP scope | 192.168.10.100 – 192.168.10.200; exclusions: .1 – .99 |
| DNS configured | 192.168.10.10 (primary), 8.8.8.8 (secondary) |
| NAT | PAT (overload) on GigabitEthernet0/1 |
| Remote management | SSH enabled; Telnet disabled |
| Date configured | 23/06/2026 |
| Configured by | (Technician name) |

### 5.2 Switch

| Parameter | Value |
|-----------|-------|
| Hostname | SW-ACCESS-01 |
| Model | Cisco Catalyst 2960-X |
| Firmware version | IOS 15.2(7)E6 |
| VLANs | VLAN 10 — MANAGEMENT; VLAN 20 — STAFF; VLAN 30 — GUEST |
| Trunk ports | GigabitEthernet0/1 (to router); GigabitEthernet0/2 (to SW-ACCESS-02) |
| Access ports | Fa0/1–Fa0/8 — VLAN 20; Fa0/9–Fa0/16 — VLAN 30 |
| Management IP | VLAN 10 SVI: 192.168.10.2/24 |
| Default gateway | 192.168.10.1 |
| Port security | Enabled on all access ports; maximum 1 MAC; violation: shutdown |
| Date configured | 23/06/2026 |
| Configured by | (Technician name) |

### 5.3 Wireless Access Point

| Parameter | Value |
|-----------|-------|
| Hostname | AP-OFFICE-01 |
| Model | Ubiquiti UniFi AP-AC-Lite |
| Firmware version | 6.6.55 |
| Management IP | 192.168.10.3/24 (static) |
| SSID (Staff) | OFFICE_STAFF — VLAN 20 — WPA2-AES |
| SSID (Guest) | OFFICE_GUEST — VLAN 30 — WPA2-AES — client isolation enabled |
| Channel (2.4 GHz) | 6 |
| Channel (5 GHz) | 36 |
| PoE source | SW-ACCESS-01 Fa0/24 (802.3af) |
| Date configured | 23/06/2026 |
| Configured by | (Technician name) |

---

## 6.0 IP Address Register

The IP address register is a complete table of every IP address assigned in the network. It must be verified against the actual device configurations — not copied from the specification.

| Device | Hostname | Role | VLAN | IP Address | Subnet Mask | Gateway | MAC Address | Allocation Method |
|--------|----------|------|------|------------|-------------|---------|-------------|-------------------|
| Router | GW-ROUTER-01 | Gateway / NAT / DHCP | — | 192.168.10.1 | 255.255.255.0 | — | 00:AA:BB:CC:DD:01 | Static |
| Switch | SW-ACCESS-01 | Access switch | 10 | 192.168.10.2 | 255.255.255.0 | 192.168.10.1 | 00:AA:BB:CC:DD:02 | Static |
| Wireless AP | AP-OFFICE-01 | Wireless AP | 10 | 192.168.10.3 | 255.255.255.0 | 192.168.10.1 | 00:AA:BB:CC:DD:03 | Static |
| File Server | FILESERVER-01 | File / DNS server | 20 | 192.168.10.10 | 255.255.255.0 | 192.168.10.1 | 00:AA:BB:CC:DD:10 | Static |
| PC-01 | PC-FINANCE-01 | Staff workstation | 20 | 192.168.10.101 | 255.255.255.0 | 192.168.10.1 | 00:AA:BB:CC:DD:A1 | DHCP |
| PC-02 | PC-FINANCE-02 | Staff workstation | 20 | 192.168.10.102 | 255.255.255.0 | 192.168.10.1 | 00:AA:BB:CC:DD:A2 | DHCP |
| Printer | PRINTER-01 | Network printer | 20 | 192.168.10.50 | 255.255.255.0 | 192.168.10.1 | 00:AA:BB:CC:DD:50 | Static |

**Notes:**
- DHCP pool: 192.168.10.100 – 192.168.10.200 (101 addresses available for dynamic assignment).
- Addresses 192.168.10.1 – 192.168.10.99 excluded from DHCP pool.
- All static addresses verified against `ipconfig /all` or `show running-config`.

---

## 7.0 Connectivity Test Results Summary

The test results section summarises the outcome of the structured connectivity tests performed in the testing phase (CoCu 6, Work Activity 3). The full detailed test record is attached as Appendix A.

| Test No. | Test | Method | Result |
|----------|------|--------|--------|
| 1 | Loopback test — all PCs | `ping 127.0.0.1` | Pass — all 8 PCs |
| 2 | LAN connectivity — wired | `ping <gateway>` from all PCs | Pass — all 8 PCs |
| 3 | LAN connectivity — wireless | `ping <gateway>` from 3 laptops | Pass — all 3 laptops |
| 4 | Inter-VLAN routing | `ping` from VLAN 20 to VLAN 10 | Pass |
| 5 | DHCP assignment | `ipconfig /all` — DHCP clients | Pass — 6/6 clients received correct address, mask, gateway, DNS |
| 6 | DNS resolution — internal | `nslookup fileserver.office.local` | Pass — correct IP returned |
| 7 | DNS resolution — external | `nslookup www.google.com` | Pass — resolved via forwarder |
| 8 | Internet reachability | `ping 8.8.8.8` | Pass — all PCs |
| 9 | Internet via hostname | `ping www.google.com` | Pass — all PCs |
| 10 | Path trace to internet | `tracert 8.8.8.8` | Pass — 4 hops |

**Overall result: PASS** — All 10 tests passed. No outstanding failures.

---

## 8.0 Fault and Resolution Log

Document every fault discovered during configuration and testing. Faults that were resolved are not failures — they demonstrate thorough testing.

| Fault ID | Date | Description | Root Cause | Resolution | Verified By |
|----------|------|-------------|------------|------------|-------------|
| FLT-001 | 23/06/2026 | PC-01 received APIPA address instead of DHCP | Fa0/1 assigned to VLAN 30 instead of VLAN 20; DHCP scope only serves VLAN 20 | Corrected port VLAN: `switchport access vlan 20`; ran `ipconfig /renew` | `ipconfig /all` — correct address 192.168.10.101 received |
| FLT-002 | 23/06/2026 | `nslookup www.google.com` failed from all PCs | DNS forwarder not configured on FILESERVER-01 | Added forwarder 8.8.8.8 in DNS server settings | `nslookup www.google.com` — resolved successfully |
| FLT-003 | 23/06/2026 | AP-OFFICE-01 could not be accessed via web GUI after IP change | Management VLAN SVI on SW-ACCESS-01 had incorrect gateway | Corrected SVI default gateway: `ip default-gateway 192.168.10.1` | `ping 192.168.10.3` from management PC — pass; web GUI accessible |

---

## 9.0 As-Built Network Diagram

The as-built diagram shows the network as it was actually installed, which may differ from the original specification due to changes during installation. The diagram must be included as a figure within the report body or as Appendix B.

**Minimum content of the as-built diagram:**

- All network devices (router, switches, APs, servers, end devices) with hostnames.
- All physical connections with cable type labelled.
- IP address of each device's relevant interface.
- VLAN membership of each switch port.
- Trunk links clearly marked.
- Internet cloud symbol connected to the router WAN interface.
- Physical location of each device (floor plan overlay if available).

**Diagram tools:** Microsoft Visio, draw.io (diagrams.net), or hand-drawn with straight lines and standard network symbols (ISO/IEC 11801 symbols or Cisco icons).

---

## 10.0 Recommendations

The recommendations section records any findings that do not rise to the level of a fault but should be addressed to improve the network's security, reliability, or performance.

**Format:**

| No. | Finding | Recommendation | Priority |
|-----|---------|----------------|----------|
| 1 | Default VLAN 1 still carrying management traffic on trunk ports | Reassign management traffic to a dedicated VLAN (currently VLAN 10); disable VLAN 1 on all trunks | High |
| 2 | Router and switch passwords set to default values at initial login | Change all default credentials immediately; implement a password policy | High |
| 3 | No UPS (Uninterruptible Power Supply) for switch and router | Install UPS to protect core network devices from power interruptions | Medium |
| 4 | DHCP lease duration set to default (1 day); not optimal for environment | Reduce lease to 8 hours for a hot-desk environment; increase to 7 days for stable workstations | Low |
| 5 | No network monitoring tool deployed | Install a free SNMP monitoring tool (e.g., PRTG free tier, Zabbix) to alert on device failures | Medium |

---

## 11.0 Conclusion

The conclusion is a formal statement summarising the outcome of the set-up project.

**Example:**

> The computer network connectivity set-up for [Site Name] was completed on [Date] in accordance with the approved network configuration specification. A total of [N] network devices were configured, [N] connectivity tests were conducted, and [N] faults were identified and resolved during the testing phase. All connectivity tests have been verified and passed as documented in this report.
>
> The network is ready for handover and operational use. The recommendations in Section 10 are advisory and do not affect current network functionality. The client or IT administrator should review and action them at the earliest opportunity.
>
> This report has been prepared by:
>
> **[Technician Full Name]**
> ICT Technician / Pelatih Tahap 3
> [Date]

---

## 12.0 Sign-Off Page

The sign-off page confirms that all parties have reviewed and accepted the report.

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Technician | | | |
| Supervisor / Instructor | | | |
| Client / Site Representative | | | |

**Acceptance statement:**
> I confirm that the computer network connectivity set-up has been completed and tested as described in this report, and I accept the network for operational use.

---

## 13.0 Report Writing Standards

| Standard | Guidance |
|----------|----------|
| Language | English throughout; Malay translations for key terms in headers (bilingual format). Use formal, third-person language. |
| Technical terms | Use correct technical terminology. Avoid slang (e.g., write "default gateway", not "the router's home address"). |
| Accuracy | Every IP address, hostname, and configuration parameter in the report must be verified against the actual device. Do not estimate or guess. |
| Clarity | Each section should be understandable by a non-specialist reader (e.g., a manager or auditor). Define acronyms on first use. |
| Completeness | Do not omit sections. A missing test record or unsigned sign-off page will cause the report to be returned. |
| Version control | If the report is revised after submission, increment the version number (v1.0 → v1.1) and record the change in a revision history table. |
| File format | Submit in PDF format for final version. Retain the source file (Word or equivalent) for revision purposes. |

---

## 14.0 Common Errors in Report Preparation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Copying IP addresses from the specification without verifying against the actual device | Report contains incorrect as-built data | Run `show running-config` or `ipconfig /all` on each device and copy values directly |
| Omitting failed tests from the results table | Assessor or client cannot trust the completeness of testing | Record all tests; document failed tests and their resolution; re-test after fixing |
| Handwritten corrections on a printed report | Appears unprofessional; may be illegible | Correct the source document and reprint; do not cross out and write over |
| Missing sign-off | Report is not officially accepted; handover is not complete | Obtain all signatures before submitting the final report |
| Diagram not matching the actual installation | Future technicians configure devices based on an incorrect diagram | Update the diagram immediately after any change; verify before printing |
| Using informal language | Report is not suitable for a government or corporate submission | Review language; replace informal phrases with formal equivalents |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCu 6
- Jabatan Pembangunan Kemahiran (JPK) — Buku Panduan WIM Edisi 2020 (Edisi Berkuat Kuasa Januari 2021)
- CompTIA Network+ Certification Study Guide — Chapter on Network Documentation
- Cisco Networking Academy — CCNA: Introduction to Networks (Module 17: Build a Small Network — Documentation)
- TIA/EIA-568-C Commercial Building Telecommunications Cabling Standard — labelling and documentation sections
- Malaysian Standard MS 1672:2003 — Information Technology — Guidelines for the Management and Operation of IT