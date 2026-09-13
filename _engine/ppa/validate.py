"""Validators V01–V09 for a generated PPT-PPA paper.

Each validator encodes one defect that a human reviewer actually caught on
2026-08-24. They are deliberately mechanical: the point is that no future round
can regress on a defect that has already cost a review cycle.

A validator returns a list of `Finding`. Empty list = pass. `severity` is either
`error` (blocks delivery) or `warn` (report, do not block).
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path

from .schema import NossGraph, Profile

# --------------------------------------------------------------------------- #

@dataclass
class Finding:
    check: str
    severity: str          # "error" | "warn"
    message: str
    evidence: str = ""     # the actual line/snippet, so the report is not a claim
    line: int | None = None

    def as_dict(self) -> dict:
        return asdict(self)


@dataclass
class Paper:
    """A generated markdown paper, with the bits validators need pre-extracted."""
    path: Path
    text: str
    kind: str              # "soalan" | "skema" | "answer-sheet" | "equipment"
    set_id: str            # "A" | "B" | ""

    @staticmethod
    def load(path: str | Path) -> "Paper":
        p = Path(path)
        stem = p.stem.lower()
        kind = ("skema" if "skema" in stem else
                "answer-sheet" if "answer-sheet" in stem else
                "equipment" if "equipment" in stem else
                "soalan")
        m = re.search(r"set-([ab])", stem)
        return Paper(path=p, text=p.read_text(encoding="utf-8"),
                     kind=kind, set_id=(m.group(1).upper() if m else ""))

    @property
    def lines(self) -> list[str]:
        return self.text.splitlines()


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def _cu_mentions(text: str, code: str) -> list[tuple[int, str]]:
    """Every line that names a CU code as a standalone token.

    `\\b` alone is not enough: `C01` would match inside `C011`. The trailing
    lookahead keeps that from happening while still allowing `C01:` / `C01,`.
    """
    pat = re.compile(rf"(?<![A-Z0-9]){re.escape(code)}(?![0-9])", re.IGNORECASE)
    return [(i + 1, ln) for i, ln in enumerate(text.splitlines()) if pat.search(ln)]


# English function words that have no Bahasa Malaysia homograph. `and`/`or` are
# excluded on purpose — they show up inside legitimate English product names.
_EN_MARKERS = {
    "the", "of", "to", "is", "are", "with", "for", "from", "shall", "must",
    "been", "following", "required", "candidate", "according", "based",
    "will", "on", "in", "at", "as", "by", "this", "that", "these", "should",
    "provided", "prepare", "complete", "each", "their", "there", "which",
}
# English content words that betray a translated-pair right-hand side. Kept
# separate from the function words above because a gloss is usually all nouns.
_EN_GLOSS = _EN_MARKERS | {
    "market", "product", "survey", "sales", "online", "service", "services",
    "customer", "assessment", "performance", "inventory", "control", "report",
    "marketing", "direct", "retail", "collateral", "pitch", "form", "sheet",
    "working", "candidate", "printing", "paper", "folder", "filing", "clipboard",
    # Office-administration vocabulary, added after `Stock Card / Inventory
    # Issuance Record` — two English form names — was misread as a bilingual pair.
    "stock", "card", "cash", "petty", "bills", "purchase", "requisition",
    "issuance", "cabinet", "environment", "payment", "collection", "office",
    "procurement", "logistic", "documentation", "reception", "front", "back",
}

# Bahasa Malaysia function and structure words. Used to establish that a phrase
# really is Malay, rather than inferring it from the absence of English.
_BM_MARKERS = {
    "dan", "atau", "yang", "untuk", "pada", "dalam", "dengan", "oleh", "kepada",
    "daripada", "adalah", "ini", "itu", "bagi", "serta", "akan", "telah", "tidak",
    "mesti", "hendaklah", "boleh", "perlu", "semua", "setiap", "calon", "kerja",
    "laporan", "borang", "senarai", "maklumat", "bayaran", "bulanan", "jualan",
    "pelanggan", "peralatan", "bahan", "dokumen", "penilaian", "markah",
    "sediakan", "menyediakan", "kertas", "muka", "surat", "tempoh", "pemeriksa",
}


def _has(words: set[str], phrase: str) -> bool:
    return any(w in words for w in phrase.lower().split())


def _count(words: set[str], phrase: str) -> int:
    return sum(1 for w in phrase.lower().split() if w in words)


# Lines that are legitimately not prose and must never be language-checked.
_SKIP_LINE = re.compile(r"^\s*(\|[\s\-:|]+\||[-=_*]{3,}|<!--|```|\d+\.\s*$)\s*$")


def _looks_english(line: str) -> tuple[bool, int]:
    words = re.findall(r"[A-Za-z][A-Za-z'-]*", line.lower())
    if len(words) < 8:
        return False, 0
    hits = sum(1 for w in words if w in _EN_MARKERS)
    return hits >= 3, hits


# --------------------------------------------------------------------------- #
# Validators
# --------------------------------------------------------------------------- #

def v01_profile_covers_graph(graph: NossGraph, profile: Profile, _paper=None) -> list[Finding]:
    """Every CU in the NOSS must be given an explicit mode — no silent defaults.

    A CU the profile forgot is exactly how E01 ended up declared on the cover
    with zero questions behind it.
    """
    out: list[Finding] = []
    for code in graph.codes:
        if code not in profile.cu_modes:
            out.append(Finding("V01", "error",
                               f"{code} exists in {graph.noss_code} but the profile "
                               f"assigns it no mode (practical/oral/excluded)."))
    for code in profile.cu_modes:
        if code.upper() not in {c.upper() for c in graph.codes}:
            out.append(Finding("V01", "error",
                               f"profile assigns a mode to {code}, which is not a "
                               f"competency unit of {graph.noss_code}."))
    return out


def v02_practical_cu_has_task(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """Each practical CU must be named in the TUGASAN section of the soalan."""
    if paper.kind != "soalan":
        return []
    body = _tugasan_section(paper.text)
    if body is None:
        return [Finding("V02", "error",
                        "no 'TUGASAN' section found — cannot prove practical "
                        "coverage.", evidence=paper.path.name)]
    return [Finding("V02", "error",
                    f"{code} is marked practical but is never referenced in the "
                    f"TUGASAN section.", evidence=paper.path.name)
            for code in profile.practical_cus
            if not _cu_mentions(body, code)]


def v03_oral_cu_has_question(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """Oral CUs must each carry at least one question, and the total must match."""
    if paper.kind != "skema":
        return []
    body = _oral_section(paper.text)
    out: list[Finding] = []
    if body is None:
        if profile.oral_cus:
            out.append(Finding("V03", "error",
                               "no oral / 'SOAL JAWAB' section found, but the profile "
                               f"routes {', '.join(profile.oral_cus)} to oral assessment.",
                               evidence=paper.path.name))
        return out
    for code in profile.oral_cus:
        if not _cu_mentions(body, code):
            out.append(Finding("V03", "error",
                               f"{code} is marked oral but no oral question maps to it.",
                               evidence=paper.path.name))
    numbered = re.findall(r"^\s*\|?\s*5\.(\d{1,2})\b", body, re.MULTILINE)
    n = len({int(x) for x in numbered})
    if n and n != profile.oral_question_count:
        out.append(Finding("V03", "error",
                           f"profile asks for {profile.oral_question_count} oral "
                           f"questions; the skema has {n}.", evidence=paper.path.name))
    return out


def v04_no_excluded_refs(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """An excluded CU must not appear anywhere — cover page included.

    This is the D2 defect: E01 INVENTORY CONTROL printed on the cover of both the
    soalan and the skema while scoring nothing.
    """
    out: list[Finding] = []
    for code in profile.excluded_cus:
        for lineno, line in _cu_mentions(paper.text, code):
            out.append(Finding("V04", "error",
                               f"{code} is excluded by the profile but appears in "
                               f"{paper.path.name}.",
                               evidence=line.strip()[:160], line=lineno))
        cu = graph.cu(code)
        for title in (cu.title_en, cu.title_bm):
            if title and re.search(re.escape(title), paper.text, re.IGNORECASE):
                out.append(Finding("V04", "error",
                                   f"{code} is excluded but its title '{title}' still "
                                   f"appears in {paper.path.name}.", evidence=title))
    return out


def v05_monolingual(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """`language: bm` means Bahasa Malaysia only.

    Jennifer's complaint #1 was 'only one language, here mixed language'. Two
    signatures are caught: slash-joined bilingual pairs, and English prose lines.

    Which of the two applies depends on the profile:

    * `bm`               — both checks. Nothing English survives.
    * `bm_frame_en_body` — only the slash-pair check. This is the centre's actual
      house style: Malay frame, English body, never mixed inside one sentence.
      Flagging English prose here would flag her own approved paper.
    """
    if profile.language not in ("bm", "bm_frame_en_body"):
        return []
    flag_english_prose = profile.language == "bm"
    out: list[Finding] = []
    for i, line in enumerate(paper.lines, start=1):
        if _SKIP_LINE.match(line) or not line.strip():
            continue
        # Bilingual pair: "<Malay phrase> / <English phrase>". Both sides must be
        # multi-word, otherwise this fires on legitimate pairs like "PPL / PPT".
        for left, right in re.findall(r"([A-Za-z][\w &'-]{6,})\s+/\s+([A-Za-z][\w &'-]{6,})", line):
            # A bilingual pair is Malay on the left and English on the right.
            # Anything else is a slash meaning "and/or" between two items, and
            # flagging it sends a writer off to "fix" correct text:
            #   `Petty Cash Payment Form / Bills Collection Report`  — two forms
            #   `laporan bayaran bulanan / laporan petty cash`       — two reports
            #   `updated shelf qty / back end balance`               — two fields
            # Requiring positive evidence of Malay on the left and none on the
            # right is what separates those from a real translation pair. Testing
            # only for "English on the right" is not enough — Malay borrows
            # `petty`, `cash`, `report` and plenty more.
            # `Tinjauan Pasaran & Produk` carries no Malay *function* word — the
            # common case is a bare noun phrase — so "left is Malay" is read as
            # "left is not English". And the right side needs two English words,
            # not one: `back end balance` has exactly one and is a data field, not
            # a translation.
            left_is_malay = _has(_BM_MARKERS, left) or not _has(_EN_GLOSS, left)
            right_is_english = (_count(_EN_GLOSS, right) >= 2
                                and not _has(_BM_MARKERS, right))
            if len(left.split()) >= 2 and len(right.split()) >= 2 and \
                    left_is_malay and right_is_english:
                out.append(Finding("V05", "error",
                                   "bilingual slash pair — pick one language.",
                                   evidence=f"{left.strip()} / {right.strip()}", line=i))
                break
        is_en, hits = _looks_english(line)
        if is_en and flag_english_prose:
            out.append(Finding("V05", "error",
                               f"English prose line ({hits} English function words) "
                               f"in a Bahasa Malaysia paper.",
                               evidence=line.strip()[:160], line=i))
    return out


def v06_cover_cu_list(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """The cover's competency-unit list must equal the assessed set, exactly."""
    if paper.kind not in ("soalan", "skema"):
        return []
    cover = paper.text[:4000]
    listed = sorted(set(re.findall(r"(?<![A-Z0-9])([CE]\d{2})(?![0-9])", cover.upper())))
    expected = sorted(profile.assessed_cus)
    out: list[Finding] = []
    for extra in set(listed) - set(expected):
        out.append(Finding("V06", "error",
                           f"cover lists {extra}, which the profile does not assess.",
                           evidence=paper.path.name))
    for missing in set(expected) - set(listed):
        out.append(Finding("V06", "error",
                           f"cover omits {missing}, which the profile does assess.",
                           evidence=paper.path.name))
    return out


