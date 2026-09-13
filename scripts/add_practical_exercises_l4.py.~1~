#!/usr/bin/env python3
"""
Add Practical Exercises sections to all Level 4 CoCu files for US-014.

This script automates the insertion of administrative/supervisory exercise scenarios
aligned with each L4 CoCu's work activities. Exercises include planning, configuration,
security audits, and procurement scenarios following NOSS standards for L4
administrative/supervisory-level competencies.
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
    """Generate practical exercises section for an L4 CoCu."""
    exercises = "## Practical Exercises\n\n"
    exercises += f"The following administrative and supervisory exercise scenarios develop the competencies required for {cocu_title}. "
    exercises += "Each exercise is designed for L4 administrative/supervisory professionals and includes simulation scenarios, "
    exercises += "planning templates, documentation requirements, and assessment criteria aligned with NOSS standards.\n\n"

    # Define exercise templates based on CoCu
    exercise_templates = {
        1: {  # CoCu 1: Server Configuration
            "Analyse server configuration requirements": {
                "title": "Lab 1.1: Analysing Server Requirements and Planning",
                "objective": "Analyse business requirements and plan a server configuration strategy",
                "duration": "90 minutes",
                "equipment": ["Requirements document template", "Server sizing calculator", "Active Directory planning worksheet", "Hardware specification checklist"],
                "procedures": [
                    "Receive a simulated business requirement: expand file services to 200 users across 3 sites",
                    "Analyse requirements: identify number of users, storage needs, performance targets, availability requirements, budget",
                    "Consult vendor documentation for server CPU, memory, storage recommendations",
                    "Calculate required resources and identify single vs multi-server architecture",
                    "Design the server configuration including RAID level, backup strategy, and security baseline",
                    "Create a requirements specification document for stakeholder approval",
                    "Present recommendation with cost-benefit analysis"
                ],
                "expected_outcome": "Approved server configuration specification with justified architectural decisions",
                "checklist": [
                    "[ ] Business requirements clearly documented",
                    "[ ] Hardware sizing calculated with vendor specifications",
                    "[ ] Architecture decision (single/multi-server) justified",
                    "[ ] Cost estimates provided",
                    "[ ] Risk assessment completed",
                    "[ ] Stakeholder approval obtained"
                ]
            },
            "Plan server roles and services": {
                "title": "Lab 1.2: Planning Active Directory and Server Roles",
                "objective": "Design an Active Directory structure and plan role distribution across servers",
                "duration": "120 minutes",
                "equipment": ["Active Directory planning template", "GPO worksheet", "Organisational unit (OU) hierarchy diagram", "Role dependency matrix"],
                "procedures": [
                    "Review organisational structure: departments, teams, geographic locations",
                    "Design OU hierarchy reflecting company structure and delegated administration model",
                    "Plan role distribution: which server hosts DNS, DHCP, AD, file services, backup",
                    "Identify role dependencies and installation order",
                    "Create Group Policy strategy for security and compliance",
                    "Document naming conventions for computers, users, groups, OUs",
                    "Design site topology if multi-site deployment",
                    "Review plan with IT manager and stakeholders"
                ],
                "expected_outcome": "Comprehensive AD and role planning document with OU hierarchy, GPO strategy, and implementation roadmap",
                "checklist": [
                    "[ ] OU hierarchy defined and documented",
                    "[ ] Role distribution planned with justification",
                    "[ ] Role dependencies identified",
                    "[ ] Naming conventions defined",
                    "[ ] GPO strategy documented",
                    "[ ] Implementation sequence planned",
                    "[ ] Plan reviewed and approved"
                ]
            },
            "Configure server hardware and storage": {
                "title": "Lab 1.3: Hands-on Server Hardware Configuration",
                "objective": "Configure RAID storage and install server components in a lab environment",
                "duration": "120 minutes",
                "equipment": ["Lab server hardware", "RAID controller utility", "Multiple hard drives", "System utilities", "Configuration log sheet"],
                "procedures": [
                    "Power on the lab server and enter BIOS/UEFI setup",
                    "Verify processor, memory, and storage detection",
                    "Access RAID controller and configure RAID 5 with appropriate stripe size",
                    "Assign hot spare drive",
                    "Set boot order and enable/disable secure boot based on requirements",
                    "Configure power settings (wake-on-LAN, power loss recovery)",
                    "Record all BIOS settings that deviate from defaults",
                    "Document hardware configuration for reference"
                ],
                "expected_outcome": "Configured server hardware with RAID array built and documented settings",
                "checklist": [
                    "[ ] BIOS/UEFI settings verified and customized",
                    "[ ] RAID array successfully built and configured",
                    "[ ] Hot spare assigned",
                    "[ ] Boot sequence set correctly",
                    "[ ] Security features enabled/disabled per requirement",
                    "[ ] Configuration documented with photos/screenshots"
                ]
            },
            "Configure server OS and roles": {
                "title": "Lab 1.4: Installing Windows Server and Adding Roles",
                "objective": "Install Windows Server OS and add required server roles following the configuration plan",
                "duration": "180 minutes",
                "equipment": ["Configured lab server", "Windows Server installer media", "Server roles installation checklist", "Configuration documentation"],
                "procedures": [
                    "Boot from Windows Server installer media",
                    "Perform clean OS installation with appropriate partitioning",
                    "Configure networking (IP address, DNS, gateway) per plan",
                    "Install and configure Active Directory Domain Services",
                    "Install DHCP and configure scope with appropriate settings",
                    "Install DNS and create zones",
                    "Add file server role and create shares with permissions",
                    "Join additional test clients to the domain",
                    "Verify all roles are functioning correctly"
                ],
                "expected_outcome": "Fully functional server with all planned roles installed and verified working",
                "checklist": [
                    "[ ] OS installed successfully",
                    "[ ] Network configuration correct",
                    "[ ] AD installed and forest/domain created",
                    "[ ] DHCP scope functional",
                    "[ ] DNS resolving correctly",
                    "[ ] File shares accessible with correct permissions",
                    "[ ] Client domain join successful",
                    "[ ] All roles verified in Server Manager"
                ]
            },
            "Implement server security settings": {
                "title": "Lab 1.5: Server Security Hardening and Group Policy",
                "objective": "Apply security hardening baselines and create initial Group Policy Objects",
                "duration": "120 minutes",
                "equipment": ["Server running with roles", "Security Compliance Toolkit (Microsoft)", "Group Policy Management Console", "Hardening checklist"],
                "procedures": [
                    "Review CIS Benchmark for Windows Server baseline",
                    "Disable unnecessary services and features",
                    "Configure local Group Policy for password policy and account lockout",
                    "Configure audit policy for account logon, privilege use, and system events",
                    "Create first-run GPOs for domain-joined computers (eg. antivirus deployment)",
                    "Configure Windows Defender exclusions and update schedule",
                    "Enable Windows Firewall rules for required services",
                    "Configure BitLocker for sensitive partitions",
                    "Run security baseline scanning tool to identify remaining gaps"
                ],
                "expected_outcome": "Hardened server with baseline security controls and initial GPO infrastructure in place",
                "checklist": [
                    "[ ] CIS Benchmark reviewed and documented",
                    "[ ] Unnecessary services disabled",
                    "[ ] Password policy configured",
                    "[ ] Audit policy enabled",
                    "[ ] Initial GPOs created and linked",
                    "[ ] Firewall rules enabled for services",
                    "[ ] Antivirus configured",
                    "[ ] Security baseline scan shows improvement"
                ]
            },
            "Document server configuration": {
                "title": "Lab 1.6: Creating Configuration Documentation and Runbooks",
                "objective": "Complete comprehensive documentation for operations and disaster recovery",
                "duration": "90 minutes",
                "equipment": ["Configured and hardened server", "Documentation template", "Runbook template", "Network diagram tool"],
                "procedures": [
                    "Create server asset record with hostname, IP, OS version, serial numbers",
                    "Document all installed roles and features with versions",
                    "Create network diagram showing server, network segments, and connectivity",
                    "Document Active Directory structure (forest, domains, OUs, trust relationships)",
                    "Create DHCP scope and DNS zone documentation",
                    "Create troubleshooting runbook for common issues",
                    "Create disaster recovery runbook for rebuilding the server",
                    "Document change history and approval signatures",
                    "Store documentation in a centralized location with version control"
                ],
                "expected_outcome": "Complete documentation package including asset record, network diagram, runbooks, and change history",
                "checklist": [
                    "[ ] Asset information recorded",
                    "[ ] All roles and features documented",
                    "[ ] Network topology diagram created",
                    "[ ] AD structure documented",
                    "[ ] Troubleshooting runbook completed",
                    "[ ] Disaster recovery runbook completed",
                    "[ ] Change history and approvals recorded",
                    "[ ] Documentation stored and indexed"
                ]
            }
        },
        2: {  # CoCu 2: Computer System Security Control
            "Identify security requirements": {
                "title": "Lab 2.1: Security Requirements Assessment",
                "objective": "Assess organisational security requirements and create a security requirements specification",
                "duration": "90 minutes",
                "equipment": ["Security requirements template", "Risk assessment matrix", "Compliance checklist (ISO 27001, GDPR, PCI-DSS)", "Regulatory documents"],
                "procedures": [
                    "Interview stakeholders about current security concerns and incidents",
                    "Review data classification: identify critical, sensitive, and public data",
                    "Analyse current security posture (existing firewalls, antivirus, access controls)",
                    "Identify compliance requirements (industry standards, legal regulations, customer contracts)",
                    "Conduct risk assessment: identify threats and vulnerabilities",
                    "Prioritize security controls based on risk and business impact",
                    "Create security requirements specification with measurable objectives",
                    "Present recommendations to management for approval"
                ],
                "expected_outcome": "Approved security requirements specification aligned with compliance and risk",
                "checklist": [
                    "[ ] Stakeholder input documented",
                    "[ ] Data classification completed",
                    "[ ] Current state assessed",
                    "[ ] Compliance requirements identified",
                    "[ ] Risk assessment completed",
                    "[ ] Security controls prioritized",
                    "[ ] Requirements document approved"
                ]
            },
            "Implement access control and authentication": {
                "title": "Lab 2.2: Active Directory Security and MFA Deployment Planning",
                "objective": "Plan and implement access control using Active Directory and multi-factor authentication",
                "duration": "120 minutes",
                "equipment": ["Active Directory Users and Computers", "Group Policy editor", "MFA solution (Azure AD/Okta)", "Access control matrix template"],
                "procedures": [
                    "Design role-based access control (RBAC) groups aligned with job functions",
                    "Create security groups: departmental groups, project groups, administrative groups",
                    "Implement group nesting for efficient permission management",
                    "Configure Group Policy for password complexity and expiry",
                    "Enable MFA for remote access and privileged accounts",
                    "Create and test MFA enrolment process",
                    "Document access control matrix (who has what access)",
                    "Conduct access review with department managers"
                ],
                "expected_outcome": "Implemented access control structure with MFA enabled and documented access matrix",
                "checklist": [
                    "[ ] Security groups created per design",
                    "[ ] Group nesting implemented",
                    "[ ] Password policy configured",
                    "[ ] MFA enrolled for sensitive accounts",
                    "[ ] MFA tested and working",
                    "[ ] Access matrix documented",
                    "[ ] Access review completed and approved"
                ]
            },
            "Configure firewall and network security": {
                "title": "Lab 2.3: Firewall Rule Configuration and Network Segmentation",
                "objective": "Design and configure firewall rules implementing network segmentation and zero-trust principles",
                "duration": "120 minutes",
                "equipment": ["Firewall management console", "Network topology diagram", "Firewall rule template", "Port reference guide"],
                "procedures": [
                    "Design network zones: trusted (internal), DMZ (semi-trusted), untrusted (internet)",
                    "Identify traffic flows required between zones (e.g., user to file server, web to database)",
                    "Create baseline firewall rules: allow critical services, deny all else",
                    "Implement stateful inspection to permit return traffic",
                    "Configure rules for management traffic (restrict to admin subnet)",
                    "Test firewall rules: verify allowed traffic flows, block denied traffic",
                    "Document all firewall rules with business justification",
                    "Implement monitoring/logging for rule hits"
                ],
                "expected_outcome": "Configured firewall with segmented zones, baseline rules, and monitoring in place",
                "checklist": [
                    "[ ] Network zones defined and documented",
                    "[ ] Traffic flow requirements identified",
                    "[ ] Firewall rules created and prioritized",
                    "[ ] Stateful inspection enabled",
                    "[ ] Rules tested and verified working",
                    "[ ] Rule documentation completed",
                    "[ ] Logging and monitoring configured",
                    "[ ] Rules reviewed for optimization"
                ]
            },
            "Manage patches and security updates": {
                "title": "Lab 2.4: WSUS Deployment and Patch Management Planning",
                "objective": "Plan and implement a patch management process using WSUS and measure compliance",
                "duration": "90 minutes",
                "equipment": ["WSUS server", "Group Policy editor", "Patch management policy template", "Vulnerability scanner"],
                "procedures": [
                    "Design patch management policy: critical=immediate, high=within 2 weeks, etc.",
                    "Install and configure WSUS server with appropriate synchronization schedule",
                    "Create WSUS computer groups: production servers, test workstations, user devices",
                    "Create GPO to configure clients to use WSUS",
                    "Approve critical security patches for immediate deployment",
                    "Test patches in non-production environment before production release",
                    "Schedule patch deployment during maintenance windows",
                    "Monitor compliance reporting in WSUS",
                    "Document patch process and escalation procedures"
                ],
                "expected_outcome": "Functional WSUS infrastructure with patch policy documented and compliance monitoring in place",
                "checklist": [
                    "[ ] Patch policy defined and documented",
                    "[ ] WSUS installed and configured",
                    "[ ] Client GPO configured",
                    "[ ] Computer groups created",
                    "[ ] Critical patches approved",
                    "[ ] Test environment patching successful",
                    "[ ] Deployment schedule established",
                    "[ ] Compliance monitoring working",
                    "[ ] Patch process documented"
                ]
            },
            "Document security configuration and incidents": {
                "title": "Lab 2.5: Security Documentation and Incident Response Procedures",
                "objective": "Create comprehensive security documentation and incident response runbooks",
                "duration": "90 minutes",
                "equipment": ["Security policy templates", "Incident response template", "Change management process", "Evidence tracking worksheet"],
                "procedures": [
                    "Create security baseline document: access control rules, firewall rules, hardening standards",
                    "Create incident response procedure: detection, containment, eradication, recovery, post-incident review",
                    "Document escalation procedures and contact lists",
                    "Create security incident log template with fields: date, description, impact, actions, outcome",
                    "Create change management process for security changes",
                    "Document forensic preservation procedures for incident investigation",
                    "Create evidence handling and audit trail procedures",
                    "Review and approve documentation with security team and management"
                ],
                "expected_outcome": "Complete security documentation suite including baselines, incident procedures, and change management",
                "checklist": [
                    "[ ] Security baseline documented",
                    "[ ] Incident response procedure created",
                    "[ ] Escalation procedures and contacts documented",
                    "[ ] Incident log template created",
                    "[ ] Change management process documented",
                    "[ ] Forensic procedures documented",
                    "[ ] Evidence procedures documented",
                    "[ ] Documentation reviewed and approved"
                ]
            }
        },
        3: {  # CoCu 3: System & Network Procurement
            "Analyse procurement requirements": {
                "title": "Lab 3.1: IT Procurement Requirements Analysis",
                "objective": "Analyse business needs and create a detailed procurement specification",
                "duration": "90 minutes",
                "equipment": ["Procurement requirements template", "Cost analysis worksheet", "Vendor comparison matrix", "Technical specification template"],
                "procedures": [
                    "Receive business requirement: replace aging network switches for 10 sites",
                    "Gather requirements: ports, speed, PoE capability, management features, budget",
                    "Identify technical specifications: VLAN support, redundancy, monitoring, disaster recovery",
                    "Research available vendors and products in market",
                    "Create detailed technical specification document",
                    "Develop cost analysis: hardware, software, installation, training, support",
                    "Create vendor evaluation criteria (price, performance, support, reputation)",
                    "Prepare business case with ROI analysis"
                ],
                "expected_outcome": "Detailed procurement specification with vendor comparison and approved business case",
                "checklist": [
                    "[ ] Business requirements documented",
                    "[ ] Technical specifications defined",
                    "[ ] Vendors and products researched",
                    "[ ] Cost analysis completed",
                    "[ ] Vendor evaluation criteria established",
                    "[ ] Business case prepared with ROI",
                    "[ ] Approval obtained from stakeholders"
                ]
            },
            "Assess vendor products and services": {
                "title": "Lab 3.2: Vendor Evaluation and Product Testing",
                "objective": "Evaluate vendors and conduct proof-of-concept testing of selected products",
                "duration": "120 minutes",
                "equipment": ["Test network segment", "Vendor product (trial/demo)", "Testing checklist", "Vendor scoreboard"],
                "procedures": [
                    "Request product trials and datasheets from shortlisted vendors",
                    "Conduct vendor site visits and reference checks",
                    "Set up test environment with sample of required product",
                    "Execute test cases based on requirements (throughput, latency, failover, management)",
                    "Document test results: what worked, what didn't, gaps",
                    "Score vendors based on evaluation criteria",
                    "Negotiate terms, pricing, warranty, and support SLAs",
                    "Present vendor recommendation to procurement and IT management"
                ],
                "expected_outcome": "Completed vendor evaluation report with test results and recommended vendor",
                "checklist": [
                    "[ ] Vendor datasheets reviewed",
                    "[ ] Reference checks completed",
                    "[ ] POC testing conducted",
                    "[ ] Test results documented",
                    "[ ] Vendor scored against criteria",
                    "[ ] Negotiations completed",
                    "[ ] SLAs documented",
                    "[ ] Recommendation approved"
                ]
            },
            "Plan procurement and delivery": {
                "title": "Lab 3.3: Procurement Planning and Logistics",
                "objective": "Create a procurement plan with delivery schedule and implementation timeline",
                "duration": "90 minutes",
                "equipment": ["Project plan template", "Procurement timeline", "Logistics checklist", "Vendor contract template"],
                "procedures": [
                    "Create detailed procurement schedule: order placement, delivery, staging, installation",
                    "Identify long lead time items and order early",
                    "Plan receiving and QA inspection process",
                    "Arrange staging and pre-configuration in a central location",
                    "Plan distribution to 10 sites with phased deployment schedule",
                    "Arrange training for network administrators on new equipment",
                    "Plan decommissioning of old equipment and e-waste disposal",
                    "Create risk mitigation plan for supply chain disruptions",
                    "Document procurement contract with vendor commitments"
                ],
                "expected_outcome": "Comprehensive procurement plan with timeline, logistics, training plan, and contract",
                "checklist": [
                    "[ ] Procurement timeline created",
                    "[ ] Delivery schedule established",
                    "[ ] Staging plan documented",
                    "[ ] Installation schedule created",
                    "[ ] Training plan prepared",
                    "[ ] Equipment disposal plan included",
                    "[ ] Risk mitigation identified",
                    "[ ] Vendor contract signed"
                ]
            },
            "Execute procurement and monitor delivery": {
                "title": "Lab 3.4: Procurement Execution and Quality Assurance",
                "objective": "Place orders, monitor delivery, and conduct receiving QA",
                "duration": "90 minutes",
                "equipment": ["Purchase order", "Delivery tracking system", "QA checklist", "Receiving log"],
                "procedures": [
                    "Generate and issue purchase orders to vendor",
                    "Set up delivery tracking and receive notifications",
                    "Receive shipment and verify: count, serial numbers, condition",
                    "Conduct QA testing: power on, basic functionality, default configuration",
                    "Document any discrepancies and initiate claims with vendor if needed",
                    "Prepare equipment for staging: firmware updates, documentation",
                    "Stage equipment in lab for pre-configuration",
                    "Update inventory system with new asset information",
                    "Prepare for deployment phase"
                ],
                "expected_outcome": "Received and QA-tested equipment ready for staged deployment across sites",
                "checklist": [
                    "[ ] Purchase order issued",
                    "[ ] Delivery tracked and received on time",
                    "[ ] Quantity and serial numbers verified",
                    "[ ] Equipment tested for basic functionality",
                    "[ ] No damage or defects found",
                    "[ ] Discrepancies resolved with vendor",
                    "[ ] Equipment staged and documented",
                    "[ ] Inventory updated"
                ]
            },
            "Create procurement documentation": {
                "title": "Lab 3.5: Procurement Records and Compliance Documentation",
                "objective": "Create procurement records for audit and compliance",
                "duration": "60 minutes",
                "equipment": ["Procurement records template", "Vendor contract", "Receiving documentation", "QA test results"],
                "procedures": [
                    "Organize all procurement documentation: RFQ, vendor responses, evaluation results",
                    "Create procurement approval log showing who approved at each stage",
                    "Document vendor contract terms, pricing, warranty, support SLAs",
                    "Maintain receiving documentation: packing slips, serial numbers, QA results",
                    "Create asset register with equipment details, cost, depreciation schedule",
                    "Document procurement compliance: approved vendors, bidding process, documentation retention",
                    "Prepare compliance evidence for audit (e.g., competitive bidding documented)",
                    "Store records in centralized location with access control"
                ],
                "expected_outcome": "Complete procurement documentation package meeting audit and compliance requirements",
                "checklist": [
                    "[ ] All RFQ and vendor responses filed",
                    "[ ] Evaluation process documented",
                    "[ ] Approval log created",
                    "[ ] Vendor contract filed",
                    "[ ] Receiving documentation organized",
                    "[ ] Asset register updated",
                    "[ ] Compliance documentation prepared",
                    "[ ] Records stored and indexed"
                ]
            }
        },
        4: {  # CoCu 4: Network Cabling Management
            "Analyse cabling requirements": {
                "title": "Lab 4.1: Network Cabling Design and Requirements",
                "objective": "Analyse network requirements and design a cabling infrastructure",
                "duration": "90 minutes",
                "equipment": ["Network cabling design template", "Building floor plan", "Cabling category reference", "Cost estimator"],
                "procedures": [
                    "Review building layout and identify network equipment locations",
                    "Determine cabling requirements: ethernet runs, fiber backbone, patch panels",
                    "Calculate cable lengths and cabling categories (Cat6, Cat6a, Cat7, or fiber)",
                    "Design cable pathways: conduit, trays, risers avoiding power and RF interference",
                    "Plan patch panel locations and port allocation",
                    "Design redundancy: dual paths, diverse routing for critical links",
                    "Estimate quantities and costs for materials and installation",
                    "Create cabling design drawing with specifications"
                ],
                "expected_outcome": "Detailed cabling design with specifications, quantities, and cost estimates",
                "checklist": [
                    "[ ] Building layout analyzed",
                    "[ ] Equipment locations identified",
                    "[ ] Cabling requirements calculated",
                    "[ ] Cable categories selected",
                    "[ ] Pathways designed and documented",
                    "[ ] Patch panels planned",
                    "[ ] Redundancy incorporated",
                    "[ ] Cost estimates completed"
                ]
            },
            "Plan cabling installation": {
                "title": "Lab 4.2: Cabling Installation Project Planning",
                "objective": "Create a detailed installation plan minimizing network downtime",
                "duration": "90 minutes",
                "equipment": ["Project plan template", "Installation schedule", "Material list", "Team resource plan"],
                "procedures": [
                    "Create phased installation schedule: zone-by-zone or time-based",
                    "Plan equipment staging and pre-termination of cables in lab",
                    "Schedule installation during maintenance windows to minimize user impact",
                    "Identify required resources: contractors, tools, equipment, supervision",
                    "Plan testing and certification: cable length, continuity, performance",
                    "Plan decommissioning of old cabling",
                    "Prepare documentation: as-built diagrams, patching records",
                    "Plan user communication and support during installation"
                ],
                "expected_outcome": "Comprehensive installation plan with timeline, resource allocation, and risk mitigation",
                "checklist": [
                    "[ ] Phased installation schedule created",
                    "[ ] Maintenance windows identified",
                    "[ ] Materials and tools planned",
                    "[ ] Team resources allocated",
                    "[ ] Testing plan documented",
                    "[ ] Decommissioning plan included",
                    "[ ] Communication plan prepared",
                    "[ ] Risk mitigation documented"
                ]
            },
            "Manage cabling installation": {
                "title": "Lab 4.3: Cabling Installation Supervision and Quality Control",
                "objective": "Oversee installation process and ensure quality standards are met",
                "duration": "120 minutes",
                "equipment": ["Cable tester", "Crimping tool", "Labeling system", "QA checklist", "Installation log"],
                "procedures": [
                    "Brief installation team on design requirements and quality standards",
                    "Inspect cable pathways before installation begins",
                    "Inspect cable runs as installed: proper slack, separation from power, labeling",
                    "Verify patch panel installation and port mapping",
                    "Conduct cable testing: length, continuity, impedance, crosstalk per TIA-568",
                    "Certify cables meeting Cat6 or Cat6a performance standards",
                    "Verify proper termination: 568B standard, consistent across all ports",
                    "Create as-built documentation: actual cable runs, port assignments"
                ],
                "expected_outcome": "Certified cabling installation with test results and as-built documentation",
                "checklist": [
                    "[ ] Installation team briefed",
                    "[ ] Cable pathways inspected",
                    "[ ] Installed cables inspected for quality",
                    "[ ] Patch panels verified",
                    "[ ] Cable testing completed",
                    "[ ] Performance standards met",
                    "[ ] Proper labeling verified",
                    "[ ] As-built documentation created"
                ]
            },
            "Document cabling installation": {
                "title": "Lab 4.4: Cabling Infrastructure Documentation",
                "objective": "Create comprehensive documentation for operations and maintenance",
                "duration": "60 minutes",
                "equipment": ["Documentation template", "Cable management software", "Labeling system", "Archive system"],
                "procedures": [
                    "Create as-built cabling diagram matching final installation",
                    "Document patch panel port assignments and cross-connect",
                    "Record cable types, lengths, and locations for each run",
                    "Create outlet and termination records with test results",
                    "Document warranty information and certification dates",
                    "Create maintenance procedures: how to add/move cables, avoid damage",
                    "Store documentation in centralized location (paper and digital)",
                    "Create change log for future modifications"
                ],
                "expected_outcome": "Complete cabling documentation package for operational handover",
                "checklist": [
                    "[ ] As-built diagram created",
                    "[ ] Port assignments documented",
                    "[ ] Cable records complete",
                    "[ ] Test certificates filed",
                    "[ ] Warranty information recorded",
                    "[ ] Maintenance procedures documented",
                    "[ ] Documentation stored and indexed",
                    "[ ] Change log established"
                ]
            }
        },
        5: {  # CoCu 5: Network Installation Management
            "Analyse network installation requirements": {
                "title": "Lab 5.1: Network Deployment Requirements Analysis",
                "objective": "Analyse business and technical requirements for network deployment",
                "duration": "90 minutes",
                "equipment": ["Network design template", "Requirement gathering worksheet", "Network calculator", "Vendor specifications"],
                "procedures": [
                    "Interview stakeholders on network performance, reliability, and security needs",
                    "Assess current network: bottlenecks, scalability, aging equipment",
                    "Determine network scope: number of users, sites, device types, bandwidth requirements",
                    "Analyse application requirements: latency sensitivity, redundancy, disaster recovery",
                    "Evaluate network architecture options: flat, segmented, software-defined",
                    "Calculate IP addressing and VLAN requirements",
                    "Create high-level network design proposal",
                    "Obtain management approval and funding"
                ],
                "expected_outcome": "Approved network design specification with business justification",
                "checklist": [
                    "[ ] Stakeholder requirements gathered",
                    "[ ] Current state assessed",
                    "[ ] Scope clearly defined",
                    "[ ] Architecture options evaluated",
                    "[ ] IP addressing planned",
                    "[ ] VLAN design created",
                    "[ ] Design proposal approved",
                    "[ ] Funding authorized"
                ]
            },
            "Plan network installation": {
                "title": "Lab 5.2: Network Installation Project Planning",
                "objective": "Create detailed installation plan with timeline and risk management",
                "duration": "90 minutes",
                "equipment": ["Project plan template", "Gantt chart", "Risk register", "Communication plan"],
                "procedures": [
                    "Create detailed project schedule: design, procurement, testing, deployment, cutover",
                    "Plan hardware staging and pre-configuration",
                    "Design testing plan: lab validation, pilot site, production validation",
                    "Plan training for network administrators and support staff",
                    "Develop rollback procedures for cutover",
                    "Create change management process for approvals and documentation",
                    "Identify risks: vendor delays, compatibility, performance issues",
                    "Prepare communication plan for users and stakeholders"
                ],
                "expected_outcome": "Comprehensive network installation project plan with timeline, risks, and communication strategy",
                "checklist": [
                    "[ ] Project schedule created with milestones",
                    "[ ] Staging and pre-config plan documented",
                    "[ ] Testing plan detailed",
                    "[ ] Training schedule prepared",
                    "[ ] Rollback procedures documented",
                    "[ ] Change management process defined",
                    "[ ] Risk register completed",
                    "[ ] Communication plan prepared"
                ]
            },
            "Execute network installation": {
                "title": "Lab 5.3: Network Installation Execution and Testing",
                "objective": "Execute installation plan and conduct comprehensive testing",
                "duration": "120 minutes",
                "equipment": ["Lab network equipment", "Network testing tools", "Performance monitoring software", "Test plan checklist"],
                "procedures": [
                    "Execute lab network build following design specifications",
                    "Configure devices: routing, VLANs, ACLs, spanning tree",
                    "Conduct lab testing: connectivity, routing, load balancing, failover",
                    "Measure performance: throughput, latency, jitter, packet loss",
                    "Test redundancy: link failure, device failure, failover timing",
                    "Verify security: access control lists, isolation between VLANs",
                    "Document test results and address any issues found",
                    "Create deployment runbook based on lab testing"
                ],
                "expected_outcome": "Validated network design with test results and deployment procedures ready",
                "checklist": [
                    "[ ] Lab network built to spec",
                    "[ ] Devices configured correctly",
                    "[ ] Connectivity verified",
                    "[ ] Routing tested",
                    "[ ] Load balancing verified",
                    "[ ] Failover tested",
                    "[ ] Performance meets requirements",
                    "[ ] Deployment runbook created"
                ]
            },
            "Document network installation": {
                "title": "Lab 5.4: Network Documentation and Operational Handover",
                "objective": "Create comprehensive documentation for operations and maintenance",
                "duration": "90 minutes",
                "equipment": ["Documentation template", "Network diagram tool", "Configuration backup", "Runbook template"],
                "procedures": [
                    "Create network topology diagram: physical and logical",
                    "Document IP addressing scheme and VLAN assignments",
                    "Document device configurations: routing, access lists, QoS",
                    "Create device inventory: model, serial, firmware, purchase date",
                    "Create operational runbooks: troubleshooting, failover, recovery",
                    "Document monitoring and alerting strategy",
                    "Create change management process for network modifications",
                    "Backup all device configurations for disaster recovery"
                ],
                "expected_outcome": "Complete network documentation package for operational handover",
                "checklist": [
                    "[ ] Topology diagram created",
                    "[ ] IP scheme documented",
                    "[ ] VLAN assignments recorded",
                    "[ ] Device configurations documented",
                    "[ ] Device inventory created",
                    "[ ] Runbooks prepared",
                    "[ ] Monitoring strategy defined",
                    "[ ] Configurations backed up"
                ]
            }
        },
        6: {  # CoCu 6: Maintenance Management
            "Analyse maintenance requirements": {
                "title": "Lab 6.1: IT Maintenance Strategy and Planning",
                "objective": "Analyse systems and develop a comprehensive maintenance strategy",
                "duration": "90 minutes",
                "equipment": ["Maintenance strategy template", "System inventory", "Risk assessment matrix", "SLA template"],
                "procedures": [
                    "Inventory all systems: servers, network devices, storage, workstations",
                    "Classify systems by criticality: tier 1 (24/7), tier 2 (business hours), tier 3 (standard)",
                    "Analyse failure history: what breaks, how often, impact",
                    "Identify single points of failure and redundancy gaps",
                    "Determine maintenance needs: preventive (scheduled), corrective (reactive), perfective (optimization)",
                    "Design maintenance windows for tier 1/2 systems",
                    "Create SLAs: availability targets, response times, resolution times",
                    "Plan maintenance resource allocation (staff, contractors, tools)"
                ],
                "expected_outcome": "Approved maintenance strategy with SLAs and resource plan",
                "checklist": [
                    "[ ] System inventory complete",
                    "[ ] Systems classified by criticality",
                    "[ ] Failure history analyzed",
                    "[ ] SPOF identified",
                    "[ ] Maintenance types defined",
                    "[ ] Maintenance windows scheduled",
                    "[ ] SLAs documented",
                    "[ ] Resources allocated"
                ]
            },
            "Plan preventive maintenance": {
                "title": "Lab 6.2: Preventive Maintenance Planning and Scheduling",
                "objective": "Create preventive maintenance schedule to minimize system failures",
                "duration": "90 minutes",
                "equipment": ["Maintenance schedule template", "Vendor maintenance recommendations", "Calendar tool", "Procedure templates"],
                "procedures": [
                    "Review vendor recommendations for each system type",
                    "Define preventive maintenance tasks: cleaning, firmware updates, security patching",
                    "Determine frequencies: daily checks, weekly backups, monthly updates, quarterly audits",
                    "Schedule maintenance to avoid business impact and system dependencies",
                    "Create maintenance checklists for each task type",
                    "Define success criteria: system up, performance normal, no errors",
                    "Create runbooks for complex maintenance procedures",
                    "Assign responsibilities and escalation procedures"
                ],
                "expected_outcome": "Comprehensive preventive maintenance schedule with procedures and checklists",
                "checklist": [
                    "[ ] Vendor recommendations reviewed",
                    "[ ] Maintenance tasks defined",
                    "[ ] Frequencies determined",
                    "[ ] Schedule created and published",
                    "[ ] Checklists prepared",
                    "[ ] Runbooks documented",
                    "[ ] Responsibilities assigned",
                    "[ ] Escalation procedures defined"
                ]
            },
            "Execute and monitor maintenance": {
                "title": "Lab 6.3: Maintenance Execution and Performance Monitoring",
                "objective": "Execute maintenance procedures and monitor system performance",
                "duration": "120 minutes",
                "equipment": ["Maintenance management system", "Monitoring tools", "System utilities", "Maintenance log"],
                "procedures": [
                    "Execute preventive maintenance according to schedule",
                    "Document each maintenance task: date, time, technician, actions, result",
                    "Monitor system performance before and after maintenance",
                    "Verify systems meet performance baselines after maintenance",
                    "Track issue resolution times and escalation patterns",
                    "Identify systems requiring additional maintenance attention",
                    "Collect maintenance metrics: MTTR, MTBF, availability percentage",
                    "Review metrics monthly to identify trends and improvements needed"
                ],
                "expected_outcome": "Regular maintenance execution with documented results and performance trending",
                "checklist": [
                    "[ ] Maintenance executed on schedule",
                    "[ ] Each task documented",
                    "[ ] Performance monitored",
                    "[ ] Baselines maintained",
                    "[ ] Response times tracked",
                    "[ ] Escalations analyzed",
                    "[ ] Metrics calculated",
                    "[ ] Trends identified"
                ]
            },
            "Document and report on maintenance": {
                "title": "Lab 6.4: Maintenance Documentation and Reporting",
                "objective": "Create maintenance reports and manage operational knowledge",
                "duration": "60 minutes",
                "equipment": ["Maintenance reporting template", "Maintenance management system", "Knowledge base", "SLA dashboard"],
                "procedures": [
                    "Create monthly maintenance report: tasks completed, issues found, metrics",
                    "Track SLA compliance: availability, response time, resolution time",
                    "Create system health report: critical systems status, risk areas, improvements",
                    "Maintain maintenance knowledge base: common issues, solutions, procedures",
                    "Create trend analysis: failure patterns, seasonal issues, preventive action recommendations",
                    "Present maintenance metrics to management for budget/resource justification",
                    "Store all maintenance records for audit and warranty claims",
                    "Use reports to continuously improve maintenance strategy"
                ],
                "expected_outcome": "Regular maintenance reports with metrics, SLA tracking, and knowledge base",
                "checklist": [
                    "[ ] Monthly reports prepared",
                    "[ ] SLA compliance tracked",
                    "[ ] System health assessed",
                    "[ ] Knowledge base updated",
                    "[ ] Trends analyzed",
                    "[ ] Reports presented to management",
                    "[ ] Records archived",
                    "[ ] Strategy improvements identified"
                ]
            },
            "Manage maintenance resources": {
                "title": "Lab 6.5: Maintenance Team Management and Optimization",
                "objective": "Manage maintenance team performance and optimize resource allocation",
                "duration": "90 minutes",
                "equipment": ["Team management template", "Time tracking system", "Training plan", "Performance review template"],
                "procedures": [
                    "Track maintenance team workload: maintenance tasks completed, issues resolved, response times",
                    "Identify skill gaps and training needs: new technologies, compliance requirements",
                    "Plan training and certification programs",
                    "Conduct regular performance reviews with team members",
                    "Identify high-performers and knowledge experts for knowledge transfer",
                    "Plan cross-training to reduce single points of failure in team",
                    "Optimize team schedule based on workload patterns",
                    "Manage contractor relationships and costs"
                ],
                "expected_outcome": "Well-managed maintenance team with optimized resource allocation and continuous improvement",
                "checklist": [
                    "[ ] Workload tracked and analyzed",
                    "[ ] Skill gaps identified",
                    "[ ] Training plans created",
                    "[ ] Performance reviews conducted",
                    "[ ] Knowledge experts identified",
                    "[ ] Cross-training scheduled",
                    "[ ] Schedule optimized",
                    "[ ] Contractors managed"
                ]
            }
        }
    }

    # Get templates for this CoCu if they exist
    cocu_templates = exercise_templates.get(cocu_num, {})

    # Generate exercises for each activity
    for activity in activities:
        if activity in cocu_templates:
            template = cocu_templates[activity]
            exercises += f"### {template['title']}\n\n"
            exercises += f"**Objective:** {template['objective']}\n\n"
            exercises += f"**Duration:** {template['duration']}\n\n"
            exercises += f"**Resources Required:**\n"
            exercises += f"{', '.join(template['equipment'])}\n\n"
            exercises += "**Procedures:**\n"
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
            exercises += f"**Objective:** Execute {activity.lower()} according to L4 administrative standards\n\n"
            exercises += "**Duration:** 90 minutes\n\n"
            exercises += "**Resources Required:** Templates, documentation, planning tools appropriate to the activity\n\n"
            exercises += "**Procedures:**\n"
            exercises += f"1. Review requirements and planning templates\n"
            exercises += f"2. Complete planning and analysis for {activity.lower()}\n"
            exercises += f"3. Document decisions and create implementation plan\n"
            exercises += f"4. Present recommendations to stakeholders for approval\n\n"
            exercises += "**Expected Outcome:**\n"
            exercises += f"Approved plan with documented analysis and stakeholder sign-off\n\n"
            exercises += "**Assessment Checklist:**\n"
            exercises += "- [ ] Requirements clearly understood\n"
            exercises += "- [ ] Analysis completed and documented\n"
            exercises += "- [ ] Plan covers all relevant areas\n"
            exercises += "- [ ] Recommendations justified with evidence\n"
            exercises += "- [ ] Stakeholder approval obtained\n"
            exercises += "- [ ] Documentation complete and clear\n\n"

    return exercises


def add_practical_exercises_to_file(file_path: str) -> bool:
    """Add practical exercises section to an L4 CoCu file."""
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
    """Main function to process all L4 CoCu files."""
    base_dir = Path(__file__).parent.parent / "content" / "IT-020-4"

    # Files to process (L4 CoCu files only)
    cocu_files = [
        "01_CoCu-1-Server-Configuration.md",
        "02_CoCu-2-Computer-System-Security-Control.md",
        "03_CoCu-3-System-Network-Procurement.md",
        "04_CoCu-4-Network-Cabling-Management.md",
        "05_CoCu-5-Computer-Network-Installation-Management.md",
        "06_CoCu-6-Computer-System-Maintenance-Management.md"
    ]

    print("Adding Practical Exercises sections to L4 CoCu files...\n")

    successes = 0
    for file_name in cocu_files:
        file_path = base_dir / file_name
        if add_practical_exercises_to_file(str(file_path)):
            successes += 1

    print(f"\n✓ Successfully processed {successes}/{len(cocu_files)} files")
    return 0 if successes == len(cocu_files) else 1


if __name__ == "__main__":
    exit(main())
