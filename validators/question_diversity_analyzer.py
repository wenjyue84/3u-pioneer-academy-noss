"""KT Question Diversity Analyzer — classifies questions by type and generates metrics.

Usage:
    uv run python validators/question_diversity_analyzer.py --root . --output report.json
    uv run python validators/question_diversity_analyzer.py --root . --output report.html
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

TYPES = ("mcq", "short_answer", "scenario", "calculation", "matching", "true_false")
IDEAL = {"mcq": 0.30, "scenario": 0.30, "short_answer": 0.20, "calculation": 0.20}

_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("mcq", re.compile(r"multiple.?choice|aneka.?pilihan|pelbagai.?pilihan|选择题|\(a\).*\(b\).*\(c\)", re.I)),
    ("true_false", re.compile(r"true.?(?:or|/)\s*false|betul.?(?:atau|/)\s*salah|TRUE or FALSE|判断|改错", re.I)),
    ("matching", re.compile(r"match(?:ing)?|padanan|column\s*a.*column\s*b|配对|匹配", re.I)),
    ("scenario", re.compile(r"scenario|senario|case.?study|situasi|kes.?kajian|案例|处置|辨识", re.I)),
    ("calculation", re.compile(r"calculat|pengiraan|compute|formula|hitung|计算", re.I)),
    ("short_answer", re.compile(r"short.?answer|jawapan.?pendek|explain|describe|list|huraikan|senaraikan|nyatakan|terangkan|简答|填空", re.I)),
]


def classify_question_type(text: str) -> str:
    """Classify a question block into a type using keyword heuristics."""
    for qtype, pat in _PATTERNS:
        if pat.search(text):
            return qtype
    return "short_answer"  # default


def extract_questions(kt_path: Path) -> list[dict[str, str]]:
    """Parse a KT markdown file into individual question blocks."""
    content = kt_path.read_text(encoding="utf-8")
    _Q = r"Soalan|Question|Bahagian|第[一二三四五六七八九十]+部分"
    blocks = re.split(r"(?=^###?\s+(?:" + _Q + r"))", content, flags=re.M)
    questions: list[dict[str, str]] = []
    for block in blocks:
        block = block.strip()
        if not block or not re.match(r"^###?\s+(?:" + _Q + r")", block):
            continue
        qtype = classify_question_type(block)
        title_m = re.match(r"^###?\s+(.+)", block)
        title = title_m.group(1).strip() if title_m else "Untitled"
        questions.append({"title": title, "type": qtype, "file": kt_path.name})
    return questions


def scan_all_kt(root: Path) -> dict[str, dict[str, list[dict[str, str]]]]:
    """Scan all KT files grouped by subject and CU."""
    results: dict[str, dict[str, list[dict[str, str]]]] = {}
    for kt in sorted(root.rglob("KT-*.md")):
        parts = kt.relative_to(root).parts
        if len(parts) < 3:
            continue
        subject, cu = parts[0], parts[1]
        qs = extract_questions(kt)
        results.setdefault(subject, {}).setdefault(cu, []).extend(qs)
    return results


def _distribution(questions: list[dict[str, str]]) -> dict[str, int]:
    dist: dict[str, int] = {t: 0 for t in TYPES}
    for q in questions:
        dist[q["type"]] = dist.get(q["type"], 0) + 1
    return dist


def _flags(dist: dict[str, int]) -> list[str]:
    total = sum(dist.values()) or 1
    flags: list[str] = []
    if dist.get("scenario", 0) / total < 0.20:
        flags.append("too_few_scenario")
    if dist.get("mcq", 0) / total > 0.40:
        flags.append("too_many_mcq")
    return flags


def _recommendations(dist: dict[str, int]) -> list[str]:
    total = sum(dist.values()) or 1
    recs: list[str] = []
    for qtype, target in IDEAL.items():
        actual = dist.get(qtype, 0) / total
        diff = round((target - actual) * total)
        if diff > 0:
            recs.append(f"Add {diff} more {qtype} questions")
        elif diff < 0:
            recs.append(f"Convert {-diff} {qtype} questions to other types")
    return recs


def generate_report(data: dict[str, dict[str, list[dict[str, str]]]], output: Path) -> dict:
    """Build report dict and write JSON or HTML."""
    report: dict = {"subjects": {}, "total_questions": 0}
    for subj, cus in data.items():
        subj_entry: dict = {"CUs": {}, "total": 0}
        for cu, qs in cus.items():
            dist = _distribution(qs)
            cu_entry = {"distribution": dist, "flags": _flags(dist), "recommendations": _recommendations(dist), "count": len(qs)}
            subj_entry["CUs"][cu] = cu_entry
            subj_entry["total"] += len(qs)
        report["subjects"][subj] = subj_entry
        report["total_questions"] += subj_entry["total"]

    if output.suffix == ".html":
        _write_html(report, output)
    else:
        output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return report


def _write_html(report: dict, output: Path) -> None:
    rows: list[str] = []
    for subj, sd in report["subjects"].items():
        for cu, cd in sd["CUs"].items():
            d = cd["distribution"]
            fl = ", ".join(cd["flags"]) or "OK"
            rows.append(f"<tr><td>{subj}</td><td>{cu}</td><td>{cd['count']}</td>"
                        f"<td>{d.get('mcq',0)}</td><td>{d.get('scenario',0)}</td>"
                        f"<td>{d.get('short_answer',0)}</td><td>{d.get('calculation',0)}</td>"
                        f"<td>{d.get('matching',0)}</td><td>{d.get('true_false',0)}</td>"
                        f"<td>{fl}</td></tr>")
    body = "\n".join(rows)
    html = (f"<html><head><title>KT Question Diversity</title></head><body>"
            f"<h1>Question Diversity Report</h1><p>Total: {report['total_questions']}</p>"
            f"<table border=1><tr><th>Subject</th><th>CU</th><th>Total</th>"
            f"<th>MCQ</th><th>Scenario</th><th>Short</th><th>Calc</th>"
            f"<th>Match</th><th>T/F</th><th>Flags</th></tr>{body}</table></body></html>")
    output.write_text(html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="KT Question Diversity Analyzer")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("question_diversity_report.json"))
    args = parser.parse_args()
    data = scan_all_kt(args.root)
    report = generate_report(data, args.output)
    print(f"Analyzed {report['total_questions']} questions → {args.output}")
    flagged = sum(1 for s in report["subjects"].values() for c in s["CUs"].values() if c["flags"])
    if flagged:
        print(f"  {flagged} CU(s) flagged for rebalancing")
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
