"""Tests for Aesthetic C04 Performance Assessment modality coverage (US-023)."""
from __future__ import annotations

from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
_PA_DIR = PROJECT_ROOT / "aesthetic-services" / "C04"
_pa_matches = sorted(_PA_DIR.glob("PA*.md")) if _PA_DIR.is_dir() else []
PA_PATH = _pa_matches[0] if _pa_matches else _PA_DIR / "PA.md"

REQUIRED_MODALITIES = [
    "microcurrent",
    "high frequency",
    "ultrasonic",
    "galvanic",
    "ems",
    "led light therapy",
]


@pytest.fixture()
def pa_content() -> str:
    """Read PA.md content once for all tests."""
    return PA_PATH.read_text(encoding="utf-8").lower()


def test_six_modalities_covered(pa_content: str) -> None:
    """PA.md must reference all 6 required electrotherapy modalities."""
    missing = [m for m in REQUIRED_MODALITIES if m not in pa_content]
    assert not missing, f"Missing modalities in PA.md: {missing}"


def test_modality_parameters_count(pa_content: str) -> None:
    """Each modality section should have 8-12 parameter rows."""
    sections = ["c1.", "c2.", "c3.", "c4.", "c5.", "c6."]
    for section in sections:
        assert section in pa_content, f"Section {section} not found in PA.md"


def test_client_screening_checklist(pa_content: str) -> None:
    """PA.md must include client screening with key contraindications."""
    required_items = ["pregnancy", "metal implant", "skin sensitivity", "contraindication"]
    for item in required_items:
        assert item in pa_content, f"Screening item '{item}' not in PA.md"
    assert "pass" in pa_content and "fail" in pa_content, "Pass/fail criteria missing"


def test_equipment_maintenance(pa_content: str) -> None:
    """PA.md must include monthly/quarterly maintenance and troubleshooting."""
    assert "monthly" in pa_content, "Monthly procedures missing"
    assert "quarterly" in pa_content, "Quarterly procedures missing"
    assert "troubleshoot" in pa_content, "Troubleshooting decision tree missing"


def test_kp_cross_references(pa_content: str) -> None:
    """PA.md must cross-reference KP information sheets."""
    for kp in ["kp-01", "kp-03", "kp-04", "kp-07", "kp-08"]:
        assert kp in pa_content, f"Cross-reference to {kp} missing in PA.md"
