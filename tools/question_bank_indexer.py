#!/usr/bin/env python3
"""Assessment Question Bank Indexer — builds SQLite FTS5 index of all KA/KT questions."""
from __future__ import annotations

import argparse
import re
import sqlite3
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DB_PATH = PROJECT_ROOT / "questions.db"

SUBJECT_MAP = {
    "bev-diagnostic-rectification": "BEV",
    "aesthetic-services": "Aesthetic",
    "it-computer-system": "IT",
    "tuinalogy-services": "Tuinalogy",
}

NOSS_MAP = {
    "BEV": "G452-010-3:2023",
    "Aesthetic": "S960-002-3:2020",
    "IT": "IT-020-3/4/5:2013",
    "Tuinalogy": "S960-003-3:2020",
}

COGNITIVE_PATTERNS = [
    ("evaluate", r"\b(evaluat\w*|justify|recommend\w*|assess\w*|critique|prioriti\w*)"),
    ("analyze", r"\b(analys\w*|analyz\w*|distinguish\w*|classif\w*|compar\w*|contrast\w*|differentiat\w*)"),
    ("apply", r"\b(calculat\w*|comput\w*|demonstrat\w*|implement\w*|perform\w*|appl[yi]\w*)"),
    ("understand", r"\b(explain\w*|describ\w*|summariz\w*|interpret\w*|paraphras\w*|predict\w*)"),
    ("remember", r"\b(list\b|identif\w*|name\b|state\b|defin\w*|recall\w*|recogni\w*|label\w*)"),
]

QTYPE_PATTERNS = [
    ("mcq", r"(?i)(multiple.choice|soalan.aneka.pilihan|soalan.pelbagai.pilihan|mcq)"),
    ("true_false", r"(?i)(true.or.false|betul.atau.salah|true\/false|betul\/salah)"),
    ("matching", r"(?i)(matching|padanan|match.column|match.each)"),
    ("scenario", r"(?i)(scenario|senario|case.study|kes.kajian)"),
    ("calculation", r"(?i)(calculat|pengiraan|compute|work.out)"),
]


def infer_subject(path: Path) -> str:
    for part in path.parts:
        if part in SUBJECT_MAP:
            return SUBJECT_MAP[part]
    return "Unknown"


def infer_noss_code(path: Path) -> str:
    subj = infer_subject(path)
    # extract level from IT paths like L3-C01
    if subj == "IT":
        m = re.search(r"L(\d+)", str(path))
        return f"IT-020-{m.group(1)}:2013" if m else NOSS_MAP["IT"]
    return NOSS_MAP.get(subj, "Unknown")


def infer_cu(path: Path) -> str:
    # parent dir of the file is the CU folder
    return path.parent.name.upper()


def infer_level(path: Path) -> str:
    m = re.search(r"[Ll](\d+)", path.parent.name)
    return f"L{m.group(1)}" if m else "L3"


def classify_cognitive(text: str) -> str:
    lower = text.lower()
    for level, pattern in COGNITIVE_PATTERNS:
        if re.search(pattern, lower):
            return level
    return "understand"


def classify_qtype(header: str) -> str:
    for qtype, pattern in QTYPE_PATTERNS:
        if re.search(pattern, header):
            return qtype
    return "short_answer"


def extract_keywords(text: str) -> str:
    words = re.findall(r"[A-Za-z]{4,}", text.lower())
    stop = {"each", "that", "with", "from", "this", "what", "which", "when", "where",
            "answer", "question", "soalan", "jawapan", "explain", "describe", "list"}
    kws = list(dict.fromkeys(w for w in words if w not in stop))[:8]
    return ",".join(kws)


