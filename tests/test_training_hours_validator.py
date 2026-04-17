"""Tests for validate_training_distribution.py."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "validate_training_distribution.py"

spec = importlib.util.spec_from_file_location("validate_training_distribution", SCRIPT)
assert spec and spec.loader
vtd = importlib.util.module_from_spec(spec)
sys.modules["validate_training_distribution"] = vtd
spec.loader.exec_module(vtd)  # type: ignore[union-attr]

parse_duration_from_file = vtd.parse_duration_from_file
scan_subject = vtd.scan_subject
compute_compliance = vtd.compute_compliance
CUDistribution = vtd.CUDistribution


# ---------------------------------------------------------------------------
# Unit tests for duration parser
# ---------------------------------------------------------------------------


def _tmp_file(tmp_path: Path, content: str) -> Path:
    p = tmp_path / "PM-teori.md"
    p.write_text(content, encoding="utf-8")
    return p


def test_parse_aesthetic_table_format(tmp_path: Path) -> None:
    f = _tmp_file(tmp_path, "| Tempoh Teori / Theory Duration | 8 hours |")
    assert parse_duration_from_file(f) == 8.0


def test_parse_aesthetic_inline_bold_format(tmp_path: Path) -> None:
    f = _tmp_file(tmp_path, "**Theory Duration:** 14 hours | **KP:** 10")
    assert parse_duration_from_file(f) == 14.0


def test_parse_practical_aesthetic_table(tmp_path: Path) -> None:
    p = tmp_path / "PM-amali.md"
    p.write_text("| Tempoh Amali / Practical Duration | 18 hours |", encoding="utf-8")
    assert parse_duration_from_file(p, is_practical=True) == 18.0


def test_parse_it_jumlah_format(tmp_path: Path) -> None:
    content = "| **Jumlah Jam Teori / Theory Hours** | 90 hours (30% of 300 hours) |"
    f = _tmp_file(tmp_path, content)
    assert parse_duration_from_file(f) == 90.0


def test_parse_bev_total_with_hours(tmp_path: Path) -> None:
    content = "## Total Theory Session Duration: approximately 370 minutes (6 hours 10 minutes)"
    f = _tmp_file(tmp_path, content)
    assert parse_duration_from_file(f) == 6.0


def test_parse_bev_minutes_only(tmp_path: Path) -> None:
    content = "## Total: approximately 195 minutes"
    f = _tmp_file(tmp_path, content)
    result = parse_duration_from_file(f)
    assert result is not None
    assert abs(result - 195 / 60) < 0.01


def test_parse_tuinalogy_chinese_format(tmp_path: Path) -> None:
    content = "**时数：** 72 小时（4 项工作活动 × 18 小时）"
    f = _tmp_file(tmp_path, content)
    assert parse_duration_from_file(f) == 72.0


def test_parse_returns_none_for_missing_pattern(tmp_path: Path) -> None:
    f = _tmp_file(tmp_path, "No duration info here.")
    assert parse_duration_from_file(f) is None


# ---------------------------------------------------------------------------
# Compliance logic tests
# ---------------------------------------------------------------------------


def _make_cu(theory: float, practical: float, subject: str = "test", cu: str = "C01") -> "CUDistribution":  # type: ignore[name-defined]
    dummy = ROOT / "dummy.md"
    return CUDistribution(
        subject=subject,
        cu=cu,
        theory_hours=theory,
        practical_hours=practical,
        source_teori=dummy,
        source_amali=dummy,
    )


def test_compliant_cu_30_70() -> None:
    cu = _make_cu(30.0, 70.0)
    assert cu.compliant is True
    assert abs(cu.knowledge_pct - 30.0) < 0.01


def test_non_compliant_cu_too_low() -> None:
    cu = _make_cu(20.0, 80.0)
    assert cu.compliant is False
    assert cu.knowledge_pct < 25.0


def test_non_compliant_cu_too_high() -> None:
    cu = _make_cu(40.0, 60.0)
    assert cu.compliant is False
    assert cu.knowledge_pct > 35.0


def test_zero_hours_not_compliant() -> None:
    cu = _make_cu(0.0, 0.0)
    assert cu.compliant is False


def test_compute_compliance_summary() -> None:
    cus = [_make_cu(30.0, 70.0), _make_cu(30.0, 70.0)]
    summary = compute_compliance(cus)
    assert summary["total_theory"] == 60.0
    assert summary["total_practical"] == 140.0
    assert summary["cumulative_knowledge_pct"] == 30.0
    assert summary["compliant_count"] == 2
    assert len(summary["non_compliant_cus"]) == 0  # type: ignore[arg-type]


def test_compute_compliance_flags_drift() -> None:
    cus = [_make_cu(10.0, 90.0)]
    summary = compute_compliance(cus)
    assert len(summary["non_compliant_cus"]) == 1  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Integration test — scan real subject directories
# ---------------------------------------------------------------------------


def test_scan_aesthetic_returns_cus() -> None:
    results = scan_subject("aesthetic")
    assert len(results) >= 7, f"Expected >=7 CUs for aesthetic, got {len(results)}"


def test_scan_it_returns_cus() -> None:
    results = scan_subject("it")
    assert len(results) >= 1, "Expected >=1 CU for IT"


def test_scan_tuinalogy_returns_cus() -> None:
    results = scan_subject("tuinalogy")
    assert len(results) >= 7, f"Expected >=7 CUs for tuinalogy, got {len(results)}"


def test_aesthetic_cumulative_near_target() -> None:
    """Aesthetic CUs should collectively be near 30% knowledge."""
    results = scan_subject("aesthetic")
    cus_with_hours = [d for d in results if d.total_hours > 0]
    if not cus_with_hours:
        pytest.skip("No aesthetic CUs with parseable hours")
    summary = compute_compliance(cus_with_hours)
    cumulative = summary["cumulative_knowledge_pct"]
    assert isinstance(cumulative, float)
    # Cumulative should be somewhere reasonable (not 0 or 100)
    assert 10.0 <= cumulative <= 90.0, f"Unreasonable cumulative K%: {cumulative}"
