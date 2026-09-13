# CoCu 1: Computer Systems Planning and Operations Management (L5, 200 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) |
| LEVEL | L5 | L5 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 1: Computer Systems Planning and Operations Management (Perancangan Sistem Komputer dan Pengurusan Operasi) | CoCu 1: Computer Systems Planning and Operations Management (Perancangan Sistem Komputer dan Pengurusan Operasi) |
| NO. AND WORK ACTIVITY STATEMENT | PLAN RESOURCES · COORDINATE OPERATIONS · MONITOR PERFORMANCE · REPORT TO MANAGEMENT | PLAN RESOURCES · COORDINATE OPERATIONS · MONITOR PERFORMANCE · REPORT TO MANAGEMENT |
| NO. CODE | IT-020-5:2013 - CoCu 1 / P(1/7) | PAGE: 1 - 22 |


| SET-UP CONTEXT | SINGLE-DEPARTMENT / SMALL IT TEAM | ENTERPRISE / MULTI-DEPARTMENT IT OPERATIONS |
|----------------|-------------------------------------|----------------------------------------------|
| Resource planning | Small IT team (2-5 staff) managing a single department's computing resources. Capacity planning based on current headcount and known growth. Budget prepared as a simple annual CAPEX/OPEX request with limited vendor negotiation. Lifecycle planning covers desktop PCs, printers, and a single file server. | Enterprise IT division managing computing resources across multiple departments, branches, or subsidiaries. Capacity planning uses demand forecasting models aligned to business strategy. Budget involves multi-year CAPEX/OPEX planning, competitive vendor evaluation, and board-level approval. Lifecycle planning covers data centres, cloud subscriptions, end-user devices, and enterprise applications. |
| Operations coordination | Operations coordinated informally through email and shared calendars. Change requests handled ad hoc with minimal documentation. Vendor interaction limited to break-fix support contracts. Escalation paths are informal and person-dependent. | Operations coordinated through an ITSM platform with formal change management, incident management, and service request workflows. Multiple vendors managed through SLAs with defined response and resolution times. Escalation matrix documented and communicated to all stakeholders. Maintenance windows scheduled and approved through change advisory board (CAB). |
| Reporting | Monthly status report covering system uptime, open incidents, and budget spend. Reports prepared in spreadsheet or presentation format for department head. Limited use of dashboards or automated reporting. | Comprehensive management reporting suite including executive dashboard, KPI scorecards, financial variance reports, risk register updates, and SLA compliance summaries. Reports presented to IT steering committee and C-level management. Automated reporting from ITSM and monitoring tools with drill-down capability. |


