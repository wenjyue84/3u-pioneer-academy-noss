# CoCu 4: Disaster Recovery Management (L5, 350 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) |
| LEVEL | L5 | L5 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 4: Disaster Recovery Management (Pengurusan Pemulihan Bencana) | CoCu 4: Disaster Recovery Management (Pengurusan Pemulihan Bencana) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE DISASTER RECOVERY REQUIREMENTS · DEVELOP DISASTER RECOVERY MANAGEMENT PLAN · IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN · PRODUCE DISASTER RECOVERY MANAGEMENT REPORT | ANALYSE DISASTER RECOVERY REQUIREMENTS · DEVELOP DISASTER RECOVERY MANAGEMENT PLAN · IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN · PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. CODE | IT-020-5:2013 - CoCu 4 / P(4/7) | PAGE: 143 - 156 |


| SET-UP CONTEXT | SINGLE-SITE / SME ENVIRONMENT | MULTI-SITE / ENTERPRISE ENVIRONMENT |
|----------------|-------------------------------|--------------------------------------|
| Recovery requirements | Small-to-medium organisation with one data centre or server room. Recovery requirements derived from SLA and business continuity needs. Key concerns are data backup, hardware availability, and restoration time. Budget is limited; cloud-based DR may be the primary strategy. | Large organisation with multiple sites, data centres, or hybrid cloud infrastructure. Requirements driven by ISO/IEC 24762, regulatory mandates, and complex SLAs with 99.9% uptime. Hot site, warm site, and cold site options are evaluated. |
| Planning and resources | DR plan covers data backup schedule, contact list, recovery site (cloud or off-site), and roles. Cost-benefit analysis focuses on backup storage costs and basic insurance. Staff training is done internally. | DR plan includes full BIA, risk register, recovery strategies for each tier (mission-critical, business-essential, non-critical), Gantt chart, WBS, budget for DR tools (virtualisation, replication), and outsourced DR simulation. DR committee oversees the plan. |
| Report | DR management report with backup status, simulation test results, issues log, and cost summary. Presented to management. | DR management report with DR committee meeting minutes, simulation results (structured walk-through, parallel test, full interruption test), insurance review, environmental impact assessment, and compliance evidence. Presented to DR committee and board. |


| Type / Framework | Description |
|------------------|-------------|
| ISO/IEC 24762:2008 | International standard providing guidelines for ICT disaster recovery services. Covers requirements for DR service providers, facility requirements, and capability assessments. Used as the baseline for establishing DR programmes and evaluating third-party DR services. Helps managers set measurable recovery objectives and audit DR readiness. |
| Business continuity planning (BCP) | A broader framework that encompasses disaster recovery as one component. BCP ensures that critical business functions continue during and after a disaster. Includes business impact analysis, recovery strategy selection, plan development, testing, and maintenance. DR focuses specifically on IT systems recovery within the BCP framework. |
| Recovery point objective (RPO) and recovery time objective (RTO) | RPO defines the maximum acceptable data loss measured in time (e.g. 4 hours means backups must be no older than 4 hours). RTO defines the maximum acceptable downtime before systems must be restored. These two metrics drive decisions on backup frequency, replication technology, and recovery site type (hot, warm, cold). |
| Risk and business impact analysis | Identification of single points of failure (location, expertise, technology, infrastructure, lifespan) and assessment of their impact on business continuity, productivity, service quality, and confidentiality. Results are quantified in financial terms where possible and used to prioritise recovery investments. |
| DR simulation and testing | Exercises to validate the DR plan under controlled conditions. Types include structured walk-through (tabletop review), parallel test (systems recovered in parallel without switching production), and full interruption test (production switched to recovery site). Test results are documented, gaps identified, and the plan is updated accordingly. |
| Data classification and backup strategy | Classification of data by protection level, sensitivity, access level, and criticality. Each class is assigned a backup strategy (full, incremental, differential), frequency, retention period, and storage location (on-site, off-site, cloud). The 3-2-1 rule (3 copies, 2 media types, 1 off-site) is a common baseline. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 33% | 116 | Analyse disaster recovery requirements | 34.8 | 81.2 | 116.0 |
| 15% | 52 | Develop disaster recovery management plan | 15.6 | 36.4 | 52.0 |
| 30% | 104 | Implement computer network disaster recovery management plan | 31.2 | 72.8 | 104.0 |
| 22% | 78 | Produce disaster recovery management report | 23.4 | 54.6 | 78.0 |
| **100%** | **350** | | **105.0** | **245.0** | **350.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) |
| LEVEL | L5 | L5 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 4: Disaster Recovery Management (Pengurusan Pemulihan Bencana) | CoCu 4: Disaster Recovery Management (Pengurusan Pemulihan Bencana) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE DISASTER RECOVERY REQUIREMENTS · DEVELOP DISASTER RECOVERY MANAGEMENT PLAN · IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN · PRODUCE DISASTER RECOVERY MANAGEMENT REPORT | ANALYSE DISASTER RECOVERY REQUIREMENTS · DEVELOP DISASTER RECOVERY MANAGEMENT PLAN · IMPLEMENT COMPUTER NETWORK DISASTER RECOVERY MANAGEMENT PLAN · PRODUCE DISASTER RECOVERY MANAGEMENT REPORT |
| NO. CODE | IT-020-5:2013 - CoCu 4 / P(4/7) | PAGE: 157 - 166 |


