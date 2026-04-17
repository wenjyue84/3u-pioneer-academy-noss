"""Tests for accuracy_auditor.py."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from accuracy_auditor import (
    audit_aesthetic_standards,
    audit_bev_standards,
    audit_it_standards,
    format_audit_report,
    load_standards,
)


def test_48v_high_voltage_requirement() -> None:
    # 400V should PASS IEC 61508 HV threshold (>=48V)
    findings_pass = audit_bev_standards("The BEV 400V high voltage battery system is present.")
    passes = [
        f for f in findings_pass
        if f["standard_reference"] == "IEC 61508" and f["compliance_status"] == "Pass"
    ]
    assert passes, "400V should pass IEC 61508 HV threshold (>=48V)"

    # 12V labeled as HV should FAIL (12 < 48)
    findings_fail = audit_bev_standards("The HV system operates at 12V.")
    fails = [
        f for f in findings_fail
        if f["standard_reference"] == "IEC 61508" and f["compliance_status"] == "Fail"
    ]
    assert fails, "12V labeled as HV should fail IEC 61508 threshold check"


def test_bev_ppe_en455_reference() -> None:
    text_with = "Always wear PPE including insulated gloves (EN 455 rated)."
    text_without = "Always wear protective gloves when handling HV battery packs."
    findings_with = audit_bev_standards(text_with)
    findings_without = audit_bev_standards(text_without)
    assert any(
        f["compliance_status"] == "Pass" and "EN 455" in f["standard_reference"]
        for f in findings_with
    ), "EN 455 reference present should give Pass"
    assert any(
        f["compliance_status"] == "Fail" and "EN 455" in f["standard_reference"]
        for f in findings_without
    ), "Missing EN 455 reference should give Fail"


def test_bev_connector_iec62196() -> None:
    text_with = "Use IEC 62196 Type 2 connector for AC charging."
    text_without = "Connect the charging port to the vehicle socket."
    findings_with = audit_bev_standards(text_with)
    findings_without = audit_bev_standards(text_without)
    assert any(
        f["compliance_status"] == "Pass" and "IEC 62196" in f["standard_reference"]
        for f in findings_with
    ), "IEC 62196 reference present should give Pass"
    assert any(
        f["compliance_status"] == "Fail" and "IEC 62196" in f["standard_reference"]
        for f in findings_without
    ), "Missing IEC 62196 reference should give Fail"


def test_aesthetic_ultrasound_frequency() -> None:
    text_safe = "Apply ultrasound therapy at 40kHz for cavitation treatment."
    text_unsafe = "Apply ultrasound at 15kHz frequency to the skin."
    findings_safe = audit_aesthetic_standards(text_safe)
    findings_unsafe = audit_aesthetic_standards(text_unsafe)
    assert any(
        f["compliance_status"] == "Pass" for f in findings_safe
    ), "40kHz should be within safe clinical range"
    assert any(
        f["compliance_status"] == "Fail" for f in findings_unsafe
    ), "15kHz should be flagged as below safe minimum (20kHz)"


def test_aesthetic_chemical_warning() -> None:
    text_with = "Apply acid solution — caution: chemical safety warning applies."
    text_without = "Apply the serum solution to the treatment area."
    findings_with = audit_aesthetic_standards(text_with)
    findings_without = audit_aesthetic_standards(text_without)
    assert any(f["compliance_status"] == "Pass" for f in findings_with)
    assert any(f["compliance_status"] == "Fail" for f in findings_without)


def test_it_cabling_iso11801() -> None:
    text_with = "Install Cat6 cable per ISO/IEC 11801 structured cabling standard."
    text_without = "Install Cat6 cable throughout the building."
    findings_with = audit_it_standards(text_with)
    findings_without = audit_it_standards(text_without)
    assert any(f["compliance_status"] == "Pass" for f in findings_with)
    assert any(f["compliance_status"] == "Fail" for f in findings_without)


def test_format_audit_report_headers() -> None:
    findings = audit_bev_standards("The BEV 400V system uses IEC 62196 connectors.")
    report = format_audit_report(findings)
    assert "KP Section" in report
    assert "Standard" in report
    assert "Status" in report


def test_format_audit_report_empty() -> None:
    report = format_audit_report([])
    assert report == "No findings.\n"


def test_load_standards() -> None:
    standards = load_standards()
    assert len(standards) > 0
    names = [s["standard_name"] for s in standards]
    assert "IEC 61508" in names
    assert "EN 455" in names
    assert "IEC 62196" in names
