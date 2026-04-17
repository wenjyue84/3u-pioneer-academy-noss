"""Assessment question time-box validator — estimates per-question time and flags overruns."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT / "_tools" / "assessment-time-reports"
TIME_LIMITS = {"KA": 60, "PA": 90}
QTYPE_MINUTES = {"mcq": 2, "fill": 2, "short": 5, "essay": 8, "scenario": 10, "practical": 15}

_QTYPE_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("mcq", re.compile(r"\*\*[A-Z]?\d+[\.\):].*(?:A[\.\)]|A\))", re.I)),
    ("fill", re.compile(r"_{4,}|填空", re.I)),
    ("scenario", re.compile(r"scenario|senario|案例|情境", re.I)),
    ("essay", re.compile(r"essay|esei|论述", re.I)),
    ("practical", re.compile(r"practical|task|任务|实操", re.I)),
    ("short", re.compile(r"short.?answer|jawapan pendek|简答|列[举出]|说明|nyatakan", re.I)),
]


def estimate_question_time(block: str) -> tuple[str, int]:
    """Return (question_type, minutes) for a question text block."""
    for qtype, pat in _QTYPE_PATTERNS:
        if pat.search(block):
            return qtype, QTYPE_MINUTES[qtype]
    return "short", QTYPE_MINUTES["short"]


def _split_questions(text: str) -> list[str]:
    """Split assessment text into per-question blocks."""
    parts = re.split(r"(?m)(?=^\s*\*{0,2}(?:Q|[A-Z])\d+[\s\.\):])", text)
    return [p for p in parts if re.match(r"\s*\*{0,2}(?:Q|[A-Z])\d+", p.strip())]


def calculate_assessment_duration(filepath: Path) -> dict[str, object]:
    """Parse a KA/PA file and return timing summary."""
    text = filepath.read_text(encoding="utf-8")
    questions = _split_questions(text)
    total = 0
    counts: dict[str, int] = {}
    for q in questions:
        qtype, mins = estimate_question_time(q)
        counts[qtype] = counts.get(qtype, 0) + 1
        total += mins
    atype = "PA" if "/PA" in filepath.as_posix() or "PA.md" in filepath.name else "KA"
    limit = TIME_LIMITS[atype]
    pct = round(total / limit * 100, 1) if limit else 0
    rel = str(filepath.relative_to(PROJECT)) if filepath.is_relative_to(PROJECT) else filepath.name
    return {
        "file": rel,
        "assessment_type": atype,
        "question_count": len(questions),
        "type_counts": counts,
        "total_minutes": total,
        "limit_minutes": limit,
        "pct_of_limit": pct,
        "exceeds": pct > 110,
    }


def generate_report(out_path: Path | None = None) -> list[dict[str, object]]:
    """Scan all KA/PA files and write CSV report. Returns row list."""
    files = sorted(PROJECT.rglob("KA.md")) + sorted(PROJECT.rglob("PA.md"))
    rows = [calculate_assessment_duration(f) for f in files]
    if out_path is None:
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = REPORTS_DIR / "time-allocation.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["file", "type", "questions", "total_min", "limit_min", "pct", "exceeds"])
        for r in rows:
            w.writerow([
                r["file"], r["assessment_type"], r["question_count"],
                r["total_minutes"], r["limit_minutes"], r["pct_of_limit"], r["exceeds"],
            ])
    flags = [r for r in rows if r["exceeds"]]
    if flags:
        print(f"\n⚠ {len(flags)} assessment(s) exceed 110% of recommended duration:")
        for f in flags:
            print(f"  {f['file']}: {f['total_minutes']}min / {f['limit_minutes']}min ({f['pct_of_limit']}%)")
            print(f"    → Suggest removing {(f['total_minutes'] - f['limit_minutes'])}min of questions or splitting")
    return rows


if __name__ == "__main__":
    rows = generate_report()
    print(f"\nProcessed {len(rows)} assessments → {REPORTS_DIR / 'time-allocation.csv'}")
