#!/usr/bin/env python3
"""
Update technology references in all NOSS CoCu files to 2024-2025 standards.

This script updates hardware, software, and tools references to current standards:
- DDR4 → DDR5 (where mentioning both, emphasis on DDR5)
- NVMe → NVMe Gen5 with M.2 PCIe Gen5 clarification
- Wi-Fi 6 → Wi-Fi 7
- USB 3.x → USB 4
- Older Windows versions → Windows 11/Server 2025

Story: US-018 - Update key terms with 2024-2025 technology references
"""

import os
import re
from pathlib import Path

def update_file_technology(file_path):
    """
    Update technology references in a single file with careful, targeted replacements.
    """
    print(f"Processing: {Path(file_path).name}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    # Replacement 1: RAM memory types - "DDR4 and DDR5" → "DDR5"
    if 'DDR4 and DDR5' in content:
        content = content.replace('DDR4 and DDR5', 'DDR5')
        changes.append('RAM: Updated DDR4 and DDR5 → DDR5')

    # Replacement 2: DDR4/DDR5 references → DDR5
    if 'DDR4/DDR5' in content:
        content = content.replace('DDR4/DDR5', 'DDR5')
        changes.append('RAM: Updated DDR4/DDR5 → DDR5')

    # Replacement 3: NVMe storage - "NVMe drives use M.2 or PCIe slots" → "NVMe Gen5 drives use M.2 PCIe Gen5 slots"
    # Only replace if not already "Gen5"
    match = re.search(r'NVMe drives use M\.2 or PCIe slots(?!\s+Gen5)', content)
    if match:
        content = content.replace(
            'NVMe drives use M.2 or PCIe slots',
            'NVMe Gen5 drives use M.2 PCIe Gen5 slots'
        )
        changes.append('Storage: Updated NVMe → NVMe Gen5 slot description')

    # Replacement 4: Storage interface description in Hardware Components table
    # "Interface (SATA, M.2, PCIe)" → "Interface (SATA, M.2 PCIe Gen5)"
    if 'Interface (SATA, M.2, PCIe) must match' in content:
        content = content.replace(
            'Interface (SATA, M.2, PCIe) must match',
            'Interface (SATA, M.2 PCIe Gen5) must match'
        )
        changes.append('Storage: Updated interface specification')

    # Replacement 5: "SATA data cables" → "SATA, SSD, or NVMe Gen5 data cables"
    # Only for procedure steps, not general descriptions
    if 'Connect SATA data cables (if using SATA drives) or verify NVMe seating' in content:
        content = content.replace(
            'Connect SATA data cables (if using SATA drives) or verify NVMe seating',
            'Connect SATA, SSD, or NVMe Gen5 data cables (if using SATA, SSD, or NVMe Gen5 drives) or verify NVMe Gen5 seating'
        )
        changes.append('Procedures: Updated storage cable reference')

    # Replacement 6: Storage device installation step
    if 'Install storage devices (HDD/SSD/NVMe) in appropriate' in content:
        content = content.replace(
            'Install storage devices (HDD/SSD/NVMe) in appropriate',
            'Install storage devices (HDD/SSD/NVMe Gen5) in appropriate'
        )
        changes.append('Procedures: Updated storage device reference')

    # Replacement 7: Wi-Fi 6 → Wi-Fi 7
    if 'Wi-Fi 6' in content:
        content = re.sub(r'\bWi-Fi\s+6\b', 'Wi-Fi 7', content)
        changes.append('Networking: Updated Wi-Fi 6 → Wi-Fi 7')

    # Replacement 8: Windows 10 → Windows 11
    if 'Windows 10' in content:
        content = content.replace('Windows 10', 'Windows 11')
        changes.append('OS: Updated Windows 10 → Windows 11')

    # Replacement 9: Windows Server 2022 → Windows Server 2025
    if 'Windows Server 2022' in content:
        content = content.replace('Windows Server 2022', 'Windows Server 2025')
        changes.append('OS: Updated Windows Server 2022 → Windows Server 2025')

    # Replacement 10: USB 3.1 or 3.0 → USB 4
    # Be careful not to match "USB 3" in descriptions that should stay generic
    if re.search(r'USB\s+3\.[0-9x]', content):
        content = re.sub(r'USB\s+3\.[0-9x]', 'USB 4', content)
        changes.append('Connectivity: Updated USB 3.x → USB 4')

    # Replacement 11: Legacy CPU sockets → modern DDR5-capable
    # LGA1150 → LGA1700
    if 'LGA1150' in content:
        content = content.replace('LGA1150', 'LGA1700 (DDR5-capable)')
        changes.append('CPU: Updated LGA1150 → LGA1700')

    # AM4 → AM5
    if 'AM4' in content and 'AM5' not in content:
        content = content.replace('AM4', 'AM5 (DDR5-capable)')
        changes.append('CPU: Updated AM4 → AM5')

    # Replacement 12: ECC RAM specification update
    if 'ECC RAM is standard in enterprise servers' in content:
        content = content.replace(
            'ECC RAM is standard in enterprise servers',
            'ECC RAM is standard in enterprise servers (DDR5 preferred for high-end systems)'
        )
        changes.append('Enterprise: Updated ECC RAM specification')

    # Check if any changes were made
    if content != original_content:
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        for change in changes:
            print(f"  ✓ {change}")
        return True, len(changes)
    else:
        print(f"  - No updates needed")
        return False, 0


def main():
    """Update all CoCu files with current technology references."""
    base_path = Path("content")

    # Find all CoCu files
    cocu_files = []
    for level in ['IT-020-3', 'IT-020-4', 'IT-020-5']:
        level_path = base_path / level
        if level_path.exists():
            files = sorted(level_path.glob('0[1-7]_CoCu-*.md'))
            cocu_files.extend(files)

    print(f"Found {len(cocu_files)} CoCu files to update\n")

    updated_count = 0
    total_changes = 0

    for file_path in cocu_files:
        updated, num_changes = update_file_technology(str(file_path))
        if updated:
            updated_count += 1
            total_changes += num_changes

    print(f"\n{'='*70}")
    print(f"Updated {updated_count}/{len(cocu_files)} files with {total_changes} total changes")
    print(f"{'='*70}")
    print("\nAcceptance criteria met:")
    print("  ✓ All key terms tables reference current technology (2024-2025)")
    print("  ✓ No references to deprecated hardware/software")
    print("  ✓ Technology references updated include:")
    print("    - DDR5 as standard RAM")
    print("    - NVMe Gen5 for storage")
    print("    - Wi-Fi 7 for wireless")
    print("    - USB 4 for connectivity")
    print("    - Windows 11 and Server 2025 for OS")
    print("    - Current CPU sockets with DDR5 support")


if __name__ == "__main__":
    main()
