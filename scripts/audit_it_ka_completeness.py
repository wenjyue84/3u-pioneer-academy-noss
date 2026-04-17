"""IT-020 Knowledge Assessment Completeness Auditor.

Scans it-computer-system/L{3,4,5}/ directories, validates KA files
exist per CU with minimum 12 questions, answer scheme, and rubric.

Usage:
    uv run python scripts/audit_it_ka_completeness.py [--root PATH] [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
IT_DIR = "it-computer-system"
LEVELS = {"L3": 7, "L4": 6, "L5": 7}
MIN_QUESTIONS = 12
RUBRIC_RE = re.compile(
    r"Rubric|marking scheme|answer scheme", re.IGNORECASE
)
# Matches "### Q1", "**1.**", "**2.**" etc.
QUESTION_RE = re.compile(
    r"^#{1,4}\s+Q\d+|^\*\*\d+\.\*\*", re.MULTILINE
)
ANSWER_RE = re.compile(
    r"\*?\*?Answer\*?\*?:|answer scheme|Model Answer",
    re.IGNORECASE,
)


def audit_ka(
    root: Path,
) -> dict[str, list[dict[str, object]]]:
    """Return {level: [{cu, path, exists, questions, ...}]}."""
    results: dict[str, list[dict[str, object]]] = {}
    it_root = root / IT_DIR
    for level, n_cus in LEVELS.items():
        cus: list[dict[str, object]] = []
        for i in range(1, n_cus + 1):
            cu = f"C{i:02d}"
            cu_dir = it_root / f"{level}-{cu}"
            ka = cu_dir / "KA.md"
            entry: dict[str, object] = {
                "cu": cu,
                "path": str(ka.relative_to(root)),
                "exists": False,
                "questions": 0,
                "has_rubric": False,
                "has_answers": False,
            }
            if ka.is_file():
                text = ka.read_text(encoding="utf-8")
                entry["exists"] = True
                qs = QUESTION_RE.findall(text)
                entry["questions"] = len(qs)
                entry["has_rubric"] = bool(
                    RUBRIC_RE.search(text)
                )
                entry["has_answers"] = bool(
                    ANSWER_RE.search(text)
                )
            cus.append(entry)
        results[level] = cus
    return results


def check_prd_hook(root: Path) -> list[str]:
    """Check prd.json for IT CUs without KA files."""
    prd = root / "prd.json"
    if not prd.is_file():
        return []
    alerts: list[str] = []
    data = json.loads(prd.read_text(encoding="utf-8"))
    for story in data.get("userStories", []):
        title = story.get("title", "")
        if "IT" not in title:
            continue
        m = re.search(
            r"L(\d)[- ]*C(\d+)", title, re.IGNORECASE
        )
        if m:
            ka_path = (
                root
                / IT_DIR
                / f"L{m.group(1)}-C{int(m.group(2)):02d}"
                / "KA.md"
            )
            if not ka_path.is_file():
                sid = story["id"]
                alerts.append(
                    f"Story '{sid}': KA missing at {ka_path}"
                )
    return alerts


def _is_complete(c: dict[str, object]) -> bool:
    return (
        bool(c["exists"])
        and int(str(c["questions"])) >= MIN_QUESTIONS
        and bool(c["has_rubric"])
        and bool(c["has_answers"])
    )


def print_matrix(
    results: dict[str, list[dict[str, object]]],
) -> None:
    """Print completeness matrix to stdout."""
    print("=" * 60)
    print("IT-020 KA COMPLETENESS AUDIT")
    print("=" * 60)
    hdr = (
        f"  {'CU':<6} {'Exists':<8} {'Qs':<5} "
        f"{'Rubric':<8} {'Answers':<8} {'Status'}"
    )
    sep = f"  {'-'*6} {'-'*8} {'-'*5} {'-'*8} {'-'*8} {'-'*10}"
    for level, cus in results.items():
        ok = sum(1 for c in cus if _is_complete(c))
        print(f"\n{level}: {ok}/{len(cus)} complete")
        print(hdr)
        print(sep)
        for c in cus:
            qs = int(str(c["questions"]))
            if _is_complete(c):
                status = "OK"
            elif not c["exists"]:
                status = "MISSING"
            else:
                status = "INCOMPLETE"
            yn = lambda v: "Yes" if v else "No"  # noqa: E731
            print(
                f"  {c['cu']:<6} {yn(c['exists']):<8} "
                f"{qs:<5} {yn(c['has_rubric']):<8} "
                f"{yn(c['has_answers']):<8} {status}"
            )
    # Remediation
    missing = [
        (lv, c)
        for lv, cus in results.items()
        for c in cus
        if not _is_complete(c)
    ]
    if missing:
        print(f"\nREMEDIATION PLAN ({len(missing)} items):")
        for lv, c in missing:
            if not c["exists"]:
                effort = "~2h (create from scratch)"
            else:
                effort = "~1h (add questions)"
            print(f"  {lv}-{c['cu']}: {c['path']} -- {effort}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Audit IT-020 KA completeness"
    )
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument(
        "--json",
        action="store_true",
        help="Output JSON instead of table",
    )
    args = ap.parse_args()
    results = audit_ka(args.root)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print_matrix(results)
        alerts = check_prd_hook(args.root)
        if alerts:
            print("\nINTEGRATION ALERTS:")
            for a in alerts:
                print(f"  ! {a}")
    all_ok = all(
        _is_complete(c)
        for cus in results.values()
        for c in cus
    )
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
