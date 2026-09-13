"""Update original Google Docs with .docx content using refresh_token from keyring."""
import ctypes
import ctypes.wintypes
import json
import sys
import subprocess
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "output"
CREDS_PATH = Path.home() / "AppData" / "Roaming" / "gogcli" / "credentials.json"

DOCS = {
    "IT-020-3": ("1LHPCgRvy4rGVxCcIEoZAm5CVOtPRW_ubflvJSs8WsEo", "NOSS-IT-020-3-Computer-System-Operation.docx"),
    "IT-020-4": ("1c8K5bgHxgRABNyjNuhyNWBDIJ4FDgChwd8Oy_bafRog", "NOSS-IT-020-4-Computer-Systems-Administration.docx"),
    "IT-020-5": ("1lUAmUsevG4OwJ94pSq8TD2CnwXAuMe2Y3ubm2ySzxTg", "NOSS-IT-020-5-Computer-Systems-Management.docx"),
}

# Step 1: Read refresh_token from Windows Credential Manager
CRED_TYPE_GENERIC = 1

class CREDENTIAL(ctypes.Structure):
    _fields_ = [
        ("Flags", ctypes.wintypes.DWORD),
        ("Type", ctypes.wintypes.DWORD),
        ("TargetName", ctypes.wintypes.LPWSTR),
        ("Comment", ctypes.wintypes.LPWSTR),
        ("LastWritten", ctypes.wintypes.FILETIME),
        ("CredentialBlobSize", ctypes.wintypes.DWORD),
        ("CredentialBlob", ctypes.POINTER(ctypes.c_byte)),
        ("Persist", ctypes.wintypes.DWORD),
        ("AttributeCount", ctypes.wintypes.DWORD),
        ("Attributes", ctypes.c_void_p),
        ("TargetAlias", ctypes.wintypes.LPWSTR),
        ("UserName", ctypes.wintypes.LPWSTR),
    ]

advapi32 = ctypes.windll.advapi32
cred_ptr = ctypes.POINTER(CREDENTIAL)()
ok = advapi32.CredReadW("keyring:gogcli:token:default:wenjyue@gmail.com", CRED_TYPE_GENERIC, 0, ctypes.byref(cred_ptr))

if not ok:
    print("FAILED: could not read credential")
    sys.exit(1)

blob = ctypes.string_at(cred_ptr.contents.CredentialBlob, cred_ptr.contents.CredentialBlobSize)
advapi32.CredFree(cred_ptr)
token_data = json.loads(blob.decode("utf-8"))
refresh_token = token_data["refresh_token"]

# Step 2: Read client_id and client_secret
creds = json.loads(CREDS_PATH.read_text())
client_id = creds["client_id"]
client_secret = creds["client_secret"]

# Step 3: Exchange refresh_token for access_token
print("Exchanging refresh_token for access_token...")
data = urlencode({
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token,
    "grant_type": "refresh_token",
}).encode()

req = Request("https://oauth2.googleapis.com/token", data=data, method="POST")
req.add_header("Content-Type", "application/x-www-form-urlencoded")
resp = urlopen(req, timeout=30)
token_resp = json.loads(resp.read())
access_token = token_resp["access_token"]
print(f"Got access_token (length: {len(access_token)})")

# Step 4: Update each Google Doc
for level, (doc_id, filename) in DOCS.items():
    docx_path = OUTPUT_DIR / filename
    if not docx_path.exists():
        print(f"[{level}] SKIP - {filename} not found")
        continue

    print(f"[{level}] Updating {doc_id} with {filename} ({docx_path.stat().st_size // 1024} KB)...")

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
            r = json.loads(result.stdout)
            if "id" in r:
                print(f"[{level}] OK")
            else:
                print(f"[{level}] ERROR: {r.get('error', {}).get('message', result.stdout[:200])}")
        except json.JSONDecodeError:
            print(f"[{level}] ERROR: {result.stdout[:200]}")
    else:
        print(f"[{level}] CURL FAILED: {result.stderr[:200]}")

print()
print("Original Google Doc links (now with content):")
print("  L3: https://docs.google.com/document/d/1LHPCgRvy4rGVxCcIEoZAm5CVOtPRW_ubflvJSs8WsEo/edit")
print("  L4: https://docs.google.com/document/d/1c8K5bgHxgRABNyjNuhyNWBDIJ4FDgChwd8Oy_bafRog/edit")
print("  L5: https://docs.google.com/document/d/1lUAmUsevG4OwJ94pSq8TD2CnwXAuMe2Y3ubm2ySzxTg/edit")
