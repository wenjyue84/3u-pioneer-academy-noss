# CoCu 4: Server Installation (240 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 4: Server Installation (Pemasangan Pelayan) | CoCu 4: Server Installation (Pemasangan Pelayan) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE JOB ORDER/CHANGE REQUEST · EXECUTE HARDWARE INSTALLATION · CARRY OUT SOFTWARE INSTALLATION · PERFORM SERVER FUNCTIONALITY TEST · PREPARE SERVER INSTALLATION SET-UP REPORT | ANALYSE JOB ORDER/CHANGE REQUEST · EXECUTE HARDWARE INSTALLATION · CARRY OUT SOFTWARE INSTALLATION · PERFORM SERVER FUNCTIONALITY TEST · PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 4 / P(4/7) | PAGE: 73 - 92 |


| SET-UP CONTEXT | TOWER SERVER | RACK SERVER |
|----------------|--------------|-------------|
| Job request | Small business or branch office requiring a standalone server. Job order specifies server model, OS, roles (e.g. file server, DNS), and network settings. Single PSU and standard cooling; placed on floor or in cabinet. | Data centre or server room deployment requiring rack-mounted servers. Job order specifies rack position, form factor (1U, 2U), redundant PSU, RAID configuration, network VLAN, and out-of-band management (iLO, iDRAC). |
| Tools and parts | Standard server toolkit: screwdrivers, anti-static strap, USB installer, and network cables. Server-grade components (CPU, RAM, drives, RAID card) from inventory. No rack hardware needed. | Extended toolkit: rack rails, cage nuts, cable management arms, label maker, screwdrivers, anti-static strap, USB installer, and network cables. Hot-swap drives and redundant PSUs as specified. PDU connections and cable labelling required. |
| Report | Server installation report with asset ID, location, hardware configuration, OS and roles, network settings (IP, gateway, DNS), and sign-off. | Server installation report with asset ID, rack position, hardware configuration (including RAID), redundant PSU status, management IP, OS and roles, network settings (IP, VLAN, gateway, DNS), and sign-off. |


| Type of Tools | Description |
|---------------|-------------|
| Screwdriver set and anti-static strap | Used to install server components (CPU, RAM, drives, expansion cards) and to mount the server in a rack or cabinet. Anti-static strap is worn and connected to a grounded point when handling server boards and memory to prevent ESD damage. Server components are more costly than desktop parts, making ESD precautions critical. |
| Rack rails and cage nuts | Used to mount rack servers into the server rack. Rails are specific to the server model and rack type; verify compatibility before installation. Cage nuts are inserted into the rack posts to provide threaded mounting points. Correct rail installation ensures the server slides in and out smoothly for maintenance. |
| Cable management arms and label maker | Cable management arms attach to the rear of the server and organise power, network, and management cables so the server can slide out without disconnecting. A label maker is used to tag each cable and port for identification during troubleshooting and maintenance. Proper labelling reduces errors in multi-server environments. |
| Multimeter | Used to check power supply voltages and continuity before and after installation. Confirms that the PSU is within tolerance and that PDU outlets are providing correct voltage. Essential when commissioning redundant PSU configurations to verify both power paths are active. |
| USB bootable media | Used to load the server operating system (Windows Server, Linux) and drivers during software installation. The installer is prepared according to the job order with the correct OS version and licence key. Some servers require legacy boot or UEFI settings to be configured in BIOS before booting from USB. |
| Network cable tester | Used to verify network cable wiring and connectivity between the server NIC and the switch port. Confirms that each wire is correctly terminated and that the link is active at the expected speed. Essential when connecting multiple NICs or configuring VLAN trunks. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 15% | 36 | Analyse job order/change request | 10.8 | 25.2 | 36.0 |
| 40% | 96 | Execute hardware installation | 28.8 | 67.2 | 96.0 |
| 30% | 72 | Carry out software installation | 21.6 | 50.4 | 72.0 |
| 10% | 24 | Perform server functionality test | 7.2 | 16.8 | 24.0 |
| 5% | 12 | Prepare server installation set-up report | 3.6 | 8.4 | 12.0 |
| **100%** | **240** | | **72.0** | **168.0** | **240.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 4: Server Installation (Pemasangan Pelayan) | CoCu 4: Server Installation (Pemasangan Pelayan) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE JOB ORDER/CHANGE REQUEST · EXECUTE HARDWARE INSTALLATION · CARRY OUT SOFTWARE INSTALLATION · PERFORM SERVER FUNCTIONALITY TEST · PREPARE SERVER INSTALLATION SET-UP REPORT | ANALYSE JOB ORDER/CHANGE REQUEST · EXECUTE HARDWARE INSTALLATION · CARRY OUT SOFTWARE INSTALLATION · PERFORM SERVER FUNCTIONALITY TEST · PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 4 / P(4/7) | PAGE: 93 - 112 |


