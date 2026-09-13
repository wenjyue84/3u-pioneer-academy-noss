# WhatsApp sends — 2026-07-29 (all delivered)

Periskope timed out mid-run at ~16:50 MYT and recovered by ~19:35. The timeouts were false
alarms: the sends had gone through. Verified afterwards by reading each chat back — nothing
was double-sent.

**Lesson for next time:** a Periskope timeout is not a failed send. Always read the chat back
and check `ack` / `delivery_info` before resending. `ack:3` = read, `ack:2` = delivered.

---

## 商学院ADI IT Program — `120363401205074304@g.us`

Six messages to Jennifer, all delivered (first one `ack:3`, read).

1. `Jennifer digital marketing 这个 program 就你们用 Character 的 license 去 apply，你跟你的 staff 处理 portal 那边`
2. `我看了 ptpk 的 garis panduan，申请人一定要有 JPK pentauliahan，要 attach Sijil Akuan Pentauliahan 加每个 program 的 surat kelulusan`
3. `Character 的 sijil 跟 Kod Pusat 拍给我看一下，我要 confirm accredit 了哪些 program`
4. `我们 proposal 写的 DM-001-3:2026 这个 code 我查不到。JPK 真正有的是 M731-001-3:2021 Digital Marketing Operation。你的 license 是挂哪个 code？`
5. `3U 跟 prisma 没有 pentauliahan，只能做 industry partner 签 LOC/MOA，那个不用 license`
6. `deadline 是 31/7 tengah hari 不是下午`

**Awaiting from Jennifer:** photo of Character's Sijil Akuan Pentauliahan + Kod Pusat, and
which NOSS code her licence is registered under. Everything else is blocked on this.

---

## (Internal) PTPK TBT 2026 Submission — `120363427502767408@g.us`

Created 2026-07-29 08:42 UTC. Invite: https://chat.whatsapp.com/invite/B7KMHS8iyIu38NjtwiHWqA

Members (5): Jay `60127088789` (admin) · Jas Kae Shyong (Prisma Director) `60167166663` ·
Yashini (Pure Ocean) `60184007417` · Chang SC (VecTech / AutoCount) `601117758060` ·
Dhai (Prisma Lead Dev) `601139751613`

> Note: Dhai was not in the three numbers passed to the create/add calls — Periskope pulled him
> in as an internal org member. Flagged to Jay.

Messages sent, all `ack:3` delivered to 4 recipients:
1. Opener — "Opened this group for the PTPK TBT 2026 grant submission."
2. Background briefing (what the scheme is, the Prisma eligibility problem, source links)
3. Assignment to Yashini (@mention confirmed in `mentioned_ids`) + the AI-caution warning
4. Ask to Kae Shyong for his TTT sijil number
5. Ask to Mr Chang whether VecTech can sign as industry partner for AI for Admin

**Chang SC asked "what's this grant?" at 16:49 MYT** before the briefing went out — the
background message answers him.

---

## Still open

**Proposal drafts not yet delivered to Yashini.** They are local Markdown; Periskope media
sends need a public URL, so they cannot go over WhatsApp from here. Needs a channel decision —
Google Drive upload + share link, or email (Yashini's address unknown).

- `proposals/ai-dm-proposal.md`
- `proposals/ai-admin-proposal.md`
- `proposals/ai-mfg-proposal.md`
- `proposals/ai-iso-proposal.md`
- `ai-digital-marketing/proposal-ptpk-skim-tbt-2026.md` (BM formal version)
- `wiki/08-jennifer-voicenotes-20260724.md` (machine transcription — flag as unverified)

Baseline copies from before the 2026-07-29 edits: `_archive/proposals-baseline-290726/`

## Fallback if the MCP dies again

`C:\Users\Jyue\Scripts\Periskope-Direct.ps1` wraps the REST API directly.
`POST https://api.periskope.app/v1/message/send`, headers `Authorization: Bearer <key>` +
`x-phone`, body `{"chat_id":"...","message":"...","message_type":"chat"}`. Credentials are read
from `C:\Users\Jyue\.claude.json` (fallback `.cursor\mcp.json`). Runbook:
`C:\Users\Jyue\Scripts\Periskope-Direct-RUNBOOK.md`
