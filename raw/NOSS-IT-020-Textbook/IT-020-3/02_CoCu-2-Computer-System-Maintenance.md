---
title: "CoCu 2: Computer System Maintenance (120 hrs)"
date: 2026-02-07
tags:
  - project
  - education
  - noss
project: "NOSS"
status: active
---

# CoCu 2: Computer System Maintenance (120 hrs)

*Layout follows Kitchen LV2 C01.txt: PROGRAM CODE, LEVEL, UNIT TITLE, numbered WORK ACTIVITY STATEMENT, NO. CODE, PAGE.*

|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION | IT-020-3:2013 COMPUTER SYSTEM OPERATION |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 2: Computer System Maintenance | CoCu 2: Computer System Maintenance |
| NO. AND WORK ACTIVITY STATEMENT | **1.** IDENTIFY COMPUTER MAINTENANCE REQUIREMENTS **2.** CARRY OUT COMPUTER SCHEDULED PREVENTIVE MAINTENANCE **3.** PERFORM COMPUTER CORRECTIVE MAINTENANCE **4.** PREPARE COMPUTER MAINTENANCE REPORT | **1.** IDENTIFY COMPUTER MAINTENANCE REQUIREMENTS **2.** CARRY OUT COMPUTER SCHEDULED PREVENTIVE MAINTENANCE **3.** PERFORM COMPUTER CORRECTIVE MAINTENANCE **4.** PREPARE COMPUTER MAINTENANCE REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 2 / P(2/7) | PAGE: 39 - 48 |


| Type of Maintenance | Description |
|--------------------|-------------|
| Preventive (scheduled) | Planned tasks carried out at regular intervals to reduce failures and extend equipment life. Includes cleaning dust from vents and heatsinks, checking fans and temperatures, updating the OS and antivirus, verifying backups, and checking cables and connectors. A maintenance schedule is followed (e.g. monthly, quarterly) and findings are recorded. |
| Corrective | Carried out after a fault or failure. The cause is diagnosed (e.g. failed fan, faulty RAM, corrupted OS), the faulty part is replaced or repaired, software is reinstalled or reconfigured as needed, and the system is retested. All actions and parts used are documented in the maintenance report. |

| Type of Tools (Maintenance) | Description |
|-----------------------------|-------------|
| Compressed air / blower | Used to remove dust from vents, heatsinks, fans, and inside the chassis without touching components. Hold fans still while blowing to avoid overspinning and damaging bearings. Use short bursts; do not use near eyes or mouth. In dusty environments, schedule cleaning more often. |
| Soft brush (anti-static) | Used with compressed air to loosen dust from heatsinks and fan blades. A small brush helps reach tight spaces. Anti-static brushes reduce risk of ESD when working near boards. Never use a vacuum directly on the motherboard—suction can generate static and damage components. |
| Thermal paste / compound | Applied between the CPU and heatsink to improve heat transfer. Degrades over time; reapply when reseating the heatsink or after several years. Use a small pea-sized amount in the centre; spread evenly or let pressure distribute. Excess paste can cause mess and poor contact; clean old paste with isopropyl alcohol before reapplying. |
| Isopropyl alcohol (IPA) and lint-free cloth | Used to clean old thermal paste from the CPU and heatsink before applying new paste. High concentration (90%+) evaporates quickly and leaves no residue. Wipe gently; allow to dry before applying new paste and reseating the heatsink. |
| Screwdriver set and anti-static strap | Same as in set-up: open chassis, remove heatsink, and secure components. Anti-static strap is worn and connected to a grounded point when handling RAM, boards, or CPU to avoid ESD damage during corrective maintenance. |
| Temperature and diagnostics software | Used to check CPU, GPU, and disk temperatures and to view SMART data and event logs. Helps identify overheating or failing hardware before failure and supports evidence for maintenance reports. |

![Cleaning PC interior with compressed air](images/maintenance-compressed-air.jpg)

| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 15% | 18 | Identify computer maintenance requirements | 5.4 | 12.6 | 18.0 |
| 40% | 48 | Carry out computer scheduled preventive maintenance | 14.4 | 33.6 | 48.0 |
| 40% | 48 | Perform computer corrective maintenance | 14.4 | 33.6 | 48.0 |
| 5% | 6 | Prepare computer maintenance report | 1.8 | 4.2 | 6.0 |
| **100%** | **120** | | **36.0** | **84.0** | **120.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION | IT-020-3:2013 COMPUTER SYSTEM OPERATION |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 2: Computer System Maintenance | CoCu 2: Computer System Maintenance |
| NO. AND WORK ACTIVITY STATEMENT | **1.** IDENTIFY COMPUTER MAINTENANCE REQUIREMENTS **2.** CARRY OUT COMPUTER SCHEDULED PREVENTIVE MAINTENANCE **3.** PERFORM COMPUTER CORRECTIVE MAINTENANCE **4.** PREPARE COMPUTER MAINTENANCE REPORT | **1.** IDENTIFY … **2.** CARRY OUT … **3.** PERFORM … **4.** PREPARE … |
| NO. CODE | IT-020-3:2013 - CoCu 2 / P(2/7) | PAGE: 49 - 52 |


