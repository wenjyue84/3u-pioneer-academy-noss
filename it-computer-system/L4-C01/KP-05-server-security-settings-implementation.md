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
| NO. KOD | IT-020-4:2013-C01/KP(5/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Ensure all profiles block inbound by default

**TUJUAN:** Set-NetFirewallProfile -Profile Domain,Private,Public -DefaultInboundAction Block -DefaultOutboundAction Allow ```

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Apply the principle of least privilege to user accounts, service accounts, and administrative access
2. Configure Windows Firewall with Advanced Security to restrict traffic to required ports only
3. Implement server hardening using Group Policy Objects (GPO) and security baselines
4. Configure audit policy to record security-relevant events
5. Implement data-at-rest encryption using BitLocker Drive Encryption
6. Apply patch management procedures to maintain server security posture

---

## 1.0 Security Principles at Level 4

Server security at Level 4 moves beyond basic access control to a structured, policy-driven approach aligned with recognised security frameworks. The administrator must implement security controls that:

- Reduce the attack surface (Permukaan Serangan) — disable or remove everything not required
- Apply the **principle of least privilege** (Prinsip Hak Minimum) — every account, service, and process has only the permissions it requires to function
- Enable **auditability** — all security-relevant events are logged and retained
- Ensure **confidentiality** of data at rest and in transit
- Align with applicable frameworks: **CIS Controls**, **NIST SP 800-53**, **ISO/IEC 27001**, **PDPA 2010**

---

## 2.0 Account Security and Least Privilege

### 2.1 Built-in Account Management

| Account | Action | Reason |
|---------|--------|--------|
| **Administrator** (local) | Rename and disable (or set a strong password and restrict logon) | Default target of brute-force attacks |
| **Guest** | Disable | Should already be disabled; verify |
| **Domain Administrator** | Restrict to Domain Controllers only; do not use for daily tasks | Compromise of this account = full domain compromise |

### 2.2 Tiered Administration Model

Microsoft recommends a three-tier model to limit lateral movement in case of account compromise:

| Tier | Scope | Account Type |
|------|-------|-------------|
| **Tier 0** | Domain Controllers and identity infrastructure | Tier 0 Admin accounts (used ONLY on DCs) |
| **Tier 1** | Servers and applications | Tier 1 Admin accounts (used ONLY on servers, not workstations) |
| **Tier 2** | Workstations and end-user devices | Tier 2 Admin accounts (helpdesk, workstation management) |

Enforce tier separation using Privileged Access Workstations (PAWs) and Group Policy logon restrictions.

### 2.3 Service Account Management

Service accounts (Akaun Perkhidmatan) run Windows services and scheduled tasks:

- **Avoid using Domain Admin** for service accounts — a compromised service account should not have domain-wide impact
- Use **Group Managed Service Accounts (gMSA):** automatically managed passwords, no manual password rotation required
  ```powershell
  New-ADServiceAccount -Name "svc-sql" -DNSHostName "SRV-SQL01.pioneer.edu.my" `
    -PrincipalsAllowedToRetrieveManagedPassword "SRV-SQL01$"
  ```
- Document all service accounts in an asset register

### 2.4 Password Policy (via GPO)

Configure the Default Domain Policy with these minimum settings:

| Setting | Recommended Value |
|---------|------------------|
| Minimum password length | 14 characters |
| Password complexity | Enabled |
| Maximum password age | 90 days |
| Minimum password age | 1 day |
| Password history | 24 remembered |
| Account lockout threshold | 5 invalid attempts |
| Account lockout duration | 30 minutes |
| Lockout observation window | 30 minutes |

---

## 3.0 Windows Firewall Configuration

### 3.1 Firewall Profiles

Windows Firewall with Advanced Security (WFAS) applies rules based on the network profile:

| Profile | When Applied | Recommended Setting |
|---------|-------------|-------------------|
| **Domain** | Computer is connected to a domain network | Custom inbound rules per role |
| **Private** | Non-domain trusted network | Restrictive |
| **Public** | Untrusted/public network | Most restrictive (block all inbound by default) |

### 3.2 Principle: Default Deny Inbound

```powershell
# Ensure all profiles block inbound by default
Set-NetFirewallProfile -Profile Domain,Private,Public -DefaultInboundAction Block -DefaultOutboundAction Allow
```

### 3.3 Role-Based Inbound Rules

Each server role requires specific inbound ports. Open only what is required:

| Server Role | Protocol | Port(s) | Direction |
|-------------|----------|---------|----------|
| Domain Controller (AD DS) | TCP/UDP | 389 (LDAP), 636 (LDAPS), 88 (Kerberos), 53 (DNS), 135, 445, 49152–65535 (RPC dynamic) | Inbound |
| File Server (SMB) | TCP | 445 | Inbound |
| Web Server (HTTP/HTTPS) | TCP | 80, 443 | Inbound |
| Remote Desktop (RDP) | TCP | 3389 | Inbound — restrict source IP |
| WinRM (PowerShell Remoting) | TCP | 5985 (HTTP), 5986 (HTTPS) | Inbound — restrict source IP |
| DHCP Server | UDP | 67, 68 | Inbound |
| DNS Server | TCP/UDP | 53 | Inbound |

```powershell
# Example: Allow RDP only from management VLAN (10.0.10.0/24)
New-NetFirewallRule -DisplayName "Allow RDP from Mgmt VLAN" -Direction Inbound `
  -Protocol TCP -LocalPort 3389 -RemoteAddress 10.0.10.0/24 -Action Allow
```

---

## 4.0 Server Hardening with Security Baselines

### 4.1 What is a Security Baseline?

A security baseline (Garis Asas Keselamatan) is a set of configuration settings that represent the minimum acceptable security posture for a server. Applying a baseline configures hundreds of registry settings, audit policies, and user rights in a consistent, documented way.

### 4.2 Microsoft Security Compliance Toolkit

Microsoft provides free security baselines for Windows Server:
- Download: https://www.microsoft.com/en-us/download/details.aspx?id=55319
- Import baselines as GPO backups and link to the appropriate OU

### 4.3 Key Hardening Settings (Group Policy)

| Policy Path | Setting | Recommended Value |
|-------------|---------|------------------|
| Computer Config > Windows Settings > Security Settings > Local Policies > Security Options | Interactive logon: Do not display last user name | Enabled |
| | Network security: LAN Manager authentication level | Send NTLMv2 response only; refuse LM and NTLM |
| | Accounts: Rename administrator account | Custom name |
| Computer Config > Administrative Templates > Windows Components > Remote Desktop Services | Set client connection encryption level | High Level (128-bit) |
| Computer Config > Windows Settings > Security Settings > Account Policies > Kerberos Policy | Maximum lifetime for user ticket | 10 hours |
| | Maximum tolerance for computer clock synchronisation | 5 minutes |

### 4.4 CIS Benchmark Hardening

The Center for Internet Security (CIS) publishes detailed hardening benchmarks for Windows Server and Linux:

- **CIS Level 1:** Recommended settings with minimal impact on functionality — apply to all production servers
- **CIS Level 2:** More restrictive settings — apply to high-security environments (financial data, personal data under PDPA)

Tools for automated assessment: **CIS-CAT Pro**, **Microsoft Security Compliance Analyzer**

---

## 5.0 Audit Policy Configuration

### 5.1 Purpose of Audit Logging

Audit logs (Log Audit) record who did what, when, and from where. They are essential for:
- Security incident investigation
- Regulatory compliance (PDPA 2010, ISO 27001)
- Detecting insider threats and anomalous access

### 5.2 Advanced Audit Policy Configuration

Configure via GPO: Computer Configuration > Windows Settings > Security Settings > Advanced Audit Policy Configuration

| Category | Subcategory | Setting |
|---------|------------|---------|
| Account Logon | Credential Validation | Success, Failure |
| Account Management | User Account Management | Success, Failure |
| | Security Group Management | Success, Failure |
| Logon/Logoff | Logon | Success, Failure |
| | Logoff | Success |
| | Account Lockout | Failure |
| Object Access | File System | Failure (enable Success only for sensitive folders) |
| | Registry | Failure |
| Policy Change | Audit Policy Change | Success, Failure |
| Privilege Use | Sensitive Privilege Use | Success, Failure |
| System | Security System Extension | Success, Failure |
| | System Integrity | Success, Failure |

### 5.3 Event Log Configuration

```powershell
# Set Security event log to 512 MB, overwrite as needed
Limit-EventLog -LogName Security -MaximumSize 524288KB -OverflowAction OverwriteOlder
```

**Best practice:** Forward security logs to a centralised SIEM (Security Information and Event Management) system — Splunk, Microsoft Sentinel, or Elastic SIEM — to enable correlation and alerting.

---

## 6.0 BitLocker Drive Encryption

BitLocker (Penyulitan Pemacu BitLocker) encrypts server volumes to protect data at rest. If a disk is removed from the server, data is unreadable without the encryption key.

### 6.1 Prerequisites

- TPM 2.0 chip enabled in BIOS (verify with `tpm.msc`)
- UEFI boot mode with Secure Boot enabled
- Server must be domain-joined for key escrow to AD

### 6.2 Enabling BitLocker on Data Volume

```powershell
# Enable BitLocker on data drive D: with recovery key stored in AD
Enable-BitLocker -MountPoint "D:" -EncryptionMethod XtsAes256 `
  -RecoveryKeyProtector -RecoveryKeyPath "\\SRV-DC01\BitLockerKeys"

# Backup recovery key to Active Directory
Backup-BitLockerKeyProtector -MountPoint "D:" `
  -KeyProtectorId (Get-BitLockerVolume -MountPoint "D:").KeyProtector[0].KeyProtectorId
```

### 6.3 Network Unlock (for servers)

Servers typically need to reboot unattended (no one to enter PIN). Use **BitLocker Network Unlock** to allow automatic unlock when connected to the corporate network:
- Requires WDS (Windows Deployment Services) server for key delivery
- Server unlocks at boot if connected to the trusted network; otherwise prompts for recovery key

---

## 7.0 Patch Management

### 7.1 Patch Management Process

| Phase | Activity |
|-------|---------|
| **Identify** | Subscribe to Microsoft Security Response Center (MSRC) advisories; monitor CVE databases |
| **Evaluate** | Assess severity (Critical/Important/Moderate/Low) and applicability to the server's OS and roles |
| **Test** | Apply patches to test/staging environment first; verify role functionality |
| **Approve** | Obtain change management approval (change request) for production patching |
| **Deploy** | Apply patches during approved maintenance window; minimise user impact |
| **Verify** | Confirm successful installation; restart if required; verify role functionality |
| **Document** | Record patch application in the system change log |

### 7.2 Windows Server Update Services (WSUS)

WSUS provides centralised management of Windows Update for all servers and workstations:

```powershell
# Install WSUS role
Install-WindowsFeature -Name UpdateServices -IncludeManagementTools

# Configure client to use WSUS (via GPO)
# Computer Config > Admin Templates > Windows Components > Windows Update
# Set: Specify intranet Microsoft update service location = http://SRV-WSUS01:8530
```

### 7.3 Patch Cadence

| Patch Type | Target Deployment Timeline |
|-----------|--------------------------|
| Critical security patches | Within 72 hours of release |
| Important security patches | Within 14 days |
| Non-security updates | Monthly, with scheduled maintenance window |
| Firmware and driver updates | Quarterly or when required by vendor advisory |

---

## 8.0 Common Errors in Security Configuration

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Using Domain Admin for daily tasks** | Any phishing or malware compromise of the admin PC = full domain compromise | Use standard user account for daily work; use Tier 1/Tier 0 accounts only when needed |
| **RDP port 3389 exposed to internet** | Brute-force and ransomware attacks directly on RDP | Never expose RDP to internet; use VPN or RD Gateway; restrict source IP via firewall |
| **Audit policy not configured** | Security incidents cannot be investigated; compliance fails | Apply audit policy via GPO before go-live; verify with `auditpol /get /category:*` |
| **BitLocker recovery key not backed up** | Server cannot be recovered after motherboard replacement (TPM bound to old hardware) | Always backup recovery key to AD before enabling BitLocker |
| **Patches not tested before production** | Defective patch breaks critical service in production | Maintain a test/staging environment; validate patches before production deployment |
| **Default firewall rules left open** | Attack surface unnecessarily large | Apply default-deny inbound; open only role-required ports |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 1: Server Configuration
- Microsoft Security Compliance Toolkit: https://www.microsoft.com/en-us/download/details.aspx?id=55319
- CIS Benchmarks — Windows Server 2022: https://www.cisecurity.org/benchmark/microsoft_windows_server
- PDPA 2010 (Personal Data Protection Act 2010), Malaysia
- ISO/IEC 27001:2022 Annex A Controls — A.8 Technological Controls
- NIST SP 800-53 Rev 5 — Security and Privacy Controls for Information Systems
- Microsoft Tiered Administration Model: https://docs.microsoft.com/en-us/security/compass/privileged-access-access-model