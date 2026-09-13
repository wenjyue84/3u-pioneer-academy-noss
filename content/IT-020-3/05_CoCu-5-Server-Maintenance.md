# CoCu 5: Server Maintenance (180 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 5: Server Maintenance (Penyelenggaraan Pelayan) | CoCu 5: Server Maintenance (Penyelenggaraan Pelayan) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE SERVER MAINTENANCE JOB ORDER · CARRY OUT HARDWARE MAINTENANCE · PERFORM SERVER OPERATING SYSTEM MAINTENANCE · PREPARE SERVER MAINTENANCE RECORD | ANALYSE SERVER MAINTENANCE JOB ORDER · CARRY OUT HARDWARE MAINTENANCE · PERFORM SERVER OPERATING SYSTEM MAINTENANCE · PREPARE SERVER MAINTENANCE RECORD |
| NO. CODE | IT-020-3:2013 - CoCu 5 / P(5/7) | PAGE: 113 - 122 |


| SET-UP CONTEXT | RACK SERVER / PREVENTIVE MAINTENANCE | TOWER SERVER / CORRECTIVE MAINTENANCE |
|----------------|--------------------------------------|---------------------------------------|
| Job order | Scheduled preventive maintenance for a rack-mounted server in the server room. Job order specifies server TAG/ID, OS version, warranty status, and maintenance checklist (hardware inspection, backup verification, log review, patch application). | Corrective maintenance for a tower server after hardware fault alert. Change request specifies server TAG/ID, fault description (e.g. degraded RAID, failed PSU), replacement parts, and expected downtime window. |
| Tools and parts | Standard server toolkit: vacuum cleaner, cable ties, screwdriver set, anti-static strap. Backup media (external drive or tape). Monitoring software access credentials and server access pass. | Extended toolkit: multimeter, replacement components (hot-swap disk, PSU), anti-static mat, manufacturer operating manual. Cable tester for network verification after repair. RAID controller documentation for rebuild procedures. |
| Record | Preventive maintenance record with server utilisation status, LED indicator readings, backup verification, log review summary, and technician sign-off. | Corrective maintenance record with fault description, root cause, parts replaced, warranty claim reference, RAID rebuild status, downtime duration, and user sign-off. Includes server maintenance costing estimate. |


| Type of Tools | Description |
|---------------|-------------|
| Vacuum cleaner (anti-static / ESD-safe) | Used to remove dust from server vents, heatsinks, fans, and internal components. Dust build-up restricts airflow and causes overheating. Only ESD-safe vacuum cleaners should be used in server rooms to avoid electrostatic discharge damage to sensitive components. Clean servers on a scheduled basis as part of preventive maintenance. |
| Screwdriver set (Phillips, flat, Torx) | Used to open server chassis, remove drive caddies, secure expansion cards, and replace hot-swap components. Server hardware often uses Torx or proprietary screws. Keep the correct bit sizes for each server model to avoid stripping. |
| Cable ties and labels | Used to organise and label server cables (power, network, SAN, KVM) for identification and airflow management. Proper cable management prevents accidental disconnection, improves cooling, and simplifies troubleshooting. Labels should include port number, destination, and VLAN or network segment where applicable. |
| Multimeter | Used to verify PSU voltages (+3.3 V, +5 V, +12 V) and check for short circuits before and after maintenance. Ensures replacement power supplies are within tolerance. Essential for corrective maintenance when a power-related fault is suspected. |
| Anti-static mat and wrist strap | Prevents electrostatic discharge when handling server components (RAM, CPU, expansion cards, drives). The wrist strap is connected to a grounded point; the mat provides a grounded working surface. Required for all internal hardware work on servers. |
| Backup software and media | Used to perform and verify server data backups before maintenance. Backup media includes external storage drives, tape cartridges, or network-attached storage. Backup software manages full and incremental backups and generates completion logs for verification. |
| Server management / monitoring software | Remote management tools (e.g. iDRAC, iLO, IPMI) and monitoring dashboards used to check server utilisation (CPU, memory, disk, network), LED status indicators, system logs, and antivirus status. Essential for analysing maintenance requirements and verifying post-maintenance health. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 15% | 27 | Analyse server maintenance job order | 8.1 | 18.9 | 27.0 |
| 45% | 81 | Carry out hardware maintenance | 24.3 | 56.7 | 81.0 |
| 30% | 54 | Perform server Operating System maintenance | 16.2 | 37.8 | 54.0 |
| 10% | 18 | Prepare server maintenance record | 5.4 | 12.6 | 18.0 |
| **100%** | **180** | | **54.0** | **126.0** | **180.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 5: Server Maintenance (Penyelenggaraan Pelayan) | CoCu 5: Server Maintenance (Penyelenggaraan Pelayan) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE SERVER MAINTENANCE JOB ORDER · CARRY OUT HARDWARE MAINTENANCE · PERFORM SERVER OPERATING SYSTEM MAINTENANCE · PREPARE SERVER MAINTENANCE RECORD | ANALYSE SERVER MAINTENANCE JOB ORDER · CARRY OUT HARDWARE MAINTENANCE · PERFORM SERVER OPERATING SYSTEM MAINTENANCE · PREPARE SERVER MAINTENANCE RECORD |
| NO. CODE | IT-020-3:2013 - CoCu 5 / P(5/7) | PAGE: 123 - 132 |


