# CoCu 2: Computer System Security Control (L4, 200 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) |
| LEVEL | L4 | L4 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 2: Computer System Security Control (Kawalan Keselamatan Sistem Komputer) | CoCu 2: Computer System Security Control (Kawalan Keselamatan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | IDENTIFY SECURITY REQUIREMENTS · IMPLEMENT ACCESS CONTROL AND AUTHENTICATION · CONFIGURE FIREWALL AND NETWORK SECURITY · MANAGE PATCHES AND SECURITY UPDATES · DOCUMENT SECURITY CONFIGURATION AND INCIDENTS | IDENTIFY SECURITY REQUIREMENTS · IMPLEMENT ACCESS CONTROL AND AUTHENTICATION · CONFIGURE FIREWALL AND NETWORK SECURITY · MANAGE PATCHES AND SECURITY UPDATES · DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. CODE | IT-020-4:2013 - CoCu 2 / P(2/6) | PAGE: 25 - 38 |


| SET-UP CONTEXT | INTERNAL NETWORK / ENDPOINT SECURITY | PERIMETER / INTERNET-FACING SECURITY |
|----------------|---------------------------------------|----------------------------------------|
| Scope and trigger | Security controls applied to internal endpoints (workstations, laptops, internal servers) within the corporate network. Focus on user access control, Group Policy enforcement, antivirus deployment, and patch management for domain-joined devices. Triggered by new device deployment, user onboarding, or periodic security review per organisational policy. | Security controls applied to perimeter devices and internet-facing services (web server, email gateway, VPN endpoint). Focus on firewall rule management, intrusion detection/prevention, SSL/TLS certificate management, and external vulnerability scanning. Triggered by new service deployment, security audit finding, or threat intelligence alert. |
| Tools and equipment | Group Policy Management Console, Active Directory Users and Computers, Windows Defender / enterprise endpoint protection console, WSUS or SCCM for patch deployment, local Windows Firewall, BitLocker management. Standard workstation for administration. | Firewall management console (hardware appliance or UTM), IDS/IPS appliance or software, vulnerability scanner (e.g. Nessus, OpenVAS), certificate authority or SSL provider portal, SIEM dashboard (e.g. Splunk, Wazuh), VPN concentrator management. Dedicated security workstation in a secured segment. |
| Documentation and reporting | Security configuration record for endpoints: GPO settings applied, antivirus status, patch compliance report, user access review log. Filed per organisational information security management system (ISMS). Periodic compliance report to IT manager. | Perimeter security configuration record: firewall rule set, IDS/IPS signatures, certificate inventory and expiry dates, vulnerability scan results, incident response log. Filed per ISMS and regulatory requirements. Incident reports include timeline, impact analysis, containment actions, and recommendations. |


| Type | Description |
|------|-------------|
| Access control and least-privilege principle | The practice of granting users only the minimum permissions required to perform their job functions. Implemented through user accounts, security groups, and NTFS/share permissions in a Windows domain, or file permissions and sudo rules in Linux. The administrator creates role-based groups, assigns permissions to groups rather than individual users, and conducts periodic access reviews to remove unnecessary rights. Misconfigured access control is the most common cause of data exposure and privilege escalation. |
| Multi-factor authentication (MFA) | An authentication method that requires users to provide two or more verification factors -- something they know (password), something they have (token, smart card, mobile app), or something they are (fingerprint, facial recognition). MFA significantly reduces the risk of unauthorised access even if a password is compromised. The administrator configures MFA through Active Directory, Azure AD, or third-party providers and manages enrolment, recovery, and exemption processes. MFA is increasingly required by compliance frameworks and organisational security policies. |
| Firewall and network security (stateful inspection, UTM, ACLs) | Firewalls inspect and filter network traffic based on rules that define allowed or denied connections by source/destination IP, port, and protocol. Stateful inspection tracks active connections and permits return traffic automatically. Unified Threat Management (UTM) appliances combine firewall, antivirus, IDS/IPS, content filtering, and VPN in a single device. Access Control Lists (ACLs) on routers and switches provide additional layer-3 filtering. The administrator defines zones (internal, DMZ, external), creates rules following a deny-by-default policy, and reviews rules periodically to remove stale entries. |
| Intrusion Detection and Prevention System (IDS/IPS) | Network security appliances or software that monitor traffic for known attack signatures, anomalous behaviour, or policy violations. An IDS passively detects and alerts; an IPS actively blocks malicious traffic in real time. Deployed at the network perimeter or at key internal segments. The administrator maintains signature updates, tunes detection rules to reduce false positives, and reviews alerts daily. IDS/IPS logs are forwarded to the SIEM for correlation and incident investigation. |
| Patch management (WSUS, SCCM, manual patching) | The process of identifying, testing, deploying, and verifying security updates for operating systems and applications. Windows Server Update Services (WSUS) provides a free, centralised patch distribution point for Microsoft products. System Center Configuration Manager (SCCM) adds advanced targeting, compliance reporting, and third-party patch support. The administrator classifies patches by severity, tests critical patches in a non-production environment, schedules deployment during maintenance windows, and monitors compliance. Unpatched systems are the primary attack vector for known exploits. |
| Security Information and Event Management (SIEM) | A centralised platform that collects, normalises, and correlates security logs from firewalls, IDS/IPS, servers, endpoints, and applications. SIEM provides real-time dashboards, alerting on suspicious patterns (e.g. multiple failed logins, unusual data transfer), and historical log analysis for incident investigation. Examples include Splunk, Wazuh, and Microsoft Sentinel. The administrator configures log sources, creates correlation rules, and uses SIEM data to produce security incident reports and compliance evidence. |
| Encryption (BitLocker, TLS/SSL, VPN) | Cryptographic techniques that protect data confidentiality at rest and in transit. BitLocker encrypts entire disk volumes on Windows, preventing data access if a device is lost or stolen. TLS/SSL encrypts network traffic between clients and servers (e.g. HTTPS, secure email). VPN creates an encrypted tunnel for remote access to the corporate network. The administrator manages encryption keys, certificates, and recovery passwords, and ensures encryption policies align with organisational and regulatory requirements. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 15% | 30 | Identify security requirements | 9.0 | 21.0 | 30.0 |
| 25% | 50 | Implement access control and authentication | 15.0 | 35.0 | 50.0 |
| 25% | 50 | Configure firewall and network security | 15.0 | 35.0 | 50.0 |
| 25% | 50 | Manage patches and security updates | 15.0 | 35.0 | 50.0 |
| 10% | 20 | Document security configuration and incidents | 6.0 | 14.0 | 20.0 |
| **100%** | **200** | | **60.0** | **140.0** | **200.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) |
| LEVEL | L4 | L4 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 2: Computer System Security Control (Kawalan Keselamatan Sistem Komputer) | CoCu 2: Computer System Security Control (Kawalan Keselamatan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | IDENTIFY SECURITY REQUIREMENTS · IMPLEMENT ACCESS CONTROL AND AUTHENTICATION · CONFIGURE FIREWALL AND NETWORK SECURITY · MANAGE PATCHES AND SECURITY UPDATES · DOCUMENT SECURITY CONFIGURATION AND INCIDENTS | IDENTIFY SECURITY REQUIREMENTS · IMPLEMENT ACCESS CONTROL AND AUTHENTICATION · CONFIGURE FIREWALL AND NETWORK SECURITY · MANAGE PATCHES AND SECURITY UPDATES · DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. CODE | IT-020-4:2013 - CoCu 2 / P(2/6) | PAGE: 39 - 48 |


| Security Hardware / Appliance | Description |
|-------------------------------|-------------|
| Firewall appliance (hardware / UTM) | A dedicated network security device deployed at the perimeter between the internal network and untrusted networks (internet, partner networks). Hardware firewalls offer higher throughput and dedicated processing compared to software firewalls. UTM appliances combine firewall, antivirus gateway, web filtering, IDS/IPS, and VPN in a single device for small-to-medium organisations. The administrator configures security zones, NAT rules, VPN tunnels, and access policies through a web-based or CLI management interface. |
| IDS/IPS appliance | A network security device that inspects traffic in real time for malicious patterns. Deployed inline (IPS) to block threats or out-of-band (IDS) via a mirror/span port to detect and alert without blocking. Enterprise models include Cisco Firepower, Palo Alto, and Snort-based appliances. The administrator positions the sensor at strategic network points, maintains signature databases, and tunes rules to balance detection sensitivity against false-positive rates. |
| MFA tokens and smart cards | Physical or software-based devices used as the second factor in multi-factor authentication. Hardware tokens (e.g. RSA SecurID, YubiKey) generate one-time passwords or respond to cryptographic challenges. Smart cards store digital certificates and require a PIN and card reader. Software tokens (e.g. Microsoft Authenticator, Google Authenticator) run on mobile devices. The administrator manages token inventory, enrolment, replacement, and revocation as part of the identity and access management lifecycle. |
| Certificate Authority (CA) server | A server or service that issues, manages, and revokes digital certificates used for SSL/TLS, code signing, email encryption (S/MIME), and smart card authentication. An internal CA (e.g. Active Directory Certificate Services) issues certificates for internal services and users. Public CAs (e.g. DigiCert, Let's Encrypt) issue certificates for internet-facing services. The administrator manages the CA hierarchy, certificate templates, auto-enrolment policies, and monitors certificate expiry to prevent service outages. |
| Network Access Control (NAC) appliance | A system that enforces security policy on devices attempting to connect to the network. NAC checks device health (antivirus status, patch level, OS version) before granting access and can quarantine non-compliant devices to a remediation VLAN. Supports 802.1X port-based authentication for wired and wireless networks. The administrator defines compliance policies, configures switch/AP integration, and manages exception lists for devices that cannot meet standard requirements. |

![Network Security Zones Architecture](images/security-zones.png)


| Security Software / Tool | Description |
|--------------------------|-------------|
| Enterprise endpoint protection (antivirus/EDR) | Centralised antivirus and endpoint detection and response (EDR) software deployed across all workstations and servers. Provides real-time malware scanning, behavioural analysis, and threat remediation. The management console shows deployment status, threat detections, and quarantine actions across the organisation. The administrator manages signature updates, scan schedules, exclusion policies, and investigates detected threats. Examples include Microsoft Defender for Endpoint, CrowdStrike Falcon, and Symantec Endpoint Protection. |
| WSUS (Windows Server Update Services) | A free Microsoft server role that downloads and distributes Windows and Microsoft product updates within the organisation. The administrator approves or declines updates, targets updates to computer groups, and monitors compliance through built-in reports. WSUS reduces internet bandwidth usage by downloading updates once and distributing locally. Proper configuration includes synchronisation schedule, automatic approval rules for critical updates, and regular cleanup of superseded updates. |
| Group Policy security templates | Predefined sets of security settings that can be imported into Group Policy Objects (GPOs) and applied to domain-joined computers and users. Templates cover password policy, account lockout, audit policy, user rights assignment, and security options. Microsoft provides Security Compliance Toolkit with recommended baselines. The administrator customises templates to match organisational policy, tests in a non-production OU, deploys to production, and documents deviations from the baseline. |
| Vulnerability scanner (Nessus, OpenVAS) | Software that scans systems and network devices for known vulnerabilities, misconfigurations, and missing patches. Produces a prioritised report with severity ratings (critical, high, medium, low) and remediation guidance. The administrator schedules regular scans (weekly or monthly), reviews findings, prioritises remediation based on risk and business impact, and re-scans to verify fixes. Scan results are included in security compliance reports and audit evidence. |


| Common Fault | Cause | Action |
|--------------|-------|--------|
| Unauthorised access to sensitive data or system | Weak or shared passwords; excessive permissions; lack of MFA; stale user accounts not disabled | Enforce strong password policy via GPO; implement MFA; apply least-privilege principle; conduct periodic access reviews; disable accounts of departed employees immediately |
| Malware outbreak across multiple endpoints | Antivirus signatures outdated; user opened malicious email attachment; endpoint protection not deployed to all machines; USB policy not enforced | Update antivirus signatures immediately; isolate affected machines; scan and remediate all endpoints; block malicious indicators in firewall; review email filtering rules; enforce USB device control policy |
| Patch deployment failure or incomplete compliance | WSUS synchronisation failure; client not reporting to WSUS; insufficient disk space on client; patch causes application incompatibility | Check WSUS synchronisation and approval status; verify client GPO for WSUS settings; free disk space on affected clients; test problematic patch in isolated environment; deploy with rollback plan |
| SSL/TLS certificate expiry causes service outage | Certificate renewal not tracked; auto-renewal not configured; certificate authority unreachable at renewal time | Maintain a certificate inventory with expiry dates and alerts; configure auto-renewal where possible; monitor certificate status in SIEM or monitoring tool; renew manually before expiry if automated renewal fails |
| Firewall rule misconfiguration blocks legitimate traffic or permits threats | Overly broad allow rule created during troubleshooting and not removed; deny rule placed before allow rule in rule order; rule applied to wrong zone or interface | Review firewall rule set periodically; follow change management process for all rule changes; test rules after implementation; use logging to verify rule hits; remove temporary rules immediately after troubleshooting |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Identify security requirements | Understand concepts related to: Identify security requirements | Successfully execute: Identify security requirements | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Implement access control and authentication | Understand concepts related to: Implement access control and authentication | Successfully execute: Implement access control and authentication | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Configure firewall and network security | Understand configuration options and best practices | Configure systems correctly according to requirements | Practical configuration; verification against requirements | Configuration screenshots; settings verification; test proof |
| Manage patches and security updates | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |
| Document security configuration and incidents | Know documentation standards and requirements | Create complete and accurate documentation | Documentation review; accuracy verification | Completed documentation; review checklist |

## Practical Exercises

The following administrative and supervisory exercise scenarios develop the competencies required for Computer System Security Control. Each exercise is designed for L4 administrative/supervisory professionals and includes simulation scenarios, planning templates, documentation requirements, and assessment criteria aligned with NOSS standards.

### Lab 2.1: Security Requirements Assessment

**Objective:** Assess organisational security requirements and create a security requirements specification

**Duration:** 90 minutes

**Resources Required:**
Security requirements template, Risk assessment matrix, Compliance checklist (ISO 27001, GDPR, PCI-DSS), Regulatory documents

**Procedures:**
1. Interview stakeholders about current security concerns and incidents
2. Review data classification: identify critical, sensitive, and public data
3. Analyse current security posture (existing firewalls, antivirus, access controls)
4. Identify compliance requirements (industry standards, legal regulations, customer contracts)
5. Conduct risk assessment: identify threats and vulnerabilities
6. Prioritize security controls based on risk and business impact
7. Create security requirements specification with measurable objectives
8. Present recommendations to management for approval

**Expected Outcome:**
Approved security requirements specification aligned with compliance and risk

**Assessment Checklist:**
[ ] Stakeholder input documented
[ ] Data classification completed
[ ] Current state assessed
[ ] Compliance requirements identified
[ ] Risk assessment completed
[ ] Security controls prioritized
[ ] Requirements document approved

### Lab 2.2: Active Directory Security and MFA Deployment Planning

**Objective:** Plan and implement access control using Active Directory and multi-factor authentication

**Duration:** 120 minutes

**Resources Required:**
Active Directory Users and Computers, Group Policy editor, MFA solution (Azure AD/Okta), Access control matrix template

**Procedures:**
1. Design role-based access control (RBAC) groups aligned with job functions
2. Create security groups: departmental groups, project groups, administrative groups
3. Implement group nesting for efficient permission management
4. Configure Group Policy for password complexity and expiry
5. Enable MFA for remote access and privileged accounts
6. Create and test MFA enrolment process
7. Document access control matrix (who has what access)
8. Conduct access review with department managers

**Expected Outcome:**
Implemented access control structure with MFA enabled and documented access matrix

**Assessment Checklist:**
[ ] Security groups created per design
[ ] Group nesting implemented
[ ] Password policy configured
[ ] MFA enrolled for sensitive accounts
[ ] MFA tested and working
[ ] Access matrix documented
[ ] Access review completed and approved

### Lab 2.3: Firewall Rule Configuration and Network Segmentation

**Objective:** Design and configure firewall rules implementing network segmentation and zero-trust principles

**Duration:** 120 minutes

**Resources Required:**
Firewall management console, Network topology diagram, Firewall rule template, Port reference guide

**Procedures:**
1. Design network zones: trusted (internal), DMZ (semi-trusted), untrusted (internet)
2. Identify traffic flows required between zones (e.g., user to file server, web to database)
3. Create baseline firewall rules: allow critical services, deny all else
4. Implement stateful inspection to permit return traffic
5. Configure rules for management traffic (restrict to admin subnet)
6. Test firewall rules: verify allowed traffic flows, block denied traffic
7. Document all firewall rules with business justification
8. Implement monitoring/logging for rule hits

**Expected Outcome:**
Configured firewall with segmented zones, baseline rules, and monitoring in place

**Assessment Checklist:**
[ ] Network zones defined and documented
[ ] Traffic flow requirements identified
[ ] Firewall rules created and prioritized
[ ] Stateful inspection enabled
[ ] Rules tested and verified working
[ ] Rule documentation completed
[ ] Logging and monitoring configured
[ ] Rules reviewed for optimization

### Lab 2.4: WSUS Deployment and Patch Management Planning

**Objective:** Plan and implement a patch management process using WSUS and measure compliance

**Duration:** 90 minutes

**Resources Required:**
WSUS server, Group Policy editor, Patch management policy template, Vulnerability scanner

**Procedures:**
1. Design patch management policy: critical=immediate, high=within 2 weeks, etc.
2. Install and configure WSUS server with appropriate synchronization schedule
3. Create WSUS computer groups: production servers, test workstations, user devices
4. Create GPO to configure clients to use WSUS
5. Approve critical security patches for immediate deployment
6. Test patches in non-production environment before production release
7. Schedule patch deployment during maintenance windows
8. Monitor compliance reporting in WSUS
9. Document patch process and escalation procedures

**Expected Outcome:**
Functional WSUS infrastructure with patch policy documented and compliance monitoring in place

**Assessment Checklist:**
[ ] Patch policy defined and documented
[ ] WSUS installed and configured
[ ] Client GPO configured
[ ] Computer groups created
[ ] Critical patches approved
[ ] Test environment patching successful
[ ] Deployment schedule established
[ ] Compliance monitoring working
[ ] Patch process documented

### Lab 2.5: Security Documentation and Incident Response Procedures

**Objective:** Create comprehensive security documentation and incident response runbooks

**Duration:** 90 minutes

**Resources Required:**
Security policy templates, Incident response template, Change management process, Evidence tracking worksheet

**Procedures:**
1. Create security baseline document: access control rules, firewall rules, hardening standards
2. Create incident response procedure: detection, containment, eradication, recovery, post-incident review
3. Document escalation procedures and contact lists
4. Create security incident log template with fields: date, description, impact, actions, outcome
5. Create change management process for security changes
6. Document forensic preservation procedures for incident investigation
7. Create evidence handling and audit trail procedures
8. Review and approve documentation with security team and management

**Expected Outcome:**
Complete security documentation suite including baselines, incident procedures, and change management

**Assessment Checklist:**
[ ] Security baseline documented
[ ] Incident response procedure created
[ ] Escalation procedures and contacts documented
[ ] Incident log template created
[ ] Change management process documented
[ ] Forensic procedures documented
[ ] Evidence procedures documented
[ ] Documentation reviewed and approved



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Mapping:** Document security policies, firewall rules, and incident reports; present security risk assessments and recommendations to management; communicate security advisories and patch schedules to stakeholders

### 2. Teamwork & Collaboration
- **Mapping:** Coordinate with network and server teams on access control implementation; collaborate with management on security policy enforcement; share threat intelligence and incident findings across departments

### 3. Problem-solving
- **Mapping:** Diagnose security breaches and unauthorized access attempts; evaluate firewall and access control configurations to close vulnerabilities; implement corrective measures after security incidents

### 4. Initiative & Self-reliance
- **Mapping:** Proactively identify security gaps before exploitation; take responsibility for patch management schedules and compliance deadlines; initiate security hardening without waiting for incidents

### 5. Planning & Organizing
- **Mapping:** Plan access control structures and firewall rule sets; organize patch deployment schedules to minimize disruption; manage security audit timelines and remediation activities

### 6. Self-management & Safety Awareness
- **Mapping:** Follow change management procedures for all security configuration changes; manage risk of service disruption during patch application; maintain compliance with data protection regulations (PDPA, GDPR)

### 7. Technology Use & Technical Proficiency
- **Mapping:** Configure firewalls, IDS/IPS, and access control systems; use SIEM tools and log analysis for threat detection; manage encryption, certificate, and authentication infrastructure

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Stay current on emerging threats, CVEs, and security standards; analyze security incidents to improve defensive measures; update security procedures based on audit findings and industry best practices



## Attitude, Safety and Environmental

### Workplace Safety
- **Change Management and Approval:** Always follow formal change management procedures before implementing server configurations or updates. Obtain required approvals and communicate changes to stakeholders to avoid unexpected downtime.
- **Risk Management:** Assess security risks when configuring server roles and implement hardening measures to protect against known vulnerabilities and attack vectors.
- **Data Protection Compliance:** Handle server security configuration in accordance with data protection regulations (e.g., PDPA, GDPR) and organisational security policies. Ensure proper access controls and audit logging are in place.
- **Documentation and Knowledge Sharing:** Maintain comprehensive documentation of all server configurations, changes, and troubleshooting procedures to support team knowledge and ensure continuity during staff transitions.

### Environmental Considerations
- **Sustainable IT Practices:** Plan for efficient resource utilisation (power, cooling, storage) when configuring server environments. Consider virtualisation and consolidation to reduce physical hardware footprint and energy consumption.
- **Responsible Asset Disposal:** Ensure decommissioned servers and storage devices are securely wiped and responsibly recycled through certified e-waste facilities.

### Professional Attitudes
- **Ethical Decision-Making:** Make recommendations based on technical merit and organisational benefit, not vendor preferences or personal convenience. Maintain transparency with stakeholders about trade-offs and costs.
- **Continuous Learning:** Stay current with new server technologies, security standards, and industry best practices to make informed decisions about infrastructure improvements.
- **Team Leadership:** Lead technical teams with respect and clear communication; ensure team members understand the rationale behind decisions and have opportunity to contribute expertise.
- **Accountability:** Take responsibility for system stability and performance; proactively monitor configurations and respond quickly to issues that could impact business operations.

## References

**Official Standards and Frameworks:**

- NOSS IT-020-4:2013 Computer System Administration Syllabus
- Malaysian Standard MS 1546-1:2003 – Information Security Management Code of Practice
- NIST SP 800-53 – Security and Privacy Controls for Information Systems
- ISO/IEC 27001:2022 – Information Security Management Systems Standard
- CompTIA Security+ Certification Study Guide – Cryptography and Access Control

**Technical References and Best Practices:**

- OWASP Top 10 – Application Security Risks and Mitigation Strategies
- Microsoft Active Directory (AD) Security Hardening and Group Policy Administration
- Linux Security – SELinux, AppArmor, and Firewall Configuration (iptables, firewalld)
- Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) Implementation
- NIST Cybersecurity Framework – Core Functions and Categories

**Contact hour:** [[00_Contact-hour_IT-020-4-L4-Administration]]


---

↑ [README](../../README.md) · **IT-020-4** > CoCu 2 - Computer System Security Control

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-4-L4-Administration.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Server-Configuration.md) · [03_CoCu-3](03_CoCu-3-System-Network-Procurement.md) · [04_CoCu-4](04_CoCu-4-Network-Cabling-Management.md) · [05_CoCu-5](05_CoCu-5-Computer-Network-Installation-Management.md) · [06_CoCu-6](06_CoCu-6-Computer-System-Maintenance-Management.md)

**Other levels:** [IT-020-3 (L3)](../IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
