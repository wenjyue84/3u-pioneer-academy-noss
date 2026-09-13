"""Bring an existing PPT-PPA paper up to the JPK cover format, mechanically.

The 36 papers generated on 2026-08-24 all share one cover shape: a stack of bold
paragraphs separated by `---` rules. Jennifer's own papers put the same
information in **one bordered table** with the Jata Negara crest in its top-left
cell (`_engine/FORMAT-jpk-ppa.md` §2). Rewriting forty files by hand is not a
plan; the transformation is deterministic, so it belongs in code.

What it does, per file:
  * replaces the paragraph cover with the bordered-table cover, using the
    `⟪LOGO⟫` / `⏎` / `⟪SPAN⟫` tokens the renderer resolves;
  * bolds the practical competency units when a profile says which they are —
    that is how Jennifer's paper encodes the selection;
  * swaps a hardcoded printed-page count for `⟪PAGES⟫` so the renderer backfills
    the real one;
  * drops the H1 that duplicates the title now inside the table.

Idempotent: a file that already has `⟪LOGO⟫` is left alone.

    uv run python -m _engine.migrate_cover --all --dry-run
    uv run python -m _engine.migrate_cover output/jennifer-ppa-soalan/n821-*.md
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _engine.ppa.schema import Profile

ROOT = Path(__file__).resolve().parent.parent
PAPER_DIR = ROOT / "output" / "jennifer-ppa-soalan"
PROFILE_DIR = ROOT / "_engine" / "profiles"

JPK_ADDRESS = ("**JABATAN PEMBANGUNAN KEMAHIRAN**⏎**KEMENTERIAN SUMBER MANUSIA**⏎"
               "ARAS 7 & 8 SETIA PERKASA 4,⏎KOMPLEKS SETIA PERKASA⏎62530 PUTRAJAYA")

CANDIDATE_ROWS = ["NAMA CALON", "NO KAD PENGENALAN", "TARIKH PENILAIAN",
                  "MASA MULA", "MASA TAMAT"]


def _grab(pattern: str, text: str, group: int = 1) -> str:
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(group).strip() if m else ""


def build_cover(text: str, kind: str, practical: set[str],
                unit_source: str = "") -> str | None:
    """Return the replacement cover table, or None if the parts aren't all there."""
    # Three cover dialects exist across the 2026-08-24 batch — the title is
    # sometimes a bold line, sometimes only the H1; the centre name sometimes sits
    # a blank line below its label and sometimes on the very next line. Accept
    # whichever spelling is present rather than insisting on one canonical form.
    title = (_grab(r"^\*\*((?:SOALAN|SKEMA)[^*]+\(SET [AB]\))\*\*", text)
             or _grab(r"^#\s+((?:SOALAN|SKEMA)[^\n]*\(SET [AB]\))", text))
    centre = _grab(r"^\*\*KOD DAN NAMA PUSAT BERTAULIAH/SYARIKAT\*\*\s*\n+\s*(.+)$", text)
    kod = _grab(r"^\*\*KOD KOMPETENSI:?\*\*[:\s]*(.+)$", text)
    units = re.findall(r"^-\s+([A-Z]{1,2}\d{2}\s+.+)$", text, re.MULTILINE)
    if not units and unit_source:
        # A SKEMA cover in the 2026-08-24 batch omits the competency-unit list
        # entirely; Jennifer's carries it. Take it from the paper's own SOALAN
        # sibling rather than inventing one.
        units = re.findall(r"^-\s+([A-Z]{1,2}\d{2}\s+.+)$", unit_source, re.MULTILINE)
    if not (title and centre and kod and units):
        return None

    def fmt(u: str) -> str:
        code = u.split()[0].upper()
        return f"**{u.strip()}**" if code in practical else u.strip()

    rows = [
        f"| ⟪LOGO⟫ | {JPK_ADDRESS} |",
        "|---|---|",
        f"| **KOD DAN NAMA PUSAT BERTAULIAH/SYARIKAT** | {centre} |",
        f"| ⟪SPAN⟫**{title}** | |",
        f"| **KOD KOMPETENSI** | {kod} |",
        f"| **NAMA UNIT KOMPETENSI** | {'⏎'.join(fmt(u) for u in units)} |",
    ]
    # The SKEMA is the examiner's copy: it carries a date rather than the
    # candidate's particulars.
    rows += ([f"| **TARIKH** | |"] if kind == "skema"
             else [f"| {label} | _________________________ |" for label in CANDIDATE_ROWS])
    return "\n".join(rows)


