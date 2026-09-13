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

## KERTAS KERJA

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C03 COMPUTER SYSTEM REPAIR |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS COMPUTER REPAIR JOB ORDER/CHANGE REQUEST<br>2. CARRY OUT ONLINE TROUBLESHOOTING<br>3. PERFORM ON-SITE REPAIR<br>4. PREPARE COMPUTER STATUS REPORT |
| NO. KOD | IT-020-3:2013-C03/KK(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-online-troubleshooting

**TUJUAN:** Kertas rujukan untuk KK-02-online-troubleshooting.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

Upon completion of this activity, the trainee will be able to:
1. Apply a systematic troubleshooting methodology to diagnose computer system faults remotely.
2. Use built-in OS diagnostic tools and remote access utilities to gather fault evidence.
3. Interpret system event logs, error codes, and diagnostic reports to isolate root causes.
4. Apply software-based corrective actions where the fault is resolvable without physical intervention.
5. Escalate faults that require on-site repair and document all findings for handover.

---

## Peralatan / Equipment Required

| No. | Item | Quantity |
|-----|------|----------|
| 1 | PC or laptop with Windows OS (trainee unit) | 1 |
| 2 | PC or laptop with Windows OS (simulated client unit) | 1 |
| 3 | Remote desktop / remote access software (e.g. Windows Remote Desktop, AnyDesk) | 1 set |
| 4 | Network connection (LAN or Wi-Fi) | 1 |
| 5 | Simulated fault scenario card (issued by instructor) | 1 |
| 6 | Troubleshooting log form | 1 |
| 7 | Pen and notepad | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Obtain explicit consent (simulated) from the customer before establishing any remote connection.
- Never access files, folders, or accounts beyond the scope stated on the job order.
- Disconnect the remote session immediately upon completing the troubleshooting task.
- Do not download or install unauthorised software on the client machine.
- Ensure the remote connection is made over a secured network; do not troubleshoot over an open public Wi-Fi without a VPN.
- Record all actions taken during the remote session in the troubleshooting log — omitting steps may cause repeated or conflicting repairs.

---

## Prosedur / Procedure

| Langkah | Arahan / Instruction |
|---------|----------------------|
| 1 | Receive the simulated fault scenario card from the instructor. Read the reported symptoms carefully. Common scenario types include: system failing to boot, application crash loop, network connectivity loss, slow performance, or recurring Blue Screen of Death (BSOD). |
| 2 | Contact the simulated client (role-played by a fellow trainee or instructor). Confirm the symptoms verbally or via the provided scenario script. Ask the following: (a) When did the fault first occur? (b) Were any changes made before the fault appeared (e.g. Windows Update, new software install)? (c) Is the fault intermittent or consistent? |
| 3 | Establish a remote desktop connection to the simulated client machine. Verify you are connected to the correct unit (check hostname and logged-in user against the job order). |
| 4 | Open **Event Viewer** (eventvwr.msc). Navigate to: Windows Logs > System and Windows Logs > Application. Filter for Critical and Error events from the past 7 days. Record the top 3 most relevant event IDs and their descriptions in the troubleshooting log. |
| 5 | Open **Device Manager** (devmgmt.msc). Scan for any devices showing a yellow warning triangle or red error icon. For each flagged device, note the device name, error code, and recommended action. |
| 6 | Open **Task Manager** (Ctrl+Shift+Esc). Check the Performance tab for CPU, RAM, and Disk utilisation. A sustained CPU or Disk usage above 90% at idle indicates a software or driver issue. Record the values observed. |
| 7 | Run the appropriate built-in diagnostic based on the fault type: (a) **sfc /scannow** in an elevated Command Prompt to check for corrupted system files; (b) **chkdsk C: /f /r** scheduled for next restart if disk errors are suspected; (c) **ipconfig /all** and **ping 8.8.8.8** to diagnose network faults; (d) **msconfig** > Selective Startup to isolate startup program conflicts. Record the command used and the output obtained. |
| 8 | Based on the diagnostic results, determine whether the fault is: (a) resolvable online (software fix, driver update, settings change), or (b) requires physical intervention (hardware replacement, on-site visit). Document the determination with justification. |
| 9 | If the fault is resolvable online, apply the corrective action: (a) roll back or update the flagged driver via Device Manager; (b) uninstall the conflicting application via Control Panel; (c) restore a previous system restore point via System Protection; or (d) reset network adapter settings. |
| 10 | After applying the fix, verify the resolution: restart the client machine, confirm the fault symptom no longer occurs, and re-run the relevant diagnostic tool to confirm a clean result. Record the verification outcome. |
| 11 | Terminate the remote session. Complete the troubleshooting log with: symptoms, diagnostic steps taken, tools used, findings, corrective action applied, and resolution status. If the fault is not resolved, document the recommended on-site escalation steps for handover. |

---

## Hasil Dijangka / Expected Outcome

- Remote session established successfully and disconnected properly after use.
- Fault symptoms confirmed and systematically investigated using at least two built-in diagnostic tools.
- Root cause identified and documented with supporting evidence (event IDs, device manager status, or performance data).
- Corrective action applied (if resolvable online) and verified, OR clear escalation recommendation documented (if on-site intervention is required).
- Completed troubleshooting log submitted to instructor.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Remote connection established with correct authorisation procedure | [ ] Yes  [ ] No |
| 2 | Fault symptoms confirmed with client before commencing diagnostics | [ ] Yes  [ ] No |
| 3 | Event Viewer reviewed; relevant error events recorded | [ ] Yes  [ ] No |
| 4 | Device Manager checked; flagged devices noted | [ ] Yes  [ ] No |
| 5 | At least one built-in diagnostic command executed and output recorded | [ ] Yes  [ ] No |
| 6 | Fault correctly classified as online-resolvable or requiring on-site escalation | [ ] Yes  [ ] No |
| 7 | Corrective action applied (or escalation path documented) | [ ] Yes  [ ] No |
| 8 | Resolution verified or unresolved status clearly documented | [ ] Yes  [ ] No |
| 9 | Remote session terminated after task completion | [ ] Yes  [ ] No |
| 10 | Troubleshooting log fully completed, signed, and dated | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |