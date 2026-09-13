# NOSS IT-020 Computer System Management Textbook
> **Last updated:** 2026-04-04

**Status:** Active Development
**Academy:** 3U Pioneer Academy Sdn Bhd
**Module:** IT-020 Computer System Management (Levels 3, 4, 5)

## Purpose

Generate NOSS-compliant textbooks in .docx format for JPK/MySPIKE approval submission.

## Google Docs (Live)

| Level | Title | Link |
|-------|-------|------|
| L3 | Computer System Operation | [Google Doc](https://docs.google.com/document/d/1LHPCgRvy4rGVxCcIEoZAm5CVOtPRW_ubflvJSs8WsEo/edit) |
| L4 | Computer Systems Administration | [Google Doc](https://docs.google.com/document/d/1c8K5bgHxgRABNyjNuhyNWBDIJ4FDgChwd8Oy_bafRog/edit) |
| L5 | Computer Systems Management | [Google Doc](https://docs.google.com/document/d/1lUAmUsevG4OwJ94pSq8TD2CnwXAuMe2Y3ubm2ySzxTg/edit) |

## NOSS IT-020 Series

| Code | Level | Title | CoCu Units | Contact Hours |
|------|-------|-------|-----------|--------------|
| IT-020-3:2013 | 3 | Computer System Operation | 7 | 1200 |
| IT-020-4:2013 | 4 | Computer Systems Administration | 6 | TBC |
| IT-020-5:2013 | 5 | Computer Systems Management | 7 | TBC |

## Structure

- `content/` — Editable .md source files (single source of truth)
- `output/` — Generated .docx files
- `_reference/` — Read-only reference materials
- `scripts/` — Build tooling (generate_docx.py, sync, cron, agent prompts)
- `templates/` — NOSS .docx template
- `logs/` — Cron job and agent review logs

## Automation

Every 15 minutes, a cron job:
1. Runs 7 AI agent reviewers (assessor, trainer, trainee, internal/external verifier, domain expert, JPK officer)
2. Performs gap analysis against DSD/JPK government standards
3. Rebuilds .docx from refined .md sources
4. Uploads to Google Docs


---

↑ [Projects Wiki](../WIKI.md) · [Projects MOC](../00-PROJECTS-MOC.md)
