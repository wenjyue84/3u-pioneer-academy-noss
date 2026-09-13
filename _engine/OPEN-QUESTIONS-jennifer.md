# Open questions for Jennifer

Everything here blocks a correct submission and **cannot be answered from the
documents we hold**. Each carries the evidence for why it is open, so it can be
asked once and closed.

Status as of 2026-08-26 00:25 MYT. N821 CU selection answered 00:04.

---

## 1. Competency-unit selection — 5 of 6 NOSS still unanswered ⟪BLOCKING⟫

Only FB-018-3 has a decision (C01/C04/C05 practical · C02/C03/C06 oral · E01
excluded, from her message of 2026-08-25 00:02).

The other five papers still assess **every** unit in the standard — the exact
defect she raised about Office Administration on 2026-08-24 23:15:

> 我现在刚刚开了那个 office administration 的来看，我看到他也是全部的 CU 都写下去…
> 我觉得这个是我们要先想的，因为我们要配合到我们的教学，所以我们要告诉 AI，不是给 AI 自己去选。

| NOSS | Units in the standard | Units the paper currently assesses |
|---|---|---|
| N821-001-3:2020 Office Administration | 7 | **C01 C02 C05 C06 (amali) · C03 C04 C07 (lisan)** ✅ 2026-08-26 |
| M731-001-3:2021 Digital Marketing Operation | 6 | 6 |
| G471-001-3:2018 Retail Outlet Operations | 5 | 5 |
| FB-018-45 Level 4 | 8 | 8 |
| FB-018-45 Level 5 | 8 | 8 |

A three-hour practical realistically holds **two units assessed practically**
(~48 min per station + 30 min oral + 10 min handover). Seven does not fit; that
is arithmetic, not an opinion.

**Ask:** the completed selection form per NOSS —
`_engine/worksheets/borang-pemilihan-cu-*.md`. Each unit marked `amali`, `lisan`
or `tiada`.

**Until answered:** the papers keep all units, and no unit is bolded on the cover
(bolding *is* the selection — see `_engine/FORMAT-jpk-ppa.md` §3).

---

## 2. FB-018-45 — the competency-unit codes are unattested ⟪BLOCKING⟫

The CoCU PDFs we hold (`raw/noss-character/fb018-45-L4-cocu.pdf`, `…-L5-cocu.pdf`)
have a **blank `CU Code` column on every page**, and the NOSS code itself is not
printed anywhere in them. Verified by extracting the full text: no `C0n`, no
`M0n`, no `FB-018-4…` string occurs.

So two different inventions are in circulation:

| Source | Codes used | Evidence |
|---|---|---|
| The 2026-08-24 papers | `M01`–`M08` | none |
| `_engine/graph/fb-018-4.json` | `C01`–`C08` | none — carried over from the Level 3 sibling |

**Ask:** the full NOSS document for FB-018-45 (not the CoCU extract), or her
confirmation of the official unit codes and the exact NOSS code and year.

---

## 3. FB-018-45 — Level 4 and Level 5 share one paper reference code

Both levels print `FB-018-45:2012/2026/A/01` (and `/B/01`). Two different
examinations identified identically on every page and on the PPL's sign-off.

This follows from #2: the code family covers both levels and nothing in it
distinguishes them. Detected by
`uv run python -m _engine.ppa.cli lint` → `DUPLICATE PAPER REFERENCE CODES`.

**Ask:** how the two levels should be distinguished — a different NOSS code per
level, or a serial (`/01` for L4, `/02` for L5)?

**Interim:** left as-is rather than guessing, because a fabricated code on a
submitted paper is worse than a visible collision.

---

## 4. Her SET A for FB-018-3 (property scenario)

2026-08-24 23:28:

> S&M 我已经做好 1 set property 的，我们继续使用，现在再修改那个卖电器的，作为 Set B 考题

The four files she owns in the Drive folder **are** that property set
(`Seri Harmoni Residence`) — but they carry the defects listed in §6 below and
predate the 2026-08-25 00:02 decisions (E01 is still on their cover; C02 is still
practical).

**Ask:** should we rebuild her SET A to match the corrected SET B — same three
practical units, no E01, same format — keeping her property scenario and data?

---

## 5. Accredited-centre name — confirm in writing

Her own papers say `CHARACTER INTERNATIONAL ACADEMY SDN. BHD.` Ours said
`VIZTECH TRADING SDN. BHD.`, inherited by mistake from a reference sample; that
is a **different accredited centre**. Corrected everywhere on 2026-08-25 and
blocked from returning by validator V14.

**Ask:** confirm the centre name and supply the `Kod Pusat` — the cover field is
`KOD DAN NAMA PUSAT BERTAULIAH/SYARIKAT` and we only have the name.

---

## 6. Defects in her own reference papers — for her to fix before submission

Not our files. Raised 2026-08-25 16:19.

| File | Declared | Actual |
|---|---|---|
| `SOALAN PENILAIAN AMALI PPT （SET A).pdf` | 13 pages | **14** |
| `SKEMA PENILAIAN AMALI PPT-PPA (SET A).pdf` | 14 pages | **11** |

Also in those two: `E01 INVENTORY CONTROL` is listed on both covers but scores
nothing anywhere in the skema; `Terlibut` appears for `Terlibat`; and the SOALAN
heads section D `SENARAI BAHAN / DOCUMEN` where Malay is `DOKUMEN`.

---

## 7. Does an oral-only assessment satisfy JPK for a *practical* paper? ⟪PPL⟫

Her structure — and now ours — assesses three units by oral question alone,
carrying 20% of the marks. This is a **Penilaian Amali**. Whether oral evidence
alone is acceptable for those units is a question for the PPL or JPK, not
something derivable from the documents.

Raised in the 2026-08-21 audit as R1 and still unanswered.

