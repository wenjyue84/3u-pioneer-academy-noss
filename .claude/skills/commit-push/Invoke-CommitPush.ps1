<#
.SYNOPSIS
  Stage → atomic commit → push for the 3u-pioneer-academy-noss repo. Never --no-verify, never amend, never force.
.EXAMPLE
  .\Invoke-CommitPush.ps1 -Path "video-film-editing/12-fail-pegawai" -Message "feat(video-film-editing): officer deliverables"
#>
[CmdletBinding()]
param(
    [string[]]$Path,
    [Parameter(Mandatory)][string]$Message,
    [string]$Body = "",
    [switch]$NoPush
)
$ErrorActionPreference = "Stop"
$Repo = "C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss"
$Remote = "https://github.com/wenjyue84/3u-pioneer-academy-noss"
Set-Location $Repo

if (Test-Path "$Repo\.git\index.lock") {
    throw "index.lock present — another git process is running in this repo. Wait for it (or remove the stale lock if no git.exe is alive)."
}

# refuse oversized files before staging
$limit = 95MB
$targets = if ($Path) { $Path } else { @(".") }
$big = Get-ChildItem -Path $targets -Recurse -File -ErrorAction SilentlyContinue |
       Where-Object { $_.Length -gt $limit } |
       Where-Object { git check-ignore -q -- $_.FullName 2>$null; $LASTEXITCODE -ne 0 }
if ($big) { throw ("Refusing to stage files > 95 MB (GitHub limit): " + ($big.FullName -join "; ")) }

git add -- $targets
if ($LASTEXITCODE -ne 0) { throw "git add failed" }
$staged = git diff --cached --name-only
if (-not $staged) { Write-Host "Nothing staged for: $($targets -join ', ') — nothing to commit."; exit 0 }
Write-Host ("Staged {0} file(s)" -f ($staged | Measure-Object).Count)

$trailer = "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
$full = $Message
if ($Body) { $full += "`n`n$Body" }
$full += "`n`n$trailer"

$tmp = [System.IO.Path]::GetTempFileName()
[System.IO.File]::WriteAllText($tmp, $full, (New-Object System.Text.UTF8Encoding($false)))
git commit -q -F $tmp
$rc = $LASTEXITCODE
Remove-Item $tmp -Force
if ($rc -ne 0) { throw "git commit failed (pre-commit hook or empty commit) — see output above." }
$hash = git rev-parse --short HEAD
Write-Host "Committed $hash : $Message"

if ($NoPush) { Write-Host "(-NoPush) not pushed."; exit 0 }
$branch = git rev-parse --abbrev-ref HEAD
git push -q origin $branch
if ($LASTEXITCODE -ne 0) { throw "git push failed — commit $hash is local only." }
$remoteHash = (git ls-remote origin $branch).Substring(0,7)
Write-Host "Pushed: origin/$branch = $remoteHash"
$first = if ($Path) { ($Path[0] -replace '\\','/').TrimEnd('/') } else { "" }
Write-Host ("URL: {0}/tree/{1}/{2}" -f $Remote, $branch, [uri]::EscapeUriString($first))
