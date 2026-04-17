"""Tests for IT-020 Lab Activity Coverage Validator (US-036)."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "validate_it_lab_coverage.py"


def _run(*extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--root", str(ROOT), *extra],
        capture_output=True, text=True, encoding="utf-8",
    )


def test_script_runs_without_crash() -> None:
    r = _run()
    assert r.returncode == 0, f"Crash:\n{r.stderr}"
    assert "LAB ACTIVITY COVERAGE" in r.stdout


def test_reports_all_levels() -> None:
    r = _run()
    for level in ("L3:", "L4:", "L5:"):
        assert level in r.stdout, f"{level} missing"


def test_minimum_8_unmapped_kps() -> None:
    r = _run("--json")
    data = json.loads(r.stdout)
    total_unmapped = sum(
        len(data[lv]["unmapped"]) for lv in ("L3", "L4", "L5")
    )
    assert total_unmapped >= 8, f"Only {total_unmapped} unmapped"


def test_coverage_percentages_valid() -> None:
    r = _run("--json")
    data = json.loads(r.stdout)
    for lv in ("L3", "L4", "L5"):
        pct = data[lv]["pct"]
        assert 0 < pct < 100, f"{lv} coverage {pct}% out of range"


def test_suggestions_for_unmapped() -> None:
    r = _run()
    assert "Suggested lab activities" in r.stdout
    assert "TBD" not in r.stdout, "All unmapped should have suggestions"
