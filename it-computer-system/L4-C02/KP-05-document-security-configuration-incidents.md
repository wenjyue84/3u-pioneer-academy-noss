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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/KP(5/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Enable logon success and failure auditing

**TUJUAN:** AuditPol /set /subcategory:"Logon" /success:enable /failure:enable ```

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and components of a security configuration baseline document
2. Produce a security configuration record for a managed computer system
3. Describe the stages of an incident response lifecycle
4. Complete an incident report in accordance with organisational and regulatory requirements
5. Maintain a security log and audit trail that supports forensic investigation

---

## 1.0 Introduction to Security Documentation

Security documentation (dokumentasi keselamatan) is the systematic recording of all security-related configurations, events, and decisions made in a computing environment. It serves two equally important purposes:

1. **Operational:** Enables consistent configuration, rapid troubleshooting, and knowledge transfer between administrators
2. **Compliance and legal:** Provides an auditable evidence trail demonstrating that security controls are in place and that incidents have been properly handled

A Level 4 systems administrator must produce documentation that is accurate, complete, version-controlled, and accessible to authorised personnel only.

---

## 2.0 Security Configuration Documentation

### 2.1 Security Configuration Baseline

A security configuration baseline (garis dasar konfigurasi keselamatan) is a documented set of minimum-security settings that all systems of a given type must meet. It is derived from the organisation's security policy and industry standards such as CIS Benchmarks.

| Component | Content |
|-----------|---------|
| System identification | Hostname, IP address, OS version, hardware model, asset tag |
| OS configuration | Installed updates (KB numbers), enabled/disabled features, local security policy settings |
| User and group configuration | Local accounts, group memberships, password policy applied |
| Network configuration | IP settings, firewall rules applied, open ports list |
| Services configuration | Running services list, disabled services list, startup type of each |
| Installed software | Application name, version, licence status, last update date |
| Audit and logging | Audit policy settings, log storage location, retention period |
| Last reviewed | Date of last configuration review and name of reviewing administrator |

### 2.2 Configuration Management Register

Every change to a system's configuration must be recorded in a configuration management register:

| Field | Description |
|-------|-------------|
| Change ID | Unique identifier (e.g. CHG-2026-0042) |
| System | Hostname or asset affected |
| Date and time | When the change was made |
| Change description | What was changed and why |
| Made by | Name of the administrator |
| Approved by | Name of the authorising person |
| Pre-change state | Configuration before the change |
| Post-change state | Configuration after the change |
| Test result | Outcome of post-change verification |
| Rollback procedure | Steps to reverse the change if needed |

### 2.3 Hardening Checklist

A system hardening checklist documents the specific steps taken to secure a newly deployed system. It is completed for every server and workstation and retained as part of the system's asset record.

| Hardening Action | Applied | Date | Verified By |
|-----------------|---------|------|------------|
| Default administrator account renamed or disabled | [ ] | | |
| Password policy applied via GPO | [ ] | | |
| Unnecessary services disabled | [ ] | | |
| Host-based firewall enabled and configured | [ ] | | |
| All available security patches applied | [ ] | | |
| Audit logging enabled (logon, object access, policy change) | [ ] | | |
| Antivirus/EDR agent installed and updated | [ ] | | |
| Remote desktop restricted to admin VLAN only | [ ] | | |
| Configuration baseline document completed and filed | [ ] | | |

---

## 3.0 Security Incident Response

### 3.1 Definition

A security incident (insiden keselamatan) is any event that actually or potentially compromises the confidentiality, integrity, or availability of information or systems. Examples include:

- Ransomware infection on a workstation
- Unauthorised login detected in audit logs
- Data exfiltration by a former employee
- Denial of service attack affecting a server
- Discovery of malware on a USB drive brought in by a user

### 3.2 Incident Response Lifecycle (NIST SP 800-61)

| Phase | Malay | Key Activities |
|-------|-------|---------------|
| 1. Preparation | Persediaan | Establish incident response policy and team; prepare tools; train staff; test response procedures |
| 2. Detection and Analysis | Pengesanan dan Analisis | Monitor alerts and logs; confirm whether an event is an incident; assess scope and severity |
| 3. Containment | Penahanan | Isolate affected systems to prevent spread; preserve evidence; apply short-term and long-term containment |
| 4. Eradication | Pembasmian | Remove malware, unauthorised accounts, or other cause of the incident; patch exploited vulnerability |
| 5. Recovery | Pemulihan | Restore systems from clean backups; verify systems are clean; return to normal operations |
| 6. Post-Incident Activity | Aktiviti Pasca Insiden | Conduct lessons-learned review; update policies and procedures; file final incident report |

### 3.3 Incident Severity Classification

| Severity | Definition | Response Time | Example |
|----------|-----------|---------------|---------|
| P1 — Critical | Major business disruption; data breach confirmed; ransomware active | Immediate (within 1 hour) | Ransomware spreading across network |
| P2 — High | Significant threat; potential for data loss; single critical system affected | Within 4 hours | Server compromised; no confirmed spread |
| P3 — Medium | Limited scope; no confirmed data loss; suspicious activity detected | Within 24 hours | Phishing email with malicious link clicked; no execution |
| P4 — Low | Minimal impact; informational; user policy violation | Within 72 hours | Unauthorised USB device connected; no data transfer |

---

## 4.0 Incident Report

An incident report (laporan insiden) is the formal document that records all details of a security incident from detection to closure. It is required for legal, regulatory, and operational purposes.

### 4.1 Incident Report Structure

| Section | Content Required |
|---------|-----------------|
| Incident ID | Unique reference number (e.g. INC-2026-0015) |
| Date and time reported | When the incident was first reported or detected |
| Reported by | Name and role of the person who detected or reported the incident |
| Incident type | Malware / Unauthorised Access / Data Breach / DDoS / Policy Violation / Other |
| Severity | P1 / P2 / P3 / P4 |
| Systems affected | Hostnames, IP addresses, departments affected |
| Description of incident | Factual account of what was observed; include evidence (log excerpts, screenshots) |
| Timeline | Chronological sequence of events from detection to closure |
| Root cause analysis | What caused the incident (e.g. unpatched vulnerability, phishing, misconfiguration) |
| Containment actions | Steps taken to isolate and limit the spread |
| Eradication actions | Steps taken to remove the cause |
| Recovery actions | Steps taken to restore normal operations |
| Data affected | Whether personal data or sensitive data was involved (relevant to PDPA reporting) |
| Lessons learned | What can be improved in policy, configuration, or training to prevent recurrence |
| Recommended actions | Specific follow-up tasks with owner and deadline |
| Closed by | Name, signature, and date of closing administrator |
| Verified by | Name and signature of IT Manager or Security Officer |

---

## 5.0 Audit Logging and Log Management

### 5.1 Windows Audit Policy Settings

Audit logging must be enabled to create an evidence trail for incident investigation and compliance.

| Audit Category | Setting | Events Captured |
|---------------|---------|----------------|
| Audit logon events | Success and Failure | All interactive and network logon attempts |
| Audit account logon events | Success and Failure | Domain authentication attempts |
| Audit object access | Success and Failure | Access to files, folders, registry keys |
| Audit policy change | Success | Changes to audit policy or user rights |
| Audit privilege use | Failure | Unauthorised use of privileges |
| Audit process creation | Success | New process start events (useful for malware detection) |
| Audit account management | Success and Failure | User/group creation, modification, deletion |

**Enable via PowerShell:**
```powershell
# Enable logon success and failure auditing
AuditPol /set /subcategory:"Logon" /success:enable /failure:enable
```

### 5.2 Log Retention and Protection

| Requirement | Recommendation |
|-------------|---------------|
| Minimum retention | 12 months (longer for regulated sectors) |
| Log storage | Centralised SIEM (Security Information and Event Management) system; not only on the local machine |
| Log integrity | Use write-once storage or cryptographic hashing to prevent tampering |
| Review frequency | Critical servers: daily automated alerting; weekly manual review |
| PDPA compliance | Logs containing personal data must be protected with same controls as other personal data |

### 5.3 Windows Event Log — Key Event IDs

| Event ID | Category | Meaning |
|----------|----------|---------|
| 4624 | Logon | Successful logon |
| 4625 | Logon | Failed logon attempt |
| 4648 | Logon | Logon using explicit credentials (pass-the-hash indicator) |
| 4720 | Account Management | User account created |
| 4726 | Account Management | User account deleted |
| 4740 | Account Management | Account locked out |
| 4771 | Kerberos | Kerberos pre-authentication failure |
| 7045 | System | New service installed (malware persistence indicator) |

---

## 6.0 Common Errors in Security Documentation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Incomplete incident reports | Regulatory non-compliance; inability to reconstruct the incident | Use a mandatory template; supervisor sign-off before closure |
| Logs stored only on the affected system | Attacker deletes logs; evidence destroyed | Forward all logs to a central SIEM immediately |
| No version control on configuration documents | Old and new configurations confused; rollback impossible | Use version numbering and date stamps on all configuration documents |
| Incident classified lower than actual severity | Insufficient response; incident escalates | When in doubt, classify higher; downgrade later if evidence warrants |
| Lessons learned not acted upon | Same incident recurs | Assign every recommendation from lessons-learned a named owner and deadline |
| Personal data in incident reports not protected | PDPA violation | Store incident reports in access-controlled location; redact personal data where not essential |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer System Security Control — CoCu 2
- NIST SP 800-61 Rev 2: Computer Security Incident Handling Guide
- Personal Data Protection Act 2010 (Malaysia) — Section 9: Security
- MS ISO/IEC 27001:2022 — Annex A: Information Security Controls
- CIS Controls v8: Control 8 — Audit Log Management
- Microsoft Documentation: Windows Security Auditing