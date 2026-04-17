"""WIM Header Box Enforcer — validates and optionally fixes header boxes in all WIM documents.

Usage:
    uv run python _tools/enforcer/header_box_enforcer.py --scan [--all-subjects] [--subject SUBJECT]
    uv run python _tools/enforcer/header_box_enforcer.py --fix [--all-subjects]

Expected header format (each field on its own `**Key:** Value` line):
    **Kod WIM / WIM Code:** [NOSS]-[CU]/[DocCode]([Seq]/[Total])
    **Effective / Berkuat Kuasa:** YYYY-MM-DD
    **Subject / Subjek:** [Subject Name]
    **Level / Tahap:** [N]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SUBJECTS = {
    "Aesthetic": ("aesthetic-services", "S960-002-3:2020", "Aesthetic Services", "3"),
    "BEV": ("bev-diagnostic-rectification", "G452-010-3:2023", "BEV Diagnostic and Rectification", "3"),
    "IT-L3": ("it-computer-system", "IT-020-3:2013", "Computer System Management", "3"),
    "IT-L4": ("it-computer-system", "IT-020-4:2013", "Computer System Management", "4"),
    "IT-L5": ("it-computer-system", "IT-020-5:2013", "Computer System Management", "5"),
}

DOC_TYPES = ("KP", "KT", "KK", "KA", "PA", "PM")

REQUIRED_FIELDS = {
    "code": re.compile(r"\*\*Kod(?:\s+WIM)?(?:\s*/\s*WIM Code)?(?:\s*/\s*Code)?:\*\*\s*\S+"),
    "effective": re.compile(r"\*\*Effective(?:\s*/[^:]+)?:\*\*\s*\d{4}-\d{2}-\d{2}"),
    "subject": re.compile(r"\*\*Subject(?:\s*/[^:]+)?:\*\*\s*\S+"),
    "level": re.compile(r"\*\*Level(?:\s*/[^:]+)?:\*\*\s*\d"),
}

HEADER_SECTION_LINES = 20  # only check first N lines for header presence


def detect_doc_type(path: Path) -> str:
    stem = path.stem.upper()
    for dt in DOC_TYPES:
        if stem.startswith(dt):
            return dt
    return "UNKNOWN"


def validate_header(path: Path) -> dict[str, bool]:
    """Return dict of {field: present} for required header fields."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return {k: False for k in REQUIRED_FIELDS}
    header = "\n".join(text.splitlines()[:HEADER_SECTION_LINES])
    return {field: bool(pat.search(header)) for field, pat in REQUIRED_FIELDS.items()}


def scan_wim_files(subject_dirs: list[Path]) -> list[dict]:  # type: ignore[type-arg]
    """Scan all WIM .md files and return compliance results."""
    results = []
    for subject_dir in subject_dirs:
        for md_file in sorted(subject_dir.rglob("*.md")):
            # Skip non-WIM files (README, noss-extract, etc.)
            stem = md_file.stem.upper()
            if not any(stem.startswith(dt) for dt in DOC_TYPES):
                continue
            presence = validate_header(md_file)
            missing = [f for f, ok in presence.items() if not ok]
            results.append(
                {
                    "file": md_file.relative_to(ROOT),
                    "doc_type": detect_doc_type(md_file),
                    "missing": missing,
                    "compliant": len(missing) == 0,
                }
            )
    return results


def generate_template_snippet(doc_type: str, noss_code: str, cu: str, subject: str, level: str) -> str:
    """Return a corrected header block snippet for the given doc type."""
    code_map = {
        "KP": f"{noss_code}-{cu}/KP(X/Y)",
        "KT": f"{noss_code}-{cu}/KT(X/Y)",
        "KK": f"{noss_code}-{cu}/KK(X/Y)",
        "KA": f"{noss_code}-{cu}/KA",
        "PA": f"{noss_code}-{cu}/PA",
        "PM": f"{noss_code}-{cu}/PM",
    }
    wim_code = code_map.get(doc_type, f"{noss_code}-{cu}/{doc_type}")
    return (
        f"**Kod WIM / WIM Code:** {wim_code}\n"
        f"**Effective / Berkuat Kuasa:** 2024-01-01  <!-- verify date -->\n"
        f"**Subject / Subjek:** {subject}\n"
        f"**Level / Tahap:** {level}\n"
    )


