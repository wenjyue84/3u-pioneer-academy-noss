<!-- JPK_ENVELOPE_v1 -->
<table border="0" cellspacing="0" cellpadding="8" width="100%">
<tr>
<td width="130" valign="top"><img src="../_assets/logos/jpk-logo.png" alt="JPK Logo" width="110"></td>
<td valign="middle">
<b>JABATAN PEMBANGUNAN KEMAHIRAN (JPK)</b><br>
TINGKAT 7-8, BLOK D4, KOMPLEKS D,<br>
PUSAT PENTADBIRAN KERAJAAN PERSEKUTUAN,<br>
62530 PUTRAJAYA
</td>
</tr>
</table>

## KERTAS TUGASAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/KT(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-02-server-script-development-assignment

**TUJUAN:** Kertas rujukan untuk KT-02-server-script-development-assignment.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions. Refer to KP(2/4) for guidance. This assignment is formative.

**Masa / Duration:** 1 hour 30 minutes

---

## Soalan / Questions

### Bahagian A: Soalan Pelbagai Pilihan / Multiple Choice (20 marks)

**A1.** The PowerShell directive `Set-StrictMode -Version Latest` causes the script to:

- (a) Run only on the latest version of PowerShell
- (b) Treat uninitialized variables and undefined properties as errors, making bugs easier to find
- (c) Prevent other scripts from modifying global variables
- (d) Enable verbose logging automatically

**A2.** In Bash, the directive `set -euo pipefail` does NOT:

- (a) Exit the script on any unhandled error (`-e`)
- (b) Treat unset variables as errors (`-u`)
- (c) Return a non-zero exit code if any command in a pipeline fails (`-o pipefail`)
- (d) Prevent the script from running as root

**A3.** Which PowerShell collection type should be preferred over `$array += $item` when building a large list in a loop?

- (a) `[hashtable]`
- (b) `[System.Collections.Generic.List[PSCustomObject]]`
- (c) `[string[]]`
- (d) `[xml]`

**A4.** In Python, the `if __name__ == "__main__":` guard ensures that:

- (a) The script can only be run by the root user
- (b) The `main()` function only executes when the script is run directly, not when imported as a module
- (c) The script will restart automatically if it crashes
- (d) All logging output is suppressed

**A5.** A server script exits with code **3**. Based on the exit code convention from KP(2/4), this means:

- (a) Fatal error — an unhandled exception occurred
- (b) Invalid arguments were supplied
- (c) Partial success — the script completed but some operations failed
- (d) Success — the script completed without any issues

**A6.** Which Git commit message follows the Conventional Commits specification correctly?

- (a) `updated the disk check script`
- (b) `FEAT: new disk space monitoring`
- (c) `feat: add disk space monitoring script for Windows Server fleet`
- (d) `disk_check.ps1 — added feature`

**A7.** The Bash `mapfile -t old_logs < <(find "$LOG_DIR" -name "*.log" -mtime +7)` command:

- (a) Pipes log file content into a variable
- (b) Reads filenames older than 7 days from `find` into the `old_logs` array
- (c) Deletes log files older than 7 days
- (d) Counts the number of log files in the directory

**A8.** In Python's `logging` module, setting a handler's level to `logging.INFO` means:

- (a) Only INFO messages are written; DEBUG messages are suppressed
- (b) All messages including DEBUG are written to that handler
- (c) The handler writes only ERROR and CRITICAL messages
- (d) The handler is disabled

**A9.** Which file should NEVER be committed to a Git repository containing server scripts?

- (a) `README.md`
- (b) `CHANGELOG.md`
- (c) `.env` file containing database passwords
- (d) `scripts/Check-DiskSpace.ps1`

**A10.** A PowerShell module file ends with the extension:

- (a) `.ps1`
- (b) `.psd1`
- (c) `.psm1`
- (d) `.psxml`

---

### Bahagian B: Soalan Jawapan Pendek / Short Answer (30 marks)

**B1.** State FIVE (5) design principles of a well-written server script and explain each in one sentence. (10 marks)

**B2.** Compare error handling in PowerShell, Bash, and Python. For each language, provide: (a) the directive/setting used to halt on unhandled errors, and (b) the syntax for a try/catch (or equivalent) block. (12 marks)

**B3.** Explain the exit code convention for server scripts (exit codes 0, 1, 2, and 3). Why is it important for scripts to return correct exit codes? (8 marks)

---

### Bahagian C: Soalan Esei / Essay (30 marks)

**C1.** Study the following PowerShell code snippet. It was written by a junior administrator and has FOUR (4) significant problems. Identify each problem and provide the corrected code.

```powershell
$servers = "Server01,Server02,Server03"
$adminPass = "P@ssword123"

foreach ($s in $servers) {
    $disk = Get-WmiObject Win32_LogicalDisk -ComputerName $s
    if ($disk.FreeSpace -lt 1073741824) {
        Write-Host "Low disk on $s"
    }
}
```

For each problem: (a) identify and explain the problem, (b) state the consequence if not fixed, and (c) provide the corrected code. (20 marks)

**C2.** A colleague asks: "Why do we need to use Git for server scripts? We can just keep copies in a shared folder." Write a response of at least 200 words explaining the specific advantages of Git version control for server scripts over a shared folder approach, with reference to at least THREE (3) concrete scenarios where Git would prevent a problem that a shared folder approach could not. (10 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*