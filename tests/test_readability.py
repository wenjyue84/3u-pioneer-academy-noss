"""Tests for _tools/readability-analyzer.py (US-040)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "ra", str(Path(__file__).resolve().parent.parent / "_tools" / "readability-analyzer.py")
)
assert spec and spec.loader
ra = importlib.util.module_from_spec(spec)
sys.modules["ra"] = ra
spec.loader.exec_module(ra)  # type: ignore[union-attr]

# Simple high-FLESCH English text (short words, short sentences)
EASY_TEXT = (
    "The cat sat on the mat. The dog ran fast. It was a good day. "
    "Sun is bright. Kids play well. She can run and jump far. "
    "He read the book. We like to learn new things each day. "
) * 8

# Complex low-FLESCH text (long multi-syllable words, long sentences)
HARD_TEXT = (
    "The electrocardiographic manifestations of ventricular hypertrophy demonstrate "
    "characteristic morphological alterations in the precordial and limb lead configurations, "
    "necessitating comprehensive electrophysiological interpretation methodologies "
    "for accurate cardiovascular pathophysiological assessment."
) * 6


def test_analyze_returns_required_keys(tmp_path: Path) -> None:
    f = tmp_path / "KP-01.md"
    f.write_text(EASY_TEXT, encoding="utf-8")
    result = ra.analyze_file_readability(f)
    for key in ("file", "level", "target", "flesch", "fog", "grade", "passes", "problem_paras"):
        assert key in result, f"Missing key: {key}"


def test_default_level_3_target(tmp_path: Path) -> None:
    f = tmp_path / "KP-01.md"
    f.write_text(EASY_TEXT, encoding="utf-8")
    result = ra.analyze_file_readability(f)
    assert result["level"] == 3
    assert result["target"] == 60.0


def test_level_4_detection(tmp_path: Path) -> None:
    level4 = tmp_path / "level-4"
    level4.mkdir()
    f = level4 / "KP-01.md"
    f.write_text(EASY_TEXT, encoding="utf-8")
    result = ra.analyze_file_readability(f)
    assert result["level"] == 4
    assert result["target"] == 65.0


def test_level_5_detection(tmp_path: Path) -> None:
    level5 = tmp_path / "level-5"
    level5.mkdir()
    f = level5 / "KK-03.md"
    f.write_text(EASY_TEXT, encoding="utf-8")
    result = ra.analyze_file_readability(f)
    assert result["level"] == 5
    assert result["target"] == 70.0


def test_easy_text_passes_l3(tmp_path: Path) -> None:
    f = tmp_path / "KP-easy.md"
    f.write_text(EASY_TEXT, encoding="utf-8")
    result = ra.analyze_file_readability(f)
    assert result["flesch"] is not None
    assert result["flesch"] >= 60.0
    assert result["passes"] is True


def test_hard_text_fails(tmp_path: Path) -> None:
    f = tmp_path / "KP-hard.md"
    f.write_text(HARD_TEXT, encoding="utf-8")
    result = ra.analyze_file_readability(f)
    assert result["flesch"] is not None
    assert result["passes"] is False


def test_cjk_text_skipped(tmp_path: Path) -> None:
    f = tmp_path / "KP-chinese.md"
    cjk_text = "推拿是一种传统的中医疗法。经络是气血运行的通道。阴阳平衡对健康至关重要。" * 10
    f.write_text(cjk_text, encoding="utf-8")
    result = ra.analyze_file_readability(f)
    assert result["passes"] is None
    assert result["flesch"] is None
    assert "CJK" in str(result["grade"])


def test_html_report_generated(tmp_path: Path) -> None:
    f = tmp_path / "KP-01.md"
    f.write_text(EASY_TEXT, encoding="utf-8")
    results = [ra.analyze_file_readability(f)]
    out = tmp_path / "report.html"
    ra.generate_html_report(results, out)
    assert out.exists()
    content = out.read_text(encoding="utf-8")
    assert "WIM Readability Report" in content
    assert "FLESCH" in content
    assert "PASS" in content or "FAIL" in content or "SKIP" in content


def test_project_files_found() -> None:
    files = (
        sorted(ra.PROJECT.rglob("KP*.md"))
        + sorted(ra.PROJECT.rglob("KT*.md"))
        + sorted(ra.PROJECT.rglob("KK*.md"))
    )
    assert len(files) > 0, "No KP/KT/KK files found in project"
