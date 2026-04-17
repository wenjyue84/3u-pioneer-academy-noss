"""tests/test_hv_component_index.py — Tests for BEV HV Component Indexer (US-038)"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Load the module under test without requiring a package __init__.py
# ---------------------------------------------------------------------------
_SCRIPTS = Path(__file__).parent.parent / "scripts"
_INDEX_PATH = (
    Path(__file__).parent.parent
    / "bev-diagnostic-rectification"
    / "_reference"
    / "hv-component-index.json"
)

spec = importlib.util.spec_from_file_location(
    "index_hv_components", _SCRIPTS / "index_hv_components.py"
)
assert spec and spec.loader
_mod = importlib.util.module_from_spec(spec)
sys.modules["index_hv_components"] = _mod
spec.loader.exec_module(_mod)  # type: ignore[union-attr]

extract_components = _mod.extract_components
validate_safety_fields = _mod.validate_safety_fields
scan_kp_files = _mod.scan_kp_files
build_index = _mod.build_index
generate_validation_report = _mod.generate_validation_report


# ---------------------------------------------------------------------------
# 1. JSON index file tests
# ---------------------------------------------------------------------------


class TestHvComponentIndexFile:
    def test_index_file_exists(self) -> None:
        assert _INDEX_PATH.exists(), f"Index file not found: {_INDEX_PATH}"

    def test_index_has_at_least_15_components(self) -> None:
        data = json.loads(_INDEX_PATH.read_text(encoding="utf-8"))
        assert len(data["components"]) >= 15, (
            f"Expected >=15 components, got {len(data['components'])}"
        )

    def test_every_component_has_required_fields(self) -> None:
        data = json.loads(_INDEX_PATH.read_text(encoding="utf-8"))
        required = {"id", "name_en", "name_bm", "function", "voltage_range", "safety_standard", "cus_referenced"}
        for comp in data["components"]:
            missing = required - comp.keys()
            assert not missing, f"Component {comp.get('id','?')} missing fields: {missing}"

    def test_every_component_has_nonempty_voltage_and_safety(self) -> None:
        data = json.loads(_INDEX_PATH.read_text(encoding="utf-8"))
        for comp in data["components"]:
            assert comp["voltage_range"].strip(), (
                f"{comp['id']} has empty voltage_range"
            )
            assert comp["safety_standard"].strip(), (
                f"{comp['id']} has empty safety_standard"
            )

    def test_cus_referenced_lists_valid_cu_labels(self) -> None:
        data = json.loads(_INDEX_PATH.read_text(encoding="utf-8"))
        valid_labels = {"C01", "C02", "C03", "C04", "C05"}
        for comp in data["components"]:
            for cu in comp["cus_referenced"]:
                assert cu in valid_labels, (
                    f"{comp['id']} references unknown CU label '{cu}'"
                )


# ---------------------------------------------------------------------------
# 2. extract_components() unit tests
# ---------------------------------------------------------------------------


class TestExtractComponents:
    def test_detects_bms_keyword(self) -> None:
        text = "The Battery Management System (BMS) monitors cell voltages."
        result = extract_components(text, "C02")
        assert "HVC-002" in result
        assert result["HVC-002"] == "C02"

    def test_detects_service_plug_keyword(self) -> None:
        text = "Always remove the service plug before commencing HV work."
        result = extract_components(text, "C01")
        assert "HVC-007" in result

    def test_detects_dc_dc_converter(self) -> None:
        text = "The DC-DC converter steps down HV battery voltage to 12V."
        result = extract_components(text, "C03")
        assert "HVC-009" in result

    def test_case_insensitive(self) -> None:
        text = "Replace the ON-BOARD CHARGER (OBC) if fault code appears."
        result = extract_components(text, "C04")
        assert "HVC-010" in result

    def test_no_match_returns_empty(self) -> None:
        text = "Torque the wheel bolts to 110 Nm."
        result = extract_components(text, "C01")
        # No HV component keywords present
        assert result == {}


# ---------------------------------------------------------------------------
# 3. validate_safety_fields() unit tests
# ---------------------------------------------------------------------------


class TestValidateSafetyFields:
    def _make_comp(self, **kwargs: str) -> dict:
        base = {
            "id": "HVC-TEST",
            "name_en": "Test Component",
            "name_bm": "Komponen Ujian",
            "function": "Test function",
            "voltage_range": "200-800V DC",
            "safety_standard": "IEC 99999",
            "cus_referenced": ["C01"],
        }
        base.update(kwargs)
        return base

    def test_valid_component_has_no_errors(self) -> None:
        comp = self._make_comp()
        assert validate_safety_fields(comp) == []

    def test_missing_voltage_range_flagged(self) -> None:
        comp = self._make_comp(voltage_range="")
        errors = validate_safety_fields(comp)
        assert any("voltage_range" in e for e in errors)

    def test_missing_safety_standard_flagged(self) -> None:
        comp = self._make_comp(safety_standard="")
        errors = validate_safety_fields(comp)
        assert any("safety_standard" in e for e in errors)

    def test_missing_name_bm_flagged(self) -> None:
        comp = self._make_comp(name_bm="")
        errors = validate_safety_fields(comp)
        assert any("name_bm" in e for e in errors)

    def test_multiple_missing_fields_all_reported(self) -> None:
        comp = self._make_comp(voltage_range="", safety_standard="")
        errors = validate_safety_fields(comp)
        assert len(errors) >= 2


# ---------------------------------------------------------------------------
# 4. scan_kp_files() integration test
# ---------------------------------------------------------------------------


class TestScanKpFiles:
    def test_scan_detects_bms_in_c02(self) -> None:
        root = Path(__file__).parent.parent
        scanned = scan_kp_files(root)
        # BMS should appear in C02 (KP-01.md has BMS content)
        assert "C02" in scanned.get("HVC-002", []) or "C03" in scanned.get("HVC-002", [])

    def test_scan_returns_all_component_ids(self) -> None:
        root = Path(__file__).parent.parent
        scanned = scan_kp_files(root)
        from index_hv_components import _COMPONENT_KEYWORDS  # type: ignore[import]
        for cid in _COMPONENT_KEYWORDS:
            assert cid in scanned, f"Component {cid} missing from scan output"


# ---------------------------------------------------------------------------
# 5. generate_validation_report() tests
# ---------------------------------------------------------------------------


class TestGenerateValidationReport:
    def test_valid_index_produces_no_findings(self) -> None:
        data = json.loads(_INDEX_PATH.read_text(encoding="utf-8"))
        findings = generate_validation_report(data)
        # The curated JSON should pass validation
        assert findings == [], f"Unexpected validation findings: {findings}"

    def test_component_with_empty_voltage_produces_finding(self) -> None:
        index = {
            "components": [
                {
                    "id": "HVC-X01",
                    "name_en": "Fake Component",
                    "name_bm": "Komponen Palsu",
                    "function": "Nothing",
                    "voltage_range": "",
                    "safety_standard": "IEC 00001",
                    "cus_referenced": ["C01"],
                }
            ]
        }
        findings = generate_validation_report(index)
        assert any("voltage_range" in f for f in findings)
