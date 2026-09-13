# CoCu 7: Server Scripting (L5, 120 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) |
| LEVEL | L5 | L5 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 7: Server Scripting (Pengskrip Pelayan) | CoCu 7: Server Scripting (Pengskrip Pelayan) |
| NO. AND WORK ACTIVITY STATEMENT | ASSESS SERVER SCRIPTING REQUIREMENT · DEVELOP SERVER SCRIPT · EXECUTE AND DEPLOY SERVER SCRIPT · PREPARE SERVER SCRIPT DOCUMENTATION | ASSESS SERVER SCRIPTING REQUIREMENT · DEVELOP SERVER SCRIPT · EXECUTE AND DEPLOY SERVER SCRIPT · PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. CODE | IT-020-5:2013 - CoCu 7 / P(7/7) | PAGE: 229 - 236 |


| SET-UP CONTEXT | SMALL-SCALE / SINGLE-PLATFORM AUTOMATION | ENTERPRISE / MULTI-PLATFORM AUTOMATION STRATEGY |
|----------------|-------------------------------------------|--------------------------------------------------|
| Automation scope and governance | Organisation operates a small server environment on a single platform (Linux or Windows). Automation is managed by a small team or individual administrator. Governance is informal, with scripts developed and deployed as needed. Management oversees scripting activities through periodic review and ensures alignment with departmental objectives. | Organisation operates a large-scale, multi-platform environment (Linux, Windows, cloud). A dedicated automation team reports to IT management. Formal governance framework defines scripting standards, approval workflows, security requirements, and compliance obligations. Management establishes an automation strategy aligned with organisational goals and regulatory requirements. |
| Development and deployment governance | Scripts are developed, tested, and deployed following a basic change control process. Management authorises deployment after reviewing test results and risk assessment. Version control is used to track changes and enable rollback. Deployment scheduling is coordinated with operations to minimise service disruption. | Scripting development follows a formal software development lifecycle with defined stages: requirements analysis, design, development, code review, testing, UAT, and production deployment. Management governs the process through stage-gate approvals, change advisory board reviews, and deployment authorisation. Enterprise version control, CI/CD pipelines, and configuration management tools are mandated. |
| Reporting and documentation | Management requires basic documentation for each automation initiative: purpose, scope, ownership, and operational procedures. Script inventory is maintained and reviewed periodically. Reports on automation effectiveness and incident impact are prepared for departmental review. | Management mandates comprehensive documentation standards: automation strategy documents, script inventory with ownership and classification, operational runbooks, test reports, and periodic management reports. Automation KPIs (uptime improvement, manual effort reduction, incident prevention) are tracked and reported to senior leadership. Compliance with documentation standards is audited. |


