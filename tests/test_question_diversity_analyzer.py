"""Tests for KT Question Diversity Analyzer (US-027)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from validators.question_diversity_analyzer import (
    classify_question_type,
    extract_questions,
    generate_report,
    scan_all_kt,
)

PROJECT_ROOT = Path(__file__).parent.parent


def test_classify_question_types() -> None:
    """Classifier accurately identifies all 6 question types."""
    cases = [
        ("Multiple Choice (Soalan Aneka Pilihan)\nA. Option\nB. Option", "mcq"),
        ("Soalan Pelbagai Pilihan\n(a) one (b) two (c) three", "mcq"),
        ("True or False (Betul atau Salah)\nState whether...", "true_false"),
        ("Betul/Salah\na) Statement one", "true_false"),
        ("Matching (Padanan)\nMatch Column A with Column B", "matching"),
        ("Scenario-Based Question\nA technician encounters...", "scenario"),
        ("Case Study (Kes Kajian)\nGiven the following situation...", "scenario"),
        ("Calculation (Pengiraan)\nCompute the total voltage...", "calculation"),
        ("Short Answer (Jawapan Pendek)\nList FIVE types...", "short_answer"),
        ("Explain the purpose of a toolbox talk.", "short_answer"),
        ("Describe the procedure for...", "short_answer"),
        ("Huraikan langkah-langkah keselamatan", "short_answer"),
    ]
    correct = sum(1 for text, expected in cases if classify_question_type(text) == expected)
    accuracy = correct / len(cases)
    assert accuracy >= 0.95, f"Accuracy {accuracy:.0%} < 95% threshold"


def test_classify_defaults_to_short_answer() -> None:
    """Ambiguous text defaults to short_answer."""
    assert classify_question_type("Some random question text") == "short_answer"


def test_extract_questions_from_real_file() -> None:
    """Extract questions from a real BEV KT file."""
    kt = PROJECT_ROOT / "bev-diagnostic-rectification" / "C01" / "KT-01.md"
    if not kt.exists():
        return
    qs = extract_questions(kt)
    assert len(qs) >= 3, f"Expected >=3 questions, got {len(qs)}"
    types_found = {q["type"] for q in qs}
    assert len(types_found) >= 2, "Expected at least 2 different question types"


def test_scan_produces_results() -> None:
    """Scanning project root finds questions across subjects."""
    data = scan_all_kt(PROJECT_ROOT)
    assert len(data) >= 1, "Expected at least 1 subject"
    total = sum(len(qs) for cus in data.values() for qs in cus.values())
    assert total >= 100, f"Expected >=100 questions, got {total}"


def test_report_json(tmp_path: Path) -> None:
    """JSON report contains expected structure."""
    data = scan_all_kt(PROJECT_ROOT)
    out = tmp_path / "report.json"
    report = generate_report(data, out)
    assert out.exists()
    loaded = json.loads(out.read_text(encoding="utf-8"))
    assert "subjects" in loaded
    assert loaded["total_questions"] >= 100
    for subj in loaded["subjects"].values():
        for cu in subj["CUs"].values():
            assert "distribution" in cu
            assert "flags" in cu
            assert "recommendations" in cu


def test_report_html(tmp_path: Path) -> None:
    """HTML report is valid and contains table."""
    data = scan_all_kt(PROJECT_ROOT)
    out = tmp_path / "report.html"
    generate_report(data, out)
    html = out.read_text(encoding="utf-8")
    assert "<table" in html
    assert "Question Diversity Report" in html


def test_flags_too_many_mcq(tmp_path: Path) -> None:
    """CU with >40% MCQ is flagged."""
    data = {"test": {"C01": [
        {"title": "Q1", "type": "mcq", "file": "KT-01.md"},
        {"title": "Q2", "type": "mcq", "file": "KT-01.md"},
        {"title": "Q3", "type": "mcq", "file": "KT-01.md"},
        {"title": "Q4", "type": "short_answer", "file": "KT-01.md"},
    ]}}
    report = generate_report(data, tmp_path / "r.json")
    cu = report["subjects"]["test"]["CUs"]["C01"]
    assert "too_many_mcq" in cu["flags"]


def test_flags_too_few_scenario(tmp_path: Path) -> None:
    """CU with <20% scenario is flagged."""
    data = {"test": {"C01": [
        {"title": "Q1", "type": "mcq", "file": "KT-01.md"},
        {"title": "Q2", "type": "short_answer", "file": "KT-01.md"},
        {"title": "Q3", "type": "calculation", "file": "KT-01.md"},
        {"title": "Q4", "type": "matching", "file": "KT-01.md"},
        {"title": "Q5", "type": "true_false", "file": "KT-01.md"},
    ]}}
    report = generate_report(data, tmp_path / "r.json")
    cu = report["subjects"]["test"]["CUs"]["C01"]
    assert "too_few_scenario" in cu["flags"]
