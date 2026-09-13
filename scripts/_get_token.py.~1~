"""Debug: inspect credential blob from Windows Credential Manager."""
import ctypes
import ctypes.wintypes
import json
import sys

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

PCREDENTIAL = ctypes.POINTER(CREDENTIAL)
advapi32 = ctypes.windll.advapi32

target = "keyring:gogcli:token:default:wenjyue@gmail.com"
cred_ptr = PCREDENTIAL()
ok = advapi32.CredReadW(target, CRED_TYPE_GENERIC, 0, ctypes.byref(cred_ptr))

if not ok:
    print(f"CredReadW failed, error: {ctypes.get_last_error()}")
    sys.exit(1)

cred = cred_ptr.contents
blob_size = cred.CredentialBlobSize
print(f"Blob size: {blob_size}")
print(f"UserName: {cred.UserName}")

blob = ctypes.string_at(cred.CredentialBlob, blob_size)
print(f"Raw blob (first 100 bytes): {blob[:100]}")

# Try different decodings
for enc in ["utf-8", "utf-16-le", "ascii", "latin-1"]:
    try:
        text = blob.decode(enc)
        print(f"\n{enc} decode (first 200 chars): {text[:200]}")
        # Try JSON parse
        try:
            data = json.loads(text)
            print(f"\nJSON keys: {list(data.keys())}")
            if "access_token" in data:
                print(f"access_token length: {len(data['access_token'])}")
            if "refresh_token" in data:
                print(f"refresh_token: present")
        except json.JSONDecodeError:
            pass
    except UnicodeDecodeError:
        print(f"{enc}: decode failed")

advapi32.CredFree(cred_ptr)
