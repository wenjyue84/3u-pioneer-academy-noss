---
title: "CoCu 6: Computer System Maintenance Management (L4, 200 hrs)"
date: 2026-04-04
tags:
  - project
  - education
  - noss
project: "NOSS"
status: active
---

# CoCu 6: Computer System Maintenance Management (L4, 200 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) |
| LEVEL | L4 | L4 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 6: Computer System Maintenance Management (Pengurusan Penyelenggaraan Sistem Komputer) | CoCu 6: Computer System Maintenance Management (Pengurusan Penyelenggaraan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE COMPUTER SYSTEM MAINTENANCE REQUIREMENTS · DEVELOP COMPUTER SYSTEM MAINTENANCE PLAN · MANAGE COMPUTER SYSTEM MAINTENANCE WORK · MANAGE COMPUTER SYSTEM TROUBLESHOOTING ISSUES/FAILURES · PRODUCE COMPUTER SYSTEM MAINTENANCE MANAGEMENT REPORT | ANALYSE COMPUTER SYSTEM MAINTENANCE REQUIREMENTS · DEVELOP COMPUTER SYSTEM MAINTENANCE PLAN · MANAGE COMPUTER SYSTEM MAINTENANCE WORK · MANAGE COMPUTER SYSTEM TROUBLESHOOTING ISSUES/FAILURES · PRODUCE COMPUTER SYSTEM MAINTENANCE MANAGEMENT REPORT |
| NO. CODE | IT-020-4:2013 - CoCu 6 / P(6/6) | PAGE: 129 - 144 |


| SET-UP CONTEXT | ROUTINE / SCHEDULED MAINTENANCE | INCIDENT-DRIVEN / CORRECTIVE MAINTENANCE |
|----------------|----------------------------------|-------------------------------------------|
| Trigger | Scheduled preventive maintenance based on maintenance plan, SLA, and vendor service intervals. Maintenance window is pre-approved and announced to users via trouble ticket or notice. | Unscheduled corrective maintenance triggered by hardware failure, software issue, security threat, or user complaint. Requires obtaining permission for emergency access and prioritising based on business impact. |
| Scope and tools | Standard toolkit: cleaning kit, thermal paste, multimeter, diagnostic software, backup media. Tasks include dust removal, firmware updates, log review, disk defragmentation, and driver updates. Asset inventory is checked and updated. | Extended toolkit: OS recovery disc, replacement components, external USB connector, data backup software. Tasks include fault diagnosis, component replacement, software reinstallation, patch application, and root cause analysis. Vendor warranty and procurement procedures may apply. |
| Reporting | Maintenance management report with work breakdown structure, schedule, checklist, team members, expenses, and recommendations for next maintenance cycle. Documents filed per company document management system. | Incident report with problem description, symptoms, root cause analysis, remedy applied, parts replaced, expenses, and recommendation for process improvement. Includes user feedback summary and escalation history (1st/2nd/3rd level support). |


| Type | Description |
|------|-------------|
| Preventive maintenance | Scheduled activities performed at regular intervals to prevent failures before they occur. Includes cleaning, firmware updates, log review, disk health checks, and backup verification. Follows the maintenance plan and SLA. Reduces unplanned downtime and extends equipment life. The administrator plans and delegates tasks using a work breakdown structure and checklist. |
| Corrective maintenance | Reactive maintenance performed after a fault or failure has been identified. Includes diagnosis, repair or replacement of failed components, software reinstallation, and patch application. Requires a cost-benefit analysis to decide between repair, replacement, or disposal. The administrator must obtain permission for unscheduled access and document all actions taken. |
| Predictive maintenance | Uses monitoring data (error logs, performance counters, SMART disk data, temperature sensors) to predict failures before they occur. Enables proactive replacement of components showing early warning signs. More cost-effective than corrective maintenance but requires monitoring tools and data analysis capability. |
| Troubleshooting techniques (substitution, elimination, testing) | Systematic methods for diagnosing computer system problems. Substitution replaces a suspected faulty component with a known-good one. Elimination removes variables one at a time to isolate the fault. Testing uses diagnostic tools (multimeter, self-test routines, error logging) to verify component function. The administrator selects the technique based on symptoms and available resources. |
| Support service levels (1st, 2nd, 3rd level) | Tiered support structure for handling user issues. 1st level: help desk, basic troubleshooting, password resets. 2nd level: desktop support, hardware/software diagnosis and repair. 3rd level: specialist or vendor escalation for complex issues (e.g. firmware bugs, warranty claims). The administrator manages escalation, tracks resolution, and evaluates service quality. |
| Risk and business impact analysis | Assessment of how hardware failure, software issues, or security threats affect business operations. Considers downtime cost, data loss risk, user safety, and business continuity. Results determine maintenance priority, budget allocation, and whether to repair, replace, or dispose. Required when presenting maintenance plans to management for approval. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 18% | 36 | Analyse computer system maintenance requirements | 10.8 | 25.2 | 36.0 |
| 15% | 30 | Develop computer system maintenance plan | 9.0 | 21.0 | 30.0 |
| 27% | 54 | Manage computer system maintenance work | 16.2 | 37.8 | 54.0 |
| 26% | 52 | Manage computer system troubleshooting issues/failures | 15.6 | 36.4 | 52.0 |
| 14% | 28 | Produce computer system maintenance management report | 8.4 | 19.6 | 28.0 |
| **100%** | **200** | | **60.0** | **140.0** | **200.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) |
| LEVEL | L4 | L4 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 6: Computer System Maintenance Management (Pengurusan Penyelenggaraan Sistem Komputer) | CoCu 6: Computer System Maintenance Management (Pengurusan Penyelenggaraan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE COMPUTER SYSTEM MAINTENANCE REQUIREMENTS · DEVELOP COMPUTER SYSTEM MAINTENANCE PLAN · MANAGE COMPUTER SYSTEM MAINTENANCE WORK · MANAGE COMPUTER SYSTEM TROUBLESHOOTING ISSUES/FAILURES · PRODUCE COMPUTER SYSTEM MAINTENANCE MANAGEMENT REPORT | ANALYSE COMPUTER SYSTEM MAINTENANCE REQUIREMENTS · DEVELOP COMPUTER SYSTEM MAINTENANCE PLAN · MANAGE COMPUTER SYSTEM MAINTENANCE WORK · MANAGE COMPUTER SYSTEM TROUBLESHOOTING ISSUES/FAILURES · PRODUCE COMPUTER SYSTEM MAINTENANCE MANAGEMENT REPORT |
| NO. CODE | IT-020-4:2013 - CoCu 6 / P(6/6) | PAGE: 145 - 156 |


| Hardware Tool | Description |
|---------------|-------------|
| Multimeter | Measures voltage (AC/DC), current, and resistance using interchangeable probes. Used to verify power supply unit (PSU) output on each rail (+3.3 V, +5 V, +12 V) against ATX specifications, with tolerances of plus or minus 5%; readings outside this range indicate a failing PSU that should be replaced. Also used to check for short circuits on motherboard power traces, test cable continuity for network and power cables, and measure wall outlet voltage to confirm adequate and stable mains power delivery. A digital multimeter with auto-ranging (such as the Fluke 115 or UNI-T UT61E) is recommended for IT maintenance as it provides accurate readings with minimal manual setup. Essential for diagnosing power-related failures -- including random shutdowns, boot failures, and component damage -- and for verifying repairs before powering on the system. |
| Repair toolkit (screwdrivers, pliers, torch) | Standard hand tools for opening chassis, removing and replacing components (drives, expansion cards, fans, cables), and inspecting internal connections. A well-equipped IT repair toolkit includes Phillips-head screwdrivers (#0, #1, #2 for different screw sizes), Torx drivers (T5 through T20, required by many Dell, HP, and Lenovo enterprise systems), flat-head screwdrivers, long-nose pliers for retrieving dropped screws or repositioning jumpers, and an ESD (electrostatic discharge) wrist strap to protect sensitive components from static damage during handling. A torch or headlamp aids visual inspection in poorly lit server rooms, rack interiors, and cramped workstation enclosures. Kits such as the iFixit Pro Tech Toolkit or Wiha precision sets provide comprehensive coverage for both desktop and server hardware across major manufacturers. |
| Thermal paste and cleaning kit | Thermal paste (also called thermal compound or TIM -- thermal interface material) is applied as a thin layer between the CPU die and heatsink base to fill microscopic air gaps and ensure efficient heat transfer; quality compounds such as Arctic MX-6, Noctua NT-H2, or Thermal Grizzly Kryonaut provide thermal conductivity of 8-12 W/mK. Thermal paste must be cleaned and reapplied whenever a heatsink is removed or reseated, during preventive maintenance cycles (typically every 2-3 years for workstations, annually for high-load servers), and when thermal monitoring shows elevated CPU temperatures despite clean fans. The cleaning kit includes anti-static brushes, compressed air cans or an electric blower (e.g. DataVac ED-500) for removing dust from fans, heatsinks, vents, and motherboard surfaces, lint-free microfibre cloths, and isopropyl alcohol (90% or higher concentration) for removing old thermal paste and cleaning contacts. Regular dust removal during preventive maintenance prevents overheating, reduces fan noise, and extends the lifespan of heat-sensitive components such as CPUs, GPUs, and voltage regulators. |
| External USB hard disk connector | A USB adapter or docking station used to connect internal drives (2.5-inch and 3.5-inch SATA, and legacy IDE/PATA) externally via USB 4 or USB-C for data recovery, backup, cloning, or migration when a system cannot boot from its own drive. Common products include the Sabrent USB 4 to SATA/IDE adapter, StarTech USB 4 dual-bay dock, and Inateck FE2010 drive enclosures. Allows the administrator to mount the drive on a working system, access and back up critical user data (documents, profiles, databases), verify drive health using SMART tools, and clone the drive to a replacement before performing repairs, OS reinstallation, or secure data wiping prior to disposal. This tool is essential in corrective maintenance scenarios where the original system is non-functional but the data on the drive must be preserved. |
| Network cable tester | Verifies cable continuity, correct pin-to-pin mapping (T568A or T568B wiring standard), and cable length for Ethernet cables (Cat5e, Cat6, Cat6a). Used during maintenance to confirm that network cables are not the cause of intermittent connectivity, slow speed, or complete link failure. Identifies common faults including open circuits (broken conductor), short circuits (conductors touching), miswired pairs (incorrect pin assignments), and split pairs (a wiring error that passes basic continuity tests but degrades performance due to increased crosstalk). Tools such as the Fluke Networks LinkIQ or MicroScanner PoE also verify PoE availability and cable distance, providing quick first-line diagnostics without the cost of a full cable certifier. |
| Equipment operating and service manuals | Vendor-provided documentation covering hardware specifications, component locations, disassembly and reassembly procedures, firmware and BIOS update instructions, supported replacement parts, and warranty terms and conditions. Must be consulted before performing any repair, upgrade, or component replacement to ensure the correct procedure is followed and the warranty is not voided -- for example, HP ProLiant and Dell PowerEdge servers have specific procedures for hot-swapping drives and memory that differ by model generation. Most manufacturers now provide service manuals as downloadable PDFs from their support portals (e.g. Dell Support, HP Support Center, Lenovo PSREF), and these should be saved locally or bookmarked for offline access in the server room. Manuals are kept on file as part of the asset inventory and cross-referenced with the maintenance plan to ensure firmware update schedules and preventive maintenance intervals align with vendor recommendations. |


| Software Tool | Description |
|---------------|-------------|
| Diagnostic and antivirus software | Software used to scan for malware, test hardware components (memory, disk, CPU), and identify system errors as part of both preventive and corrective maintenance workflows. Hardware diagnostic tools include Windows Memory Diagnostic and MemTest86 (bootable, thorough RAM testing that runs multiple pass patterns to detect intermittent memory faults), CHKDSK and fsck (file system integrity checks that detect and repair bad sectors and corrupted metadata), CrystalDiskInfo and Hard Disk Sentinel (real-time SMART data monitoring that tracks health indicators such as reallocated sector count, pending sector count, and power-on hours to predict drive failure), and vendor-specific diagnostics such as Dell SupportAssist, HP PC Hardware Diagnostics UEFI, and Lenovo Vantage. Enterprise antivirus and endpoint protection suites -- such as Symantec Endpoint Protection, ESET Endpoint Security, Trend Micro Apex One, or Microsoft Defender for Endpoint -- provide real-time malware scanning, scheduled full-system scans, quarantine management, and centralised reporting through a management console. All diagnostic and scan results are logged with timestamps and included in the maintenance or troubleshooting report for audit trail and trend analysis. |
| Monitoring and error logging programs | Tools that continuously track system performance metrics (CPU utilisation, memory usage, disk I/O, network throughput, temperature) and record errors, warnings, and informational events for analysis. Windows Event Viewer aggregates system, application, and security logs with event IDs that can be cross-referenced with Microsoft's knowledge base for diagnosis; Windows Performance Monitor (PerfMon) provides real-time and historical performance counters and can generate Data Collector Sets for baseline comparison. Enterprise monitoring platforms such as Nagios (open-source, plugin-based, widely used for server and service monitoring), Zabbix (open-source with SNMP, agent-based, and IPMI monitoring), PRTG Network Monitor (sensor-based licensing with auto-discovery), and SolarWinds Server & Application Monitor provide centralised dashboards, configurable alert thresholds, and automated notifications via email or SMS when metrics exceed normal ranges. Logs are analysed during preventive maintenance to identify recurring issues, spot deteriorating trends (e.g. steadily increasing disk error rates), and support predictive maintenance decisions -- for example, replacing a drive that shows rising reallocated sector counts before it fails completely. |
| Operating system recovery disc / USB | Bootable media (DVD or USB flash drive) used to repair or reinstall the operating system when the system cannot boot normally due to corrupted boot files, driver conflicts, failed updates, or malware damage. The Windows installation media (created using Microsoft's Media Creation Tool) contains the Windows Recovery Environment (WinRE) with repair tools including Startup Repair (automatic boot fix), System Restore (revert to a previous restore point), Command Prompt (for manual repair commands such as bootrec, bcdedit, SFC /scannow, and DISM), and System Image Recovery (restore from a full image backup). For Linux systems, a live USB (e.g. Ubuntu Live, SystemRescue) provides a bootable environment for mounting and repairing the installed OS, recovering files, or repairing GRUB boot loader configurations. Product keys, licence information, and activation status must be recorded in the asset inventory before any reinstallation to ensure proper re-activation; for volume-licensed environments, the KMS server address must be noted. The administrator should maintain a set of current recovery media for each OS version deployed in the organisation, stored securely and updated when new OS versions are adopted. |
| Data backup software | Software for creating full, incremental, or differential backups of user data, system state, and application configurations to protect against data loss during maintenance operations. A full backup captures all selected data (largest size, longest duration); incremental backups capture only changes since the last backup of any type (smallest size, fastest); differential backups capture changes since the last full backup (moderate size, simpler restore than incremental). Common solutions include Windows Server Backup (built-in, supports bare-metal recovery and system state backup), Veeam Backup & Replication (enterprise-grade, supports physical and virtual machine backup with instant VM recovery), Acronis Cyber Protect (combines backup with anti-malware), and Clonezilla (open-source disk/partition imaging). A backup must be performed before any destructive maintenance operation such as OS reinstallation, disk replacement, firmware update, or hardware disposal. After each backup, integrity is verified by checking logs for errors, performing a test restore of sample files, or running the software's built-in verification routine. Backup media (external drives, NAS, tape, or cloud storage), retention schedule, and rotation policy (e.g. grandfather-father-son) are documented in the maintenance plan and reviewed during preventive maintenance cycles. |

![Annual Preventive Maintenance Schedule](images/maintenance-schedule.png)


| Common Fault During Maintenance | Cause | Action |
|----------------------------------|-------|--------|
| System overheating or unexpected shutdown | Dust buildup on fans and heatsinks; dried thermal paste; blocked vents; fan failure | Clean fans and vents with compressed air; replace thermal paste; replace failed fan; verify airflow in rack or chassis |
| Disk errors or degraded performance | Aging drive with bad sectors; fragmented file system; failing SMART indicators | Run CHKDSK or equivalent; defragment if HDD; check SMART data; replace drive if failing and restore from backup |
| Software crash or blue screen (BSOD) | Incompatible driver or update; corrupted system files; insufficient memory or disk space | Check event logs for error code; roll back recent driver/update; run SFC or DISM repair; add memory or free disk space |
| Network connectivity intermittent after maintenance | Cable disturbed during work; NIC driver removed during software update; IP configuration changed | Reseat network cable; reinstall NIC driver; verify IP settings; test with ping and tracert |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse computer system maintenance requirements | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Develop computer system maintenance plan | Understand design and development principles | Design and develop systems/documents/procedures | Product review; quality assessment | Completed deliverable; design documentation; review feedback |
| Manage computer system maintenance work | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |
| Manage computer system troubleshooting issues/failures | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |
| Produce computer system maintenance management report | Understand management procedures and protocols | Manage resources and processes according to procedures | Practical management task; documentation review | Management logs; configuration records; audit trail |

## Practical Exercises

The following administrative and supervisory exercise scenarios develop the competencies required for Computer System Maintenance Management. Each exercise is designed for L4 administrative/supervisory professionals and includes simulation scenarios, planning templates, documentation requirements, and assessment criteria aligned with NOSS standards.

### Analyse computer system maintenance requirements

**Objective:** Execute analyse computer system maintenance requirements according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for analyse computer system maintenance requirements
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear

### Develop computer system maintenance plan

**Objective:** Execute develop computer system maintenance plan according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for develop computer system maintenance plan
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear

### Manage computer system maintenance work

**Objective:** Execute manage computer system maintenance work according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for manage computer system maintenance work
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear

### Manage computer system troubleshooting issues/failures

**Objective:** Execute manage computer system troubleshooting issues/failures according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for manage computer system troubleshooting issues/failures
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear

### Produce computer system maintenance management report

**Objective:** Execute produce computer system maintenance management report according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for produce computer system maintenance management report
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Mapping:** Document maintenance plans, schedules, and management reports; present maintenance performance metrics and failure trends to management; communicate scheduled downtime and troubleshooting outcomes to users and stakeholders

### 2. Teamwork & Collaboration
- **Mapping:** Lead maintenance teams across routine and corrective activities; coordinate with help desk on fault escalation and user communication; collaborate with vendors on warranty repairs and parts procurement

### 3. Problem-solving
- **Mapping:** Diagnose complex hardware and software failures escalated from L3 technicians; evaluate root causes of recurring faults to implement preventive measures; determine repair-versus-replace decisions based on cost and lifecycle analysis

### 4. Initiative & Self-reliance
- **Mapping:** Proactively analyze maintenance trends to anticipate failures; take responsibility for maintenance plan effectiveness and SLA compliance; initiate process improvements based on troubleshooting data

### 5. Planning & Organizing
- **Mapping:** Develop and manage preventive maintenance schedules across the asset fleet; organize spare parts inventory and tool allocation; plan corrective maintenance windows to minimize business disruption

### 6. Self-management & Safety Awareness
- **Mapping:** Follow change management procedures for maintenance activities affecting production systems; manage ESD, electrical, and thermal safety compliance across the maintenance team; ensure maintenance records meet audit and compliance requirements

### 7. Technology Use & Technical Proficiency
- **Mapping:** Use diagnostic and monitoring tools for proactive fault detection; manage CMDB and asset management systems for maintenance tracking; apply advanced troubleshooting techniques for complex system failures

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Stay current on hardware lifecycle management and new diagnostic tools; analyze maintenance reports to identify improvement opportunities; update maintenance procedures based on field experience and vendor advisories



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
- ITIL 4 Service Management – Maintenance and Operations Management Processes
- ISO/IEC 20000-1:2018 – IT Service Management Systems Standard
- System Center Configuration Manager (SCCM) – Patch Management and Deployment
- ManageEngine Patch Manager – Automated Patch Distribution and Compliance

**Technical References and Best Practices:**

- Puppet, Ansible, and Chef – Infrastructure as Code and Automation
- Maintenance Planning and Scheduling Best Practices for Data Centers
- Predictive Analytics for IT Asset Management – AI-Driven Maintenance Strategies
- CompTIA Server+ Advanced Maintenance and Troubleshooting Objectives
- SLA (Service Level Agreement) Development and KPI Monitoring Frameworks

**Contact hour:** [[00_Contact-hour_IT-020-4-L4-Administration]]


---

↑ [README](../../README.md) · **IT-020-4** > CoCu 6 - Computer System Maintenance Management

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-4-L4-Administration.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Server-Configuration.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Security-Control.md) · [03_CoCu-3](03_CoCu-3-System-Network-Procurement.md) · [04_CoCu-4](04_CoCu-4-Network-Cabling-Management.md) · [05_CoCu-5](05_CoCu-5-Computer-Network-Installation-Management.md)

**Other levels:** [IT-020-3 (L3)](../IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
