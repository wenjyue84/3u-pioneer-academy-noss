# CoCu 1: Computer System Set-up (300 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 1: Computer System Set-up (Persediaan Sistem Komputer) | CoCu 1: Computer System Set-up (Persediaan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE JOB REQUEST/CHANGE ORDER · PREPARE COMPUTER SET-UP TOOLS, HARDWARE PARTS AND SOFTWARE · SET-UP COMPUTER HARDWARE · CARRY OUT COMPUTER SOFTWARE INSTALLATION · SET-UP COMPUTER PERIPHERALS · CARRY OUT UNIT FUNCTIONALITY TEST · PREPARE COMPUTER SYSTEM SET-UP REPORT | ANALYSE JOB REQUEST/CHANGE ORDER · PREPARE COMPUTER SET-UP TOOLS, HARDWARE PARTS AND SOFTWARE · SET-UP COMPUTER HARDWARE · CARRY OUT COMPUTER SOFTWARE INSTALLATION · SET-UP COMPUTER PERIPHERALS · CARRY OUT UNIT FUNCTIONALITY TEST · PREPARE COMPUTER SYSTEM SET-UP REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 1 / P(1/7) | PAGE: 1 - 22 |


| SET-UP CONTEXT | DESKTOP / STANDARD BUILD | WORKSTATION / CUSTOM BUILD |
|----------------|--------------------------|----------------------------|
| Job request | Standard office build: single PC, standard OS and applications, one user. Job request specifies model, OS version, and software list. | Custom or workstation build: high-end CPU/GPU, multiple drives, special software or dual-boot. Change request may specify hardware list, RAID, and software versions. |
| Tools and parts | Standard toolkit: screwdrivers, anti-static strap, USB installer. Parts from standard inventory; one system unit, monitor, keyboard, mouse. | Extended toolkit: multimeter, cable tester, thermal paste. Parts ordered per spec; multiple drives, expansion cards, or special peripherals. |
| Report | Set-up report with serial numbers, OS version, and user sign-off. | Set-up report with full hardware list, RAID config, software versions, and acceptance test result. |