def extract_questions_from_file(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    subject = infer_subject(path)
    cu = infer_cu(path)
    level = infer_level(path)
    noss_code = infer_noss_code(path)
    # Accept bare `KA.md` and descriptive `KA-foo.md`; everything else is treated as KT.
    doc_type = "KA" if path.stem == "KA" or path.stem.startswith("KA-") else "KT"

    # Split by question headers (### Soalan N, ### Question N, **QN**, A1., A2. etc.)
    question_blocks = re.split(
        r"\n(?=###\s+(?:Soalan|Question)\s+\d|\*\*[QqAa]\d+[.\s]|##\s+SECTION\s+[A-C])",
        text,
    )

    questions: list[dict] = []
    for i, block in enumerate(question_blocks[1:], start=1):  # skip file header
        lines = block.strip().splitlines()
        if not lines:
            continue
        header = lines[0]
        body = "\n".join(lines[1:10])  # first 10 lines of body

        # find answer_key
        ans_match = re.search(
            r"\*\*(?:Answer|Jawapan)[^*]*\*\*[:\s]*([^\n|]+)", block, re.IGNORECASE
        )
        answer_key = ans_match.group(1).strip()[:120] if ans_match else ""

        qtype = classify_qtype(header + " " + body[:80])
        cog = classify_cognitive(header + " " + body[:200])
        keywords = extract_keywords(header + " " + body[:200])

        questions.append({
            "subject": subject,
            "cu": cu,
            "level": level,
            "qtype": qtype,
            "cognitive_level": cog,
            "keywords": keywords,
            "noss_code": noss_code,
            "answer_key": answer_key,
            "question_text": (header + "\n" + body[:300]).strip(),
            "source_file": str(path.relative_to(PROJECT_ROOT)),
            "doc_type": doc_type,
        })
    return questions


def build_index(root: Path, db_path: Path) -> int:
    conn = sqlite3.connect(db_path)
    conn.execute("DROP TABLE IF EXISTS questions")
    conn.execute("""
        CREATE TABLE questions (
            question_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT, cu TEXT, level TEXT, qtype TEXT,
            cognitive_level TEXT, keywords TEXT, noss_code TEXT,
            answer_key TEXT, question_text TEXT,
            source_file TEXT, doc_type TEXT
        )
    """)
    conn.execute("DROP TABLE IF EXISTS questions_fts")
    conn.execute("""
        CREATE VIRTUAL TABLE questions_fts USING fts5(
            question_text, answer_key, keywords,
            content='questions', content_rowid='question_id'
        )
    """)
    # Accept bare (`KA.md`) and descriptive (`KA-foo.md`) names; KT already wildcarded.
    ka_files = list(root.rglob("KA.md")) + list(root.rglob("KA-*.md"))
    kt_files = list(root.rglob("KT-*.md"))
    total = 0
    for f in ka_files + kt_files:
        if "_archive" in str(f) or "_reference" in str(f) or "_agents" in str(f):
            continue
        qs = extract_questions_from_file(f)
        for q in qs:
            conn.execute(
                "INSERT INTO questions (subject,cu,level,qtype,cognitive_level,keywords,"
                "noss_code,answer_key,question_text,source_file,doc_type) VALUES "
                "(?,?,?,?,?,?,?,?,?,?,?)",
                (q["subject"], q["cu"], q["level"], q["qtype"], q["cognitive_level"],
                 q["keywords"], q["noss_code"], q["answer_key"], q["question_text"],
                 q["source_file"], q["doc_type"]),
            )
            total += 1
    conn.execute("INSERT INTO questions_fts(questions_fts) VALUES('rebuild')")
    conn.commit()
    conn.close()
    return total


def cmd_index(args: argparse.Namespace) -> None:
    db = Path(args.db)
    t0 = time.time()
    count = build_index(PROJECT_ROOT, db)
    elapsed = (time.time() - t0) * 1000
    print(f"Indexed {count} questions into {db} in {elapsed:.0f}ms")


def cmd_search(args: argparse.Namespace) -> None:
    db = Path(args.db)
    if not db.exists():
        print("Database not found — run 'index' first"); return

    clauses, params = [], []
    if args.subject:
        clauses.append("subject = ?"); params.append(args.subject)
    if args.cu:
        clauses.append("cu = ?"); params.append(args.cu.upper())
    if args.level:
        clauses.append("cognitive_level = ?"); params.append(args.level)
    if args.qtype:
        clauses.append("qtype = ?"); params.append(args.qtype)

    conn = sqlite3.connect(db)
    t0 = time.time()

    if args.query:
        fts_sql = (
            "SELECT q.question_id,q.subject,q.cu,q.cognitive_level,q.qtype,"
            "snippet(questions_fts,0,'>>','<<','...',8) as snippet "
            "FROM questions_fts JOIN questions q ON questions_fts.rowid=q.question_id "
            "WHERE questions_fts MATCH ?"
        )
        fts_params = [args.query]
        if clauses:
            fts_sql += " AND " + " AND ".join(clauses)
            fts_params.extend(params)
        rows = conn.execute(fts_sql, fts_params).fetchall()
    else:
        sql = "SELECT question_id,subject,cu,cognitive_level,qtype,question_text FROM questions"
        if clauses:
            sql += " WHERE " + " AND ".join(clauses)
        rows = conn.execute(sql, params).fetchall()

    elapsed_ms = (time.time() - t0) * 1000

    if not rows:
        print("No results found.")
        conn.close(); return

    dist: dict[str, int] = {}
    for r in rows:
        cog = r[3]
        dist[cog] = dist.get(cog, 0) + 1

    print(f"\nResults: {len(rows)} questions  (search: {elapsed_ms:.1f}ms)")
    print(f"Cognitive distribution: {dict(sorted(dist.items()))}\n")
    for r in rows[:20]:
        snippet = r[5][:100].replace("\n", " ")
        print(f"  [{r[0]:>4}] {r[1]:10} {r[2]:6} cog={r[3]:10} type={r[4]:12} | {snippet}")
    if len(rows) > 20:
        print(f"  ... and {len(rows)-20} more")
    conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Assessment Question Bank Indexer")
    parser.add_argument("--db", default=str(DB_PATH), help="SQLite database path")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("index", help="Build/rebuild the question index")

    sp = sub.add_parser("search", help="Search questions")
    sp.add_argument("--subject", help="Filter by subject (BEV/Aesthetic/IT)")
    sp.add_argument("--cu", help="Filter by competency unit (e.g. C01)")
    sp.add_argument("--level", help="Filter by cognitive level (remember/understand/apply/analyze/evaluate)")
    sp.add_argument("--qtype", help="Filter by question type (mcq/short_answer/scenario/...)")
    sp.add_argument("--query", help="Full-text search query")

    args = parser.parse_args()
    if args.cmd == "index":
        cmd_index(args)
    else:
        cmd_search(args)


if __name__ == "__main__":
    main()