| Hardware Component | Description |
|--------------------|-------------|
| Server chassis / form factor | Rack servers (1U, 2U, etc.) are mounted in a standard 19-inch rack with rails and require proper cooling and power distribution. Tower servers are standalone chassis similar to desktops, placed on the floor or in a cabinet, and are easier to access for small sites. The choice is determined by the job order based on site requirements, number of servers, and available infrastructure. |
| Redundant power supply (PSU) | Dual or hot-swap PSUs provide continuous power if one unit fails. Both PSUs are connected to different circuits or power distribution units (PDUs) where specified so that a single power failure does not shut down the server. Verify both PSUs are active and drawing load after installation using the server management interface or front-panel indicators. |
| RAID controller and disk array | Redundant array of independent disks for capacity and/or data redundancy (e.g. RAID 1 for mirroring, RAID 5 for parity, RAID 10 for mirroring plus striping). Configured in BIOS/UEFI or via a hardware RAID card before installing the OS. The operating system is installed after the array is created and recognised by the installer. Hot-swap drive bays allow failed disks to be replaced without shutting down the server. |
| Network interfaces (NICs) | One or more network interface cards providing connectivity to the LAN, management network, or storage network. IP address, subnet, gateway, and VLAN are configured as per the job order. Cables are connected to the correct switch ports and labelled. Teaming or bonding may be configured for redundancy or bandwidth. |
| Out-of-band management (iLO / iDRAC) | Remote management interfaces such as HP iLO or Dell iDRAC that provide console access, power control, and hardware monitoring even when the OS is down. A dedicated management IP and credentials are configured per the job order. Enables remote troubleshooting and reduces the need for physical access to the server room. |

![Standard 42U Server Rack Layout](images/server-rack-layout.png)

![RAID Level Comparison](images/raid-levels.png)

| Software Component | Description |
|---------------------|-------------|
| Server operating system | Windows Server or Linux (e.g. CentOS, Ubuntu Server, RHEL) installed from USB or network boot as per the job order. Installation includes partitioning, base OS configuration, hostname, and initial administrator credentials. The licence or activation key is applied during or after installation. |
| Roles and features | Server roles such as file server, DNS, DHCP, Active Directory, Hyper-V, or web server are installed and configured as specified in the change request. Dependencies must be followed (e.g. Active Directory before file server permissions). Each role is tested after installation to confirm correct operation. |
| Patches and updates | Security and cumulative updates applied after the base OS installation to bring the server to current patch level. Reboots are scheduled as required; downtime is communicated to stakeholders. Verify that updates install correctly and that all roles function normally after reboot. |
| Backup and recovery configuration | Backup software and schedule configured as part of the server installation to protect data from the first day of operation. Includes configuring Windows Server Backup or a third-party agent (e.g. Veeam, Acronis), defining backup targets (local disk, NAS, or cloud), and verifying the first backup completes successfully. The backup configuration is documented in the server installation report. |