| Type of Tools | Description |
|---------------|-------------|
| Screwdriver set (Phillips, flat, Torx) | The most used tools in computer set-up. Used to open the chassis, secure drives and expansion cards, and assemble or disassemble computer components. Phillips and flat heads are for general screws; Torx for manufacturer-specific screws on some brands. An anti-static wrist strap is recommended when handling boards to avoid electrostatic discharge (ESD) that can damage components. |
| Multimeter | Used to check power supply voltages (e.g. +3.3 V, +5 V, +12 V), continuity, and basic electrical safety before and after set-up. Ensures the PSU is within tolerance and that there are no short circuits before powering on the system. |
| Cable tester / LAN tester | Used to verify network cable wiring (e.g. straight-through, crossover) and connectivity. Confirms that each wire is correctly terminated and that the cable can carry signal. Essential when laying or repairing network cables. |
| Anti-static mat and wrist strap | Reduces electrostatic discharge (ESD) when handling motherboards, RAM, and other sensitive components. The wrist strap is worn and connected to a grounded point or the chassis; the mat provides a grounded surface for components. Never handle boards without grounding in dry environments. |
| USB bootable media / optical drive | Used to load the operating system and drivers during software installation. The installer is prepared on USB or disc according to the job request (e.g. Windows, Linux). Some systems require legacy boot or secure boot settings in BIOS/UEFI. |
| Label maker or tags | Used to label cables, ports, and assets for identification and reporting. Labels help during troubleshooting and when completing the set-up report with asset and serial information. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 10% | 30 | Analyse job request/change order | 9.0 | 21.0 | 30.0 |
| 15% | 45 | Prepare computer set-up tools, computer hardware parts and computer software | 13.5 | 31.5 | 45.0 |
| 30% | 90 | Set-up computer hardware | 27.0 | 63.0 | 90.0 |
| 20% | 60 | Carry out computer software installation | 18.0 | 42.0 | 60.0 |
| 10% | 30 | Set-up computer peripherals | 9.0 | 21.0 | 30.0 |
| 10% | 30 | Carry out unit functionality test | 9.0 | 21.0 | 30.0 |
| 5% | 15 | Prepare computer system set-up report | 4.5 | 10.5 | 15.0 |
| **100%** | **300** | | **90.0** | **210.0** | **300.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 1: Computer System Set-up (Persediaan Sistem Komputer) | CoCu 1: Computer System Set-up (Persediaan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE JOB REQUEST/CHANGE ORDER · PREPARE COMPUTER SET-UP TOOLS, HARDWARE PARTS AND SOFTWARE · SET-UP COMPUTER HARDWARE · CARRY OUT COMPUTER SOFTWARE INSTALLATION · SET-UP COMPUTER PERIPHERALS · CARRY OUT UNIT FUNCTIONALITY TEST · PREPARE COMPUTER SYSTEM SET-UP REPORT | ANALYSE JOB REQUEST/CHANGE ORDER · PREPARE COMPUTER SET-UP TOOLS, HARDWARE PARTS AND SOFTWARE · SET-UP COMPUTER HARDWARE · CARRY OUT COMPUTER SOFTWARE INSTALLATION · SET-UP COMPUTER PERIPHERALS · CARRY OUT UNIT FUNCTIONALITY TEST · PREPARE COMPUTER SYSTEM SET-UP REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 1 / P(1/7) | PAGE: 23 - 38 |


| Hardware Component | Description |
|--------------------|-------------|
| CPU (Central Processing Unit) | The processor that executes instructions. It must match the socket type of the motherboard (e.g. LGA1700, AM5). Thermal paste and a heatsink or fan are required; the paste fills microscopic gaps between the CPU and heatsink for efficient heat transfer. Incorrect installation can cause overheating and permanent damage. |
| RAM (Random Access Memory) | Temporary storage for running programs and data. Types include DDR5; capacity and speed must be compatible with the motherboard and CPU. Modules are installed in the correct slots (often pairs for dual-channel). Not fully seated or incompatible RAM can cause no POST or random crashes. |
| Motherboard | The main board that connects the CPU, RAM, storage, and peripherals. Form factor (e.g. ATX, micro-ATX) determines case compatibility. The BIOS or UEFI firmware is used to set boot order, secure boot, and hardware options. All other components connect to the motherboard. |
| Storage (HDD / SSD / NVMe) | HDD (hard disk drive) is used for bulk storage at lower cost; SSD and NVMe offer much faster boot and application load. Interface (SATA, M.2 PCIe Gen5) must match the motherboard. NVMe Gen5 drives use M.2 PCIe Gen5 slots and often require a standoff and screw for mounting. |
| Power supply unit (PSU) | Converts AC from the wall to DC and supplies the correct voltages to the motherboard and components. Wattage must meet the total system requirement (CPU, GPU, drives). Cabling must match the motherboard (e.g. 24-pin, 8-pin CPU, PCIe for GPU). Modular PSUs allow unused cables to be left off for better airflow. |
| Peripherals | Monitor, keyboard, mouse, printer, and other devices. Connected via USB, HDMI or DisplayPort, or legacy ports as specified in the job request. Drivers and settings (e.g. resolution, refresh rate) are configured during software installation and set-up. |

![RAID Level Comparison](images/raid-levels.png)

| Software Type | Description |
|---------------|-------------|
| Operating system (OS) | Windows, Linux, or other OS as per job request. Installation media (USB or disc) and a valid licence or key are required. The installer partitions the drive, copies files, and configures the initial user and settings. Updates and drivers are applied after the base install. |
| Drivers | Device drivers for the motherboard (chipset, LAN, audio), GPU, and peripherals. Often supplied by the OS or from the manufacturer website. Missing or wrong drivers can cause devices not to work or to perform poorly. Install in the order recommended by the manufacturer (e.g. chipset first). |
| Applications | Office, browser, antivirus, and other applications as specified in the change order or standard build. May be installed from media, network share, or app store. Licence keys and configuration (e.g. default browser, updates) are applied according to organisational policy. |
| System utilities and firmware | Built-in tools (disk management, device manager, task manager) and BIOS/UEFI firmware used to configure, monitor, and troubleshoot the system after installation. Firmware updates may be needed for hardware compatibility. Utilities are used during set-up to verify partitions, check device status, and confirm system performance before user handover. |


| Common Fault During Set-up | Cause | Action |
|----------------------------|-------|--------|
| No power / no POST | PSU not switched on, power cable loose, front-panel wires wrong, or PSU fault | Check power cable and switch; verify front-panel header; test with known-good PSU if needed |
| No display | Monitor not connected or wrong input; GPU not seated; RAM not seated | Check cable and input; reseat GPU and RAM; try onboard video if available |
| OS installer not booting | Boot order wrong; secure boot or legacy setting; corrupted USB | Set boot order in BIOS/UEFI; disable secure boot for some installers; recreate USB installer |
| Driver or device not working | Wrong or missing driver; driver not installed after OS | Install correct driver from manufacturer; run Windows Update or equivalent |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse job request/change order | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Prepare computer set-up tools, computer hardware parts and computer software | Know tools, parts, and materials needed | Gather and organize tools, parts, and materials | Practical observation of tool/material preparation; checklist verification | Photo/log of prepared toolkit; materials checklist |
| Set-up computer hardware | Understand installation procedures and hardware compatibility | Correctly assemble and install components according to specifications | Practical hands-on assembly; functionality test verification | Correctly assembled system; successful test results |
| Carry out computer software installation | Know procedures and troubleshooting techniques | Execute procedures and resolve issues | Practical demonstration; problem-solving observed | Completed task log; troubleshooting notes; final working state |
| Set-up computer peripherals | Understand installation procedures and hardware compatibility | Correctly assemble and install components according to specifications | Practical hands-on assembly; functionality test verification | Correctly assembled system; successful test results |
| Carry out unit functionality test | Know procedures and troubleshooting techniques | Execute procedures and resolve issues | Practical demonstration; problem-solving observed | Completed task log; troubleshooting notes; final working state |
| Prepare computer system set-up report | Know tools, parts, and materials needed | Gather and organize tools, parts, and materials | Practical observation of tool/material preparation; checklist verification | Photo/log of prepared toolkit; materials checklist |

## Practical Exercises

The following hands-on lab exercises develop the practical competencies required for Computer System Set-up. Each exercise is designed for L3 operational-level technicians and includes step-by-step procedures, required equipment, and assessment criteria aligned with NOSS standards.

### Lab 1.1: Analysing and Planning a Computer Build

**Objective:** Analyse a job request and plan the computer set-up sequence

**Duration:** 45 minutes

**Equipment Required:**
Job request template, Customer specifications sheet, Hardware checklist, Parts inventory list, Scheduling tool

**Procedures:**
1. Receive a simulated job request specifying CPU model, RAM capacity, storage type, and software requirements
2. Extract and verify all customer requirements from the job request
3. Cross-check hardware specifications against supplier inventory
4. Create a logical set-up sequence (order of installation steps)
5. Identify any missing parts or incompatibilities and document actions
6. Prepare a bill of materials and tools checklist
7. Document the analysis in a structured format for team review

**Expected Outcome:**
Completed analysis showing identified requirements, compatibility verification, and set-up plan

**Assessment Checklist:**
- [ ] Job request completely read and understood
- [ ] All hardware specifications extracted and verified
- [ ] Incompatibilities or gaps identified
- [ ] Set-up sequence documented in logical order
- [ ] Bill of materials prepared
- [ ] Analysis signed off for proceeding to set-up

### Lab 1.2: Gathering and Organizing Set-up Materials

**Objective:** Prepare and organize all tools, hardware, and software required for set-up

**Duration:** 30 minutes

**Equipment Required:**
Full technician toolkit, Hardware components, Anti-static mat and wrist strap, USB installer, Software media, Labelling equipment

**Procedures:**
1. Gather all tools from the workshop: screwdrivers, multimeter, cable tester, anti-static strap, thermal paste
2. Retrieve required hardware components from inventory: CPU, RAM, storage, motherboard, power supply, peripherals
3. Prepare OS and driver media (USB installers, disc if required)
4. Set up anti-static mat in the work area and verify grounding
5. Organize all materials in a logical sequence for installation
6. Create a checklist confirming all items are present and functional
7. Label cables, connectors, and components for easy identification during installation

**Expected Outcome:**
Organized workspace with all tools and materials ready, verified checklist, and labelled components

**Assessment Checklist:**
- [ ] Toolkit is complete and tools are functional
- [ ] All hardware components are present and undamaged
- [ ] Software media is prepared and bootable
- [ ] Anti-static precautions are in place
- [ ] Workspace is organized and clear
- [ ] All items verified on equipment checklist

### Lab 1.3: Hardware Assembly and Installation

**Objective:** Assemble and install computer hardware components correctly

**Duration:** 90 minutes

**Equipment Required:**
Computer case, Motherboard, CPU with heatsink, RAM, Storage drives, Power supply, Expansion cards, Cable management supplies

**Procedures:**
1. Install the motherboard in the case, using correct standoffs and screws
2. Install the CPU with thermal paste and cooler, following manufacturer specifications
3. Install RAM modules in correct slots (verify dual-channel configuration if applicable)
4. Install storage devices (HDD/SSD/NVMe Gen5) in appropriate bays and slots
5. Connect all power connectors: 24-pin motherboard, 8-pin CPU, PCIe for GPU if present
6. Connect SATA, SSD, or NVMe Gen5 data cables (if using SATA, SSD, or NVMe Gen5 drives) or verify NVMe Gen5 seating
7. Organize and secure cables to avoid obstruction of airflow
8. Verify all components are properly seated and secured
9. Do not power on yet—prepare for BIOS checks

**Expected Outcome:**
Fully assembled computer with all components correctly installed and cables organized

**Assessment Checklist:**
- [ ] Motherboard is properly seated and secured
- [ ] CPU is installed with thermal paste and cooler attached
- [ ] RAM is installed in correct slots and fully seated
- [ ] Storage devices are installed and connected
- [ ] All power connectors are connected and secure
- [ ] Cables are organized and do not block airflow
- [ ] No loose screws or components remain

### Lab 1.4: Operating System and Driver Installation

**Objective:** Install the operating system and drivers to bring the system to working state

**Duration:** 75 minutes

**Equipment Required:**
Assembled computer from Lab 1.3, OS USB installer, Driver media/downloads, Monitor and peripherals

**Procedures:**
1. Connect monitor, keyboard, and mouse; power on the system
2. Enter BIOS/UEFI to verify hardware detection (check CPU, RAM, storage)
3. Set boot order to USB and enable/disable secure boot as needed for OS installer
4. Boot from USB installer and follow OS installation prompts
5. Partition the storage drive according to job requirements
6. Complete base OS installation and initial configuration
7. Install chipset drivers from manufacturer support site or media
8. Install GPU, network, audio, and other device drivers in correct order
9. Apply Windows updates or OS patches
10. Verify all devices are recognized in Device Manager and no unknown devices remain

**Expected Outcome:**
Working computer with OS installed and all drivers recognized; Device Manager shows no errors

**Assessment Checklist:**
- [ ] OS installed successfully and boots without errors
- [ ] All hardware detected in BIOS and OS
- [ ] All device drivers installed (no unknown devices)
- [ ] Network and audio working
- [ ] No driver errors in Device Manager
- [ ] System stable for initial testing

### Lab 1.5: Peripheral Connection and Configuration

**Objective:** Connect and configure peripheral devices (monitor, keyboard, mouse, printer) correctly

**Duration:** 30 minutes

**Equipment Required:**
Installed computer from Lab 1.4, Monitor, Keyboard, Mouse, Printer (optional), USB peripherals

**Procedures:**
1. Verify monitor is connected with correct cable (HDMI, DisplayPort, DVI)
2. Set monitor resolution and refresh rate in OS display settings to match hardware capability
3. Connect keyboard and mouse via USB and verify device detection
4. Install printer driver if a printer is part of the job request
5. Connect printer via USB or network and verify it appears in Devices and Printers
6. Test each peripheral: type with keyboard, move mouse, send test print if applicable
7. Configure peripheral settings (keyboard layout, mouse sensitivity, printer defaults)

**Expected Outcome:**
All peripherals connected, recognized, and functioning correctly

**Assessment Checklist:**
- [ ] Monitor connected and resolution correct
- [ ] Keyboard responds and is recognized
- [ ] Mouse responds and is recognized
- [ ] Printer (if applicable) installed and ready
- [ ] All peripherals visible in Device Manager with no errors

### Lab 1.6: System Functionality and Stability Testing

**Objective:** Perform comprehensive testing to verify the system is stable and ready for user handover

**Duration:** 45 minutes

**Equipment Required:**
Fully configured system from Lab 1.5, System utilities (Windows, Linux built-in tools), Multimeter (optional)

**Procedures:**
1. Power on the system and observe boot sequence for any errors or warnings
2. Log in and verify user account creation
3. Run Device Manager and check for any unknown or error devices
4. Use system utilities to check disk status: Run Check Disk (chkdsk) or equivalent
5. Monitor CPU and RAM usage during normal operations using Task Manager or top command
6. Test network connectivity by opening a browser and visiting a website
7. Copy a test file to storage and verify read/write speeds are acceptable
8. Launch one or two applications (office, browser) specified in the job and verify they open correctly
9. Stress-test the system briefly (e.g., run antivirus scan or CPU-intensive tool for 5 minutes)
10. Check temperatures using BIOS monitoring or system utilities; ensure CPU/GPU temps are in normal range
11. Document test results on the functionality test checklist

**Expected Outcome:**
All system tests pass; system is stable, all devices respond, and no errors are logged

**Assessment Checklist:**
- [ ] System boots without errors
- [ ] User account is functional
- [ ] All hardware is recognized with no unknown devices
- [ ] Disk check completed with no errors
- [ ] CPU and RAM are operating within expected parameters
- [ ] Network connectivity confirmed
- [ ] Applications launch and respond normally
- [ ] System remains stable under load
- [ ] CPU and GPU temperatures are within safe range

### Lab 1.7: Documentation and Set-up Report Completion

**Objective:** Complete comprehensive documentation of the set-up for user handover and future reference

**Duration:** 30 minutes

**Equipment Required:**
Tested computer, Set-up report template, Camera or photo capture device, Pen/signature area

**Procedures:**
1. Gather serial numbers and product keys from all hardware components
2. Record installed OS version, edition, and licence key (if applicable)
3. Document all installed drivers and applications with versions
4. Record BIOS/UEFI settings (boot order, secure boot, XMP, TPM status) that differ from defaults
5. Capture a screenshot of Device Manager showing all recognized hardware
6. Take photos of hardware configuration and cable organization for future reference
7. Record RAM configuration (total capacity, speed, dual-channel status)
8. Record storage configuration (drive types, total capacity, partition layout)
9. Document any deviations from the original job request or changes made during set-up
10. Complete the set-up checklist with sign-off from a senior technician
11. Prepare handover notes for the user (user guide, support contact information)

**Expected Outcome:**
Complete set-up report with all hardware details, software versions, test results, and user sign-off

**Assessment Checklist:**
- [ ] All hardware serial numbers and specs recorded
- [ ] OS version and licence recorded
- [ ] All drivers and applications documented with versions
- [ ] Non-default BIOS settings recorded
- [ ] Hardware photos and Device Manager screenshot attached
- [ ] System configuration diagram or notes prepared
- [ ] Any deviations from job request explained
- [ ] Technician sign-off obtained
- [ ] User handover notes prepared



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Activity:** Prepare computer system set-up report
- **Mapping:** Write clear technical documentation; prepare reports showing hardware configurations, software versions, and test results for user handover and quality assurance

### 2. Teamwork & Collaboration
- **Activities:** Analyse job request/change order, Prepare computer set-up tools and hardware
- **Mapping:** Coordinate with help desk and other technicians; clarify user requirements from job requests; work together when sourcing parts and tools

### 3. Problem-solving
- **Activities:** Carry out computer software installation, Carry out unit functionality test
- **Mapping:** Diagnose and resolve installation failures, driver issues, and hardware compatibility problems; troubleshoot boot failures and hardware conflicts

### 4. Initiative & Self-reliance
- **Activities:** Set-up computer hardware, Set-up computer peripherals
- **Mapping:** Work independently to assemble and configure systems; take personal responsibility for checking component compatibility and installation accuracy

### 5. Planning & Organizing
- **Activities:** Analyse job request/change order, Prepare computer set-up tools and hardware
- **Mapping:** Plan the logical sequence of setup tasks; organize tools and components before starting; follow correct installation order (chipset drivers, then device drivers)

### 6. Self-management & Safety Awareness
- **All activities, especially those involving electrical equipment**
- **Mapping:** Follow ESD protocols and electrical safety practices; manage time to meet deadlines; maintain organized workspace and documentation

### 7. Technology Use & Technical Proficiency
- **All activities requiring hands-on work with hardware and software**
- **Mapping:** Use multimeters, cable testers, and diagnostic tools; configure BIOS/UEFI settings; install and configure OS and drivers; troubleshoot using system utilities

### 8. Learning Skills & Continuous Improvement
- **All activities; especially relevant for new hardware platforms and OS versions**
- **Mapping:** Stay current with new hardware standards and driver updates; learn from installation failures; apply lessons to improve future procedures


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
- **Punctuality and Reliability:** Complete system set-up work on schedule to meet user handover deadlines and support business operations.
- **Integrity in Documentation:** Prepare accurate and complete set-up reports with all hardware details, software versions, and test results. Honest documentation supports future troubleshooting and maintains system integrity.
- **Teamwork and Support:** Collaborate with help desk staff and other technicians; share knowledge about system configurations and troubleshooting techniques to improve overall technical capability.
- **Attention to Detail:** Verify every connection, configuration setting, and test result to ensure systems are correctly set up and function as intended.

## References

**Official Standards and Frameworks:**

- Malaysian Standard MS 1546-1:2003 – Code of Practice for Information Security Management
- NOSS IT-020-3:2013 Computer System Operation Syllabus
- Dell PowerEdge Documentation – Server Hardware Installation and Configuration
- Intel ARK Processor Specifications – Socket Compatibility and Thermal Design Power
- JEDEC DDR5 Memory Standard – Performance Profiles and Compatibility Guidelines

**Technical References and Best Practices:**

- CompTIA A+ Certification Study Guide – Hardware Installation and Troubleshooting
- Linus Torvalds et al. (2024). Linux Kernel Documentation – UEFI Booting
- Microsoft Windows Server 2025 Installation and Configuration Guide
- American Megatrends (AMI) BIOS/UEFI Setup Documentation
- Institute of Electrical and Electronics Engineers (IEEE) 802.3 Network Standards

**Contact hour:** [[00_Contact-hour_IT-020-3-L3-Operation]]


---

↑ [README](../../README.md) · **IT-020-3** > CoCu 1 - Computer System Set-up

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-3-L3-Operation.md) · [00_standard-practice](00_standard-practice.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Maintenance.md) · [03_CoCu-3](03_CoCu-3-Computer-System-Repair.md) · [04_CoCu-4](04_CoCu-4-Server-Installation.md) · [05_CoCu-5](05_CoCu-5-Server-Maintenance.md) · [06_CoCu-6](06_CoCu-6-Computer-Network-Connectivity-Set-up.md) · [07_CoCu-7](07_CoCu-7-Mobile-Device-Configuration.md)

**Other levels:** [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
