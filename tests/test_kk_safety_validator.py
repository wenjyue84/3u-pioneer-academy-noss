"""Tests for KK Safety Checkpoint Validator (US-028)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from validators.kk_safety_checkpoint_validator import (
    REQUIRED_CHECKPOINTS,
    audit_kk_file,
    detect_subject,
    generate_report,
    scan_all_kk,
)

# Minimal BEV KK — missing ALL safety checkpoints (no PPE, no insulation test, no ground, no HV isolation, no LOTO)
_BEV_KK_BARE = """\
# KERTAS KERJA / WORK SHEET
**Kod:** G452-010-3:2023-C01/KK(1/3)

## Prosedur Kerja / Work Procedure

### Step 1: Connect Diagnostic Tool
1.1 Connect OBD-II cable to vehicle port.
1.2 Launch scan tool software.

### Step 2: Read Fault Codes
2.1 Select BEV diagnostic menu.
2.2 Record all active DTCs.

### Step 3: Clear Codes After Repair
3.1 Select clear codes option.
3.2 Verify no codes return.
"""

# Aesthetic KK — missing contraindication_screening, patch_test, equipment_sterilisation (3 gaps)
_AESTHETIC_KK_PARTIAL = """\
# KERTAS KERJA / WORK SHEET
**Kod:** S960-002-3:2020-C02/KK(1/4)

## Safety Precautions
1. Wash hands before treatment.
2. Confirm client comfort and obtain informed consent.

## Procedure

### Step 1: Prepare Client
1.1 Ask client to lie on the couch.
1.2 Drape client with towel.

### Step 2: Apply Treatment
2.1 Apply product to skin.
2.2 Massage in circular motions.

### Step 3: Post Treatment
3.1 Remove product.
3.2 Apply finishing lotion.
"""


def _write_kk(tmp_path: Path, subdir: str, filename: str, content: str) -> Path:
    d = tmp_path / subdir / "C01"
    d.mkdir(parents=True, exist_ok=True)
    p = d / filename
    p.write_text(content, encoding="utf-8")
    return p


def test_detect_subject_bev() -> None:
    """detect_subject correctly identifies BEV from path."""
    p = Path("bev-diagnostic-rectification/C01/KK-01.md")
    assert detect_subject(p) == "bev"


def test_detect_subject_aesthetic() -> None:
    """detect_subject correctly identifies Aesthetic from path."""
    p = Path("aesthetic-services/C01/KK-01.md")
    assert detect_subject(p) == "aesthetic"


def test_required_checkpoints_structure() -> None:
    """required_checkpoints has entries for both subjects."""
    assert "bev" in REQUIRED_CHECKPOINTS
    assert "aesthetic" in REQUIRED_CHECKPOINTS
    assert len(REQUIRED_CHECKPOINTS["bev"]) >= 3
    assert len(REQUIRED_CHECKPOINTS["aesthetic"]) >= 3


def test_detect_missing_hv_safety_checkpoints(tmp_path: Path) -> None:
    """Integration: seeded BEV + Aesthetic KK files yield 8+ missing checkpoints."""
    bev_path = _write_kk(tmp_path, "bev-diagnostic-rectification", "KK-01.md", _BEV_KK_BARE)
    aes_path = _write_kk(tmp_path, "aesthetic-services", "KK-01.md", _AESTHETIC_KK_PARTIAL)

    bev_gaps = audit_kk_file(bev_path, "bev")
    aes_gaps = audit_kk_file(aes_path, "aesthetic")
    total_gaps = len(bev_gaps) + len(aes_gaps)

    assert total_gaps >= 8, f"Expected >=8 missing checkpoints, got {total_gaps} (bev={len(bev_gaps)}, aes={len(aes_gaps)})"

    bev_cp_names = {g["checkpoint"] for g in bev_gaps}
    assert "ppe_verification" in bev_cp_names, "BEV must flag missing PPE verification"
    assert "insulation_test" in bev_cp_names, "BEV must flag missing insulation test"
    assert "ground_continuity" in bev_cp_names, "BEV must flag missing ground continuity"

    aes_cp_names = {g["checkpoint"] for g in aes_gaps}
    assert "contraindication_screening" in aes_cp_names, "Aesthetic must flag missing contraindication screening"


def test_gap_has_noss_ref(tmp_path: Path) -> None:
    """Each gap includes a NOSS reference and suggestion."""
    path = _write_kk(tmp_path, "bev-diagnostic-rectification", "KK-02.md", _BEV_KK_BARE)
    gaps = audit_kk_file(path, "bev")
    assert gaps, "Expected gaps in bare BEV KK file"
    for g in gaps:
        assert g.get("noss_ref"), f"Gap {g['checkpoint']} missing noss_ref"
        assert g.get("suggestion"), f"Gap {g['checkpoint']} missing suggestion"
        assert g["risk"] in ("CRITICAL", "HIGH", "MEDIUM")


def test_generate_html_report(tmp_path: Path) -> None:
    """HTML report contains table and gap counts."""
    path = _write_kk(tmp_path, "bev-diagnostic-rectification", "KK-03.md", _BEV_KK_BARE)
    gaps = audit_kk_file(path, "bev")
    out = tmp_path / "report.html"
    report = generate_report(gaps, out)
    html = out.read_text(encoding="utf-8")
    assert "<table" in html
    assert "CRITICAL" in html
    assert report["total_gaps"] == len(gaps)


def test_scan_all_kk(tmp_path: Path) -> None:
    """scan_all_kk finds gaps across multiple KK files."""
    _write_kk(tmp_path, "bev-diagnostic-rectification", "KK-01.md", _BEV_KK_BARE)
    _write_kk(tmp_path, "aesthetic-services", "KK-01.md", _AESTHETIC_KK_PARTIAL)
    gaps = scan_all_kk(tmp_path)
    assert len(gaps) >= 8
