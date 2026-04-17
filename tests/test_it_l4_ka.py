"""Tests for IT-020 Level 4 KA — Network Diagnostic Scenarios (US-053)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).parents[1]
KA_PATH = ROOT / "it-computer-system" / "level-4" / "KA.md"

REQUIRED_TYPES = ("switching", "routing", "vpn", "firewall")
RFC_PATTERN = re.compile(r"\bRFC\s+\d{3,}", re.IGNORECASE)
SCENARIO_RE = re.compile(r'<!-- SCENARIO type="(\w+)" -->')
RUBRIC_RE = re.compile(r"<!-- RUBRIC-TOTAL: ([\d.]+) -->")


def _load() -> str:
    assert KA_PATH.exists(), f"KA.md not found: {KA_PATH}"
    return KA_PATH.read_text(encoding="utf-8")


def test_scenario_coverage() -> None:
    """Verify 15-20 scenarios covering all four network diagnostic types and RFC refs."""
    text = _load()
    types = SCENARIO_RE.findall(text)

    assert 15 <= len(types) <= 20, (
        f"Expected 15–20 scenarios, got {len(types)}"
    )
    for required in REQUIRED_TYPES:
        count = types.count(required)
        assert count >= 1, f"Missing scenario type: '{required}' (found: {types})"

    assert RFC_PATTERN.search(text), (
        "No RFC references found — networking terms must cite relevant RFCs"
    )


def test_rubric_totals() -> None:
    """Verify every scenario has a valid partial-credit rubric total."""
    text = _load()
    scenario_types = SCENARIO_RE.findall(text)
    rubric_totals = [float(m) for m in RUBRIC_RE.findall(text)]

    assert len(rubric_totals) == len(scenario_types), (
        f"Rubric total count ({len(rubric_totals)}) must equal "
        f"scenario count ({len(scenario_types)})"
    )
    for i, total in enumerate(rubric_totals):
        assert total > 0, f"Scenario {i + 1}: invalid rubric total {total}"
        assert total <= 10, f"Scenario {i + 1}: rubric total {total} exceeds 10 pts"

    total_marks = sum(rubric_totals)
    assert total_marks >= 30, f"Total assessment marks too low: {total_marks}"
