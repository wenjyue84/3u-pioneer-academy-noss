#!/usr/bin/env python3
"""WIM Format Compliance Validator — enforces Buku Panduan WIM Edisi 2020 standards."""

import argparse
import json
import re
import sys
from pathlib import Path

RULES_PATH = Path(__file__).parent / "wim_format_rules.json"
SUBJECT_DIRS = ["bev-diagnostic-rectification", "aesthetic-services", "it-computer-system"]


def load_rules() -> dict:
    with open(RULES_PATH, encoding="utf-8") as f:
        return json.load(f)


def check_file_coding(path: Path, content: str, rules: dict) -> list[dict]:
    violations: list[dict] = []
    pattern = rules["wim_code_pattern"]
    match = re.search(r"Kod WIM.*?:\*{0,2}\s*(.+?)(?:\*{0,2}\s*$|\n)", content, re.MULTILINE)
    if not match:
        violations.append({
            "type": "file_naming",
            "location": path.name,
            "suggestion": "Add WIM code header: **Kod WIM / WIM Code:** [NOSS]-C[XX]/[Type]([seq]/[total])",
        })
        return violations
    code = match.group(1).strip().strip("*").strip()
    if not re.match(pattern, code):
        violations.append({
            "type": "file_naming",
            "location": path.name,
            "suggestion": f"WIM code '{code}' does not match required format (e.g. G452-010-3:2023-C01/KP(1/3))",
        })
    return violations


def check_headings(content: str, rules: dict) -> list[dict]:
    violations: list[dict] = []
    required = rules["required_headings"]
    for section_key, patterns in required.items():
        found = any(re.search(p, content, re.MULTILINE | re.IGNORECASE) for p in patterns)
        if not found:
            label = section_key.replace("_", " ").title()
            violations.append({
                "type": "missing_section",
                "location": section_key,
                "suggestion": f"Add mandatory section: ## {label} (per Buku Panduan WIM Edisi 2020)",
            })
    return violations


def check_bilingual(content: str, rules: dict) -> list[dict]:
    violations: list[dict] = []
    words = len(content.split())
    if words == 0:
        return violations

    # Explicit EN:/BM: markers
    en_count = len(re.findall(r"\b(?:EN|English)\s*:", content, re.IGNORECASE))
    bm_count = len(re.findall(r"\b(?:BM|Melayu|Bahasa Malaysia)\s*:", content, re.IGNORECASE))
    explicit_pairs = min(en_count, bm_count)

    # Bilingual headings: "## Term / Terma" or "## Term (Terma)"
    slash_headings = len(re.findall(r"^#{1,3}\s+.+/.+", content, re.MULTILINE))
    paren_headings = len(re.findall(r"^#{1,3}\s+.+\(.+\)", content, re.MULTILINE))

    # Inline parenthetical bilingual terms (e.g. "voltage (voltan)")
    inline_parens = len(re.findall(r"\b[A-Za-z]{3,}\s+\([A-Za-z]{3,}[^)]*\)", content))

    total_pairs = explicit_pairs + slash_headings + paren_headings + inline_parens
    pairs_per_500 = (total_pairs / words) * 500 if words > 0 else 0

    threshold = rules["bilingual_density"]["min_pairs_per_500_words"]
    if pairs_per_500 < threshold:
        violations.append({
            "type": "bilingual_terms",
            "location": "document",
            "suggestion": (
                f"Found {pairs_per_500:.1f} bilingual pairs per 500 words "
                f"(min {threshold}). Add EN/BM term pairs using EN:/BM: markers "
                "or 'Term (Terma)' / 'Term / Terma' format in headings."
            ),
        })
    return violations


