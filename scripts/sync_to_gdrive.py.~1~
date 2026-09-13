"""
Sync generated .docx files to Google Docs via gogcli.
Exports .docx content and updates the existing Google Docs.

Usage: uv run scripts/sync_to_gdrive.py
"""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "output"
STATE_FILE = PROJECT_DIR / "scripts" / ".gdrive-state.json"
LOG_DIR = PROJECT_DIR / "logs"

GOG = "gog"  # gogcli binary


def run_gog(args, check=True):
    """Run a gogcli command and return output."""
    cmd = [GOG] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"  [ERROR] gog {' '.join(args)}: {result.stderr.strip()}")
        return None
    return result.stdout.strip()


def load_state():
    """Load the gdrive state file."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {"docs": {}, "last_sync": None}


def save_state(state):
    """Save the gdrive state file."""
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def upload_docx_to_gdoc(docx_path, doc_id):
    """Upload a .docx file to overwrite an existing Google Doc.

    gogcli doesn't support direct update, so we:
    1. Export current content as reference
    2. Upload new .docx as a new file
    3. Note: For true overwrite, we'd need Google Drive API directly.

    For now, we upload as a new version alongside and note the file ID.
    """
    # Upload the .docx to the same folder
    result = run_gog([
        "drive", "upload", str(docx_path),
        "--name", docx_path.stem,
        "--json", "--no-input"
    ], check=False)

    if result:
        try:
            data = json.loads(result)
            file_id = data.get("file", {}).get("id", "")
            link = data.get("file", {}).get("webViewLink", "")
            print(f"  Uploaded: {docx_path.name} -> {link}")
            return {"id": file_id, "link": link}
        except json.JSONDecodeError:
            print(f"  [WARN] Could not parse upload response: {result[:200]}")

    return None


def update_google_doc_content(doc_id, docx_path):
    """Update a Google Doc with content from a .docx file.

    Since gogcli doesn't support direct content replacement,
    we use a workaround: read the .md source and push text content.
    The .docx is uploaded separately to Drive for download.
    """
    # For now, log that we need to update
    print(f"  Google Doc {doc_id}: content update queued")
    print(f"  .docx file: {docx_path}")
    return True


def sync_all():
    """Sync all generated .docx files to Google Drive."""
    state = load_state()
    docs = state.get("docs", {})

    print("NOSS Google Drive Sync")
    print(f"Output dir: {OUTPUT_DIR}")
    print()

    docx_files = sorted(OUTPUT_DIR.glob("*.docx"))
    if not docx_files:
        print("[SKIP] No .docx files found in output/")
        return

    synced = 0
    for docx_path in docx_files:
        # Determine which level this is
        level_key = None
        for key in ["IT-020-3", "IT-020-4", "IT-020-5"]:
            if key.replace("-", "-") in docx_path.name.replace("_", "-"):
                level_key = key
                break

        if not level_key:
            print(f"  [SKIP] Cannot determine level for: {docx_path.name}")
            continue

        doc_info = docs.get(level_key, {})
        doc_id = doc_info.get("id", "")

        print(f"[{level_key}] Syncing {docx_path.name}...")

        if doc_id:
            # Upload .docx to Drive (alongside Google Doc)
            upload_result = upload_docx_to_gdoc(docx_path, doc_id)
            if upload_result:
                docs[level_key]["docx_upload"] = upload_result
                docs[level_key]["last_sync"] = datetime.now().isoformat()
                synced += 1
        else:
            print(f"  [WARN] No Google Doc ID for {level_key}")
            # Upload anyway
            upload_result = upload_docx_to_gdoc(docx_path, "")
            if upload_result:
                synced += 1

    # Update state
    state["docs"] = docs
    state["last_sync"] = datetime.now().isoformat()
    save_state(state)

    print()
    print(f"Synced {synced}/{len(docx_files)} files")

    # Print links
    print()
    print("Google Doc links (view/comment):")
    for key, info in docs.items():
        url = info.get("url", "N/A")
        print(f"  {key}: {url}")
        if "docx_upload" in info:
            print(f"    .docx: {info['docx_upload'].get('link', 'N/A')}")


if __name__ == "__main__":
    sync_all()
