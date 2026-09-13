# CoCu 3: Computer System Repair (180 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 3: Computer System Repair (Pembaikan Sistem Komputer) | CoCu 3: Computer System Repair (Pembaikan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST · CARRY OUT ONLINE TROUBLESHOOTING · PERFORM ON-SITE REPAIR · PREPARE COMPUTER STATUS REPORT | ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST · CARRY OUT ONLINE TROUBLESHOOTING · PERFORM ON-SITE REPAIR · PREPARE COMPUTER STATUS REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 3 / P(3/7) | PAGE: 53 - 64 |


| SET-UP CONTEXT | ONLINE TROUBLESHOOTING | ON-SITE REPAIR |
|----------------|------------------------|----------------|
| Job request | Fault report from user describing symptoms (error message, no boot, slow performance). Initial assessment determines whether the fault can be resolved remotely. Job order includes asset ID, user contact, fault description, and priority. | Escalated from online troubleshooting when remote steps have not resolved the fault, or when hardware failure is suspected. Job order includes online troubleshooting history, fault description, and parts or tools likely needed. |
| Tools and parts | Phone or communication tool, remote desktop or remote support software, knowledge base, diagnostic scripts, and event log access. No physical parts needed. | Full toolkit: screwdrivers, multimeter, anti-static strap, spare parts (RAM, PSU, disk, cables), USB bootable media, and diagnostic software. Parts drawn from inventory based on the diagnosed fault. |
| Report | Record fault description, steps taken remotely, diagnostic findings, and outcome (resolved, pending, or escalated to on-site). | Computer status report with fault description, on-site actions taken, parts used (with serial numbers), test result, and recommendation (follow-up, disposal, or user training). |