| Type / Tool | Description |
|-------------|-------------|
| Automation strategy and governance | The process of planning, evaluating, and governing the organisation's approach to server automation. Management assesses current manual processes, identifies automation opportunities, and prioritises initiatives based on business impact, risk reduction, and cost-benefit analysis. An automation governance framework defines roles, responsibilities, approval workflows, and escalation paths. Regular strategic reviews ensure automation initiatives remain aligned with organisational objectives and regulatory requirements. |
| Scripting standards and code review policy | Organisational standards that govern how scripts are written, reviewed, and approved before deployment. Management establishes coding conventions, naming standards, documentation requirements, and mandatory peer review processes. Code review policies ensure scripts meet quality, security, and maintainability requirements before authorisation. Compliance with scripting standards is monitored through periodic audits, and deviations are reported to management for corrective action. |
| Script lifecycle management | A governance framework covering the full lifecycle of automation scripts: development, testing, deployment, operational use, maintenance, and retirement. Management oversees each lifecycle stage through defined approval gates and ensures scripts are inventoried, version-controlled, and assigned to responsible owners. Retirement criteria are established to ensure obsolete scripts are decommissioned in an orderly manner. Lifecycle management ensures the organisation maintains a current, secure, and well-documented automation portfolio. |
| Security governance for privileged scripts | The policies and controls governing scripts that execute with elevated privileges (root, administrator, service accounts). Management mandates least-privilege execution, secure credential storage, input validation requirements, and audit logging for all privileged automation. Security reviews are required before deployment authorisation, and periodic re-certification ensures continued compliance with the organisation's security policy. Incidents involving privileged script misuse or compromise are escalated and reported to management. |
| Version control and change management | The governance of version control systems and change management processes applied to automation assets. Management ensures all scripts are stored in approved repositories with enforced branching, merging, and tagging standards. Change requests for production scripts follow the organisation's change advisory board process, including risk assessment, rollback planning, and post-deployment verification. Audit trails from version control are maintained for compliance reporting and incident investigation. |
| Automation ROI and performance metrics | The measurement and reporting of automation programme outcomes to management and stakeholders. Key performance indicators include manual effort reduction, error rate improvement, mean time to resolution, system uptime contribution, and cost savings. Management evaluates automation ROI to justify continued investment, prioritise new initiatives, and report programme effectiveness to senior leadership. Performance metrics are reviewed periodically and used to drive continuous improvement of the automation strategy. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 18% | 22 | Assess server scripting requirement | 6.6 | 15.4 | 22.0 |
| 25% | 30 | Develop server script | 9.0 | 21.0 | 30.0 |
| 42% | 50 | Execute and deploy server script | 15.0 | 35.0 | 50.0 |
| 15% | 18 | Prepare server script documentation | 5.4 | 12.6 | 18.0 |
| **100%** | **120** | | **36.0** | **84.0** | **120.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) |
| LEVEL | L5 | L5 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 7: Server Scripting (Pengskrip Pelayan) | CoCu 7: Server Scripting (Pengskrip Pelayan) |
| NO. AND WORK ACTIVITY STATEMENT | ASSESS SERVER SCRIPTING REQUIREMENT · DEVELOP SERVER SCRIPT · EXECUTE AND DEPLOY SERVER SCRIPT · PREPARE SERVER SCRIPT DOCUMENTATION | ASSESS SERVER SCRIPTING REQUIREMENT · DEVELOP SERVER SCRIPT · EXECUTE AND DEPLOY SERVER SCRIPT · PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. CODE | IT-020-5:2013 - CoCu 7 / P(7/7) | PAGE: 237 - 244 |


| Management Framework / Tool | Description |
|------------------------------|-------------|
| Automation capability assessment | A management-led evaluation of the organisation's current automation maturity, identifying gaps between existing capabilities and strategic requirements. Assessment covers scripting skills inventory, tooling landscape, process coverage, and governance readiness. Management uses the assessment to develop a roadmap for automation improvement, allocate resources, and set measurable capability targets. Results are reported to senior leadership to secure investment and executive sponsorship. |
| Script development governance framework | A formal framework that governs how automation scripts are proposed, approved, developed, and maintained within the organisation. Management defines the governance structure including roles (script owner, reviewer, approver), stage-gate criteria, escalation procedures, and compliance checkpoints. The framework ensures all scripting activities align with organisational standards, security policies, and regulatory obligations. Governance effectiveness is evaluated through periodic audits and management review. |
| Quality assurance and testing standards | Organisational standards that define testing requirements for all automation scripts before deployment authorisation. Management establishes mandatory testing phases: functionality validation, integration testing, stability assessment, performance benchmarking, and user acceptance testing. Test plans, results, and defect resolution records are documented and reviewed by management before granting deployment approval. Standards are periodically updated to reflect lessons learned from production incidents. |
| Deployment authorisation and change control | The management process for authorising script deployment into production environments. All deployment requests are evaluated through the organisation's change advisory board, which assesses risk, rollback readiness, and business impact. Management ensures deployments are scheduled within approved maintenance windows and that affected stakeholders are notified. Post-deployment verification and monitoring requirements are defined, and management reviews deployment outcomes to confirm success criteria are met. |
| Script documentation and knowledge management standards | Management-mandated standards for documenting automation assets and ensuring organisational knowledge retention. Documentation requirements include programmer's manuals, operational runbooks, test reports, and ownership records for every production script. Management oversees a centralised knowledge management system where documentation is version-controlled, searchable, and accessible to authorised personnel. Compliance with documentation standards is audited, and gaps are reported to management for remediation. |
| Operational monitoring and incident response for automation | The governance of monitoring systems and incident response procedures for automated scripts and scheduled tasks. Management ensures all production automation is covered by monitoring tools that detect failures, performance degradation, and unexpected behaviour. Incident response procedures define escalation paths, root cause analysis requirements, and management reporting obligations. Management reviews automation incident trends periodically and directs corrective actions to improve reliability and reduce operational risk. |


