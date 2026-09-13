#!/usr/bin/env python3
"""Generate `git mv` rename plan for BEV / Aesthetic / IT WIM files.

Pattern (Option B): keep doc-code prefix, add descriptive English suffix.
  KP-01.md -> KP-01-<slug>.md
  KK-03.md -> KK-03-<slug>.md
  KA.md    -> KA-<slug>.md
  PM-teori.md -> PM-teori-<slug>.md  (CU-name based)

Title extraction (per-subject):
  BEV: body H2 `## Work Activity N: <name>`
  IT:  body H2 `## Tajuk / Title: <name>`
  Aesthetic: body bold line `**Work Activity N:** <name>`

Fallback for KA/PA/PM-teori/PM-amali:
  CU name from JPK envelope row "KOD DAN TAJUK UNIT KOMPETENSI",
  stripped of code prefix.

Outputs:
  _tools/rename_plan.csv
  _tools/rename_other_subjects.sh   (review then `bash` it)
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUBJECTS = {
    "bev": ROOT / "bev-diagnostic-rectification",
    "aesthetic": ROOT / "aesthetic-services",
    "it": ROOT / "it-computer-system",
}
SKIP_DIRS = {"_assets", "_docs", "_reference", "_tools", "c03-manual-body-massage", "level-4"}

STOPWORDS = {"a", "an", "the", "of", "for", "and", "to", "in", "on", "with"}


def slugify(text: str, max_words: int = 6) -> str:
    text = re.sub(r"\([^)]*\)", " ", text)              # drop parenthetical
    text = re.sub(r"[\u4e00-\u9fff\u3000-\u303f]+", " ", text)  # drop CJK
    text = re.sub(r"[^A-Za-z0-9\s-]", " ", text)
    words = [w.lower() for w in text.split() if w]
    # keep up to max_words but always keep first word
    kept: list[str] = []
    for w in words:
        if len(kept) >= max_words:
            break
        if kept and w in STOPWORDS:
            continue
        kept.append(w)
    slug = "-".join(kept)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug or "untitled"


def read_envelope_cu_name(text: str) -> str | None:
    """Pull descriptive CU name from 'KOD DAN TAJUK UNIT KOMPETENSI' row."""
    m = re.search(
        r"KOD DAN TAJUK UNIT KOMPETENSI\s*\|\s*([^\n|]+)", text, re.IGNORECASE
    )
    if not m:
        return None
    raw = m.group(1).strip()
    # strip leading code like "G452-010-3:2023-C01" or "IT-020-3:2013-L3-C01"
    # (any whitespace-bounded token containing both letters and a digit)
    raw = re.sub(r"^(?=[\w:.-]*\d)[\w:.-]+\s+", "", raw, count=1)
    return raw or None


def extract_title(path: Path, doc: str, seq: int) -> str | None:
    text = path.read_text(encoding="utf-8", errors="replace")

    if doc in ("KP", "KT", "KK"):
        # BEV pattern: ## Work Activity N: <name>
        m = re.search(rf"^##\s*Work Activity\s*{seq}\s*[:\-]\s*(.+)$", text, re.M)
        if m:
            return m.group(1).strip()
        # IT pattern: ## Tajuk / Title: <name>
        m = re.search(r"^##\s*Tajuk\s*/?\s*Title\s*[:\-]\s*(.+)$", text, re.M)
        if m:
            return m.group(1).strip()
        # Aesthetic pattern: **Work Activity N:** <name>
        m = re.search(rf"\*\*Work Activity\s*{seq}\s*[:\-]\s*\*\*\s*(.+)$", text, re.M)
        if m:
            return m.group(1).strip()
        # Aesthetic fallback: first ## 2.0 <topic> heading
        m = re.search(r"^##\s*\d+\.\d+\s+([A-Z][^\n]+)$", text, re.M)
        if m:
            return m.group(1).strip()
        # KT-only fallback: title in `## Title (Tajuk):` style
        m = re.search(r"^##\s*(?:Title|Tajuk).*?[:\-]\s*(.+)$", text, re.M)
        if m:
            return m.group(1).strip()

    # KA / PA / PM-teori / PM-amali → CU name
    cu_name = read_envelope_cu_name(text)
    if cu_name:
        return cu_name

    # last resort: first H1
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        return m.group(1).strip()
    return None


DOC_RE = re.compile(r"^(KP|KT|KK)-(\d+)$|^(KA|PA|PM-teori|PM-amali)$")


def classify(stem: str) -> tuple[str, int] | None:
    m = DOC_RE.match(stem)
    if not m:
        return None
    if m.group(1):
        return (m.group(1), int(m.group(2)))
    return (m.group(3), 0)


def main() -> int:
    plan: list[tuple[str, str, str, str]] = []  # (subject, cu, old_rel, new_rel)
    warnings: list[str] = []

    for subject, root in SUBJECTS.items():
        if not root.exists():
            warnings.append(f"missing subject root: {root}")
            continue
        for cu_dir in sorted(root.iterdir()):
            if not cu_dir.is_dir() or cu_dir.name in SKIP_DIRS:
                continue
            files = sorted(cu_dir.glob("*.md"))
            if not files:
                continue
            # skip CU folders that are KA-only stubs (already minimal)
            if len(files) == 1 and files[0].name == "KA.md":
                warnings.append(f"skip KA-only stub: {cu_dir.relative_to(ROOT)}")
                continue

            for path in files:
                cls = classify(path.stem)
                if not cls:
                    continue
                doc, seq = cls
                # already renamed?
                if path.stem != ("KA" if doc == "KA" else
                                 "PA" if doc == "PA" else
                                 "PM-teori" if doc == "PM-teori" else
                                 "PM-amali" if doc == "PM-amali" else
                                 f"{doc}-{seq:02d}"):
                    continue
                title = extract_title(path, doc, seq)
                if not title:
                    warnings.append(f"NO TITLE: {path.relative_to(ROOT)}")
                    continue
                slug = slugify(title)
                if not slug:
                    warnings.append(f"EMPTY SLUG: {path.relative_to(ROOT)} <- {title!r}")
                    continue
                if doc in ("KP", "KT", "KK"):
                    new_name = f"{doc}-{seq:02d}-{slug}.md"
                else:
                    new_name = f"{doc}-{slug}.md"
                old_rel = path.relative_to(ROOT).as_posix()
                new_rel = (path.parent / new_name).relative_to(ROOT).as_posix()
                if old_rel == new_rel:
                    continue
                plan.append((subject, cu_dir.name, old_rel, new_rel))

    out_csv = ROOT / "_tools" / "rename_plan.csv"
    with out_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["subject", "cu", "old", "new"])
        writer.writerows(plan)

    sh = ROOT / "_tools" / "rename_other_subjects.sh"
    lines = ["#!/usr/bin/env bash",
             "# Auto-generated by _tools/generate_rename_script.py",
             "# Review carefully, then run:  bash _tools/rename_other_subjects.sh",
             "set -e",
             "cd \"$(dirname \"$0\")/..\"",
             "",
             "mv_one() {",
             "  if [ -e \"$1\" ]; then",
             "    git mv \"$1\" \"$2\"",
             "  else",
             "    echo \"skip (missing): $1\"",
             "  fi",
             "}",
             ""]
    cur_subject = None
    for subject, cu, old, new in plan:
        if subject != cur_subject:
            lines.append(f"# === {subject} ===")
            cur_subject = subject
        lines.append(f'mv_one "{old}" "{new}"')
    lines.append("")
    lines.append('echo "done."')
    sh.write_text("\n".join(lines), encoding="utf-8")

    print(f"plan: {len(plan)} renames")
    print(f"  csv : {out_csv.relative_to(ROOT)}")
    print(f"  sh  : {sh.relative_to(ROOT)}")
    if warnings:
        print(f"warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
