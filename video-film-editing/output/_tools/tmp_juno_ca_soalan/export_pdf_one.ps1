$ErrorActionPreference = "Stop"
$dir = "C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\07 3.4b Soalan Penilaian Pengetahuan\Core Abilities L1-L3 (format JPK)"
$name = "SOALAN-CA-08 Z-009-2-2015 CA04 SOALAN PENILAIAN HEALTH SAFETY AND ENVIRONMENTAL ADAPTATION (IT-072).docx"
$f = Get-Item (Join-Path $dir $name)
$pdfPath = [System.IO.Path]::ChangeExtension($f.FullName, "pdf")
Get-Process WINWORD -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2
$word = New-Object -ComObject Word.Application
$word.Visible = $false
Start-Sleep -Seconds 1
$doc = $word.Documents.Open($f.FullName)
$doc.SaveAs([ref]$pdfPath, [ref]17)
$pages = $doc.ComputeStatistics(2)
Write-Output "pages=$pages"
$doc.Close([ref]$false)
$word.Quit()
