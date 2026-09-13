#!/usr/bin/env python3
"""
Add Practical Exercises sections to all Level 5 CoCu files for US-015.

This script automates the insertion of management-level exercise scenarios
aligned with each L5 CoCu's work activities. Exercises include case studies,
strategic planning, governance, policy development, and risk management
scenarios following NOSS standards for L5 management-level competencies.
"""

import os
import re
from pathlib import Path


def extract_work_activities(content: str) -> list[str]:
    """Extract work activities from the contact hour distribution table."""
    lines = content.split('\n')
    activities = []

    for line in lines:
        # Match table rows with percentage, hours, and activity name
        # Format: | 10% | 30 | Activity Name | ...
        match = re.match(r'\|\s*\d+%\s*\|\s*\d+\s*\|\s*([^|]+)\s*\|', line)
        if match:
            activity = match.group(1).strip()
            # Skip the total row
            if activity and not activity.startswith('**'):
                activities.append(activity)

    return activities


def generate_practical_exercises(cocu_num: int, cocu_title: str, activities: list[str]) -> str:
    """Generate practical exercises section for an L5 CoCu."""
    exercises = "## Practical Exercises\n\n"
    exercises += f"The following management-level exercise scenarios develop the strategic and governance competencies required for {cocu_title}. "
    exercises += "Each exercise is designed for L5 managers and includes case studies, policy scenarios, governance frameworks, "
    exercises += "strategic planning simulations, and assessment criteria aligned with NOSS standards.\n\n"

    # Define exercise templates based on CoCu
    exercise_templates = {
        1: {  # CoCu 1: Management Overview
            "Plan resources": {
                "title": "Lab 1.1: Strategic IT Resource Planning and Capacity Forecasting",
                "objective": "Develop a multi-year IT resource plan aligned to business strategy",
                "duration": "120 minutes",
                "equipment": ["Resource planning template", "Business strategy document", "Capacity forecasting model", "Budget projection worksheet"],
                "procedures": [
                    "Review 3-year business strategy and growth projections",
                    "Assess current IT resource utilisation and gaps",
                    "Forecast resource demand: staff, hardware, software, infrastructure, cloud services",
                    "Analyse skills gaps and workforce planning requirements",
                    "Create multi-year CAPEX and OPEX budget forecast",
                    "Design resource allocation aligned to business priorities",
                    "Identify risks (skills shortage, vendor lock-in) and mitigation plans",
                    "Present resource plan to executive leadership with ROI justification"
                ],
                "expected_outcome": "Approved multi-year IT resource plan with budget justification and strategic alignment",
                "checklist": [
                    "[ ] Business strategy clearly understood",
                    "[ ] Current state assessed and gaps identified",
                    "[ ] Demand forecasts created with documented assumptions",
                    "[ ] Skills and staffing requirements defined",
                    "[ ] Budget forecast aligned to business strategy",
                    "[ ] Resource allocation justified",
                    "[ ] Risk mitigation plan developed",
                    "[ ] Executive approval obtained"
                ]
            },
            "Coordinate operations": {
                "title": "Lab 1.2: Enterprise Operations Coordination and Change Management",
                "objective": "Design and implement an ITSM change management process",
                "duration": "120 minutes",
                "equipment": ["ITIL change management template", "CAB charter", "Change scheduling calendar", "Communication plan"],
                "procedures": [
                    "Design change management workflow: request → assessment → CAB review → approval → implementation → verification",
                    "Define change categorisation: standard, normal, emergency",
                    "Create Change Advisory Board (CAB) charter with members and decision criteria",
                    "Develop change scheduling process to minimise business impact",
                    "Create communication templates for change notifications",
                    "Define rollback procedures for failed changes",
                    "Design impact assessment criteria for change risk evaluation",
                    "Document escalation procedures and stakeholder responsibilities"
                ],
                "expected_outcome": "Documented ITSM change management process aligned to ITIL standards",
                "checklist": [
                    "[ ] Workflow defined with clear approval gates",
                    "[ ] Change categories documented",
                    "[ ] CAB charter approved",
                    "[ ] Scheduling process documented",
                    "[ ] Communication templates created",
                    "[ ] Rollback procedures defined",
                    "[ ] Risk assessment criteria established",
                    "[ ] Escalation procedures documented"
                ]
            },
            "Monitor performance": {
                "title": "Lab 1.3: KPI Framework and Performance Dashboarding",
                "objective": "Design KPIs and dashboards for IT service management reporting",
                "duration": "90 minutes",
                "equipment": ["KPI framework template", "SLA definitions", "Dashboard design tool", "Sample data"],
                "procedures": [
                    "Define IT service KPIs: availability %, MTTR, incident resolution rate, change success rate, SLA compliance",
                    "Align KPIs to business objectives: revenue protection, cost efficiency, customer satisfaction",
                    "Define KPI measurement methods and data collection points",
                    "Create KPI targets and thresholds for alerts",
                    "Design dashboard views for operational staff, managers, and executives",
                    "Plan reporting frequency: real-time alerts, daily operational, weekly management, monthly executive",
                    "Define ownership: who owns each KPI, who approves targets",
                    "Plan data quality checks and validation procedures"
                ],
                "expected_outcome": "Approved KPI framework with dashboard design and reporting schedule",
                "checklist": [
                    "[ ] KPIs defined and documented",
                    "[ ] Alignment to business objectives verified",
                    "[ ] Measurement methods established",
                    "[ ] Targets and thresholds set",
                    "[ ] Dashboard layouts designed",
                    "[ ] Reporting schedule defined",
                    "[ ] Ownership assigned",
                    "[ ] Data quality process documented"
                ]
            },
            "Report to management": {
                "title": "Lab 1.4: Executive-Level IT Performance Reporting",
                "objective": "Create executive-ready IT performance and risk reports",
                "duration": "90 minutes",
                "equipment": ["Executive reporting template", "SLA compliance data", "Risk register", "Financial summary"],
                "procedures": [
                    "Gather data from operational systems: KPIs, SLA compliance, incidents, changes",
                    "Create executive summary highlighting key metrics and exceptions",
                    "Prepare trend analysis: month-over-month, year-over-year performance",
                    "Summarise risk register: top risks, mitigation status, new risks identified",
                    "Prepare financial summary: budget vs actual spend, variance explanations",
                    "Include recommendations: process improvements, investment requests, strategic changes",
                    "Design report layout for clarity and executive audience (avoid technical jargon)",
                    "Present report to IT steering committee and C-suite"
                ],
                "expected_outcome": "Executive-ready IT performance report with insights and recommendations",
                "checklist": [
                    "[ ] Data sources identified and validated",
                    "[ ] Executive summary clear and concise",
                    "[ ] Trend analysis completed",
                    "[ ] Risk summary included",
                    "[ ] Financial summary accurate",
                    "[ ] Recommendations supported by data",
                    "[ ] Report format appropriate for audience",
                    "[ ] Presentation delivery clear and engaging"
                ]
            }
        },
        2: {  # CoCu 2: Asset Management
            "Analyse computer system asset inventory": {
                "title": "Lab 2.1: IT Asset Inventory Analysis and Audit Planning",
                "objective": "Conduct comprehensive analysis of IT asset inventory and plan audit",
                "duration": "120 minutes",
                "equipment": ["Asset inventory report", "ITAM system access", "Audit checklist", "Analysis template"],
                "procedures": [
                    "Export current ITAM system inventory across all locations",
                    "Analyse inventory completeness: compare ITAM records to purchase orders, HR records, network discovery",
                    "Identify discrepancies: ghost assets, missing tags, incorrect locations",
                    "Classify assets by type, criticality, age, and condition",
                    "Calculate inventory accuracy percentage (matching vs total)",
                    "Identify high-risk assets: end-of-life, unsupported versions, security vulnerabilities",
                    "Create remediation plan for discrepancies and high-risk assets",
                    "Present audit findings and remediation roadmap to management"
                ],
                "expected_outcome": "Comprehensive asset inventory audit report with remediation plan",
                "checklist": [
                    "[ ] Inventory exported and validated",
                    "[ ] Data sources cross-checked",
                    "[ ] Discrepancies identified and categorised",
                    "[ ] Asset classification completed",
                    "[ ] Inventory accuracy calculated",
                    "[ ] High-risk assets flagged",
                    "[ ] Remediation plan created with timeline",
                    "[ ] Management sign-off obtained"
                ]
            },
            "Define operational status of assets": {
                "title": "Lab 2.2: Asset Lifecycle Status Management and Workflow",
                "objective": "Design and implement asset status tracking and workflow",
                "duration": "90 minutes",
                "equipment": ["Asset status framework", "Workflow diagram tool", "Approval matrix", "Configuration management tool"],
                "procedures": [
                    "Define asset status categories: planning, procurement, deployment, in service, maintenance, pending disposal, disposed",
                    "Create workflow diagram showing status transitions and required approvals",
                    "Define responsibilities: who updates status, who approves transitions",
                    "Create business rules: conditions triggering status changes, approval requirements",
                    "Design notifications: who gets notified when status changes",
                    "Plan audit procedures: periodic status reconciliation, data quality checks",
                    "Configure status fields in ITAM system with workflow automation",
                    "Train administrators on status update procedures and approvals"
                ],
                "expected_outcome": "Documented asset status workflow integrated into ITAM system",
                "checklist": [
                    "[ ] Status categories defined",
                    "[ ] Workflow diagram created",
                    "[ ] Approval rules documented",
                    "[ ] Responsibilities assigned",
                    "[ ] Notifications configured",
                    "[ ] Audit procedures established",
                    "[ ] System configuration completed",
                    "[ ] Training delivered"
                ]
            },
            "Estimate costs and space requirements": {
                "title": "Lab 2.3: TCO Analysis and Capacity Planning",
                "objective": "Develop total cost of ownership model and space forecasting",
                "duration": "120 minutes",
                "equipment": ["TCO template", "Capacity calculator", "Historical cost data", "Vendor pricing"],
                "procedures": [
                    "Define TCO model components: acquisition, deployment, operation, maintenance, support, energy, disposal",
                    "Collect historical cost data for each asset type",
                    "Create TCO calculator for hardware refresh decisions (lease vs buy)",
                    "Analyse space requirements: current utilisation, growth forecast, cooling/power capacity",
                    "Forecast 3-year space and infrastructure needs",
                    "Evaluate alternative solutions: on-premise vs cloud, internal vs outsourced",
                    "Create cost-benefit comparison models for decision support",
                    "Present TCO and space analysis to finance and operations leadership"
                ],
                "expected_outcome": "TCO model and space forecast supporting strategic planning",
                "checklist": [
                    "[ ] TCO model components defined",
                    "[ ] Historical data collected and analyzed",
                    "[ ] TCO calculator functional",
                    "[ ] Space requirements forecasted",
                    "[ ] Growth projections documented",
                    "[ ] Alternative solutions evaluated",
                    "[ ] Cost-benefit models created",
                    "[ ] Analysis presented to decision-makers"
                ]
            },
            "Determine asset management systems": {
                "title": "Lab 2.4: ITAM System Selection and Implementation Planning",
                "objective": "Evaluate and select ITAM platform; plan implementation",
                "duration": "120 minutes",
                "equipment": ["ITAM vendor comparison matrix", "Requirements document", "Implementation roadmap", "Business case template"],
                "procedures": [
                    "Document business requirements: asset types, discovery capabilities, integration needs, reporting",
                    "Create evaluation criteria scorecard: functionality, scalability, cost, vendor support, roadmap",
                    "Research ITAM platforms: ServiceNow, Lansweeper, Snipe-IT, others",
                    "Create vendor comparison matrix with weighted scoring",
                    "Develop RFP (Request for Proposal) for finalists",
                    "Conduct demonstrations and reference customer interviews",
                    "Create business case: implementation costs, ongoing costs, benefits (cost savings, efficiency, compliance)",
                    "Plan phased implementation: data migration, user training, process alignment"
                ],
                "expected_outcome": "ITAM vendor selection and implementation roadmap",
                "checklist": [
                    "[ ] Requirements documented",
                    "[ ] Evaluation criteria defined",
                    "[ ] Vendor research completed",
                    "[ ] Comparison matrix created",
                    "[ ] RFP issued",
                    "[ ] Demonstrations conducted",
                    "[ ] Business case approved",
                    "[ ] Implementation timeline finalized"
                ]
            },
            "Monitor asset tagging and labelling": {
                "title": "Lab 2.5: Asset Identification Strategy and Audit Program",
                "objective": "Design asset tagging/labelling standards and audit procedures",
                "duration": "90 minutes",
                "equipment": ["Tagging standards document", "Barcode/RFID options", "Audit checklist", "Tag printer and samples"],
                "procedures": [
                    "Review existing tagging standards and identify improvements",
                    "Compare barcode vs RFID: cost, durability, scanning speed, environmental factors",
                    "Design tag format: unique ID, asset type, location, QR code",
                    "Define tag placement standards for different asset types",
                    "Create tag replacement criteria: faded, damaged, illegible",
                    "Plan tagging campaign: scheduling, resource allocation, training",
                    "Design audit procedures: periodic verification, completeness checks, exception reporting",
                    "Configure automated alerting for missing or non-compliant tags"
                ],
                "expected_outcome": "Asset tagging standards and automated audit program",
                "checklist": [
                    "[ ] Tagging technology evaluated",
                    "[ ] Tag format standardized",
                    "[ ] Placement rules documented",
                    "[ ] Replacement criteria established",
                    "[ ] Tagging campaign planned",
                    "[ ] Audit procedures designed",
                    "[ ] Automation configured",
                    "[ ] Training prepared"
                ]
            },
            "Execute asset disposal": {
                "title": "Lab 2.6: Secure Asset Disposal and Compliance",
                "objective": "Develop compliant asset disposal process aligned to NIST SP 800-88",
                "duration": "120 minutes",
                "equipment": ["NIST SP 800-88 reference", "Disposal policy template", "Data destruction vendor list", "Certificate template"],
                "procedures": [
                    "Review regulatory requirements: PDPA, e-waste disposal, environmental standards",
                    "Design disposal workflow: identification, data sanitisation, certification, logistics",
                    "Define data destruction methods: Clear (overwrite), Purge (degaussing), Destroy (physical shredding)",
                    "Evaluate data destruction vendors: capabilities, certifications, costs, turnaround",
                    "Create disposal policy: approval requirements, vendor selection, documentation",
                    "Design asset decommissioning checklist: data backup, asset wiping, tag removal, condition assessment",
                    "Create certificate of destruction template for audit trail",
                    "Plan secure logistics: transportation, storage, tracking of disposed assets"
                ],
                "expected_outcome": "NIST-aligned asset disposal process with vendor contracts and documentation",
                "checklist": [
                    "[ ] Regulatory requirements identified",
                    "[ ] Disposal workflow documented",
                    "[ ] Data destruction methods evaluated",
                    "[ ] Vendors selected and contracted",
                    "[ ] Disposal policy approved",
                    "[ ] Decommissioning checklist created",
                    "[ ] Certificate template prepared",
                    "[ ] Logistics plan finalized"
                ]
            },
            "Prepare asset management reports": {
                "title": "Lab 2.7: Asset Management Reporting and Analytics",
                "objective": "Create asset management dashboards and reports for management",
                "duration": "90 minutes",
                "equipment": ["Reporting tool (Power BI, Excel)", "ITAM system data export", "Report template", "KPI definitions"],
                "procedures": [
                    "Define asset management KPIs: inventory accuracy, lifecycle status, TCO per asset type, disposal compliance",
                    "Create automated report queries from ITAM system",
                    "Design operational dashboard: inventory completeness, high-risk assets, aging equipment",
                    "Design management dashboard: asset costs, lifecycle status distribution, disposal pipeline",
                    "Create executive summary report: key metrics, trends, compliance status, recommendations",
                    "Plan report distribution: weekly/monthly automated emails to stakeholders",
                    "Create drill-down capability: executives can explore detail behind summary metrics",
                    "Test reporting pipeline and validate accuracy against source data"
                ],
                "expected_outcome": "Automated asset management reporting suite with dashboards and trending",
                "checklist": [
                    "[ ] KPIs defined and validated",
                    "[ ] Data extraction queries created",
                    "[ ] Operational dashboard designed",
                    "[ ] Management dashboard designed",
                    "[ ] Executive report template created",
                    "[ ] Automation configured",
                    "[ ] Drill-down capability tested",
                    "[ ] Accuracy verified"
                ]
            }
        },
        3: {  # CoCu 3: Security Management
            "Develop information security strategy": {
                "title": "Lab 3.1: Enterprise Information Security Strategy",
                "objective": "Develop comprehensive information security strategy aligned to business",
                "duration": "120 minutes",
                "equipment": ["Security strategy template", "Risk assessment framework", "Compliance requirements matrix", "Business objectives"],
                "procedures": [
                    "Review business objectives and risk tolerance",
                    "Conduct enterprise-wide risk assessment: threats, vulnerabilities, impact",
                    "Map compliance requirements: PDPA, industry standards, customer contracts",
                    "Define security pillars: confidentiality, integrity, availability, accountability",
                    "Create multi-year security roadmap aligned to business priorities",
                    "Design governance structure: CISO role, security steering committee, incident response team",
                    "Develop security policies framework: acceptable use, data classification, incident response",
                    "Estimate budget for security initiatives and ROI"
                ],
                "expected_outcome": "Board-approved information security strategy with 3-year roadmap",
                "checklist": [
                    "[ ] Business objectives understood",
                    "[ ] Risk assessment completed",
                    "[ ] Compliance requirements mapped",
                    "[ ] Security pillars defined",
                    "[ ] Roadmap created with milestones",
                    "[ ] Governance structure designed",
                    "[ ] Policies framework planned",
                    "[ ] Budget approved"
                ]
            },
            "Design access control framework": {
                "title": "Lab 3.2: Identity and Access Management (IAM) Architecture",
                "objective": "Design enterprise-wide IAM framework with zero-trust principles",
                "duration": "120 minutes",
                "equipment": ["IAM architecture template", "AD design worksheet", "MFA options analysis", "Zero-trust model"],
                "procedures": [
                    "Map organizational structure and access requirements",
                    "Design Active Directory hierarchy: forests, domains, OUs, trust relationships",
                    "Plan role-based access control (RBAC): job roles, permission groups, separation of duties",
                    "Design privileged access management (PAM): privileged accounts, monitoring, approval workflows",
                    "Evaluate MFA solutions: FIDO2, Windows Hello, authenticator apps, smart cards",
                    "Design zero-trust architecture: deny by default, verify every access request, microsegmentation",
                    "Plan identity federation for cloud and third-party access",
                    "Create access review procedures: periodic certification, entitlement audits"
                ],
                "expected_outcome": "Enterprise IAM architecture supporting zero-trust security model",
                "checklist": [
                    "[ ] Organizational structure mapped",
                    "[ ] Access requirements gathered",
                    "[ ] AD design approved",
                    "[ ] RBAC schema designed",
                    "[ ] PAM framework documented",
                    "[ ] MFA solution selected",
                    "[ ] Zero-trust principles applied",
                    "[ ] Review procedures established"
                ]
            },
            "Establish security monitoring and incident response": {
                "title": "Lab 3.3: Security Operations Center (SOC) Design",
                "objective": "Design SOC and incident response program",
                "duration": "120 minutes",
                "equipment": ["SIEM tool selection matrix", "IRP template", "Staffing model", "Tools evaluation"],
                "procedures": [
                    "Define SOC mission: threat detection, incident response, threat intelligence, forensics",
                    "Evaluate SIEM platforms: Splunk, IBM QRadar, Microsoft Sentinel, Wazuh",
                    "Design threat detection use cases and alert tuning strategy",
                    "Create incident response plan: detection, analysis, containment, eradication, recovery, post-incident review",
                    "Define incident severity levels and escalation procedures",
                    "Plan SOC staffing: 24/7 coverage, skills mix, training requirements",
                    "Design forensics capabilities for incident investigation and legal proceedings",
                    "Create threat intelligence and adversary tracking program"
                ],
                "expected_outcome": "SOC architecture and incident response program",
                "checklist": [
                    "[ ] SOC mission and scope defined",
                    "[ ] SIEM tool selected",
                    "[ ] Detection use cases designed",
                    "[ ] IRP documented and approved",
                    "[ ] Severity levels defined",
                    "[ ] Staffing plan created",
                    "[ ] Forensics capabilities planned",
                    "[ ] Threat intelligence program launched"
                ]
            },
            "Manage compliance and auditing": {
                "title": "Lab 3.4: Security Compliance and Audit Program",
                "objective": "Develop compliance management and internal audit program",
                "duration": "90 minutes",
                "equipment": ["Compliance matrix", "Audit framework", "Policy templates", "Evidence collection procedures"],
                "procedures": [
                    "Map applicable regulations: PDPA, ISO 27001, industry standards, contractual requirements",
                    "Create compliance matrix: requirements, responsible party, evidence type, review frequency",
                    "Design security policies: information classification, acceptable use, password management, incident reporting",
                    "Plan evidence collection: audit logs, configuration baselines, policy acknowledgement records",
                    "Create annual audit plan: scope, objectives, testing procedures, reporting",
                    "Design audit workflow: planning, fieldwork, findings, remediation tracking, reporting to board",
                    "Establish remediation tracking: issue logging, root cause analysis, action plans, closure verification",
                    "Plan external audit preparation and response"
                ],
                "expected_outcome": "Compliance mapping and audit program supporting regulatory requirements",
                "checklist": [
                    "[ ] Regulations identified",
                    "[ ] Compliance matrix created",
                    "[ ] Policies documented",
                    "[ ] Evidence procedures established",
                    "[ ] Annual audit plan approved",
                    "[ ] Audit workflow defined",
                    "[ ] Remediation process established",
                    "[ ] External audit ready"
                ]
            }
        },
        4: {  # CoCu 4: Disaster Recovery Management
            "Develop disaster recovery strategy": {
                "title": "Lab 4.1: Enterprise Disaster Recovery Strategy",
                "objective": "Develop DR strategy aligned to business continuity objectives",
                "duration": "120 minutes",
                "equipment": ["DR strategy template", "BIA framework", "Recovery metrics", "Business case"],
                "procedures": [
                    "Conduct Business Impact Analysis (BIA): identify critical systems, RPO/RTO requirements, dependencies",
                    "Classify applications by criticality: Tier 1 (minutes RPO/RTO), Tier 2 (hours), Tier 3 (days)",
                    "Evaluate DR strategies: backup and restore, standby site, active-active replication, cloud DR",
                    "Design DR architecture: on-site backups, off-site copies, geographically distributed sites",
                    "Define RPO (Recovery Point Objective) and RTO (Recovery Time Objective) by tier",
                    "Plan staffing: DR coordinator, response team, roles and responsibilities",
                    "Develop testing strategy: quarterly tabletop, annual full recovery test",
                    "Create business case: investment, operating costs, benefit of avoiding downtime"
                ],
                "expected_outcome": "Board-approved DR strategy with recovery targets and investment case",
                "checklist": [
                    "[ ] BIA completed for all systems",
                    "[ ] Systems classified by criticality",
                    "[ ] DR strategies evaluated",
                    "[ ] Architecture designed",
                    "[ ] RPO/RTO defined by tier",
                    "[ ] Roles assigned",
                    "[ ] Testing plan created",
                    "[ ] Investment approved"
                ]
            },
            "Design backup and recovery architecture": {
                "title": "Lab 4.2: Backup, Recovery, and Replication Architecture",
                "objective": "Design enterprise backup and recovery solution",
                "duration": "120 minutes",
                "equipment": ["Backup architecture template", "Recovery site options", "Tool evaluation matrix", "Capacity plan"],
                "procedures": [
                    "Assess current backup capabilities: coverage, retention, testing frequency",
                    "Design backup topology: source, local copies, off-site copies, media rotation",
                    "Evaluate backup tools: NetBackup, Commvault, Veeam, Bacula",
                    "Plan recovery site: hot standby (real-time), warm standby (periodic sync), cold (restore from backups)",
                    "Design replication for critical systems: synchronous (zero RPO), asynchronous",
                    "Create retention policy: daily, weekly, monthly, annual archives",
                    "Plan testing: annual recovery drills, specific system recoveries, whole system failover",
                    "Document recovery procedures: step-by-step runbooks for different failure scenarios"
                ],
                "expected_outcome": "Enterprise backup architecture supporting defined RPO/RTO",
                "checklist": [
                    "[ ] Current capabilities assessed",
                    "[ ] Backup topology designed",
                    "[ ] Tools selected",
                    "[ ] Recovery site defined",
                    "[ ] Replication strategy planned",
                    "[ ] Retention policy established",
                    "[ ] Testing procedures documented",
                    "[ ] Recovery runbooks created"
                ]
            },
            "Develop disaster recovery plans": {
                "title": "Lab 4.3: Disaster Recovery Plan (DRP) Development",
                "objective": "Create comprehensive DRP with procedures and contact lists",
                "duration": "120 minutes",
                "equipment": ["DRP template", "Contact lists", "Recovery procedures", "Communication plan"],
                "procedures": [
                    "Define disaster scenarios: data centre failure, ransomware, regional outage, supply chain disruption",
                    "Create communication plan: notification hierarchy, stakeholder groups, escalation procedures",
                    "Develop recovery procedures: data recovery, system restart, network reconnection, application startup",
                    "Create contact list: disaster recovery team, external vendors, internal executives, customers",
                    "Design command centre setup: location, equipment, communication infrastructure",
                    "Document decision triggers: when to invoke DR, who makes decisions, escalation criteria",
                    "Create periodic review procedures: quarterly updates, annual testing, lessons learned capture",
                    "Plan training and awareness: annual briefings, role-specific training, drill participation"
                ],
                "expected_outcome": "Comprehensive DRP with procedures and contact information",
                "checklist": [
                    "[ ] Scenarios identified",
                    "[ ] Communication plan documented",
                    "[ ] Recovery procedures detailed",
                    "[ ] Contact list current",
                    "[ ] Command centre configured",
                    "[ ] Decision triggers defined",
                    "[ ] Review schedule established",
                    "[ ] Training plan created"
                ]
            },
            "Test and maintain disaster recovery capability": {
                "title": "Lab 4.4: DR Testing and Continuous Improvement",
                "objective": "Execute and evaluate DR testing program",
                "duration": "120 minutes",
                "equipment": ["Test plan template", "Lab environment", "Monitoring tools", "Results tracking"],
                "procedures": [
                    "Conduct tabletop exercise: walk-through of procedures, identify gaps, role clarity",
                    "Perform targeted recovery tests: single system, specific application, database recovery",
                    "Execute full DR test: invoke recovery site, recover all critical systems, validate functionality",
                    "Monitor test: measure actual RTO/RPO, track issues, measure recovery success rate",
                    "Document results: what worked, what failed, lessons learned",
                    "Identify gaps: missing procedures, outdated contact info, capacity shortfalls",
                    "Create action plan: fix critical gaps, schedule next test, update DRP",
                    "Present test results to leadership with improvement recommendations"
                ],
                "expected_outcome": "Validated DR capability with test results and improvement plan",
                "checklist": [
                    "[ ] Tabletop exercise completed",
                    "[ ] Targeted tests executed",
                    "[ ] Full test performed successfully",
                    "[ ] Metrics collected",
                    "[ ] Results documented",
                    "[ ] Gaps identified",
                    "[ ] Action plan created",
                    "[ ] DRP updated"
                ]
            }
        },
        5: {  # CoCu 5: Network Project Management
            "Plan network projects": {
                "title": "Lab 5.1: Enterprise Network Project Planning",
                "objective": "Develop comprehensive network project plan",
                "duration": "120 minutes",
                "equipment": ["Project plan template", "Gantt chart tool", "Stakeholder analysis", "Risk register"],
                "procedures": [
                    "Define project scope: network redesign, technology refresh, expansion, consolidation",
                    "Identify stakeholders: business users, IT operations, executives, vendors, external partners",
                    "Create detailed schedule: design, procurement, testing, deployment, cutover phases",
                    "Plan resource allocation: internal staff, external consultants, vendor support",
                    "Identify dependencies: procurement lead times, testing sequencing, third-party coordination",
                    "Conduct risk analysis: technical risks, vendor risks, schedule risks, budget risks",
                    "Create mitigation plans for identified risks",
                    "Develop communication plan and stakeholder management strategy"
                ],
                "expected_outcome": "Comprehensive network project plan with stakeholder engagement strategy",
                "checklist": [
                    "[ ] Scope clearly defined",
                    "[ ] Stakeholders identified",
                    "[ ] Schedule detailed with milestones",
                    "[ ] Resources allocated",
                    "[ ] Dependencies identified",
                    "[ ] Risks analyzed",
                    "[ ] Mitigation plans developed",
                    "[ ] Communication plan approved"
                ]
            },
            "Design network architecture": {
                "title": "Lab 5.2: Enterprise Network Architecture Design",
                "objective": "Design scalable network architecture",
                "duration": "120 minutes",
                "equipment": ["Network design template", "Diagramming tool", "Traffic analysis", "Vendor specifications"],
                "procedures": [
                    "Analyse business requirements: growth projections, application needs, security requirements",
                    "Evaluate network topologies: mesh, hub-and-spoke, hybrid approaches",
                    "Design IP addressing scheme: subnetting, VLAN design, routing domains",
                    "Plan redundancy: link redundancy, device redundancy, site failover",
                    "Evaluate technology options: traditional vs software-defined networking, cloud integration",
                    "Design security segmentation: DMZ, internal zones, guest network",
                    "Create detailed network diagram: physical and logical topology",
                    "Document design decisions with business justification"
                ],
                "expected_outcome": "Detailed network design supporting business objectives",
                "checklist": [
                    "[ ] Requirements understood",
                    "[ ] Topology evaluated",
                    "[ ] IP scheme designed",
                    "[ ] Redundancy planned",
                    "[ ] Technology selected",
                    "[ ] Security design complete",
                    "[ ] Diagrams created",
                    "[ ] Design approved"
                ]
            },
            "Manage network implementation": {
                "title": "Lab 5.3: Network Implementation and Change Control",
                "objective": "Execute network deployment with change management discipline",
                "duration": "120 minutes",
                "equipment": ["Implementation schedule", "Change management process", "Rollback procedures", "Testing plan"],
                "procedures": [
                    "Plan deployment phases: minimal impact approach, maintenance windows, pilot site first",
                    "Create change records: what's changing, why, who's impacted, rollback procedures",
                    "Plan testing gates: lab validation, pilot site validation, production validation",
                    "Design pilot approach: select representative site, run in parallel, measure success",
                    "Develop training plan: IT operations staff, help desk, power users",
                    "Create communication timeline: stakeholder notifications, status updates",
                    "Plan troubleshooting: known issues, workarounds, escalation procedures",
                    "Document lessons learned from each phase"
                ],
                "expected_outcome": "Successful network deployment with controlled change management",
                "checklist": [
                    "[ ] Deployment phases planned",
                    "[ ] Change records created",
                    "[ ] Testing gates defined",
                    "[ ] Pilot plan approved",
                    "[ ] Training scheduled",
                    "[ ] Communications scheduled",
                    "[ ] Troubleshooting procedures documented",
                    "[ ] Lessons learned captured"
                ]
            },
            "Operate and optimize network": {
                "title": "Lab 5.4: Network Operations and Performance Optimization",
                "objective": "Establish network operations and continuous improvement",
                "duration": "90 minutes",
                "equipment": ["Operations procedures", "Monitoring dashboards", "Capacity planning model", "Optimization toolkit"],
                "procedures": [
                    "Document network operating procedures: maintenance windows, escalation, incident response",
                    "Establish performance baselines: bandwidth utilisation, latency, packet loss",
                    "Plan capacity monitoring: trending, alerts, growth forecasting",
                    "Design performance optimization: QoS policies, link aggregation, load balancing",
                    "Create optimization recommendations based on performance data",
                    "Plan periodic reviews: quarterly health checks, annual architecture review",
                    "Establish change management for network modifications",
                    "Create knowledge base for troubleshooting and maintenance"
                ],
                "expected_outcome": "Network operations program with optimization and capacity planning",
                "checklist": [
                    "[ ] Operating procedures documented",
                    "[ ] Baselines established",
                    "[ ] Monitoring configured",
                    "[ ] QoS policies implemented",
                    "[ ] Optimization recommendations created",
                    "[ ] Review schedule established",
                    "[ ] Change process defined",
                    "[ ] Knowledge base created"
                ]
            }
        },
        6: {  # CoCu 6: SOP Development and Implementation
            "Develop standard operating procedures": {
                "title": "Lab 6.1: SOP Development and Documentation Standards",
                "objective": "Create comprehensive SOP framework and standards",
                "duration": "120 minutes",
                "equipment": ["SOP template", "Process documentation tool", "Approval workflow", "Knowledge base"],
                "procedures": [
                    "Define SOP scope: IT operations, incident response, change management, security",
                    "Create SOP structure: title, objective, scope, prerequisites, step-by-step procedures, troubleshooting",
                    "Design documentation standards: formatting, terminology, visuals, accessibility",
                    "Identify critical processes requiring SOPs: highest risk, highest impact",
                    "Prioritize SOP development: quick wins first, major processes second",
                    "Create approval workflow: technical review, process owner approval, executive sign-off",
                    "Plan SOP maintenance: annual reviews, version control, update triggers",
                    "Design SOP accessibility: searchable knowledge base, role-based access"
                ],
                "expected_outcome": "SOP framework with development standards and approval process",
                "checklist": [
                    "[ ] SOP scope defined",
                    "[ ] Template created and approved",
                    "[ ] Standards documented",
                    "[ ] Critical processes identified",
                    "[ ] Prioritization completed",
                    "[ ] Approval workflow designed",
                    "[ ] Maintenance plan established",
                    "[ ] Knowledge base setup"
                ]
            },
            "Document critical IT processes": {
                "title": "Lab 6.2: Critical Process Documentation",
                "objective": "Document critical IT operations processes",
                "duration": "120 minutes",
                "equipment": ["SOP template", "Process analysis tools", "Stakeholder interviews", "Review checklist"],
                "procedures": [
                    "Interview process owners and practitioners",
                    "Map current process: inputs, decision points, outputs, exceptions",
                    "Identify risks and failure points in existing process",
                    "Design improved process: eliminate waste, clarify responsibilities, add controls",
                    "Create step-by-step procedure documentation with clear language",
                    "Add troubleshooting section: common issues and solutions",
                    "Include security controls and compliance requirements",
                    "Create checklists for critical steps"
                ],
                "expected_outcome": "Well-documented critical processes with improvement opportunities identified",
                "checklist": [
                    "[ ] Current process understood",
                    "[ ] Improvements identified",
                    "[ ] Procedures documented clearly",
                    "[ ] Troubleshooting included",
                    "[ ] Security controls documented",
                    "[ ] Checklists created",
                    "[ ] Review completed",
                    "[ ] Approval obtained"
                ]
            },
            "Implement and train on SOPs": {
                "title": "Lab 6.3: SOP Implementation and Training Program",
                "objective": "Deploy SOPs and train staff on new procedures",
                "duration": "120 minutes",
                "equipment": ["Training plan", "Training materials", "Knowledge base", "Competency assessment"],
                "procedures": [
                    "Develop training plan: classroom, hands-on labs, online modules, mentoring",
                    "Create training materials: slides, step-by-step guides, videos, scenarios",
                    "Schedule training sessions: all shifts, role-specific sessions",
                    "Conduct classroom training: explanation, Q&A, discussion of scenarios",
                    "Conduct hands-on labs: supervised practice, feedback, troubleshooting",
                    "Assign mentors for on-the-job training during transition period",
                    "Perform competency assessments: practical tests, knowledge checks",
                    "Capture feedback and make improvements to SOPs based on real-world experience"
                ],
                "expected_outcome": "Trained staff with documented competency and improved SOPs",
                "checklist": [
                    "[ ] Training plan completed",
                    "[ ] Training materials developed",
                    "[ ] Training sessions held",
                    "[ ] Hands-on labs conducted",
                    "[ ] Mentoring assigned",
                    "[ ] Competency assessed",
                    "[ ] Feedback captured",
                    "[ ] SOPs improved"
                ]
            },
            "Monitor SOP compliance and effectiveness": {
                "title": "Lab 6.4: SOP Compliance Auditing and Continuous Improvement",
                "objective": "Monitor compliance and measure SOP effectiveness",
                "duration": "90 minutes",
                "equipment": ["Audit procedures", "Compliance metrics", "Effectiveness measures", "Improvement process"],
                "procedures": [
                    "Define compliance metrics: procedure adherence, step completion, approval requirements",
                    "Design audit procedures: random sampling, observation, documentation review",
                    "Establish effectiveness measures: incident reduction, cycle time improvement, error reduction",
                    "Conduct quarterly compliance audits: observe work, interview staff, review documentation",
                    "Measure process metrics: time required, error rate, first-time success rate",
                    "Identify improvement opportunities: bottlenecks, exceptions, common errors",
                    "Create improvement process: priority, impact assessment, implementation plan",
                    "Report results to management: compliance rate, effectiveness measures, improvements completed"
                ],
                "expected_outcome": "Compliance metrics and continuous improvement program for SOPs",
                "checklist": [
                    "[ ] Metrics defined",
                    "[ ] Audit procedures created",
                    "[ ] Effectiveness measures established",
                    "[ ] Quarterly audits conducted",
                    "[ ] Metrics tracked",
                    "[ ] Improvements identified",
                    "[ ] Improvement process followed",
                    "[ ] Results reported"
                ]
            }
        },
        7: {  # CoCu 7: Server Scripting
            "Plan scripting initiatives": {
                "title": "Lab 7.1: IT Automation and Scripting Strategy",
                "objective": "Develop enterprise scripting and automation strategy",
                "duration": "120 minutes",
                "equipment": ["Scripting strategy template", "ROI calculator", "Automation tool evaluation", "Skills inventory"],
                "procedures": [
                    "Identify repetitive, manual IT processes that could be automated",
                    "Assess automation ROI: staff time savings, error reduction, consistency improvement",
                    "Evaluate scripting platforms: PowerShell, Python, Bash, orchestration tools (Ansible, Terraform)",
                    "Assess current skills: who can write scripts, what training needed",
                    "Create automation roadmap: quick wins, high-value automations, infrastructure investment",
                    "Design governance: script approval, testing, change management, version control",
                    "Plan infrastructure: script repository, scheduling engine, monitoring, logging",
                    "Define standards: coding standards, documentation, error handling, security"
                ],
                "expected_outcome": "Enterprise scripting strategy with automation roadmap",
                "checklist": [
                    "[ ] Automation opportunities identified",
                    "[ ] ROI calculated",
                    "[ ] Platforms evaluated",
                    "[ ] Skills assessed",
                    "[ ] Roadmap created",
                    "[ ] Governance designed",
                    "[ ] Infrastructure planned",
                    "[ ] Standards documented"
                ]
            },
            "Develop core automation scripts": {
                "title": "Lab 7.2: Core Automation Script Development",
                "objective": "Develop critical automation scripts",
                "duration": "120 minutes",
                "equipment": ["Development environment", "Script templates", "Testing framework", "Documentation"],
                "procedures": [
                    "Select high-value automation targets: user provisioning, patch deployment, backups, monitoring",
                    "Design script architecture: parameters, error handling, logging, modularity",
                    "Implement scripts with best practices: comments, variable naming, functions, testing",
                    "Create error handling: catch exceptions, provide meaningful errors, retry logic",
                    "Add monitoring/alerting: log script execution, alert on failures",
                    "Develop automated testing: unit tests, integration tests, rollback procedures",
                    "Document scripts: purpose, parameters, expected output, troubleshooting",
                    "Create runbooks: how to execute, what can go wrong, escalation procedures"
                ],
                "expected_outcome": "Production-ready automation scripts with testing and documentation",
                "checklist": [
                    "[ ] Scripts selected and prioritized",
                    "[ ] Architecture designed",
                    "[ ] Scripts implemented",
                    "[ ] Error handling robust",
                    "[ ] Monitoring configured",
                    "[ ] Testing completed",
                    "[ ] Documentation complete",
                    "[ ] Runbooks created"
                ]
            },
            "Implement and manage scripts in production": {
                "title": "Lab 7.3: Script Deployment and Operational Management",
                "objective": "Deploy and operationalize scripts",
                "duration": "120 minutes",
                "equipment": ["Deployment procedures", "Scheduling engine", "Monitoring platform", "Change management"],
                "procedures": [
                    "Plan deployment: pilot rollout, phased introduction, success criteria",
                    "Test in production-like environment: realistic data volumes, timing, dependencies",
                    "Schedule script execution: timing, frequency, parallel execution constraints",
                    "Set up monitoring: script execution logging, performance metrics, failure alerts",
                    "Create response procedures: what to do if script fails, manual recovery steps",
                    "Document operational runbooks: script purpose, when it runs, who to contact if it fails",
                    "Train operations staff: troubleshooting, escalation, manual intervention procedures",
                    "Perform periodic reviews: execution success rate, performance, opportunity for improvement"
                ],
                "expected_outcome": "Operationalized scripts with monitoring and support procedures",
                "checklist": [
                    "[ ] Deployment plan approved",
                    "[ ] Production testing completed",
                    "[ ] Scheduling configured",
                    "[ ] Monitoring implemented",
                    "[ ] Response procedures documented",
                    "[ ] Runbooks completed",
                    "[ ] Training delivered",
                    "[ ] Reviews scheduled"
                ]
            },
            "Manage and improve scripting capability": {
                "title": "Lab 7.4: Scripting Capability Management and Continuous Improvement",
                "objective": "Manage scripting program and drive continuous improvement",
                "duration": "90 minutes",
                "equipment": ["Script inventory", "Performance metrics", "Improvement process", "Training plan"],
                "procedures": [
                    "Maintain script inventory: what scripts exist, purpose, owner, last updated",
                    "Track script execution metrics: success rate, duration, resource usage",
                    "Identify opportunities: scripts failing frequently, slow execution, new automation targets",
                    "Plan improvements: script optimization, feature additions, error handling enhancements",
                    "Manage script versions: version control, rollback capability, change history",
                    "Update documentation: keep runbooks current with actual behavior",
                    "Plan skills development: advanced scripting training, new languages, best practices",
                    "Report to leadership: automation ROI, staff time savings, error reduction achieved"
                ],
                "expected_outcome": "Managed scripting program with continuous improvement",
                "checklist": [
                    "[ ] Inventory maintained",
                    "[ ] Metrics tracked",
                    "[ ] Improvements identified",
                    "[ ] Version control implemented",
                    "[ ] Documentation updated",
                    "[ ] Training planned",
                    "[ ] ROI documented",
                    "[ ] Leadership reporting in place"
                ]
            }
        }
    }

    # Generate exercises for each activity
    for activity in activities:
        # Look for template matching this activity
        template = None
        if cocu_num in exercise_templates:
            # Try exact match first
            if activity in exercise_templates[cocu_num]:
                template = exercise_templates[cocu_num][activity]
            else:
                # Try partial match (case-insensitive prefix)
                activity_lower = activity.lower()
                for template_activity, template_data in exercise_templates[cocu_num].items():
                    if activity_lower.startswith(template_activity.lower()[:20]):
                        template = template_data
                        break

        if template:
            # Use detailed template
            exercises += f"### {template['title']}\n\n"
            exercises += f"**Objective:** {template['objective']}\n\n"
            exercises += f"**Duration:** {template['duration']}\n\n"
            exercises += "**Resources Required:**\n"
            for resource in template['equipment']:
                exercises += f"- {resource}\n"
            exercises += "\n**Procedures:**\n"
            for i, proc in enumerate(template['procedures'], 1):
                exercises += f"{i}. {proc}\n"
            exercises += f"\n**Expected Outcome:**\n{template['expected_outcome']}\n\n"
            exercises += "**Assessment Checklist:**\n"
            for item in template['checklist']:
                exercises += f"{item}\n"
            exercises += "\n"
        else:
            # Fallback for activities not in templates
            exercises += f"### {activity}\n\n"
            exercises += f"**Objective:** Execute {activity.lower()} following management and governance standards\n\n"
            exercises += "**Duration:** 120 minutes\n\n"
            exercises += "**Resources Required:** Planning templates, analysis tools, stakeholder engagement, documentation\n\n"
            exercises += "**Procedures:**\n"
            exercises += f"1. Review business objectives and requirements\n"
            exercises += f"2. Conduct stakeholder consultation and impact analysis\n"
            exercises += f"3. Develop strategy or plan for {activity.lower()}\n"
            exercises += f"4. Document decisions with business justification\n"
            exercises += f"5. Obtain management and stakeholder approval\n"
            exercises += f"6. Plan implementation with success criteria\n"
            exercises += f"7. Create monitoring and review procedures\n\n"
            exercises += "**Expected Outcome:**\n"
            exercises += f"Approved management decision document with implementation plan and success metrics\n\n"
            exercises += "**Assessment Checklist:**\n"
            exercises += "- [ ] Business requirements clearly understood\n"
            exercises += "- [ ] Stakeholder consultation completed\n"
            exercises += "- [ ] Strategy/plan comprehensively developed\n"
            exercises += "- [ ] Decisions justified with evidence\n"
            exercises += "- [ ] Management approval obtained\n"
            exercises += "- [ ] Implementation plan realistic\n"
            exercises += "- [ ] Success criteria measurable\n"
            exercises += "- [ ] Documentation complete and clear\n\n"

    return exercises


