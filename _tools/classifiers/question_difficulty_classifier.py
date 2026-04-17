#!/usr/bin/env python3
"""question_difficulty_classifier.py — Bloom's Taxonomy cognitive level classifier for KA/PA assessments."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

BLOOM_VERBS: dict[int, list[str]] = {
    6: ["create", "design", "construct", "develop", "formulate", "compose",
        "produce", "propose", "plan", "generate", "devise", "draft"],
    5: ["evaluate", "assess", "judge", "critique", "justify", "defend",
        "recommend", "prioritize", "rate", "argue", "appraise", "validate"],
    4: ["analyze", "analyse", "differentiate", "examine", "investigate",
        "categorize", "deduce", "infer", "contrast", "distinguish",
        "diagnose", "troubleshoot", "interpret", "inspect"],
    3: ["apply", "demonstrate", "use", "solve", "calculate", "operate",
        "perform", "complete", "prepare", "execute", "implement", "show",
        "conduct", "carry out", "choose", "determine", "measure", "select"],
    2: ["explain", "describe", "summarize", "classify", "compare", "discuss",
        "outline", "paraphrase", "give examples", "express", "state the"],
    1: ["define", "identify", "list", "name", "state", "recall", "recognize",
        "label", "match", "what is", "which", "who is", "when is", "how many"],
}


def classify_verb(text: str) -> tuple[int, float]:
    """Return (bloom_level 1-6, confidence 0-1) based on action verb analysis."""
    low = text.lower()
    for level in [6, 5, 4, 3, 2, 1]:
        for verb in BLOOM_VERBS[level]:
            if re.search(r"\b" + re.escape(verb) + r"\b", low):
                return level, 0.9 if level >= 4 else 0.75
    return 1, 0.5  # default recall


def _add(questions: list[dict], q_text: str, qtype: str) -> None:
    lvl, conf = classify_verb(q_text[:100])
    questions.append({"type": qtype, "bloom": lvl, "confidence": conf})


def parse_questions(filepath: Path) -> list[dict]:
    """Extract questions from KA or PA markdown files using multi-pattern detection."""
    text = filepath.read_text(encoding="utf-8")
    questions: list[dict] = []
    is_pa = filepath.stem == "PA"

    if is_pa:
        # Task heading descriptions: ## TASK 1: X or ### Task 1 — X
        for m in re.finditer(
            r"##+ (?:TASK|Task|SENARIO|Scenario)\s+\d+[^:\n\—–-]*[:\—–-]\s*(.+)", text
        ):
            _add(questions, m.group(1).strip(), "practical")
        # Numbered subtask lines: "1. Complete HV isolation (5 marks)"
        for m in re.finditer(r"^\d+\.\s+([A-Z][^(|\n]{8,}?)(?:\s*\(\d+[^)]*\))?\s*$",
                             text, re.MULTILINE):
            _add(questions, m.group(1).strip(), "practical")
        # Bold rubric criteria: | **S1-A Communication Effectiveness** |
        for m in re.finditer(r"\|\s*\*\*[A-Z0-9\-]+\s+([^*|]{5,})\*\*", text):
            _add(questions, m.group(1).strip(), "rubric")
        # Plain table criteria rows: | Client profile reviewed | 3 |
        for m in re.finditer(r"^\|\s+([A-Z][^|]{8,}?)\s+\|\s+\d", text, re.MULTILINE):
            txt = m.group(1).strip()
            if txt not in ("Criteria", "Task", "Field", "Duration"):
                _add(questions, txt, "rubric")
    else:
        # KA bilingual Q-style: **Q1 (MCQ):** **EN:** What is...
        q_en = re.findall(r"\*\*Q\d+\s*\([^)]+\):\*\*\s*\*\*EN:\*\*\s*(.+?)(?=\n)", text)
        for q in q_en:
            _add(questions, q.strip(), "MCQ")

        # KA BEV-style sections: **A1.** MCQ / **B1.** Short-answer / **C1.** Scenario
        for m in re.finditer(
            r"\*\*([ABC])(\d+)\.\*\*\s+(.+?)(?=\n\*\*[ABC]\d+\.|\n---|\Z)", text, re.DOTALL
        ):
            prefix = m.group(1)
            q_text = m.group(3).strip().split("\n")[0]
            qtype = "MCQ" if prefix == "A" else ("short-answer" if prefix == "B" else "scenario")
            _add(questions, q_text, qtype)

        # KA plain numbered style: **1.** **2.** (IT format — fallback if nothing found)
        if not questions:
            for m in re.finditer(
                r"\*\*(\d+)\.\*\*\s+(.+?)(?=\n\*\*\d+\.|\n---|\Z)", text, re.DOTALL
            ):
                q_text = m.group(2).strip().split("\n")[0]
                _add(questions, q_text, "MCQ")

    return questions


def analyze_assessment(filepath: Path) -> dict | None:
    """Return per-assessment Bloom's distribution metrics, or None if no questions parsed."""
    rel = filepath.relative_to(ROOT)
    code = "/".join(rel.parts[:-1]) + "/" + filepath.stem  # e.g. bev.../C01/KA

    questions = parse_questions(filepath)
    if not questions:
        return None

    total = len(questions)
    counts = [0] * 6
    for q in questions:
        counts[q["bloom"] - 1] += 1

    dist_pct = [round(c / total * 100, 1) for c in counts]
    hot_pct = round(sum(counts[3:]) / total * 100, 1)
    max_pct = round(max(counts) / total * 100, 1)
    max_lvl = counts.index(max(counts)) + 1

    flags: list[str] = []
    if hot_pct < 20:
        flags.append(f"LOW_HOT:{hot_pct}%")
    if max_pct > 50:
        flags.append(f"DOMINANT_L{max_lvl}:{max_pct}%")

    return {
        "code": code,
        "type": filepath.stem,
        "n": total,
        "dist": dist_pct,   # [L1%, L2%, L3%, L4%, L5%, L6%]
        "hot_pct": hot_pct,
        "flags": flags,
    }


