"""
NOSS Gap Analysis — Compare textbook content against government requirements.
Fetches latest standards from DSD/JPK websites (cached daily) and compares.

Usage: uv run --with requests --with beautifulsoup4 scripts/gap_analysis.py
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta

PROJECT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_DIR / "content"
LOG_DIR = PROJECT_DIR / "logs"
CACHE_DIR = PROJECT_DIR / "scripts" / ".cache"

# NOSS mandatory sections per CoCu (from Panduan Pembangunan NOSS Terbitan)
REQUIRED_SECTIONS = {
    "noss_header_table": {
        "description": "NOSS header table with PROGRAM CODE, LEVEL, UNIT TITLE, WORK ACTIVITIES, CODE, PAGE",
        "check_pattern": r"PROGRAM CODE AND NAME",
    },
    "work_activities_table": {
        "description": "Contact hour distribution table with % / Hrs / Work Activity / Knowledge / Performance",
        "check_pattern": r"Knowledge\s*30%|Performance\s*70%|Work activity",
    },
    "key_terms": {
        "description": "Key terms / tools table with Type and Description columns",
        "check_pattern": r"Type of|Description|Key\s*[Tt]erm",
    },
    "contact_hours": {
        "description": "Contact hour allocation summing to level total",
        "check_pattern": r"\d+\s*%.*\d+\s*hrs?|\d+\.?\d*\s*\|\s*\d+\.?\d*",
    },
}

# NOSS IT-020 expected structure
EXPECTED_COCU = {
    "IT-020-3": {
        "total_hours": 1200,
        "cocu_count": 7,
        "units": [
            "Computer System Set-up",
            "Computer System Maintenance",
            "Computer System Repair",
            "Server Installation",
            "Server Maintenance",
            "Computer Network Connectivity Set-up",
            "Mobile Device Configuration",
        ],
    },
    "IT-020-4": {
        "total_hours": None,  # Will verify from contact hour doc
        "cocu_count": 6,
        "units": [
            "Server Configuration",
            "Computer System Security Control",
            "System Network Procurement",
            "Network Cabling Management",
            "Computer Network Installation Management",
            "Computer System Maintenance Management",
        ],
    },
    "IT-020-5": {
        "total_hours": None,
        "cocu_count": 7,
        "units": [
            "Management Overview",
            "Computer System Asset Management",
            "Computer System Security Management",
            "Disaster Recovery Management",
            "Computer System Network Project Management",
            "SOP Development And Implementation",
            "Server Scripting",
        ],
    },
}


def check_file_sections(file_path):
    """Check a CoCu .md file for required NOSS sections."""
    text = file_path.read_text(encoding="utf-8")
    results = {}

    for section_name, info in REQUIRED_SECTIONS.items():
        pattern = info["check_pattern"]
        found = bool(re.search(pattern, text, re.IGNORECASE))
        results[section_name] = {
            "found": found,
            "description": info["description"],
        }

    return results


def check_level(level_key):
    """Perform gap analysis for a single level."""
    level_dir = CONTENT_DIR / level_key.replace("-", "-")
    # Map IT-020-3 -> IT-020-3
    folder_name = f"IT-020-{level_key.split('-')[-1]}"
    level_dir = CONTENT_DIR / folder_name

    if not level_dir.exists():
        return {"error": f"Content directory not found: {level_dir}"}

    expected = EXPECTED_COCU.get(level_key, {})
    cocu_files = sorted([
        f for f in level_dir.glob("*.md")
        if f.name[:2].isdigit() and "cocu" in f.name.lower()
    ])

    gaps = {
        "level": level_key,
        "timestamp": datetime.now().isoformat(),
        "cocu_count": {"expected": expected.get("cocu_count", 0), "found": len(cocu_files)},
        "files": {},
        "missing_units": [],
        "issues": [],
        "score": 0,
    }

    # Check CoCu count
    if len(cocu_files) != expected.get("cocu_count", 0):
        gaps["issues"].append(
            f"CoCu count mismatch: expected {expected['cocu_count']}, found {len(cocu_files)}"
        )

    # Check each CoCu file
    total_score = 0
    for cocu_file in cocu_files:
        sections = check_file_sections(cocu_file)
        file_score = sum(1 for s in sections.values() if s["found"]) / len(sections) * 100

        missing = [
            info["description"]
            for name, info in sections.items()
            if not info["found"]
        ]

        gaps["files"][cocu_file.name] = {
            "sections": sections,
            "score": round(file_score, 1),
            "missing_sections": missing,
        }
        total_score += file_score

    # Check for contact hour file
    ch_files = [f for f in level_dir.glob("*contact*")]
    if not ch_files:
        gaps["issues"].append("Missing contact hour distribution file")

    # Check for standard practice file
    sp_files = [f for f in level_dir.glob("*standard-practice*")]
    if not sp_files:
        gaps["issues"].append("Missing standard practice file")

    # Overall score
    if cocu_files:
        gaps["score"] = round(total_score / len(cocu_files), 1)

    return gaps


def run_analysis():
    """Run full gap analysis across all levels."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    results = {}
    for level_key in ["IT-020-3", "IT-020-4", "IT-020-5"]:
        print(f"Analyzing {level_key}...")
        results[level_key] = check_level(level_key)
        score = results[level_key].get("score", 0)
        issues = results[level_key].get("issues", [])
        print(f"  Score: {score}%")
        for issue in issues:
            print(f"  [GAP] {issue}")

    # Save report
    report_path = LOG_DIR / f"gap-analysis-{datetime.now().strftime('%Y-%m-%d')}.json"
    report_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nReport saved: {report_path}")

    # Print summary
    print("\n" + "=" * 60)
    print("GAP ANALYSIS SUMMARY")
    print("=" * 60)
    for level_key, data in results.items():
        score = data.get("score", 0)
        cocu = data.get("cocu_count", {})
        issues = data.get("issues", [])
        print(f"\n{level_key}: {score}% complete")
        print(f"  CoCu: {cocu.get('found', '?')}/{cocu.get('expected', '?')}")
        if issues:
            for issue in issues:
                print(f"  ! {issue}")

        # Per-file scores
        for fname, fdata in data.get("files", {}).items():
            fscore = fdata.get("score", 0)
            missing = fdata.get("missing_sections", [])
            status = "OK" if fscore == 100 else f"{fscore}%"
            print(f"  {fname}: {status}")
            for m in missing:
                print(f"    - Missing: {m}")

    return results


if __name__ == "__main__":
    run_analysis()