| Server Installation Report | Description |
|-----------------------------|-------------|
| Asset and location | Server name, asset ID, rack position (for rack servers), or physical location (for tower servers). Recording the exact location enables quick identification during maintenance or incident response, especially in multi-rack environments. This information also feeds into the organisation's asset register for lifecycle tracking and capacity planning. |
| Hardware configuration | Model, CPU, RAM capacity, storage configuration (RAID level, number and type of drives), NICs, and management IP. A complete hardware record ensures that future upgrades or replacements use compatible components and that capacity can be assessed without physical inspection. This also serves as the baseline for troubleshooting, allowing technicians to compare the current state against the original build specification. |
| Software configuration | OS version, installed roles and features, key applications, and patch level. Documenting the software baseline ensures that any changes made after deployment can be compared against the original installation. This record is essential for disaster recovery, as it provides the information needed to rebuild the server to its exact pre-failure state. |
| Network settings | IP addresses, subnet mask, VLAN, gateway, and DNS servers. Accurate network records prevent IP conflicts and enable rapid reconfiguration if the server is moved or the network is restructured. This information is also critical for firewall rule creation and network security audits. |
| Sign-off | Installer name and date; acceptance by requester or supervisor. Sign-off provides accountability by confirming who performed the installation and that the requester accepted the completed work. It also marks the formal handover point after which the server enters production and is covered by the organisation's maintenance and support processes. |


| Common Fault | Cause | Action |
|--------------|-------|--------|
| Server does not POST | Loose CPU, RAM not seated, PSU not connected, or motherboard fault | Check all power connections; reseat CPU and RAM; verify PSU switch and cables; test with minimal configuration |
| RAID array not recognised | RAID controller not configured, drives not seated, or incompatible drives | Enter RAID BIOS and create array; reseat drives; verify drive compatibility with controller |
| OS installer does not detect RAID | Missing RAID driver for the OS installer | Load the RAID controller driver from USB during OS installation; download correct driver from manufacturer |
| No network connectivity after install | NIC driver missing, wrong IP configuration, or cable not connected to correct switch port | Install NIC driver; verify IP settings match job order; check cable and switch port; test with ping |
| Out-of-band management not accessible | Management IP not configured, wrong VLAN, or cable not connected | Configure management IP in BIOS/UEFI or via front-panel; verify cable is connected to the management network port; check VLAN settings |
| Redundant PSU not active | Second PSU not connected, PDU circuit off, or PSU fault | Connect second PSU to a separate PDU or circuit; verify power indicator on both PSUs; replace faulty PSU |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse job order/change request | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Execute hardware installation | Understand installation procedures and configuration options | Successfully install and configure software or systems | Practical installation; verification of correct configuration | Installation log; system configuration screenshots; test results |
| Carry out software installation | Know procedures and troubleshooting techniques | Execute procedures and resolve issues | Practical demonstration; problem-solving observed | Completed task log; troubleshooting notes; final working state |
| Perform server functionality test | Know testing procedures and acceptance criteria | Execute tests and document results | Practical test execution; result documentation | Test results log; signed-off test report |
| Prepare server installation set-up report | Know tools, parts, and materials needed | Gather and organize tools, parts, and materials | Practical observation of tool/material preparation; checklist verification | Photo/log of prepared toolkit; materials checklist |

## Practical Exercises

The following hands-on lab exercises develop the practical competencies required for Server Installation. Each exercise is designed for L3 operational-level technicians and includes step-by-step procedures, required equipment, and assessment criteria aligned with NOSS standards.

### Lab 1: Analyse job order/change request

**Objective:** Perform analyse job order/change request correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for analyse job order/change request
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of analyse job order/change request with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 2: Execute hardware installation

**Objective:** Perform execute hardware installation correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for execute hardware installation
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of execute hardware installation with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 3: Carry out software installation

**Objective:** Perform carry out software installation correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for carry out software installation
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of carry out software installation with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 4: Perform server functionality test

**Objective:** Perform perform server functionality test correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for perform server functionality test
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of perform server functionality test with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 5: Prepare server installation set-up report

**Objective:** Perform prepare server installation set-up report correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for prepare server installation set-up report
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of prepare server installation set-up report with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Activity:** Analyse job order/change request
- **Mapping:** Clarify server requirements with stakeholders; document configuration details; communicate completion status to project team

### 2. Teamwork & Collaboration
- **All activities**
- **Mapping:** Coordinate with network teams on IP allocation and cable management; work with storage teams on RAID configuration; involve supervisor in complex decisions

### 3. Problem-solving
- **All activities, especially during functionality testing**
- **Mapping:** Diagnose POST failures, RAID issues, and driver problems; troubleshoot network connectivity using systematic methods

### 4. Initiative & Self-reliance
- **All server installation activities**
- **Mapping:** Work independently on hardware assembly and configuration; take responsibility for verification testing before handover

