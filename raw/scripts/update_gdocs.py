"""
Update existing Google Docs with .docx content using Drive API files.update.
Reads gogcli credentials and keyring token, then uploads .docx as replacement content.

Usage: uv run --with google-api-python-client --with google-auth --with keyring scripts/update_gdocs.py
"""

import json
import sys
import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "output"
STATE_FILE = PROJECT_DIR / "scripts" / ".gdrive-state.json"

# The original Google Docs created at the start
TARGET_DOCS = {
    "IT-020-3": {
        "doc_id": "1LHPCgRvy4rGVxCcIEoZAm5CVOtPRW_ubflvJSs8WsEo",
        "docx": "NOSS-IT-020-3-Computer-System-Operation.docx",
    },
    "IT-020-4": {
        "doc_id": "1c8K5bgHxgRABNyjNuhyNWBDIJ4FDgChwd8Oy_bafRog",
        "docx": "NOSS-IT-020-4-Computer-Systems-Administration.docx",
    },
    "IT-020-5": {
        "doc_id": "1lUAmUsevG4OwJ94pSq8TD2CnwXAuMe2Y3ubm2ySzxTg",
        "docx": "NOSS-IT-020-5-Computer-Systems-Management.docx",
    },
}


def get_access_token():
    """Get a fresh access token by running gog auth and extracting from keyring."""
    # Force a token refresh by making a simple API call
    result = subprocess.run(
        ["gog", "drive", "ls", "--json", "--no-input"],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        print(f"[ERROR] Failed to refresh token: {result.stderr}")
        return None

    # Try to extract token from keyring via Python
    try:
        import keyring
        token_json = keyring.get_password("gogcli", "wenjyue@gmail.com:default:token")
        if token_json:
            token_data = json.loads(token_json)
            return token_data.get("access_token")
    except Exception as e:
        print(f"[WARN] Keyring access failed: {e}")

    # Fallback: try to get token from gog's internal state
    try:
        import ctypes
        import ctypes.wintypes

        # Try Windows Credential Manager directly
        from ctypes import windll, byref, create_unicode_buffer, Structure, POINTER
        # This is complex — fall back to google-auth
    except Exception:
        pass

    # Final fallback: use google-auth with stored credentials
    try:
        creds_path = Path.home() / "AppData" / "Roaming" / "gogcli" / "credentials.json"
        if creds_path.exists():
            creds_data = json.loads(creds_path.read_text())
            client_id = creds_data.get("client_id")
            client_secret = creds_data.get("client_secret")
            if client_id and client_secret:
                print(f"  Found client credentials, but need refresh token from keyring")
    except Exception:
        pass

    return None


def update_doc_via_curl(doc_id, docx_path, access_token):
    """Update a Google Doc by replacing its content with .docx via Drive API."""
    import subprocess

    url = f"https://www.googleapis.com/upload/drive/v3/files/{doc_id}?uploadType=media"
    result = subprocess.run(
        [
            "curl", "-s", "-X", "PATCH",
            "-H", f"Authorization: Bearer {access_token}",
            "-H", "Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "--data-binary", f"@{docx_path}",
            url,
        ],
        capture_output=True, text=True, timeout=60
    )
    if result.returncode == 0:
        try:
            resp = json.loads(result.stdout)
            if "id" in resp:
                return resp
            elif "error" in resp:
                print(f"  [ERROR] {resp['error'].get('message', resp)}")
        except json.JSONDecodeError:
            print(f"  [ERROR] Response: {result.stdout[:200]}")
    else:
        print(f"  [ERROR] curl failed: {result.stderr[:200]}")
    return None


def update_doc_via_gapi(doc_id, docx_path):
    """Update via google-api-python-client (if available)."""
    try:
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
        import keyring

        # Get token from keyring
        token_json = keyring.get_password("gogcli", "wenjyue@gmail.com:default:token")
        if not token_json:
            print("  [ERROR] No token in keyring")
            return None

        token_data = json.loads(token_json)
        creds_path = Path.home() / "AppData" / "Roaming" / "gogcli" / "credentials.json"
        creds_data = json.loads(creds_path.read_text())

        creds = Credentials(
            token=token_data.get("access_token"),
            refresh_token=token_data.get("refresh_token"),
            token_uri="https://oauth2.googleapis.com/token",
            client_id=creds_data.get("client_id"),
            client_secret=creds_data.get("client_secret"),
        )

        service = build("drive", "v3", credentials=creds)
        media = MediaFileUpload(
            str(docx_path),
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            resumable=True,
        )

        result = service.files().update(
            fileId=doc_id,
            media_body=media,
        ).execute()

        return result

    except ImportError as e:
        print(f"  [ERROR] Missing dependency: {e}")
        return None
    except Exception as e:
        print(f"  [ERROR] API call failed: {e}")
        return None


def main():
    print("Updating original Google Docs with .docx content...")
    print()

    for level_key, info in TARGET_DOCS.items():
        doc_id = info["doc_id"]
        docx_path = OUTPUT_DIR / info["docx"]

        if not docx_path.exists():
            print(f"[{level_key}] SKIP - .docx not found: {docx_path}")
            continue

        print(f"[{level_key}] Updating doc {doc_id}...")
        print(f"  Source: {docx_path} ({docx_path.stat().st_size / 1024:.1f} KB)")

        result = update_doc_via_gapi(doc_id, docx_path)

        if result:
            print(f"  OK - Updated: https://docs.google.com/document/d/{doc_id}/edit")
        else:
            print(f"  FAILED - Could not update doc")

    print()
    print("Done. Original Google Doc links:")
    print("  L3: https://docs.google.com/document/d/1LHPCgRvy4rGVxCcIEoZAm5CVOtPRW_ubflvJSs8WsEo/edit")
    print("  L4: https://docs.google.com/document/d/1c8K5bgHxgRABNyjNuhyNWBDIJ4FDgChwd8Oy_bafRog/edit")
    print("  L5: https://docs.google.com/document/d/1lUAmUsevG4OwJ94pSq8TD2CnwXAuMe2Y3ubm2ySzxTg/edit")


if __name__ == "__main__":
    main()
