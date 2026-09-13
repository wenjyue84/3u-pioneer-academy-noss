"""md → docx → real page count → backfill ⟪PAGES⟫ → re-render → PDF.

JPK papers declare their own printed length on the cover ("KERTAS INI MENGANDUNGI
n MUKA SURAT BERCETAK"). The declaration is what stops a page being pulled from a
sealed paper without anyone noticing, so it has to be right — and it cannot be
known until the document is laid out. Both of Jennifer's own reference papers got
it wrong (soalan declared 13 for 14 pages, skema declared 14 for 11).

So the markdown carries the literal placeholder `⟪PAGES⟫`, and this script:
  1. renders the docx,
  2. asks Word for the page count,
  3. writes the number back into the markdown,
  4. re-renders — because the number itself can change the layout — and
  5. re-counts, repeating until the count is stable,
  6. exports the PDF and verifies the file was actually written this run.

Replaces `build/ppa_integrate.py`, which drove the WIM textbook renderer. Traps
inherited from it and kept: Word COM can raise HRESULT and still leave a stale
PDF on disk, so every export is verified by mtime and size; and Word 2007 dies on
rapid open/close cycles, so a dead instance is restarted rather than propagated.

Usage:
    uv run --with pywin32 --with python-docx python -m _engine.render.integrate \
        output/jennifer-ppa-soalan/fb-018-3-set-b-soalan.md
"""
from __future__ import annotations

import argparse
import re
import time
from pathlib import Path

import pythoncom
import win32com.client
from pywintypes import com_error

from .ppa_docx import render

ROOT = Path(__file__).resolve().parents[2]
PLACEHOLDER = "⟪" + "PAGES" + "⟫"   # ⟪PAGES⟫
WD_STAT_PAGES = 2
WD_EXPORT_PDF = 17
MAX_LAYOUT_ROUNDS = 4

_word = None


def word():
    global _word
    if _word is None:
        _word = win32com.client.DispatchEx("Word.Application")
        _word.Visible = False
        _word.DisplayAlerts = 0
    return _word


def kill_word() -> None:
    global _word
    try:
        if _word is not None:
            _word.Quit()
    except Exception:                      # noqa: BLE001 — Word is already gone
        pass
    _word = None


REF_CODE = re.compile(
    # NOSS codes come in two shapes: letters only (FB-018-3:2012) and letters
    # followed by digits (N821-001-3:2020, M731-001-3:2021, G471-001-3:2018).
    # An earlier pattern required `[A-Z]{1,3}` then digits-as-the-block, so the
    # second shape never matched and three of the five subjects rendered with no
    # page header at all.
    # `\d{1,2}` on the level, because FB-018-45 covers levels 4 and 5 together.
    r"\b([A-Z]{1,3}\d*-\d{3}-\d{1,2}(?::\d{4})?/\d{4}/[AB]/\d+)\b")


def _ref_code(text: str) -> str:
    """The paper's own reference code, for the page header."""
    m = REF_CODE.search(text)
    return m.group(1) if m else ""


def measure(docx: Path, pdf: Path | None = None) -> int:
    """One Word Open: page count, and the PDF export too when asked.

    Counting and exporting share a single Open on purpose — the open/close cycle
    is what kills Word, not the work done inside it.
    """
    doc = word().Documents.Open(str(docx.resolve()), ReadOnly=True)
    try:
        pages = doc.ComputeStatistics(WD_STAT_PAGES)
        if pdf is not None:
            doc.ExportAsFixedFormat(OutputFileName=str(pdf.resolve()),
                                    ExportFormat=WD_EXPORT_PDF)
        return pages
    finally:
        doc.Close(False)


def measure_retry(docx: Path, pdf: Path | None = None, tries: int = 3) -> int:
    for i in range(tries):
        try:
            return measure(docx, pdf)
        except com_error as e:
            if i == tries - 1:
                raise
            print(f"    word died ({e.args[1] if len(e.args) > 1 else e}); restarting…",
                  flush=True)
            kill_word()
    raise RuntimeError("unreachable")


# Render settings that belong to the document type, not to whoever runs the
# command. The JPK equipment-verification form is one page by design and needs
# tighter type and margins to stay that way; everything else uses the house
# defaults. Keeping this here rather than in the caller's flags is deliberate —
# on 2026-08-25 a batch was launched with the equipment settings applied to
# soalan and skema too, which would have made those papers inconsistent with the
# eighteen already rendered.
KIND_SETTINGS = {
    "equipment-verification": {"table_font_pt": 9, "margin_cm": 1.8},
}
DEFAULT_SETTINGS = {"table_font_pt": 10, "margin_cm": None}


