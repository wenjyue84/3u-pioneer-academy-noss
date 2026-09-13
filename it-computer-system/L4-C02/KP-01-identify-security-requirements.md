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
| NO. KOD | IT-020-4:2013-C02/KP(1/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-identify-security-requirements

**TUJUAN:** Kertas rujukan untuk KP-01-identify-security-requirements.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the concept and importance of computer system security in an organisational context
2. Identify and classify security threats and vulnerabilities affecting computer systems
3. Interpret security policy documents and regulatory requirements relevant to IT administration at Level 4
4. Conduct a structured security requirements analysis for a given computing environment
5. Produce a security requirements specification document aligned with organisational risk posture

---

## 1.0 Introduction to Computer System Security

Computer system security (keselamatan sistem komputer) is the set of policies, procedures, and technical controls applied to protect hardware, software, data, and network resources from unauthorised access, damage, disruption, or misuse. At Level 4, the systems administrator is responsible not only for implementing security controls but also for analysing the security requirements of the organisation and translating them into actionable configurations.

Security requirements analysis is the foundation of all subsequent security work. Without a clear understanding of what assets must be protected, what threats are relevant, and what the organisation is willing to accept as residual risk, any implemented controls may be incomplete, misdirected, or disproportionate.

---

## 2.0 Security Concepts and Terminology

### 2.1 The CIA Triad

All computer system security goals can be mapped to three fundamental properties:

| Property | Malay Term | Definition | Example |
|----------|-----------|------------|---------|
| Confidentiality (Kerahsiaan) | Kerahsiaan | Information is accessible only to those authorised to access it | Encrypting payroll data so only HR staff can read it |
| Integrity (Integriti) | Integriti | Information is accurate, complete, and unmodified by unauthorised parties | Using file hashes to verify that a downloaded software installer has not been tampered with |
| Availability (Kesediaan) | Kesediaan | Information and systems are accessible to authorised users when needed | Configuring redundant servers and UPS to maintain uptime |

### 2.2 Key Security Terms

| Term | Malay Equivalent | Definition |
|------|-----------------|------------|
| Threat (Ancaman) | Ancaman | Any potential event or actor that could cause harm to an asset |
| Vulnerability (Kelemahan) | Kelemahan / Kerentanan | A weakness in a system that a threat could exploit |
| Risk (Risiko) | Risiko | The probability that a threat will exploit a vulnerability, multiplied by the impact |
| Asset (Aset) | Aset | Any resource of value that must be protected (hardware, data, software, reputation) |
| Control (Kawalan) | Kawalan | A safeguard or countermeasure applied to reduce risk |
| Residual Risk (Risiko Baki) | Risiko Baki | Risk that remains after controls are applied |
| Security Policy (Dasar Keselamatan) | Dasar Keselamatan | A formal document that states the organisation's security objectives and rules |

---

## 3.0 Threat Classification

Understanding threat types allows the administrator to scope security requirements accurately.

### 3.1 Threat Categories

| Category | Malay | Examples |
|----------|-------|----------|
| Malware | Perisian Hasad | Viruses, worms, ransomware, spyware, trojans |
| Unauthorised Access | Capaian Tidak Dibenarkan | Password attacks, privilege escalation, insider threat |
| Social Engineering | Kejuruteraan Sosial | Phishing, pretexting, vishing, tailgating |
| Denial of Service | Penafian Perkhidmatan | DDoS attacks, resource exhaustion, flooding |
| Physical Threats | Ancaman Fizikal | Theft, vandalism, natural disasters, power outages |
| Data Leakage | Kebocoran Data | Accidental disclosure, unencrypted backups, improper disposal |
| Supply Chain Attacks | Serangan Rantaian Bekalan | Compromised software updates, hardware implants |

### 3.2 Threat Sources

| Source | Description |
|--------|-------------|
| External attackers | Hackers, criminal organisations, nation-state actors targeting the organisation's systems from outside |
| Malicious insiders | Disgruntled or compromised employees who abuse legitimate access |
| Negligent users | Staff who inadvertently cause breaches through poor security hygiene |
| Third-party vendors | Contractors or suppliers with access to systems who introduce risk |

---

## 4.0 Vulnerability Assessment

A vulnerability assessment (penilaian kelemahan) is a systematic process of identifying weaknesses in a computing environment before they can be exploited.

### 4.1 Vulnerability Categories

| Category | Examples | Risk Level |
|----------|----------|------------|
| Unpatched software | OS missing security updates, outdated application versions | High |
| Weak authentication | Default passwords, no MFA, shared accounts | High |
| Misconfigured services | Open ports, unnecessary services running, permissive firewall rules | Medium–High |
| Missing encryption | Data at rest unencrypted, cleartext protocols (Telnet, FTP, HTTP) | Medium–High |
| Insufficient logging | No audit trail, log tampering possible | Medium |
| Physical access weaknesses | Unlocked server rooms, unattended workstations | Medium |

### 4.2 Steps in a Vulnerability Assessment

1. **Asset identification** — Enumerate all hardware, software, and data assets in scope
2. **Threat modelling** — Identify which threats are relevant to each asset
3. **Vulnerability scanning** — Use tools (e.g. OpenVAS, Nessus, Windows Security Baseline Analyser) to detect known vulnerabilities
4. **Manual review** — Inspect configurations, user accounts, and policies for issues tools may miss
5. **Risk rating** — Score each vulnerability using a framework such as CVSS (Common Vulnerability Scoring System)
6. **Reporting** — Document findings in a vulnerability report for management decision

---

## 5.0 Security Policy and Regulatory Requirements

### 5.1 Types of Security Policy Documents

| Document Type | Purpose |
|--------------|---------|
| Acceptable Use Policy (AUP) | Defines permitted and prohibited uses of organisational IT resources |
| Password Policy | Specifies minimum password complexity, length, age, and reuse rules |
| Access Control Policy | Defines who may access which resources and under what conditions |
| Incident Response Policy | Outlines procedures for detecting, containing, and recovering from security incidents |
| Data Classification Policy | Categorises data by sensitivity (e.g. Public, Internal, Confidential, Restricted) |
| Patch Management Policy | Specifies timelines and procedures for applying security updates |

### 5.2 Malaysian Regulatory Context

| Regulation / Standard | Relevance |
|----------------------|-----------|
| Personal Data Protection Act 2010 (PDPA) | Requires organisations handling personal data to implement adequate security controls |
| National Cyber Security Policy (NCSP) | Provides the national framework for protecting critical information infrastructure |
| MS ISO/IEC 27001 | International standard for information security management systems (ISMS); adopted as Malaysian Standard |
| CyberSecurity Malaysia Guidelines | Sector-specific security advisories and baseline requirements |

---

## 6.0 Security Requirements Analysis Process

The systems administrator follows a structured process to identify and document security requirements:

| Step | Activity | Output |
|------|----------|--------|
| 1. Scope definition | Define the boundary of the system or environment to be secured | System boundary diagram |
| 2. Asset inventory | List all assets: servers, workstations, network devices, data stores, applications | Asset register |
| 3. Threat identification | Identify all plausible threats using threat categories and threat modelling | Threat register |
| 4. Vulnerability assessment | Scan and review for weaknesses | Vulnerability report |
| 5. Risk analysis | Rate each risk (likelihood × impact) | Risk register |
| 6. Control selection | Select appropriate controls (preventive, detective, corrective) | Control list |
| 7. Requirements specification | Document security requirements in formal language for implementation | Security Requirements Specification (SRS) |

### 6.1 Security Requirements Specification (SRS) Structure

A well-formed SRS includes:
- **Purpose and scope:** What system or environment is being secured and why
- **Asset list:** All assets with their classification and value
- **Threat register:** All identified threats with likelihood and impact ratings
- **Vulnerability register:** All identified vulnerabilities with CVSS scores
- **Risk register:** Risk = Likelihood × Impact; prioritised list
- **Control requirements:** Specific, measurable security controls to be implemented
- **Compliance requirements:** Applicable laws, standards, and policies
- **Review schedule:** How often the requirements will be re-assessed

---

## 7.0 Common Errors in Security Requirements Analysis

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Defining scope too narrowly | Critical assets outside scope are unprotected | Include all systems with access to sensitive data, not just servers |
| Treating all risks as equal priority | Resources wasted on low-risk items; critical risks under-addressed | Apply risk rating; prioritise by impact and likelihood |
| Ignoring insider threats | Insider attacks go undetected and unmitigated | Include insider threat scenarios in threat modelling |
| Relying solely on automated scanning | Manual misconfigurations and policy gaps missed | Combine tool-based scanning with manual policy review |
| Failing to link requirements to controls | Controls implemented without documented justification | Every control must trace back to a risk in the risk register |
| Not reviewing requirements periodically | Outdated SRS leads to security gaps as the environment changes | Schedule SRS reviews at least annually or after significant changes |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer System Security Control — CoCu 2
- Personal Data Protection Act 2010 (Malaysia)
- MS ISO/IEC 27001:2022 Information Security Management Systems
- NIST SP 800-30 Rev 1: Guide for Conducting Risk Assessments
- CyberSecurity Malaysia — Baseline Security Standard for Government
- CompTIA Security+ Study Guide — Domain: Threats, Attacks and Vulnerabilities