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
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C03 COMPUTER SYSTEM SECURITY MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM SECURITY MANAGEMENT REQUIREMENTS<br>2. PLAN COMPUTER SYSTEM SECURITY MANAGEMENT<br>3. MANAGE COMPUTER SYSTEM SECURITY<br>4. PRODUCE COMPUTER SYSTEM SECURITY MANAGEMENT REPORT |
| NO. KOD | IT-020-5:2013-C03/KP(3/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-managing-computer-system-security

**TUJUAN:** Kertas rujukan untuk KP-03-managing-computer-system-security.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Oversee the implementation and operation of ISMS controls across the organisation
2. Manage Security Operations Centre (SOC) functions including monitoring, detection, and escalation
3. Direct and oversee the information security incident management lifecycle
4. Govern identity and access management (IAM) at an organisational level
5. Manage vulnerability and patch management programmes from a governance perspective
6. Maintain security awareness and training programmes for all staff

---

## 1.0 Overseeing ISMS Control Implementation

The security manager at Level 5 is responsible for **ensuring** that controls defined in the Security Management Plan and Risk Treatment Plan are implemented effectively — not necessarily performing the implementation directly, but overseeing, directing, and verifying it.

### 1.1 Control Implementation Oversight Framework

| Oversight Activity | Description | Frequency |
|-------------------|-------------|-----------|
| Control status tracking | Monitor implementation progress against the Risk Treatment Plan schedule | Monthly |
| Control effectiveness review | Verify that implemented controls achieve their intended security objective | Quarterly |
| Exception management | Review and approve exceptions to security policies with compensating controls | As required |
| Control owner accountability | Ensure designated control owners are fulfilling their responsibilities | Monthly |
| Evidence collection | Gather and maintain evidence of control operation for audit purposes | Ongoing |

### 1.2 Key Control Domains to Manage

| Control Domain | Management Focus |
|---------------|-----------------|
| Access Control (IAM) | Policy enforcement, privileged access governance, periodic access reviews |
| Network Security | Firewall rule governance, network segmentation policy, remote access controls |
| Endpoint Security | Endpoint protection policy, BYOD governance, mobile device management (MDM) |
| Data Protection | Data classification scheme, encryption policy, DLP programme oversight |
| Cryptography | Key management policy, encryption standards (algorithm and key length) |
| Application Security | Secure development policy, third-party application vetting, patch governance |
| Physical Security | Physical access policy, data centre security standards, clear desk enforcement |
| Supplier Security | Third-party security assessment, contract clause management, ongoing monitoring |

---

## 2.0 Security Operations Centre (SOC) Management

The SOC is the operational hub for security monitoring and incident first-response. At Level 5, the manager's role is to **direct and govern** the SOC — defining its mandate, staffing, tools, processes, and performance metrics.

### 2.1 SOC Functions and Management Responsibilities

| SOC Function | Operational Team Does | Manager Oversees |
|---|---|---|
| Security Monitoring | Monitors SIEM alerts 24×7; triages events | Defines alert thresholds; reviews escalation policy |
| Threat Intelligence | Consumes threat feeds; updates detection rules | Approves threat intelligence sources; reviews threat landscape |
| Incident Detection | Identifies potential security incidents from alerts | Reviews detection coverage; approves detection use cases |
| Incident Response | Executes first-response and containment procedures | Approves escalation decisions; directs major incident response |
| Forensic Analysis | Conducts digital forensics on affected systems | Commissions investigations; reviews findings |
| Reporting | Produces operational SOC reports | Reviews SOC metrics; escalates to management |

### 2.2 SOC Performance Metrics (Key Performance Indicators)

| KPI | Definition | Target Example |
|-----|-----------|----------------|
| Mean Time to Detect (MTTD) | Average time from incident occurrence to SOC detection | ≤ 4 hours |
| Mean Time to Respond (MTTR) | Average time from detection to containment actions | ≤ 2 hours |
| Alert-to-Incident Ratio | Proportion of alerts that escalate to confirmed incidents | < 5% (low false positive rate) |
| False Positive Rate | Proportion of triaged alerts that are non-events | < 20% |
| Incident Closure Rate | % of incidents closed within SLA | ≥ 95% |
| SOC Coverage | Hours of active monitoring per day | 24×7 (or defined business hours + automated off-hours) |

### 2.3 Security Information and Event Management (SIEM)

A SIEM system aggregates log data from across the IT environment and correlates events to detect potential security incidents. The manager must govern:

- **Log source coverage** — which systems are feeding logs to the SIEM (servers, firewalls, endpoints, applications, cloud platforms)
- **Retention policy** — how long logs are retained (typically 12 months online, 24–36 months archived), aligned with regulatory requirements
- **Use case library** — the detection rules (correlation rules) that trigger alerts; these must be reviewed and updated regularly
- **SIEM integration** — connection to threat intelligence platforms, ticketing systems, and incident response tools

---

## 3.0 Information Security Incident Management

ISO/IEC 27001:2022 Clause 8 and Annex A controls A.5.24–A.5.28 require a formal incident management process. At Level 5, management is responsible for governing this process and directing major incident response.

### 3.1 Incident Management Lifecycle

| Phase | Key Activities | Management Role |
|-------|---------------|----------------|
| **1. Identification** | SOC detects and classifies potential incident | Reviews classification criteria; approves severity thresholds |
| **2. Containment** | Isolate affected systems; prevent spread | Approves containment actions that impact business operations |
| **3. Eradication** | Remove threat; patch vulnerabilities exploited | Approves system changes; coordinates with IT management |
| **4. Recovery** | Restore systems; verify integrity; resume operations | Approves return to production; coordinates with business units |
| **5. Post-Incident Review** | Root cause analysis; lessons learned; report | Chairs post-incident review meeting; approves final report |
| **6. Improvement** | Update controls, procedures, and training | Ensures corrective actions are implemented; tracks closure |

### 3.2 Incident Severity Classification

| Severity Level | Criteria | Response Time | Management Involvement |
|---------------|----------|---------------|----------------------|
| Critical (P1) | Confirmed breach; data exfiltration; ransomware active; major service down | Immediate (< 1 hour) | Direct management involvement; Board notification may be required |
| High (P2) | Suspected breach; significant system compromise; critical service degraded | < 4 hours | Management notified; escalation decision required |
| Medium (P3) | Isolated malware; policy violation; minor service impact | < 24 hours | Management briefed; standard response procedures |
| Low (P4) | Minor policy violation; informational alert; single endpoint affected | < 72 hours | Logged and tracked; management review at next cycle |

### 3.3 Legal and Regulatory Notification Obligations

| Obligation | Trigger | Timeframe | Notified Party |
|-----------|---------|-----------|----------------|
| Personal Data Protection Act 2010 (Malaysia) | Breach of personal data | As soon as practicable | Personal Data Protection Commissioner (PDPC) |
| Bank Negara Malaysia RMiT | Technology or cyber incident at financial institution | Within 1 hour (critical); 24 hours (significant) | BNM |
| Securities Commission Guidelines | Cyber incident at capital market entity | Immediately for critical events | Securities Commission |
| Contractual obligations | Breach affecting customer data | As specified in SLA / contract | Affected customers |

---

## 4.0 Identity and Access Management (IAM) Governance

IAM governance ensures that access to systems and data is appropriately controlled throughout the user lifecycle.

### 4.1 IAM Governance Principles

| Principle | Description |
|-----------|-------------|
| Least Privilege | Users are granted only the minimum access required to perform their role |
| Need to Know | Access to sensitive information is restricted to those with a legitimate business need |
| Separation of Duties | Critical functions are divided so that no single person can complete a high-risk action alone (e.g. payment approval and payment execution must be separate roles) |
| Mandatory Access Review | All user accounts and their privileges must be reviewed on a scheduled basis (typically quarterly for privileged accounts, annually for standard users) |
| Joiner-Mover-Leaver (JML) | Formal processes ensure access is provisioned on joining, updated on role change, and revoked promptly on departure |

### 4.2 Privileged Access Management (PAM)

Privileged accounts (system administrators, database administrators, network engineers) pose the highest access risk and require additional governance:

| PAM Control | Description |
|-------------|-------------|
| Privileged Access Workstation (PAW) | Dedicated, hardened workstation used only for privileged administration tasks |
| Just-in-Time (JIT) Access | Privileged access granted on-demand for a defined time window, then automatically revoked |
| Privileged Account Inventory | Complete register of all privileged accounts, their owners, and last-use dates |
| Session Recording | All privileged sessions recorded for audit and forensic purposes |
| Multi-Factor Authentication (MFA) | MFA mandatory for all privileged account logins without exception |

---

## 5.0 Vulnerability and Patch Management Governance

### 5.1 Vulnerability Management Programme

| Stage | Activity | Management Responsibility |
|-------|----------|--------------------------|
| Discovery | Automated vulnerability scanning of all assets (weekly minimum) | Approves scan scope; reviews coverage |
| Assessment | Prioritise vulnerabilities by CVSS score, asset criticality, and exploitability | Reviews prioritisation criteria and escalation thresholds |
| Remediation | IT team applies patches or implements compensating controls | Approves emergency change requests; reviews remediation SLAs |
| Verification | Re-scan to confirm vulnerabilities are resolved | Reviews closure rate metrics |
| Reporting | Monthly vulnerability status report | Reviews and escalates critical unresolved vulnerabilities |

### 5.2 Patch Management SLAs

| Vulnerability Severity | CVSS Score | Patch Deadline |
|----------------------|------------|----------------|
| Critical | 9.0–10.0 | 24 hours (emergency change) |
| High | 7.0–8.9 | 7 days |
| Medium | 4.0–6.9 | 30 days |
| Low | 0.1–3.9 | 90 days |

---

## 6.0 Security Awareness and Training Management

ISO/IEC 27001:2022 Clause 7.3 requires all personnel to be aware of the information security policy and their contribution to ISMS effectiveness.

### 6.1 Security Awareness Programme Components

| Component | Target Audience | Frequency | Format |
|-----------|----------------|-----------|--------|
| Security awareness induction | All new employees | On joining | Online module + face-to-face briefing |
| Annual security refresher | All staff | Annually | E-learning or classroom |
| Phishing simulation | All staff | Quarterly | Simulated phishing emails; click-rate tracking |
| Role-based security training | IT, security, finance, HR staff | Annually + on role change | Technical training by function |
| Incident response drills | Security team, IT management | Bi-annually | Tabletop exercise or live simulation |
| Executive security briefing | Board, senior management | Semi-annually | Summary of threat landscape, incidents, and ISMS status |

### 6.2 Training Effectiveness Measurement

| Metric | Description | Target |
|--------|-------------|--------|
| Training completion rate | % of staff who completed mandatory training | ≥ 95% |
| Phishing click rate | % of staff who click simulated phishing links | < 5% (trending down) |
| Incident reporting rate | % of incidents reported by non-IT staff vs. detected by SOC | Increasing trend |
| Policy acknowledgement | % of staff who have signed the acceptable use policy | 100% |

---

## Rujukan / References

- ISO/IEC 27001:2022 — Information Security Management Systems — Requirements
- ISO/IEC 27035:2023 — Information Security Incident Management
- ISO/IEC 27002:2022 — Controls A.5.24–A.5.28 (Incident Management), A.5.15–A.5.18 (Access Control)
- NIST SP 800-61 Rev.2 — Computer Security Incident Handling Guide
- CIS Controls v8 — Controls 4 (IAM), 7 (Vulnerability Management), 17 (Incident Response)
- Bank Negara Malaysia, RMiT Policy Document, 2020
- NOSS IT-020-5:2013 Computer Systems Management — CoCU 3