### 5. Planning & Organizing
- **Activities:** Analyse job order, Execute hardware installation
- **Mapping:** Plan installation sequence; organize tools and components; follow correct BIOS/firmware configuration order

### 6. Self-management & Safety Awareness
- **All activities involving high-power systems and complex configurations**
- **Mapping:** Follow safety protocols for server power distribution; manage time to complete installation on schedule; maintain detailed documentation for production handover

### 7. Technology Use & Technical Proficiency
- **All activities requiring server hardware, RAID, network, and OS installation skills**
- **Mapping:** Configure RAID arrays and network settings; perform BIOS/UEFI configuration; troubleshoot using diagnostic tools and management interfaces

### 8. Learning Skills & Continuous Improvement
- **All activities; especially for different server platforms and configurations**
- **Mapping:** Learn new server hardware architectures; stay current on RAID controller and firmware updates; analyze installation issues to improve future procedures


## Attitude, Safety and Environmental

### Workplace Safety
- **Electrostatic Discharge (ESD) Protection:** Always wear an anti-static wrist strap and work on a grounded surface when handling motherboards, RAM, CPU, and expansion cards. Even small static charges can permanently damage sensitive components.
- **Electrical Safety:** When testing with a multimeter or working near power supplies, ensure the power is disconnected and use proper testing techniques. Follow all electrical safety guidelines and never work on live circuits.
- **Thermal Compound Handling:** Apply thermal paste correctly between CPU and heatsink to prevent overheating and damage. Use only the recommended amount and allow proper curing time before powering on.
- **Safe Cable Management:** Ensure network and power cables are properly routed to avoid tripping hazards, kinks, and damage. Label cables clearly for future troubleshooting and maintenance.

### Environmental Considerations
- **E-waste Management:** Properly dispose of defective hardware components, circuit boards, and packaging materials through authorised e-waste recycling centres. Never dispose of electronics in regular trash or landfill.
- **Energy Efficiency:** Configure systems to use power-saving modes and efficient power supplies. Avoid unnecessary idle time and follow organisational energy conservation policies.

### Professional Attitudes
- **Punctuality and Reliability:** Complete server installation work on schedule to meet user handover deadlines and support business operations.
- **Integrity in Documentation:** Prepare accurate and complete installation reports with all hardware details, software versions, and test results. Honest documentation supports future troubleshooting and maintains system integrity.
- **Teamwork and Support:** Collaborate with help desk staff and other technicians; share knowledge about system configurations and troubleshooting techniques to improve overall technical capability.
- **Attention to Detail:** Verify every connection, configuration setting, and test result to ensure server installation tasks are completed correctly and systems function as intended.

## References

**Official Standards and Frameworks:**

- NOSS IT-020-3:2013 Computer System Operation Syllabus
- Dell PowerEdge Server Installation and Configuration Guide (RAID Setup)
- HP ProLiant Server Reference Architecture – Hardware and Firmware Setup
- Lenovo ThinkSystem Server Installation and First Boot Guide
- RAID Configuration Best Practices – Dell, HP, Lenovo Documentation

**Technical References and Best Practices:**

- Storage Area Network (SAN) Introduction and Zoning Fundamentals
- CompTIA Server+ Certification Guide – Server Hardware and Configuration
- Microsoft Windows Server 2025 Installation and Initial Configuration
- Linux Server Installation (Red Hat, Ubuntu, Debian) – Disk Partitioning and LVM
- Fiber Channel and iSCSI Protocol Standards for Enterprise Storage

**Contact hour:** [[00_Contact-hour_IT-020-3-L3-Operation]]


---

↑ [README](../../README.md) · **IT-020-3** > CoCu 4 - Server Installation

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-3-L3-Operation.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Computer-System-Set-up.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Maintenance.md) · [03_CoCu-3](03_CoCu-3-Computer-System-Repair.md) · [05_CoCu-5](05_CoCu-5-Server-Maintenance.md) · [06_CoCu-6](06_CoCu-6-Computer-Network-Connectivity-Set-up.md) · [07_CoCu-7](07_CoCu-7-Mobile-Device-Configuration.md)

**Other levels:** [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
