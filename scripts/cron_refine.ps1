# NOSS Textbook Cron Refinement Script
# Runs every 15 minutes via Windows Task Scheduler
# 1. Checks for .md changes
# 2. Runs gap analysis
# 3. Runs 7 AI agent reviewers
# 4. Rebuilds .docx
# 5. Uploads to Google Drive

$ErrorActionPreference = "Continue"
$ProjectDir = "C:\Users\Jyue\Documents\1-projects\NOSS"
$ContentDir = "$ProjectDir\content"
$OutputDir = "$ProjectDir\output"
$LogDir = "$ProjectDir\logs"
$ScriptsDir = "$ProjectDir\scripts"
$StateFile = "$ScriptsDir\.last-build"
$LogFile = "$LogDir\refine-$(Get-Date -Format 'yyyy-MM-dd').log"

# Ensure log directory exists
New-Item -ItemType Directory -Path $LogDir -Force | Out-Null

function Write-Log {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $entry = "[$timestamp] $Message"
    Add-Content -Path $LogFile -Value $entry
    Write-Host $entry
}

function Get-ContentHash {
    # Get combined hash of all .md files in content/
    $files = Get-ChildItem -Path $ContentDir -Recurse -Filter "*.md" | Sort-Object FullName
    $hashes = $files | ForEach-Object {
        (Get-FileHash $_.FullName -Algorithm MD5).Hash
    }
    return ($hashes -join "")
}

# ── Main ──────────────────────────────────────────────────────

Write-Log "=== NOSS Cron Refinement Start ==="

# Step 1: Check for changes
$currentHash = Get-ContentHash
$previousHash = ""
if (Test-Path $StateFile) {
    $previousHash = Get-Content $StateFile -Raw
}

if ($currentHash -eq $previousHash) {
    Write-Log "No changes detected in content/ — skipping"
    Write-Log "=== NOSS Cron Refinement End (no changes) ==="
    exit 0
}

Write-Log "Changes detected in content/ — proceeding with refinement"

# Step 2: Gap Analysis
Write-Log "Running gap analysis..."
try {
    $gapOutput = & uv run "$ScriptsDir\gap_analysis.py" 2>&1
    Write-Log "Gap analysis complete"
    Add-Content -Path $LogFile -Value ($gapOutput | Out-String)
} catch {
    Write-Log "Gap analysis failed: $_"
}

# Step 3: Multi-Agent Review (skip if no delegation CLIs available)
Write-Log "Running multi-agent review..."
try {
    $agentOutput = & uv run "$ScriptsDir\run_agents.py" --level all 2>&1
    Write-Log "Agent review complete"
    Add-Content -Path $LogFile -Value ($agentOutput | Out-String)
} catch {
    Write-Log "Agent review skipped/failed: $_"
}

# Step 4: Rebuild .docx
Write-Log "Rebuilding .docx files..."
try {
    $buildOutput = & uv run --with python-docx "$ScriptsDir\generate_docx.py" 2>&1
    Write-Log "Build complete"
    Add-Content -Path $LogFile -Value ($buildOutput | Out-String)
} catch {
    Write-Log "Build failed: $_"
    Write-Log "=== NOSS Cron Refinement End (build error) ==="
    exit 1
}

# Step 5: Upload to Google Drive
Write-Log "Uploading to Google Drive..."
try {
    # Upload each .docx file
    $docxFiles = Get-ChildItem -Path $OutputDir -Filter "*.docx"
    foreach ($file in $docxFiles) {
        Write-Log "  Uploading: $($file.Name)"
        $uploadResult = & gog drive upload $file.FullName --json --no-input 2>&1
        Add-Content -Path $LogFile -Value ($uploadResult | Out-String)
    }
    Write-Log "Upload complete"
} catch {
    Write-Log "Upload failed: $_"
}

# Step 6: Update state
$currentHash | Set-Content $StateFile -NoNewline
Write-Log "State updated"

# Summary
$docxCount = (Get-ChildItem -Path $OutputDir -Filter "*.docx").Count
Write-Log "Generated $docxCount .docx files"
Write-Log "=== NOSS Cron Refinement End (success) ==="
