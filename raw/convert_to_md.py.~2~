"""
Convert From-WhatsApp doc/docx/pdf to Markdown.
Uses: pypdf (PDF), python-docx (docx). For .doc, extracts raw text via olefile if possible, else placeholder.
Run: uv run --with pypdf --with python-docx convert_to_md.py
"""
import re
import sys
from pathlib import Path

# Optional deps - fail gracefully
try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None
try:
    from docx import Document as DocxDocument
except ImportError:
    DocxDocument = None

FROM_DIR = Path(__file__).resolve().parent / "From-WhatsApp"
DOC_MIMETYPES = {".doc", ".docx", ".pdf"}


def safe_md_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", name).strip() or "unnamed"


def pdf_to_md(path: Path) -> str:
    if not PdfReader:
        return f"*[Install pypdf to convert PDF: uv run --with pypdf]*\n\nSource: {path.name}"
    reader = PdfReader(path)
    parts = [f"# {path.stem}\n\n"]
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            parts.append(f"## Page {i + 1}\n\n{text}\n\n")
    return "\n".join(parts)


def docx_to_md(path: Path) -> str:
    if not DocxDocument:
        return f"*[Install python-docx to convert DOCX]*\n\nSource: {path.name}"
    doc = DocxDocument(path)
    parts = [f"# {path.stem}\n\n"]
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        style = para.style.name if para.style else ""
        if "Heading" in style or "Title" in style:
            level = 2
            if "Heading 1" in style or "Title" in style:
                level = 1
            parts.append(f"{'#' * level} {text}\n\n")
        else:
            parts.append(f"{text}\n\n")
    for table in doc.tables:
        rows = []
        for row in table.rows:
            cells = [c.text.replace("\n", " ").strip() for c in row.cells]
            rows.append("| " + " | ".join(cells) + " |")
        if rows:
            parts.append("\n".join(rows) + "\n\n")
    return "\n".join(parts)


def doc_to_md(path: Path) -> str:
    """Legacy .doc: try reading as OLE and extract WordDocument stream text (simplified)."""
    try:
        import olefile
        ole = olefile.OleFileIO(path)
        if ole.exists("WordDocument"):
            stream = ole.openstream("WordDocument")
            data = stream.read()
            # Very simplified: extract printable ASCII/Unicode runs (CP1252/UTF-16 common in .doc)
            text = data.decode("utf-16-le", errors="ignore") if b"\x00" in data[:100] else data.decode("latin-1", errors="ignore")
            # Keep only reasonable text runs
            text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]+", " ", text)
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) > 100:
                return f"# {path.stem}\n\n{text}\n"
    except Exception:
        pass
    return f"# {path.stem}\n\n*[Legacy .doc: open in Word and Save As .docx, then re-run this script to convert.]*\n\nSource: {path.name}"


def main():
    FROM_DIR.mkdir(parents=True, exist_ok=True)
    converted = []
    for f in sorted(FROM_DIR.iterdir()):
        if f.suffix.lower() not in DOC_MIMETYPES:
            continue
        md_path = FROM_DIR / (f.stem + ".md")
        try:
            if f.suffix.lower() == ".pdf":
                content = pdf_to_md(f)
            elif f.suffix.lower() == ".docx":
                content = docx_to_md(f)
            else:
                content = doc_to_md(f)
            md_path.write_text(content, encoding="utf-8")
            converted.append(md_path.name)
        except Exception as e:
            md_path.write_text(f"# {f.stem}\n\nConversion error: {e}\n\nSource: {f.name}", encoding="utf-8")
            converted.append(md_path.name + " (error)")
    for c in converted:
        print(c)
    return 0


if __name__ == "__main__":
    sys.exit(main())
