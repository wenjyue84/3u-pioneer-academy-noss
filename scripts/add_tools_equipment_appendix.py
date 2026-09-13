#!/usr/bin/env python3
"""
Add Tools and Equipment List appendix to contact hour files.
Consolidates all tools, software, and equipment required across all CoCu units.
"""

import re
from pathlib import Path
from collections import defaultdict

PROJECT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_DIR / "content"

LEVELS = {
    "3": {
        "cocu_dir": CONTENT_DIR / "IT-020-3",
        "contact_file": "00_Contact-hour_IT-020-3-L3-Operation.md",
        "level_name": "L3 (Operation)",
    },
    "4": {
        "cocu_dir": CONTENT_DIR / "IT-020-4",
        "contact_file": "00_Contact-hour_IT-020-4-L4-Administration.md",
        "level_name": "L4 (Administration)",
    },
    "5": {
        "cocu_dir": CONTENT_DIR / "IT-020-5",
        "contact_file": "00_Contact-hour_IT-020-5-L5-Management.md",
        "level_name": "L5 (Management)",
    },
}


def extract_tools_from_cocu(cocu_path):
    """Extract tools/equipment table from a CoCu file."""
    text = cocu_path.read_text(encoding="utf-8")
    tools = []

    # Find table with tools/equipment (Type of Tools, Hardware Component, Software Type, etc.)
    lines = text.split("\n")
    in_table = False
    current_table = []
    is_tools_table = False

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Check if this might be a tools table (look for headers)
        if stripped.startswith("|") and not in_table:
            # Check the header row for keywords
            if any(
                keyword in stripped.lower()
                for keyword in ["type of", "component", "software", "tools", "equipment"]
            ):
                is_tools_table = True
                in_table = True
                current_table = [line]
        elif in_table and stripped.startswith("|"):
            current_table.append(line)
        elif in_table and not stripped.startswith("|"):
            # End of table
            if is_tools_table and len(current_table) > 2:
                # Parse this table
                parsed_tools = parse_tools_table(current_table, cocu_path.stem)
                tools.extend(parsed_tools)
            in_table = False
            is_tools_table = False
            current_table = []

    return tools


def parse_tools_table(table_lines, cocu_name):
    """Parse a tools table and extract structured data."""
    tools = []

    # Parse table rows
    rows = []
    for line in table_lines:
        cells = [c.strip() for c in line.split("|")]
        # Remove empty first/last from leading/trailing |
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        if cells:
            rows.append(cells)

    # Skip separator row if present
    if len(rows) > 1 and all(re.match(r"^[-:]+$", c) for c in rows[1] if c):
        header_row = rows[0]
        data_rows = rows[2:]
    else:
        header_row = rows[0] if rows else []
        data_rows = rows[1:] if len(rows) > 1 else []

    # Extract tools with descriptions
    for row in data_rows:
        if len(row) >= 2:
            tool_name = row[0].strip()
            description = row[1].strip() if len(row) > 1 else ""

            # Skip empty rows or summary rows
            if not tool_name or tool_name.startswith("**") or tool_name.lower() == "total":
                continue

            tools.append(
                {
                    "name": tool_name,
                    "description": description,
                    "cocu": cocu_name,
                }
            )

    return tools


def consolidate_tools(tools_list):
    """Consolidate tools, removing duplicates."""
    seen = {}
    consolidated = []

    for tool in tools_list:
        key = tool["name"].lower()
        if key not in seen:
            seen[key] = tool
            consolidated.append(tool)

    return consolidated


