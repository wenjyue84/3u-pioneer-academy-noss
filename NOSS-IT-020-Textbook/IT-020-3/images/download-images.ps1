# Download images for NOSS IT-020-3 textbook (Obsidian image format).
# Run from this folder: .\download-images.ps1
# If you get 429 (rate limit), run again later or download manually from URLs in IMAGES-README.md.

$ErrorActionPreference = 'Stop'
$base = 'https://commons.wikimedia.org/wiki/Special:FilePath'

# CoCu 2: Computer System Maintenance
@(
    @{ File = 'maintenance-compressed-air.jpg'; Url = "$base/Computer_onderhoud.jpg" }
    @{ File = 'maintenance-thermal-paste.jpg'; Url = "$base/Thermal_compound_pl.jpg" }
# CoCu 3: Computer System Repair
    @{ File = 'repair-toolkit-multimeter.jpg'; Url = "$base/Digital_multimeter.jpg" }
    @{ File = 'repair-remote-support.png'; Url = "$base/Remote_Assistance_Icon.png" }
) | ForEach-Object {
    $out = Join-Path $PSScriptRoot $_.File
    if (-not (Test-Path $out)) {
        Write-Host "Downloading $($_.File) ..."
        try {
            Invoke-WebRequest -Uri $_.Url -OutFile $out -UseBasicParsing
        } catch {
            Write-Warning "Failed: $($_.File) - $($_.Exception.Message). Download manually from IMAGES-README.md."
        }
    } else {
        Write-Host "Exists: $($_.File)"
    }
}

Write-Host "Done. CoCu 2: maintenance-event-viewer.png, maintenance-report.png. CoCu 3: repair-post-beep.png, repair-status-report.png — take screenshots or create manually (see IMAGES-README.md)."