| Type of Tools | Description |
|---------------|-------------|
| Phone / communication tool | Used to gather symptoms from the user, guide them step-by-step (e.g. restart, safe mode, check cables), and confirm the outcome. Clear questions and simple instructions reduce repeat visits. Document what the user reports and what was tried for the status report. |
| Remote desktop / remote support tool | Used when the user can boot and connect to the network: view their screen, run diagnostics (event log, disk check, memory test), remove malware or bad drivers, and apply fixes without visiting. Requires user permission and network access; document all steps for the status report. |
| Knowledge base / diagnostic scripts | Used to look up error codes, beep codes, and known fixes; run scripted checks (e.g. disk SMART, memory test) to narrow the fault. Speeds up both online and on-site repair and ensures consistent procedure across technicians. |
| Screwdriver set and anti-static strap | Used to open the chassis, replace RAM, GPU, PSU, or drives during on-site repair. Anti-static strap is worn and connected to a grounded point when handling boards to avoid ESD damage. Essential for any hardware replacement. |
| Multimeter | Used to check PSU voltages (+3.3 V, +5 V, +12 V), continuity, and power at the connector. Confirms PSU fault before replacement and checks front-panel wiring. Helps isolate electrical faults that are not visible. |
| Spare parts and USB installer | Known-good RAM, PSU, or disk for swap testing; USB bootable media for OS reinstall or recovery. Verify compatibility (socket, form factor, interface) before use; record serial numbers for the status report. Swap testing isolates the faulty component by replacing one part at a time. |
| Diagnostic software | Memory test (e.g. Memtest86), disk SMART tools, event log viewer, and temperature monitors. Run after repair to verify stability and document the test result in the computer status report. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 10% | 18 | Assess computer repair job order/change request | 5.4 | 12.6 | 18.0 |
| 30% | 54 | Carry out online trouble shooting | 16.2 | 37.8 | 54.0 |
| 50% | 90 | Perform on-site repair | 27.0 | 63.0 | 90.0 |
| 10% | 18 | Prepare computer status report | 5.4 | 12.6 | 18.0 |
| **100%** | **180** | | **54.0** | **126.0** | **180.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 3: Computer System Repair (Pembaikan Sistem Komputer) | CoCu 3: Computer System Repair (Pembaikan Sistem Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST · CARRY OUT ONLINE TROUBLESHOOTING · PERFORM ON-SITE REPAIR · PREPARE COMPUTER STATUS REPORT | ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST · CARRY OUT ONLINE TROUBLESHOOTING · PERFORM ON-SITE REPAIR · PREPARE COMPUTER STATUS REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 3 / P(3/7) | PAGE: 65 - 72 |

![Computer System Troubleshooting Flowchart](images/troubleshooting-flowchart.png)

| Hardware Component | Description |
|--------------------|-------------|
| POST (Power-On Self-Test) | Firmware checks run at boot that test RAM, drives, keyboard, and other devices. Beep codes or on-screen codes indicate which check failed. Consult the motherboard or system manual for the meaning of codes. No beep or no display often points to PSU, motherboard, RAM, or CPU failure. Understanding POST is essential for on-site diagnosis before opening the chassis. |
| Power supply unit (PSU) | Converts AC to DC and supplies voltages to the motherboard and components. A failed or degrading PSU may cause no power, random shutdowns, or instability. Use a multimeter to check +3.3 V, +5 V, and +12 V rails at the connector. Replace with a unit of equal or greater wattage and matching connector types. Record the replacement part serial number in the status report. |
| RAM modules | Temporary storage for running programs. Faulty RAM causes no POST, random crashes, or blue screens. Run Memtest86 or Windows Memory Diagnostic to confirm. During on-site repair, reseat modules first; if the fault persists, test each stick individually in a known-good slot. Replace faulty modules with compatible type (DDR5) and speed. |
| Storage drives (HDD / SSD / NVMe) | Failed or failing drives cause no boot, data loss, or slow performance. Check SMART data for warnings (reallocated sectors, pending sectors). Back up data if possible before replacement. Replace with a compatible drive and reinstall the OS or restore from backup. Record the old and new drive serial numbers. |


| Software Component | Description |
|---------------------|-------------|
| Safe mode / recovery environment | The OS loads with minimal drivers and services. Used to isolate software versus hardware faults and to remove malware or bad drivers. Recovery options (e.g. Windows Recovery Environment) allow restore point, system repair, or full reinstall. Accessible via boot menu or installation media. |
| Event log and minidump analysis | Windows Event Viewer (Application and System logs) and minidump files record errors, warnings, and crash details. Review these during online troubleshooting to identify the failing component or driver. Repeated errors for the same source suggest a persistent fault that requires corrective action. |
| Replacement parts compatibility | Use parts that match the system's specifications: same socket, form factor, interface, and supported speed. Check the motherboard or system manual before ordering. Record serial numbers and warranty information for the status report. Verify compatibility before swap testing to avoid introducing new faults. |
| Backup verification | Before performing destructive repairs (OS reinstall, disk replacement), verify that a current backup exists and is restorable. Backup tools include Windows Backup, cloud sync (OneDrive, Google Drive), and external media. Confirming backup status protects the user's data and reduces the risk of data loss during repair. |


| Computer Status Report | Description |
|------------------------|-------------|
| Fault description | Clear statement of the reported fault and observed symptoms during diagnosis. Accurate fault descriptions allow future technicians to recognise recurring patterns and speed up diagnosis of similar issues. This record also provides evidence for management when deciding whether to repair or replace an aging asset. |
| Actions taken | All steps performed during online troubleshooting and on-site repair, in sequence. Documenting each step in order prevents repeated work if another technician takes over and provides a reference for similar faults in the future. This also demonstrates due diligence and compliance with the organisation's repair procedures. |
| Parts used | Part numbers, serial numbers, and quantities of replacement components. Recording serial numbers ties each part to a specific asset for warranty tracking and audit purposes. This information also supports inventory management by updating stock records and enabling cost analysis per repair. |
| Test result | Outcome of post-repair testing (POST, boot, diagnostics, stress test if required). Documenting test results provides evidence that the system was verified as functional before being returned to the user. If the fault recurs, the previous test results help narrow down whether the original repair was effective or a different component is now failing. |
| Recommendation | Follow-up actions such as monitoring, user training, further repair, or disposal. Recommendations guide management in planning next steps, such as scheduling a follow-up check or budgeting for a replacement. Including user training suggestions helps reduce repeat fault reports caused by operator error. |


| Common Fault | Cause | Action |
|--------------|-------|--------|
| No power / no POST | PSU fault, loose power cable, wrong front-panel wiring, or motherboard failure | Check cable and switch; verify front-panel header; test PSU with multimeter; replace or escalate |
| No display | Loose or wrong cable, wrong monitor input, GPU or RAM not seated, or faulty GPU | Check cable and input; reseat GPU and RAM; try onboard video if available |
| Blue screen / crash | Driver conflict, faulty RAM, or disk error; overheating | Check event log and minidump; run memory and disk test; check temperatures |
| Slow or freezing | Malware, too many startup programs, low RAM, or failing disk | Scan for malware; check startup programs and RAM usage; check SMART and disk health |
| No boot / corrupted OS | Failed disk, bad OS update, or malware damage | Attempt repair via recovery environment; reinstall OS; replace disk if SMART shows failure; restore from backup |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Assess computer repair job order/change request | Understand concepts related to: Assess computer repair job order/change request | Successfully execute: Assess computer repair job order/change request | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Carry out online trouble shooting | Know procedures and troubleshooting techniques | Execute procedures and resolve issues | Practical demonstration; problem-solving observed | Completed task log; troubleshooting notes; final working state |
| Perform on-site repair | Understand concepts related to: Perform on-site repair | Successfully execute: Perform on-site repair | Practical demonstration and documentation review | Completed task documentation and supervisor sign-off |
| Prepare computer status report | Know tools, parts, and materials needed | Gather and organize tools, parts, and materials | Practical observation of tool/material preparation; checklist verification | Photo/log of prepared toolkit; materials checklist |

## Practical Exercises

The following hands-on lab exercises develop the practical competencies required for Computer System Repair. Each exercise is designed for L3 operational-level technicians and includes step-by-step procedures, required equipment, and assessment criteria aligned with NOSS standards.

### Lab 3.1: Fault Analysis and Diagnosis

**Objective:** Analyse a system fault report and develop a repair strategy

**Duration:** 45 minutes

**Equipment Required:**
Faulty computer system, Diagnostics software, Hardware reference guides, Multimeter

**Procedures:**
1. Receive a fault report describing symptoms (no power, slow performance, error messages)
2. Ask clarifying questions: when did it start, what was the last action before failure
3. Run diagnostics software to identify failing components
4. Check event logs for clues about the fault cause
5. Use a multimeter to check power supply voltages if power-related
6. Develop a repair strategy addressing the root cause
7. Document the analysis and proposed repair steps

**Expected Outcome:**
Fault analysis report with diagnosed problem and proposed repair plan

**Assessment Checklist:**
- [ ] Symptoms documented
- [ ] Diagnostics run successfully
- [ ] Logs reviewed for errors
- [ ] Root cause identified
- [ ] Repair strategy documented
- [ ] Required parts/tools listed

### Lab 3.3: Remote Troubleshooting and Online Support

**Objective:** Perform remote troubleshooting to diagnose and resolve computer faults

**Duration:** 45 minutes

**Equipment Required:**
Customer computer (remote access), Remote support software, Knowledge base or diagnostic scripts, Phone or chat for communication

**Procedures:**
1. Contact the user and gather detailed symptom information (error messages, when it started, what was the last action)
2. Ask the user to check basic connectivity (network, power, cables)
3. Request remote desktop access or use remote support software to view the user's screen
4. Run diagnostics remotely: open Event Viewer, check Device Manager, run memory test if available
5. Guide the user through basic troubleshooting steps: restart, Safe Mode boot, check cables
6. Look up error codes in knowledge base and apply known fixes
7. If remotely fixable, apply the fix and confirm resolution with the user
8. If hardware fault is likely, escalate to on-site repair and document findings

**Expected Outcome:**
Fault diagnosed; issue resolved remotely or escalated with documentation for on-site repair

**Assessment Checklist:**
- [ ] Symptom information fully documented
- [ ] Remote access established
- [ ] Diagnostics run and logs reviewed
- [ ] Troubleshooting steps documented
- [ ] Issue resolved OR escalated with clear handoff
- [ ] User confirmation obtained

### Lab 3.2: Hardware Component Replacement and On-site Repair

**Objective:** Replace a faulty hardware component and verify repair success

**Duration:** 60 minutes

**Equipment Required:**
Computer with faulty component, Replacement component, Screwdrivers, Anti-static strap, Thermal paste (if CPU/heatsink)

**Procedures:**
1. Power off and unplug the computer
2. Ground yourself with an anti-static strap
3. Identify the faulty component location in the system
4. Remove any screws or clips holding the component
5. Carefully extract the faulty component
6. Inspect the replacement component for any visible damage
7. Install the replacement component securely
8. Reapply thermal paste if replacing CPU or GPU heatsink
9. Power on and verify the system boots correctly
10. Run diagnostics to confirm the fault is resolved

**Expected Outcome:**
System repaired with faulty component replaced and verified working

**Assessment Checklist:**
- [ ] Faulty component identified and removed safely
- [ ] Replacement component installed correctly
- [ ] System boots without errors
- [ ] Diagnostics pass
- [ ] All cables reconnected properly
- [ ] Repair verified complete

### Lab 3.4: Computer Status Report and Repair Documentation

**Objective:** Complete comprehensive computer status report documenting repair activities and outcomes

**Duration:** 30 minutes

**Equipment Required:**
Repaired computer, Status report template, Pen and paper or text editor, Camera (optional for photos)

**Procedures:**
1. Record the original fault description and symptoms from the job order
2. Document online troubleshooting steps performed and findings (if applicable)
3. Record on-site repair actions taken and components accessed or replaced
4. List replaced hardware with part numbers and serial numbers for inventory tracking
5. Record technician time spent on diagnosis and repair
6. Include test results (temperature readings, diagnostics) confirming repair success
7. Note any warranty, service tags, or asset ID labels applied
8. Add recommendation: follow-up maintenance, user training, or hardware upgrade suggestions
9. Obtain user or supervisor sign-off if required by policy

**Expected Outcome:**
Complete status report documenting initial fault, troubleshooting, repair actions, parts used, test results, and recommendations

**Assessment Checklist:**
- [ ] Fault description clear and complete
- [ ] Troubleshooting steps documented
- [ ] On-site repair actions detailed
- [ ] Parts replaced with serial numbers recorded
- [ ] Test results showing success
- [ ] Recommendations included
- [ ] Report signed and dated



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Activity:** Prepare computer status report
- **Mapping:** Document repair work clearly; explain faults and solutions to users and supervisors; prepare status reports with findings and recommendations

### 2. Teamwork & Collaboration
- **Activities:** Assess computer repair job order, Carry out online troubleshooting
- **Mapping:** Work with help desk and support staff; escalate complex issues appropriately; ask technical experts for advice on difficult repairs

### 3. Problem-solving
- **Activities:** Carry out online troubleshooting, Perform on-site repair
- **Mapping:** Diagnose root causes using systematic troubleshooting; isolate hardware vs software issues; use event logs, diagnostics, and multimeters to identify faults

### 4. Initiative & Self-reliance
- **Activities:** Assess computer repair job order, Perform on-site repair
- **Mapping:** Take responsibility for repair decisions; work independently to resolve on-site issues; manage user expectations and communicate timelines

### 5. Planning & Organizing
- **Activities:** Assess computer repair job order, Carry out troubleshooting
- **Mapping:** Plan troubleshooting sequence logically; organize tools and spare parts for on-site visits; prioritize high-impact repairs

### 6. Self-management & Safety Awareness
- **All repair activities, especially those involving electrical components**
- **Mapping:** Work safely with multimeters and power supplies; manage time to complete repairs efficiently; maintain composure when troubleshooting complex issues; follow safety protocols for on-site work

### 7. Technology Use & Technical Proficiency
- **All activities requiring diagnostic and repair skills**
- **Mapping:** Use multimeters, diagnostic software, and event viewers; interpret SMART data and memory test results; perform hands-on repairs with precision

### 8. Learning Skills & Continuous Improvement
- **All activities; especially relevant for new hardware and error patterns**
- **Mapping:** Learn new troubleshooting techniques; stay informed on common hardware failures and malware signatures; analyze repair cases to improve future efficiency


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
- **Punctuality and Reliability:** Complete system repair work on schedule to meet user handover deadlines and support business operations.
- **Integrity in Documentation:** Prepare accurate and complete repair status reports with all hardware details, software versions, and test results. Honest documentation supports future troubleshooting and maintains system integrity.
- **Teamwork and Support:** Collaborate with help desk staff and other technicians; share knowledge about system configurations and troubleshooting techniques to improve overall technical capability.
- **Attention to Detail:** Verify every connection, configuration setting, and test result to ensure repair tasks are completed correctly and systems function as intended.

## References

**Official Standards and Frameworks:**

- NOSS IT-020-3:2013 Computer System Operation Syllabus
- Intel and AMD Processor Replacement and RMA Procedures
- HP ProDesk and ProLiant Hardware Service Bulletins
- Troubleshooting and Diagnostics Guide – Windows Memory Diagnostics, memtest86
- Seagate and Western Digital HDD Diagnostic Tools and RMA Procedures

**Technical References and Best Practices:**

- Samsung and SK Hynix SSD SMART Monitoring and Data Recovery Guidelines
- BIOS/UEFI Diagnostics and Hardware Test Procedures
- CompTIA A+ Troubleshooting Methodology (CompTIA A+ 220-1001/1002)
- Linux Hardware Diagnostics – dmidecode, lspci, lsusb Utilities
- NZXT and Corsair Liquid Cooling System Maintenance and Repair Guides

**Contact hour:** [[00_Contact-hour_IT-020-3-L3-Operation]]


---

↑ [README](../../README.md) · **IT-020-3** > CoCu 3 - Computer System Repair

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-3-L3-Operation.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Computer-System-Set-up.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Maintenance.md) · [04_CoCu-4](04_CoCu-4-Server-Installation.md) · [05_CoCu-5](05_CoCu-5-Server-Maintenance.md) · [06_CoCu-6](06_CoCu-6-Computer-Network-Connectivity-Set-up.md) · [07_CoCu-7](07_CoCu-7-Mobile-Device-Configuration.md)

**Other levels:** [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
