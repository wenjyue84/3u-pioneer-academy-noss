---
name: commit-push
description: Commit and push immediately after any change in the 3u-pioneer-academy-noss repo (Jay's standing instruction, 2026-09-18). Runs Invoke-CommitPush.ps1 — stage the paths you touched, atomic commit with a conventional message, push to origin/master, print the remote hash and GitHub URL. Use after every batch of edits here; never leave work uncommitted.
---

# commit-push — 3u-pioneer-academy-noss

**Jay's rule (2026-09-18): in this repo, always commit + push right after the work lands.** This overrides the global "commit only when asked" default for this repository only.

## Run

```powershell
& "C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\.claude\skills\commit-push\Invoke-CommitPush.ps1" `
    -Path "video-film-editing/12-fail-pegawai","LOG.md" `
    -Message "feat(video-film-editing): officer-format deliverables (12-fail-pegawai)"
```

- `-Path` — one or more repo-relative paths to stage (files or folders). Omit to stage everything tracked+untracked except ignored.
- `-Message` — conventional-commit subject; the script appends a body line and the Claude attribution trailer.
- `-Body` — optional extra body text.
- `-NoPush` — commit only (rarely wanted).

Output: the new commit hash, `origin/master` hash after push, and the GitHub tree URL for the first path. Exit ≠ 0 means nothing was pushed — read the message (pre-commit secret hook, nothing staged, push rejected) and fix; do not retry blindly.

## Rules baked into the script

1. Runs `git status` first and refuses to touch a repo that has an `index.lock` (another commit in progress).
2. Never uses `--no-verify`; the global secret-scan hook (`~/.git-hooks/pre-commit`, single-pass since 2026-09-18) always runs.
3. Never amends, never force-pushes, always pushes to the current branch's upstream (`origin/master`).
4. Files > 95 MB are refused before staging (GitHub hard limit is 100 MB); the 1.87 GB Core Abilities zip is gitignored.
5. One commit per call — keep commits atomic: call it once per logical change, not once per file and not once per day.

## Commit message conventions used in this repo

`feat|fix|docs|chore(scope): subject` — scopes seen: `video-film-editing`, `raw`, `wim-jpk`, `proposals`, `gitignore`. Subject in English, ≤ 72 chars.
