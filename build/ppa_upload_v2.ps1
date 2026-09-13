# PPA Upload v2 — 44 files (formatting-fixed + 8 new sets).
# Covers: N821 A/B, M731 A/B, G471 A/B, FB-018-3 B, FB45L4 A/B, FB45L5 A/B
# FB-018-3 SET A will be uploaded separately after workflow completes.
# Convention: SOALAN PENILAIAN AMALI PPT (SET X).pdf
#             SKEMA PENILAIAN AMALI PPT-PPA (SET X).pdf
#             ASSESSMENT ANSWER SHEET (SET X).pdf
#             EQUIPMENT VERIFICATION (SET X).pdf
# Run with: pwsh build/ppa_upload_v2.ps1

$ErrorActionPreference = "Stop"
$pdf  = "C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\output\jennifer-ppa-soalan\pdf"
$acct = "wenjyue@gmail.com"

$folders = @{
  n821  = "169-72I6UsuhSU55ExxVUDfSNzgmonCf1"   # N821-001-3-2020 OFFICE ADMINISTRATION
  m731  = "1UVrPhmrG0dkE-2YbSeFcQCzT-JZH_h30"   # M731-001-3-2021 DIGITAL MARKETING OPERATION
  g471  = "1w_BdONXPVyTBVDUQOUv7dKCkq3K8RQOn"   # G471-001-3-2018 RETAIL OUTLET OPERATIONS
  fb3   = "1grg0ck28lAZHeMhmVB7g1vh4V80NlY_o"   # FB-018-3 2012 SALES & MARKETING OPERATION
  l4    = "1yRsIymqd3AzLMIzoHJ7epf2zsDJqBigC"   # Sales & Marketing Administration L4
  l5    = "1B-ExSfT9MdjzoD0r23H_ZUuDftlXpFfc"   # Sales & Marketing Management L5
}

$docNames = @{
  "soalan"                 = "SOALAN PENILAIAN AMALI PPT (SET {0}).pdf"
  "skema"                  = "SKEMA PENILAIAN AMALI PPT-PPA (SET {0}).pdf"
  "answer-sheet"           = "ASSESSMENT ANSWER SHEET (SET {0}).pdf"
  "equipment-verification" = "EQUIPMENT VERIFICATION (SET {0}).pdf"
}

# localPrefix, set letter, folder key
$sets = @(
  @("n821-001-3-office-admin-set-a",      "A", "n821"),
  @("n821-001-3-office-admin-set-b",      "B", "n821"),
  @("m731-001-3-digital-marketing-set-a", "A", "m731"),
  @("m731-001-3-digital-marketing-set-b", "B", "m731"),
  @("g471-001-3-retail-outlet-set-a",     "A", "g471"),
  @("g471-001-3-retail-outlet-set-b",     "B", "g471"),
  @("fb-018-3-set-b",                     "B", "fb3"),
  @("fb-018-45-l4-set-a",                 "A", "l4"),
  @("fb-018-45-l4-set-b",                 "B", "l4"),
  @("fb-018-45-l5-set-a",                 "A", "l5"),
  @("fb-018-45-l5-set-b",                 "B", "l5")
)

$failed = @()
$ok = 0
foreach ($s in $sets) {
  $prefix, $setLetter, $fkey = $s
  foreach ($doc in $docNames.Keys) {
    $local  = Join-Path $pdf "$prefix-$doc.pdf"
    $remote = $docNames[$doc] -f $setLetter
    if (-not (Test-Path $local)) { $failed += "MISSING LOCAL: $local"; continue }
    Write-Host "-> [$fkey $setLetter] $remote"
    gog drive upload $local --account $acct --parent $folders[$fkey] --name $remote --no-input | Out-Null
    if ($LASTEXITCODE -ne 0) { $failed += "UPLOAD FAILED: $remote" } else { $ok++ }
  }
}

Write-Host "`n$ok uploaded."
if ($failed) {
  Write-Host "`nFAILURES:"
  $failed | ForEach-Object { Write-Host "  $_" }
  exit 1
}
Write-Host "Now verify each folder with: gog drive ls --account wenjyue@gmail.com --parent <id>"
