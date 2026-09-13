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
| NO. KOD | IT-020-4:2013-C02/KP(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-manage-patches-security-updates

**TUJUAN:** Kertas rujukan untuk KP-04-manage-patches-security-updates.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the importance of patch management in maintaining computer system security
2. Classify patches by type and severity using industry-standard rating frameworks
3. Describe and implement a structured patch management lifecycle
4. Configure Windows Server Update Services (WSUS) to centralise and control patch deployment
5. Test patches in a staging environment before production deployment
6. Maintain a patch register and verify patch compliance across managed systems

---

## 1.0 Introduction to Patch Management

Patch management (pengurusan tampalan) is the process of identifying, acquiring, testing, and applying software updates — particularly security patches — to computer systems in a controlled and documented manner.

Unpatched systems are the single most exploited category of vulnerability in real-world attacks. High-profile breaches such as WannaCry (2017) and NotPetya (2017) spread rapidly because organisations had not applied available patches. A Level 4 systems administrator is responsible for ensuring all managed systems are kept current and that the patch management process is auditable.

---

## 2.0 Patch Classification

### 2.1 Patch Types

| Patch Type | Malay | Description |
|-----------|-------|-------------|
| Security Update | Kemas Kini Keselamatan | Addresses a specific vulnerability that could be exploited by an attacker |
| Critical Update | Kemas Kini Kritikal | Fixes a severe non-security bug with significant operational impact |
| Service Pack | Pek Perkhidmatan | A cumulative collection of updates, fixes, and sometimes new features |
| Feature Update | Kemas Kini Ciri | Adds new functionality; may carry compatibility risk |
| Driver Update | Kemas Kini Pemacu | Updates hardware driver software; may affect hardware compatibility |
| Firmware Update | Kemas Kini Perisian Tegar | Updates firmware in hardware devices (BIOS, network cards, storage controllers) |

### 2.2 Severity Ratings

Microsoft uses the following severity classification for security updates:

| Severity | Definition | Example | Response Time |
|----------|-----------|---------|---------------|
| Critical | Exploitation could allow remote code execution without user interaction | MS17-010 (EternalBlue / WannaCry) | Apply within 24–72 hours |
| Important | Exploitation could compromise data confidentiality, integrity, or availability | Elevation of privilege vulnerability | Apply within 7–14 days |
| Moderate | Impact mitigated by factors such as authentication requirement or non-default configuration | Information disclosure requiring local access | Apply within 30 days |
| Low | Very difficult to exploit; minimal impact | Browser-based minor disclosure | Apply within next scheduled maintenance window |

CVSS (Common Vulnerability Scoring System) scores provide a numeric rating (0.0–10.0) used across all vendors:

| CVSS Score | Severity Category |
|-----------|-----------------|
| 9.0–10.0 | Critical |
| 7.0–8.9 | High |
| 4.0–6.9 | Medium |
| 0.1–3.9 | Low |

---

## 3.0 Patch Management Lifecycle

A structured patch management lifecycle ensures that patches are applied consistently, safely, and with full documentation.

| Phase | Activity | Responsible Party |
|-------|----------|------------------|
| 1. Identification | Monitor vendor security advisories (Microsoft, CISA, CVE databases) for new vulnerabilities and patches | Security/IT Admin |
| 2. Categorisation | Classify each patch by type and severity; assign priority | Security/IT Admin |
| 3. Acquisition | Download patches from official vendor sources; verify digital signatures and checksums | IT Admin |
| 4. Testing | Deploy patch to isolated staging/test environment; verify system stability and application compatibility | IT Admin |
| 5. Approval | Obtain change management approval (CAB — Change Advisory Board) before production deployment | IT Manager / CAB |
| 6. Deployment | Deploy to production systems in controlled maintenance windows; use phased rollout for large environments | IT Admin |
| 7. Verification | Confirm patch is installed on all target systems; re-scan for vulnerability | IT Admin |
| 8. Documentation | Update patch register and change log; record any issues or rollbacks | IT Admin |

---

## 4.0 Windows Server Update Services (WSUS)

WSUS is a Microsoft server role that allows administrators to centralise the management and distribution of updates released through Microsoft Update to computers in a network.

### 4.1 WSUS Architecture

```
Microsoft Update (Internet)
        ↓
  WSUS Server (internal)
        ↓
  ┌─────┴──────┐
Servers    Workstations
```

WSUS downloads updates once from Microsoft and distributes them internally, saving bandwidth and giving the administrator control over which updates are approved and when.

### 4.2 Installing and Configuring WSUS (Windows Server)

| Step | Action |
|------|--------|
| 1 | Add the WSUS server role via Server Manager → Add Roles and Features |
| 2 | Complete the WSUS configuration wizard: specify update storage location and synchronisation schedule |
| 3 | Configure synchronisation with Microsoft Update: select products (e.g. Windows Server, Office) and update classifications |
| 4 | Create computer groups in WSUS: e.g. Test Computers, Servers, Workstations |
| 5 | Configure Group Policy to point client computers to the WSUS server: `HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate` |
| 6 | Approve updates for the Test group first; after validation, approve for production groups |

### 4.3 WSUS Group Policy Settings

| GPO Setting | Path | Value |
|-------------|------|-------|
| Specify intranet Microsoft update service location | Computer Configuration → Administrative Templates → Windows Components → Windows Update | `http://wsus-server:8530` |
| Configure Automatic Updates | Same path | 4 — Auto download and schedule install |
| Scheduled install day and time | Same path | 0 (every day), 03:00 (3:00 AM) |
| Do not connect to Windows Update internet locations | Same path | Enabled |

---

## 5.0 Patch Testing in a Staging Environment

Before deploying any patch to production, it must be tested in a staging environment that mirrors the production configuration.

### 5.1 Staging Environment Requirements

| Requirement | Detail |
|-------------|--------|
| Representative hardware/VM | Same OS version, service packs, and installed applications as production |
| Isolated network | Staging must not affect production systems |
| Test scenarios | Functional testing of critical business applications after patch; check for crashes, performance degradation, service failures |
| Rollback capability | Snapshot (VM) or system restore point taken before patch is applied |

### 5.2 Patch Testing Checklist

| Check | Pass / Fail |
|-------|------------|
| System boots normally after patch | [ ] |
| All critical services start without errors | [ ] |
| Core business applications function correctly | [ ] |
| No new events in Event Viewer (Critical / Error level) | [ ] |
| Network connectivity maintained | [ ] |
| Performance within acceptable baseline | [ ] |

---

## 6.0 Patch Compliance Verification

After deployment, the administrator must verify that the patch has been successfully applied to all target systems.

### 6.1 Verification Methods

| Method | Tool | Description |
|--------|------|-------------|
| WSUS Reports | WSUS console | Built-in reports show patch status per computer group |
| PowerShell query | `Get-HotFix -Id KB<number>` | Lists installed KB on a local or remote system |
| Microsoft Baseline Security Analyser (MBSA) | MBSA / Microsoft Security Compliance Toolkit | Scans systems for missing patches and misconfigurations |
| Third-party tools | Nessus, OpenVAS, Qualys | Vulnerability scanners report on unpatched systems across the network |

### 6.2 Patch Register

A patch register (daftar tampalan) is a maintained record of all patches applied to each system:

| Patch Register Field | Example |
|---------------------|---------|
| KB / Patch ID | KB5034441 |
| CVE reference | CVE-2024-21325 |
| Severity | Critical |
| Systems affected | All Windows Server 2022 |
| Date tested | 2026-01-15 |
| Date approved | 2026-01-16 |
| Date deployed | 2026-01-17 |
| Verified by | IT Admin name |
| Status | Installed — Compliant |

---

## 7.0 Common Errors in Patch Management

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Applying critical patches directly to production without testing | Patch causes application failure in production; business disruption | Always test in staging first, regardless of severity urgency |
| No documented approval process | Unauthorised patches applied; no audit trail | Implement a Change Advisory Board (CAB) sign-off for all production patches |
| Patching only the OS and ignoring applications | Application vulnerabilities (e.g. Adobe, Java, browsers) exploited | Include all installed software in the patch scope |
| Not verifying patch installation | Patch deployment fails silently; system remains vulnerable | Run compliance reports after every patch cycle |
| Delaying critical patches indefinitely | Systems exposed to known exploits during delay | Define and enforce maximum response times per severity level |
| No rollback plan | Failed patch cannot be reversed; extended downtime | Take VM snapshots or system restore points before every patch deployment |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer System Security Control — CoCu 2
- Microsoft Documentation: Windows Server Update Services (WSUS)
- NIST SP 800-40 Rev 4: Guide to Enterprise Patch Management Planning
- CIS Controls v8: Control 7 — Continuous Vulnerability Management
- CVE / NVD: https://nvd.nist.gov
- Microsoft Security Response Center: https://msrc.microsoft.com