def validate_file(path: Path, rules: dict) -> dict:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as exc:
        return {
            "file_path": str(path),
            "compliance_score": 0,
            "violation_count": 1,
            "violations": [{"type": "file_naming", "location": str(path), "suggestion": f"Cannot read file: {exc}"}],
        }

    violations: list[dict] = []
    score = 100

    coding_violations = check_file_coding(path, content, rules)
    violations.extend(coding_violations)
    if coding_violations:
        score -= rules["file_coding_weight"]

    heading_violations = check_headings(content, rules)
    violations.extend(heading_violations)
    weights = rules["heading_weights"]
    for v in heading_violations:
        score -= weights.get(v["location"], 12)

    bilingual_violations = check_bilingual(content, rules)
    violations.extend(bilingual_violations)
    if bilingual_violations:
        score -= rules["bilingual_density_weight"]

    return {
        "file_path": str(path),
        "compliance_score": max(0, score),
        "violation_count": len(violations),
        "violations": violations,
    }


def scan_directory(dir_path: Path, rules: dict, verbose: bool = False) -> list[dict]:
    results: list[dict] = []
    for md_file in sorted(dir_path.rglob("*.md")):
        result = validate_file(md_file, rules)
        results.append(result)
        if verbose:
            status = "PASS" if result["compliance_score"] >= 95 else "FAIL"
            print(f"  [{status}] {md_file} — score:{result['compliance_score']} violations:{result['violation_count']}")
    return results


def generate_summary(all_results: list[dict]) -> dict:
    counts: dict[str, int] = {"file_naming": 0, "missing_section": 0, "table_format": 0, "bilingual_terms": 0}
    for r in all_results:
        for v in r["violations"]:
            vtype = v.get("type", "")
            if vtype in counts:
                counts[vtype] += 1

    total = len(all_results)
    compliant = sum(1 for r in all_results if r["compliance_score"] >= 95)
    at_risk = sum(1 for r in all_results if 60 <= r["compliance_score"] < 95)
    non_compliant = sum(1 for r in all_results if r["compliance_score"] < 60)

    return {
        "total_files_scanned": total,
        "compliant_files": compliant,
        "at_risk_files": at_risk,
        "non_compliant_files": non_compliant,
        "violation_counts_by_type": counts,
        "files": all_results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="WIM Format Compliance Validator (Buku Panduan WIM Edisi 2020)")
    parser.add_argument("--path", type=Path, help="Directory to scan")
    parser.add_argument("--output", type=Path, default=Path("_agents/wim_compliance_report.json"))
    parser.add_argument("--check-all", action="store_true", help="Scan all 3 WIM subject directories")
    parser.add_argument("--verbose", action="store_true", help="Print per-file results to stdout")
    args = parser.parse_args()

    rules = load_rules()
    root = Path(__file__).parent.parent

    if args.check_all:
        scan_dirs = [root / d for d in SUBJECT_DIRS if (root / d).exists()]
    elif args.path:
        scan_dirs = [args.path]
    else:
        print("Error: specify --path <dir> or --check-all", file=sys.stderr)
        sys.exit(2)

    if args.verbose:
        print(f"Scanning {len(scan_dirs)} subject director(ies)...")

    all_results: list[dict] = []
    parent_dirs: set[str] = set()

    for d in scan_dirs:
        if args.verbose:
            print(f"\n[DIR] {d}")
        results = scan_directory(d, rules, args.verbose)
        all_results.extend(results)
        for r in results:
            parent_dirs.add(str(Path(r["file_path"]).parent))

    report = generate_summary(all_results)

    output_path = args.output
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    if args.verbose:
        s = report
        print(
            f"\nReport → {output_path}\n"
            f"Total: {s['total_files_scanned']} files | "
            f"Compliant(≥95%): {s['compliant_files']} | "
            f"At-risk(60-94%): {s['at_risk_files']} | "
            f"Non-compliant(<60%): {s['non_compliant_files']}"
        )

    min_dirs = rules.get("min_directories_required", 5)
    non_compliant_list = [r for r in all_results if r["compliance_score"] < 95]
    if non_compliant_list or len(parent_dirs) < min_dirs:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
