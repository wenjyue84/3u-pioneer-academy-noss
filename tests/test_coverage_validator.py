"""Tests for NOSS-to-WIM Competency-to-Assessment Coverage Validator (US-022)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
VALIDATOR = PROJECT_ROOT / "_tools" / "coverage_validator.py"


def _run(subject: str, out: Path | None = None) -> subprocess.CompletedProcess:
    cmd = [sys.executable, str(VALIDATOR), "--subject", subject, "--root", str(PROJECT_ROOT)]
    if out:
        cmd += ["--output", str(out)]
    return subprocess.run(cmd, capture_output=True, text=True)


def test_no_unmapped_activities(tmp_path: Path) -> None:
    """All BEV work activities and knowledge items map to existing WIM documents."""
    out = tmp_path / "gap-report.txt"
    result = _run("BEV", out)
    assert result.returncode == 0, (
        f"BEV coverage gaps found:\n{out.read_text(encoding='utf-8') if out.exists() else result.stdout}"
    )
    report = out.read_text(encoding="utf-8")
    assert "Not Covered" not in report or "0 items" in report or "All documents covered" in report


def test_all_subjects_run_without_error(tmp_path: Path) -> None:
    """Validator runs for --subject all and creates report file."""
    out = tmp_path / "all-subjects.txt"
    result = _run("all", out)
    assert out.exists(), "Output file not created"
    report = out.read_text(encoding="utf-8")
    assert "BEV" in report
    assert "Aesthetic" in report
    assert "IT" in report
    # Exit code 0 means zero gaps; 1 means gaps exist — both are valid runs (not crashes)
    assert result.returncode in (0, 1), f"Unexpected exit code: {result.returncode}\n{result.stderr}"


def test_coverage_report_format(tmp_path: Path) -> None:
    """Report contains required sections: coverage percentage and status line."""
    out = tmp_path / "format-check.txt"
    _run("BEV", out)
    report = out.read_text(encoding="utf-8")
    assert "Coverage:" in report
    assert "Overall Status:" in report
    assert "G452-010-3:2023" in report
