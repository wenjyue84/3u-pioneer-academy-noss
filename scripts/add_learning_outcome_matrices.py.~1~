"""
Add Learning Outcome Matrices to all CoCu markdown files.
Maps work activities to knowledge outcomes, performance outcomes, assessment methods, and evidence.
Usage: uv run scripts/add_learning_outcome_matrices.py
"""

import re
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_DIR / "content"

# Mapping of work activity keywords to learning outcome descriptions
ACTIVITY_OUTCOMES = {
    # L3 patterns
    "analyse": {
        "knowledge": "Identify and interpret requirements",
        "performance": "Analyse requirements and extract key priorities",
        "assessment": "Written test on requirement analysis; oral questions on decision criteria",
        "evidence": "Completed analysis checklist; documented decision rationale"
    },
    "prepare": {
        "knowledge": "Know tools, parts, and materials needed",
        "performance": "Gather and organize tools, parts, and materials",
        "assessment": "Practical observation of tool/material preparation; checklist verification",
        "evidence": "Photo/log of prepared toolkit; materials checklist"
    },
    "set-up": {
        "knowledge": "Understand installation procedures and hardware compatibility",
        "performance": "Correctly assemble and install components according to specifications",
        "assessment": "Practical hands-on assembly; functionality test verification",
        "evidence": "Correctly assembled system; successful test results"
    },
    "carry out": {
        "knowledge": "Know procedures and troubleshooting techniques",
        "performance": "Execute procedures and resolve issues",
        "assessment": "Practical demonstration; problem-solving observed",
        "evidence": "Completed task log; troubleshooting notes; final working state"
    },
    "install": {
        "knowledge": "Understand installation procedures and configuration options",
        "performance": "Successfully install and configure software or systems",
        "assessment": "Practical installation; verification of correct configuration",
        "evidence": "Installation log; system configuration screenshots; test results"
    },
    "test": {
        "knowledge": "Know testing procedures and acceptance criteria",
        "performance": "Execute tests and document results",
        "assessment": "Practical test execution; result documentation",
        "evidence": "Test results log; signed-off test report"
    },
    "manage": {
        "knowledge": "Understand management procedures and protocols",
        "performance": "Manage resources and processes according to procedures",
        "assessment": "Practical management task; documentation review",
        "evidence": "Management logs; configuration records; audit trail"
    },
    "develop": {
        "knowledge": "Understand design and development principles",
        "performance": "Design and develop systems/documents/procedures",
        "assessment": "Product review; quality assessment",
        "evidence": "Completed deliverable; design documentation; review feedback"
    },
    "configure": {
        "knowledge": "Understand configuration options and best practices",
        "performance": "Configure systems correctly according to requirements",
        "assessment": "Practical configuration; verification against requirements",
        "evidence": "Configuration screenshots; settings verification; test proof"
    },
    "monitor": {
        "knowledge": "Know monitoring tools and alert thresholds",
        "performance": "Monitor systems and respond to alerts",
        "assessment": "Practical monitoring; response to simulated alerts",
        "evidence": "Monitoring logs; incident response records"
    },
    "update": {
        "knowledge": "Understand update procedures and compatibility",
        "performance": "Successfully update systems and verify functionality",
        "assessment": "Practical update; post-update testing",
        "evidence": "Update log; version verification; test results"
    },
    "document": {
        "knowledge": "Know documentation standards and requirements",
        "performance": "Create complete and accurate documentation",
        "assessment": "Documentation review; accuracy verification",
        "evidence": "Completed documentation; review checklist"
    },
    "report": {
        "knowledge": "Know report formats and required information",
        "performance": "Generate accurate and complete reports",
        "assessment": "Report review; accuracy and completeness check",
        "evidence": "Signed-off report; supporting documentation"
    }
}


