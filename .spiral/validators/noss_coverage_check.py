#!/usr/bin/env python3
"""NOSS CoCU Work Activity Coverage Validator.

Usage:
    uv run python .spiral/validators/noss_coverage_check.py --subject bev --output coverage-report.json
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SUBJECT_CONFIG: dict[str, dict] = {
    "bev": {
        "noss": "bev-diagnostic-rectification/00-noss-extract.md",
        "kk_glob": "bev-diagnostic-rectification/C*/KK-*.md",
        "noss_code": "G452-010-3:2023",
    },
    "aesthetic": {
        "noss": "aesthetic-services/00-noss-extract.md",
        "kk_glob": "aesthetic-services/C*/KK-*.md",
        "noss_code": "S960-002-3:2020",
    },
    "it": {
        "noss": "it-computer-system/00-noss-extract.md",
        "kk_glob": "it-computer-system/L3-C*/KK-*.md",
        "noss_code": "IT-020-3:2013",
    },
}

_BEV_WA_RE = re.compile(r"\|\s*(G452-010-3:\d{4}-C\d+-W\d+)\s*\|\s*(.+?)\s*\|")
_AES_CU_RE = re.compile(r"###\s*CU\d+:.+\(S960-002-3:2020-(C\d+)\)")
_AES_WA_RE = re.compile(r"\|\s*(\d+)\s*\|\s*([A-Z][^|]{3,}?)\s*\|")

_KK_PATTERNS = [
    re.compile(r"##\s*Work Activity \d+:\s*(.+)"),
    re.compile(r"\*\*Work Activity \d+:\*\*\s*(.+)"),
    re.compile(r"\*\*Aktiviti Kerja / Work Activity\*\*\s*\|\s*\d+\.\s*(.+?)\s*\|"),
    re.compile(r"\*\*WA \d+:\*\*\s*(.+?)\s*\|"),
    re.compile(r"\|\s*WA \d+:\s*(.+?)\s*\|"),
]

_STOPWORDS = {
    "a", "an", "the", "of", "and", "or", "to", "for", "in", "out",
    "carry", "perform", "conduct", "out", "up", "its",
}


def parse_bev_work_activities(noss_path: Path) -> list[dict]:
    activities = []
    with open(noss_path, encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        m = _BEV_WA_RE.match(line)
        if m:
            wa_id = m.group(1).strip()
            title = m.group(2).strip()
            cu_m = re.search(r"(C\d+)", wa_id)
            cu = cu_m.group(1) if cu_m else "C01"
            activities.append({"id": wa_id, "cu": cu, "title": title, "line": i, "snippet": line.strip()})
    return activities


def parse_aesthetic_work_activities(noss_path: Path) -> list[dict]:
    activities = []
    current_cu: str | None = None
    with open(noss_path, encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if re.match(r"^## ", line):
            current_cu = None
            continue
        cu_m = _AES_CU_RE.match(line)
        if cu_m:
            current_cu = cu_m.group(1)
            continue
        if current_cu and not re.search(r"\|\s*WA\s*\|", line, re.IGNORECASE):
            wa_m = _AES_WA_RE.match(line)
            if wa_m:
                wa_num = int(wa_m.group(1))
                title = wa_m.group(2).strip()
                wa_id = f"S960-002-3:2020-{current_cu}-W{wa_num:02d}"
                activities.append({"id": wa_id, "cu": current_cu, "title": title, "line": i, "snippet": line.strip()})
    return activities


def parse_work_activities(subject: str, noss_path: Path) -> list[dict]:
    if subject == "bev":
        return parse_bev_work_activities(noss_path)
    if subject == "aesthetic":
        return parse_aesthetic_work_activities(noss_path)
    return []  # IT NOSS extract has no explicit WA section; WAs derived from KK files


def extract_kk_work_activity(kk_path: Path) -> str:
    try:
        content = kk_path.read_text(encoding="utf-8")
    except OSError:
        return ""
    for pattern in _KK_PATTERNS:
        m = pattern.search(content)
        if m:
            return m.group(1).strip()
    return ""


def _tokenize(text: str) -> set[str]:
    return {w.lower() for w in re.findall(r"\w+", text) if w.lower() not in _STOPWORDS and len(w) > 2}


def keyword_overlap(wa_title: str, kk_title: str) -> float:
    wa_words = _tokenize(wa_title)
    kk_words = _tokenize(kk_title)
    union = wa_words | kk_words
    if not union:
        return 0.0
    return round(len(wa_words & kk_words) / len(union) * 100, 1)


def find_best_kk_match(wa: dict, kk_files: list[dict]) -> tuple[dict | None, float]:
    cu_kk = [kk for kk in kk_files if kk["cu"] == wa["cu"]]
    if not cu_kk:
        return None, 0.0
    best = max(cu_kk, key=lambda kk: keyword_overlap(wa["title"], kk["activity"]))
    score = keyword_overlap(wa["title"], best["activity"])
    return best, score


def build_coverage_report(subject: str, root: Path) -> dict:
    config = SUBJECT_CONFIG[subject]
    noss_path = root / config["noss"]
    kk_paths = sorted(root.glob(config["kk_glob"]))

    work_activities = parse_work_activities(subject, noss_path)

    kk_files: list[dict] = []
    for kk_path in kk_paths:
        cu_m = re.search(r"(C\d+)", kk_path.parent.name)
        cu = cu_m.group(1) if cu_m else "C01"
        kk_files.append({
            "path": str(kk_path.relative_to(root)).replace("\\", "/"),
            "cu": cu,
            "activity": extract_kk_work_activity(kk_path),
        })

    # For subjects with no NOSS WA list, derive from KK files
    if not work_activities:
        for idx, kk in enumerate(kk_files, 1):
            wa_id = f"{config['noss_code']}-{kk['cu']}-W{idx:02d}"
            work_activities.append({
                "id": wa_id, "cu": kk["cu"], "title": kk["activity"],
                "line": 0, "snippet": kk["activity"],
            })

    mapped: list[dict] = []
    unmapped: list[dict] = []
    cu_coverage: dict[str, dict] = {}

    for wa in work_activities:
        cu = wa["cu"]
        cu_coverage.setdefault(cu, {"total": 0, "mapped": 0})
        cu_coverage[cu]["total"] += 1
        best_kk, score = find_best_kk_match(wa, kk_files)
        if best_kk and score >= 25.0:
            cu_coverage[cu]["mapped"] += 1
            mapped.append({
                "wa_id": wa["id"],
                "wa_title": wa["title"],
                "kk_path": best_kk["path"],
                "confidence": score,
            })
        else:
            unmapped.append({
                "wa_id": wa["id"],
                "wa_title": wa["title"],
                "noss_line": wa["line"],
                "noss_snippet": wa["snippet"],
                "best_match_confidence": score,
            })

    total = len(work_activities)
    cu_pct = {
        cu: round(v["mapped"] / v["total"] * 100, 1) if v["total"] else 0.0
        for cu, v in cu_coverage.items()
    }
    subject_pct = round(len(mapped) / total * 100, 1) if total else 0.0

    return {
        "subject": subject,
        "noss_code": config["noss_code"],
        "total_work_activities": total,
        "mapped": mapped,
        "unmapped": unmapped,
        "coverage_by_cu": cu_pct,
        "subject_coverage_pct": subject_pct,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="NOSS CoCU Work Activity Coverage Validator")
    parser.add_argument("--subject", choices=list(SUBJECT_CONFIG), required=True)
    parser.add_argument("--output", required=True, help="Output JSON report path")
    parser.add_argument("--root", default=".", help="Project root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    report = build_coverage_report(args.subject, root)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    total = report["total_work_activities"]
    covered = len(report["mapped"])
    print(f"Coverage: {report['subject_coverage_pct']}% ({covered}/{total} WAs mapped)")
    print(f"Report saved to {args.output}")


if __name__ == "__main__":
    main()
