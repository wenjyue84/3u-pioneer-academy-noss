"""BEV Diagnostic Fault Code Scenario Generator.

Generates KT-format diagnostic troubleshooting scenarios from fault-code-scenarios.json.

Usage:
    uv run python bev-diagnostic-rectification/_tools/generate-scenarios.py
    uv run python bev-diagnostic-rectification/_tools/generate-scenarios.py --output C02
    uv run python bev-diagnostic-rectification/_tools/generate-scenarios.py --list
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "fault-code-scenarios.json"


def load_fault_codes(path: Path = DATA_FILE) -> list[dict]:
    """Load fault code scenarios from JSON file."""
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["fault_codes"]


def create_scenario_question(entry: dict, idx: int = 1) -> str:
    """Format a single fault code entry as a KT-format markdown scenario question."""
    code = entry["fault_code"]
    component = entry["component"]
    system = entry.get("system", "")
    symptoms = "\n".join(f"   - {s}" for s in entry["symptoms"])
    steps = "\n".join(f"   {i}. {s}" for i, s in enumerate(entry["diagnosis_steps"], 1))
    kps = ", ".join(entry["relevant_kps"])
    return (
        f"### Senario {idx} / Scenario {idx}: {code} — {component}\n\n"
        f"**Kod Kesalahan / Fault Code:** {code}\n"
        f"**Komponen / Component:** {component}\n"
        f"**Sistem / System:** {system}\n"
        f"**KP Rujukan / Reference KPs:** {kps}\n\n"
        f"**Simptom / Symptoms:**\n{symptoms}\n\n"
        f"**B1.** Namakan komponen yang terlibat dan terangkan fungsi utamanya.\n"
        f"*(Name the component involved and explain its main function.)*\n\n"
        f"**B2.** Berdasarkan simptom di atas, senaraikan tiga (3) punca yang mungkin.\n"
        f"*(Based on the symptoms above, list three (3) possible causes.)*\n\n"
        f"**B3.** Huraikan prosedur diagnosis langkah-demi-langkah:\n"
        f"*(Describe the step-by-step diagnosis procedure:)*\n\n"
        f"**Diagnosis Procedure:**\n{steps}\n\n"
        f"**Reference:** {kps}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate BEV diagnostic scenarios")
    parser.add_argument("--list", action="store_true", help="List all fault codes")
    parser.add_argument("--output", choices=["C01", "C02", "C03"], help="Filter by CU")
    parser.add_argument("--out-dir", type=Path, help="Write output files to directory")
    args = parser.parse_args()

    codes = load_fault_codes()

    if args.list:
        for c in codes:
            print(f"{c['fault_code']}  {c['component']:30s}  {', '.join(c['relevant_kps'])}")
        return

    cu_filter = args.output
    if cu_filter:
        codes = [c for c in codes if any(cu_filter in kp for kp in c["relevant_kps"])]

    suffix = cu_filter or "all"
    md_lines = [
        "# KERTAS TUGASAN / ASSIGNMENT SHEET — BEV Diagnostic Fault Code Scenarios\n",
        f"**WIM Standard:** G452-010-3:2023 — {suffix.upper()}",
        "**Kertas Warna / Paper Color:** MERAH JAMBU / PINK",
        f"**Jumlah Senario / Total Scenarios:** {len(codes)}",
        "",
        "---",
        "",
    ]
    for i, entry in enumerate(codes, 1):
        md_lines.append(create_scenario_question(entry, i))
        md_lines.append("---\n")

    md = "\n".join(md_lines)

    if args.out_dir:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        dest = args.out_dir / f"KT-fault-scenarios-{suffix}.md"
        dest.write_text(md, encoding="utf-8")
        print(f"Generated {len(codes)} scenarios -> {dest}")
    else:
        print(md)


if __name__ == "__main__":
    main()
