"""Tests for NOSS CoCU Work Activity Coverage Validator (US-021)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).parent.parent
VALIDATOR = PROJECT_ROOT / ".spiral" / "validators" / "noss_coverage_check.py"


def _run_validator(subject: str, out: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            sys.executable,
            str(VALIDATOR),
            "--subject", subject,
            "--output", str(out),
            "--root", str(PROJECT_ROOT),
        ],
        capture_output=True,
        text=True,
    )


def test_script_runs_without_error(tmp_path: Path) -> None:
    """Validator runs for --subject bev without error and creates output file."""
    out = tmp_path / "coverage-report.json"
    result = _run_validator("bev", out)
    assert result.returncode == 0, f"Script failed:\n{result.stderr}"
    assert out.exists(), "Output file was not created"


def test_output_json_valid(tmp_path: Path) -> None:
    """Output JSON has all required fields and correct types."""
    out = tmp_path / "coverage-report.json"
    _run_validator("bev", out)
    with open(out, encoding="utf-8") as f:
        report = json.load(f)
    assert report["subject"] == "bev"
    assert "noss_code" in report
    assert "total_work_activities" in report
    assert isinstance(report["mapped"], list)
    assert isinstance(report["unmapped"], list)
    assert isinstance(report["coverage_by_cu"], dict)
    assert isinstance(report["subject_coverage_pct"], float)
    assert report["total_work_activities"] > 0
    # mapped items must have required fields
    for item in report["mapped"]:
        assert "wa_id" in item
        assert "kk_path" in item
        assert "confidence" in item
        assert isinstance(item["confidence"], float)


def test_unmapped_activities_reported(tmp_path: Path) -> None:
    """Unmapped activities include noss_line and noss_snippet for manual review."""
    out = tmp_path / "coverage-report.json"
    _run_validator("bev", out)
    with open(out, encoding="utf-8") as f:
        report = json.load(f)
    # Coverage by CU should list all CUs
    assert len(report["coverage_by_cu"]) > 0
    # All unmapped items must have noss_line and noss_snippet
    for item in report["unmapped"]:
        assert "noss_line" in item, f"Missing noss_line in unmapped: {item}"
        assert "noss_snippet" in item, f"Missing noss_snippet in unmapped: {item}"
    # Subject coverage must be a valid percentage
    assert 0.0 <= report["subject_coverage_pct"] <= 100.0
