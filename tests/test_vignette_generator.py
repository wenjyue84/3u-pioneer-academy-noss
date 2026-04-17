"""Tests for clinical vignette generator — validates structure and contraindications."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from clinical_vignette_generator import CU_META, SECTIONS, generate_vignettes

PREGNANCY_POINTS = ["合谷 LI4", "三阴交 SP6", "肩井 GB21", "至阴 BL67", "昆仑 BL60"]


@pytest.mark.parametrize("cu", list(CU_META.keys()))
def test_vignette_structure(cu: str) -> None:
    content = generate_vignettes(cu)
    for section in SECTIONS:
        assert section in content, f"{cu} missing section: {section}"


@pytest.mark.parametrize("cu", list(CU_META.keys()))
def test_vignette_count(cu: str) -> None:
    content = generate_vignettes(cu)
    cases = content.count("## 案例")
    assert 3 <= cases <= 5, f"{cu} has {cases} vignettes, expected 3-5"


@pytest.mark.parametrize("cu", list(CU_META.keys()))
def test_contraindication_mentions(cu: str) -> None:
    content = generate_vignettes(cu)
    for pt in PREGNANCY_POINTS:
        assert pt in content, f"{cu} missing pregnancy contraindication: {pt}"


def test_vignette_word_count() -> None:
    content = generate_vignettes("C01")
    cases = content.split("## 案例")[1:]
    for i, case in enumerate(cases):
        chars = len(case.replace(" ", "").replace("\n", "").replace("#", ""))
        assert chars >= 100, f"Case {i + 1} too short: {chars} chars"


def test_invalid_cu_raises() -> None:
    with pytest.raises(ValueError, match="Unknown CU"):
        generate_vignettes("X99")
