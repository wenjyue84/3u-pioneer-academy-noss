<#
.SYNOPSIS  Export every .docx in a folder to .pdf (same name) using one fresh Word process per file — robust against the COM RPC drops seen on this box.
.EXAMPLE   .\Export-Pdf.ps1 -Folder "<output>\07 ...\Core Abilities L1-L3 (format JPK)"
#>
param([Parameter(Mandatory)][string]$Folder, [string]$Filter = "*.docx")
$tmpd = "C:\tmp_juno_pdf"; New-Item -ItemType Directory -Force $tmpd | Out-Null
$i = 0
foreach ($f in Get-ChildItem -LiteralPath $Folder -Filter $Filter -File) {
    $i++; $tmp = "$tmpd\d$i.docx"; $pdf = "$tmpd\d$i.pdf"
    Copy-Item -LiteralPath $f.FullName $tmp -Force
    Remove-Item $pdf -Force -ErrorAction SilentlyContinue
    $w = $null
    try {
        $w = New-Object -ComObject Word.Application; $w.Visible = $false; $w.DisplayAlerts = 0
        $doc = $w.Documents.Open($tmp, $false, $true)
        $null = $doc.Fields.Update()
        # CreateBookmarks=1 (wdExportCreateHeadingBookmarks) -> PDF outline/navigation from Heading 1/2
        $doc.ExportAsFixedFormat($pdf, 17, $false, 0, 0, 1, 1, 0, $true, $true, 1, $true, $true, $false)
        $pages = $doc.ComputeStatistics(2)
        $doc.Close($false)
        Write-Output ("{0} pages={1}" -f $f.Name, $pages)
    } catch { Write-Output ("{0} ERROR {1}" -f $f.Name, $_.Exception.Message) }
    finally { if ($w) { try { $w.Quit() } catch {} } }
    if (Test-Path $pdf) { Copy-Item $pdf -Destination ([IO.Path]::ChangeExtension($f.FullName, '.pdf')) -Force }
}
