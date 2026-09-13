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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KP(6/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-06-server-configuration-documentation

**TUJUAN:** Kertas rujukan untuk KP-06-server-configuration-documentation.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose, audience, and lifecycle of server configuration documentation
2. Produce a complete Server Configuration Record (Rekod Konfigurasi Pelayan) for a configured server
3. Construct an As-Built Document (Dokumen Sebina) that captures the final server state
4. Apply version control principles to infrastructure documentation
5. Conduct a formal handover from project/configuration phase to operations
6. Maintain ongoing documentation through a change log

---

## 1.0 Why Documentation is a Professional Obligation

Configuration documentation (Dokumentasi Konfigurasi) is not optional or a post-deployment afterthought — it is a professional and operational obligation at Level 4. Undocumented infrastructure creates:

- **Operational risk:** When the configuring administrator leaves, no one knows the configuration — recovery from failure becomes guesswork
- **Security risk:** Unknown configuration = unknown attack surface; auditors cannot verify compliance
- **Compliance failure:** PDPA 2010, ISO/IEC 27001, and JPK assessment criteria all require demonstrated ability to produce accurate records
- **Support degradation:** Helpdesk and on-call engineers cannot troubleshoot effectively without accurate documentation

A server that is fully configured but undocumented is considered **incomplete work** from a professional and JPK assessment standpoint.

---

## 2.0 Types of Server Documentation

| Document Type | Purpose | Primary Audience |
|--------------|---------|-----------------|
| **Server Configuration Record** | Baseline of all hardware and software settings at a point in time | IT operations, auditors |
| **As-Built Document** | Final verified state after configuration; becomes the operational reference | Operations team, NOC |
| **Change Log** | Append-only record of all changes made after initial deployment | IT team, change manager |
| **Network Diagram** | Visual representation of server connectivity, VLANs, and IP addressing | Network engineers, new staff |
| **Runbook / Standard Operating Procedure (SOP)** | Step-by-step procedures for routine operations (backup restore, patching, failover) | Operations team, on-call |
| **Disaster Recovery Plan (DRP)** | Procedures for recovering the server after major failure | IT management, operations |

---

## 3.0 Server Configuration Record — Structure and Content

The Server Configuration Record (Rekod Konfigurasi Pelayan) must capture the full state of the server at the time of documentation:

### Section 1: Server Identity

| Field | Example |
|-------|---------|
| Server name (hostname) | SRV-DC01 |
| FQDN | SRV-DC01.pioneer.edu.my |
| Role(s) | Domain Controller, DNS Server, DHCP Server |
| Physical location | Server Room A, Rack 2, U3–U4 |
| Asset tag | IT-2026-0042 |
| Serial number | DELL-SVC-XY123456 |
| Purchase date | 2026-03-01 |
| Warranty expiry | 2029-03-01 |
| Owner / Responsible admin | IT Administrator — Ahmad bin Razak |

### Section 2: Hardware Configuration

| Component | Specification |
|-----------|--------------|
| Make and model | Dell PowerEdge R750 |
| CPU | 2 × Intel Xeon Gold 6326 (16 cores each, 2.9 GHz, LGA4189) |
| RAM | 256 GB DDR4 ECC RDIMM (16 × 16 GB) |
| Storage controller | Dell PERC H755 (RAID controller, 8 GB FBWC) |
| Physical disks | 4 × 1.2 TB SAS SSD (10K RPM) + 2 × 480 GB SATA SSD (hot spare) |
| RAID configuration | RAID 10 (4 × 1.2 TB SAS, logical drive: "DATA-RAID10", 2.4 TB usable); RAID 1 (OS logical drive: "OS-RAID1", 480 GB usable) |
| NIC | 2 × Dell Broadcom 25GbE Dual-Port SFP28; bonded (802.3ad LACP) |
| PSU | 2 × 1100W Titanium redundant PSU |
| Management | iDRAC9 Enterprise, IP: 10.0.10.5 |

### Section 3: Network Configuration

| Interface | IP Address | Subnet | Gateway | VLAN | Purpose |
|-----------|-----------|--------|---------|------|---------|
| Bond0 (eth0+eth1) | 10.0.1.10 | /24 | 10.0.1.1 | VLAN 10 | Production |
| iDRAC | 10.0.10.5 | /24 | 10.0.10.1 | VLAN 20 | Management |

### Section 4: Operating System Configuration

| Field | Value |
|-------|-------|
| OS | Windows Server 2022 Standard (Desktop Experience) |
| Build | 20348.1547 |
| Activation | KMS (Volume License) |
| Time zone | Malay Peninsula Standard Time (UTC+8) |
| NTP server | time.windows.com |
| Windows Update | WSUS (http://SRV-WSUS01:8530) |
| Last patched | 2026-06-10 |

### Section 5: Roles and Features Installed

| Role / Feature | Status | Configuration Notes |
|---------------|--------|-------------------|
| Active Directory Domain Services | Installed | Domain: pioneer.edu.my; Forest: WinThreshold |
| DNS Server | Installed | Forward zone: pioneer.edu.my; Reverse zone: 1.0.10.in-addr.arpa |
| DHCP Server | Installed | Scope: 10.0.1.100–10.0.1.250; authorised in AD |
| File Server | Not installed | Hosted on separate server SRV-FILE01 |

### Section 6: Security Configuration

| Security Control | Configuration |
|-----------------|--------------|
| Windows Firewall | Enabled — Domain profile; default deny inbound |
| BitLocker | Enabled on D: (XTS-AES 256); recovery key in AD |
| Audit policy | Advanced audit policy applied via GPO: all logon/account events, Success+Failure |
| Password policy | 14 char min; complexity; 90-day max age; 24 history |
| Admin account | Renamed; local administrator disabled |
| Security baseline | Microsoft Security Baseline for Windows Server 2022 applied via GPO |

### Section 7: Backup Configuration

| Field | Value |
|-------|-------|
| Backup software | Veeam Backup & Replication 12 |
| Backup schedule | Daily at 02:00; weekly full on Sunday at 01:00 |
| Retention | Daily: 14 days; Weekly: 4 weeks; Monthly: 12 months |
| Backup target | SRV-BACKUP01 (D:\VeeamBackups\SRV-DC01) |
| Last successful backup | 2026-06-22 02:15 |
| Recovery tested | 2026-05-15 — full VM restore verified |

---

## 4.0 As-Built Document

The As-Built Document (Dokumen Sebina) is produced after all configuration is complete and verified. It differs from the configuration plan in that it reflects the **actual deployed state** rather than the intended design. Deviations from the plan must be documented with justification.

### As-Built Content Additions (beyond the Configuration Record)

| Section | Content |
|---------|---------|
| **Deviations from plan** | Any differences between the Server Role Plan and the actual deployed configuration, with justification (e.g. "NIC bonding using LACP instead of active-backup due to switch capability") |
| **Verification test results** | Results of all acceptance tests performed (pass/fail for each test case) |
| **Known issues / limitations** | Any outstanding issues not resolved at handover (e.g. WSUS not yet replicating, to be resolved within 7 days) |
| **Sign-off** | Signatures of configuring administrator, IT manager, and operations team accepting handover |

---

## 5.0 Version Control for Documentation

Infrastructure documentation changes over time. Without version control, teams may work from outdated documents.

### 5.1 Versioning Convention

| Version | Meaning |
|---------|---------|
| v1.0 | Initial As-Built — signed off at go-live |
| v1.1, v1.2... | Minor updates — configuration changes within same deployment |
| v2.0 | Major changes — OS upgrade, hardware refresh, role addition |

### 5.2 Document Header

Every configuration document must include:

```
Document Title:  Server Configuration Record — SRV-DC01
Document Owner:  IT Administrator
Version:         v1.2
Last Updated:    2026-06-22
Last Updated By: Ahmad bin Razak
Review Date:     2026-12-22
```

### 5.3 Storage Location

Store documentation in a location that:
- Is accessible to the entire IT team (not a personal folder)
- Is backed up
- Has version history (SharePoint, Confluence, Git repository)

**Recommended:** IT documentation SharePoint site or a Git repository for infrastructure-as-code environments.

---

## 6.0 Change Log Maintenance

After go-live, all changes to the server must be recorded in an append-only change log:

| Date | Change ID | Description | Changed By | Approved By | Rollback Plan |
|------|-----------|-------------|-----------|------------|--------------|
| 2026-06-22 | CR-042 | Initial deployment and go-live | Ahmad | IT Manager | Decommission VM; restore from backup |
| 2026-07-01 | CR-051 | Applied June 2026 security patches (KB5027231, KB5026780) | Ahmad | IT Manager | Remove patches via DISM; restore snapshot |
| 2026-07-15 | CR-058 | Increased DHCP scope end range from 250 to 240 to reserve static pool | Siti | IT Manager | Restore previous DHCP scope settings |

**Rule:** No undocumented changes. Every change, however minor, generates a change log entry.

---

## 7.0 Formal Handover Procedure

The handover (Serahterima) formally transfers responsibility for the server from the configuring team to the operations team:

### Handover Checklist

| Item | Status |
|------|--------|
| Server Configuration Record completed and reviewed | [ ] |
| As-Built Document signed off | [ ] |
| All acceptance tests passed | [ ] |
| Backup configured and first successful backup verified | [ ] |
| Monitoring agent installed and server visible in monitoring dashboard | [ ] |
| Alert notifications configured and tested | [ ] |
| Operations team briefed on server role, network, and access | [ ] |
| Runbook / SOP for routine operations provided | [ ] |
| Admin credentials handed over securely (password manager) | [ ] |
| iDRAC / out-of-band management access verified by operations | [ ] |
| All documentation stored in team-accessible location | [ ] |

### Handover Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Configuring Administrator | | | |
| IT Manager | | | |
| Operations Team Lead | | | |

---

## 8.0 Common Errors in Documentation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Documentation created weeks after deployment from memory** | Inaccurate details; unverified; does not reflect actual state | Document during configuration; record settings as they are applied |
| **No deviation section in As-Built** | Operations team uses plan document; actual configuration differs; troubleshooting errors | Explicitly document every deviation, however small |
| **Single copy of documentation in configuring admin's laptop** | Admin leaves; documentation lost | Store in shared, backed-up team repository from day one |
| **Version number not updated after changes** | Team uses outdated configuration record; makes incorrect assumptions | Update version number and header immediately after any change |
| **Backup not verified before handover** | Operations team discovers backup was failing silently after an incident | Perform and document a test restore before signing off handover |
| **No change log after go-live** | After six months, nobody knows what changed; incident investigation is impossible | Make change log a mandatory step in the change management process |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 1: Server Configuration
- ISO/IEC 27001:2022 — A.5.9 Inventory of information and other associated assets
- ITIL 4 — Configuration Management and Change Enablement practices
- Microsoft Docs — Document your Windows Server infrastructure: https://docs.microsoft.com/
- PDPA 2010 — Data governance and record-keeping obligations