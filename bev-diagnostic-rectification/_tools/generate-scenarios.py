"""BEV Diagnostic Fault Code Scenario Generator.

Generates KT-format diagnostic troubleshooting scenarios from fault-code-scenarios.json.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "fault-code-scenarios.json"


def load_fault_codes(path: Path = DATA_FILE) -> list[dict]:
    """Load fault code scenarios from JSON file."""
    return json.loads(path.read_text(encoding="utf-8"))


def create_scenario_question(entry: dict, idx: int = 1) -> str:
    """Format a single fault code entry as a KT markdown scenario."""
    symptoms = ", ".join(entry["symptoms"])
    steps = "\n".join(f"   {i}. {s}" for i, s in enumerate(entry["diagnosis_steps"], 1))
    kps = ", ".join(entry["relevant_kps"])
    return (
        f"### Scenario {idx}: {entry['fault_code']} — {entry['component']}\n\n"
        f"**Fault Code:** {entry['fault_code']}\n"
        f"**Component:** {entry['component']}\n"
        f"**Symptoms:** {symptoms}\n\n"
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
            print(f"{c['fault_code']}  {c['component']:20s}  {', '.join(c['relevant_kps'])}")
        return

    if args.output:
        codes = [c for c in codes if any(args.output in kp for kp in c["relevant_kps"])]

    md = "# BEV Diagnostic Fault Code Scenarios\n\n"
    for i, entry in enumerate(codes, 1):
        md += create_scenario_question(entry, i) + "\n---\n\n"

    if args.out_dir:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        dest = args.out_dir / f"scenarios-{args.output or 'all'}.md"
        dest.write_text(md, encoding="utf-8")
        print(f"Written to {dest}")
    else:
        print(md)


if __name__ == "__main__":
    main()