def migrate(path: Path, practical: set[str], dry_run: bool = False) -> str:
    text = path.read_text(encoding="utf-8")
    if "⟪LOGO⟫" in text:
        return "already migrated"

    kind = "skema" if "skema" in path.stem else "soalan"
    sibling = path.with_name(path.stem.replace("-skema", "-soalan") + ".md")
    unit_source = sibling.read_text(encoding="utf-8") if (
        kind == "skema" and sibling.exists()) else ""
    cover = build_cover(text, kind, practical, unit_source)
    if cover is None:
        return "SKIPPED — cover fields not recognised"

    # The old cover runs from the JPK address block to the candidate table.
    start = text.find("**JABATAN PEMBANGUNAN KEMAHIRAN")
    end_marker = re.search(r"^\|\s*MASA TAMAT\s*\|.*$|^\|\s*TARIKH\s*\|.*$",
                           text, re.MULTILINE)
    if not end_marker:
        # A SKEMA with no candidate block ends its cover at the last
        # competency-unit bullet, or failing that at the competency-code line.
        bullets = list(re.finditer(r"^-\s+[A-Z]{1,2}\d{2}\s+.+$", text, re.MULTILINE))
        end_marker = (bullets[-1] if bullets else
                      re.search(r"^\*\*KOD KOMPETENSI:?\*\*[^\n]*$", text, re.MULTILINE))
    if start < 0 or not end_marker:
        return "SKIPPED — cover boundaries not found"
    new = text[:start] + cover + text[end_marker.end():]

    # The title now lives inside the table; the H1 above it is a duplicate.
    new = re.sub(r"\A#\s+(?:SOALAN|SKEMA)[^\n]*\n+", "", new)
    # Leftover horizontal rules where the paragraph blocks used to be, including
    # one stranded above the new table — it renders as a stray line over the crest.
    new = re.sub(r"(\n---\n){2,}", "\n---\n", new)
    new = re.sub(r"\A(?:\s*---\s*\n)+", "", new)
    new = re.sub(r"\n-{3,}\n(\s*\|\s*⟪LOGO⟫)", r"\n\1", new)

    before = new
    new = re.sub(r"(MENGANDUNGI\s+)\*{0,2}\d+\*{0,2}(\s+MUKA SURAT)",
                 r"\1⟪PAGES⟫\2", new)
    pages = "page count → ⟪PAGES⟫" if new != before else "no page declaration"

    if not dry_run:
        path.write_text(new, encoding="utf-8")
    bolded = len(practical & {u.split()[0].upper()
                              for u in re.findall(r"^-\s+([A-Z]{1,2}\d{2}\s+.+)$", text,
                                                  re.MULTILINE)})
    return f"cover → table ({bolded} units bolded), {pages}"


def practical_for(path: Path) -> set[str]:
    """The practical units from a matching profile, or empty if none exists yet.

    No profile means the course owner has not chosen yet — in that case every unit
    stays unbolded rather than guessing, because the bolding *is* the choice.
    """
    for pf in PROFILE_DIR.glob("*.json"):
        if path.stem.startswith(pf.stem):
            return set(Profile.load(pf).practical_cus)
    return set()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if args.all:
        paths = sorted(p for p in PAPER_DIR.glob("*.md")
                       if re.search(r"-(soalan|skema)$", p.stem))
    else:
        paths = [Path(p) for p in args.paths]
    if not paths:
        sys.exit("nothing to migrate")

    for p in paths:
        print(f"{p.name:<56} {migrate(p, practical_for(p), args.dry_run)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
