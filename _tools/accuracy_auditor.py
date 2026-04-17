"""Technical content accuracy auditor against industry standards."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STANDARDS_PATH = (
    Path(__file__).resolve().parent.parent / "_reference" / "industry_standards_index.json"
)


def load_standards() -> list[dict[str, object]]:
    """Load industry standards index from JSON."""
    return json.loads(STANDARDS_PATH.read_text(encoding="utf-8"))  # type: ignore[return-value]


def _finding(
    kp_section: str,
    claim: str,
    standard: str,
    status: str,
    action: str,
) -> dict[str, str]:
    return {
        "kp_section": kp_section,
        "technical_claim": claim,
        "standard_reference": standard,
        "compliance_status": status,
        "recommended_action": action,
    }


def audit_bev_standards(
    text: str,
    standards: list[dict[str, object]] | None = None,
) -> list[dict[str, str]]:
    """Audit BEV text against IEC 61508, EN 455, IEC 62196 standards."""
    if standards is None:
        standards = load_standards()
    bev_stds = {s["standard_name"]: s for s in standards if s["applicable_subject"] == "BEV"}
    findings: list[dict[str, str]] = []

    # IEC 61508: HV threshold >=48V
    if "IEC 61508" in bev_stds:
        reqs = bev_stds["IEC 61508"]["key_requirements"]
        threshold = int(reqs["hv_threshold_volts"])  # type: ignore[arg-type,index]
        voltages = [int(m) for m in re.findall(r"(\d+)\s*[Vv](?:olt)?s?\b", text)]
        has_hv_label = bool(re.search(r"high.?voltage|HV\b", text, re.IGNORECASE))
        hv_voltages = [v for v in voltages if v >= threshold]
        if hv_voltages:
            for v in hv_voltages:
                findings.append(_finding(
                    "BEV",
                    f"{v}V detected",
                    "IEC 61508",
                    "Pass",
                    f"Voltage meets >={threshold}V HV classification threshold",
                ))
        elif has_hv_label and voltages:
            for v in voltages:
                findings.append(_finding(
                    "BEV",
                    f"{v}V labeled as high voltage",
                    "IEC 61508",
                    "Fail",
                    f"Voltage must be >={threshold}V for HV classification per IEC 61508",
                ))

    # EN 455: PPE glove standard reference
    if "EN 455" in bev_stds and re.search(
        r"\bPPE\b|protective.?glove|insulated.?glove", text, re.IGNORECASE
    ):
        if re.search(r"EN\s*455", text, re.IGNORECASE):
            findings.append(_finding(
                "BEV", "PPE glove standard referenced", "EN 455", "Pass", "EN 455 cited correctly",
            ))
        else:
            findings.append(_finding(
                "BEV",
                "PPE/gloves mentioned without EN 455 reference",
                "EN 455",
                "Fail",
                "Add EN 455 standard reference for protective gloves",
            ))

    # IEC 62196: EV connector standard
    if "IEC 62196" in bev_stds and re.search(
        r"connector|charging.?port|socket", text, re.IGNORECASE
    ):
        if re.search(r"IEC\s*62196", text, re.IGNORECASE):
            findings.append(_finding(
                "BEV", "EV connector standard referenced", "IEC 62196", "Pass", "IEC 62196 cited",
            ))
        else:
            findings.append(_finding(
                "BEV",
                "EV connector mentioned without IEC 62196 reference",
                "IEC 62196",
                "Fail",
                "Add IEC 62196 reference for EV connector types",
            ))

    return findings


def audit_aesthetic_standards(
    text: str,
    standards: list[dict[str, object]] | None = None,
) -> list[dict[str, str]]:
    """Audit Aesthetic text against ISO 18562 and medical safety standards."""
    if standards is None:
        standards = load_standards()
    aes_std = next(
        (s for s in standards if s["standard_name"] == "ISO 18562"), None
    )
    findings: list[dict[str, str]] = []

    # Ultrasound frequency range
    freq_matches = re.findall(r"(\d+(?:\.\d+)?)\s*kHz", text, re.IGNORECASE)
    for freq_str in freq_matches:
        freq = float(freq_str)
        f_min: float = 20.0
        f_max: float = 10000.0
        if aes_std:
            reqs = aes_std["key_requirements"]
            f_min = float(reqs["ultrasound_freq_khz_min"])  # type: ignore[arg-type,index]
            f_max = float(reqs["ultrasound_freq_khz_max"])  # type: ignore[arg-type,index]
        std_name = aes_std["standard_name"] if aes_std else "ISO 18562"
        if f_min <= freq <= f_max:
            findings.append(_finding(
                "Aesthetic",
                f"Ultrasound {freq}kHz",
                str(std_name),
                "Pass",
                f"Frequency within safe clinical range ({f_min}kHz-{f_max}kHz)",
            ))
        else:
            findings.append(_finding(
                "Aesthetic",
                f"Ultrasound {freq}kHz outside safe range",
                str(std_name),
                "Fail",
                f"Verify frequency is within {f_min}kHz-{f_max}kHz clinical range",
            ))

    # Chemical compatibility warnings
    if re.search(r"chemical|acid|base|solution|serum", text, re.IGNORECASE):
        if re.search(r"warning|caution|contraindic|safety", text, re.IGNORECASE):
            findings.append(_finding(
                "Aesthetic",
                "Chemical safety warning present",
                "Medical Standards",
                "Pass",
                "Chemical hazard warning included",
            ))
        else:
            findings.append(_finding(
                "Aesthetic",
                "Chemical substance without safety warning",
                "Medical Standards",
                "Fail",
                "Add chemical compatibility and safety warnings",
            ))

    return findings


def audit_it_standards(
    text: str,
    standards: list[dict[str, object]] | None = None,
) -> list[dict[str, str]]:
    """Audit IT text against ISO/IEC 11801 cabling standard."""
    if standards is None:
        standards = load_standards()
    findings: list[dict[str, str]] = []

    cable_match = re.search(r"Cat\s*(\d\w*)|category\s*(\d\w*)", text, re.IGNORECASE)
    if cable_match:
        cat = cable_match.group(1) or cable_match.group(2)
        if re.search(r"ISO.?IEC\s*11801|11801", text, re.IGNORECASE):
            findings.append(_finding(
                "IT",
                f"Cat{cat} cabling with ISO/IEC 11801 reference",
                "ISO/IEC 11801",
                "Pass",
                "Cabling standard correctly referenced",
            ))
        else:
            findings.append(_finding(
                "IT",
                f"Cat{cat} cabling without ISO/IEC 11801 reference",
                "ISO/IEC 11801",
                "Fail",
                "Add ISO/IEC 11801 reference for structured cabling",
            ))

    return findings


def format_audit_report(findings: list[dict[str, str]]) -> str:
    """Format audit findings as a human-readable report table."""
    if not findings:
        return "No findings.\n"
    header = (
        f"{'KP Section':<12} {'Technical Claim':<45} "
        f"{'Standard':<18} {'Status':<10} Action\n"
    )
    sep = "-" * 115 + "\n"
    rows = ""
    for f in findings:
        rows += (
            f"{f['kp_section']:<12} {f['technical_claim']:<45} "
            f"{f['standard_reference']:<18} {f['compliance_status']:<10} "
            f"{f['recommended_action']}\n"
        )
    return header + sep + rows


if __name__ == "__main__":
    text = sys.stdin.read() if not sys.stdin.isatty() else ""
    stds = load_standards()
    all_findings = (
        audit_bev_standards(text, stds)
        + audit_aesthetic_standards(text, stds)
        + audit_it_standards(text, stds)
    )
    print(format_audit_report(all_findings))