| Management Framework / Tool | Description |
|------------------------------|-------------|
| DR plan development process | A structured process: information gathering (brainstorming, interviews, questionnaires, workshops), drafting, management approval, implementation, and review for improvement. The plan document includes mission statement, metrics, DR committee roles, documentation list, vendor contacts, strategies, site designation, data backup procedures, drills schedule, key personnel backup, insurance, communication plan, and emergency procedures. |
| DR committee | A cross-functional team responsible for overseeing DR planning, testing, and execution. Membership typically includes IT management, operations, finance, HR, and legal. The committee approves the DR plan, reviews test results, authorises expenditure, and ensures the plan remains current. Meeting minutes are documented and retained. |
| Cloud computing and virtualisation for DR | Cloud-based DR (DRaaS) enables rapid provisioning of recovery infrastructure without maintaining a dedicated physical site. Virtualisation allows server images to be replicated and spun up quickly at the recovery site. Benefits include lower capital cost, scalability, and faster RTO. Risks include vendor lock-in, bandwidth dependency, and data sovereignty concerns. |
| Preventive disaster recovery tasks | Scheduled activities that reduce the likelihood or impact of a disaster: data backups (full, incremental, differential), application backups, preventive maintenance, hardware health checks, and UPS battery testing. A maintenance calendar is maintained and compliance is tracked. Missed preventive tasks increase recovery risk. |
| DR awareness and training programme | Staff briefings, training sessions, demonstrations, and manual distribution to ensure all personnel understand their DR roles and responsibilities. Includes training on emergency procedures, evacuation, communication channels, and data recovery steps. Effectiveness is measured through drill participation and feedback surveys. |
| Insurance and environmental considerations | Review of insurance policies covering IT equipment, data loss, business interruption, and third-party liability. Environmental considerations include safe disposal of damaged equipment, power and cooling resilience, flood and fire risk at recovery sites. Both are documented in the DR plan and reviewed annually. |


| DR Tool / Technology | Description |
|----------------------|-------------|
| Backup and recovery software | Enterprise tools for scheduling, executing, and verifying backups (full, incremental, differential). Support multiple targets: tape, disk, NAS, SAN, and cloud. Examples include Veeam, Commvault, and Acronis. Features include deduplication, encryption, and automated restore verification. |
| Virtualisation platforms | Hypervisors (VMware vSphere, Microsoft Hyper-V, KVM) that enable server consolidation and rapid recovery by restoring virtual machine images. Snapshots provide point-in-time recovery. Replication features allow near-real-time copy to a secondary site. |
| Disaster recovery planning software | Specialised tools for documenting DR plans, managing contact lists, scheduling tests, and tracking action items. Examples include Fusion Risk Management, Castellan, and Assurance Software. Helps maintain plan currency and audit readiness. |
| Cloud-based disaster recovery (DRaaS) | Disaster Recovery as a Service platforms (e.g. Azure Site Recovery, AWS Elastic Disaster Recovery, Zerto) that replicate servers and data to cloud infrastructure for rapid failover. DRaaS eliminates the need for a dedicated physical recovery site, reducing capital expenditure. Recovery can be tested non-disruptively and initiated within minutes. Selection criteria include RPO/RTO capability, bandwidth requirements, data sovereignty, and cost model (pay-per-use vs reserved). |

![Disaster Recovery Site Types — RTO vs Cost](images/dr-recovery-sites.png)


| Common Issue | Root Cause | Management Action |
|--------------|------------|-------------------|
| DR plan not tested or outdated | No scheduled testing; plan not reviewed after infrastructure changes; staff turnover | Establish mandatory DR simulation schedule (at minimum annually); assign plan ownership; trigger review after every major change |
| Backup failure discovered during recovery | Backup job errors not monitored; media degraded; no automated verification | Implement backup monitoring with alerts; perform periodic restore tests; rotate and retire media per schedule |
| RTO/RPO not met during recovery exercise | Recovery strategy insufficient for the criticality tier; bandwidth to recovery site too low; manual steps too slow | Reassess recovery strategy against BIA results; upgrade replication bandwidth; automate recovery runbooks; consider DRaaS |
| Lack of staff awareness of DR roles | No training programme; DR plan not disseminated; high staff turnover | Conduct DR awareness sessions for all staff; include DR orientation in onboarding; distribute DR pocket cards with contact lists and roles |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse disaster recovery requirements | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Develop disaster recovery management plan | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |
| Implement computer network disaster recovery management plan | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |
| Produce disaster recovery management report | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |

## Practical Exercises

The following management-level exercise scenarios develop the strategic and governance competencies required for Disaster Recovery Management. Each exercise is designed for L5 managers and includes case studies, policy scenarios, governance frameworks, strategic planning simulations, and assessment criteria aligned with NOSS standards.

