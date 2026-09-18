$ErrorActionPreference = "Stop"
$dir = "C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\07 3.4b Soalan Penilaian Pengetahuan\Core Abilities L1-L3 (format JPK)"
$files = Get-ChildItem -Path $dir -Filter "*.docx" | Sort-Object Name
$results = @()
foreach ($f in $files) {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    Start-Sleep -Milliseconds 300
    $doc = $word.Documents.Open($f.FullName)
    $pdfPath = [System.IO.Path]::ChangeExtension($f.FullName, "pdf")
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $pages = $doc.ComputeStatistics(2)
    $results += "$($f.Name)|$pages"
    $doc.Close([ref]$false)
    $word.Quit()
    Start-Sleep -Milliseconds 300
}
$results | ForEach-Object { Write-Output $_ }
