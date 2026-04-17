"""Tests for _tools/rubric-standardizer.py (US-041).

Run: uv run pytest tests/test_rubric_standards.py -v
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

spec = importlib.util.spec_from_file_location(
    "rs", str(ROOT / "_tools" / "rubric-standardizer.py")
)
assert spec and spec.loader
rs = importlib.util.module_from_spec(spec)
sys.modules["rs"] = rs
spec.loader.exec_module(rs)  # type: ignore[union-attr]


COMPLIANT_MD = """\
# PA — Test CU

| Competency Dimension | Level Descriptor | Score | Evidence |
|----------------------|------------------|-------|----------|
| Safety | Follows all PPE rules | 10 | Direct observation |
| Communication | Explains steps clearly | 5 | Verbal check |
| Technique | Correct procedure | 15 | Checklist |
"""

MISSING_EVIDENCE_MD = """\
# PA — Missing Column

| Criteria | Description | Marks |
|----------|-------------|-------|
| Safety | Follows rules | 10 |
| Technique | Correct | 15 |
"""

NO_TABLE_MD = "# PA — No rubric table here\n\nJust some text.\n"


def _with_root(tmp_path: Path):
    """Context manager to temporarily set rs.ROOT to tmp_path."""
    import contextlib

    @contextlib.contextmanager
    def _ctx():
        old = rs.ROOT
        rs.ROOT = tmp_path
        try:
            yield
        finally:
            rs.ROOT = old

    return _ctx()


def test_validate_compliant_rubric(tmp_path: Path) -> None:
    f = tmp_path / "PA.md"
    f.write_text(COMPLIANT_MD, encoding="utf-8")
    with _with_root(tmp_path):
        result = rs.validate_rubric_format(f)
    assert result["compliant"] is True
    assert result["compliant_tables"] >= 1
    assert result["issues"] == []


def test_validate_missing_column(tmp_path: Path) -> None:
    f = tmp_path / "PA.md"
    f.write_text(MISSING_EVIDENCE_MD, encoding="utf-8")
    with _with_root(tmp_path):
        result = rs.validate_rubric_format(f)
    assert result["compliant"] is False
    assert any("missing columns" in i for i in result["issues"])


def test_validate_no_table(tmp_path: Path) -> None:
    f = tmp_path / "PA.md"
    f.write_text(NO_TABLE_MD, encoding="utf-8")
    with _with_root(tmp_path):
        result = rs.validate_rubric_format(f)
    assert result["compliant"] is False
    assert any("No markdown table" in i for i in result["issues"])


def test_reformat_adds_placeholder(tmp_path: Path) -> None:
    f = tmp_path / "PA.md"
    f.write_text(NO_TABLE_MD, encoding="utf-8")
    with _with_root(tmp_path):
        out = rs.reformat_rubric(f)
    assert "Competency Dimension" in out
    assert "Auto-generated placeholder" in out


def test_reformat_preserves_compliant(tmp_path: Path) -> None:
    f = tmp_path / "PA.md"
    f.write_text(COMPLIANT_MD, encoding="utf-8")
    with _with_root(tmp_path):
        out = rs.reformat_rubric(f)
    assert out == COMPLIANT_MD


def test_pa_rubric_format() -> None:
    """Audit all real PA files and report compliance %."""
    report = rs.generate_compliance_report(ROOT)
    assert report["total_files"] > 0, "No PA files found"
    assert isinstance(report["compliance_pct"], float)
    assert 0.0 <= report["compliance_pct"] <= 100.0
    # Report structure check
    for r in report["all_results"]:
        assert "file" in r
        assert "compliant" in r
        assert "issues" in r


def test_compliance_report_structure() -> None:
    report = rs.generate_compliance_report(ROOT)
    assert "total_files" in report
    assert "compliant_files" in report
    assert "compliance_pct" in report
    assert "non_compliant" in report
    nc = report["non_compliant"]
    for item in nc:
        assert "file" in item
        assert "issues" in item
