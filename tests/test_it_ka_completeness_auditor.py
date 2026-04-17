"""Tests for IT-020 KA Completeness Auditor (US-034)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "audit_it_ka_completeness.py"


def _run(
    *extra: str,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(ROOT), *extra],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def test_script_runs_without_crash() -> None:
    r = _run()
    assert r.returncode in (0, 1), f"Crash:\n{r.stderr}"
    assert "KA COMPLETENESS AUDIT" in r.stdout


def test_matrix_shows_all_levels() -> None:
    r = _run()
    for level in ("L3:", "L4:", "L5:"):
        assert level in r.stdout, f"{level} missing"


def test_detects_existing_ka_files() -> None:
    r = _run()
    lines = [
        ln
        for ln in r.stdout.splitlines()
        if "C01" in ln and "Yes" in ln
    ]
    assert len(lines) >= 1, "L3-C01 KA should exist"


def test_reports_missing_ka() -> None:
    r = _run()
    assert "MISSING" in r.stdout or "INCOMPLETE" in r.stdout


def test_remediation_plan_present() -> None:
    r = _run()
    assert "REMEDIATION" in r.stdout


def test_json_output() -> None:
    r = _run("--json")
    data = json.loads(r.stdout)
    assert "L3" in data and "L4" in data and "L5" in data
    assert len(data["L3"]) == 7
    assert len(data["L4"]) == 6
    assert len(data["L5"]) == 7


def test_ka_validation_fields() -> None:
    r = _run("--json")
    data = json.loads(r.stdout)
    c01 = data["L3"][0]
    assert c01["cu"] == "C01"
    assert c01["exists"] is True
    assert isinstance(c01["questions"], int)
    assert "has_rubric" in c01
    assert "has_answers" in c01