| Type / Framework | Description |
|------------------|-------------|
| ITIL service management | The Information Technology Infrastructure Library provides a comprehensive framework for managing IT services across their lifecycle: service strategy, service design, service transition, service operation, and continual service improvement. ITIL aligns IT operations with business objectives by defining processes such as incident management, problem management, and change management. Adoption of ITIL enables consistent service delivery, measurable performance, and structured escalation. Organisations typically implement ITIL processes incrementally, starting with incident and change management. |
| Capacity planning and demand management | The process of forecasting future computing resource requirements (hardware, software, network bandwidth, storage, and staffing) based on business growth projections, usage trends, and technology refresh cycles. Capacity planning ensures that infrastructure can meet service level targets without over-provisioning or under-provisioning. Methods include trend analysis, workload characterisation, and modelling tools. Results feed directly into budget planning and procurement decisions. |
| CAPEX/OPEX budgeting | Capital expenditure (CAPEX) covers acquisition of new hardware, infrastructure, and major software licences, while operational expenditure (OPEX) covers recurring costs such as cloud subscriptions, maintenance contracts, utilities, and staffing. IT managers must prepare and justify budgets that balance investment in new capability with ongoing operational costs. Budget proposals require cost-benefit analysis, return on investment (ROI) estimation, and alignment with organisational financial policy. Variance tracking (budget vs actual) is reported to management periodically. |
| SLA management | Service Level Agreements define measurable targets for IT service delivery, including availability (e.g. 99.5% uptime), response time, resolution time, and throughput. SLAs are agreed between IT and business units (internal) or between the organisation and external service providers (external). Performance against SLAs is monitored continuously and reported in management dashboards. Breaches trigger escalation, root cause analysis, and corrective action. |
| IT governance (COBIT) | Control Objectives for Information and Related Technologies (COBIT) is a governance framework that ensures IT investments deliver value, risks are managed, and resources are optimised. COBIT defines governance and management objectives across five domains: Evaluate, Direct and Monitor (EDM); Align, Plan and Organise (APO); Build, Acquire and Implement (BAI); Deliver, Service and Support (DSS); and Monitor, Evaluate and Assess (MEA). It provides maturity models and metrics for benchmarking IT management capability. Adoption supports compliance with regulatory and audit requirements. |
| Change management | A structured process for evaluating, approving, and implementing changes to IT systems and services to minimise disruption and risk. All changes are logged as change requests, classified by risk and impact, reviewed by a change advisory board (CAB), and scheduled within approved maintenance windows. Post-implementation reviews verify that changes achieved their objectives without adverse effects. Change management is a core ITIL process and a key control for IT governance and audit. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 25% | 50 | Plan resources (capacity, budget, lifecycle) | 15.0 | 35.0 | 50.0 |
| 25% | 50 | Coordinate operations (IT, users, vendors) | 15.0 | 35.0 | 50.0 |
| 25% | 50 | Monitor performance (KPIs, availability, incidents) | 15.0 | 35.0 | 50.0 |
| 25% | 50 | Report to management (status, costs, risks) | 15.0 | 35.0 | 50.0 |
| **100%** | **200** | | **60.0** | **140.0** | **200.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) | IT-020-5:2013 COMPUTER SYSTEMS MANAGEMENT (Pengurusan Sistem Komputer) |
| LEVEL | L5 | L5 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 1: Computer Systems Planning and Operations Management (Perancangan Sistem Komputer dan Pengurusan Operasi) | CoCu 1: Computer Systems Planning and Operations Management (Perancangan Sistem Komputer dan Pengurusan Operasi) |
| NO. AND WORK ACTIVITY STATEMENT | PLAN RESOURCES · COORDINATE OPERATIONS · MONITOR PERFORMANCE · REPORT TO MANAGEMENT | PLAN RESOURCES · COORDINATE OPERATIONS · MONITOR PERFORMANCE · REPORT TO MANAGEMENT |
| NO. CODE | IT-020-5:2013 - CoCu 1 / P(1/7) | PAGE: 23 - 40 |


| Management Framework / Tool | Description |
|------------------------------|-------------|
| Resource planning process | A systematic approach to identifying, quantifying, and scheduling the resources (staff, hardware, software, facilities) required to deliver IT services. Includes skills gap analysis, workforce planning, hardware refresh scheduling, and software licence management. Resource plans are aligned to the annual budget cycle and reviewed quarterly against actual utilisation and business demand changes. Outputs include resource allocation tables, procurement schedules, and staffing plans. |
| Operations coordination and scheduling | The practice of coordinating day-to-day IT activities across teams, departments, and external vendors to ensure seamless service delivery. Includes maintenance window scheduling, change implementation coordination, incident handover between shifts, and vendor service coordination. Tools such as shared calendars, ITSM workflow engines, and communication platforms are used to maintain visibility and accountability. Documented run books and standard operating procedures (SOPs) support consistent execution. |
| KPI monitoring and dashboards | Definition, collection, and visualisation of key performance indicators that measure IT service health and operational efficiency. Common KPIs include system availability (%), mean time to repair (MTTR), mean time between failures (MTBF), incident volume and resolution rate, change success rate, and customer satisfaction scores. Dashboards aggregate data from monitoring tools and ITSM platforms into real-time or periodic views for operational staff and management. Thresholds and alerts are configured to trigger proactive intervention before SLA breaches occur. |
| Management reporting | The preparation and presentation of structured reports that communicate IT performance, financial status, risks, and strategic recommendations to senior management and stakeholders. Report types include monthly operational summaries, quarterly business reviews, annual IT performance reports, and ad hoc incident or project reports. Reports must be accurate, timely, and tailored to the audience (technical detail for IT management, executive summary for board). Effective reporting supports evidence-based decision-making and demonstrates IT value to the business. |
| Vendor and stakeholder management | The process of managing relationships with external vendors (hardware suppliers, software vendors, ISPs, managed service providers) and internal stakeholders (business unit heads, finance, HR). Includes vendor selection and evaluation, contract negotiation, SLA monitoring, performance reviews, and escalation management. Stakeholder management involves understanding requirements, managing expectations, and maintaining regular communication. A vendor register and stakeholder matrix are maintained and updated as relationships evolve. |
| Continuous improvement (PDCA) | The Plan-Do-Check-Act cycle applied to IT operations to drive ongoing enhancement of processes, services, and outcomes. Plan identifies improvement opportunities from incident trends, audit findings, or stakeholder feedback. Do implements the improvement on a trial basis. Check measures results against expected outcomes. Act standardises successful improvements or revises the approach. PDCA is embedded in ITIL continual service improvement and supports organisational maturity growth. |