| Scripting Language / Platform | Description |
|-------------------------------|-------------|
| Bash (Linux/Unix) | The Bourne Again Shell, the default command-line interpreter on most Linux distributions. Scripts automate file operations, service management, cron jobs, and system monitoring. Supports variables, loops, conditionals, functions, and piping between commands. Widely used for server administration automation on Linux platforms. |
| PowerShell (Windows) | A command-line shell and scripting language built on .NET. Provides rich cmdlets for managing Windows Server, Active Directory, Exchange, SQL Server, and Azure. Supports objects (not just text), modules, remote execution, and desired state configuration. PowerShell 7+ is cross-platform. |
| Python | A general-purpose programming language increasingly used for server automation, configuration management, and API integration. Libraries such as paramiko (SSH), psutil (system monitoring), and boto3 (AWS) extend its capabilities. Readable syntax makes it suitable for both simple scripts and complex automation frameworks. |
| C++ and compiled languages | Used for performance-critical server applications, custom services, and system-level utilities where scripting languages are too slow. C++ programs are compiled to machine code and can interact directly with operating system APIs and hardware. Server applications written in C++ include custom daemons, network services, and monitoring agents. Deployment requires compilation on or for the target platform, and source code is managed alongside scripts in version control. |


| Common Issue | Root Cause | Management Action |
|--------------|------------|-------------------|
| Lack of automation governance framework | Automation initiatives are pursued ad hoc without formal oversight; no defined standards, approval processes, or strategic alignment | Establish and mandate an automation governance framework that defines roles, approval workflows, scripting standards, and compliance requirements; assign executive sponsorship and conduct periodic governance reviews |
| Scripts running with excessive privileges (security risk) | No organisational policy enforcing least-privilege execution; privilege requirements not reviewed during development or deployment authorisation | Mandate security review and least-privilege certification for all scripts before deployment; establish a privileged script register with periodic re-certification; ensure audit logging of all elevated-privilege automation and report violations to management |
| No script inventory or ownership assignment | Scripts developed informally without registration; no centralised repository or ownership tracking; departing staff leave undocumented automation | Implement a mandatory script inventory system with assigned owners, classification, and review schedules; require inventory registration as a condition of deployment authorisation; audit the inventory periodically and report unowned or undocumented scripts to management for remediation |
| Automation failures not monitored or reported | No centralised monitoring of scheduled automation; failure alerts not configured; management unaware of automation-related incidents | Deploy monitoring and alerting for all production automation; establish incident response procedures with defined escalation paths and management reporting obligations; include automation reliability metrics in periodic operational reports to senior leadership |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Assess server scripting requirement | Understand concepts related to: Assess server scripting requirement | Successfully execute: Assess server scripting requirement | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Develop server script | Understand design and development principles | Design and develop systems/documents/procedures | Product review; quality assessment | Completed deliverable; design documentation; review feedback |
| Execute and deploy server script | Understand concepts related to: Execute and deploy server script | Successfully execute: Execute and deploy server script | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Prepare server script documentation | Know tools, parts, and materials needed | Gather and organize tools, parts, and materials | Practical observation of tool/material preparation; checklist verification | Photo/log of prepared toolkit; materials checklist |

## Practical Exercises

The following management-level exercise scenarios develop the strategic and governance competencies required for Server Scripting. Each exercise is designed for L5 managers and includes case studies, policy scenarios, governance frameworks, strategic planning simulations, and assessment criteria aligned with NOSS standards.

### Assess server scripting requirement

**Objective:** Execute assess server scripting requirement following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for assess server scripting requirement
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

### Develop server script

**Objective:** Execute develop server script following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for develop server script
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

### Execute and deploy server script

**Objective:** Execute execute and deploy server script following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for execute and deploy server script
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

### Prepare server script documentation

**Objective:** Execute prepare server script documentation following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for prepare server script documentation
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
- **Mapping:** Document script purpose, usage, and parameters clearly for other administrators; present automation proposals and efficiency gains to management; communicate script deployment plans and change impacts to operations teams

