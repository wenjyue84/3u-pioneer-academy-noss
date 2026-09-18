$ErrorActionPreference = "Stop"
$f = Get-Item "C:\tmp_juno_ca_soalan\CA08retry.docx"
$pdfPath = "C:\tmp_juno_ca_soalan\CA08retry.pdf"
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
