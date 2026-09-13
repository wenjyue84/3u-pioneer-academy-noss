#!/usr/bin/env python3
"""Apply JPK envelope to WIM markdown files across NOSS subjects.

Usage:
    python enhance_wim_jpk.py <subject> [--cu CUxx] [--dry-run]

Subjects: tuinalogy | aesthetic | bev | it | it4 | it5 | multimedia_l3 | multimedia_l4 | all
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
PROJECT_ROOT = SKILL_DIR.parent.parent.parent

ENV_START = "<!-- JPK_ENVELOPE_v1 -->"
ENV_END = "<!-- /JPK_ENVELOPE_v1 -->"

DOC_TYPE_LABELS: dict[str, tuple[str, str, str]] = {
    "PM-teori": ("PELAN MENGAJAR \u2013 TEORI", "KUNING", "Yellow"),
    "PM-amali": ("PELAN MENGAJAR \u2013 AMALI", "KUNING", "Yellow"),
    "KP":       ("KERTAS PENERANGAN",               "PUTIH",        "White"),
    "KT":       ("KERTAS TUGASAN",                   "MERAH JAMBU",  "Pink"),
    "KK":       ("KERTAS KERJA",                     "BIRU",         "Blue"),
    "KA":       ("KERTAS PENILAIAN PENGETAHUAN",     "MERAH JAMBU",  "Pink"),
    "PA":       ("KERTAS PENILAIAN PRESTASI",        "BIRU MUDA",    "Light Blue"),
}

JPK_ADDRESS_LINES = [
    "**JABATAN PEMBANGUNAN KEMAHIRAN (JPK)**",
    "TINGKAT 7-8, BLOK D4, KOMPLEKS D,",
    "PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,",
    "62530 PUTRAJAYA",
]

SKIP_FILENAMES = {
    "00-cocu.md",
    "00-noss-extract.md",
    "00-README.md",
    "01-jpw-distribution.md",
    "00-aesthetic-terminology.md",
    "00-source-summary.md",
    "lab-activity-mapping.json",
}

LEGACY_META_PREFIXES = (
    "**WIM \u7f16\u7801\uff1a**",   # Chinese colon
    "**NOSS\uff1a**",
    "**CU\uff1a**",
    "**\u5bf9\u5e94\u5de5\u4f5c\u6d3b\u52a8\uff1a**",
    "**\u7eb8\u5f20\u989c\u8272\uff1a**",
    "**\u65f6\u6570\uff1a**",
    "**\u6700\u540e\u66f4\u65b0\uff1a**",
    "**WIM Code:**",
    "**Paper:**",
    "**Paper Color:**",
    "**Hours:**",
    "**Last Updated:**",
)


@dataclass
class DocInfo:
    kind: str        # PM-teori, PM-amali, KP, KT, KK, KA, PA
    seq: int | None  # None if not applicable
    cu: str          # C01, L3-C02, etc.
    filename: str


def classify(filename: str) -> DocInfo | None:
    """Classify a WIM filename.

    Accepts both bare codes (`KA.md`, `PM-teori.md`, `KP-01.md`) and
    descriptive variants (`KA-centre-management.md`, `PM-teori-sports-tuina.md`,
    `KP-01-eight-core-techniques.md`). The optional suffix is ignored.
    """
    stem = filename[:-3] if filename.endswith(".md") else filename
    if filename in SKIP_FILENAMES:
        return None
    if stem == "PM-teori" or stem.startswith("PM-teori-"):
        return DocInfo("PM-teori", None, "", filename)
    if stem == "PM-amali" or stem.startswith("PM-amali-"):
        return DocInfo("PM-amali", None, "", filename)
    if stem == "KA" or stem.startswith("KA-"):
        return DocInfo("KA", None, "", filename)
    if stem == "PA" or stem.startswith("PA-"):
        return DocInfo("PA", None, "", filename)
    m = re.match(r"^(KP|KT|KK)-(\d+)(?:-|$)", stem)
    if m:
        return DocInfo(m.group(1), int(m.group(2)), "", filename)
    return None


def count_total_for_type(cu_dir: Path, kind: str) -> int:
    if kind not in {"KP", "KT", "KK"}:
        return 1
    return len(list(cu_dir.glob(f"{kind}-*.md")))


def wim_code(noss: str, cu: str, kind: str, seq: int | None, total: int) -> str:
    base = f"{noss}-{cu}"
    if kind == "PM-teori":
        return f"{base}/PM(TEORI)"
    if kind == "PM-amali":
        return f"{base}/PM(AMALI)"
    if kind == "KA":
        return f"{base}/KA"
    if kind == "PA":
        return f"{base}/PA"
    return f"{base}/{kind}({seq}/{total})"


def logo_relpath_from(cu_dir: Path, subject_root: Path) -> str:
    # cu_dir is subject_root/CU; asset is subject_root/_assets/logos/jpk-logo.png
    # from CU dir that's ../_assets/logos/jpk-logo.png
    return "../_assets/logos/jpk-logo.png"


def work_activity_list(meta: dict) -> str:
    items = meta.get("work_activities", [])
    parts = [f"{i+1}. {wa}" for i, wa in enumerate(items)]
    return "<br>".join(parts)


H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def extract_existing_title_and_purpose(body: str, fallback_stem: str) -> tuple[str, str]:
    # Title: first H1 in body, else filename stem
    m = H1_RE.search(body)
    title = m.group(1).strip() if m else fallback_stem
    # Purpose: first non-heading, non-empty paragraph after H1 (or top)
    purpose = ""
    lines = body.splitlines()
    started = False
    buf: list[str] = []
    for ln in lines:
        if not started:
            if ln.startswith("# "):
                started = True
            continue
        stripped = ln.strip()
        if not stripped:
            if buf:
                break
            continue
        if stripped.startswith(("#", "![", "|", "---", "**WIM", "**NOSS", "**CU", "**")):
            if buf:
                break
            continue
        if re.match(r"\d+[.)]", stripped) or stripped.startswith(("-", "*")):
            if buf:
                break
            continue
        buf.append(stripped)
        if len(" ".join(buf)) > 220:
            break
    purpose = " ".join(buf).strip()
    if not purpose:
        purpose = f"Kertas rujukan untuk {title}."
    return title, purpose


NATIVE_H1_RE = re.compile(r"^#\s+(KERTAS|PELAN MENGAJAR|PENILAIAN)\b", re.IGNORECASE)
TAJUK_RE = re.compile(r"^##\s*Tajuk\b.*?:\s*(.+?)\s*$", re.IGNORECASE)


def strip_native_header_and_get_title(body: str, fallback: str) -> tuple[str, str] | None:
    """Remove the spiral-generated native header block and return (title, body).

    The native header is a redundant simpler version of the JPK envelope:
        # KERTAS PENERANGAN (Information Sheet)
        **Kod:** ... / **Kertas Warna:** ...
        ---
        | bilingual metadata table |
        ---
        ## Tajuk / Title: <real title>      (KP/KK; absent on KA/PA)
    The JPK envelope replaces this block, so it is stripped to avoid a duplicate
    header (matching Jennifer's single-header layout). Returns None when no native
    header is present (caller then keeps the body unchanged).
    """
    lines = body.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or not NATIVE_H1_RE.match(lines[i].strip()):
        return None
    title = fallback
    content_start: int | None = None
    j = i
    while j < len(lines):
        st = lines[j].strip()
        m = TAJUK_RE.match(st)
        if m:
            title = m.group(1).strip()
            k = j + 1
            while k < len(lines) and lines[k].strip() in ("", "---"):
                k += 1
            content_start = k
            break
        if j > i and st.startswith("## "):
            content_start = j
            break
        j += 1
    if content_start is None:
        # Header with no detectable content boundary — do not risk dropping body.
        return None
    new_body = "\n".join(lines[content_start:]).lstrip("\n")
    return title, new_body


def strip_legacy_metadata(body: str) -> str:
    # Remove existing envelope if present
    if ENV_START in body:
        end_idx = body.find(ENV_END)
        if end_idx != -1:
            body = body[end_idx + len(ENV_END):].lstrip("\n")
        else:
            # malformed; strip until first blank line after start
            start_idx = body.find(ENV_START)
            body = body[:start_idx] + body[start_idx + len(ENV_START):]
    # Strip leading legacy metadata lines following first H1
    lines = body.splitlines()
    out: list[str] = []
    skip = False
    past_first_h1 = False
    for ln in lines:
        if not past_first_h1:
            out.append(ln)
            if ln.startswith("# "):
                past_first_h1 = True
            continue
        stripped = ln.strip()
        if any(stripped.startswith(p) for p in LEGACY_META_PREFIXES):
            skip = True
            continue
        if skip and stripped == "":
            continue
        if skip and stripped == "---":
            skip = False
            continue
        skip = False
        out.append(ln)
    return "\n".join(out)


def build_envelope(
    doc: DocInfo,
    cu: str,
    subject_meta: dict,
    total: int,
    title: str,
    purpose: str,
) -> str:
    label, color_bm, color_en = DOC_TYPE_LABELS[doc.kind]
    noss = subject_meta["noss_code"]
    program_bm = subject_meta.get("program_bm", subject_meta["program_en"])
    level = subject_meta["level"]
    cu_meta = subject_meta["cus"][cu]
    cu_title_en = cu_meta["title_en"]
    wa_str = work_activity_list(cu_meta)
    # The folder key may carry a disambiguating level prefix (e.g. "L3-C01"),
    # but the official JPK document code omits it because the NOSS code already
    # encodes the level (IT-020-3:2013). Strip the prefix for the code segment.
    prefix = subject_meta.get("cu_prefix", "")
    code_cu = cu[len(prefix):] if prefix and cu.startswith(prefix) else cu
    code = wim_code(noss, code_cu, doc.kind, doc.seq, total)

    lines: list[str] = []
    lines.append(ENV_START)
    # Logo LEFT, address RIGHT — matches JPK PDF layout via HTML table
    # (markdown native tables require a header row; HTML table renders cleanly
    # in GitHub, VS Code, and the wim_md_to_docx.py DOCX builder.)
    lines.append('<table border="0" cellspacing="0" cellpadding="8" width="100%">')
    lines.append("<tr>")
    lines.append('<td width="130" valign="top"><img src="../_assets/logos/jpk-logo.png" alt="JPK Logo" width="110"></td>')
    lines.append('<td valign="middle">')
    lines.append("<b>JABATAN PEMBANGUNAN KEMAHIRAN (JPK)</b><br>")
    lines.append("TINGKAT 7-8, BLOK D4, KOMPLEKS D,<br>")
    lines.append("PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,<br>")
    lines.append("62530 PUTRAJAYA")
    lines.append("</td>")
    lines.append("</tr>")
    lines.append("</table>")
    lines.append("")
    lines.append(f"## {label}")
    lines.append("")
    lines.append("| Medan | Nilai |")
    lines.append("| --- | --- |")
    lines.append(f"| KOD DAN NAMA PROGRAM | {noss} {program_bm} |")
    lines.append(f"| TAHAP | {level} |")
    lines.append(f"| KOD DAN TAJUK UNIT KOMPETENSI | {noss}-{code_cu} {cu_title_en} |")
    lines.append(f"| NO. DAN PERNYATAAN AKTIVITI KERJA | {wa_str} |")
    lines.append(f"| NO. KOD | {code} |")
    lines.append("| Muka Surat | 1/1 |")
    lines.append(f"| WARNA KERTAS | {color_bm} ({color_en}) |")
    lines.append("")
    lines.append(f"**TAJUK:** {title}")
    lines.append("")
    lines.append(f"**TUJUAN:** {purpose}")
    if doc.kind in {"PM-teori", "PM-amali"}:
        place = "BILIK KULIAH" if doc.kind == "PM-teori" else "BILIK AMALI / MAKMAL"
        lines.append("")
        lines.append(f"**TEMPAT:** {place}")
        lines.append("")
        lines.append("**TEMPOH:** Rujuk JPW/RK.")
        lines.append("")
        lines.append("**TUJUAN PENGAJARAN:** Pada akhir sesi pengajaran, pelatih akan dapat menguasai pengetahuan/kemahiran berkaitan aktiviti kerja CU ini.")
        lines.append("")
        lines.append("**ALAT BANTUAN MENGAJAR:** Papan putih, projektor, slaid pengajaran, bahan tunjuk-cara.")
    elif doc.kind in {"KT", "KK"}:
        lines.append("")
        lines.append("**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.")
    elif doc.kind in {"KA", "PA"}:
        lines.append("")
        lines.append("**ARAHAN:** Jawab semua soalan / laksanakan semua tugas penilaian. Penilaian ini adalah sebahagian daripada Penilaian Akhir CU.")
    lines.append("")
    lines.append(ENV_END)
    lines.append("")
    return "\n".join(lines)


def apply_envelope(
    file_path: Path,
    cu_dir: Path,
    subject_meta: dict,
    cu: str,
) -> tuple[bool, str]:
    doc = classify(file_path.name)
    if doc is None:
        return False, "skip-classify"
    total = count_total_for_type(cu_dir, doc.kind)
    body = file_path.read_text(encoding="utf-8")
    # Always strip existing envelope + legacy meta before rebuilding
    cleaned = strip_legacy_metadata(body)
    # Strip the redundant native header block (the JPK envelope replaces it) and
    # recover the real document title from its "Tajuk / Title:" line. For docs
    # without a Tajuk line (KA/PA/PM), fall back to the CU title rather than the
    # raw filename stem.
    cu_meta_fallback = subject_meta["cus"][cu]
    fallback_title = cu_meta_fallback.get("title_en", file_path.stem).title()
    stripped = strip_native_header_and_get_title(cleaned, fallback_title)
    if stripped is not None:
        title, cleaned = stripped
        _, purpose = extract_existing_title_and_purpose(body, file_path.stem)
    else:
        title, purpose = extract_existing_title_and_purpose(cleaned, file_path.stem)
    envelope = build_envelope(doc, cu, subject_meta, total, title, purpose)
    new_body = envelope + cleaned.lstrip("\n")
    if new_body == body:
        return False, "no-change"
    return True, new_body


def process_subject(
    key: str,
    subjects: dict,
    only_cu: str | None,
    dry_run: bool,
) -> tuple[int, int]:
    meta = subjects[key]
    subject_root = PROJECT_ROOT / meta["root"]
    if not subject_root.exists():
        print(f"[{key}] SKIP: {subject_root} does not exist")
        return 0, 0
    changed = 0
    skipped = 0
    cu_keys = list(meta["cus"].keys())
    for cu in cu_keys:
        if only_cu and only_cu != cu:
            continue
        cu_dir = subject_root / cu
        if not cu_dir.exists():
            print(f"[{key}] SKIP CU {cu}: dir missing")
            continue
        md_files = sorted(cu_dir.glob("*.md"))
        for md in md_files:
            if md.name in SKIP_FILENAMES:
                skipped += 1
                continue
            changed_flag, result = apply_envelope(md, cu_dir, meta, cu)
            if not changed_flag:
                skipped += 1
                continue
            if dry_run:
                preview = md.with_suffix(".md.preview")
                preview.write_text(result, encoding="utf-8")
                print(f"[{key}/{cu}] DRY {md.name} -> {preview.name}")
            else:
                md.write_text(result, encoding="utf-8")
                print(f"[{key}/{cu}] WROTE {md.name}")
            changed += 1
    return changed, skipped


def main() -> None:
    subjects = json.loads((SKILL_DIR / "data" / "subjects.json").read_text(encoding="utf-8"))
    valid_choices = list(subjects.keys()) + ["all"]
    ap = argparse.ArgumentParser()
    ap.add_argument("subject", choices=valid_choices)
    ap.add_argument("--cu", default=None, help="Only process one CU (e.g., C01)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    keys = list(subjects.keys()) if args.subject == "all" else [args.subject]

    total_changed = 0
    total_skipped = 0
    for key in keys:
        c, s = process_subject(key, subjects, args.cu, args.dry_run)
        total_changed += c
        total_skipped += s
        print(f"[{key}] summary: changed={c} skipped={s}")
    print(f"TOTAL changed={total_changed} skipped={total_skipped} dry_run={args.dry_run}")


if __name__ == "__main__":
    main()
