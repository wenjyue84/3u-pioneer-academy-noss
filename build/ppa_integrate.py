#!/usr/bin/env python3
"""PPA integrator — md -> docx -> real page count -> backfill declaration -> rebuild -> PDF.

Known traps (LOG 2026-08-24 + this session):
- Word COM PDF export can raise HRESULT yet leave a stale file -> every PDF verified
  by mtime-after-start AND size > 0.
- Word 2007 COM crashes (RPC unavailable) on rapid open/close cycles -> one Open per
  measurement, page count + export share a single Open, and a dead Word instance is
  restarted automatically (max 2 retries per file).

Usage: uv run --with pywin32 --with python-docx python build/ppa_integrate.py <f1.md> [...]
"""
import subprocess
import sys
import time
from pathlib import Path

import pythoncom
import win32com.client
from pywintypes import com_error

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "output" / "jennifer-ppa-soalan"
DOCX_DIR = OUT / "docx"
PDF_DIR = OUT / "pdf"
PLACEHOLDER = "⟪" + "PAGES" + "⟫"  # ⟪PAGES⟫
WD_STAT_PAGES = 2
WD_EXPORT_PDF = 17

_word = None


def word():
    global _word
    if _word is None:
        _word = win32com.client.gencache.EnsureDispatch("Word.Application")
        _word.Visible = False
        time.sleep(1)
    return _word


def kill_word():
    global _word
    try:
        _word.Quit()
    except Exception:
        subprocess.run(["taskkill", "/f", "/im", "WINWORD.EXE"],
                       capture_output=True)
    _word = None
    time.sleep(2)


def build_docx(md: Path, docx: Path):
    r = subprocess.run(
        [sys.executable, str(ROOT / "build" / "wim_md_to_docx.py"), str(md),
         "--style", "KP", "--output", str(docx)],
        capture_output=True, text=True)
    if r.returncode != 0 or not docx.exists():
        raise RuntimeError(f"build failed for {md.name}: {r.stderr[-400:]}")


def measure(docx: Path, pdf: Path = None):
    """One Word Open: return page count; export PDF too if pdf given."""
    doc = word().Documents.Open(str(docx), ReadOnly=True)
    try:
        pages = doc.ComputeStatistics(WD_STAT_PAGES)
        if pdf is not None:
            doc.ExportAsFixedFormat(OutputFileName=str(pdf),
                                    ExportFormat=WD_EXPORT_PDF)
        return pages
    finally:
        doc.Close(False)


def measure_retry(docx, pdf=None, tries=3):
    for i in range(tries):
        try:
            return measure(docx, pdf)
        except com_error as e:
            if i == tries - 1:
                raise
            print(f"  word died ({e.args[1] if len(e.args) > 1 else e}); restarting…",
                  flush=True)
            kill_word()


def process(md: Path):
    name = md.stem
    docx = DOCX_DIR / f"{name}.docx"
    pdf = PDF_DIR / f"{name}.pdf"
    text = md.read_text(encoding="utf-8")

    build_docx(md, docx)
    if PLACEHOLDER in text:
        pages = measure_retry(docx)          # open #1: count only
        for _ in range(3):
            md.write_text(text.replace(PLACEHOLDER, str(pages)), encoding="utf-8")
            build_docx(md, docx)
            t0 = time.time()
            if pdf.exists():
                pdf.unlink()
            newpages = measure_retry(docx, pdf)  # open #2: verify + export
            if newpages == pages:
                break
            pages = newpages
        else:
            raise RuntimeError(f"page count never stabilised for {name}")
    else:
        t0 = time.time()
        if pdf.exists():
            pdf.unlink()
        pages = measure_retry(docx, pdf)

    if not pdf.exists() or pdf.stat().st_size == 0 or pdf.stat().st_mtime < t0:
        raise RuntimeError(f"PDF verify failed for {name}")
    return pages, pdf.stat().st_size


def main(files):
    DOCX_DIR.mkdir(exist_ok=True)
    PDF_DIR.mkdir(exist_ok=True)
    pythoncom.CoInitialize()
    ok, failures = [], []
    for f in files:
        md = Path(f).resolve()
        try:
            pages, size = process(md)
            ok.append((md.stem, pages))
            print(f"OK  {md.stem}: {pages}pp, pdf {size//1024}KB", flush=True)
        except Exception as e:  # noqa: BLE001 — keep batch going
            failures.append((md.stem, str(e)))
            print(f"FAIL {md.stem}: {e}", flush=True)
    kill_word()
    print(f"\n{len(ok)} ok, {len(failures)} failed")
    for n, err in failures:
        print(f"  FAILED: {n}: {err}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    main(sys.argv[1:])
