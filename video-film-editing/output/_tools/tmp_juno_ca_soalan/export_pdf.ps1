$ErrorActionPreference = "Stop"
$dir = "C:\Users\Jyue\Documents\1-projects\3u-pioneer-academy-noss\video-film-editing\output\07 3.4b Soalan Penilaian Pengetahuan\Core Abilities L1-L3 (format JPK)"
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$files = Get-ChildItem -Path $dir -Filter "*.docx" | Sort-Object Name
foreach ($f in $files) {
    $doc = $word.Documents.Open($f.FullName)
    $pdfPath = [System.IO.Path]::ChangeExtension($f.FullName, "pdf")
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $pages = $doc.ComputeStatistics(2)  # wdStatisticPages = 2
    Write-Output "$($f.Name) => pages=$pages"
    $doc.Close([ref]$false)
}
$word.Quit()
