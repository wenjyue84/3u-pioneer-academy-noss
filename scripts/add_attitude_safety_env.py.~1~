#!/usr/bin/env python3
"""
Add Attitude, Safety and Environmental sections to all CoCu files.
Per NOSS standards, each CoCu must have this section covering workplace safety,
environmental considerations, and professional attitudes.
"""

import re
from pathlib import Path

def get_attitude_safety_section(file_path, level):
    """Generate context-specific Attitude, Safety and Environmental section."""

    # Extract CoCu title from file path for context
    filename = file_path.stem

    if level == "L3":
        return """## Attitude, Safety and Environmental

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
- **Attention to Detail:** Verify every connection, configuration setting, and test result to ensure systems are correctly set up and function as intended."""

    elif level == "L4":
        return """## Attitude, Safety and Environmental

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
- **Accountability:** Take responsibility for system stability and performance; proactively monitor configurations and respond quickly to issues that could impact business operations."""

    else:  # L5
        return """## Attitude, Safety and Environmental

### Workplace Safety
- **Enterprise Risk Governance:** Establish and maintain governance frameworks that identify, assess, and mitigate IT-related risks at the organisational level. Ensure compliance with regulatory requirements and industry standards (ISO 27001, COBIT, ITIL).
- **Change Management at Scale:** Implement formal change management processes that balance innovation with stability; ensure all significant infrastructure changes are reviewed, approved, and documented for organisational accountability.
- **Cybersecurity Leadership:** Foster a culture of security awareness throughout the organisation; establish policies and procedures that protect critical systems, data, and intellectual property from threats.
- **Crisis Preparedness:** Develop and maintain disaster recovery and business continuity plans that protect the organisation's ability to operate during emergencies.

### Environmental Considerations
- **Sustainable IT Strategy:** Develop long-term IT strategies that consider environmental impact; promote energy-efficient infrastructure, virtualisation, and cloud solutions that reduce organisational carbon footprint.
- **Responsible Technology Governance:** Establish policies for responsible technology use, data privacy, and ethical IT practices that align with organisational values and community expectations.

### Professional Attitudes
- **Strategic Integrity:** Make decisions based on long-term organisational benefit; resist short-term pressures that could compromise system stability, security, or sustainability.
- **Visionary Leadership:** Champion innovation and emerging technologies while balancing risk; inspire teams to think strategically about technology's role in organisational success.
- **Stakeholder Trust:** Maintain credibility with executive leadership, boards, and external partners through transparent communication, ethical conduct, and delivery of promised results.
- **Continuous Improvement Culture:** Foster an environment where teams continuously learn from experiences, share knowledge, and improve processes to enhance organisational capability and competitiveness."""


def add_attitude_safety_section(file_path):
    """Add Attitude, Safety and Environmental section to a CoCu file."""

    # Determine level from file path
    if "IT-020-3" in str(file_path):
        level = "L3"
    elif "IT-020-4" in str(file_path):
        level = "L4"
    elif "IT-020-5" in str(file_path):
        level = "L5"
    else:
        print(f"⚠️  Skipped {file_path.name}: Unknown level")
        return False

    try:
        content = file_path.read_text(encoding='utf-8')

        # Check if section already exists
        if "## Attitude, Safety and Environmental" in content:
            print(f"✓ {file_path.name}: Section already exists")
            return False

        # Find the position to insert - before the Contact hour link
        # Pattern: \n\n**Contact hour:**
        pattern = r'\n\n\*\*Contact hour:\*\*'
        match = re.search(pattern, content)

        if not match:
            print(f"⚠️  Skipped {file_path.name}: Could not find Contact hour reference")
            return False

        insert_pos = match.start()

        # Get the section content
        section = get_attitude_safety_section(file_path, level)

        # Insert the section with proper spacing
        new_content = content[:insert_pos] + "\n\n" + section + content[insert_pos:]

        # Write back
        file_path.write_text(new_content, encoding='utf-8')
        print(f"✓ {file_path.name}: Section added")
        return True

    except Exception as e:
        print(f"✗ {file_path.name}: Error - {e}")
        return False


def main():
    """Process all CoCu files."""
    content_dir = Path("content")

    if not content_dir.exists():
        print("Error: content/ directory not found")
        return

    # Find all CoCu files
    cocu_files = list(content_dir.glob("IT-020-*/[0-9]*_CoCu-*.md"))
    cocu_files.sort()

    if not cocu_files:
        print("No CoCu files found")
        return

    print(f"Processing {len(cocu_files)} CoCu files...\n")

    added = 0
    for file_path in cocu_files:
        if add_attitude_safety_section(file_path):
            added += 1

    print(f"\n✅ Added sections to {added}/{len(cocu_files)} files")


if __name__ == "__main__":
    main()
