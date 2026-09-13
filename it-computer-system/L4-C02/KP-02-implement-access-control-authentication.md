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
| NO. KOD | IT-020-4:2013-C02/KP(2/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-implement-access-control-authentication

**TUJUAN:** Kertas rujukan untuk KP-02-implement-access-control-authentication.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the principles of access control and their application in computer system administration
2. Differentiate between authentication, authorisation, and accounting (AAA)
3. Configure user accounts, groups, and permissions according to the principle of least privilege
4. Implement multi-factor authentication (MFA) and account lockout policies
5. Apply Role-Based Access Control (RBAC) in a Windows Server or Linux environment

---

## 1.0 Introduction to Access Control

Access control (kawalan akses) is the set of mechanisms that regulate who or what can view, use, or modify resources in a computing environment. It is the primary technical defence against unauthorised access, which is one of the most common vectors for security incidents.

At Level 4, the systems administrator must not only create accounts but design an access control architecture — deciding which users belong to which groups, what permissions those groups carry, and how access is authenticated and logged.

---

## 2.0 The AAA Framework

| Component | Malay | Function | Example |
|-----------|-------|----------|---------|
| Authentication (Pengesahan) | Pengesahan Identiti | Verifying the identity of a user or system | Username + password; smart card; fingerprint |
| Authorisation (Kebenaran) | Kebenaran | Determining what an authenticated entity is allowed to do | User X can read File Y but not modify it |
| Accounting (Perakaunan) | Perakaunan / Pengauditan | Recording what an authenticated and authorised entity has done | Audit log showing User X read File Y at 09:15 |

All three components must be implemented together. Authentication alone is insufficient if authorisation grants excessive permissions or if accounting does not record access events.

---

## 3.0 Authentication Methods

### 3.1 Authentication Factors

| Factor Type | Description | Examples |
|-------------|-------------|---------|
| Something you know (Sesuatu yang anda tahu) | A secret known only to the user | Password, PIN, security question answer |
| Something you have (Sesuatu yang anda miliki) | A physical or digital token | Smart card, hardware token (YubiKey), OTP via authenticator app |
| Something you are (Sesuatu yang anda ada) | A biometric characteristic | Fingerprint, facial recognition, iris scan |

Single-factor authentication (SFA) uses one factor; multi-factor authentication (MFA) combines two or more.

### 3.2 Password Policy Requirements (Windows Group Policy)

| Parameter | Recommended Setting | GPO Path |
|-----------|--------------------|---------
| Minimum password length | 12 characters | Computer Configuration → Windows Settings → Security Settings → Account Policies → Password Policy |
| Password complexity | Enabled (uppercase, lowercase, digit, symbol) | Same path |
| Maximum password age | 90 days | Same path |
| Minimum password age | 1 day (prevents immediate re-use cycling) | Same path |
| Enforce password history | 10 passwords | Same path |

### 3.3 Account Lockout Policy

| Parameter | Recommended Setting |
|-----------|---------------------|
| Account lockout threshold | 5 invalid attempts |
| Account lockout duration | 30 minutes (or until administrator unlocks) |
| Reset account lockout counter after | 15 minutes |

### 3.4 Multi-Factor Authentication (MFA)

MFA adds a second (or third) verification step after the password, significantly reducing the risk of account compromise even if the password is stolen.

**Implementation options:**
- **Microsoft Authenticator / TOTP apps** — Generate a time-based one-time password (TOTP) that changes every 30 seconds
- **Hardware tokens** — Physical devices (e.g. YubiKey) that generate or store cryptographic credentials
- **SMS OTP** — One-time code sent to a registered mobile number (lower security; subject to SIM-swap attacks)
- **Windows Hello for Business** — PIN + biometric tied to the device's TPM; eliminates password entirely for domain-joined systems

---

## 4.0 Access Control Models

### 4.1 Discretionary Access Control (DAC)

The resource owner controls who has access. Standard on NTFS and Linux file systems. Flexible but dependent on individual users making correct decisions.

### 4.2 Mandatory Access Control (MAC)

Access is determined by security labels assigned to subjects (users) and objects (files). The system enforces policy; users cannot override it. Used in high-security environments (e.g. SELinux).

### 4.3 Role-Based Access Control (RBAC)

Permissions are assigned to roles, and users are assigned to roles. This is the most common model in enterprise environments.

| Role | Example Permissions |
|------|---------------------|
| IT Administrator | Full system administration; can create/delete accounts |
| Finance User | Read/write access to finance shared folder; no access to HR data |
| HR Manager | Read/write access to HR data; read-only access to payroll reports |
| Guest | Read-only access to public shared resources only |

### 4.4 Principle of Least Privilege (PoLP)

Every user, process, and service should have the minimum permissions required to perform its function — no more. This limits the blast radius of a compromised account.

**Implementation steps:**
1. Document the tasks each user role must perform
2. Map tasks to the minimum required permissions
3. Create groups reflecting each role
4. Assign permissions to groups, not individual users
5. Review and revoke excessive permissions quarterly

---

## 5.0 User and Group Management in Windows Server

### 5.1 Account Types

| Account Type | Scope | Use Case |
|-------------|-------|----------|
| Local User Account | Single computer only | Standalone workstations; emergency access |
| Domain User Account | All computers in the Active Directory domain | Standard enterprise accounts |
| Service Account | Runs background services; no interactive login | SQL Server service, backup agent |
| Built-in Administrator | Local administrator on each machine | Emergency recovery; normally disabled |
| Domain Administrator | Full control of the entire domain | Reserved for senior IT staff; use sparingly |

### 5.2 Active Directory Organisational Unit (OU) Structure

A well-designed OU structure enables Group Policy to be applied precisely:

```
domain.local
├── Computers
│   ├── Servers
│   ├── Workstations
│   └── Laptops
└── Users
    ├── IT Department
    ├── Finance Department
    ├── HR Department
    └── Service Accounts
```

### 5.3 Group Policy Object (GPO) for Access Control

| GPO Setting | Purpose |
|-------------|---------|
| Deny log on locally | Prevents service accounts from interactive desktop login |
| Restrict access to Control Panel | Prevents standard users from changing system settings |
| Audit logon events | Records all successful and failed logon attempts |
| Software Restriction Policies / AppLocker | Prevents execution of unauthorised applications |

---

## 6.0 Linux User and Permission Management

### 6.1 Key Commands

| Command | Function | Example |
|---------|----------|---------|
| `useradd` | Create a new user account | `useradd -m -s /bin/bash jsmith` |
| `passwd` | Set or change a user's password | `passwd jsmith` |
| `usermod -aG` | Add user to a group | `usermod -aG sudo jsmith` |
| `chmod` | Change file/directory permissions | `chmod 750 /data/finance` |
| `chown` | Change file/directory owner | `chown root:finance /data/finance` |
| `getfacl` / `setfacl` | View/set extended Access Control Lists | `setfacl -m u:jsmith:r /data/hr` |

### 6.2 Linux Permission Notation

| Permission | Octal | Meaning |
|-----------|-------|---------|
| `rwx` | 7 | Read, write, execute |
| `rw-` | 6 | Read and write only |
| `r-x` | 5 | Read and execute only |
| `r--` | 4 | Read only |
| `---` | 0 | No permissions |

---

## 7.0 Privileged Access Management (PAM)

Privileged accounts (administrator, root) represent the highest risk in any environment. Level 4 administrators must apply additional controls:

| Control | Description |
|---------|-------------|
| Separate privileged accounts | Administrators use a standard account for daily tasks and a separate admin account only when elevated access is needed |
| Just-In-Time (JIT) access | Elevated permissions granted only for the duration of a specific task, then automatically revoked |
| Privileged Access Workstations (PAW) | Dedicated, hardened workstations used only for administrative tasks; no internet browsing or email |
| Audit all privileged actions | Every action taken with an elevated account must be logged and reviewed |

---

## 8.0 Common Errors in Access Control Implementation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Granting excessive permissions ("just in case") | Breaches have larger blast radius; principle of least privilege violated | Audit permissions quarterly; remove what is not actively needed |
| Using shared accounts | Actions cannot be attributed to an individual; accountability lost | One account per person; no shared passwords |
| Not disabling accounts when staff leave | Former employees retain access; insider threat risk persists | Include account deactivation in HR offboarding checklist |
| Weak or default passwords | Accounts easily compromised by dictionary or brute-force attacks | Enforce password policy via GPO; require password change at first login |
| No MFA on administrator accounts | Single stolen credential gives full system control | Enforce MFA on all privileged accounts without exception |
| Permissions set on individual users instead of groups | Unmanageable permission sprawl as organisation grows | Always assign permissions to groups; assign users to groups |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer System Security Control — CoCu 2
- Microsoft Documentation: Active Directory Users and Computers, Group Policy Management
- NIST SP 800-63B: Digital Identity Guidelines — Authentication and Lifecycle Management
- CIS Benchmark: Windows Server 2022 — Access Control Section
- Linux man pages: useradd, chmod, setfacl
- CompTIA Security+ Study Guide — Domain: Identity and Access Management