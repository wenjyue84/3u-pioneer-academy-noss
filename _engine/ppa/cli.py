"""Command line for the PPA engine.

    uv run python -m _engine.ppa.cli validate --all
    uv run python -m _engine.ppa.cli validate --profile _engine/profiles/fb-018-3.json
    uv run python -m _engine.ppa.cli plan     --profile _engine/profiles/fb-018-3.json

`validate` exits 1 when any finding has severity `error`, so it can gate a build.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from .schema import NossGraph, Profile
from .validate import Paper, run

ROOT = Path(__file__).resolve().parents[2]
PROFILE_DIR = ROOT / "_engine" / "profiles"
REPORT_DIR = ROOT / "_engine" / "reports"
PAPER_DIR = ROOT / "output" / "jennifer-ppa-soalan"

SEV_ORDER = {"error": 0, "warn": 1}


def _papers_for(profile: Profile) -> list[Paper]:
    """Every generated markdown belonging to this profile.

    Matched by the profile filename stem, which is also the paper filename prefix
    (`fb-018-3` → `fb-018-3-set-a-soalan.md`). Keeping the two in sync by
    convention is deliberate: a profile with no papers should be visible as such,
    not silently validate clean.
    """
    stem = profile.noss_code.split(":")[0].lower().replace("_", "-")
    return [Paper.load(p) for p in sorted(PAPER_DIR.glob(f"{stem}-*.md"))]


def _load(profile_path: Path) -> tuple[NossGraph, Profile]:
    profile = Profile.load(profile_path)
    graph_path = ROOT / profile.graph_file
    if not graph_path.exists():
        sys.exit(f"profile {profile_path.name} points at a missing graph: {profile.graph_file}")
    return NossGraph.load(graph_path), profile


def cmd_validate(args: argparse.Namespace) -> int:
    profiles = (sorted(PROFILE_DIR.glob("*.json")) if args.all
                else [Path(args.profile)])
    if not profiles:
        sys.exit(f"no profiles found in {PROFILE_DIR}")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    all_rows: list[dict] = []
    exit_code = 0

    for pp in profiles:
        graph, profile = _load(pp)
        papers = ([Paper.load(args.paper)] if args.paper else _papers_for(profile))
        if not papers:
            print(f"  {profile.noss_code}: no papers found — nothing validated")
            all_rows.append({"noss": profile.noss_code, "check": "—",
                             "severity": "warn", "message": "no papers found",
                             "paper": ""})
            continue

        findings = run(graph, profile, papers)
        findings.sort(key=lambda f: (SEV_ORDER.get(f.severity, 9), f.check))
        errors = [f for f in findings if f.severity == "error"]
        warns = [f for f in findings if f.severity == "warn"]

        status = "FAIL" if errors else "ok"
        print(f"{status:>4}  {profile.noss_code}  "
              f"{len(papers)} papers · {len(errors)} errors · {len(warns)} warnings")
        for f in findings[: args.limit]:
            loc = f":{f.line}" if f.line else ""
            print(f"        [{f.check} {f.severity}]{loc} {f.message}")
            if f.evidence:
                print(f"              ↳ {f.evidence}")
        if len(findings) > args.limit:
            print(f"        … {len(findings) - args.limit} more (see report)")

        all_rows += [dict(noss=profile.noss_code, **f.as_dict()) for f in findings]
        if errors:
            exit_code = 1

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = REPORT_DIR / f"validate-{stamp}.json"
    out.write_text(json.dumps(all_rows, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")
    print(f"\nreport: {out.relative_to(ROOT)}")
    return exit_code


def cmd_plan(args: argparse.Namespace) -> int:
    graph, profile = _load(Path(args.profile))
    print(f"{graph.noss_code}  {graph.noss_title}  (Level {graph.level})")
    print(f"centre     : {profile.centre.name}")
    print(f"language   : {profile.language}")
    print(f"duration   : {profile.duration_min_minutes}–{profile.duration_max_minutes} min")
    print(f"weights    : amali {profile.practical_weight}% · lisan {profile.oral_weight}%")
    print()
    print(f"{'CU':<5} {'mode':<10} {'WA':>3} {'PC':>3}  title")
    for cu in graph.competency_units:
        mode = profile.cu_modes.get(cu.code, "—")
        mark = {"practical": "▓", "oral": "▒", "excluded": "·"}.get(mode, "?")
        print(f"{cu.code:<5} {mark} {mode:<8} {len(cu.work_activities):>3} "
              f"{cu.pc_count:>3}  {cu.title(profile.language)}")
    print()
    print(f"practical : {', '.join(profile.practical_cus) or '—'}")
    print(f"oral      : {', '.join(profile.oral_cus) or '—'} "
          f"({profile.oral_question_count} soalan)")
    print(f"excluded  : {', '.join(profile.excluded_cus) or '—'}")
    for s in profile.sets:
        print(f"\nSET {s.set_id}: {s.industry} — {s.company} — {s.product}")
        if s.notes:
            print(f"          {s.notes}")
    return 0


def cmd_lint(args: argparse.Namespace) -> int:
    """Profile-free checks — the ones that need no decision from the course owner.

    Which competency units to assess is the client's call, so most validators
    cannot run until a profile exists. Language, marks arithmetic and the printed
    page declaration are not opinions: they are wrong or they are not. This lets a
    paper be triaged before anyone has decided anything.
    """
    from .validate import (Paper, v05_monolingual, v08_page_declaration,
                           v10_skema_arithmetic, v11_malay_frame, v12_page_header,
                           v13_skema_boilerplate, v14_forbidden_strings,
                           v15_survey_data_reconciles,
                           v16_supporting_doc_shape,
                           v17_appendix_label)

    class _BM:
        """Minimal stand-in for a Profile.

        These checks read only `language`, so a paper can be triaged before its
        competency units have been chosen. `bm_frame_en_body` is the centre's
        house style; using plain `bm` here would flag every English sentence in
        papers that are correctly written that way.
        """
        language = "bm_frame_en_body"

    # Only actual papers. README.md, BASELINE.md and the audit notes live in the
    # same directory and are prose about the papers, not papers.
    is_paper = re.compile(r"-(soalan|skema|answer-sheet|equipment-verification)$")
    papers = ([Paper.load(p) for p in args.paper] if args.paper
              else [Paper.load(p) for p in sorted(PAPER_DIR.glob("*.md"))
                    if is_paper.search(p.stem)
                    and (not args.only or args.only in p.stem)])
    if not papers:
        sys.exit("no papers to lint")

    checks = [v05_monolingual, v08_page_declaration, v10_skema_arithmetic,
              v11_malay_frame, v12_page_header, v13_skema_boilerplate,
              v14_forbidden_strings, v15_survey_data_reconciles,
              v16_supporting_doc_shape, v17_appendix_label]

    by_file: dict[str, list] = {}
    for paper in papers:
        found = [f for check in checks for f in check(None, _BM, paper)]
        if found:
            by_file[paper.path.name] = found

    dupes = _duplicate_reference_codes(papers)
    total = sum(len(v) for v in by_file.values()) + len(dupes)
    print(f"{len(papers)} papers linted · {total} findings in {len(by_file)} files\n")
    cols = ["V05", "V08", "V10", "V11", "V13", "V15", "V16", "V17"]
    head = {"V05": "bahasa", "V08": "muka", "V10": "markah", "V11": "rangka",
            "V13": "amaran", "V15": "data", "V16": "borang", "V17": "lampiran"}
    print(f"{'file':<52}" + "".join(f"{c + ' ' + head[c]:>12}" for c in cols))
    for paper in papers:
        f = by_file.get(paper.path.name, [])
        counts = {c: sum(1 for x in f if x.check == c) for c in cols}
        if any(counts.values()):
            print(f"{paper.path.name:<52}" +
                  "".join(f"{counts[c] or '·':>12}" for c in cols))

    for line in _critical_item_scored(papers):
        print(line)

    for line in _appendix_crossrefs(papers):
        print(line)

    for line in _equipment_mismatches(papers):
        print(line)

    if dupes:
        print("\nDUPLICATE PAPER REFERENCE CODES")
        for code, names in dupes.items():
            print(f"  {code}")
            for n in names:
                print(f"      {n}")
    return 1 if total else 0


def _critical_item_scored(papers: list[Paper]) -> list[str]:
    """A critical item declared in the SOALAN must be recordable in the SKEMA.

    Every one of Jennifer's six JPK-approved BEAUTY marking schemes opens with
    `Perkara kritikal (Wajib Lulus)` and a `Terima / Tidak Terima` box. It is the
    pass/fail gate: a candidate who falsifies the source data is not competent
    regardless of marks.

    Found 2026-08-25: the two N821 papers declared a critical item in section F of
    the SOALAN, and their marking schemes had nowhere to record it — `BAHAGIAN 1`
    was candidate details. The gate was announced and then not enforced, which is
    the same shape as the E01 defect: declared but unassessed.
    """
    by_set: dict[str, dict[str, Paper]] = {}
    for p in papers:
        by_set.setdefault(re.sub(r"-(soalan|skema|answer-sheet|equipment-verification)$",
                                 "", p.path.stem), {})[p.kind] = p

    out: list[str] = []
    for set_id, docs in sorted(by_set.items()):
        soalan, skema = docs.get("soalan"), docs.get("skema")
        if not soalan or not skema:
            continue
        declares = re.search(r"Perkara\s+Kritikal", soalan.text, re.IGNORECASE)
        scores = re.search(r"Perkara\s+Kritikal", skema.text, re.IGNORECASE)
        if declares and not scores:
            out.append(f"      {set_id}: soalan declares a critical item; "
                       f"the skema has nowhere to record it")
    return (["\nCRITICAL ITEM NOT SCORED (soalan declares, skema omits)"] + out
            if out else [])


def _appendix_crossrefs(papers: list[Paper]) -> list[str]:
    """Every appendix the answer sheet reproduces must exist in its own SOALAN.

    The answer sheet is the examiner's key: each block says "this is what
    Appendix N should look like when completed". If it names an appendix the
    paper does not contain, the examiner is sent looking for something that is
    not there.

    Found 2026-08-25: a G471 answer sheet reproduced `APPENDIX 3A` and
    `APPENDIX 3B`. The paper has `APPENDIX 3` containing sub-sections `A.` and
    `B.` — a reasonable reading of the content, but `Appendix 3A` appears nowhere
    in the paper an examiner is holding.
    """
    by_set: dict[str, dict[str, Paper]] = {}
    for p in papers:
        by_set.setdefault(re.sub(r"-(soalan|skema|answer-sheet|equipment-verification)$",
                                 "", p.path.stem), {})[p.kind] = p

    pat = re.compile(r"APPENDIX\s+(\d+[A-Z]?)", re.IGNORECASE)
    out: list[str] = []
    for set_id, docs in sorted(by_set.items()):
        soalan, answers = docs.get("soalan"), docs.get("answer-sheet")
        if not soalan or not answers:
            continue
        in_paper = {m.upper() for m in pat.findall(soalan.text)}
        claimed = {m.upper() for m in pat.findall(answers.text)}
        missing = sorted(claimed - in_paper)
        if missing:
            out.append(f"      {set_id}: answer sheet cites "
                       f"{', '.join('Appendix ' + m for m in missing)}, "
                       f"absent from the soalan")
    return (["\nAPPENDIX CROSS-REFERENCE (answer sheet vs soalan)"] + out
            if out else [])


def _equipment_mismatches(papers: list[Paper]) -> list[str]:
    """The equipment-verification checklist must match the SOALAN's sections D and E.

    The verification form is what an officer walks the room with. If the SOALAN
    asks for a printer and the checklist does not list one, nobody checks there is
    a printer; if the checklist lists something the paper never uses, the centre
    is asked to produce equipment for no reason.

    Cross-document, so it cannot live in the per-paper V-series. Compares item
    counts rather than wording — the two documents legitimately phrase things
    differently — and reports the gap for a human to read.
    """
    def count_rows(text: str, *headings: str) -> int:
        total = 0
        for head in headings:
            m = re.search(rf"^[#*\s]*[A-Z]\.\s*{head}", text, re.I | re.M)
            if not m:
                continue
            body = text[m.end():]
            nxt = re.search(r"^[#*\s]*[A-Z]\.\s+[A-Z]", body, re.M)
            if nxt:
                body = body[:nxt.start()]
            total += len([r for r in body.splitlines()
                          if re.match(r"^\s*\|\s*\d+\s*\|", r)])
        return total

    by_set: dict[str, dict[str, Paper]] = {}
    for p in papers:
        by_set.setdefault(re.sub(r"-(soalan|skema|answer-sheet|equipment-verification)$",
                                 "", p.path.stem), {})[p.kind] = p

    out: list[str] = []
    for set_id, docs in sorted(by_set.items()):
        soalan, equip = docs.get("soalan"), docs.get("equipment")
        if not soalan or not equip:
            continue
        want = count_rows(soalan.text, "SENARAI BAHAN", "SENARAI PERALATAN")
        have = len([r for r in equip.text.splitlines()
                    if re.match(r"^\s*\|\s*\d+\s*\|", r)])
        if want and have and want != have:
            out.append(f"      {set_id}: soalan lists {want} items, "
                       f"equipment-verification checks {have}")
    return (["\nEQUIPMENT LIST MISMATCH (soalan §D+§E vs verification form)"] + out
            if out else [])


def _duplicate_reference_codes(papers: list[Paper]) -> dict[str, list[str]]:
    """Two *different papers* must never carry the same reference code.

    The four documents of one set — soalan, skema, answer sheet, equipment
    verification — share a code by design; Jennifer's own set does exactly that.
    So the unit of comparison is the set, not the file.

    Found 2026-08-25: the FB-018-45 Level 4 and Level 5 papers both printed
    `FB-018-45:2012/2026/A/01`. The NOSS code family covers both levels and
    nothing in the code distinguished them, so two different examinations were
    identified identically on every page and on the PPL's sign-off.

    Cross-file, so it cannot live in the per-paper V-series.
    """
    pat = re.compile(r"\b([A-Z]{1,3}\d*-\d{3}-\d{1,2}(?::\d{4})?/\d{4}/[AB]/\d+)\b")
    seen: dict[str, set[str]] = {}
    for paper in papers:
        m = pat.search(paper.text)
        if not m:
            continue
        set_id = re.sub(r"-set-[ab].*$", "", paper.path.stem)
        seen.setdefault(m.group(1), set()).add(set_id)
    return {code: sorted(ids) for code, ids in seen.items() if len(ids) > 1}


def cmd_worksheet(args: argparse.Namespace) -> int:
    from .worksheet import render_worksheet, write_all

    out_dir = ROOT / args.out
    if args.graph:
        gp = Path(args.graph)
        graph = NossGraph.load(gp)
        pf = PROFILE_DIR / gp.name
        existing = Profile.load(pf) if pf.exists() else None
        out_dir.mkdir(parents=True, exist_ok=True)
        dest = out_dir / f"borang-pemilihan-cu-{gp.stem}.md"
        dest.write_text(render_worksheet(graph, existing), encoding="utf-8")
        written = [dest]
    else:
        written = write_all(ROOT / "_engine" / "graph", PROFILE_DIR, out_dir)

    for p in written:
        print(f"wrote {p.relative_to(ROOT)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="ppa", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate", help="check generated papers against their profile")
    v.add_argument("--profile", help="path to a profile JSON")
    v.add_argument("--all", action="store_true", help="validate every profile")
    v.add_argument("--paper", help="validate a single paper instead of the whole set")
    v.add_argument("--limit", type=int, default=25, help="findings printed per profile")
    v.set_defaults(func=cmd_validate)

    p = sub.add_parser("plan", help="print the assessment plan a profile implies")
    p.add_argument("--profile", required=True)
    p.set_defaults(func=cmd_plan)

    ln = sub.add_parser("lint",
                        help="profile-free checks: language, marks, page declaration")
    ln.add_argument("--paper", nargs="*", help="papers to lint (default: all)")
    ln.add_argument("--only", help="substring filter on the filename")
    ln.set_defaults(func=cmd_lint)

    w = sub.add_parser("worksheet",
                       help="generate the CU-selection form for the course owner")
    w.add_argument("--all", action="store_true", help="one sheet per graph")
    w.add_argument("--graph", help="a single graph JSON")
    w.add_argument("--out", default="_engine/worksheets")
    w.set_defaults(func=cmd_worksheet)

    args = ap.parse_args(argv)
    if args.cmd == "validate" and not args.all and not args.profile:
        ap.error("validate needs --profile or --all")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