def fix_file(path: Path, noss_code: str, subject: str, level: str) -> bool:
    """Insert missing header fields after the first heading line."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return False

    presence = validate_header(path)
    if all(presence.values()):
        return False  # already compliant

    lines = text.splitlines()
    insert_at = 1  # default after H1
    for i, line in enumerate(lines[:HEADER_SECTION_LINES]):
        if line.startswith("#"):
            insert_at = i + 1
            break

    # Infer CU from parent directory name
    cu = path.parent.name
    doc_type = detect_doc_type(path)
    snippet = generate_template_snippet(doc_type, noss_code, cu, subject, level)

    insert_block = ["\n<!-- AUTO-INSERTED HEADER — verify fields before use -->"]
    insert_block += snippet.splitlines()
    insert_block.append("")

    lines = lines[:insert_at] + insert_block + lines[insert_at:]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def print_report(results: list[dict]) -> int:  # type: ignore[type-arg]
    """Print compliance report. Returns count of non-compliant files."""
    compliant = [r for r in results if r["compliant"]]
    non_compliant = [r for r in results if not r["compliant"]]

    print(f"\n{'='*60}")
    print(f"WIM Header Box Compliance Report")
    print(f"{'='*60}")
    print(f"Total WIM files scanned: {len(results)}")
    print(f"Compliant:               {len(compliant)}")
    print(f"Non-compliant:           {len(non_compliant)}")
    print(f"{'='*60}\n")

    for r in non_compliant:
        missing_str = ", ".join(r["missing"])
        print(f"Missing: {r['file']}")
        print(f"  Doc type: {r['doc_type']} | Missing fields: {missing_str}")

    if non_compliant:
        # Show one template snippet per doc_type found in non-compliant files
        seen_types: set[str] = set()
        print(f"\n{'='*60}")
        print("Template snippets for quick correction:")
        print(f"{'='*60}")
        for r in non_compliant:
            dt = r["doc_type"]
            if dt not in seen_types:
                seen_types.add(dt)
                # Use a generic placeholder snippet (NOSS-specific values need manual update)
                snippet = generate_template_snippet(dt, "[NOSS_CODE]", "[CU]", "[Subject]", "[N]")
                print(f"\n--- {dt} template ---")
                print(snippet)
        print(f"Full templates: _reference/wim-header-template.md")

    return len(non_compliant)


def main() -> None:
    parser = argparse.ArgumentParser(description="WIM Header Box Enforcer")
    parser.add_argument("--scan", action="store_true", help="Scan and report non-compliant files")
    parser.add_argument("--fix", action="store_true", help="Auto-insert missing header fields")
    parser.add_argument("--all-subjects", action="store_true", help="Scan all subjects")
    parser.add_argument("--subject", choices=list(SUBJECTS.keys()), help="Scan a specific subject")
    args = parser.parse_args()

    if not args.scan and not args.fix:
        parser.print_help()
        sys.exit(1)

    if args.all_subjects:
        selected = list(SUBJECTS.items())
    elif args.subject:
        selected = [(args.subject, SUBJECTS[args.subject])]
    else:
        parser.error("Specify --all-subjects or --subject SUBJECT")

    all_results = []
    for label, (folder, noss_code, subject_name, level) in selected:
        subject_dir = ROOT / folder
        if not subject_dir.exists():
            print(f"WARNING: Subject folder not found: {subject_dir}", file=sys.stderr)
            continue
        results = scan_wim_files([subject_dir])
        all_results.extend(results)

        if args.fix:
            fixed = 0
            for r in results:
                if not r["compliant"]:
                    full_path = ROOT / r["file"]
                    if fix_file(full_path, noss_code, subject_name, level):
                        fixed += 1
                        print(f"Fixed: {r['file']}")
            print(f"[{label}] Fixed {fixed} files.")

    if args.scan:
        count = print_report(all_results)
        sys.exit(0 if count == 0 else 1)


if __name__ == "__main__":
    main()
