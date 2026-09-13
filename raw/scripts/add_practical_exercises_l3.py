#!/usr/bin/env python3
"""
Add Practical Exercises sections to all Level 3 CoCu files for US-013.

This script automates the insertion of hands-on lab exercises aligned with
each CoCu's work activities. Exercises include objective, equipment, procedures,
expected outcomes, and assessment checklists following NOSS standards for
L3 operational/technician-level competencies.
"""

import os
import re
from pathlib import Path


def extract_work_activities(content: str) -> list[str]:
    """Extract work activities from the contact hour distribution table."""
    # Find the contact hour distribution table (lines with %, hrs, activity names)
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
    """Generate practical exercises section for a CoCu."""
    exercises = "## Practical Exercises\n\n"
    exercises += f"The following hands-on lab exercises develop the practical competencies required for {cocu_title}. "
    exercises += "Each exercise is designed for L3 operational-level technicians and includes step-by-step procedures, "
    exercises += "required equipment, and assessment criteria aligned with NOSS standards.\n\n"

    lab_num = 1

    # Define exercise templates based on CoCu and activity type
    exercise_templates = {
        2: {  # CoCu 2: Computer System Maintenance
            "Identify computer maintenance requirements": {
                "title": "Lab 2.1: Identifying Maintenance Needs",
                "objective": "Identify maintenance requirements from system logs and performance indicators",
                "duration": "45 minutes",
                "equipment": ["Test computer system", "System monitoring software (HWiNFO, Event Viewer)", "BIOS/UEFI access", "Temperature monitoring tools"],
                "procedures": [
                    "Boot the test system and log in",
                    "Open system monitoring software and check CPU, GPU, and disk temperatures",
                    "Open Windows Event Viewer and review System and Application logs for warnings or errors",
                    "Check SMART data on storage drives for early warnings",
                    "Inspect the system physically for dust buildup in vents and heatsinks",
                    "Document findings in a maintenance requirement checklist",
                    "Prioritize maintenance tasks based on urgency and risk"
                ],
                "expected_outcome": "Completed maintenance requirement checklist with identified issues and priority ranking",
                "checklist": [
                    "System logs reviewed for errors or warnings",
                    "Temperatures checked and documented",
                    "SMART health status checked",
                    "Physical inspection completed",
                    "Maintenance needs documented",
                    "Priority assigned to each task"
                ]
            },
            "Carry out computer scheduled preventive maintenance": {
                "title": "Lab 2.2: Performing Preventive Maintenance",
                "objective": "Perform scheduled preventive maintenance tasks to keep systems optimal",
                "duration": "60 minutes",
                "equipment": ["Test computer", "Compressed air", "Soft anti-static brush", "Lint-free cloth", "Isopropyl alcohol", "Thermal paste"],
                "procedures": [
                    "Power off the computer and unplug the power cable",
                    "Remove the side panel and visually inspect for dust accumulation",
                    "Use compressed air in short bursts to blow out dust from vents, fans, and heatsink",
                    "Use a soft brush to gently loosen dust from fan blades and tight spaces",
                    "Wipe down the motherboard and components with a lint-free cloth (no moisture)",
                    "Power on the system and verify all fans spin correctly and smoothly",
                    "Check temperatures in BIOS/UEFI to ensure cooling is working properly",
                    "Apply Windows/Linux updates if scheduled",
                    "Verify backup completion if automated backups are in place"
                ],
                "expected_outcome": "Clean system with verified cooling function and current updates applied",
                "checklist": [
                    "System powered down and unplugged",
                    "Dust removed from vents, fans, and heatsink",
                    "Fans spinning correctly after restart",
                    "Temperatures within normal range",
                    "Updates applied successfully",
                    "Backup status verified"
                ]
            },
            "Perform computer corrective maintenance": {
                "title": "Lab 2.3: Corrective Maintenance Response",
                "objective": "Diagnose and repair a simulated hardware or software fault",
                "duration": "75 minutes",
                "equipment": ["Test computer with simulated fault", "Multimeter", "Screwdrivers", "Spare parts (RAM, fan, thermal paste)", "USB diagnostics media"],
                "procedures": [
                    "Receive a fault description (e.g., 'system overheating', 'blue screen')",
                    "Use diagnostics software to narrow down the issue",
                    "Perform physical inspection if hardware is suspected",
                    "For thermal issues: check heatsink seating, clean dust, reapply thermal paste",
                    "For memory errors: reseat RAM modules, test with single module",
                    "For fan failure: check BIOS for fan readings, replace fan if failed",
                    "Run stress tests to verify the issue is resolved",
                    "Document the fault, action taken, and parts replaced"
                ],
                "expected_outcome": "System fully functional with fault corrected and documented",
                "checklist": [
                    "Fault correctly diagnosed",
                    "Appropriate corrective action taken",
                    "System stable after repair",
                    "Replaced parts documented with serial numbers",
                    "Testing confirms fault resolution"
                ]
            },
            "Prepare computer maintenance report": {
                "title": "Lab 2.4: Maintenance Documentation",
                "objective": "Complete comprehensive maintenance documentation",
                "duration": "30 minutes",
                "equipment": ["Computer system", "Maintenance report template", "Pen and paper or text editor"],
                "procedures": [
                    "Gather all information: system asset ID, date, technician name",
                    "Summarize preventive or corrective tasks performed",
                    "Record parts replaced (if any) with serial numbers and costs",
                    "Document temperatures before and after maintenance",
                    "List any outstanding issues requiring future action",
                    "Include sign-off from technician and verification of completion",
                    "Attach or reference photos if major work was performed"
                ],
                "expected_outcome": "Completed maintenance report with all required details",
                "checklist": [
                    "System asset ID recorded",
                    "Date and technician documented",
                    "All tasks listed with outcomes",
                    "Parts replaced documented",
                    "Next scheduled maintenance date recorded",
                    "Report signed and dated"
                ]
            }
        },
        3: {  # CoCu 3: Computer System Repair
            "Assess computer repair job order/change request": {
                "title": "Lab 3.1: Fault Analysis and Diagnosis",
                "objective": "Analyse a system fault report and develop a repair strategy",
                "duration": "45 minutes",
                "equipment": ["Faulty computer system", "Diagnostics software", "Hardware reference guides", "Multimeter"],
                "procedures": [
                    "Receive a fault report describing symptoms (no power, slow performance, error messages)",
                    "Ask clarifying questions: when did it start, what was the last action before failure",
                    "Run diagnostics software to identify failing components",
                    "Check event logs for clues about the fault cause",
                    "Use a multimeter to check power supply voltages if power-related",
                    "Develop a repair strategy addressing the root cause",
                    "Document the analysis and proposed repair steps"
                ],
                "expected_outcome": "Fault analysis report with diagnosed problem and proposed repair plan",
                "checklist": [
                    "Symptoms documented",
                    "Diagnostics run successfully",
                    "Logs reviewed for errors",
                    "Root cause identified",
                    "Repair strategy documented",
                    "Required parts/tools listed"
                ]
            },
            "Perform on-site repair": {
                "title": "Lab 3.2: Hardware Component Replacement and On-site Repair",
                "objective": "Replace a faulty hardware component and verify repair success",
                "duration": "60 minutes",
                "equipment": ["Computer with faulty component", "Replacement component", "Screwdrivers", "Anti-static strap", "Thermal paste (if CPU/heatsink)"],
                "procedures": [
                    "Power off and unplug the computer",
                    "Ground yourself with an anti-static strap",
                    "Identify the faulty component location in the system",
                    "Remove any screws or clips holding the component",
                    "Carefully extract the faulty component",
                    "Inspect the replacement component for any visible damage",
                    "Install the replacement component securely",
                    "Reapply thermal paste if replacing CPU or GPU heatsink",
                    "Power on and verify the system boots correctly",
                    "Run diagnostics to confirm the fault is resolved"
                ],
                "expected_outcome": "System repaired with faulty component replaced and verified working",
                "checklist": [
                    "Faulty component identified and removed safely",
                    "Replacement component installed correctly",
                    "System boots without errors",
                    "Diagnostics pass",
                    "All cables reconnected properly",
                    "Repair verified complete"
                ]
            },
            "Carry out online trouble shooting": {
                "title": "Lab 3.3: Remote Troubleshooting and Online Support",
                "objective": "Perform remote troubleshooting to diagnose and resolve computer faults",
                "duration": "45 minutes",
                "equipment": ["Customer computer (remote access)", "Remote support software", "Knowledge base or diagnostic scripts", "Phone or chat for communication"],
                "procedures": [
                    "Contact the user and gather detailed symptom information (error messages, when it started, what was the last action)",
                    "Ask the user to check basic connectivity (network, power, cables)",
                    "Request remote desktop access or use remote support software to view the user's screen",
                    "Run diagnostics remotely: open Event Viewer, check Device Manager, run memory test if available",
                    "Guide the user through basic troubleshooting steps: restart, Safe Mode boot, check cables",
                    "Look up error codes in knowledge base and apply known fixes",
                    "If remotely fixable, apply the fix and confirm resolution with the user",
                    "If hardware fault is likely, escalate to on-site repair and document findings"
                ],
                "expected_outcome": "Fault diagnosed; issue resolved remotely or escalated with documentation for on-site repair",
                "checklist": [
                    "Symptom information fully documented",
                    "Remote access established",
                    "Diagnostics run and logs reviewed",
                    "Troubleshooting steps documented",
                    "Issue resolved OR escalated with clear handoff",
                    "User confirmation obtained"
                ]
            },
            "Prepare computer status report": {
                "title": "Lab 3.4: Computer Status Report and Repair Documentation",
                "objective": "Complete comprehensive computer status report documenting repair activities and outcomes",
                "duration": "30 minutes",
                "equipment": ["Repaired computer", "Status report template", "Pen and paper or text editor", "Camera (optional for photos)"],
                "procedures": [
                    "Record the original fault description and symptoms from the job order",
                    "Document online troubleshooting steps performed and findings (if applicable)",
                    "Record on-site repair actions taken and components accessed or replaced",
                    "List replaced hardware with part numbers and serial numbers for inventory tracking",
                    "Record technician time spent on diagnosis and repair",
                    "Include test results (temperature readings, diagnostics) confirming repair success",
                    "Note any warranty, service tags, or asset ID labels applied",
                    "Add recommendation: follow-up maintenance, user training, or hardware upgrade suggestions",
                    "Obtain user or supervisor sign-off if required by policy"
                ],
                "expected_outcome": "Complete status report documenting initial fault, troubleshooting, repair actions, parts used, test results, and recommendations",
                "checklist": [
                    "Fault description clear and complete",
                    "Troubleshooting steps documented",
                    "On-site repair actions detailed",
                    "Parts replaced with serial numbers recorded",
                    "Test results showing success",
                    "Recommendations included",
                    "Report signed and dated"
                ]
            }
        },
        1: {  # CoCu 1: Computer System Set-up
            "Analyse job request/change order": {
                "title": "Lab 1.1: Analysing and Planning a Computer Build",
                "objective": "Analyse a job request and plan the computer set-up sequence",
                "duration": "45 minutes",
                "equipment": ["Job request template", "Customer specifications sheet", "Hardware checklist", "Parts inventory list", "Scheduling tool"],
                "procedures": [
                    "Receive a simulated job request specifying CPU model, RAM capacity, storage type, and software requirements",
                    "Extract and verify all customer requirements from the job request",
                    "Cross-check hardware specifications against supplier inventory",
                    "Create a logical set-up sequence (order of installation steps)",
                    "Identify any missing parts or incompatibilities and document actions",
                    "Prepare a bill of materials and tools checklist",
                    "Document the analysis in a structured format for team review"
                ],
                "expected_outcome": "Completed analysis showing identified requirements, compatibility verification, and set-up plan",
                "checklist": [
                    "Job request completely read and understood",
                    "All hardware specifications extracted and verified",
                    "Incompatibilities or gaps identified",
                    "Set-up sequence documented in logical order",
                    "Bill of materials prepared",
                    "Analysis signed off for proceeding to set-up"
                ]
            },
            "Prepare computer set-up tools, computer hardware parts and computer software": {
                "title": "Lab 1.2: Gathering and Organizing Set-up Materials",
                "objective": "Prepare and organize all tools, hardware, and software required for set-up",
                "duration": "30 minutes",
                "equipment": ["Full technician toolkit", "Hardware components", "Anti-static mat and wrist strap", "USB installer", "Software media", "Labelling equipment"],
                "procedures": [
                    "Gather all tools from the workshop: screwdrivers, multimeter, cable tester, anti-static strap, thermal paste",
                    "Retrieve required hardware components from inventory: CPU, RAM, storage, motherboard, power supply, peripherals",
                    "Prepare OS and driver media (USB installers, disc if required)",
                    "Set up anti-static mat in the work area and verify grounding",
                    "Organize all materials in a logical sequence for installation",
                    "Create a checklist confirming all items are present and functional",
                    "Label cables, connectors, and components for easy identification during installation"
                ],
                "expected_outcome": "Organized workspace with all tools and materials ready, verified checklist, and labelled components",
                "checklist": [
                    "Toolkit is complete and tools are functional",
                    "All hardware components are present and undamaged",
                    "Software media is prepared and bootable",
                    "Anti-static precautions are in place",
                    "Workspace is organized and clear",
                    "All items verified on equipment checklist"
                ]
            },
            "Set-up computer hardware": {
                "title": "Lab 1.3: Hardware Assembly and Installation",
                "objective": "Assemble and install computer hardware components correctly",
                "duration": "90 minutes",
                "equipment": ["Computer case", "Motherboard", "CPU with heatsink", "RAM", "Storage drives", "Power supply", "Expansion cards", "Cable management supplies"],
                "procedures": [
                    "Install the motherboard in the case, using correct standoffs and screws",
                    "Install the CPU with thermal paste and cooler, following manufacturer specifications",
                    "Install RAM modules in correct slots (verify dual-channel configuration if applicable)",
                    "Install storage devices (HDD/SSD/NVMe) in appropriate bays and slots",
                    "Connect all power connectors: 24-pin motherboard, 8-pin CPU, PCIe for GPU if present",
                    "Connect SATA data cables (if using SATA drives) or verify NVMe seating",
                    "Organize and secure cables to avoid obstruction of airflow",
                    "Verify all components are properly seated and secured",
                    "Do not power on yet—prepare for BIOS checks"
                ],
                "expected_outcome": "Fully assembled computer with all components correctly installed and cables organized",
                "checklist": [
                    "Motherboard is properly seated and secured",
                    "CPU is installed with thermal paste and cooler attached",
                    "RAM is installed in correct slots and fully seated",
                    "Storage devices are installed and connected",
                    "All power connectors are connected and secure",
                    "Cables are organized and do not block airflow",
                    "No loose screws or components remain"
                ]
            },
            "Carry out computer software installation": {
                "title": "Lab 1.4: Operating System and Driver Installation",
                "objective": "Install the operating system and drivers to bring the system to working state",
                "duration": "75 minutes",
                "equipment": ["Assembled computer from Lab 1.3", "OS USB installer", "Driver media/downloads", "Monitor and peripherals"],
                "procedures": [
                    "Connect monitor, keyboard, and mouse; power on the system",
                    "Enter BIOS/UEFI to verify hardware detection (check CPU, RAM, storage)",
                    "Set boot order to USB and enable/disable secure boot as needed for OS installer",
                    "Boot from USB installer and follow OS installation prompts",
                    "Partition the storage drive according to job requirements",
                    "Complete base OS installation and initial configuration",
                    "Install chipset drivers from manufacturer support site or media",
                    "Install GPU, network, audio, and other device drivers in correct order",
                    "Apply Windows updates or OS patches",
                    "Verify all devices are recognized in Device Manager and no unknown devices remain"
                ],
                "expected_outcome": "Working computer with OS installed and all drivers recognized; Device Manager shows no errors",
                "checklist": [
                    "OS installed successfully and boots without errors",
                    "All hardware detected in BIOS and OS",
                    "All device drivers installed (no unknown devices)",
                    "Network and audio working",
                    "No driver errors in Device Manager",
                    "System stable for initial testing"
                ]
            },
            "Set-up computer peripherals": {
                "title": "Lab 1.5: Peripheral Connection and Configuration",
                "objective": "Connect and configure peripheral devices (monitor, keyboard, mouse, printer) correctly",
                "duration": "30 minutes",
                "equipment": ["Installed computer from Lab 1.4", "Monitor", "Keyboard", "Mouse", "Printer (optional)", "USB peripherals"],
                "procedures": [
                    "Verify monitor is connected with correct cable (HDMI, DisplayPort, DVI)",
                    "Set monitor resolution and refresh rate in OS display settings to match hardware capability",
                    "Connect keyboard and mouse via USB and verify device detection",
                    "Install printer driver if a printer is part of the job request",
                    "Connect printer via USB or network and verify it appears in Devices and Printers",
                    "Test each peripheral: type with keyboard, move mouse, send test print if applicable",
                    "Configure peripheral settings (keyboard layout, mouse sensitivity, printer defaults)"
                ],
                "expected_outcome": "All peripherals connected, recognized, and functioning correctly",
                "checklist": [
                    "Monitor connected and resolution correct",
                    "Keyboard responds and is recognized",
                    "Mouse responds and is recognized",
                    "Printer (if applicable) installed and ready",
                    "All peripherals visible in Device Manager with no errors"
                ]
            },
            "Carry out unit functionality test": {
                "title": "Lab 1.6: System Functionality and Stability Testing",
                "objective": "Perform comprehensive testing to verify the system is stable and ready for user handover",
                "duration": "45 minutes",
                "equipment": ["Fully configured system from Lab 1.5", "System utilities (Windows, Linux built-in tools)", "Multimeter (optional)"],
                "procedures": [
                    "Power on the system and observe boot sequence for any errors or warnings",
                    "Log in and verify user account creation",
                    "Run Device Manager and check for any unknown or error devices",
                    "Use system utilities to check disk status: Run Check Disk (chkdsk) or equivalent",
                    "Monitor CPU and RAM usage during normal operations using Task Manager or top command",
                    "Test network connectivity by opening a browser and visiting a website",
                    "Copy a test file to storage and verify read/write speeds are acceptable",
                    "Launch one or two applications (office, browser) specified in the job and verify they open correctly",
                    "Stress-test the system briefly (e.g., run antivirus scan or CPU-intensive tool for 5 minutes)",
                    "Check temperatures using BIOS monitoring or system utilities; ensure CPU/GPU temps are in normal range",
                    "Document test results on the functionality test checklist"
                ],
                "expected_outcome": "All system tests pass; system is stable, all devices respond, and no errors are logged",
                "checklist": [
                    "System boots without errors",
                    "User account is functional",
                    "All hardware is recognized with no unknown devices",
                    "Disk check completed with no errors",
                    "CPU and RAM are operating within expected parameters",
                    "Network connectivity confirmed",
                    "Applications launch and respond normally",
                    "System remains stable under load",
                    "CPU and GPU temperatures are within safe range"
                ]
            },
            "Prepare computer system set-up report": {
                "title": "Lab 1.7: Documentation and Set-up Report Completion",
                "objective": "Complete comprehensive documentation of the set-up for user handover and future reference",
                "duration": "30 minutes",
                "equipment": ["Tested computer", "Set-up report template", "Camera or photo capture device", "Pen/signature area"],
                "procedures": [
                    "Gather serial numbers and product keys from all hardware components",
                    "Record installed OS version, edition, and licence key (if applicable)",
                    "Document all installed drivers and applications with versions",
                    "Record BIOS/UEFI settings (boot order, secure boot, XMP, TPM status) that differ from defaults",
                    "Capture a screenshot of Device Manager showing all recognized hardware",
                    "Take photos of hardware configuration and cable organization for future reference",
                    "Record RAM configuration (total capacity, speed, dual-channel status)",
                    "Record storage configuration (drive types, total capacity, partition layout)",
                    "Document any deviations from the original job request or changes made during set-up",
                    "Complete the set-up checklist with sign-off from a senior technician",
                    "Prepare handover notes for the user (user guide, support contact information)"
                ],
                "expected_outcome": "Complete set-up report with all hardware details, software versions, test results, and user sign-off",
                "checklist": [
                    "All hardware serial numbers and specs recorded",
                    "OS version and licence recorded",
                    "All drivers and applications documented with versions",
                    "Non-default BIOS settings recorded",
                    "Hardware photos and Device Manager screenshot attached",
                    "System configuration diagram or notes prepared",
                    "Any deviations from job request explained",
                    "Technician sign-off obtained",
                    "User handover notes prepared"
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
            exercises += f"**Equipment Required:**\n"
            exercises += f"{', '.join(template['equipment'])}\n\n"
            exercises += "**Procedures:**\n"
            for i, proc in enumerate(template['procedures'], 1):
                exercises += f"{i}. {proc}\n"
            exercises += f"\n**Expected Outcome:**\n{template['expected_outcome']}\n\n"
            exercises += "**Assessment Checklist:**\n"
            for item in template['checklist']:
                exercises += f"- [ ] {item}\n"
            exercises += "\n"
        else:
            # Fallback for activities not in templates
            exercises += f"### Lab {lab_num}: {activity}\n\n"
            exercises += f"**Objective:** Perform {activity.lower()} correctly according to NOSS standards\n\n"
            exercises += "**Duration:** 60 minutes\n\n"
            exercises += "**Equipment Required:** Standard technician tools and components appropriate to the activity\n\n"
            exercises += "**Procedures:**\n"
            exercises += f"1. Follow established procedures for {activity.lower()}\n"
            exercises += "2. Complete the activity according to job specifications\n"
            exercises += "3. Verify the work meets quality standards\n"
            exercises += "4. Document the completion and any issues encountered\n\n"
            exercises += "**Expected Outcome:**\n"
            exercises += f"Successful completion of {activity.lower()} with no errors\n\n"
            exercises += "**Assessment Checklist:**\n"
            exercises += "- [ ] Activity completed according to procedure\n"
            exercises += "- [ ] Quality standards met\n"
            exercises += "- [ ] No safety incidents\n"
            exercises += "- [ ] Documentation complete\n\n"
            lab_num += 1

    return exercises


def add_practical_exercises_to_file(file_path: str) -> bool:
    """Add practical exercises section to a CoCu file."""
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
    """Main function to process all L3 CoCu files."""
    base_dir = Path(__file__).parent.parent / "content" / "IT-020-3"

    # Files to process (L3 CoCu files only, not practice/contact hour files)
    cocu_files = [
        "01_CoCu-1-Computer-System-Set-up.md",
        "02_CoCu-2-Computer-System-Maintenance.md",
        "03_CoCu-3-Computer-System-Repair.md",
        "04_CoCu-4-Server-Installation.md",
        "05_CoCu-5-Server-Maintenance.md",
        "06_CoCu-6-Computer-Network-Connectivity-Set-up.md",
        "07_CoCu-7-Mobile-Device-Configuration.md"
    ]

    print("Adding Practical Exercises sections to L3 CoCu files...\n")

    successes = 0
    for file_name in cocu_files:
        file_path = base_dir / file_name
        if add_practical_exercises_to_file(str(file_path)):
            successes += 1

    print(f"\n✓ Successfully processed {successes}/{len(cocu_files)} files")
    return 0 if successes == len(cocu_files) else 1


if __name__ == "__main__":
    exit(main())