| Key Term | Description |
|----------|-------------|
| Dust and airflow | Dust blocks vents and heatsinks and causes overheating. The system should be powered off and unplugged before cleaning. Use compressed air and a soft brush; avoid vacuum directly on boards to reduce static risk. Clean fans, vents, and heatsinks according to the schedule. |
| Thermal paste | The compound between the CPU and heatsink that improves heat transfer. It degrades over time. Reapply when reseating the heatsink or after several years of use. Use a small amount in the centre; excess can cause mess and poor contact. |
| BIOS / UEFI | Firmware that controls boot and hardware settings. Updates can fix compatibility and security issues; follow the manufacturer procedure and back up current settings before updating. A failed update can make the system unbootable. |
| Event log / diagnostics | The OS and hardware keep logs (e.g. Windows Event Viewer, SMART for disks) that record errors and warnings. Use these to identify recurring faults, plan preventive actions, and document corrective maintenance. |

![Thermal paste application](images/maintenance-thermal-paste.jpg)

**Preventive maintenance checklist (scheduled)**

| Task | Frequency | Notes |
|------|-----------|--------|
| Clean vents, heatsinks, fans | Monthly (dusty) / Quarterly | Power off, unplug; compressed air and soft brush; hold fans still when blowing. |
| Check fan operation and temperatures | Monthly | Use BIOS/UEFI or software (e.g. HWiNFO, SpeedFan); replace noisy or failed fans. |
| Update OS and antivirus | As per policy (e.g. weekly) | Apply security updates; verify definitions; schedule outside peak hours. |
| Verify backups | Weekly / Monthly | Confirm backup job ran; test restore if required by policy. |
| Check cables and connectors | Quarterly | Reseat loose cables; replace damaged or frayed cables. |
| Check disk health (SMART) | Monthly | Use manufacturer or OS tool; plan replacement if warnings. |
| Review event log for errors | Monthly | Windows Event Viewer or equivalent; note recurring faults for corrective action. |

**Thermal paste replacement procedure**

1. Power off, unplug, open chassis; wear anti-static strap.
2. Disconnect CPU fan cable; remove heatsink (often four screws or clips).
3. Wipe old paste from CPU and heatsink with isopropyl alcohol and lint-free cloth; allow to dry.
4. Apply small pea-sized amount of thermal paste to centre of CPU; do not spread with finger.
5. Reseat heatsink firmly and evenly; reconnect fan cable.
6. Power on; check temperatures in BIOS or with software; verify fan spins.

![Event Viewer / diagnostics](images/maintenance-event-viewer.png)

**Common corrective faults**

| Fault | Likely cause | Action |
|-------|--------------|--------|
| Overheating / thermal shutdown | Dust block, failed fan, dried thermal paste | Clean vents and heatsink; replace fan; reapply thermal paste. |
| No POST / no display | Loose RAM, faulty RAM, loose GPU | Reseat RAM and GPU; test with one stick; replace if faulty. |
| Random crash / BSOD | Faulty RAM, driver, disk error | Run memory test; update or roll back driver; check disk SMART and event log. |
| No boot / corrupted OS | Failed disk, bad update, malware | Repair or reinstall OS; replace disk if SMART failed; restore from backup if available. |
| Noisy fan | Worn bearing, dust | Clean; replace fan if noise persists. |
| USB / device not working | Loose cable, driver, port fault | Reseat cable; reinstall driver; try another port. |

| Maintenance Report | Required Information |
|--------------------|----------------------|
| Date and asset | Date of maintenance; asset ID or serial number; location. |
| Type of maintenance | Preventive (scheduled) or corrective; reference to schedule or job order if applicable. |
| Tasks performed | List of tasks (cleaning, parts replaced, updates applied, tests run). |
| Parts and materials | Part numbers and quantities used; none if preventive only. |
| Sign-off | Technician name and date; user or supervisor acceptance if required. |

![Maintenance report example](images/maintenance-report.png)

**Learning outcomes (Knowledge 30% / Performance 70%)**

| Work activity | Knowledge (30%) | Performance (70%) |
|---------------|-----------------|--------------------|
| 1. Identify computer maintenance requirements | Explain preventive vs corrective maintenance; list tools and schedule; interpret event log and SMART. | Check schedule and asset list; gather tools and parts; review logs and plan tasks. |
| 2. Carry out computer scheduled preventive maintenance | Describe cleaning and inspection steps; explain thermal paste and fan checks; state backup and update procedures. | Power off, open chassis; clean vents and heatsinks; check fans and temps; update OS/AV; verify backups; record findings. |
| 3. Perform computer corrective maintenance | Describe common faults (overheat, no POST, crash, no boot); explain diagnostic use of event log and SMART. | Diagnose fault; replace or repair part; reinstall or reconfigure software; retest; document parts and actions. |
| 4. Prepare computer maintenance report | List required report fields (date, asset, type, tasks, parts, sign-off). | Complete report with date, asset ID, type, tasks performed, parts used, and sign-off. |

**Contact hour:** [[00_Contact-hour_IT-020-3-L3-Operation]]
