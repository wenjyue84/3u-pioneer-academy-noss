# CoCu 3: Computer System Security Management (L5, 300 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) |
| LEVEL | L5 | L5 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 3: Computer System Security Management (Pengurusan Keselamatan Sistem Komputer) | CoCu 3: Computer System Security Management (Pengurusan Keselamatan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE COMPUTER SYSTEM SECURITY MANAGEMENT REQUIREMENTS · PLAN COMPUTER SYSTEM SECURITY MANAGEMENT · MANAGE COMPUTER SYSTEM SECURITY · PRODUCE COMPUTER SYSTEM SECURITY MANAGEMENT REPORT | ANALYSE COMPUTER SYSTEM SECURITY MANAGEMENT REQUIREMENTS · PLAN COMPUTER SYSTEM SECURITY MANAGEMENT · MANAGE COMPUTER SYSTEM SECURITY · PRODUCE COMPUTER SYSTEM SECURITY MANAGEMENT REPORT |
| NO. CODE | IT-020-5:2013 - CoCu 3 / P(3/7) | PAGE: 121 - 132 |


| SET-UP CONTEXT | ENTERPRISE / MULTI-SITE ENVIRONMENT | REGULATED / COMPLIANCE-DRIVEN ENVIRONMENT |
|----------------|--------------------------------------|---------------------------------------------|
| Security requirements | Enterprise-wide security programme covering multiple departments and sites. Requirements derived from ISO/IEC 27002 and company policy. Scope includes physical, procedural, and technical controls across servers, endpoints, and network infrastructure. | Security programme driven by regulatory obligations (e.g. Computer Crime Act 1997, PDPA 2010, Bank Negara RMiT). Compliance checklist and audit trail are mandatory. Third-party auditors may be involved. |
| Planning and resources | Security management plan with budget for tools (SIEM, antivirus, encryption), staff training, and outsourced penetration testing. Cost-benefit analysis presented to management for approval. | Security management plan must map controls to regulatory clauses. Budget includes compliance audit fees, certification costs, and specialised legal or consulting resources. |
| Report | Security management report covering risk register, incident summary, control effectiveness, and cost analysis. Presented to IT steering committee. | Security management report with compliance status matrix, audit findings, remediation timeline, and evidence package for regulators or auditors. |


| Type / Framework | Description |
|------------------|-------------|
| ISO/IEC 27002 | International standard providing a reference set of information security controls and implementation guidance. Used as the baseline for establishing, implementing, and improving an organisation's information security management system (ISMS). Controls are grouped into categories such as access control, cryptography, physical security, and incident management. The standard helps managers select controls proportionate to the organisation's risk profile. |
| Risk assessment and treatment | The process of identifying threats and vulnerabilities, evaluating likelihood and impact, and selecting treatment options (accept, mitigate, transfer, or avoid). Common frameworks include ISO 27005 and NIST SP 800-30. A risk register is maintained and reviewed periodically. Risk assessment results drive security investment decisions and control prioritisation. |
| Business impact analysis (BIA) | An analysis that identifies critical business processes and the potential impact of disruption (financial loss, reputational damage, regulatory penalty). BIA results feed into security planning by establishing which systems require the highest level of protection and which recovery priorities apply. |
| Security policy and access control | Documented rules governing who may access what resources and under what conditions. Includes user access rights, authentication methods (password, MFA, biometrics), network access control, and physical access control. Policies must be communicated, enforced, and audited regularly. |
| Cryptographic controls | Technologies such as encryption (AES, RSA), hashing (SHA-256), digital signatures, and PKI certificates used to protect data confidentiality and integrity at rest and in transit. Selection of algorithm and key length must follow organisational policy and regulatory requirements. Key management (generation, distribution, storage, rotation, destruction) is critical and must be documented. |
| SIEM and monitoring tools | Security Information and Event Management systems that aggregate logs from servers, firewalls, IDS/IPS, and endpoints; correlate events; and generate alerts. Used for real-time monitoring, incident detection, forensic analysis, and compliance reporting. Examples include Splunk, IBM QRadar, and open-source ELK stack with security plugins. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 23% | 69 | Analyse computer system security management requirements | 20.7 | 48.3 | 69.0 |
| 20% | 60 | Plan computer system security management | 18.0 | 42.0 | 60.0 |
| 50% | 150 | Manage computer system security | 45.0 | 105.0 | 150.0 |
| 7% | 21 | Produce computer system security management report | 6.3 | 14.7 | 21.0 |
| **100%** | **300** | | **90.0** | **210.0** | **300.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) |
| LEVEL | L5 | L5 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 3: Computer System Security Management (Pengurusan Keselamatan Sistem Komputer) | CoCu 3: Computer System Security Management (Pengurusan Keselamatan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE COMPUTER SYSTEM SECURITY MANAGEMENT REQUIREMENTS · PLAN COMPUTER SYSTEM SECURITY MANAGEMENT · MANAGE COMPUTER SYSTEM SECURITY · PRODUCE COMPUTER SYSTEM SECURITY MANAGEMENT REPORT | ANALYSE COMPUTER SYSTEM SECURITY MANAGEMENT REQUIREMENTS · PLAN COMPUTER SYSTEM SECURITY MANAGEMENT · MANAGE COMPUTER SYSTEM SECURITY · PRODUCE COMPUTER SYSTEM SECURITY MANAGEMENT REPORT |
| NO. CODE | IT-020-5:2013 - CoCu 3 / P(3/7) | PAGE: 133 - 142 |


| Management Framework / Tool | Description |
|------------------------------|-------------|
| Security threat and risk evaluation | Systematic identification of threats (viruses, intrusion, interception, inference, insider threat) and evaluation of their likelihood and impact. Results are recorded in a risk register and used to prioritise mitigation. Methods include qualitative scales (high/medium/low) and quantitative models (annual loss expectancy). Regular review ensures emerging threats are captured. |
| Security management plan | A document that consolidates scope, objectives, risk assessment findings, control selection, schedule (Gantt chart), work breakdown structure, budget, and resource allocation. The plan is approved by management, communicated to stakeholders, and reviewed at defined intervals. It serves as the master reference for all security activities. |
| Access control and password policy | Rules for user access provisioning, de-provisioning, periodic review, and password creation (complexity, length, expiry, CAPTCHA, security questions). Includes network access control, remote access rules, and digital file cabinet permissions. Non-compliance must be detected and escalated. |
| Security audit | A structured review of controls against policy and standards (ISO 27002, company policy). Includes checklist preparation, evidence collection, finding documentation, and corrective action tracking. Audits may be internal or by external parties. Results feed into the security management report and continuous improvement cycle. |
| Security awareness programme | Briefings, technical training, demonstrations, and manual preparation aimed at staff and users to raise awareness of threats, policies, and correct behaviour. Effectiveness is measured through feedback, incident rates, and compliance checks. Programmes are refreshed annually or when significant changes occur. |
| Encryption scheme (MD5, AES, RSA) | Application of encryption to protect data confidentiality and integrity. MD5 (legacy hash, not recommended for new systems), SHA-256 (current standard hash), AES (symmetric encryption for data at rest and in transit), and RSA (asymmetric encryption for key exchange and digital signatures). Selection depends on regulatory requirements and data sensitivity. |


| Software / Tool Type | Description |
|----------------------|-------------|
| Antivirus / endpoint protection | Software installed on servers and endpoints to detect, quarantine, and remove malware. Enterprise solutions offer centralised management console, automatic signature updates, and real-time scanning. Examples include Symantec Endpoint Protection, Microsoft Defender for Endpoint, and CrowdStrike Falcon. |
| Firewall (network and host) | Hardware or software that filters network traffic based on rules. Network firewalls protect perimeter and segments; host firewalls protect individual servers. Next-generation firewalls (NGFW) add application-layer inspection, intrusion prevention, and threat intelligence feeds. Configuration is governed by security policy. |
| Patch management software | Tools that scan systems for missing patches, schedule deployment, and verify installation. Ensures operating systems and applications are up to date against known vulnerabilities. Examples include WSUS, SCCM, and Ivanti. Patch management must follow a defined schedule and change control process. |
| Data loss prevention (DLP) tools | Software that monitors, detects, and prevents unauthorised transmission of sensitive data outside the organisation. DLP policies are configured for email, web uploads, USB transfers, and cloud storage. Integration with SIEM and endpoint protection provides centralised visibility into data handling. DLP is required for compliance with data protection regulations such as PDPA 2010. |

![Network Security Zones Architecture](images/security-zones.png)


| Common Issue | Root Cause | Management Action |
|--------------|------------|-------------------|
| Unauthorised access to critical systems | Weak password policy or lack of multi-factor authentication; excessive user privileges | Review and enforce password policy; implement MFA; conduct periodic access rights review and remove unnecessary privileges |
| Malware or ransomware incident | Outdated antivirus signatures; unpatched systems; user clicked phishing link | Ensure automatic updates for AV and OS patches; conduct security awareness training; establish incident response procedure and test it |
| Non-compliance with regulatory requirements | Security controls not mapped to regulation; no audit schedule; staff unaware of obligations | Map controls to regulatory clauses; schedule internal audits; conduct compliance training; engage external auditor if required |
| Data breach or data leakage | Lack of encryption; poor access control; no data loss prevention (DLP) tools | Implement encryption for data at rest and in transit; deploy DLP solution; classify data by sensitivity; review and tighten access controls |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse computer system security management requirements | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Plan computer system security management | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |
| Manage computer system security | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |
| Produce computer system security management report | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |

## Practical Exercises

The following management-level exercise scenarios develop the strategic and governance competencies required for Computer System Security Management. Each exercise is designed for L5 managers and includes case studies, policy scenarios, governance frameworks, strategic planning simulations, and assessment criteria aligned with NOSS standards.

### Analyse computer system security management requirements

**Objective:** Execute analyse computer system security management requirements following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for analyse computer system security management requirements
4. Document decisions with business justification
5. Obtain management and stakeholder approval
6. Plan implementation with success criteria
7. Create monitoring and review procedures

**Expected Outcome:**
Approved management decision document with implementation plan and success metrics

**Assessment Checklist:**
- [ ] Business requirements clearly understood
- [ ] Stakeholder consultation completed
- [ ] Strategy/plan comprehensively developed
- [ ] Decisions justified with evidence
- [ ] Management approval obtained
- [ ] Implementation plan realistic
- [ ] Success criteria measurable
- [ ] Documentation complete and clear

### Plan computer system security management

**Objective:** Execute plan computer system security management following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for plan computer system security management
4. Document decisions with business justification
5. Obtain management and stakeholder approval
6. Plan implementation with success criteria
7. Create monitoring and review procedures

**Expected Outcome:**
Approved management decision document with implementation plan and success metrics

**Assessment Checklist:**
- [ ] Business requirements clearly understood
- [ ] Stakeholder consultation completed
- [ ] Strategy/plan comprehensively developed
- [ ] Decisions justified with evidence
- [ ] Management approval obtained
- [ ] Implementation plan realistic
- [ ] Success criteria measurable
- [ ] Documentation complete and clear

### Manage computer system security

**Objective:** Execute manage computer system security following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for manage computer system security
4. Document decisions with business justification
5. Obtain management and stakeholder approval
6. Plan implementation with success criteria
7. Create monitoring and review procedures

**Expected Outcome:**
Approved management decision document with implementation plan and success metrics

**Assessment Checklist:**
- [ ] Business requirements clearly understood
- [ ] Stakeholder consultation completed
- [ ] Strategy/plan comprehensively developed
- [ ] Decisions justified with evidence
- [ ] Management approval obtained
- [ ] Implementation plan realistic
- [ ] Success criteria measurable
- [ ] Documentation complete and clear

### Produce computer system security management report

**Objective:** Execute produce computer system security management report following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for produce computer system security management report
4. Document decisions with business justification
5. Obtain management and stakeholder approval
6. Plan implementation with success criteria
7. Create monitoring and review procedures

**Expected Outcome:**
Approved management decision document with implementation plan and success metrics

**Assessment Checklist:**
- [ ] Business requirements clearly understood
- [ ] Stakeholder consultation completed
- [ ] Strategy/plan comprehensively developed
- [ ] Decisions justified with evidence
- [ ] Management approval obtained
- [ ] Implementation plan realistic
- [ ] Success criteria measurable
- [ ] Documentation complete and clear



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Mapping:** Present security risk assessments and policy recommendations to senior management; prepare security incident reports and compliance status for board audiences; communicate security awareness programmes across the organisation

### 2. Teamwork & Collaboration
- **Mapping:** Lead the security management team across enterprise and multi-site environments; collaborate with executive leadership on security policy and budget; coordinate with legal, HR, and external auditors on compliance requirements

### 3. Problem-solving
- **Mapping:** Analyze enterprise-wide security threats and develop mitigation strategies; evaluate complex trade-offs between security controls and operational efficiency; respond to and manage security incidents with root cause analysis

### 4. Initiative & Self-reliance
- **Mapping:** Drive proactive security posture improvements including threat hunting and vulnerability management; make high-impact decisions during security incidents; take responsibility for organisational security outcomes and compliance

### 5. Planning & Organizing
- **Mapping:** Develop enterprise security management plans aligned with ISO 27001 and organisational risk appetite; organize security audits, penetration testing, and compliance review schedules; manage security budgets and resource allocation

### 6. Self-management & Safety Awareness
- **Mapping:** Ensure compliance with data protection regulations (PDPA, GDPR) and industry security standards; manage risk of data breaches and system compromise; maintain governance frameworks for access control and incident response

### 7. Technology Use & Technical Proficiency
- **Mapping:** Manage SIEM, endpoint protection, and network security infrastructure; use threat intelligence platforms and vulnerability scanning tools; oversee identity and access management systems at the enterprise level

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Stay informed on emerging cyber threats, attack techniques, and security frameworks; analyze security incidents and audit findings to drive continuous improvement; foster a security-aware culture through ongoing training and awareness



## Attitude, Safety and Environmental

### Workplace Safety
- **Enterprise Risk Governance:** Establish and maintain governance frameworks that identify, assess, and mitigate IT-related risks at the organisational level. Ensure compliance with regulatory requirements and industry standards (ISO 27001, COBIT, ITIL).
- **Change Management at Scale:** Implement formal change management processes that balance innovation with stability; ensure all significant infrastructure changes are reviewed, approved, and documented for organisational accountability.
- **Cybersecurity Leadership:** Foster a culture of security awareness throughout the organisation; establish policies and procedures that protect critical systems, data, and intellectual property from threats.
- **Crisis Preparedness:** Develop and maintain disaster recovery and business continuity plans that protect the organisation's ability to operate during emergencies.

### Environmental Considerations
- **Sustainable IT Strategy:** Develop long-term IT strategies that consider environmental impact; promote energy-efficient infrastructure, virtualisation, and cloud solutions that reduce organisational carbon footprint.
- **Responsible Technology Governance:** Establish policies for responsible technology use, data privacy, and ethical IT practices that align with organisational values and community expectations.

### Professional Attitudes
- **Strategic Integrity:** Make decisions based on long-term organisational benefit; resist short-term pressures that could compromise system stability, security, or sustainability.
- **Visionary Leadership:** Champion innovation and emerging technologies while balancing risk; inspire teams to think strategically about technology's role in organisational success.
- **Stakeholder Trust:** Maintain credibility with executive leadership, boards, and external partners through transparent communication, ethical conduct, and delivery of promised results.
- **Continuous Improvement Culture:** Foster an environment where teams continuously learn from experiences, share knowledge, and improve processes to enhance organisational capability and competitiveness.

## References

**Official Standards and Frameworks:**

- NOSS IT-020-5:2013 Computer System Management Syllabus
- ISO/IEC 27001:2022 and ISO/IEC 27002:2022 – Information Security Standards
- NIST SP 800-39 – Managing Information and Technology Risk
- NIST Cybersecurity Framework – Risk Assessment and Mitigation
- OWASP Security Risk Assessment Methodology

**Technical References and Best Practices:**

- CompTIA CASP+ Certification Study Guide – Advanced Security Management
- Incident Response Planning and Digital Forensics Best Practices
- Security Awareness Training and Change Management for IT Teams
- Third-Party Risk Management and Vendor Security Assessment
- Malaysian Regulatory Compliance – BNM Technology Risk Management Guidelines

**Contact hour:** [[00_Contact-hour_IT-020-5-L5-Management]]


---

↑ [README](../../README.md) · **IT-020-5** > CoCu 3 - Computer System Security Management

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-5-L5-Management.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Management-Overview.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Asset-Management.md) · [04_CoCu-4](04_CoCu-4-Disaster-Recovery-Management.md) · [05_CoCu-5](05_CoCu-5-Computer-System-Network-Project-Management.md) · [06_CoCu-6](06_CoCu-6-SOP-Development-And-Implementation.md) · [07_CoCu-7](07_CoCu-7-Server-Scripting.md)

**Other levels:** [IT-020-3 (L3)](../IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md) · [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md)
