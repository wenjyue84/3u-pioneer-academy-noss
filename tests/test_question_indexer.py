"""Tests for Assessment Question Bank Indexer (US-029)."""
from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Load via importlib (tool file has no hyphens, safe for direct import)
spec = importlib.util.spec_from_file_location(
    "question_bank_indexer",
    PROJECT_ROOT / "tools" / "question_bank_indexer.py",
)
assert spec and spec.loader
qbi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qbi)  # type: ignore[arg-type]


def test_index_and_search(tmp_path: Path) -> None:
    """Index all KA/KT files; verify 200+ questions; search latency < 100ms."""
    db = tmp_path / "questions.db"
    count = qbi.build_index(PROJECT_ROOT, db)
    assert count >= 200, f"Expected >=200 questions indexed, got {count}"

    import sqlite3
    conn = sqlite3.connect(db)

    # verify schema columns
    cols = {row[1] for row in conn.execute("PRAGMA table_info(questions)").fetchall()}
    required = {"question_id", "subject", "cu", "level", "qtype", "cognitive_level",
                "keywords", "noss_code", "answer_key"}
    assert required <= cols, f"Missing columns: {required - cols}"

    # verify all 3 subjects indexed
    subjects = {r[0] for r in conn.execute("SELECT DISTINCT subject FROM questions").fetchall()}
    assert {"BEV", "Aesthetic", "IT"} <= subjects, f"Missing subjects: subjects={subjects}"

    # sub-100ms search latency
    t0 = time.time()
    rows = conn.execute(
        "SELECT * FROM questions WHERE subject=? AND cu=?", ("BEV", "C01")
    ).fetchall()
    elapsed_ms = (time.time() - t0) * 1000
    assert elapsed_ms < 100, f"Search took {elapsed_ms:.1f}ms, expected <100ms"
    assert len(rows) >= 1, "Expected at least 1 BEV C01 question"

    conn.close()


def test_extract_questions_ka() -> None:
    """KA.md files yield at least 3 questions per file."""
    ka = PROJECT_ROOT / "aesthetic-services" / "C01" / "KA.md"
    if not ka.exists():
        return
    qs = qbi.extract_questions_from_file(ka)
    assert len(qs) >= 3, f"Expected >=3 from KA.md, got {len(qs)}"
    assert all(q["subject"] == "Aesthetic" for q in qs)
    assert all(q["doc_type"] == "KA" for q in qs)


def test_extract_questions_kt() -> None:
    """KT-*.md files yield questions with correct metadata."""
    kt = PROJECT_ROOT / "bev-diagnostic-rectification" / "C01" / "KT-01.md"
    if not kt.exists():
        return
    qs = qbi.extract_questions_from_file(kt)
    assert len(qs) >= 3, f"Expected >=3 from KT-01.md, got {len(qs)}"
    assert all(q["subject"] == "BEV" for q in qs)
    assert all(q["noss_code"] == "G452-010-3:2023" for q in qs)
    assert all(q["cognitive_level"] in
               {"remember", "understand", "apply", "analyze", "evaluate"} for q in qs)


def test_cognitive_level_inference() -> None:
    """Cognitive level is correctly inferred from question text."""
    cases = [
        ("List FIVE types of hazards", "remember"),
        ("Explain the purpose of a toolbox talk", "understand"),
        ("Calculate the total voltage of three cells in series", "apply"),
        ("Analyse the fault codes from the diagnostic scan", "analyze"),
        ("Evaluate the risk of proceeding without PPE", "evaluate"),
    ]
    for text, expected in cases:
        result = qbi.classify_cognitive(text)
        assert result == expected, f"'{text[:30]}' → {result}, expected {expected}"


def test_qtype_classification() -> None:
    """Question type classifier identifies MCQ, T/F, matching, scenario."""
    assert qbi.classify_qtype("Multiple Choice (Soalan Aneka Pilihan)") == "mcq"
    assert qbi.classify_qtype("True or False (Betul atau Salah)") == "true_false"
    assert qbi.classify_qtype("Matching (Padanan)") == "matching"
    assert qbi.classify_qtype("Scenario-Based Question") == "scenario"
    assert qbi.classify_qtype("Short Answer") == "short_answer"


def test_fts_search(tmp_path: Path) -> None:
    """Full-text search returns relevant results with highlighting."""
    db = tmp_path / "fts_test.db"
    qbi.build_index(PROJECT_ROOT, db)

    import sqlite3
    conn = sqlite3.connect(db)
    rows = conn.execute(
        "SELECT q.question_id, snippet(questions_fts,0,'>>','<<','...',8) "
        "FROM questions_fts JOIN questions q ON questions_fts.rowid=q.question_id "
        "WHERE questions_fts MATCH ?",
        ("battery",),
    ).fetchall()
    conn.close()

    assert len(rows) >= 1, "FTS search for 'battery' returned no results"
    # at least one result should contain the highlight markers
    snippets = [r[1] for r in rows]
    assert any(">>" in s for s in snippets), "No highlight markers in FTS snippets"