| Software / Tool Type | Description |
|----------------------|-------------|
| ITSM platforms (ServiceNow, BMC Helix) | Enterprise IT Service Management platforms that provide integrated modules for incident management, problem management, change management, service request fulfilment, and asset management. These tools enforce ITIL-aligned workflows, maintain audit trails, and generate compliance reports. Dashboards and analytics support management reporting and KPI tracking. Selection criteria include scalability, integration capability, and alignment with organisational ITIL maturity. |
| Monitoring tools (Nagios, Zabbix, PRTG) | Infrastructure monitoring solutions that track availability, performance, and health of servers, network devices, applications, and services. They collect metrics (CPU, memory, disk, bandwidth), generate alerts when thresholds are exceeded, and provide historical trend data for capacity planning. Open-source options (Nagios, Zabbix) offer flexibility, while commercial tools (PRTG, SolarWinds) provide ease of deployment and vendor support. Integration with ITSM platforms enables automatic incident creation from alerts. |
| Project and financial tracking tools | Software for planning, scheduling, and tracking IT projects and budgets. Project management tools (Microsoft Project, Jira, OpenProject) provide Gantt charts, task assignment, and progress tracking. Financial tracking may use enterprise ERP modules or dedicated tools for budget preparation, purchase order management, and variance reporting. Combined use ensures that project expenditure is tracked against approved budgets and reported to management. |
| Collaboration and communication platforms | Enterprise tools (Microsoft Teams, Slack, SharePoint) used for cross-team coordination, knowledge sharing, and stakeholder communication. These platforms support virtual meetings, document collaboration, and structured channels for incident escalation and change notifications. Integration with ITSM tools enables automated status updates and alerts within team communication flows. |


| Common Issue | Root Cause | Management Action |
|--------------|------------|-------------------|
| Resource shortfall during peak demand | Inadequate capacity planning; no demand forecasting; reactive rather than proactive resource allocation | Implement formal capacity planning process with quarterly reviews; use historical trends and business growth projections; maintain buffer capacity for peak periods |
| Vendor SLA breach | Poorly defined SLA metrics; no regular performance monitoring; weak contract terms; insufficient escalation process | Define clear and measurable SLA targets in contracts; monitor vendor performance monthly; establish escalation matrix with penalties for repeated breaches; conduct annual vendor reviews |
| Budget overrun on IT operations | Inaccurate cost estimation; unplanned expenditure on emergency repairs; scope creep in projects; insufficient tracking of actual vs budget | Prepare detailed bottom-up budget with contingency allocation; track expenditure monthly against budget baseline; require approval for unplanned spend; report variances to management with corrective action plan |
| Poor KPI tracking and reporting | No defined KPIs; data collected manually and inconsistently; monitoring tools not configured or underutilised; reports not standardised | Define KPI framework aligned to business objectives and SLAs; automate data collection through monitoring and ITSM tools; establish standard report templates and reporting schedule; train staff on dashboard usage |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Plan resources (capacity, budget, lifecycle) | Understand concepts related to: Plan resources (capacity, budget, lifecycle) | Successfully execute: Plan resources (capacity, budget, lifecycle) | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Coordinate operations (IT, users, vendors) | Understand concepts related to: Coordinate operations (IT, users, vendors) | Successfully execute: Coordinate operations (IT, users, vendors) | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Monitor performance (KPIs, availability, incidents) | Know monitoring tools and alert thresholds | Monitor systems and respond to alerts | Practical monitoring; response to simulated alerts | Monitoring logs; incident response records |
| Report to management (status, costs, risks) | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |

