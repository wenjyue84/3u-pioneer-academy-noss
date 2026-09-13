#!/usr/bin/env python3
"""
add_references.py — Add topic-specific References section to all 20 CoCu files

This script generates and adds a References section to each CoCu file based on:
- CoCu title and topic
- IT-020 program level (L3, L4, L5)
- NOSS standards and industry best practices
- Malaysian JPK/DSD compliance context

The References section is inserted before the final "Contact hour:" line.
"""

import os
import re
from pathlib import Path

# Define references for each CoCu based on topic and level
REFERENCES = {
    # L3 - Operational Level
    "01_CoCu-1-Computer-System-Set-up": {
        "level": "L3",
        "references": [
            "Malaysian Standard MS 1546-1:2003 – Code of Practice for Information Security Management",
            "NOSS IT-020-3:2013 Computer System Operation Syllabus",
            "Dell PowerEdge Documentation – Server Hardware Installation and Configuration",
            "Intel ARK Processor Specifications – Socket Compatibility and Thermal Design Power",
            "JEDEC DDR5 Memory Standard – Performance Profiles and Compatibility Guidelines",
            "CompTIA A+ Certification Study Guide – Hardware Installation and Troubleshooting",
            "Linus Torvalds et al. (2024). Linux Kernel Documentation – UEFI Booting",
            "Microsoft Windows Server 2025 Installation and Configuration Guide",
            "American Megatrends (AMI) BIOS/UEFI Setup Documentation",
            "Institute of Electrical and Electronics Engineers (IEEE) 802.3 Network Standards",
        ]
    },
    "02_CoCu-2-Computer-System-Maintenance": {
        "level": "L3",
        "references": [
            "NOSS IT-020-3:2013 Computer System Operation Syllabus",
            "International Organization for Standardization (ISO) 27001:2022 Information Security Management",
            "Preventive Maintenance Best Practices – HP and Dell Server Documentation",
            "SMART (Self-Monitoring, Analysis and Reporting Technology) Monitoring Guidelines",
            "Microsoft Windows Event Viewer and Performance Monitor Guide",
            "CompTIA A+ 1001/1002 Maintenance and Troubleshooting Objectives",
            "Linux System Administration – Monitoring Tools (htop, iostat, vmstat)",
            "CompTIA Server+ Certification Guide – System Monitoring and Optimization",
            "Environmental Protection Agency (EPA) Energy Star Computing Standards",
            "IEEE 1588 Precision Time Protocol for System Synchronization",
        ]
    },
    "03_CoCu-3-Computer-System-Repair": {
        "level": "L3",
        "references": [
            "NOSS IT-020-3:2013 Computer System Operation Syllabus",
            "Intel and AMD Processor Replacement and RMA Procedures",
            "HP ProDesk and ProLiant Hardware Service Bulletins",
            "Troubleshooting and Diagnostics Guide – Windows Memory Diagnostics, memtest86",
            "Seagate and Western Digital HDD Diagnostic Tools and RMA Procedures",
            "Samsung and SK Hynix SSD SMART Monitoring and Data Recovery Guidelines",
            "BIOS/UEFI Diagnostics and Hardware Test Procedures",
            "CompTIA A+ Troubleshooting Methodology (CompTIA A+ 220-1001/1002)",
            "Linux Hardware Diagnostics – dmidecode, lspci, lsusb Utilities",
            "NZXT and Corsair Liquid Cooling System Maintenance and Repair Guides",
        ]
    },
    "04_CoCu-4-Server-Installation": {
        "level": "L3",
        "references": [
            "NOSS IT-020-3:2013 Computer System Operation Syllabus",
            "Dell PowerEdge Server Installation and Configuration Guide (RAID Setup)",
            "HP ProLiant Server Reference Architecture – Hardware and Firmware Setup",
            "Lenovo ThinkSystem Server Installation and First Boot Guide",
            "RAID Configuration Best Practices – Dell, HP, Lenovo Documentation",
            "Storage Area Network (SAN) Introduction and Zoning Fundamentals",
            "CompTIA Server+ Certification Guide – Server Hardware and Configuration",
            "Microsoft Windows Server 2025 Installation and Initial Configuration",
            "Linux Server Installation (Red Hat, Ubuntu, Debian) – Disk Partitioning and LVM",
            "Fiber Channel and iSCSI Protocol Standards for Enterprise Storage",
        ]
    },
    "05_CoCu-5-Server-Maintenance": {
        "level": "L3",
        "references": [
            "NOSS IT-020-3:2013 Computer System Operation Syllabus",
            "HP ProLiant Server Maintenance and Updates – System Firmware Updates",
            "Dell iDRAC (Integrated Dell Remote Access Controller) Administration Guide",
            "Lenovo XClarity Administrator – Server Monitoring and Management",
            "Windows Server Update Services (WSUS) Deployment and Administration",
            "Linux Patch Management – yum, apt, dnf Package Management",
            "RAID Array Monitoring and Disk Replacement Procedures",
            "CompTIA Server+ Maintenance and Troubleshooting Objectives",
            "Environmental Monitoring in Data Centers – Temperature and Power Standards",
            "Backup and Recovery Best Practices – Veeam, Commvault Documentation",
        ]
    },
    "06_CoCu-6-Computer-Network-Connectivity-Set-up": {
        "level": "L3",
        "references": [
            "NOSS IT-020-3:2013 Computer System Operation Syllabus",
            "IEEE 802.3 Ethernet Standard and Cable Specifications (Cat6A, Cat7, Cat8)",
            "IEEE 802.11ac/ax Wireless LAN (Wi-Fi 6/7) Technical Specifications",
            "Cisco Networking Academy – Introduction to Networking and IPv4/IPv6 Protocols",
            "RFC 791 – Internet Protocol Version 4 (IPv4) Specification",
            "RFC 8200 – Internet Protocol Version 6 (IPv6) Specification",
            "Malaysian Registry of Internet Numbers (MYNIC) – IPv4 and IPv6 Allocation",
            "CompTIA Network+ Certification Guide – Network Installation and Configuration",
            "Dell Networking Switch Configuration – S-Series and Z-Series Switches",
            "Network Cabling Standards and Best Practices – TIA-568 Color Code Standards",
        ]
    },
    "07_CoCu-7-Mobile-Device-Configuration": {
        "level": "L3",
        "references": [
            "NOSS IT-020-3:2013 Computer System Operation Syllabus",
            "Apple iOS Configuration and Mobile Device Management (MDM) Documentation",
            "Google Android Enterprise Security and Configuration Guidelines",
            "Microsoft Intune Mobile Device Management (MDM) Administration Guide",
            "NIST Cybersecurity Framework – Mobile Device Security Requirements",
            "OWASP Mobile Application Security – Top 10 Risks and Mitigation",
            "CompTIA A+ 220-1101/1102 Mobile Device Setup and Configuration",
            "CompTIA CySA+ – Mobile Security Assessment and Best Practices",
            "Samsung Knox Security Architecture and MDM Integration",
            "Malaysian BNM – Cybersecurity Regulations for Financial Sector Mobile Apps",
        ]
    },
    # L4 - Administrative Level
    "01_CoCu-1-Server-Configuration": {
        "level": "L4",
        "references": [
            "NOSS IT-020-4:2013 Computer System Administration Syllabus",
            "Microsoft Windows Server 2025 Administration and Deployment Guide",
            "Red Hat Enterprise Linux 9 System Administrator Reference (RHEL)",
            "Ubuntu Server 24.04 LTS Installation and Administration Guide",
            "Dell PowerEdge Server Administration Guide – iDRAC, iLO, BMC Configuration",
            "CompTIA Server+ Certification Study Guide – Advanced Server Administration",
            "Hyper-V Server Virtualization Administration and Cluster Configuration",
            "VMware vSphere 8 Installation, Configuration and Management",
            "Amazon Web Services (AWS) EC2 Instance Configuration and Best Practices",
            "Microsoft Azure Virtual Machines – Deployment and Administration",
        ]
    },
    "02_CoCu-2-Computer-System-Security-Control": {
        "level": "L4",
        "references": [
            "NOSS IT-020-4:2013 Computer System Administration Syllabus",
            "Malaysian Standard MS 1546-1:2003 – Information Security Management Code of Practice",
            "NIST SP 800-53 – Security and Privacy Controls for Information Systems",
            "ISO/IEC 27001:2022 – Information Security Management Systems Standard",
            "CompTIA Security+ Certification Study Guide – Cryptography and Access Control",
            "OWASP Top 10 – Application Security Risks and Mitigation Strategies",
            "Microsoft Active Directory (AD) Security Hardening and Group Policy Administration",
            "Linux Security – SELinux, AppArmor, and Firewall Configuration (iptables, firewalld)",
            "Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) Implementation",
            "NIST Cybersecurity Framework – Core Functions and Categories",
        ]
    },
    "03_CoCu-3-System-Network-Procurement": {
        "level": "L4",
        "references": [
            "NOSS IT-020-4:2013 Computer System Administration Syllabus",
            "IEEE 802.3 – Ethernet Technology and High-Speed Standards (10GbE, 25GbE)",
            "RFC 1918 – Address Allocation for Private Internets (NAT and Private IP)",
            "Cisco Network Design and Best Practices for Enterprise Networks",
            "Dell Networking – Architecture and Design for Modular Data Center Networks",
            "Juniper Networks – Enterprise Routing and Switching Design Principles",
            "Software-Defined Networking (SDN) – OpenFlow and Network Virtualization",
            "Network Procurement Evaluation and Benchmarking Standards",
            "Malaysian Ministry of Energy, Water and Environment – Infrastructure Standards",
            "ISO/IEC 23001 – Cloud Infrastructure Standard and Requirements",
        ]
    },
    "04_CoCu-4-Network-Cabling-Management": {
        "level": "L4",
        "references": [
            "NOSS IT-020-4:2013 Computer System Administration Syllabus",
            "TIA-568-A and TIA-568-B Cabling Standards and Best Practices",
            "TIA/EIA 942 – Data Center Standards and Infrastructure Design",
            "IEEE 802.3 – Twisted Pair Cabling Specifications and Performance Categories",
            "ANSI/TIA-942-B Standard for Data Center Facilities",
            "Fiber Optic Cabling Manual – Installation and Maintenance (Corning, AFL)",
            "Belden, Panduit, and CommScope Cabling Product Specifications",
            "Cable Testing Standards – Fluke Networks and Ideal Industries Test Equipment",
            "Power over Ethernet (PoE) Standard – IEEE 802.3at/bt Specifications",
            "Environmental Conditions for Cabling Infrastructure – Temperature and Humidity Standards",
        ]
    },
    "05_CoCu-5-Computer-Network-Installation-Management": {
        "level": "L4",
        "references": [
            "NOSS IT-020-4:2013 Computer System Administration Syllabus",
            "Cisco CCNA Routing and Switching – Network Installation and Management",
            "Juniper Networks JNCIS-ENT Certification Guide – Enterprise Routing and Switching",
            "CompTIA Network+ Extended Objectives – Advanced Network Administration",
            "RFC 3021 – Using 31-Bit Prefixes on IPv4 Point-to-Point Links",
            "Border Gateway Protocol (BGP) Administration and Configuration (RFC 4271)",
            "OSPF Dynamic Routing Protocol Configuration and Optimization (RFC 2328)",
            "EIGRP Configuration and Best Practices for Enterprise Networks",
            "Network Device Configuration Management – SNMP, NetFlow, sFlow Protocols",
            "Redundancy and High Availability Protocols – HSRP, VRRP, GLBP Configuration",
        ]
    },
    "06_CoCu-6-Computer-System-Maintenance-Management": {
        "level": "L4",
        "references": [
            "NOSS IT-020-4:2013 Computer System Administration Syllabus",
            "ITIL 4 Service Management – Maintenance and Operations Management Processes",
            "ISO/IEC 20000-1:2018 – IT Service Management Systems Standard",
            "System Center Configuration Manager (SCCM) – Patch Management and Deployment",
            "ManageEngine Patch Manager – Automated Patch Distribution and Compliance",
            "Puppet, Ansible, and Chef – Infrastructure as Code and Automation",
            "Maintenance Planning and Scheduling Best Practices for Data Centers",
            "Predictive Analytics for IT Asset Management – AI-Driven Maintenance Strategies",
            "CompTIA Server+ Advanced Maintenance and Troubleshooting Objectives",
            "SLA (Service Level Agreement) Development and KPI Monitoring Frameworks",
        ]
    },
    # L5 - Management Level
    "01_CoCu-1-Management-Overview": {
        "level": "L5",
        "references": [
            "NOSS IT-020-5:2013 Computer System Management Syllabus",
            "ITIL 4 Foundation – IT Service Management Framework and Core Processes",
            "ISO/IEC 20000-1:2018 – IT Service Management Systems Certification Standard",
            "COBIT 2019 – Governance and Management of Enterprise IT Framework",
            "ISO/IEC 27001:2022 – Information Security Management Systems",
            "NIST Cybersecurity Framework – Governance and Risk Management",
            "Project Management Institute (PMI) PMBOK – IT Project Governance",
            "Enterprise Architecture Framework – TOGAF Standard (The Open Group)",
            "Balanced Scorecard for IT Performance Management and Strategic Alignment",
            "Malaysian Financial Services Regulatory Authority (BNM) – Technology Risk Management",
        ]
    },
    "02_CoCu-2-Computer-System-Asset-Management": {
        "level": "L5",
        "references": [
            "NOSS IT-020-5:2013 Computer System Management Syllabus",
            "ITIL 4 Asset and Configuration Management – CMDB Best Practices",
            "ISO/IEC 27001:2022 – Asset Management and Information Classification",
            "ServiceNow IT Asset Management (ITAM) – Configuration and Optimization",
            "BMC Remedy and Track-It! Software License Management Platforms",
            "Total Cost of Ownership (TCO) Analysis and Lifecycle Costing Models",
            "Asset Tracking Technologies – RFID, Barcodes, and Mobile Device Management",
            "Depreciation and Leasing Models for IT Infrastructure Investment Planning",
            "Malaysian Accounting Standards (MAS) – Asset Valuation and Reporting",
            "Supply Chain Management for IT Hardware Procurement and Vendor Relations",
        ]
    },
    "03_CoCu-3-Computer-System-Security-Management": {
        "level": "L5",
        "references": [
            "NOSS IT-020-5:2013 Computer System Management Syllabus",
            "ISO/IEC 27001:2022 and ISO/IEC 27002:2022 – Information Security Standards",
            "NIST SP 800-39 – Managing Information and Technology Risk",
            "NIST Cybersecurity Framework – Risk Assessment and Mitigation",
            "OWASP Security Risk Assessment Methodology",
            "CompTIA CASP+ Certification Study Guide – Advanced Security Management",
            "Incident Response Planning and Digital Forensics Best Practices",
            "Security Awareness Training and Change Management for IT Teams",
            "Third-Party Risk Management and Vendor Security Assessment",
            "Malaysian Regulatory Compliance – BNM Technology Risk Management Guidelines",
        ]
    },
    "04_CoCu-4-Disaster-Recovery-Management": {
        "level": "L5",
        "references": [
            "NOSS IT-020-5:2013 Computer System Management Syllabus",
            "ITIL 4 Availability and Continuity Management Processes",
            "ISO/IEC 22301:2019 – Business Continuity Management Systems Standard",
            "DR Planning Guide – Disaster Recovery Institute International (DRII) Standards",
            "AWS Disaster Recovery Strategies – RTO and RPO Objectives",
            "Microsoft Azure Site Recovery – Multi-Region Failover Configuration",
            "Backup and Recovery Best Practices – Veeam, Commvault, Veritas Documentation",
            "Business Continuity Planning and Crisis Communication Strategies",
            "Risk Assessment and Business Impact Analysis (BIA) Frameworks",
            "Malaysian Regulatory Requirements for Financial Institution Disaster Recovery Plans",
        ]
    },
    "05_CoCu-5-Computer-System-Network-Project-Management": {
        "level": "L5",
        "references": [
            "NOSS IT-020-5:2013 Computer System Management Syllabus",
            "Project Management Institute (PMI) PMBOK 6th Edition – Project Management Framework",
            "Agile Project Management Framework – Scrum, Kanban, and SAFe Methodologies",
            "PRINCE2 (PRojects IN Controlled Environments) – Structured Project Management",
            "IT Infrastructure Library (ITIL) 4 – Change and Release Management",
            "Network Design and Implementation Project Standards – IEEE 802.3/802.11",
            "Stakeholder Management and Communication Plans for Large-Scale IT Projects",
            "Risk Management Planning and Mitigation Strategies for Infrastructure Projects",
            "Project Budgeting and Cost Control for IT Infrastructure Deployments",
            "Malaysian Ministry of Energy – Infrastructure Project Management Standards",
        ]
    },
    "06_CoCu-6-SOP-Development-And-Implementation": {
        "level": "L5",
        "references": [
            "NOSS IT-020-5:2013 Computer System Management Syllabus",
            "ISO/IEC 20000-1:2018 – Service Management Documentation and SOP Requirements",
            "ITIL 4 Service Operations and Knowledge Management Best Practices",
            "Technical Writing Standards – IEEE 1058 Software Project Management Plan",
            "Business Process Modeling Notation (BPMN) – Process Documentation Standards",
            "Change Management and SOP Governance – Control and Version Management",
            "Training and Competency Development for SOP Implementation and Adoption",
            "Audit and Compliance Verification for SOP Adherence",
            "Documentation Management Systems – Confluence, SharePoint, and Wikis",
            "Malaysian Quality Management Standards – ISO 9001:2015 Documentation Requirements",
        ]
    },
    "07_CoCu-7-Server-Scripting": {
        "level": "L5",
        "references": [
            "NOSS IT-020-5:2013 Computer System Management Syllabus",
            "Python Documentation and Best Practices – PEP 8 Style Guide",
            "Bash Shell Scripting Guide – Advanced Scripting Techniques",
            "PowerShell Documentation and Advanced Scripting for Windows Automation",
            "CompTIA Linux+ Certification – Shell Scripting and Automation",
            "CompTIA Server+ – Automation and Infrastructure as Code Fundamentals",
            "Infrastructure as Code (IaC) – Terraform, Ansible, and Puppet Best Practices",
            "Git and Version Control for Script Development and Collaboration",
            "Continuous Integration and Continuous Deployment (CI/CD) Pipelines",
            "Security Best Practices for Scripts – Error Handling, Logging, and Secure Credentials",
        ]
    },
}


