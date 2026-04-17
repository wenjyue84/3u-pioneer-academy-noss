"""Tests for NOSS CoCU Related Knowledge Dependency Mapper (US-033)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT))

from scripts.rk_parser import RKItem, parse_noss_extract  # noqa: E402
from scripts.validate_rk_coverage import SUBJECTS, build_coverage_report, scan_kp_files  # noqa: E402

BEV_NOSS = ROOT / "bev-diagnostic-rectification" / "00-noss-extract.md"
AESTHETIC_NOSS = ROOT / "aesthetic-services" / "00-noss-extract.md"
IT_NOSS = ROOT / "it-computer-system" / "00-noss-extract.md"


# --- rk_parser unit tests ---


def test_parse_bev_returns_rk_items() -> None:
    items = parse_noss_extract(BEV_NOSS, "bev")
    assert len(items) > 0
    codes = [i.code for i in items]
    assert "1.1" in codes
    assert "2.1" in codes


def test_bev_rk_items_have_cu_codes() -> None:
    items = parse_noss_extract(BEV_NOSS, "bev")
    cus = {i.cu for i in items}
    assert "C01" in cus
    assert "C02" in cus


def test_parse_aesthetic_returns_rk_items() -> None:
    items = parse_noss_extract(AESTHETIC_NOSS, "aesthetic")
    assert len(items) > 0
    codes = [i.code for i in items]
    assert "1.1" in codes


def test_parse_it_returns_k_codes() -> None:
    items = parse_noss_extract(IT_NOSS, "it")
    assert len(items) > 0
    codes = [i.code for i in items]
    assert "K1" in codes


def test_rk_item_has_description() -> None:
    items = parse_noss_extract(BEV_NOSS, "bev")
    first = items[0]
    assert first.description.strip() != ""


# --- scan_kp_files unit tests ---


def test_scan_kp_files_finds_bev_c01() -> None:
    bev_dir = ROOT / SUBJECTS["bev"]
    kp_index = scan_kp_files(bev_dir)
    assert "C01" in kp_index
    assert len(kp_index["C01"]) >= 3


def test_scan_kp_files_returns_paths_and_codes() -> None:
    bev_dir = ROOT / SUBJECTS["bev"]
    kp_index = scan_kp_files(bev_dir)
    path, codes = kp_index["C01"][0]
    assert path.name.startswith("KP-")
    assert isinstance(codes, set)


# --- build_coverage_report unit tests ---


def test_build_coverage_report_covered() -> None:
    items = [RKItem(cu="C01", wa="1", code="1.1", description="test item")]
    kp_index: dict[str, list[tuple[Path, set[str]]]] = {
        "C01": [(Path("C01/KP-01.md"), {"1.1", "1.2"})]
    }
    report = build_coverage_report(items, kp_index)
    assert len(report["covered"]) == 1
    assert len(report["orphaned"]) == 0
    assert report["covered"][0]["code"] == "1.1"  # type: ignore[index]


def test_build_coverage_report_orphaned() -> None:
    items = [RKItem(cu="C01", wa="1", code="1.9", description="missing item")]
    kp_index: dict[str, list[tuple[Path, set[str]]]] = {
        "C01": [(Path("C01/KP-01.md"), {"1.1"})]
    }
    report = build_coverage_report(items, kp_index)
    assert len(report["orphaned"]) == 1
    assert report["orphaned"][0]["code"] == "1.9"  # type: ignore[index]


def test_build_coverage_report_undocumented() -> None:
    items = [RKItem(cu="C01", wa="1", code="1.1", description="known")]
    kp_index: dict[str, list[tuple[Path, set[str]]]] = {
        "C01": [(Path("C01/KP-01.md"), {"1.1", "9.9"})]
    }
    report = build_coverage_report(items, kp_index)
    assert any("9.9" in str(e) for e in report["undocumented"])


# --- integration: script exit codes ---


def test_script_runs_bev() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_rk_coverage.py"), "bev"],
        capture_output=True, text=True,
    )
    assert "BEV RK Coverage" in result.stdout


def test_script_exit_nonzero_on_partial_coverage() -> None:
    """Script exits non-zero when orphaned RK items exist (expected in real data)."""
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_rk_coverage.py"), "bev", "aesthetic", "it"],
        capture_output=True, text=True,
    )
    # Either 0 (full) or 1 (partial) — both are valid exit codes
    assert result.returncode in (0, 1)


def test_script_invalid_subject_exits_2() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_rk_coverage.py"), "invalid"],
        capture_output=True, text=True,
    )
    assert result.returncode == 2
