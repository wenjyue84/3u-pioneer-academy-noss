#!/usr/bin/env python3
"""question_type_analyzer.py — Cross-subject question type distribution analyzer with rebalancing recommendations."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SUBJECTS = {
    "BEV": ROOT / "bev-diagnostic-rectification",
    "Aesthetic": ROOT / "aesthetic-services",
    "IT": ROOT / "it-computer-system",
}

QTYPES = ["MCQ", "short_answer", "scenario", "practical", "essay", "matching", "fill_in"]

MCQ_PAT = re.compile(
    r"(\*\*[A-Z]\d+\.\*\*.*?\n(?:\s*[-]\s*[A-D]\..*\n){2,})"  # BEV style
    r"|(\*\*Q\d+\s*\(MCQ\))", re.MULTILINE
)
SHORT_PAT = re.compile(
    r"\(Short Answer|Jawapan Pendek\)|BAHAGIAN B|SECTION B.*short|pendek", re.IGNORECASE
)
SCENARIO_PAT = re.compile(
    r"\(Scenario|Senario\)|scenario-based|situasi|A client .{5,80}(request|present|arrive)|"
    r"A technician .{5,80}(notice|find|observ)", re.IGNORECASE
)
PRACTICAL_PAT = re.compile(
    r"##\s*(TASK|SENARIO|Work Activity|Aktiviti Kerja)|Performance Assessment|PENILAIAN PRESTASI",
    re.IGNORECASE,
)
ESSAY_PAT = re.compile(
    r"\(Essay|Esei\)|BAHAGIAN C|SECTION C.*essay|huraikan|bincangkan|terangkan secara|explain in detail",
    re.IGNORECASE,
)
MATCHING_PAT = re.compile(r"(match|padankan|column A.*column B)", re.IGNORECASE)
FILL_PAT = re.compile(r"(fill in|isi tempat|lengkapkan|_{3,}|\[.*?\])", re.IGNORECASE)

MCQ_Q_PAT = re.compile(
    r"^\s*\*\*[A-Z]?\d+[a-z]?\.\*\*|\*\*Q\d+\s*\(MCQ\)|^\s*\*\*\d+\.\*\*.*\n(?:\s*[-–]\s*\(?\w\)?\.)",
    re.MULTILINE,
)
SHORT_Q_PAT = re.compile(r"\*\*Q\d+\s*\(Short Answer|\*\*[B-C]\d+\.\*\*", re.MULTILINE)
SCENARIO_Q_PAT = re.compile(r"\*\*Q\d+\s*\(Scenario|\bscenario\b.*\?", re.MULTILINE | re.IGNORECASE)
ESSAY_Q_PAT = re.compile(r"\*\*[C]\d+\.\*\*|\*\*Q\d+\s*\(Essay|\(esei\)", re.MULTILINE | re.IGNORECASE)
MATCH_Q_PAT = re.compile(r"match.*column|column [AB]", re.IGNORECASE)
FILL_Q_PAT = re.compile(r"_{4,}|fill in the blank|\[___\]", re.IGNORECASE)


def count_type(text: str, is_pa: bool) -> dict[str, int]:
    counts: dict[str, int] = {t: 0 for t in QTYPES}
    if is_pa:
        counts["practical"] = max(1, len(PRACTICAL_PAT.findall(text)))
        return counts
    counts["MCQ"] = len(MCQ_Q_PAT.findall(text))
    counts["short_answer"] = len(SHORT_Q_PAT.findall(text))
    counts["scenario"] = len(SCENARIO_Q_PAT.findall(text))
    counts["essay"] = len(ESSAY_Q_PAT.findall(text))
    counts["matching"] = len(MATCH_Q_PAT.findall(text))
    counts["fill_in"] = len(FILL_Q_PAT.findall(text))
    if SHORT_PAT.search(text) and counts["short_answer"] == 0:
        counts["short_answer"] = 3
    if SCENARIO_PAT.search(text) and counts["scenario"] == 0:
        counts["scenario"] = 1
    if ESSAY_PAT.search(text) and counts["essay"] == 0:
        counts["essay"] = 2
    return counts


def parse_assessment(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    is_pa = path.stem == "PA"
    counts = count_type(text, is_pa)
    total = sum(counts.values()) or 1
    pct = {k: round(v / total * 100, 1) for k, v in counts.items()}
    types_present = sum(1 for v in counts.values() if v > 0)
    dominant = max(counts, key=lambda k: counts[k])
    dominant_pct = pct[dominant]
    flagged = types_present < 4 or dominant_pct > 60
    return {
        "file": str(path.relative_to(ROOT)),
        "counts": counts,
        "pct": pct,
        "total": total,
        "types_present": types_present,
        "dominant": dominant,
        "dominant_pct": dominant_pct,
        "flagged": flagged,
    }


def rebalance_rec(info: dict) -> str:
    recs = []
    dominant = info["dominant"]
    dpct = info["dominant_pct"]
    total = info["total"]
    if dpct > 60:
        replace_n = round((dpct - 40) / 100 * total)
        targets = [t for t in QTYPES if t != dominant and info["counts"].get(t, 0) == 0][:2]
        target_str = " and ".join(targets) if targets else "scenario/essay"
        recs.append(
            f"{dpct:.0f}% {dominant} ({total} questions): replace ~{replace_n} {dominant} with {target_str}"
        )
    if info["types_present"] < 4:
        missing = [t for t in QTYPES if info["counts"].get(t, 0) == 0][:3]
        recs.append(f"Only {info['types_present']} type(s) present — add {', '.join(missing)}")
    return "; ".join(recs) if recs else "Balanced"


def build_report(results_by_subject: dict[str, list[dict]]) -> str:
    lines = ["# Assessment Question Type Distribution Report\n"]
    all_flagged = []
    for subj, results in results_by_subject.items():
        lines.append(f"\n## {subj}\n")
        lines.append(f"| Assessment | Total | MCQ% | Short% | Scenario% | Practical% | Essay% | Match% | Fill% | Types | Flagged |")
        lines.append(f"|---|---|---|---|---|---|---|---|---|---|---|")
        for r in results:
            label = Path(r["file"]).parent.name + "/" + Path(r["file"]).stem
            p = r["pct"]
            flag = "⚠️" if r["flagged"] else "✅"
            lines.append(
                f"| {label} | {r['total']} | {p['MCQ']} | {p['short_answer']} | {p['scenario']} | "
                f"{p['practical']} | {p['essay']} | {p['matching']} | {p['fill_in']} | {r['types_present']} | {flag} |"
            )
            if r["flagged"]:
                all_flagged.append((subj, label, r))
        # Subject-level aggregates
        subj_counts: dict[str, int] = {t: 0 for t in QTYPES}
        for r in results:
            for t in QTYPES:
                subj_counts[t] += r["counts"].get(t, 0)
        total_q = sum(subj_counts.values()) or 1
        lines.append(f"\n**{subj} Totals:** {', '.join(f'{t}={subj_counts[t]} ({subj_counts[t]/total_q*100:.0f}%)' for t in QTYPES)}\n")

    lines.append("\n## Flagged Assessments (Low Diversity)\n")
    if not all_flagged:
        lines.append("No assessments flagged.\n")
    else:
        all_flagged.sort(key=lambda x: (x[2]["types_present"], -x[2]["dominant_pct"]))
        lines.append("| Severity | Assessment | Issue | Recommendation |")
        lines.append("|---|---|---|---|")
        for i, (subj, label, r) in enumerate(all_flagged, 1):
            issue = f"types={r['types_present']}, dominant={r['dominant']} {r['dominant_pct']:.0f}%"
            rec = rebalance_rec(r)
            lines.append(f"| {i} | {subj}/{label} | {issue} | {rec} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all-subjects", action="store_true")
    parser.add_argument("--format", default="md", choices=["md", "json"])
    args = parser.parse_args()

    results_by_subject: dict[str, list[dict]] = {}
    for subj, subj_dir in SUBJECTS.items():
        if not subj_dir.exists():
            continue
        files = (
            sorted(subj_dir.rglob("KA.md"))
            + sorted(subj_dir.rglob("KA-*.md"))
            + sorted(subj_dir.rglob("PA.md"))
            + sorted(subj_dir.rglob("PA-*.md"))
        )
        results_by_subject[subj] = [parse_assessment(f) for f in files]

    report = build_report(results_by_subject)
    out_path = ROOT / "_reference" / "assessment-question-type-distribution.md"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    print(report[:2000])
    print(f"\n[Wrote {out_path}]")


if __name__ == "__main__":
    main()
