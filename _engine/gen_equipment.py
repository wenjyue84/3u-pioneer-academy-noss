"""Generate the one-page JPK equipment-verification form from its SOALAN.

The form is not authored — it is *derived*. Every row is an item the paper already
asks for in section D (`SENARAI BAHAN / DOKUMEN`) or section E
(`SENARAI PERALATAN`), and the header block restates facts the paper already
states. Writing it by hand invites the two failures that were actually found on
2026-08-25:

  * ten of these forms were still on a self-invented layout, because the cover
    migration that day covered `soalan` and `skema` only and nobody re-read the
    supporting documents — the 2026-08-21 audit had also left them `未審`; and
  * every set's checklist listed a different number of items from its own paper,
    so an officer walking the room with the form would verify equipment the
    candidate never uses, and miss equipment they do.

Deriving it makes both impossible: the form cannot disagree with the paper it was
built from.

Structure follows `_engine/FORMAT-jpk-ppa.md` §8, read off the form Jennifer owns
(`raw/jennifer-authoritative-fb018-3/jen-equipment-verification.pdf`).

    uv run python -m _engine.gen_equipment --all
    uv run python -m _engine.gen_equipment output/jennifer-ppa-soalan/n821-*-soalan.md
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPER_DIR = ROOT / "output" / "jennifer-ppa-soalan"

JPK_FORM_NO = "JPK/PPA-PPT/SP/1:2022"


def _section_rows(text: str, heading: str) -> list[tuple[str, str]]:
    """(description, ratio) for each numbered row of a lettered section's table."""
    m = re.search(rf"^[#*\s]*[A-Z]\.\s*{heading}", text, re.IGNORECASE | re.MULTILINE)
    if not m:
        return []
    body = text[m.end():]
    nxt = re.search(r"^[#*\s]*[A-Z]\.\s+[A-Z]", body, re.MULTILINE)
    if nxt:
        body = body[:nxt.start()]

    rows: list[tuple[str, str]] = []
    for line in body.splitlines():
        if not re.match(r"^\s*\|\s*\d+\s*\|", line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        # Layout is NO. | description | UKURAN (UNIT) | KUANTITI (Bahan:Calon).
        # The ratio is the last cell; the unit column is not carried onto the
        # verification form, which asks only "how many are there".
        rows.append((cells[1], cells[-1] if len(cells) >= 4 else "1:1"))
    return rows


def _field(text: str, pattern: str, default: str = "") -> str:
    m = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    return m.group(1).strip() if m else default


def build(soalan: Path) -> tuple[Path, str, int]:
    text = soalan.read_text(encoding="utf-8")

    kod = _field(text, r"\|\s*\*\*KOD KOMPETENSI\*\*\s*\|\s*([^|]+)\|") or \
          _field(text, r"^\*\*KOD KOMPETENSI:?\*\*[:\s]*(.+)$")
    ref = _field(text, r"\b([A-Z]{1,3}\d*-\d{3}-\d{1,2}(?::\d{4})?/\d{4}/[AB]/\d+)\b")
    set_id = (re.search(r"set-([ab])", soalan.stem).group(1).upper()
              if re.search(r"set-([ab])", soalan.stem) else "")
    tempoh = _field(text, r"^[#*\s]*[A-Z]\.\s*TEMPOH[^\n:]*:?\s*(.+)$", "3 HOURS")
    tempoh = tempoh.lstrip(": ").strip()
    keterampilan = _field(text, r"^[#*\s]*[A-Z]\.\s*KETERAMPILAN\s*\n+\s*:?\s*(.+)$")
    kritikal = _field(text,
                      r"\*\*1\)\s*Perkara Kritikal\*\*\s*\n+\s*(.+?)(?:\n\n|\Z)")
    # Bold competency units on the cover are the ones assessed practically.
    units = re.findall(r"\*\*([CEM]\d{2}\s+[^*⏎|]+)\*\*", text)

    rows = _section_rows(text, "SENARAI BAHAN") + _section_rows(text, "SENARAI PERALATAN")
    if not rows:
        raise ValueError(f"{soalan.name}: no items found in sections D or E")

    out = [
        f"**{JPK_FORM_NO}**",
        "",
        "# VERIFICATION FORM FOR PPA-PPT EQUIPMENT CHECK",
        "",
        f"**{ref}**" if ref else "",
        "",
        "Applicant / PPA-PPT: _________________________________",
        "",
        "Verification Date: _____________________________",
        "",
        "| Perkara | Maklumat |",
        "|---|---|",
        f"| **NOSS Code & Programme Name** | {kod} |",
        f"| **SET** | SET {set_id} |",
        f"| **NOSS / CU involved** | {'⏎'.join(u.strip() for u in units) if units else '⟪TBD: unit kompetensi yang dinilai secara amali | Jennifer | sebelum penghantaran⟫'} |",
        f"| **Competency** | {keterampilan or '—'} |",
        f"| **Critical Matter** | {kritikal or '—'} |",
        f"| **Assessment Duration** | {tempoh} |",
        "",
        "| NO. | LIST OF EQUIPMENT, MATERIALS AND DOCUMENTS | RATIO (P:C) | QUANTITY AVAILABLE — Filled by Applicant | QUANTITY AVAILABLE — JPK Verification |",
        "|---|---|---|---|---|",
    ]
    for i, (desc, ratio) in enumerate(rows, start=1):
        out.append(f"| {i} | {desc} | {ratio} | | |")

    # The sign-off is the table's last row, not a paragraph after it. As a
    # paragraph it orphaned onto a second page carrying nothing else — which
    # reads as a printing error on a form an officer signs. Inside the table it
    # travels with the rows, so the break happens where the content runs out.
    out.append("| ⟪SPAN⟫**Applicant / PPA-PPT** &nbsp;&nbsp; "
               "Signature: ____________________ &nbsp;&nbsp; "
               "Date: ______________ | | | | |")

    dest = soalan.with_name(soalan.stem.replace("-soalan", "-equipment-verification")
                            + ".md")
    return dest, "\n".join(line for line in out if line is not None) + "\n", len(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("soalan", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    paths = (sorted(PAPER_DIR.glob("*-soalan.md")) if args.all
             else [Path(p) for p in args.soalan])
    if not paths:
        sys.exit("nothing to generate")

    for soalan in paths:
        try:
            dest, content, n = build(soalan)
        except ValueError as e:
            print(f"SKIP {soalan.name}: {e}")
            continue
        if not args.dry_run:
            dest.write_text(content, encoding="utf-8")
        # Jennifer's own form carries 14 rows on a single page. Beyond that the
        # form genuinely needs a second page — that is a property of the paper,
        # not a layout failure, but it should be a visible decision rather than a
        # surprise at print time.
        note = f"  ⚠ over 14 rows — will run to a second page" if n > 14 else ""
        print(f"{dest.name:<58} {n} items from §D+§E{note}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