## Practical Exercises

The following management-level exercise scenarios develop the strategic and governance competencies required for Computer Systems Planning and Operations Management. Each exercise is designed for L5 managers and includes case studies, policy scenarios, governance frameworks, strategic planning simulations, and assessment criteria aligned with NOSS standards.

### Lab 1.1: Strategic IT Resource Planning and Capacity Forecasting

**Objective:** Develop a multi-year IT resource plan aligned to business strategy

**Duration:** 120 minutes

**Resources Required:**
- Resource planning template
- Business strategy document
- Capacity forecasting model
- Budget projection worksheet

**Procedures:**
1. Review 3-year business strategy and growth projections
2. Assess current IT resource utilisation and gaps
3. Forecast resource demand: staff, hardware, software, infrastructure, cloud services
4. Analyse skills gaps and workforce planning requirements
5. Create multi-year CAPEX and OPEX budget forecast
6. Design resource allocation aligned to business priorities
7. Identify risks (skills shortage, vendor lock-in) and mitigation plans
8. Present resource plan to executive leadership with ROI justification

**Expected Outcome:**
Approved multi-year IT resource plan with budget justification and strategic alignment

**Assessment Checklist:**
[ ] Business strategy clearly understood
[ ] Current state assessed and gaps identified
[ ] Demand forecasts created with documented assumptions
[ ] Skills and staffing requirements defined
[ ] Budget forecast aligned to business strategy
[ ] Resource allocation justified
[ ] Risk mitigation plan developed
[ ] Executive approval obtained

### Lab 1.2: Enterprise Operations Coordination and Change Management

**Objective:** Design and implement an ITSM change management process

**Duration:** 120 minutes

**Resources Required:**
- ITIL change management template
- CAB charter
- Change scheduling calendar
- Communication plan

**Procedures:**
1. Design change management workflow: request → assessment → CAB review → approval → implementation → verification
2. Define change categorisation: standard, normal, emergency
3. Create Change Advisory Board (CAB) charter with members and decision criteria
4. Develop change scheduling process to minimise business impact
5. Create communication templates for change notifications
6. Define rollback procedures for failed changes
7. Design impact assessment criteria for change risk evaluation
8. Document escalation procedures and stakeholder responsibilities

**Expected Outcome:**
Documented ITSM change management process aligned to ITIL standards

**Assessment Checklist:**
[ ] Workflow defined with clear approval gates
[ ] Change categories documented
[ ] CAB charter approved
[ ] Scheduling process documented
[ ] Communication templates created
[ ] Rollback procedures defined
[ ] Risk assessment criteria established
[ ] Escalation procedures documented

### Lab 1.3: KPI Framework and Performance Dashboarding

**Objective:** Design KPIs and dashboards for IT service management reporting

**Duration:** 90 minutes

**Resources Required:**
- KPI framework template
- SLA definitions
- Dashboard design tool
- Sample data

**Procedures:**
1. Define IT service KPIs: availability %, MTTR, incident resolution rate, change success rate, SLA compliance
2. Align KPIs to business objectives: revenue protection, cost efficiency, customer satisfaction
3. Define KPI measurement methods and data collection points
4. Create KPI targets and thresholds for alerts
5. Design dashboard views for operational staff, managers, and executives
6. Plan reporting frequency: real-time alerts, daily operational, weekly management, monthly executive
7. Define ownership: who owns each KPI, who approves targets
8. Plan data quality checks and validation procedures

**Expected Outcome:**
Approved KPI framework with dashboard design and reporting schedule