| Hardware Component | Description |
|--------------------|-------------|
| Server chassis and rack mount | The physical enclosure that houses all server components. Rack-mounted servers (1U, 2U, 4U) slide into standard 19-inch racks; tower servers stand alone. During maintenance, check the chassis for physical damage, dust accumulation, and proper airflow. Ensure rack rails and cable management arms are secure. The chassis must be accessible for hot-swap operations and cleaning. |
| Server power supply unit (PSU) | Provides power to all server components. Enterprise servers typically have redundant PSUs (e.g. 1+1) that allow hot-swap replacement without downtime. During maintenance, check PSU LED indicators: green means normal, amber or red indicates a fault. Use a multimeter to verify voltages are within tolerance. Replace faulty PSUs promptly to maintain redundancy. |
| Server fans and cooling system | Maintain operating temperature inside the server. Servers have multiple fans with redundancy; a failed fan triggers an alert on the management interface and an amber LED. During maintenance, check fan speed, listen for unusual noise, and clean dust from blades and heatsinks. Server room temperature (18–27 °C) and humidity (40–60% RH) must be within range. |
| Hard disk drives (HDD / SSD) in RAID array | Server storage configured in RAID (Redundant Array of Independent Disks) for performance and data protection. RAID levels include RAID 1 (mirror), RAID 5 (parity), and RAID 10 (mirror + stripe). During maintenance, check RAID status via the controller interface or server management tool: green = OK, amber = degraded (one disk failed), red = failed array. Replace degraded disks promptly using hot-swap procedure and allow rebuild to complete. |
| Uninterruptible Power Supply (UPS) | Provides battery backup power during mains power failure, allowing graceful server shutdown or continued operation. During maintenance, check UPS battery health, load level, and self-test results. Replace batteries on the manufacturer schedule. A failed UPS leaves the server unprotected against power outages. |
| Storage Area Network (SAN) devices | External storage connected to the server via fibre channel or iSCSI. During maintenance, check SAN connectivity, path redundancy, and disk utilisation. Verify that multipath I/O is active and that no single point of failure exists in the storage path. |
| Server LED status indicators | Physical LEDs on the front and rear panels that show system health at a glance. Key indicators include: Power ON/OFF (green = on), HDD activity (blinking green = I/O), fault indicator (amber = warning, red = critical), RAID status (green = healthy, amber = degraded), and network connectivity (green = link up, blinking = traffic). LED blinking patterns are documented in the manufacturer operating manual. |

![Standard 42U Server Rack Layout](images/server-rack-layout.png)

| Software / OS Maintenance Area | Description |
|--------------------------------|-------------|
| Server utilisation monitoring | Checking CPU usage, memory usage (physical RAM, virtual, shared), hard disk space (used, free, total), and network usage. High utilisation over sustained periods indicates the server may need a capacity upgrade or load balancing. Monitoring tools and dashboards provide historical trends. |
| Server data backup | Performing full backups (complete copy of all data) and incremental backups (only data changed since last backup). Backup is stored on internal storage, external media, or network-attached storage. After each backup, verify task completion status by checking backup logs for the location, date, backup name, and any errors. Backup must be completed before applying OS patches or performing major maintenance. |
| Server system logs | Three main log types: Security Log (login attempts, access events, policy changes), Application Log (application errors and events), and System Log (OS events, driver failures, service status). Log levels include Information, Warning, and Alert. Log file locations vary by OS (e.g. Event Viewer in Windows, /var/log/ in Linux). Review logs to identify critical errors, hardware failure alerts, OS vulnerability alerts, and service failures. |
| Server antivirus management | Maintaining antivirus software by checking: antivirus update log (pattern/definition currency), antivirus scan log (last scan results), threat log (detected and quarantined threats), and product/licence expiry date. Outdated antivirus patterns leave the server vulnerable to new threats. Schedule regular scans and ensure automatic updates are enabled. |
| Operating System patches and updates | Applying security bulletins and critical patches to the server OS. Check patch availability through Windows Update, WSUS, or the Linux distribution's package manager. Assess each patch for relevance and impact; apply in a test environment first where possible. Schedule patch installation during the maintenance window and document rollback procedures. Reboot the server after patches that require it. |


