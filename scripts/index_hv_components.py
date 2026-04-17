"""index_hv_components.py — BEV HV System Component Cross-Reference Indexer

Scans all bev-diagnostic-rectification/C**/KP*.md files, extracts HV component
mentions, cross-references against hv-component-index.json, and produces a
validation report flagging components missing safety_standard or voltage_range.

Usage:
    uv run python scripts/index_hv_components.py
    uv run python scripts/index_hv_components.py --update   # update JSON in-place
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_ROOT = Path(__file__).parent.parent
_KP_GLOB = "bev-diagnostic-rectification/C*/KP*.md"
_INDEX_PATH = _ROOT / "bev-diagnostic-rectification" / "_reference" / "hv-component-index.json"

# Keywords used to detect HV component mentions in markdown text
_COMPONENT_KEYWORDS: dict[str, list[str]] = {
    "HVC-001": ["traction battery pack", "pek bateri traksi", "hv battery pack", "battery pack"],
    "HVC-002": ["battery management system", "bms", "sistem pengurusan bateri"],
    "HVC-003": ["bms master controller", "pengawal induk bms"],
    "HVC-004": ["main positive contactor", "penyentuh positif utama"],
    "HVC-005": ["main negative contactor", "penyentuh negatif utama"],
    "HVC-006": ["pre-charge relay", "pre-charge resistor", "geganti pra-cas", "precharge"],
    "HVC-007": ["service plug", "manual service disconnect", "plag servis", "hv interlock", "interlock"],
    "HVC-008": ["hv cable", "high voltage cable", "kabel voltan tinggi", "orange cable"],
    "HVC-009": ["dc-dc converter", "penukar dc-dc", "dc/dc converter"],
    "HVC-010": ["on-board charger", "obc", "pengecas dalam kenderaan"],
    "HVC-011": ["inverter", "motor control unit", "mcu", "penyongsang"],
    "HVC-012": ["traction motor", "pmsm", "asm", "motor traksi"],
    "HVC-013": ["current sensor", "hall effect", "penderia arus"],
    "HVC-014": ["hv connector", "penyambung voltan tinggi", "orange connector"],
    "HVC-015": ["battery cell", "battery module", "sel bateri", "modul bateri", "lithium-ion cell"],
    "HVC-016": ["electric compressor", "pemampat elektrik", "hvac compressor"],
    "HVC-017": ["electric water pump", "pam air elektrik", "coolant pump"],
    "HVC-018": ["hv fuse", "pyrofuse", "fius voltan tinggi", "pirofius"],
}


def extract_components(md_content: str, cu_label: str) -> dict[str, str]:
    """Scan markdown text and return {component_id: cu_label} for each match.

    Args:
        md_content: Full text of a KP markdown file.
        cu_label: CU identifier (e.g. "C02") for cross-referencing.

    Returns:
        Dict mapping component IDs to the cu_label for each component detected.
    """
    text_lower = md_content.lower()
    found: dict[str, str] = {}
    for comp_id, keywords in _COMPONENT_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                found[comp_id] = cu_label
                break
    return found


def validate_safety_fields(component: dict[str, Any]) -> list[str]:
    """Validate that a component entry has required safety and voltage fields.

    Args:
        component: A single component dict from hv-component-index.json.

    Returns:
        List of validation error strings; empty list if component is valid.
    """
    errors: list[str] = []
    comp_id = component.get("id", "UNKNOWN")
    name = component.get("name_en", comp_id)

    if not component.get("voltage_range", "").strip():
        errors.append(f"[{comp_id}] '{name}' is missing voltage_range specification")

    if not component.get("safety_standard", "").strip():
        errors.append(f"[{comp_id}] '{name}' is missing safety_standard")

    if not component.get("name_bm", "").strip():
        errors.append(f"[{comp_id}] '{name}' is missing Bahasa Malaysia name (name_bm)")

    return errors


def scan_kp_files(root: Path | None = None) -> dict[str, list[str]]:
    """Scan all KP*.md files under bev-diagnostic-rectification/C**/ and return
    a mapping of {component_id: [cu_labels...]} indicating which CUs reference it.

    Args:
        root: Repository root path; defaults to the project root.

    Returns:
        Dict of component_id -> sorted list of CU labels.
    """
    if root is None:
        root = _ROOT

    cu_pattern = re.compile(r"/(C\d+)/KP", re.IGNORECASE)
    component_cus: dict[str, set[str]] = {cid: set() for cid in _COMPONENT_KEYWORDS}

    kp_files = sorted(root.glob(_KP_GLOB))
    for kp_file in kp_files:
        m = cu_pattern.search(kp_file.as_posix())
        cu_label = m.group(1).upper() if m else kp_file.parent.name.upper()

        content = kp_file.read_text(encoding="utf-8")
        matches = extract_components(content, cu_label)
        for comp_id in matches:
            component_cus[comp_id].add(cu_label)

    return {cid: sorted(cus) for cid, cus in component_cus.items()}


def build_index(existing_index: dict[str, Any], scanned_cus: dict[str, list[str]]) -> dict[str, Any]:
    """Merge scanned CU references back into the existing index.

    Only updates the ``cus_referenced`` field; all other fields are preserved.

    Args:
        existing_index: Loaded JSON content of hv-component-index.json.
        scanned_cus: Output from scan_kp_files().

    Returns:
        Updated index dict with refreshed cus_referenced per component.
    """
    updated = dict(existing_index)
    components = [dict(c) for c in updated.get("components", [])]
    for comp in components:
        cid = comp.get("id", "")
        if cid in scanned_cus:
            found = scanned_cus[cid]
            # Merge with existing manually-curated list
            merged = sorted(set(comp.get("cus_referenced", [])) | set(found))
            comp["cus_referenced"] = merged
    updated["components"] = components
    return updated


def generate_validation_report(index: dict[str, Any]) -> list[str]:
    """Run validate_safety_fields() on every component and return all findings.

    Also flags components with empty cus_referenced (not found in any KP).

    Args:
        index: Loaded/updated hv-component-index.json content.

    Returns:
        List of human-readable finding strings; empty list = all clear.
    """
    findings: list[str] = []
    for comp in index.get("components", []):
        findings.extend(validate_safety_fields(comp))
        if not comp.get("cus_referenced"):
            findings.append(
                f"[{comp.get('id','?')}] '{comp.get('name_en','')}' "
                "not found in any KP file — verify component name keywords"
            )
    return findings


def main() -> None:
    """CLI entry-point: scan KP files, validate, optionally update JSON."""
    update_mode = "--update" in sys.argv

    if not _INDEX_PATH.exists():
        print(f"ERROR: Index file not found: {_INDEX_PATH}", file=sys.stderr)
        sys.exit(1)

    index = json.loads(_INDEX_PATH.read_text(encoding="utf-8"))
    component_count = len(index.get("components", []))
    print(f"Loaded index: {component_count} components from {_INDEX_PATH.name}")

    print(f"\nScanning KP files under {_ROOT / 'bev-diagnostic-rectification'} ...")
    scanned_cus = scan_kp_files(_ROOT)
    found_total = sum(len(v) for v in scanned_cus.values())
    print(f"Scan complete: {found_total} component-CU associations detected")

    updated_index = build_index(index, scanned_cus)

    findings = generate_validation_report(updated_index)
    print(f"\n--- Validation Report ({len(findings)} finding(s)) ---")
    if findings:
        for f in findings:
            print(f"  WARN: {f}")
    else:
        print("  All components have required safety_standard and voltage_range fields.")

    if update_mode:
        _INDEX_PATH.write_text(
            json.dumps(updated_index, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"\nIndex updated in-place: {_INDEX_PATH}")
    else:
        print("\nRun with --update to write scan results back to hv-component-index.json")


if __name__ == "__main__":
    main()