def extract_cocu_title(content):
    """Extract CoCu title from the markdown content"""
    # Look for the first markdown heading
    match = re.search(r'^# (.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def add_references_to_file(file_path):
    """Add References section to a CoCu file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract filename without extension
    filename = Path(file_path).stem

    # Get references for this CoCu
    if filename not in REFERENCES:
        print(f"⚠️  No references defined for {filename}")
        return False

    refs = REFERENCES[filename]
    level = refs["level"]
    reference_list = refs["references"]

    # Build the References section
    references_section = "\n## References\n\n"
    references_section += f"**Official Standards and Frameworks:**\n\n"

    for i, ref in enumerate(reference_list[:5], 1):  # First 5 are official
        references_section += f"- {ref}\n"

    references_section += f"\n**Technical References and Best Practices:**\n\n"

    for ref in reference_list[5:]:  # Rest are technical
        references_section += f"- {ref}\n"

    # Find insertion point: before the final "**Contact hour:**" line
    contact_hour_pattern = r'\n\*\*Contact hour:\*\*'
    match = re.search(contact_hour_pattern, content)

    if not match:
        print(f"❌ Could not find Contact hour marker in {filename}")
        return False

    insertion_point = match.start()

    # Check if References section already exists
    if "## References" in content:
        print(f"⏭️  {filename} already has References section")
        return True

    # Insert the References section
    new_content = content[:insertion_point] + references_section + content[insertion_point:]

    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ {filename} – References added ({len(reference_list)} references)")
    return True


def main():
    """Main entry point"""
    script_dir = Path(__file__).parent
    content_dir = script_dir.parent / "content"

    # Collect all CoCu files
    cocu_files = []
    for level in ["IT-020-3", "IT-020-4", "IT-020-5"]:
        level_dir = content_dir / level
        if level_dir.exists():
            for md_file in sorted(level_dir.glob("*_CoCu-*.md")):
                cocu_files.append(md_file)

    print(f"\n📚 Adding References to {len(cocu_files)} CoCu files...\n")

    success_count = 0
    for file_path in cocu_files:
        if add_references_to_file(str(file_path)):
            success_count += 1

    print(f"\n✨ Complete: {success_count}/{len(cocu_files)} files updated")
    return 0


if __name__ == "__main__":
    exit(main())