| Common Fault During Server Maintenance | Cause | Action |
|-----------------------------------------|-------|--------|
| RAID array degraded (amber LED) | One disk in the RAID array has failed or is reporting errors | Identify the failed disk from the RAID controller interface; hot-swap with a compatible replacement disk; monitor rebuild progress and verify RAID returns to healthy status (green LED) |
| Server overheating / thermal shutdown | Dust-blocked vents, failed fan, or server room temperature above 27 °C | Clean dust from all vents and heatsinks; replace failed fans; check server room air conditioning and verify temperature is within 18–27 °C range; check that cable management is not blocking airflow |
| Backup job failed or incomplete | Insufficient storage space on backup media, network interruption during backup, or corrupted backup software configuration | Check backup log for specific error; verify available space on target media; confirm network connectivity; re-run the backup and verify completion status in backup logs |
| Critical OS patch fails to install | Patch conflicts with installed software, insufficient disk space, or service dependency not met | Review the patch installation log for the specific error code; free disk space if needed; resolve software conflicts; retry patch installation; document in maintenance record and escalate if unresolved |
| Antivirus definitions outdated / scan not running | Automatic update disabled, network proxy blocking update server, or licence expired | Check antivirus update settings and proxy configuration; verify licence validity and renew if expired; manually trigger update and scan; verify threat log for any missed detections |
| UPS battery low or failed self-test | Battery degradation over time, excessive load, or environmental temperature too high | Check UPS battery age against manufacturer replacement schedule; reduce load if overloaded; verify server room temperature; replace battery module and re-run self-test to confirm |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse server maintenance job order | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Carry out hardware maintenance | Know procedures and troubleshooting techniques | Execute procedures and resolve issues | Practical demonstration; problem-solving observed | Completed task log; troubleshooting notes; final working state |
| Perform server Operating System maintenance | Understand concepts related to: Perform server Operating System maintenance | Successfully execute: Perform server Operating System maintenance | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Prepare server maintenance record | Know tools, parts, and materials needed | Gather and organize tools, parts, and materials | Practical observation of tool/material preparation; checklist verification | Photo/log of prepared toolkit; materials checklist |

## Practical Exercises

The following hands-on lab exercises develop the practical competencies required for Server Maintenance. Each exercise is designed for L3 operational-level technicians and includes step-by-step procedures, required equipment, and assessment criteria aligned with NOSS standards.

### Lab 1: Analyse server maintenance job order

**Objective:** Perform analyse server maintenance job order correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for analyse server maintenance job order
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of analyse server maintenance job order with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 2: Carry out hardware maintenance

**Objective:** Perform carry out hardware maintenance correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for carry out hardware maintenance
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of carry out hardware maintenance with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 3: Perform server Operating System maintenance

**Objective:** Perform perform server operating system maintenance correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for perform server operating system maintenance
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of perform server operating system maintenance with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 4: Prepare server maintenance record

**Objective:** Perform prepare server maintenance record correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for prepare server maintenance record
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of prepare server maintenance record with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Activity:** Prepare server maintenance report
- **Mapping:** Document maintenance activities; record patch installations and security updates; communicate findings and recommendations to management and operations teams

### 2. Teamwork & Collaboration
- **All activities in enterprise server environment**
- **Mapping:** Coordinate with security and operations teams; schedule maintenance windows; communicate with application owners about planned downtime

### 3. Problem-solving
- **Activities:** Identify maintenance requirements, Perform corrective maintenance
- **Mapping:** Troubleshoot patch installation failures; diagnose backup issues; resolve antivirus and UPS problems using logs and diagnostics

### 4. Initiative & Self-reliance
- **All preventive and corrective activities**
- **Mapping:** Take responsibility for proactive system health monitoring; make decisions on patch priority and scheduling; work independently on maintenance tasks

