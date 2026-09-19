#!/usr/bin/env python3
"""Enforce the ADI Pekerjaan Tahap->question-format rule on Penilaian Pengetahuan files.

Source of the rule (verbatim, verified in this repo):
  - Panduan ADI Pekerjaan 552025, Jadual 8 (p.22):
      Tahap 3 (SKM)      -> objektif, 20 MCQ (4 pilihan), 30 minit
      Tahap 4/5 (DKM)    -> subjektif, 2 soalan/CU (1 Struktur + 1 Esei), 1 jam, lulus 60%
  - officer template `3.2 Format Soalan PENILAIAN PENGETAHUAN.xlsx`,
      sheet literally named `JSU STD THP 4-5 (SUBJEKTIF)`.
  - Buku Panduan Pembangunan Soalan Edisi 2024 SS5.5.6 (p.32) & Jadual 15:
      soalan struktur = 3-4 sub-soalan (a-d), covering aras R, S and T;
      struktur+esei together must cover ALL Work Activities (WA);
      esei = aras Tinggi.
  Cited in: preschool-teaching/07-soalan-penilaian-pengetahuan/00-format-subjektif-tahap4.md
  and preschool-teaching/README.md (comparison table).

  IMPORTANT: this rule is verified ONLY for the ADI Pekerjaan pathway (video-film-editing,
  preschool-teaching). It is NOT confirmed as a general JPK/WIM rule for other subjects in
  this repo (wiki/07-jpk-format-spec.md has no mention of MCQ/Struktur/Esei at all) -- do not
  run this checker against ordinary WIM subjects (Tuinalogy, Aesthetic, BEV, IT, AI-DM, etc.).

This script does NOT re-check MCQ writing-style rules (punctuation/italics/etc) -- that is
`.claude/skills/soalan-format/scripts/check_format.py`. This script only checks that the
FORMAT (MCQ vs Struktur+Esei) and its structural requirements match what the file's own Tahap
claims to be.

Usage:
    uv run check_tahap_format.py <file-or-dir> [<file-or-dir> ...] [--json]
"""
import argparse
import json
import re
import sys
from pathlib import Path


def find_md_files(paths):
    files = []
    for p in paths:
        p = Path(p)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            files.append(p)
    return files


def get_field(text, label):
    m = re.search(r"\|\s*" + re.escape(label) + r"\s*\|\s*(.+?)\s*\|", text)
    return m.group(1).strip() if m else None


def infer_tahap(text, explicit_tahap_field):
    if explicit_tahap_field:
        m = re.search(r"\d", explicit_tahap_field)
        if m:
            return int(m.group(0))
    # fall back to the NOSS code suffix, e.g. "...-4:2025-C02" or "...-3:2012"
    m = re.search(r"-(\d):\d{4}", text)
    if m:
        return int(m.group(1))
    return None