def generate_recommendations(results: list[dict]) -> list[str]:
    recs: list[str] = []
    for r in results:
        if not r["flags"]:
            continue
        low_pct = r["dist"][0] + r["dist"][1]
        replace_n = max(1, round(low_pct / 100 * r["n"] * 0.4))
        recs.append(
            f"{r['code']}: {low_pct:.0f}% Level 1-2 recall — "
            f"recommend replacing {replace_n} question(s) with analysis/diagnostic scenarios"
        )
    return recs


def main() -> None:
    parser = argparse.ArgumentParser(description="Bloom's Taxonomy difficulty classifier for WIM assessments")
    parser.add_argument("--all-subjects", action="store_true", help="Scan all subjects")
    parser.add_argument("--output", choices=["json", "text"], default="text")
    args = parser.parse_args()

    files = sorted(ROOT.rglob("KA.md")) + sorted(ROOT.rglob("PA.md"))
    results = [r for f in files if (r := analyze_assessment(f)) is not None]
    results.sort(key=lambda x: x["code"])

    recs = generate_recommendations(results)
    flagged = [r for r in results if r["flags"]]

    summary = {
        "total_assessments": len(results),
        "flagged_count": len(flagged),
        "mean_hot_pct": round(sum(r["hot_pct"] for r in results) / max(len(results), 1), 1),
        "flagged": [r["code"] for r in flagged],
    }

    # Write compact JSON: summary/legend pretty-printed, each assessment on one line
    out_path = ROOT / "_reference" / "assessment-difficulty-distribution.json"
    out_path.parent.mkdir(exist_ok=True)
    parts: list[str] = [
        "{\n",
        f'  "summary": {json.dumps(summary, ensure_ascii=False)},\n',
        '  "legend": {"dist":"L1%,L2%,L3%,L4%,L5%,L6%","hot_pct":"% at Bloom L4-L6"},\n',
        '  "recommendations": [\n',
    ]
    for i, rec in enumerate(recs):
        parts.append(f'    {json.dumps(rec, ensure_ascii=False)}{"," if i < len(recs)-1 else ""}\n')
    parts.append('  ],\n  "assessments": {\n')
    for i, r in enumerate(results):
        entry = {"type": r["type"], "n": r["n"], "dist": r["dist"],
                 "hot_pct": r["hot_pct"], "flags": r["flags"]}
        parts.append(
            f'    {json.dumps(r["code"])}: {json.dumps(entry)}'
            f'{"," if i < len(results)-1 else ""}\n'
        )
    parts.append("  }\n}\n")
    out_path.write_text("".join(parts), encoding="utf-8")

    if args.output == "json":
        print(json.dumps({"summary": summary, "recommendations": recs},
                         indent=2, ensure_ascii=False))
    else:
        print(f"Assessments: {len(results)} | Flagged: {len(flagged)} | "
              f"Mean HOT: {summary['mean_hot_pct']}%")
        for r in flagged:
            print(f"  FLAG {r['code']}: {', '.join(r['flags'])}")
        print(f"\nWritten: {out_path}")


if __name__ == "__main__":
    main()