### 2. Teamwork & Collaboration
- **Mapping:** Collaborate with system administrators and network teams to identify automation opportunities; share scripts and libraries with the team through version control; coordinate script deployment and testing with operations staff

### 3. Problem-solving
- **Mapping:** Debug script errors and unexpected behaviour in production environments; develop scripts that handle edge cases and error conditions gracefully; automate troubleshooting and diagnostic routines to accelerate incident resolution

### 4. Initiative & Self-reliance
- **Mapping:** Identify repetitive server administration tasks suitable for automation; develop scripts proactively to reduce manual workload and human error; take responsibility for script reliability, testing, and maintenance

### 5. Planning & Organizing
- **Mapping:** Plan script development from requirements assessment through testing and deployment; organize script libraries with consistent naming, versioning, and documentation; manage deployment schedules to avoid disruption to production services

### 6. Self-management & Safety Awareness
- **Mapping:** Test scripts in non-production environments before deployment; implement safeguards (confirmation prompts, dry-run modes, logging) to prevent accidental damage; ensure scripts comply with security policies and do not introduce vulnerabilities

### 7. Technology Use & Technical Proficiency
- **Mapping:** Write scripts in PowerShell (Windows) and Bash/Python (Linux/Unix); use task scheduling, configuration management, and version control tools; automate server provisioning, monitoring, backup, and maintenance tasks

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Stay current on scripting languages, automation frameworks, and server management tools; analyze script performance and refine for efficiency; learn from deployment issues to improve script robustness and error handling



## Attitude, Safety and Environmental

### Workplace Safety
- **Secure Credential Handling:** Never hardcode passwords, API keys, or other credentials in scripts. Use secure credential stores (e.g. Windows Credential Manager, Linux secret-tool, HashiCorp Vault) or environment variables with restricted file permissions. Rotate credentials regularly and audit scripts for accidental credential exposure before committing to version control.
- **Script Execution Safety:** Always test scripts in a staging or non-production environment before deploying to production servers. Implement dry-run modes, confirmation prompts for destructive operations, and clear rollback procedures. Verify that the script's intended actions match the change request before execution, and maintain a documented rollback plan for every deployment.
- **Audit Logging of Automated Actions:** Ensure all scripts produce detailed logs of their actions, including timestamps, affected resources, success/failure status, and the user or service account that triggered execution. Centralise logs for review and retain them according to organisational audit policy. Logs enable rapid incident investigation and demonstrate compliance with change management procedures.
- **Least-Privilege Execution:** Run scripts with the minimum privileges required to complete the task. Avoid running automation as root or domain administrator unless absolutely necessary; use sudo or runas for specific elevated commands only. Review and enforce execution policies (e.g. PowerShell Execution Policy, Linux file permissions) to prevent unauthorised script execution and reduce the blast radius of script errors.

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
- Python Documentation and Best Practices – PEP 8 Style Guide
- Bash Shell Scripting Guide – Advanced Scripting Techniques
- PowerShell Documentation and Advanced Scripting for Windows Automation
- CompTIA Linux+ Certification – Shell Scripting and Automation

**Technical References and Best Practices:**

- CompTIA Server+ – Automation and Infrastructure as Code Fundamentals
- Infrastructure as Code (IaC) – Terraform, Ansible, and Puppet Best Practices
- Git and Version Control for Script Development and Collaboration
- Continuous Integration and Continuous Deployment (CI/CD) Pipelines
- Security Best Practices for Scripts – Error Handling, Logging, and Secure Credentials

**Contact hour:** [[00_Contact-hour_IT-020-5-L5-Management]]


---

↑ [README](../../README.md) · **IT-020-5** > CoCu 7 - Server Scripting

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-5-L5-Management.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Management-Overview.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Asset-Management.md) · [03_CoCu-3](03_CoCu-3-Computer-System-Security-Management.md) · [04_CoCu-4](04_CoCu-4-Disaster-Recovery-Management.md) · [05_CoCu-5](05_CoCu-5-Computer-System-Network-Project-Management.md) · [06_CoCu-6](06_CoCu-6-SOP-Development-And-Implementation.md)

**Other levels:** [IT-020-3 (L3)](../IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md) · [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md)
