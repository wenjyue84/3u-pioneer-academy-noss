"""
One-off: Download document-type media from 商学院ADI IT Program WhatsApp group
into From-WhatsApp folder. Run from repo root or project folder.
"""
import json
import re
import os
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError

# Path to the agent-tools output (from Periskope list_messages_in_a_chat)
TOOLS_PATH = Path(os.environ.get("AGENT_TOOLS_PATH", r"C:\Users\Jyue\.cursor\projects\c-Users-Jyue-Desktop-Projects-Obsidian-vault\agent-tools\5d545366-cc48-48fa-bbe6-61c04ef9b205.txt"))
OUT_DIR = Path(__file__).resolve().parent / "From-WhatsApp"

# Only download documents (pdf, doc, docx)
DOC_MIMETYPES = {
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}


def safe_filename(name: str) -> str:
    """Remove or replace chars unsafe for Windows."""
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    return name.strip() or "unnamed"


def main():
    if not TOOLS_PATH.exists():
        print(f"Missing: {TOOLS_PATH}")
        return
    with open(TOOLS_PATH, "r", encoding="utf-8") as f:
        raw = f.read()
    prefix = "Messages fetched successfully: "
    if raw.startswith(prefix):
        raw = raw[len(prefix) :]
    data = json.loads(raw)
    media_list = []
    for m in data.get("messages", []):
        media = m.get("media")
        if not media or not isinstance(media, dict) or not media.get("path"):
            continue
        mimetype = (media.get("mimetype") or "").lower()
        if mimetype not in DOC_MIMETYPES:
            continue
        filename = media.get("filename") or "unnamed"
        ext = Path(filename).suffix
        if not ext and mimetype:
            if "pdf" in mimetype:
                ext = ".pdf"
            elif "msword" in mimetype:
                ext = ".doc"
            elif "wordprocessingml" in mimetype:
                ext = ".docx"
        if not ext:
            ext = ".bin"
        if not filename.lower().endswith(ext.lower()):
            filename = filename + ext
        media_list.append(
            {"path": media["path"], "filename": safe_filename(filename), "mimetype": mimetype}
        )
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    downloaded = []
    for item in media_list:
        url = item["path"]
        filename = item["filename"]
        out_path = OUT_DIR / filename
        if out_path.exists():
            downloaded.append((filename, "skipped (exists)"))
            continue
        try:
            req = Request(url, headers={"User-Agent": "MCP-Download/1.0"})
            with urlopen(req, timeout=60) as resp:
                out_path.write_bytes(resp.read())
            downloaded.append((filename, "ok"))
        except (HTTPError, URLError, OSError) as e:
            downloaded.append((filename, f"error: {e}"))
    for name, status in downloaded:
        print(f"  {name} -> {status}")
    print(f"\nSaved to: {OUT_DIR.as_posix()}")


if __name__ == "__main__":
    main()