def settings_for(md: Path) -> dict:
    for suffix, opts in KIND_SETTINGS.items():
        if md.stem.endswith(suffix):
            return opts
    return DEFAULT_SETTINGS


def process(md: Path, docx_dir: Path, pdf_dir: Path,
            table_font_pt: float | None = None,
            margin_cm: float | None = None) -> tuple[int, int]:
    docx = docx_dir / f"{md.stem}.docx"
    pdf = pdf_dir / f"{md.stem}.pdf"
    original = md.read_text(encoding="utf-8")
    ref = _ref_code(original)

    # An explicit flag wins; otherwise the document type decides.
    defaults = settings_for(md)
    if table_font_pt is None:
        table_font_pt = defaults["table_font_pt"]
    if margin_cm is None:
        margin_cm = defaults["margin_cm"]

    render(md, docx, ref, table_font_pt=table_font_pt, margin_cm=margin_cm)

    if PLACEHOLDER in original:
        pages = measure_retry(docx)
        for _ in range(MAX_LAYOUT_ROUNDS):
            md.write_text(original.replace(PLACEHOLDER, str(pages)), encoding="utf-8")
            render(md, docx, ref, table_font_pt=table_font_pt, margin_cm=margin_cm)
            t0 = time.time()
            pdf.unlink(missing_ok=True)
            settled = measure_retry(docx, pdf)
            if settled == pages:
                break
            # Writing a longer number can push a line over and add a page. Restore
            # the placeholder before trying again so the file never carries a
            # count from a previous, now-wrong layout.
            md.write_text(original, encoding="utf-8")
            pages = settled
        else:
            md.write_text(original, encoding="utf-8")
            raise RuntimeError(f"page count never settled for {md.name} "
                               f"after {MAX_LAYOUT_ROUNDS} rounds")
    else:
        t0 = time.time()
        pdf.unlink(missing_ok=True)
        pages = measure_retry(docx, pdf)

    if not pdf.exists() or pdf.stat().st_size == 0 or pdf.stat().st_mtime < t0:
        raise RuntimeError(f"PDF was not written this run: {pdf}")

    _assert_declaration_matches(md, pdf, pages)
    return pages, pdf.stat().st_size


def _assert_declaration_matches(md: Path, pdf: Path, pages: int) -> None:
    """Cross-check the number in the markdown against the PDF that was produced.

    The backfill loop above should make this impossible, and on 2026-08-25 it did
    not: a re-render after a margin change left the SOALAN declaring 12 pages
    while the PDF was 13. The loop's own bookkeeping is not evidence — the two
    artefacts are. This is the last thing that runs, and it fails the file rather
    than shipping the exact defect the loop exists to prevent.
    """
    m = re.search(r"MENGANDUNGI\s+\*{0,2}(\d+)\*{0,2}\s+MUKA SURAT",
                  md.read_text(encoding="utf-8"), re.IGNORECASE)
    if not m:
        return                                   # no declaration in this document
    declared = int(m.group(1))
    if declared != pages:
        raise RuntimeError(
            f"{md.name} declares {declared} printed pages but the rendered PDF has "
            f"{pages}. Re-run with the ⟪PAGES⟫ placeholder restored.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("input", nargs="+", help="input .md file(s)")
    ap.add_argument("--docx-dir", default=None)
    ap.add_argument("--pdf-dir", default=None)
    ap.add_argument("--table-font-pt", type=float, default=None,
                    help="override the per-document-type table font size")
    ap.add_argument("--margin-cm", type=float, default=None,
                    help="override the per-document-type page margins")
    args = ap.parse_args()

    files = [Path(f).resolve() for f in args.input]
    docx_dir = Path(args.docx_dir) if args.docx_dir else files[0].parent / "docx"
    pdf_dir = Path(args.pdf_dir) if args.pdf_dir else files[0].parent / "pdf"
    docx_dir.mkdir(parents=True, exist_ok=True)
    pdf_dir.mkdir(parents=True, exist_ok=True)

    pythoncom.CoInitialize()
    ok, failed = [], []
    for md in files:
        try:
            pages, size = process(md, docx_dir, pdf_dir, args.table_font_pt,
                                  args.margin_cm)
            ok.append((md.stem, pages))
            print(f"OK   {md.stem}: {pages}pp, pdf {size // 1024}KB", flush=True)
        except Exception as e:                      # noqa: BLE001 — keep the batch going
            failed.append((md.stem, str(e)))
            print(f"FAIL {md.stem}: {e}", flush=True)
    kill_word()

    print(f"\n{len(ok)} ok, {len(failed)} failed")
    for name, err in failed:
        print(f"  {name}: {err}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