### Analyse disaster recovery requirements

**Objective:** Execute analyse disaster recovery requirements following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for analyse disaster recovery requirements
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

### Lab 4.1: Enterprise Disaster Recovery Strategy

**Objective:** Develop DR strategy aligned to business continuity objectives

**Duration:** 120 minutes

**Resources Required:**
- DR strategy template
- BIA framework
- Recovery metrics
- Business case

**Procedures:**
1. Conduct Business Impact Analysis (BIA): identify critical systems, RPO/RTO requirements, dependencies
2. Classify applications by criticality: Tier 1 (minutes RPO/RTO), Tier 2 (hours), Tier 3 (days)
3. Evaluate DR strategies: backup and restore, standby site, active-active replication, cloud DR
4. Design DR architecture: on-site backups, off-site copies, geographically distributed sites
5. Define RPO (Recovery Point Objective) and RTO (Recovery Time Objective) by tier
6. Plan staffing: DR coordinator, response team, roles and responsibilities
7. Develop testing strategy: quarterly tabletop, annual full recovery test
8. Create business case: investment, operating costs, benefit of avoiding downtime

**Expected Outcome:**
Board-approved DR strategy with recovery targets and investment case

**Assessment Checklist:**
[ ] BIA completed for all systems
[ ] Systems classified by criticality
[ ] DR strategies evaluated
[ ] Architecture designed
[ ] RPO/RTO defined by tier
[ ] Roles assigned
[ ] Testing plan created
[ ] Investment approved

### Implement computer network disaster recovery management plan

**Objective:** Execute implement computer network disaster recovery management plan following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for implement computer network disaster recovery management plan
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

### Produce disaster recovery management report

**Objective:** Execute produce disaster recovery management report following management and governance standards

**Duration:** 120 minutes

**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation

**Procedures:**
1. Review business objectives and requirements
2. Conduct stakeholder consultation and impact analysis
3. Develop strategy or plan for produce disaster recovery management report
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
- **Mapping:** Present disaster recovery plans and risk assessments to senior management and board; prepare post-drill and post-incident reports for compliance audiences; communicate recovery procedures, roles, and escalation paths to all stakeholders

### 2. Teamwork & Collaboration
- **Mapping:** Lead cross-functional disaster recovery teams including IT, facilities, and business units; collaborate with executive leadership on business impact analysis and recovery priorities; coordinate with external partners (cloud providers, DR site operators, insurers)

### 3. Problem-solving
- **Mapping:** Analyze disaster scenarios and develop recovery strategies for critical systems; evaluate trade-offs between RTO/RPO targets and available budget; resolve recovery failures identified during DR drills and actual incidents

### 4. Initiative & Self-reliance
- **Mapping:** Drive regular DR testing and plan updates without waiting for incidents; make time-critical decisions during disaster events to minimize data loss and downtime; take responsibility for organisational recovery readiness

### 5. Planning & Organizing
- **Mapping:** Develop and maintain disaster recovery management plans covering single-site and multi-site environments; organize DR drill schedules, backup verification, and failover testing; manage recovery site provisioning and resource allocation

### 6. Self-management & Safety Awareness
- **Mapping:** Ensure DR plans comply with regulatory and audit requirements; manage risk of extended downtime through tested and documented procedures; maintain business continuity governance frameworks aligned with organisational risk appetite

### 7. Technology Use & Technical Proficiency
- **Mapping:** Manage backup infrastructure, replication technologies, and failover systems; use DR orchestration and testing tools; oversee cloud-based and on-premises recovery environments

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Stay informed on DR technologies, cloud recovery options, and business continuity standards; analyze DR drill results and incident post-mortems to improve recovery plans; update procedures based on infrastructure changes and lessons learned



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
- ITIL 4 Availability and Continuity Management Processes
- ISO/IEC 22301:2019 – Business Continuity Management Systems Standard
- DR Planning Guide – Disaster Recovery Institute International (DRII) Standards
- AWS Disaster Recovery Strategies – RTO and RPO Objectives

**Technical References and Best Practices:**

- Microsoft Azure Site Recovery – Multi-Region Failover Configuration
- Backup and Recovery Best Practices – Veeam, Commvault, Veritas Documentation
- Business Continuity Planning and Crisis Communication Strategies
- Risk Assessment and Business Impact Analysis (BIA) Frameworks
- Malaysian Regulatory Requirements for Financial Institution Disaster Recovery Plans

**Contact hour:** [[00_Contact-hour_IT-020-5-L5-Management]]


---

↑ [README](../../README.md) · **IT-020-5** > CoCu 4 - Disaster Recovery Management

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-5-L5-Management.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Management-Overview.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Asset-Management.md) · [03_CoCu-3](03_CoCu-3-Computer-System-Security-Management.md) · [05_CoCu-5](05_CoCu-5-Computer-System-Network-Project-Management.md) · [06_CoCu-6](06_CoCu-6-SOP-Development-And-Implementation.md) · [07_CoCu-7](07_CoCu-7-Server-Scripting.md)

**Other levels:** [IT-020-3 (L3)](../IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md) · [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md)
