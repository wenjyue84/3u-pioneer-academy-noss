"""Tests for assessment-time-validator.py."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "atv", str(Path(__file__).resolve().parent.parent / "_tools" / "assessment-time-validator.py")
)
assert spec and spec.loader
atv = importlib.util.module_from_spec(spec)
sys.modules["atv"] = atv
spec.loader.exec_module(atv)


def test_mcq_time() -> None:
    qtype, mins = atv.estimate_question_time("**A1.** Which Act governs... A) X B) Y")
    assert qtype == "mcq" and mins == 2


def test_scenario_time() -> None:
    qtype, mins = atv.estimate_question_time("**Q5 (Scenario):** A client presents...")
    assert qtype == "scenario" and mins == 10


def test_fill_blank_time() -> None:
    qtype, mins = atv.estimate_question_time("The answer is ____________.")
    assert qtype == "fill" and mins == 2


def test_short_answer_default() -> None:
    qtype, mins = atv.estimate_question_time("Explain briefly the concept.")
    assert qtype == "short" and mins == 5


def test_practical_time() -> None:
    qtype, mins = atv.estimate_question_time("Task 1: Perform the procedure")
    assert qtype == "practical" and mins == 15


def test_calculate_duration_ka(tmp_path: Path) -> None:
    ka = tmp_path / "KA.md"
    ka.write_text("# KA\n**A1.** Q A) X\n**A2.** Q A) Y\n**Q3 (Scenario):** S\n", encoding="utf-8")
    result = atv.calculate_assessment_duration(ka)
    assert result["question_count"] == 3
    assert result["total_minutes"] == 14  # 2+2+10
    assert result["assessment_type"] == "KA"


def test_generate_report_csv(tmp_path: Path) -> None:
    out = tmp_path / "report.csv"
    rows = atv.generate_report(out_path=out)
    assert out.exists()
    assert len(rows) > 0
    assert all(k in rows[0] for k in ("file", "total_minutes", "pct_of_limit", "exceeds"))


def test_exceeds_flag() -> None:
    qs = "\n".join(f"**A{i}.** Q A) X" for i in range(1, 41))
    with tempfile.NamedTemporaryFile(mode="w", suffix="KA.md", delete=False, encoding="utf-8") as f:
        f.write(f"# KA\n{qs}\n")
        f.flush()
        result = atv.calculate_assessment_duration(Path(f.name))
    assert result["exceeds"] is True
    assert result["pct_of_limit"] > 110
