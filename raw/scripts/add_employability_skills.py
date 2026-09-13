#!/usr/bin/env python3
"""
Add Employability Skills sections to CoCu files.
Handles L4 (administrative) and L5 (management) levels.
"""

import re
from pathlib import Path

# Templates for employability skills by level
L4_TEMPLATE = """## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Mapping:** Document planning and implementation decisions; present recommendations to management; communicate with stakeholders and project teams

### 2. Teamwork & Collaboration
- **Mapping:** Lead technical teams on implementation; coordinate across departments; share knowledge on best practices and systems management

### 3. Problem-solving
- **Mapping:** Diagnose complex system issues; evaluate solution options; implement sustainable fixes and preventive measures

### 4. Initiative & Self-reliance
- **Mapping:** Take responsibility for technical decisions; manage implementation projects; supervise technical staff

### 5. Planning & Organizing
- **Mapping:** Plan system implementations and configurations; organize resources and schedules; manage project timelines and budgets

### 6. Self-management & Safety Awareness
- **Mapping:** Follow change management and approval procedures; manage risk of system downtime; maintain security and compliance standards

### 7. Technology Use & Technical Proficiency
- **Mapping:** Configure complex systems; troubleshoot using advanced tools; manage system infrastructure and databases

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Stay current on new technologies and standards; analyze implementation results; improve procedures and documentation

"""

L5_TEMPLATE = """## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Mapping:** Present strategic recommendations to senior management; prepare reports for board and compliance audiences; communicate vision and strategy

### 2. Teamwork & Collaboration
- **Mapping:** Lead multi-disciplinary teams; collaborate with executive leadership; coordinate across organizational boundaries

### 3. Problem-solving
- **Mapping:** Address strategic challenges; evaluate complex trade-offs; develop enterprise-wide solutions

### 4. Initiative & Self-reliance
- **Mapping:** Drive strategic initiatives; make high-impact decisions; take responsibility for organizational outcomes

### 5. Planning & Organizing
- **Mapping:** Develop strategic plans; align with business objectives; manage portfolio of initiatives

### 6. Self-management & Safety Awareness
- **Mapping:** Manage organizational risk and governance; ensure regulatory compliance; maintain security and business continuity

### 7. Technology Use & Technical Proficiency
- **Mapping:** Use strategic planning and analysis tools; manage enterprise systems and infrastructure; leverage data for decision-making

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Drive continuous improvement culture; stay informed on emerging technologies; foster innovation and learning

"""

def add_employability_skills(filepath, level):
    """Add employability skills section to a CoCu file."""
    content = filepath.read_text(encoding='utf-8')

    # Check if section already exists
    if '## Employability Skills' in content:
        print(f"✓ {filepath.name} already has Employability Skills section")
        return False

    # Select template
    template = L5_TEMPLATE if level == 5 else L4_TEMPLATE

    # Find insertion point (before Contact hour reference)
    contact_hour_pattern = r'\n\n\*\*Contact hour:\*\*'
    match = re.search(contact_hour_pattern, content)

    if not match:
        print(f"✗ {filepath.name} - could not find Contact hour reference")
        return False

    # Insert employability skills section
    insert_pos = match.start()
    new_content = content[:insert_pos] + '\n\n' + template + content[insert_pos:]

    filepath.write_text(new_content, encoding='utf-8')
    print(f"✓ {filepath.name} - Employability Skills added")
    return True

# Process L4 and L5 files
content_dir = Path('content')

l4_files = sorted(content_dir.glob('IT-020-4/*CoCu-*.md'))
l5_files = sorted(content_dir.glob('IT-020-5/*CoCu-*.md'))

print("Processing L4 files...")
l4_count = sum(1 for f in l4_files if add_employability_skills(f, 4))

print(f"\nProcessing L5 files...")
l5_count = sum(1 for f in l5_files if add_employability_skills(f, 5))

print(f"\nTotal files updated: {l4_count + l5_count}/13 (L4: {l4_count}, L5: {l5_count})")