### 5. Planning & Organizing
- **Activities:** Identify maintenance requirements, Carry out scheduled preventive maintenance
- **Mapping:** Plan patch schedules around business needs; organize maintenance windows; coordinate with multiple teams and systems

### 6. Self-management & Safety Awareness
- **All activities in production server environment**
- **Mapping:** Work safely around servers and power distribution; follow change management procedures; manage risk of system downtime during maintenance

### 7. Technology Use & Technical Proficiency
- **All activities using server monitoring, patching, and backup tools**
- **Mapping:** Use system monitoring tools and event viewers; manage patch installations and rollbacks; configure backup and disaster recovery systems; troubleshoot using logs and diagnostics

### 8. Learning Skills & Continuous Improvement
- **All activities; especially for new server platforms and security threats**
- **Mapping:** Stay informed on critical security updates and vulnerabilities; learn new patching and backup technologies; improve maintenance procedures based on failure analysis


## Attitude, Safety and Environmental

### Workplace Safety
- **Hot-Swap and Rack Safety:** Follow proper hot-swap procedures when replacing drives and power supplies in live servers. Secure heavy equipment to rack rails before releasing; use a server lift or two-person handling for servers above 2U. Ensure rack doors and cable management arms are locked in position to prevent injury.
- **Server Room Environment:** Maintain server room temperature between 18-27 °C and relative humidity at 40-60 % RH. Monitor environmental sensors continuously and respond immediately to cooling failures. Restrict server room access to authorised personnel and enforce sign-in/sign-out procedures.
- **UPS Battery Handling:** Wear appropriate PPE (gloves, safety glasses) when inspecting or replacing UPS batteries. Sealed lead-acid and lithium-ion batteries contain hazardous materials; follow manufacturer handling and disposal guidelines. Never short-circuit battery terminals or expose batteries to excessive heat.
- **Cable Management for Airflow:** Route power, network, and SAN cables through designated cable management trays to maintain unobstructed airflow through server chassis and racks. Label all cables at both ends and avoid blocking front or rear ventilation zones with bundled cables.

### Environmental Considerations
- **E-waste Management:** Properly dispose of defective hardware components, circuit boards, and packaging materials through authorised e-waste recycling centres. Never dispose of electronics in regular trash or landfill.
- **Energy Efficiency:** Configure systems to use power-saving modes and efficient power supplies. Avoid unnecessary idle time and follow organisational energy conservation policies.

### Professional Attitudes
- **Punctuality and Reliability:** Complete server maintenance work on schedule to meet user handover deadlines and support business operations.
- **Integrity in Documentation:** Prepare accurate and complete server maintenance reports with all hardware details, software versions, and test results. Honest documentation supports future troubleshooting and maintains system integrity.
- **Teamwork and Support:** Collaborate with help desk staff and other technicians; share knowledge about system configurations and troubleshooting techniques to improve overall technical capability.
- **Attention to Detail:** Verify every connection, configuration setting, and test result to ensure server maintenance tasks are completed correctly and systems function as intended.

## References

**Official Standards and Frameworks:**

- NOSS IT-020-3:2013 Computer System Operation Syllabus
- HP ProLiant Server Maintenance and Updates – System Firmware Updates
- Dell iDRAC (Integrated Dell Remote Access Controller) Administration Guide
- Lenovo XClarity Administrator – Server Monitoring and Management
- Windows Server Update Services (WSUS) Deployment and Administration

**Technical References and Best Practices:**

- Linux Patch Management – yum, apt, dnf Package Management
- RAID Array Monitoring and Disk Replacement Procedures
- CompTIA Server+ Maintenance and Troubleshooting Objectives
- Environmental Monitoring in Data Centers – Temperature and Power Standards
- Backup and Recovery Best Practices – Veeam, Commvault Documentation

**Contact hour:** [[00_Contact-hour_IT-020-3-L3-Operation]]


---

↑ [README](../../README.md) · **IT-020-3** > CoCu 5 - Server Maintenance

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-3-L3-Operation.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Computer-System-Set-up.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Maintenance.md) · [03_CoCu-3](03_CoCu-3-Computer-System-Repair.md) · [04_CoCu-4](04_CoCu-4-Server-Installation.md) · [06_CoCu-6](06_CoCu-6-Computer-Network-Connectivity-Set-up.md) · [07_CoCu-7](07_CoCu-7-Mobile-Device-Configuration.md)

**Other levels:** [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
