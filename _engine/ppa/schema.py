"""Graph + profile schema for the NOSS → PPT-PPA assessment engine.

The competency graph is a faithful, traceable transcription of a NOSS Competency
Profile Chart / CoCU. It carries no assessment decisions. Every decision about
*which* competency unit gets assessed and *how* lives in the profile, supplied by
the human running the build.

Source of truth for a graph is always the `source_file` it names — a graph whose
claims cannot be found in that file is a bug, not a variation.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Literal

CUMode = Literal["practical", "oral", "excluded"]
CUType = Literal["core", "elective"]

# `bm_frame_en_body` is the house style of the accredited centre, established by
# reading the four papers Jennifer owns (see `_engine/FORMAT-jpk-ppa.md` §1):
# Malay for section headings, table headers, cover labels and fixed JPK
# boilerplate; English for everything the paper actually says. The two never
# appear in the same sentence — which is what "only one language" meant.
Language = Literal["bm", "en", "bm_frame_en_body"]


@dataclass
class PerformanceCriterion:
    id: str                      # "1.1" — numbering as printed in the NOSS
    text: str                    # verbatim from the CoCU (English; NOSS are EN)

    @staticmethod
    def from_dict(d: dict) -> "PerformanceCriterion":
        return PerformanceCriterion(id=d["id"], text=d["text"])


@dataclass
class WorkActivity:
    id: str                      # "WA1"
    title: str                   # "Identify market & product survey objective"
    title_bm: str = ""           # used when the paper's language is "bm"
    performance_criteria: list[PerformanceCriterion] = field(default_factory=list)

    def label(self, language: Language) -> str:
        return (self.title_bm or self.title) if language == "bm" else self.title

    @staticmethod
    def from_dict(d: dict) -> "WorkActivity":
        return WorkActivity(
            id=d["id"],
            title=d["title"],
            title_bm=d.get("title_bm", ""),
            performance_criteria=[PerformanceCriterion.from_dict(p)
                                  for p in d.get("performance_criteria", [])],
        )


@dataclass
class CompetencyUnit:
    code: str                    # "C01" / "E01"
    type: CUType
    title_en: str
    title_bm: str                # translation used when language == "bm"
    descriptor: str = ""
    work_activities: list[WorkActivity] = field(default_factory=list)

    @property
    def pc_count(self) -> int:
        return sum(len(wa.performance_criteria) for wa in self.work_activities)

    def title(self, language: Language) -> str:
        return self.title_bm if language == "bm" else self.title_en

    @staticmethod
    def from_dict(d: dict) -> "CompetencyUnit":
        return CompetencyUnit(
            code=d["code"],
            type=d["type"],
            title_en=d["title_en"],
            title_bm=d["title_bm"],
            descriptor=d.get("descriptor", ""),
            work_activities=[WorkActivity.from_dict(w)
                             for w in d.get("work_activities", [])],
        )


@dataclass
class NossGraph:
    noss_code: str               # "FB-018-3:2012"
    noss_title: str              # "SALES & MARKETING OPERATION"
    level: int
    source_file: str             # path, relative to project root, that this was read from
    sector: str = ""
    sub_sector: str = ""
    job_area: str = ""
    competency_units: list[CompetencyUnit] = field(default_factory=list)
    # Misprints and ambiguities found in the source NOSS, recorded rather than
    # silently corrected — a transcription that "fixes" the standard stops being
    # traceable to it.
    source_notes: list[str] = field(default_factory=list)

    def cu(self, code: str) -> CompetencyUnit:
        for c in self.competency_units:
            if c.code.upper() == code.upper():
                return c
        raise KeyError(f"{self.noss_code} has no competency unit {code!r}; "
                       f"known: {[c.code for c in self.competency_units]}")

    @property
    def codes(self) -> list[str]:
        return [c.code for c in self.competency_units]

    @staticmethod
    def load(path: str | Path) -> "NossGraph":
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        return NossGraph(
            noss_code=d["noss_code"],
            noss_title=d["noss_title"],
            level=d["level"],
            source_file=d["source_file"],
            sector=d.get("sector", ""),
            sub_sector=d.get("sub_sector", ""),
            job_area=d.get("job_area", ""),
            competency_units=[CompetencyUnit.from_dict(c)
                              for c in d.get("competency_units", [])],
            source_notes=d.get("source_notes", []),
        )

    def dump(self, path: str | Path) -> None:
        Path(path).write_text(
            json.dumps(asdict(self), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")


# --------------------------------------------------------------------------- #
# Profile — the human's decisions. Never inferred, never defaulted silently.
# --------------------------------------------------------------------------- #

@dataclass
class Centre:
    """The Pusat Bertauliah whose name goes on the cover page.

    Getting this wrong is not cosmetic: the paper is submitted under this centre's
    accreditation. Round 1 inherited "VIZTECH TRADING SDN. BHD." from the reference
    sample — a different centre entirely.
    """
    name: str
    code: str = ""


@dataclass
class ScenarioSet:
    """Set A and Set B must assess the same competencies against different context.

    Same CU modes, same time budget, same mark split — different product, customer
    and data. That is what makes them parallel forms rather than two random papers.
    """
    set_id: str                  # "A" / "B"
    industry: str                # "Hartanah kediaman"
    company: str                 # fictional company used throughout the paper
    product: str
    notes: str = ""

    @staticmethod
    def from_dict(d: dict) -> "ScenarioSet":
        return ScenarioSet(set_id=d["set_id"], industry=d["industry"],
                           company=d["company"], product=d["product"],
                           notes=d.get("notes", ""))


@dataclass
class Profile:
    noss_code: str
    graph_file: str
    assessment_type: str                     # "PPT-PPA"
    language: Language
    centre: Centre
    duration_min_minutes: int
    duration_max_minutes: int
    cu_modes: dict[str, CUMode]              # every CU in the graph must appear
    oral_question_count: int
    practical_weight: int                    # percent
    oral_weight: int                         # percent
    sets: list[ScenarioSet] = field(default_factory=list)
    notes: str = ""

    # -- derived views -------------------------------------------------------
    def codes_with_mode(self, mode: CUMode) -> list[str]:
        return sorted(c for c, m in self.cu_modes.items() if m == mode)

    @property
    def practical_cus(self) -> list[str]:
        return self.codes_with_mode("practical")

    @property
    def oral_cus(self) -> list[str]:
        return self.codes_with_mode("oral")

    @property
    def excluded_cus(self) -> list[str]:
        return self.codes_with_mode("excluded")

    @property
    def assessed_cus(self) -> list[str]:
        return sorted(self.practical_cus + self.oral_cus)

    def set(self, set_id: str) -> ScenarioSet:
        for s in self.sets:
            if s.set_id.upper() == set_id.upper():
                return s
        raise KeyError(f"profile {self.noss_code} has no set {set_id!r}")

    @staticmethod
    def load(path: str | Path) -> "Profile":
        d = json.loads(Path(path).read_text(encoding="utf-8"))
        return Profile(
            noss_code=d["noss_code"],
            graph_file=d["graph_file"],
            assessment_type=d["assessment_type"],
            language=d["language"],
            centre=Centre(**d["centre"]),
            duration_min_minutes=d["duration_min_minutes"],
            duration_max_minutes=d["duration_max_minutes"],
            cu_modes=d["cu_modes"],
            oral_question_count=d["oral_question_count"],
            practical_weight=d["practical_weight"],
            oral_weight=d["oral_weight"],
            sets=[ScenarioSet.from_dict(s) for s in d.get("sets", [])],
            notes=d.get("notes", ""),
        )

    def dump(self, path: str | Path) -> None:
        Path(path).write_text(
            json.dumps(asdict(self), ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")
