"""WIM Document Readability Analyzer — FLESCH reading ease + Gunning FOG scoring."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import textstat

PROJECT = Path(__file__).resolve().parent.parent
REPORTS_DIR = PROJECT / "_tools" / "readability-reports"

# FLESCH reading ease targets by NOSS level
LEVEL_TARGETS: dict[int, float] = {3: 60.0, 4: 65.0, 5: 70.0}


def _detect_level(filepath: Path) -> int:
    """Infer NOSS level from path segments (level-4, level-5 folders)."""
    for part in filepath.parts:
        if part == "level-5":
            return 5
        if part == "level-4":
            return 4
    return 3


def _is_cjk_heavy(text: str) -> bool:
    """Return True if >30% of characters are CJK (textstat unreliable for Chinese)."""
    total = len(text)
    if not total:
        return False
    cjk = sum(
        1 for c in text
        if "\u4e00" <= c <= "\u9fff" or "\u3040" <= c <= "\u30ff"
    )
    return cjk / total > 0.3


def _strip_markdown(text: str) -> str:
    """Remove markdown syntax for cleaner readability scoring."""
    text = re.sub(r"^#{1,6}\s.*", "", text, flags=re.MULTILINE)
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"\*{1,3}|_{1,3}|~~", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    return text.strip()


def analyze_file_readability(filepath: Path) -> dict[str, object]:
    """Score a single WIM document for readability. Returns result dict."""
    text = filepath.read_text(encoding="utf-8")
    clean = _strip_markdown(text)

    level = _detect_level(filepath)
    target = LEVEL_TARGETS[level]
    cjk = _is_cjk_heavy(clean)

    rel = str(filepath.relative_to(PROJECT)) if filepath.is_relative_to(PROJECT) else filepath.name

    if not clean or cjk:
        return {
            "file": rel,
            "level": level,
            "target": target,
            "flesch": None,
            "fog": None,
            "grade": "N/A (CJK)" if cjk else "N/A (empty)",
            "passes": None,
            "problem_paras": [],
        }

    flesch = round(textstat.flesch_reading_ease(clean), 1)
    fog = round(textstat.gunning_fog(clean), 1)
    grade = textstat.text_standard(clean, float_output=False)
    passes = flesch >= target

    paras = [p.strip() for p in re.split(r"\n{2,}", clean) if len(p.strip()) > 80]
    problem_paras = [
        p[:200] for p in paras if textstat.flesch_reading_ease(p) < target
    ]

    return {
        "file": rel,
        "level": level,
        "target": target,
        "flesch": flesch,
        "fog": fog,
        "grade": grade,
        "passes": passes,
        "problem_paras": problem_paras,
    }


def generate_html_report(results: list[dict[str, object]], out_path: Path) -> None:
    """Write HTML report of readability scores to out_path."""
    rows = ""
    for r in results:
        flesch = r["flesch"]
        passes = r["passes"]
        if passes is True:
            badge = '<span style="color:green;font-weight:bold">PASS</span>'
        elif passes is False:
            badge = '<span style="color:red;font-weight:bold">FAIL</span>'
        else:
            badge = '<span style="color:gray">SKIP</span>'
        score = str(flesch) if flesch is not None else "—"
        fog_str = str(r["fog"]) if r["fog"] is not None else "—"
        n_prob = len(r["problem_paras"])  # type: ignore[arg-type]
        prob_cell = f"{n_prob} para(s)" if n_prob else ""
        rows += (
            f"<tr><td>{r['file']}</td><td>L{r['level']}</td>"
            f"<td>{r['target']}</td><td>{score}</td><td>{fog_str}</td>"
            f"<td>{r['grade']}</td><td>{badge}</td><td>{prob_cell}</td></tr>\n"
        )

    passes_count = sum(1 for r in results if r["passes"] is True)
    fails_count = sum(1 for r in results if r["passes"] is False)
    skip_count = sum(1 for r in results if r["passes"] is None)

    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>WIM Readability Report</title>
<style>
  body{{font-family:sans-serif;font-size:13px;margin:20px}}
  h1{{color:#333}}
  table{{border-collapse:collapse;width:100%}}
  th,td{{border:1px solid #ccc;padding:5px 10px;text-align:left}}
  th{{background:#f0f0f0}}
  tr:nth-child(even){{background:#fafafa}}
  .summary{{margin-bottom:12px;color:#555}}
</style>
</head><body>
<h1>WIM Readability Report</h1>
<p class="summary">
  Targets: L3 FLESCH &gt; 60 &nbsp;|&nbsp; L4 FLESCH &gt; 65 &nbsp;|&nbsp; L5 FLESCH &gt; 70<br>
  Total: {len(results)} files &mdash; PASS: {passes_count} &nbsp;|&nbsp; FAIL: {fails_count} &nbsp;|&nbsp; SKIP (CJK/empty): {skip_count}
</p>
<table>
  <thead><tr>
    <th>File</th><th>Level</th><th>Target</th><th>FLESCH</th><th>Gunning FOG</th>
    <th>Grade Level</th><th>Status</th><th>Problem Paras</th>
  </tr></thead>
  <tbody>
{rows}  </tbody>
</table>
</body></html>"""
    out_path.write_text(html, encoding="utf-8")


if __name__ == "__main__":
    files = (
        sorted(PROJECT.rglob("KP*.md"))
        + sorted(PROJECT.rglob("KT*.md"))
        + sorted(PROJECT.rglob("KK*.md"))
    )
    if not files:
        print("No KP/KT/KK files found.")
        sys.exit(0)
    results = [analyze_file_readability(f) for f in files]
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out = REPORTS_DIR / "readability-report.html"
    generate_html_report(results, out)
    fails = [r for r in results if r["passes"] is False]
    print(f"Scanned {len(results)} files → {out}")
    if fails:
        print(f"\n⚠  {len(fails)} file(s) below readability target:")
        for r in fails:
            print(f"  {r['file']}: FLESCH={r['flesch']} (target {r['target']})")
            if r["problem_paras"]:
                print(f"    {len(r['problem_paras'])} problematic paragraph(s)")