def create_tools_appendix_table(tools):
    """Create a markdown table for tools and equipment."""
    if not tools:
        return ""

    lines = [
        "| Tool / Equipment | Description | Category |",
        "|---|---|---|",
    ]

    categories = {
        "screwdriver": "Hand Tools",
        "multimeter": "Testing Equipment",
        "tester": "Testing Equipment",
        "cable": "Network Equipment",
        "lan": "Network Equipment",
        "anti-static": "ESD Protection",
        "mat": "ESD Protection",
        "strap": "ESD Protection",
        "usb": "Installation Media",
        "optical": "Installation Media",
        "media": "Installation Media",
        "label": "Labeling Equipment",
        "cpu": "Hardware Components",
        "ram": "Hardware Components",
        "motherboard": "Hardware Components",
        "storage": "Hardware Components",
        "disk": "Hardware Components",
        "drive": "Hardware Components",
        "ssd": "Hardware Components",
        "nvme": "Hardware Components",
        "power supply": "Hardware Components",
        "psu": "Hardware Components",
        "peripheral": "Peripherals",
        "monitor": "Peripherals",
        "keyboard": "Peripherals",
        "mouse": "Peripherals",
        "printer": "Peripherals",
        "operating system": "Software",
        "driver": "Software",
        "application": "Software",
        "utility": "Software",
        "firmware": "Software",
    }

    for tool in tools:
        name = tool["name"]
        desc = tool["description"][:100] if tool["description"] else "See CoCu documentation"

        # Categorize
        category = "Other"
        name_lower = name.lower()
        for keyword, cat in categories.items():
            if keyword in name_lower:
                category = cat
                break

        lines.append(f"| {name} | {desc} | {category} |")

    return "\n".join(lines)


def add_appendix_to_contact_hour(level_key):
    """Add Tools and Equipment appendix to a contact hour file."""
    level_info = LEVELS[level_key]
    cocu_dir = level_info["cocu_dir"]
    contact_file = cocu_dir / level_info["contact_file"]

    if not contact_file.exists():
        print(f"[SKIP] Contact hour file not found: {contact_file}")
        return False

    # Extract tools from all CoCu files
    cocu_files = sorted(cocu_dir.glob("*_CoCu-*.md"))
    all_tools = []

    for cocu_file in cocu_files:
        tools = extract_tools_from_cocu(cocu_file)
        all_tools.extend(tools)
        print(f"  Extracted {len(tools)} tools from {cocu_file.name}")

    # Consolidate tools
    consolidated = consolidate_tools(all_tools)
    print(f"  Consolidated to {len(consolidated)} unique tools")

    # Create appendix content
    appendix_header = "## Tools and Equipment List Appendix\n\n"
    appendix_intro = (
        "The following table lists all tools, software, and equipment required across all competency units "
        "in this level. Quantities and specific models should be confirmed according to institutional "
        "purchasing policies and current availability.\n\n"
    )
    appendix_table = create_tools_appendix_table(consolidated)

    appendix_content = appendix_header + appendix_intro + appendix_table

    # Read the current contact hour file
    text = contact_file.read_text(encoding="utf-8")

    # Check if appendix already exists
    if "## Tools and Equipment List Appendix" in text:
        print(f"  [SKIP] Appendix already exists in {contact_file.name}")
        return False

    # Find insertion point: before "## CoCu documents" or at end
    insertion_point = text.rfind("## CoCu documents")
    if insertion_point == -1:
        # No CoCu documents section, add at end
        insertion_point = len(text)

    # Insert the appendix
    new_text = text[:insertion_point] + appendix_content + "\n\n---\n\n" + text[insertion_point:]

    # Write back
    contact_file.write_text(new_text, encoding="utf-8")
    print(f"  ✓ Added Tools and Equipment appendix to {contact_file.name}")
    return True


def main():
    """Add Tools and Equipment appendix to all contact hour files."""
    print("\n=== Adding Tools and Equipment List Appendix ===\n")

    success_count = 0
    for level_key in ["3", "4", "5"]:
        level_info = LEVELS[level_key]
        print(f"\nLevel {level_key} ({level_info['level_name']}):")
        if add_appendix_to_contact_hour(level_key):
            success_count += 1

    print(f"\n✓ Completed: {success_count}/3 contact hour files updated")


if __name__ == "__main__":
    main()