def check_file(path):
    text = path.read_text(encoding="utf-8")
    findings = []

    kod_cu = get_field(text, "NAMA & KOD CU")
    tahap_field = get_field(text, "TAHAP")
    jumlah_soalan = get_field(text, "JUMLAH SOALAN")
    tempoh = get_field(text, "TEMPOH PENILAIAN")
    markah_lulus = get_field(text, "MARKAH LULUS")

    if not kod_cu and not jumlah_soalan:
        return findings  # not a Penilaian Pengetahuan header file, skip silently

    tahap = infer_tahap(text, tahap_field)
    if tahap is None:
        findings.append(("WARN", "tahap_unknown",
                          "Could not determine Tahap from TAHAP field or NOSS code suffix"))
        return findings

    is_mcq_body = bool(re.search(r"BAHAGIAN A\s*—\s*SOALAN OBJEKTIF", text))
    is_subjektif_body = bool(re.search(r"BAHAGIAN A\s*—\s*SOALAN STRUKTUR", text)) and \
                         bool(re.search(r"BAHAGIAN B\s*—\s*SOALAN ESEI", text))

    if tahap == 3:
        # Rule: Tahap 3 -> MCQ, 20 soalan, 4 pilihan, 30 minit
        # The header table layout varies across files in this project (some have a
        # JUMLAH SOALAN row, others use a candidate cover-page layout without one) -- the
        # BODY (BAHAGIAN A - SOALAN OBJEKTIF + A-D options) is the authoritative check;
        # a missing header field alone is only a WARN, not proof the format is wrong.
        if jumlah_soalan and "MCQ" not in jumlah_soalan.upper():
            findings.append(("ERROR", "tahap3_not_mcq",
                              f"Tahap 3 but JUMLAH SOALAN does not say MCQ: {jumlah_soalan!r}"))
        elif jumlah_soalan and "4 PILIHAN" not in jumlah_soalan.upper():
            findings.append(("ERROR", "tahap3_not_4_choice",
                              f"Tahap 3 MCQ should state 4 pilihan: {jumlah_soalan!r}"))
        elif not jumlah_soalan:
            findings.append(("WARN", "tahap3_missing_header_field",
                              "No JUMLAH SOALAN field in header table — relying on body to confirm MCQ format"))
        if tempoh and "30 MINIT" not in tempoh.upper():
            findings.append(("WARN", "tahap3_duration",
                              f"Tahap 3 usually 30 minit per Jadual 8, found: {tempoh!r}"))
        if not is_mcq_body:
            findings.append(("ERROR", "tahap3_body_not_mcq",
                              "Tahap 3 file has no 'BAHAGIAN A — SOALAN OBJEKTIF' section"))
        if is_subjektif_body:
            findings.append(("ERROR", "tahap3_has_subjektif_body",
                              "Tahap 3 file unexpectedly has Struktur/Esei sections"))

    elif tahap in (4, 5):
        # Rule: Tahap 4/5 (DKM) -> Subjektif, 1 Struktur + 1 Esei, 1 jam, lulus 60%
        if not jumlah_soalan or "STRUKTUR" not in jumlah_soalan.upper() or "ESEI" not in jumlah_soalan.upper():
            findings.append(("ERROR", "tahap45_not_subjektif",
                              f"Tahap {tahap} (DKM) but JUMLAH SOALAN is not Struktur+Esei: {jumlah_soalan!r}"))
        if tempoh and "1 JAM" not in tempoh.upper():
            findings.append(("WARN", "tahap45_duration",
                              f"Tahap 4/5 usually 1 jam per Jadual 8, found: {tempoh!r}"))
        if markah_lulus and "60" not in markah_lulus:
            findings.append(("WARN", "tahap45_pass_mark",
                              f"Tahap 4/5 pass mark usually 60%, found: {markah_lulus!r}"))
        if not is_subjektif_body:
            findings.append(("ERROR", "tahap45_body_not_subjektif",
                              "Tahap 4/5 file missing 'BAHAGIAN A — SOALAN STRUKTUR' and/or "
                              "'BAHAGIAN B — SOALAN ESEI' sections"))
        if is_mcq_body:
            findings.append(("ERROR", "tahap45_has_mcq_body",
                              "Tahap 4/5 file unexpectedly has an MCQ (SOALAN OBJEKTIF) section"))

        # Buku Panduan 2024 SS5.5.6: struktur = 3-4 sub-soalan (a-d), covering R/S/T.
        # Scope to the Struktur section only (BAHAGIAN A up to BAHAGIAN B) so a marking
        # scheme / jawapan cadangan block re-using a./b./c./d. labels isn't double-counted.
        struktur_section_match = re.search(
            r"BAHAGIAN A\s*—\s*SOALAN STRUKTUR(.*?)(?=BAHAGIAN B\s*—\s*SOALAN ESEI|\Z)",
            text, re.DOTALL)
        struktur_section = struktur_section_match.group(1) if struktur_section_match else ""
        struktur_subs = re.findall(r"^([a-d])\.\s", struktur_section, re.MULTILINE)
        if struktur_subs and not (3 <= len(struktur_subs) <= 4):
            findings.append(("WARN", "struktur_sub_count",
                              f"Struktur has {len(struktur_subs)} sub-soalan (a-d); Jadual 15 expects 3-4"))

        aras_tags = re.findall(r"—\s*WA\d+.*?·\s*(Rendah|Sederhana|Tinggi|Rendah/Sederhana|Sederhana/Tinggi)",
                                text)
        if aras_tags and not any("Rendah" in a for a in aras_tags):
            findings.append(("WARN", "struktur_missing_rendah",
                              "No sub-soalan tagged aras Rendah (R) found — Struktur should span R/S/T"))
        if aras_tags and not any("Tinggi" in a for a in aras_tags):
            findings.append(("WARN", "struktur_missing_tinggi",
                              "No sub-soalan tagged aras Tinggi (T) found — Struktur should span R/S/T"))

        esei_block = re.search(r"BAHAGIAN B.*", text, re.DOTALL)
        if esei_block:
            esei_header = re.search(r"\*\*Esei\s*\d*\*\*[^\n]*", esei_block.group(0))
            if esei_header and "Tinggi" not in esei_header.group(0):
                findings.append(("ERROR", "esei_not_tinggi",
                                  f"Esei must be aras Tinggi per SS5.5.6: {esei_header.group(0)[:80]}"))

    else:
        findings.append(("WARN", "tahap_unhandled",
                          f"Tahap {tahap} has no known rule in this checker (only 3, 4, 5 handled)"))

    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    files = find_md_files(args.paths)
    report = {}
    total_errors = 0
    total_warns = 0
    for f in files:
        findings = check_file(f)
        if not findings:
            continue
        report[str(f)] = findings
        total_errors += sum(1 for lvl, *_ in findings if lvl == "ERROR")
        total_warns += sum(1 for lvl, *_ in findings if lvl == "WARN")

    if args.json:
        print(json.dumps(
            {str(f): [{"level": lvl, "rule": rule, "msg": msg} for lvl, rule, msg in fnds]
             for f, fnds in report.items()},
            ensure_ascii=False, indent=2))
    else:
        for f, findings in report.items():
            print(f"\n== {f} ==")
            for lvl, rule, msg in findings:
                print(f"  [{lvl}] {rule}: {msg}")
        print(f"\nTOTAL: {total_errors} ERROR, {total_warns} WARN across {len(report)} file(s)")

    sys.exit(1 if total_errors else 0)


if __name__ == "__main__":
    main()
