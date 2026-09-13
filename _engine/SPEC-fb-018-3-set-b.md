# Rewrite spec — FB-018-3:2012 SET B (Sales & Marketing Operation, Level 3)

**Supersedes the version of this file written 2026-08-25 morning.** That version
converted the paper to Bahasa Malaysia throughout. On the afternoon of the same
day the four documents Jennifer actually owns were downloaded and read, and they
are not written that way. The format contract now lives in
`_engine/FORMAT-jpk-ppa.md`, extracted from those files. **Read it before this.**

Authority, in order:
1. `_engine/FORMAT-jpk-ppa.md` — how the paper must look. Derived from files whose
   Drive owner is `jennifer@character.com.mx`; local copies in
   `raw/jennifer-authoritative-fb018-3/`.
2. `_engine/profiles/fb-018-3.json` — which competency units, what language, how long.
3. `_engine/graph/fb-018-3.json` — what the NOSS actually says.
4. Jennifer's WhatsApp of 2026-08-25 00:02 and her voice notes of 2026-08-24 22:49–23:28.

---

## 0. Start from the right file

`output/jennifer-ppa-soalan/_archive-2026-08-25-superseded/fb-018-3-set-b-soalan-automotive.md`
is a **structural mirror of Jennifer's own SET A**: same six Malay section
headings, same three tasks mapped to C01 / C05 / C04, no E01, no direct-sales
pitch, same five appendices, English body. Its only defect is the scenario — she
said on 2026-08-24 23:13 that vehicle sales has its own NOSS and cannot be used
here.

So: restore that structure and change the scenario. Do **not** start from the
all-Malay version currently at `fb-018-3-set-b-soalan.md`; that one has to be
undone, not extended.

## 1. Scenario

| | Set A (Jennifer's, keep as is) | Set B (this paper) |
|---|---|---|
| Industry | Property sales | Consumer electronics retail |
| Company | Seri Harmoni Residence | **Sinar Elektronik Sdn. Bhd.** |
| Product | Residential units | TV, air-conditioner, refrigerator, washing machine |

`Dinamik Auto Gallery` and every automotive term go. `Viztech` must not appear
anywhere — it is a different accredited centre's name (validator V14 blocks it).

The two sets are **parallel forms**: identical competency units, identical time
budget, identical mark split, identical section structure. Only the scenario,
the survey data and the product figures differ.

## 2. Language — Malay frame, English body

Per `_engine/FORMAT-jpk-ppa.md` §1. Section headings, table column headers, cover
labels and fixed JPK boilerplate in Malay; everything the paper actually says in
English. **Never both in one sentence** — no `Tinjauan Pasaran / Market Survey`
pairs, no bracketed glosses. That pairing was Jennifer's complaint, not the Malay
frame itself.

## 3. Competency units

| Unit | Mode | Where |
|---|---|---|
| C01 MARKET & PRODUCT SURVEY | amali | TUGASAN activity I |
| C05 ONLINE SALES | amali | TUGASAN activity II |
| C04 SELF SALES PERFORMANCE ASSESSMENT | amali | TUGASAN activity III |
| C02 DIRECT / RETAIL SALES | lisan | oral 5.1–5.4 |
| C03 AFTER SALES SERVICE | lisan | oral 5.5–5.7 |
| C06 PRODUCT MARKETING | lisan | oral 5.8–5.10 |
| E01 INVENTORY CONTROL | **excluded** | nowhere, cover included |

On the cover, the three practical units are **bold**; the three oral units are
not. That is how Jennifer's own paper encodes it (§3 of the format contract).

## 4. Cover

Rebuild as the single bordered table in `_engine/FORMAT-jpk-ppa.md` §2 — logo cell
top-left, JPK address top-right, then centre name, paper title, competency code,
unit list, candidate block. Below the table: `Arahan kepada calon:` (six items),
the printed-page declaration, and the bordered PPL signature box.

Centre: `CHARACTER INTERNATIONAL ACADEMY SDN. BHD.`

## 5. Page header

`FB-018-3:2012/2026/B/01` — note **B**, not A. Top right of every page; page number
centred at the bottom. Validator V12 checks the set letter matches the filename.

## 6. Duration

`A. TEMPOH MASA` → `: 3 HOURS`. Keep the time-budget table under it (45 + 50 + 45
practical, 30 oral, 10 handover = 180 minutes) — it is the evidence that the paper
is completable in the 2.5–3 hours Jennifer specified. Malay column headers,
English row labels.

## 7. Page count

`**KERTAS INI MENGANDUNGI ⟪PAGES⟫ MUKA SURAT BERCETAK**` for the SOALAN;
`**SKEMA PEMARKAHAN INI MENGANDUNGI ⟪PAGES⟫ MUKA SURAT BERCETAK TERMASUK MUKA
HADAPAN**` for the SKEMA. `_engine.render.integrate` backfills the real number.
Both of Jennifer's own papers declare the wrong count — do not copy hers.

## 8. SKEMA additions

Add the three blocks our version is missing (format contract §6): the
`UNTUK KEGUNAAN PEMERIKSA SAHAJA` notice, the `AMARAN` confidentiality paragraph,
and the `SKALA PEMARKAHAN` 0–3 scale with the `Markah Diperolehi / Markah Penuh ×
% Pemberat` formula. Verbatim Malay as quoted there.

Marks: amali 80% (Bahagian 2 = 60, 3 = 10, 4 = 10) + lisan 20% = 100%. Section
totals must equal the sum of their criteria maxima. Validator V10 checks this;
it exists because a previous rewrite reported "totals reconcile" over a paper
that totalled 94%.

`Terlibat`, never `Terlibut`.

## 9. ASSESSMENT ANSWER SHEET — different document from ours

Per format contract §7: it is **not** a blank form. It reproduces Appendices 3, 4
and 5 with the correct answers filled in, as the examiner's reference. Rebuild it
that way against the Sinar Elektronik scenario, so that every answer is derivable
from the data printed in the SOALAN's appendices.

## 10. EQUIPMENT VERIFICATION — one page, JPK form

Per format contract §8. Header `JPK/PPA-PPT/SP/1:2022` top right. Title
`VERIFICATION FORM FOR PPA-PPT EQUIPMENT CHECK`. Header block (NOSS code, SET,
Competency, Critical Item, Assessment Duration), then the numbered checklist with
`RATIO (P:C)` and the two `QUANTITY AVAILABLE` columns — one filled by the
applicant, one by JPK. Signature and date at the foot. **One page.**

The checklist must match sections D and E of the SOALAN item for item. Read them;
do not reconstruct from memory.

## 11. Acceptance

```bash
uv run python -m _engine.ppa.cli validate --profile _engine/profiles/fb-018-3.json
```

Zero errors. V08 warnings about a hardcoded page count are expected until
`_engine.render.integrate` has run.

Then render and look at two pages as images. Two defects in the last round were
invisible to all validators and obvious to the eye.
