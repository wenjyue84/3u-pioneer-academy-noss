"""KK Safety Checkpoint Validator — audits procedural steps for missing safety checkpoints.

Usage:
    uv run python validators/kk_safety_checkpoint_validator.py --root . --output report.html
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Required safety checkpoints per subject (keyword patterns)
REQUIRED_CHECKPOINTS: dict[str, dict[str, list[str]]] = {
    "bev": {
        "ppe_verification": ["PPE", "insulated gloves", "dielectric", "safety glasses", "helmet", "pelindung"],
        "insulation_test": ["insulation test", "air inflation", "megger", "insulation resistance", "ujian penebat"],
        "ground_continuity": ["ground continuity", "ground check", "earth continuity", "bumi", "pembumian", "grounding"],
        "hv_isolation": ["HV isolation", "high voltage off", "service disconnect", "isolation plug", "unplug HV"],
        "lockout_tagout": ["lockout", "tagout", "LOTO", "lock out", "kunci keluar"],
    },
    "aesthetic": {
        "hygiene": ["wash hands", "sanitise", "sanitize", "disinfect", "gloves", "PPE", "kebersihan", "basuh tangan"],
        "contraindication_screening": ["contraindication", "contraindicated", "screening", "medical history",
                                       "kontraindikasi", "saringan"],
        "client_comfort": ["client comfort", "client consent", "informed consent", "comfort", "kenyamanan",
                           "keselesaan klien", "persetujuan"],
        "patch_test": ["patch test", "sensitivity test", "ujian tampalan", "ujian sensitiviti", "allergy test"],
        "equipment_sterilisation": ["sterilise", "sterilize", "autoclave", "disinfect equipment", "pensterilan"],
    },
}

# Risk level for each missing checkpoint
SAFETY_RISK_MAP: dict[str, str] = {
    "ppe_verification": "CRITICAL",
    "insulation_test": "CRITICAL",
    "ground_continuity": "HIGH",
    "hv_isolation": "CRITICAL",
    "lockout_tagout": "HIGH",
    "hygiene": "HIGH",
    "contraindication_screening": "HIGH",
    "client_comfort": "MEDIUM",
    "patch_test": "HIGH",
    "equipment_sterilisation": "HIGH",
}

NOSS_REFS: dict[str, str] = {
    "ppe_verification": "G452-010-3:2023 §4.1 — PPE mandatory before HV contact",
    "insulation_test": "G452-010-3:2023 §4.2 — Insulation test before energising",
    "ground_continuity": "G452-010-3:2023 §4.3 — Ground continuity verification required",
    "hv_isolation": "G452-010-3:2023 §4.4 — HV isolation mandatory before work",
    "lockout_tagout": "G452-010-3:2023 §4.5 — LOTO procedure required",
    "hygiene": "S960-002-3:2020 §3.1 — Hand hygiene and PPE before client contact",
    "contraindication_screening": "S960-002-3:2020 §3.2 — Screen contraindications before treatment",
    "client_comfort": "S960-002-3:2020 §3.3 — Obtain informed consent and confirm comfort",
    "patch_test": "S960-002-3:2020 §3.4 — Patch test required for chemical treatments",
    "equipment_sterilisation": "S960-002-3:2020 §3.5 — Equipment sterilisation between clients",
}


def detect_subject(path: Path) -> str:
    """Infer subject from file path."""
    parts = str(path).lower()
    if "bev" in parts or "g452" in parts:
        return "bev"
    if "aesthetic" in parts or "s960" in parts:
        return "aesthetic"
    return "unknown"


def scan_kk_steps(path: Path) -> list[dict[str, str]]:
    """Extract procedural steps from a KK markdown file."""
    content = path.read_text(encoding="utf-8")
    # Split by step headings
    step_blocks = re.split(r"(?=^###\s+Step\s+\d+)", content, flags=re.M)
    steps: list[dict[str, str]] = []
    for block in step_blocks:
        m = re.match(r"^###\s+(Step\s+\d+[^\\n]*)", block)
        if m:
            steps.append({"title": m.group(1).strip(), "text": block})
    return steps


def audit_kk_file(path: Path, subject: str | None = None) -> list[dict[str, str]]:
    """Check KK file for missing safety checkpoints; return list of gap dicts."""
    if subject is None:
        subject = detect_subject(path)
    if subject not in REQUIRED_CHECKPOINTS:
        return []

    full_text = path.read_text(encoding="utf-8")
    checkpoints = REQUIRED_CHECKPOINTS[subject]
    gaps: list[dict[str, str]] = []

    for cp_name, keywords in checkpoints.items():
        # Check if any keyword appears anywhere in the file
        found = any(re.search(kw, full_text, re.I) for kw in keywords)
        if not found:
            gaps.append({
                "checkpoint": cp_name,
                "risk": SAFETY_RISK_MAP.get(cp_name, "MEDIUM"),
                "noss_ref": NOSS_REFS.get(cp_name, ""),
                "suggestion": f"Insert checkpoint '{cp_name}' in Safety Precautions section",
                "file": str(path),
            })
    return gaps


def scan_all_kk(root: Path) -> list[dict[str, str]]:
    """Scan all KK files under root and collect gaps."""
    all_gaps: list[dict[str, str]] = []
    for kk in sorted(root.rglob("KK-*.md")):
        subject = detect_subject(kk)
        if subject == "unknown":
            continue
        gaps = audit_kk_file(kk, subject)
        all_gaps.extend(gaps)
    return all_gaps


def generate_report(gaps: list[dict[str, str]], output: Path) -> dict[str, object]:
    """Build report and write HTML or JSON."""
    by_risk: dict[str, int] = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0}
    for g in gaps:
        by_risk[g["risk"]] = by_risk.get(g["risk"], 0) + 1

    report: dict[str, object] = {"total_gaps": len(gaps), "by_risk": by_risk, "gaps": gaps}

    if output.suffix == ".html":
        rows = "".join(
            f"<tr><td>{g['file'].split('/')[-1] if '/' in g['file'] else g['file'].split(chr(92))[-1]}</td>"
            f"<td>{g['checkpoint']}</td><td><b>{g['risk']}</b></td>"
            f"<td>{g['noss_ref']}</td><td>{g['suggestion']}</td></tr>"
            for g in gaps
        )
        html = (f"<html><head><title>KK Safety Checkpoint Report</title></head><body>"
                f"<h1>KK Safety Checkpoint Gap Report</h1>"
                f"<p>Total gaps: {len(gaps)} | CRITICAL: {by_risk['CRITICAL']} | HIGH: {by_risk['HIGH']}</p>"
                f"<table border=1><tr><th>File</th><th>Checkpoint</th><th>Risk</th>"
                f"<th>NOSS Ref</th><th>Suggestion</th></tr>{rows}</table></body></html>")
        output.write_text(html, encoding="utf-8")
    else:
        output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="KK Safety Checkpoint Validator")
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, default=Path("kk_safety_report.html"))
    args = parser.parse_args()
    gaps = scan_all_kk(args.root)
    report = generate_report(gaps, args.output)
    print(f"Found {report['total_gaps']} missing safety checkpoints → {args.output}")
    if report["total_gaps"]:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