def v07_duration(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """The declared TEMPOH must sit inside the profile's window."""
    if paper.kind != "soalan":
        return []
    # Only the paper-level `B. TEMPOH : 3 JAM` declaration counts. Per-task time
    # allocations ("Tempoh Masa: 35 minit") are budget lines, not the exam length.
    m = re.search(r"^[#*\s]*[A-Z]\.\s*TEMPOH\b[^\n]*?(\d+(?:[.,]\d+)?)\s*"
                  r"(JAM|MINIT|HOURS?|MINUTES?)",
                  paper.text, re.IGNORECASE | re.MULTILINE)
    if not m:
        return [Finding("V07", "error",
                        "no paper-level 'B. TEMPOH : n JAM' declaration found in the "
                        "soalan.", evidence=paper.path.name)]
    out: list[Finding] = []
    unit = m.group(2).upper()
    if profile.language == "bm" and unit not in ("JAM", "MINIT"):
        out.append(Finding("V07", "error",
                           f"duration unit '{m.group(2)}' is English; a Bahasa Malaysia "
                           f"paper declares JAM / MINIT.", evidence=m.group(0).strip()))
    value = float(m.group(1).replace(",", "."))
    minutes = value * 60 if unit.startswith(("JAM", "HOUR")) else value
    if not (profile.duration_min_minutes <= minutes <= profile.duration_max_minutes):
        out.append(Finding("V07", "error",
                           f"declared duration {minutes:.0f} min is outside the profile "
                           f"window {profile.duration_min_minutes}–"
                           f"{profile.duration_max_minutes} min.",
                           evidence=m.group(0).strip()))
    return out


def v08_page_declaration(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """The printed-page declaration must be a real number, not a placeholder.

    Defect D1: both of Jennifer's sample papers declared the wrong page count.
    The count is only knowable after rendering, so the markdown carries ⟪PAGES⟫
    and `build/ppa_integrate.py` backfills it. An unresolved placeholder reaching
    delivery is a hard failure; a hardcoded number is a warning because it might
    be correct by luck.
    """
    if paper.kind not in ("soalan", "skema"):
        return []
    if "⟪PAGES⟫" in paper.text:
        return [Finding("V08", "error",
                        "page-count placeholder ⟪PAGES⟫ was never backfilled — run "
                        "_engine.render.integrate before delivery.",
                        evidence=paper.path.name)]
    m = re.search(r"MENGANDUNGI\s+\*{0,2}(\d+)\*{0,2}\s+MUKA SURAT", paper.text, re.IGNORECASE)
    if not m:
        return [Finding("V08", "error",
                        "no 'MENGANDUNGI n MUKA SURAT BERCETAK' declaration found.",
                        evidence=paper.path.name)]
    return [Finding("V08", "warn",
                    f"page count is hardcoded to {m.group(1)}; verify it against the "
                    f"rendered PDF.", evidence=m.group(0).strip())]


def v10_skema_arithmetic(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """The marking scheme has to add up — every section, and the whole paper.

    Added 2026-08-25 after a rewrite removed a competency unit from the practical
    without redistributing its marks: section 2 declared 60% in its heading while
    its criteria summed to 54%, and the paper totalled 94%. Both the writer and
    its self-check reported the totals as reconciled. Arithmetic is not something
    to take a writer's word for.

    Three things are checked per `## BAHAGIAN n — TITLE (w%)` section:
      * the `**% Pemberat: x%**` lines sum to the `w%` in the heading;
      * the `Jumlah Markah Bahagian n: ___/T` denominator equals the sum of the
        per-criterion `Markah Diperolehi: ___/m` denominators;
      * across sections, the declared weights total 100%.
    """
    if paper.kind != "skema":
        return []
    out: list[Finding] = []
    declared_total = 0.0
    weighted_sections = 0
    sections = re.split(r"^##\s*BAHAGIAN\s+", paper.text, flags=re.MULTILINE)[1:]
    for sec in sections:
        head = sec.splitlines()[0].strip()
        n = head.split()[0]
        # Two conventions are in use across these papers: "(60%)" and
        # "(60 MARKAH)". Both denote a share of a 100-point paper.
        head_pct = re.search(r"\((\d+(?:\.\d+)?)\s*(?:%|MARKAH)\)", head, re.IGNORECASE)
        if not head_pct:
            continue                                  # e.g. a candidate-details section
        target = float(head_pct.group(1))
        declared_total += target
        weighted_sections += 1

        crit = [float(x) for x in re.findall(r"\*\*%\s*Pemberat:\s*([\d.]+)\s*%\*\*", sec)]
        if crit and abs(sum(crit) - target) > 0.05:
            out.append(Finding("V10", "error",
                               f"Bahagian {n} heading declares {target:g}% but its "
                               f"criteria weights sum to {sum(crit):g}%.",
                               evidence=head))

        maxes = [int(x) for x in re.findall(r"Markah Diperolehi:\s*___/(\d+)", sec)]
        m = re.search(r"Jumlah Markah Bahagian\s+\d+:\s*___/(\d+)", sec)
        if m and maxes and int(m.group(1)) != sum(maxes):
            out.append(Finding("V10", "error",
                               f"Bahagian {n} totals ___/{m.group(1)} but its "
                               f"{len(maxes)} criteria are worth {sum(maxes)} marks.",
                               evidence=m.group(0)))

    if weighted_sections and abs(declared_total - 100.0) > 0.05:
        out.append(Finding("V10", "error",
                           f"the weighted sections total {declared_total:g}%, not 100%.",
                           evidence=paper.path.name))
    return out


def v09_weights(graph: NossGraph, profile: Profile, _paper=None) -> list[Finding]:
    """Practical and oral weights must total 100%."""
    total = profile.practical_weight + profile.oral_weight
    if total != 100:
        return [Finding("V09", "error",
                        f"practical_weight + oral_weight = {total}%, expected 100%.")]
    return []


# --------------------------------------------------------------------------- #
# V11–V14: the format contract in `_engine/FORMAT-jpk-ppa.md`, extracted from the
# four papers owned by jennifer@character.com.mx. Format was previously carried
# only in prose, which is how a paper reached her with no logo, no table rules and
# a different centre's name on the cover.
# --------------------------------------------------------------------------- #

# The Malay frame of a SOALAN. What is fixed is the **sequence**; the letters and
# some of the wording are not.
#
# Evidence — the six JPK-approved BEAUTY papers Jennifer owns:
#   L1 SET A/B : A. TEMPOH / TEMPOH MASA → B → C → D. SENARAI BAHAN →
#                E. SENARAI PERALATAN → F. KRITERIA PENILAIAN
#   L2, L3     : B. TEMPOH → C → D → E. SENARAI BAHAN →
#                F. PERALATAN DAN KELENGKAPAN → G. KRITERIA PENILAIAN
#
# Same author, same approved batch, two different letter schemes and two
# different wordings for the equipment section. An earlier version of this check
# asserted A–F as "fixed by the JPK format" — that would have failed four of her
# own approved papers. Pinning the letters was over-specification.
_SOALAN_SECTIONS = [
    ("TEMPOH", r"TEMPOH(?:\s+MASA)?"),
    ("KETERAMPILAN", r"KETERAMPILAN"),
    ("TUGASAN", r"TUGASAN"),
    ("SENARAI BAHAN", r"SENARAI BAHAN"),
    ("PERALATAN", r"(?:SENARAI\s+PERALATAN|PERALATAN\s+DAN\s+KELENGKAPAN)"),
    ("KRITERIA PENILAIAN", r"KRITERIA PENILAIAN"),
]

# Fixed JPK boilerplate a SKEMA must carry. Absent = the examiner's copy is not
# marked confidential and has no marking scale.
#
# The last two are in all six of her JPK-approved BEAUTY skema. Ours had the
# formula under four different labels — `Pengiraan:`, `Pengiraan setiap kriteria:`,
# `Pengiraan Pemarkahan Keseluruhan:` — and three of those divided by a literal
# `3` rather than `Markah Penuh`, which hard-codes the per-criterion maximum.
# None carried the footnote naming who sets the weighting.
_SKEMA_BOILERPLATE = [
    ("UNTUK KEGUNAAN PEMERIKSA SAHAJA", "examiner-only notice"),
    ("AMARAN", "confidentiality warning"),
    ("SKALA PEMARKAHAN", "0–3 marking scale"),
    ("Pengiraan Pemarkahan", "mark-calculation formula"),
    ("ditentukan oleh pakar", "footnote on who sets the weighting"),
]

# Strings that must never survive, each with the reason it is banned.
_FORBIDDEN = [
    (r"VIZTECH", "the name of a different accredited centre, copied in by mistake "
                 "from the reference sample"),
    (r"\bTerlibut\b", "misspelling of 'Terlibat', inherited from the reference sample"),
    (r"SENARAI BAHAN\s*/\s*DOCUMEN\b", "'DOCUMEN' is a typo in the reference paper; "
                                       "Malay is 'DOKUMEN'"),
]


def v11_malay_frame(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """A SOALAN carries the six Malay sections, in order.

    Checks presence and sequence only. The section letters are not checked because
    Jennifer's own approved papers use two different schemes — see the comment on
    `_SOALAN_SECTIONS`.
    """
    if paper.kind != "soalan":
        return []
    out: list[Finding] = []
    positions: list[int] = []
    for label, pattern in _SOALAN_SECTIONS:
        m = re.search(rf"^[#*\s]*[A-H]\.\s*{pattern}\b", paper.text,
                      re.IGNORECASE | re.MULTILINE)
        if not m:
            out.append(Finding("V11", "error",
                               f"section '{label}' is missing from the SOALAN.",
                               evidence=paper.path.name))
        else:
            positions.append(m.start())
    if len(positions) == len(_SOALAN_SECTIONS) and positions != sorted(positions):
        found = [lbl for lbl, _ in _SOALAN_SECTIONS]
        out.append(Finding("V11", "error",
                           "the six sections appear out of order; the sequence is "
                           + " → ".join(found) + ".", evidence=paper.path.name))
    return out


def v12_page_header(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """The paper reference code must be present and carry the right SET letter.

    Format `<NOSS>/<year>/<SET>/<nn>`, top right of every page. A Set B paper
    still carrying `/A/` is the single most likely leftover when a set is
    re-lettered — it happened on 2026-08-25.
    """
    if paper.kind not in ("soalan", "skema"):
        return []
    # Two NOSS code shapes: letters only (FB-018-3:2012) and letters plus digits
    # (N821-001-3:2020). Missing the second shape silently skipped this check on
    # three of the five subjects.
    codes = set(re.findall(
        r"\b([A-Z]{1,3}\d*-\d{3}-\d{1,2}(?::\d{4})?/\d{4}/([AB])/\d+)\b", paper.text))
    if not codes:
        return [Finding("V12", "error",
                        "no paper reference code (e.g. FB-018-3:2012/2026/B/01) "
                        "found; it belongs top-right on every page.",
                        evidence=paper.path.name)]
    out: list[Finding] = []
    if paper.set_id:
        for code, letter in codes:
            if letter != paper.set_id:
                out.append(Finding("V12", "error",
                                   f"this is SET {paper.set_id} but the reference "
                                   f"code says /{letter}/.", evidence=code))
    return out


def v13_skema_boilerplate(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """A SKEMA carries the examiner-only notice, the AMARAN and the marking scale."""
    if paper.kind != "skema":
        return []
    return [Finding("V13", "error",
                    f"SKEMA is missing the {desc} block ('{token}').",
                    evidence=paper.path.name)
            for token, desc in _SKEMA_BOILERPLATE
            if not re.search(re.escape(token), paper.text, re.IGNORECASE)]


def v16_supporting_doc_shape(graph: NossGraph, profile: Profile,
                             paper: Paper) -> list[Finding]:
    """The two supporting documents must be the JPK forms, not our own inventions.

    Added 2026-08-25 after a whole document type was found still in the wrong
    shape. The cover migration on that date covered `soalan` and `skema` only, so
    ten `equipment-verification` files and four `answer-sheet` files kept the
    structure the 2026-08-21 audit had listed as `未審` — the audit never opened
    them, and neither did the migration.

    * EQUIPMENT VERIFICATION is a one-page JPK form headed `JPK/PPA-PPT/SP/1:2022`
      with a `RATIO (P:C)` column and two `QUANTITY AVAILABLE` columns, one filled
      by the applicant and one by JPK. See `_engine/FORMAT-jpk-ppa.md` §8.
    * ASSESSMENT ANSWER SHEET reproduces the SOALAN's appendix forms **with the
      answers filled in** — it is the examiner's model answer, not a blank form.
      See §7.
    """
    if paper.kind == "equipment":
        missing = [token for token in ("JPK/PPA-PPT/SP", "RATIO", "QUANTITY AVAILABLE")
                   if token.lower() not in paper.text.lower()]
        if missing:
            return [Finding("V16", "error",
                            "equipment verification is not on the JPK form — missing "
                            + ", ".join(f"'{m}'" for m in missing) + ".",
                            evidence=paper.path.name)]
        return []

    if paper.kind == "answer-sheet":
        if not re.search(r"^[#*\s]*(APPENDIX|LAMPIRAN)\s+\d", paper.text, re.MULTILINE):
            return [Finding("V16", "error",
                            "answer sheet does not reproduce the SOALAN's appendix "
                            "forms — it should be the filled-in model answer, not a "
                            "blank form.", evidence=paper.path.name)]
        return []

    return []


def v17_appendix_label(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """Appendices are called `Appendix`, and one paper uses one word for them.

    Jennifer's own SOALAN says `Appendix` eight times and `Lampiran` never, so
    `Appendix` is the house word even though the surrounding frame is Malay —
    like `KPI` and `FAQ`, it is a term the centre keeps in English.

    Found 2026-08-25: the N821 papers referred to `APPENDIX 1A` fifty times and
    `LAMPIRAN 1` twice, in the same document. A candidate told to complete
    "Lampiran 2" has to work out that it is the thing headed "Appendix 2A".
    """
    en = len(re.findall(r"\bAppendix\b", paper.text, re.IGNORECASE))
    bm = len(re.findall(r"\bLampiran\b", paper.text, re.IGNORECASE))
    if en and bm:
        return [Finding("V17", "error",
                        f"appendices are labelled both ways in one paper — "
                        f"'Appendix' ×{en} and 'Lampiran' ×{bm}. Use 'Appendix'.",
                        evidence=paper.path.name)]
    if bm and not en:
        return [Finding("V17", "error",
                        f"appendices are labelled 'Lampiran' ×{bm}; the centre's "
                        f"own paper uses 'Appendix'.", evidence=paper.path.name)]
    return []


def v14_forbidden_strings(graph: NossGraph, profile: Profile, paper: Paper) -> list[Finding]:
    """Strings that are known-wrong wherever they appear."""
    out: list[Finding] = []
    for pattern, why in _FORBIDDEN:
        for i, line in enumerate(paper.lines, start=1):
            if re.search(pattern, line, re.IGNORECASE):
                out.append(Finding("V14", "error", f"forbidden string — {why}.",
                                   evidence=line.strip()[:140], line=i))
    return out


def v15_survey_data_reconciles(graph: NossGraph, profile: Profile,
                               paper: Paper) -> list[Finding]:
    """A summary table must agree with the raw data the candidate is handed.

    The task these papers set is "analyse the survey data provided", and the paper
    supplies both the raw respondent rows and a verified summary. If they disagree,
    a candidate who counts correctly produces answers the marking scheme calls
    wrong.

    Found on 2026-08-25: the Set B summary claimed 7 respondents preferred an
    air-conditioner, 10 were married with children and 15 intended to buy; the
    twenty raw rows said 6, 11 and 16. The model answer sheet had followed the
    summary, so the whole chain was internally consistent *except* against the one
    table the candidate actually works from.

    Recognises summary blocks by a `| <Label> | NO. | % |` header and reconciles
    each against the raw table column whose values carry the same labels.
    """
    if paper.kind != "soalan":
        return []

    tables = _markdown_tables(paper.text)
    raw = [t for t in tables if t["header"][:1] == ["NO."] and len(t["rows"]) >= 10]
    summaries = [t for t in tables if t["header"][1:3] == ["NO.", "%"]]
    if not raw or not summaries:
        return []

    total = max(len(t["rows"]) for t in raw)
    out: list[Finding] = []

    for s in summaries:
        label = s["header"][0]
        claimed = {}
        for row in s["rows"]:
            if len(row) >= 2 and row[1].isdigit():
                claimed[row[0]] = int(row[1])
        if not claimed:
            continue

        if sum(claimed.values()) != total:
            out.append(Finding("V15", "error",
                               f"summary '{label}' counts total {sum(claimed.values())} "
                               f"but the raw data has {total} respondents.",
                               evidence=label))

        for row in s["rows"]:
            if len(row) >= 3 and row[1].isdigit():
                want = round(int(row[1]) / total * 100)
                got = row[2].replace("%", "").strip()
                if got.replace(".", "").isdigit() and abs(float(got) - want) > 0.6:
                    out.append(Finding("V15", "error",
                                       f"summary '{label}' row '{row[0]}': "
                                       f"{row[1]}/{total} is {want}%, not {row[2]}.",
                                       evidence=" | ".join(row)))

        # Reconcile against whichever raw column uses these labels.
        for t in raw:
            for i, col in enumerate(t["header"]):
                values = [r[i] for r in t["rows"] if i < len(r)]
                if not values or not (set(claimed) & set(values)):
                    continue
                actual = Counter(values)
                for key in set(claimed) | set(actual):
                    if claimed.get(key, 0) != actual.get(key, 0):
                        out.append(Finding("V15", "error",
                                           f"'{label}' → '{key}': summary says "
                                           f"{claimed.get(key, 0)}, the raw '{col}' "
                                           f"column has {actual.get(key, 0)}.",
                                           evidence=f"{label} / {col}"))
                break
    return out


def _markdown_tables(text: str) -> list[dict]:
    """Split markdown into pipe tables, each as {header, rows}."""
    tables, current = [], []
    for line in text.splitlines():
        if line.lstrip().startswith("|"):
            current.append(line)
        elif current:
            tables.append(current)
            current = []
    if current:
        tables.append(current)

    out = []
    for block in tables:
        cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in block]
        if len(cells) < 3:
            continue
        out.append({"header": cells[0], "rows": cells[2:]})
    return out


# --------------------------------------------------------------------------- #

def _section(text: str, *heads: str) -> str | None:
    """Return the body under the first heading matching any of `heads`.

    Sections in these papers are `**C. TUGASAN**` / `## C. TUGASAN` / `C. TUGASAN`.
    The body runs to the next single-letter section marker.
    """
    for head in heads:
        m = re.search(rf"^[#*\s]*[A-Z]\.\s*{head}\b.*$", text, re.IGNORECASE | re.MULTILINE)
        if not m:
            continue
        start = m.end()
        nxt = re.search(r"^[#*\s]*[A-Z]\.\s+[A-Z]", text[start:], re.MULTILINE)
        return text[start:start + nxt.start()] if nxt else text[start:]
    return None


def _tugasan_section(text: str) -> str | None:
    return _section(text, "TUGASAN")


def _oral_section(text: str) -> str | None:
    body = _section(text, "SESI SOAL JAWAB", "SOAL JAWAB", "SOALAN LISAN")
    if body:
        return body
    m = re.search(r"SOAL\s*[- ]?\s*JAWAB", text, re.IGNORECASE)
    return text[m.start():] if m else None


# Checks that look at the profile alone; running them once per paper would emit
# the same finding N times.
GRAPH_LEVEL = [
    v01_profile_covers_graph,
    v09_weights,
]

# Checks that need a paper to look at.
PAPER_LEVEL = [
    v02_practical_cu_has_task,
    v03_oral_cu_has_question,
    v04_no_excluded_refs,
    v05_monolingual,
    v06_cover_cu_list,
    v07_duration,
    v08_page_declaration,
    v10_skema_arithmetic,
    v11_malay_frame,
    v12_page_header,
    v13_skema_boilerplate,
    v14_forbidden_strings,
    v15_survey_data_reconciles,
    v16_supporting_doc_shape,
    v17_appendix_label,
]

VALIDATORS = GRAPH_LEVEL + PAPER_LEVEL


def run(graph: NossGraph, profile: Profile, papers: list[Paper]) -> list[Finding]:
    findings: list[Finding] = []
    for fn in GRAPH_LEVEL:
        findings += fn(graph, profile, None)
    for fn in PAPER_LEVEL:
        for paper in papers:
            findings += fn(graph, profile, paper)
    return findings
