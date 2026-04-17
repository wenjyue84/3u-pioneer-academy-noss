"""Tests for audit-regulatory-compliance.py (US-046)."""
from __future__ import annotations

import csv
import importlib.util
import sys
import tempfile
from pathlib import Path

import pytest

# Load module from hyphenated filename
_TOOL_PATH = Path(__file__).parent.parent / "tools" / "audit-regulatory-compliance.py"
_spec = importlib.util.spec_from_file_location("audit_regulatory_compliance", _TOOL_PATH)
_mod = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(_mod)  # type: ignore[union-attr]

parse_compliance_matrix = _mod.parse_compliance_matrix
files_matching_keywords = _mod.files_matching_keywords
generate_report = _mod.generate_report
write_csv = _mod.write_csv

# ---------------------------------------------------------------------------
# Test fixtures
# ---------------------------------------------------------------------------

SAMPLE_MATRIX = """\
# Compliance Matrix

### REG: T&CM Act 2013

#### SEC: Registration and Scope
**Keywords:** registered practitioner, registration, scope of practice
**Required Coverage:** All lesson plans must state practitioners must be registered.
**Verification Points:** PM-teori.md, KP-01

#### SEC: Patient Consent
**Keywords:** consent, informed consent
**Required Coverage:** KP documents must address obtaining informed consent.
**Verification Points:** KP-01, KK-01, PA.md

### REG: PDPA 2010

#### SEC: Confidentiality
**Keywords:** confidential, privacy, data security
**Required Coverage:** Address patient confidentiality obligations.
**Verification Points:** KP-01, KA.md
"""

COMPLIANT_DOC = """\
# KP-01 Client Assessment

Registered practitioner must obtain informed consent before treatment.
Patient data is confidential and protected under PDPA.
All tuina practitioners must hold valid registration.
"""

GAP_DOC = """\
# KP-02 Tuina Techniques

Apply pressure along meridian pathways.
Use appropriate force for the client's condition.
"""


def _write_matrix(content: str) -> Path:
    f = tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    )
    f.write(content)
    f.close()
    return Path(f.name)


# ---------------------------------------------------------------------------
# parse_compliance_matrix
# ---------------------------------------------------------------------------

class TestParseComplianceMatrix:
    def test_parses_regulations(self) -> None:
        rules = parse_compliance_matrix(_write_matrix(SAMPLE_MATRIX))
        regs = {r["regulation"] for r in rules}
        assert "T&CM Act 2013" in regs
        assert "PDPA 2010" in regs

    def test_parses_sections(self) -> None:
        rules = parse_compliance_matrix(_write_matrix(SAMPLE_MATRIX))
        sections = [r["section"] for r in rules]
        assert "Registration and Scope" in sections
        assert "Patient Consent" in sections
        assert "Confidentiality" in sections

    def test_parses_keywords(self) -> None:
        rules = parse_compliance_matrix(_write_matrix(SAMPLE_MATRIX))
        consent_rule = next(r for r in rules if r["section"] == "Patient Consent")
        assert "consent" in consent_rule["keywords"]
        assert "informed consent" in consent_rule["keywords"]

    def test_three_rules_total(self) -> None:
        rules = parse_compliance_matrix(_write_matrix(SAMPLE_MATRIX))
        assert len(rules) == 3


# ---------------------------------------------------------------------------
# files_matching_keywords
# ---------------------------------------------------------------------------

class TestFilesMatchingKeywords:
    def test_detects_keyword_in_doc(self) -> None:
        docs = {"KP-01.md": COMPLIANT_DOC}
        assert "KP-01.md" in files_matching_keywords(docs, ["consent"])

    def test_no_match_when_keyword_absent(self) -> None:
        docs = {"KP-02.md": GAP_DOC}
        assert files_matching_keywords(docs, ["consent", "registered practitioner"]) == []

    def test_case_insensitive_match(self) -> None:
        docs = {"doc.md": "The patient gave Informed Consent before treatment."}
        assert "doc.md" in files_matching_keywords(docs, ["informed consent"])

    def test_whole_word_boundary(self) -> None:
        # 'consent' must NOT match inside 'nonconsensual'
        docs = {"doc.md": "This was a nonconsensual procedure."}
        assert files_matching_keywords(docs, ["consent"]) == []

    def test_multiple_docs(self) -> None:
        docs = {
            "KP-01.md": COMPLIANT_DOC,
            "KP-02.md": GAP_DOC,
            "KP-03.md": "This doc also requires informed consent.",
        }
        matched = files_matching_keywords(docs, ["consent"])
        assert "KP-01.md" in matched
        assert "KP-03.md" in matched
        assert "KP-02.md" not in matched


# ---------------------------------------------------------------------------
# generate_report
# ---------------------------------------------------------------------------

class TestGenerateReport:
    def _rules(self) -> list[dict[str, str]]:
        return parse_compliance_matrix(_write_matrix(SAMPLE_MATRIX))

    def test_compliant_when_keywords_found(self) -> None:
        rows = generate_report(self._rules(), {"KP-01.md": COMPLIANT_DOC}, None)
        statuses = {r["Section"]: r["Status"] for r in rows}
        assert statuses["Registration and Scope"] == "Compliant"
        assert statuses["Patient Consent"] == "Compliant"

    def test_gap_when_no_match(self) -> None:
        rows = generate_report(self._rules(), {"KP-02.md": GAP_DOC}, None)
        statuses = {r["Section"]: r["Status"] for r in rows}
        assert statuses["Registration and Scope"] == "Gap"
        assert statuses["Patient Consent"] == "Gap"

    def test_regulation_filter(self) -> None:
        rows = generate_report(self._rules(), {"KP-01.md": COMPLIANT_DOC}, "PDPA 2010")
        assert all(r["Regulation"] == "PDPA 2010" for r in rows)
        assert len(rows) == 1

    def test_csv_columns_present(self) -> None:
        rows = generate_report(self._rules(), {"KP-01.md": COMPLIANT_DOC}, None)
        required = {"Regulation", "Section", "Required Coverage",
                    "Files Addressing", "Status", "Recommendation"}
        for row in rows:
            assert required.issubset(row.keys())


# ---------------------------------------------------------------------------
# write_csv
# ---------------------------------------------------------------------------

class TestWriteCsv:
    def test_csv_roundtrip(self) -> None:
        rows = [
            {
                "Regulation": "T&CM Act 2013",
                "Section": "Patient Consent",
                "Required Coverage": "Obtain informed consent.",
                "Files Addressing": "KP-01.md",
                "Status": "Compliant",
                "Recommendation": "Coverage confirmed.",
            }
        ]
        out = Path(tempfile.mktemp(suffix=".csv"))
        write_csv(rows, out)
        result = list(csv.DictReader(out.open(encoding="utf-8")))
        assert len(result) == 1
        assert result[0]["Regulation"] == "T&CM Act 2013"
        assert result[0]["Status"] == "Compliant"
