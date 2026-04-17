"""Learning Outcome to Assessment Linkage Matrix generator."""

import csv
import re
import sys
from pathlib import Path


def parse_noss_learning_outcomes(text: str) -> list[dict[str, str]]:
    """Parse NOSS extract markdown, return list of {cu, lo_code, text}."""
    results: list[dict[str, str]] = []
    cu, seq, in_rk = "", 0, False
    for line in text.splitlines():
        m = re.match(r"### \d+\.\d+ CoCU (C\d+):", line)
        if m:
            cu, seq, in_rk = m.group(1), 0, False
            continue
        if "**Related Knowledge:**" in line:
            in_rk = True
            continue
        if in_rk:
            rm = re.match(r"- (\d+\.\d+) (.+)", line)
            if rm and cu:
                seq += 1
                results.append({
                    "cu": cu,
                    "lo_code": f"LO-{cu}-{seq:02d}",
                    "text": rm.group(2).strip(),
                })
            elif line.strip() and not line.startswith("- "):
                in_rk = False
    return results


def extract_assessment_item_tags(
    base_dir: Path,
) -> dict[str, list[str]]:
    """Scan KA/KT files for <!-- LO-CXX-NN --> tags.

    Returns {lo_code: [item_ids]}.
    """
    mapping: dict[str, list[str]] = {}
    for f in sorted(base_dir.rglob("K[AT]*.md")):
        item_id = f.stem
        cu_dir = f.parent.name
        text = f.read_text(encoding="utf-8")
        for m in re.finditer(r"<!-- (LO-C\d+-\d+) -->", text):
            mapping.setdefault(m.group(1), []).append(f"{cu_dir}/{item_id}")
    return mapping


def compute_coverage_percentage(
    noss_path: Path,
    base_dir: Path,
    subject: str = "BEV",
) -> list[dict[str, str]]:
    """Build coverage matrix rows for CSV output."""
    text = noss_path.read_text(encoding="utf-8")
    los = parse_noss_learning_outcomes(text)
    tags = extract_assessment_item_tags(base_dir)
    rows = []
    for lo in los:
        covered = tags.get(lo["lo_code"], [])
        rows.append({
            "Subject": subject,
            "CU": lo["cu"],
            "LO_Code": lo["lo_code"],
            "LO_Text": lo["text"],
            "Covered_By": "; ".join(covered) or "NONE",
            "Coverage_Percent": "100" if covered else "0",
        })
    return rows


def write_csv(rows: list[dict[str, str]], out_path: Path) -> None:
    """Write coverage matrix CSV and print summary."""
    cols = ["Subject", "CU", "LO_Code", "LO_Text", "Covered_By", "Coverage_Percent"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    gaps = sum(1 for r in rows if r["Coverage_Percent"] == "0")
    print(f"Wrote {len(rows)} LOs to {out_path}. Gaps: {gaps}/{len(rows)}")


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    noss = root / "bev-diagnostic-rectification" / "00-noss-extract.md"
    base = root / "bev-diagnostic-rectification"
    out = root / "_reference" / "coverage_matrix.csv"
    rows = compute_coverage_percentage(noss, base)
    write_csv(rows, out)