def extract_work_activities(content):
    """
    Extract work activities from contact hour distribution table.
    Table format: | % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
    """
    activities = []
    lines = content.split("\n")

    in_contact_table = False
    for i, line in enumerate(lines):
        if "Work activity" in line and "Knowledge 30%" in line:
            in_contact_table = True
            continue

        if in_contact_table:
            if line.strip().startswith("|") and "---" not in line and "100%" not in line:
                # Parse table row
                cells = [c.strip() for c in line.split("|")]
                cells = [c for c in cells if c]  # Remove empty cells

                if len(cells) >= 3 and cells[0].replace("%", "").replace("-", "").strip():
                    try:
                        # Try to parse first cell as percentage
                        pct_str = cells[0].replace("%", "").replace("-", "").strip()
                        if pct_str and any(c.isdigit() for c in pct_str):
                            activity = cells[2] if len(cells) > 2 else None
                            if activity and activity.lower() not in ["work activity", "total"]:
                                activities.append(activity)
                    except:
                        pass
            elif "---" not in line and line.strip().startswith("|") and "100%" in line:
                in_contact_table = False

    return activities


def get_learning_outcomes(activity):
    """
    Get learning outcome descriptions for a work activity.
    Matches activity keywords to predefined outcome templates.
    """
    activity_lower = activity.lower()

    # Check for keyword matches
    for keyword, outcomes in ACTIVITY_OUTCOMES.items():
        if keyword in activity_lower:
            return outcomes

    # Default outcomes if no match
    return {
        "knowledge": f"Understand concepts related to: {activity}",
        "performance": f"Successfully execute: {activity}",
        "assessment": "Practical demonstration and documentation review",
        "evidence": "Completed task documentation and supervisor sign-off"
    }


def create_learning_outcome_matrix(activities):
    """
    Create a Learning Outcome Matrix table from work activities.
    """
    matrix_lines = ["## Learning Outcome Matrix", ""]
    matrix_lines.append("| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |")
    matrix_lines.append("|---|---|---|---|---|")

    for activity in activities:
        outcomes = get_learning_outcomes(activity)

        # Clean activity text
        activity_clean = activity.strip()
        knowledge = outcomes["knowledge"].strip()
        performance = outcomes["performance"].strip()
        assessment = outcomes["assessment"].strip()
        evidence = outcomes["evidence"].strip()

        row = f"| {activity_clean} | {knowledge} | {performance} | {assessment} | {evidence} |"
        matrix_lines.append(row)

    matrix_lines.append("")
    return "\n".join(matrix_lines)


def add_matrix_to_file(file_path):
    """
    Add Learning Outcome Matrix to a CoCu file.
    Inserts before the Employability Skills section.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already has Learning Outcome Matrix
    if "## Learning Outcome Matrix" in content:
        print(f"  ✓ Already has Learning Outcome Matrix: {file_path.name}")
        return True

    # Extract work activities
    activities = extract_work_activities(content)
    if not activities:
        print(f"  ✗ Could not extract work activities from: {file_path.name}")
        return False

    # Create matrix
    matrix = create_learning_outcome_matrix(activities)

    # Find insertion point (before "## Employability Skills" or "## Attitude, Safety")
    insert_pattern = r"\n## Employability Skills|\n## Attitude, Safety"
    match = re.search(insert_pattern, content)

    if match:
        insert_pos = match.start()
        new_content = content[:insert_pos] + "\n" + matrix + "\n" + content[insert_pos:]
    else:
        print(f"  ✗ Could not find insertion point in: {file_path.name}")
        return False

    # Write updated content
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"  ✓ Added Learning Outcome Matrix: {file_path.name}")
    return True


def main():
    """Process all CoCu files across L3, L4, and L5."""
    coco_files = list(CONTENT_DIR.glob("IT-020-*/[0-9]*.md"))
    coco_files = sorted([f for f in coco_files if "Contact-hour" not in f.name])

    if not coco_files:
        print("No CoCu files found.")
        return

    print(f"Processing {len(coco_files)} CoCu files...\n")

    success_count = 0
    for file_path in coco_files:
        if add_matrix_to_file(file_path):
            success_count += 1

    print(f"\nCompleted: {success_count}/{len(coco_files)} files updated successfully")


if __name__ == "__main__":
    main()
