"""Tests for BEV Diagnostic Fault Code Scenario Generator (US-037)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
GENERATOR = PROJECT_ROOT / "bev-diagnostic-rectification" / "_tools" / "generate-scenarios.py"
JSON_FILE = PROJECT_ROOT / "bev-diagnostic-rectification" / "_tools" / "fault-code-scenarios.json"

import importlib.util

_spec = importlib.util.spec_from_file_location("generate_scenarios", str(GENERATOR))
assert _spec and _spec.loader
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]
load_fault_codes = _mod.load_fault_codes
create_scenario_question = _mod.create_scenario_question


def test_at_least_20_fault_codes() -> None:
    codes = load_fault_codes(JSON_FILE)
    assert len(codes) >= 20, f"Expected 20+ fault codes, got {len(codes)}"


def test_schema_fields() -> None:
    for entry in load_fault_codes(JSON_FILE):
        for key in ("fault_code", "component", "symptoms", "diagnosis_steps", "relevant_kps"):
            assert key in entry, f"Missing {key} in {entry.get('fault_code', '?')}"
        assert len(entry["symptoms"]) >= 1
        assert len(entry["diagnosis_steps"]) >= 1
        assert len(entry["relevant_kps"]) >= 1


def test_scenario_kp_links() -> None:
    valid = {f"C0{c}/KP-0{k}" for c in range(1, 4) for k in range(1, 7)}
    for entry in load_fault_codes(JSON_FILE):
        for kp in entry["relevant_kps"]:
            assert kp in valid, f"{entry['fault_code']}: invalid KP ref '{kp}'"


def test_systems_covered() -> None:
    codes = load_fault_codes(JSON_FILE)
    components = {c["component"] for c in codes}
    for keyword in ("Battery", "BMS", "Motor", "Thermal"):
        assert any(keyword in comp for comp in components), f"No component contains '{keyword}'"


def test_create_scenario_question_format() -> None:
    entry = load_fault_codes(JSON_FILE)[0]
    md = create_scenario_question(entry, 1)
    assert entry["fault_code"] in md
    assert "**Diagnosis Procedure:**" in md
    assert "**Reference:**" in md


def test_cli_runs() -> None:
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--list"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert "P0A80" in result.stdout