def add_practical_exercises_to_file(file_path: str) -> bool:
    """Add practical exercises section to an L5 CoCu file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if Practical Exercises section already exists (idempotency)
        if "## Practical Exercises" in content:
            print(f"✓ {file_path} already has Practical Exercises section, skipping")
            return True

        # Extract CoCu number and title from the file
        title_match = re.match(r'^#\s+CoCu\s+(\d+):\s+(.+?)\s*\(', content, re.MULTILINE)
        if not title_match:
            print(f"✗ Could not extract CoCu number and title from {file_path}")
            return False

        cocu_num = int(title_match.group(1))
        cocu_title = title_match.group(2).strip()

        # Extract work activities
        activities = extract_work_activities(content)
        if not activities:
            print(f"✗ Could not extract work activities from {file_path}")
            return False

        # Generate practical exercises
        exercises = generate_practical_exercises(cocu_num, cocu_title, activities)

        # Find insertion point: after "## Learning Outcome Matrix" section
        insertion_pattern = r'(## Learning Outcome Matrix\n.*?\n\n)'
        match = re.search(insertion_pattern, content, re.DOTALL)

        if match:
            insert_pos = match.end()
        else:
            # Fallback: insert before "## Employability Skills"
            insertion_pattern = r'(## Employability Skills)'
            match = re.search(insertion_pattern, content)
            if match:
                insert_pos = match.start()
            else:
                print(f"✗ Could not find insertion point in {file_path}")
                return False

        # Insert practical exercises
        new_content = content[:insert_pos] + exercises + "\n" + content[insert_pos:]

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"✓ Added Practical Exercises to {file_path}")
        return True

    except Exception as e:
        print(f"✗ Error processing {file_path}: {e}")
        return False


def main():
    """Main function to process all L5 CoCu files."""
    base_dir = Path(__file__).parent.parent / "content" / "IT-020-5"

    # Files to process (L5 CoCu files only)
    cocu_files = [
        "01_CoCu-1-Management-Overview.md",
        "02_CoCu-2-Computer-System-Asset-Management.md",
        "03_CoCu-3-Computer-System-Security-Management.md",
        "04_CoCu-4-Disaster-Recovery-Management.md",
        "05_CoCu-5-Computer-System-Network-Project-Management.md",
        "06_CoCu-6-SOP-Development-And-Implementation.md",
        "07_CoCu-7-Server-Scripting.md"
    ]

    print("Adding Practical Exercises sections to L5 CoCu files...\n")

    successes = 0
    for file_name in cocu_files:
        file_path = base_dir / file_name
        if add_practical_exercises_to_file(str(file_path)):
            successes += 1

    print(f"\n✓ Successfully processed {successes}/{len(cocu_files)} files")
    return 0 if successes == len(cocu_files) else 1


if __name__ == "__main__":
    exit(main())
