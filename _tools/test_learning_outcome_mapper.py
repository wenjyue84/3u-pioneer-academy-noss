"""Tests for learning_outcome_mapper."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from learning_outcome_mapper import (
    extract_assessment_item_tags,
    parse_noss_learning_outcomes,
)

SAMPLE_NOSS = """\
### 7.1 CoCU C01: Perform BEV Scheduled Maintenance

**Learning Outcomes:** Enable trainees to deliver accurate information.

#### WA 1: Carry out workplace preparation

**Related Knowledge:**
- 1.1 BEV rules and regulations: Licensing Legislative
- 1.2 Safety guidelines: PPE, workspace
- 1.3 Environmental impact: Waste handling

**Related Skills:**
- 1.1 Identify requirements

#### WA 2: Carry out health check

**Related Knowledge:**
- 2.1 Health check safety: Equipment, PPE
- 2.2 Tools and equipment

### 7.2 CoCU C02: Perform BMS Rectification

**Learning Outcomes:** Enable trainees to perform servicing.

#### WA 1: Carry out preparation

**Related Knowledge:**
- 1.1 BMS safety: HV precautions
"""


def test_noss_extract_parsing() -> None:
    los = parse_noss_learning_outcomes(SAMPLE_NOSS)
    assert len(los) == 6
    assert los[0]["cu"] == "C01"
    assert los[0]["lo_code"] == "LO-C01-01"
    assert "BEV rules" in los[0]["text"]
    assert los[2]["lo_code"] == "LO-C01-03"
    assert los[3]["lo_code"] == "LO-C01-04"
    assert los[5] == {
        "cu": "C02",
        "lo_code": "LO-C02-01",
        "text": "BMS safety: HV precautions",
    }


def test_extract_tags_empty(tmp_path: Path) -> None:
    d = tmp_path / "C01"
    d.mkdir()
    (d / "KA.md").write_text("# No LO tags\n", encoding="utf-8")
    assert extract_assessment_item_tags(tmp_path) == {}


def test_extract_tags_with_lo(tmp_path: Path) -> None:
    d = tmp_path / "C01"
    d.mkdir()
    (d / "KA.md").write_text(
        "Q1 <!-- LO-C01-01 -->\nQ2 <!-- LO-C01-03 -->\n",
        encoding="utf-8",
    )
    result = extract_assessment_item_tags(tmp_path)
    assert result == {"LO-C01-01": ["C01/KA"], "LO-C01-03": ["C01/KA"]}