**Assessment Checklist:**
[ ] KPIs defined and documented
[ ] Alignment to business objectives verified
[ ] Measurement methods established
[ ] Targets and thresholds set
[ ] Dashboard layouts designed
[ ] Reporting schedule defined
[ ] Ownership assigned
[ ] Data quality process documented

### Lab 1.4: Executive-Level IT Performance Reporting

**Objective:** Create executive-ready IT performance and risk reports

**Duration:** 90 minutes

**Resources Required:**
- Executive reporting template
- SLA compliance data
- Risk register
- Financial summary

**Procedures:**
1. Gather data from operational systems: KPIs, SLA compliance, incidents, changes
2. Create executive summary highlighting key metrics and exceptions
3. Prepare trend analysis: month-over-month, year-over-year performance
4. Summarise risk register: top risks, mitigation status, new risks identified
5. Prepare financial summary: budget vs actual spend, variance explanations
6. Include recommendations: process improvements, investment requests, strategic changes
7. Design report layout for clarity and executive audience (avoid technical jargon)
8. Present report to IT steering committee and C-suite

**Expected Outcome:**
Executive-ready IT performance report with insights and recommendations

**Assessment Checklist:**
[ ] Data sources identified and validated
[ ] Executive summary clear and concise
[ ] Trend analysis completed
[ ] Risk summary included
[ ] Financial summary accurate
[ ] Recommendations supported by data
[ ] Report format appropriate for audience
[ ] Presentation delivery clear and engaging



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Mapping:** Present strategic recommendations to senior management; prepare reports for board and compliance audiences; communicate vision and strategy

### 2. Teamwork & Collaboration
- **Mapping:** Lead multi-disciplinary teams; collaborate with executive leadership; coordinate across organizational boundaries

### 3. Problem-solving
- **Mapping:** Address strategic challenges; evaluate complex trade-offs; develop enterprise-wide solutions

### 4. Initiative & Self-reliance
- **Mapping:** Drive strategic initiatives; make high-impact decisions; take responsibility for organizational outcomes

### 5. Planning & Organizing
- **Mapping:** Develop strategic plans; align with business objectives; manage portfolio of initiatives

### 6. Self-management & Safety Awareness
- **Mapping:** Manage organizational risk and governance; ensure regulatory compliance; maintain security and business continuity

### 7. Technology Use & Technical Proficiency
- **Mapping:** Use strategic planning and analysis tools; manage enterprise systems and infrastructure; leverage data for decision-making

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Drive continuous improvement culture; stay informed on emerging technologies; foster innovation and learning



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
- ITIL 4 Foundation – IT Service Management Framework and Core Processes
- ISO/IEC 20000-1:2018 – IT Service Management Systems Certification Standard
- COBIT 2019 – Governance and Management of Enterprise IT Framework
- ISO/IEC 27001:2022 – Information Security Management Systems

**Technical References and Best Practices:**

- NIST Cybersecurity Framework – Governance and Risk Management
- Project Management Institute (PMI) PMBOK – IT Project Governance
- Enterprise Architecture Framework – TOGAF Standard (The Open Group)
- Balanced Scorecard for IT Performance Management and Strategic Alignment
- Malaysian Financial Services Regulatory Authority (BNM) – Technology Risk Management

**Contact hour:** [[00_Contact-hour_IT-020-5-L5-Management]]


---

↑ [README](../../README.md) · **IT-020-5** > CoCu 1 - Management Overview

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-5-L5-Management.md) · [00_standard-practice](00_standard-practice.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Asset-Management.md) · [03_CoCu-3](03_CoCu-3-Computer-System-Security-Management.md) · [04_CoCu-4](04_CoCu-4-Disaster-Recovery-Management.md) · [05_CoCu-5](05_CoCu-5-Computer-System-Network-Project-Management.md) · [06_CoCu-6](06_CoCu-6-SOP-Development-And-Implementation.md) · [07_CoCu-7](07_CoCu-7-Server-Scripting.md)

**Other levels:** [IT-020-3 (L3)](../IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md) · [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md)
