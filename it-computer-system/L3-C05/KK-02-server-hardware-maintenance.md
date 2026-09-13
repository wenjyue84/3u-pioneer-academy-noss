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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C05 SERVER MAINTENANCE |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER MAINTENANCE JOB ORDER<br>2. CARRY OUT HARDWARE MAINTENANCE<br>3. PERFORM SERVER OPERATING SYSTEM MAINTENANCE<br>4. PREPARE SERVER MAINTENANCE RECORD |
| NO. KOD | IT-020-3:2013-C05/KK(2/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-server-hardware-maintenance

**TUJUAN:** Kertas rujukan untuk KK-02-server-hardware-maintenance.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

By the end of this activity, the trainee will be able to:
1. Safely power down and isolate a server before performing hardware maintenance.
2. Inspect, clean, and reseat server hardware components (RAM, HDDs/SSDs, PCIe cards, power supply units).
3. Replace a failed or degraded component (e.g., a faulty cooling fan or a RAID hot-spare drive).
4. Verify hardware integrity using server management firmware (iDRAC / iLO) and POST diagnostics.
5. Power the server back on and confirm stable operation before closing the job order.

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Tower or rack-mount server (lab unit) | 1 |
| 2 | Anti-static wrist strap | 1 |
| 3 | Anti-static mat | 1 |
| 4 | Torx/Phillips screwdriver set | 1 set |
| 5 | Compressed air can or ESD-safe vacuum | 1 |
| 6 | Replacement cooling fan (compatible model, for demonstration) | 1 |
| 7 | Replacement hard disk drive / SSD (hot-spare, lab unit) | 1 |
| 8 | Thermal paste (for CPU heat-sink re-seating if required) | 1 tube |
| 9 | Flashlight / headlamp | 1 |
| 10 | Hardware maintenance checklist form | 1 |
| 11 | Multimeter (for PSU voltage verification, if applicable) | 1 |

---

## Langkah Keselamatan / Safety Precautions

- Always wear an anti-static wrist strap and use an anti-static mat. Electrostatic discharge (ESD) can permanently damage server components.
- Follow the approved shutdown procedure — never force-power-off a server without prior authorisation; data loss or file-system corruption may result.
- Confirm that the server is fully de-energised before opening the chassis. Check that all power indicator LEDs are off.
- For rack-mounted servers, engage the rack's cable-management arm lock before sliding the server out to prevent tip-over hazards.
- Do not touch capacitors on the motherboard or PSU — residual charge may remain after shutdown.
- Do not force any connector or component. If resistance is felt, stop and inspect for misalignment.
- Replace only like-for-like components unless a verified compatible alternative has been approved.
- Keep the work area clear; small screws and components can become trip or ingestion hazards.

---

## Prosedur / Procedure

| Langkah / Step | Arahan / Instruction |
|----------------|----------------------|
| 1 | Confirm the maintenance window is active and the server has been formally handed over for maintenance (signed job order from supervisor). Notify the instructor/assessor that work is about to begin. |
| 2 | Log in to the server's out-of-band management console (iDRAC / iLO) to review the current hardware health dashboard. Record any active faults, warning events, or failed component indicators before touching the hardware. |
| 3 | Gracefully shut down the server OS: connect to the console, run the appropriate shutdown command (`shutdown /s /t 0` for Windows Server, `shutdown -h now` for Linux), and wait until the OS reports a complete shutdown. |
| 4 | Power off the server at the physical power button and disconnect all AC power cables. Wait at least 30 seconds for capacitors to discharge. Attach the anti-static wrist strap and place the server on the anti-static mat. |
| 5 | Open the server chassis according to the manufacturer's procedure (release latch or remove screws). Photograph the internal layout before disturbing any component — this reference image assists reassembly. |
| 6 | **Cleaning:** Using compressed air, blow dust from all heat sinks, fan blades, air baffles, and PCIe slot areas in short bursts (keep the can upright). Use the ESD-safe vacuum to remove dislodged dust. Do not spray compressed air directly onto exposed PCB traces. |
| 7 | **RAM inspection and reseating:** Visually inspect each DIMM for burn marks, cracks, or corrosion on gold contacts. Press each DIMM firmly downward until both retention clips click. If a DIMM is identified as faulty in the iDRAC/iLO log, remove it, note the slot label, and set it aside for replacement. |
| 8 | **Storage inspection:** Check all drive bays. Confirm each drive's activity LED status (steady green = healthy; amber = fault). For a degraded RAID array, identify the failed drive using the iDRAC/iLO storage controller view. Remove the failed drive by pressing the release lever, slide in the replacement hot-spare drive until it clicks and locks, and wait for the rebuild indicator to appear. |
| 9 | **Cooling fan replacement (if required):** Identify the faulty fan by the fault LED on the fan module or the iDRAC/iLO alert. Disconnect the fan power connector, unclip and remove the fan module, insert the replacement fan module until it seats firmly, and reconnect the power connector. |
| 10 | **PCIe card inspection:** Inspect all installed PCIe cards for secure seating. Press each card down firmly to ensure the retention latch is engaged. Check that all power connectors to PCIe devices are fully inserted. |
| 11 | Reinstall the chassis cover. Reconnect AC power cables. Power on the server and observe the POST sequence on the console. Verify that POST completes without errors. |
| 12 | Log in to the iDRAC/iLO management console after boot. Confirm that all previously faulted components now show a healthy status and that the RAID rebuild (if initiated) is progressing. |
| 13 | Log in to the server OS and confirm it has booted correctly. Run a brief system health check (e.g., check Device Manager on Windows Server, or `dmesg` and `lshw` on Linux) to confirm all components are recognised. |
| 14 | Complete the hardware maintenance checklist form. Record each component inspected, the action taken (cleaned / reseated / replaced), the replacement part serial number (if applicable), and the post-maintenance status. Submit to the instructor for review. |

---

## Hasil Dijangka / Expected Outcome

Upon completing this activity, the trainee will have:
- Safely powered down, opened, and serviced a server chassis.
- Cleaned all major internal components and removed accumulated dust.
- Reseated or replaced at least one identified hardware component.
- Verified post-maintenance hardware health via iDRAC/iLO and OS diagnostics.
- Produced a completed hardware maintenance checklist documenting all actions taken.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Anti-static wrist strap and mat used throughout | [ ] Yes  [ ] No |
| 2 | Pre-maintenance iDRAC/iLO health dashboard reviewed and faults recorded | [ ] Yes  [ ] No |
| 3 | Server gracefully shut down and fully de-energised before opening chassis | [ ] Yes  [ ] No |
| 4 | Internal photograph taken before disturbing components | [ ] Yes  [ ] No |
| 5 | Dust removed from all heat sinks, fans, and baffles using appropriate tools | [ ] Yes  [ ] No |
| 6 | All DIMMs inspected and reseated; faulty DIMM removed and labelled if found | [ ] Yes  [ ] No |
| 7 | Drive bay LEDs checked; failed/degraded drive replaced if applicable | [ ] Yes  [ ] No |
| 8 | Faulty fan replaced correctly (or fan health confirmed if no replacement needed) | [ ] Yes  [ ] No |
| 9 | PCIe cards inspected and fully seated | [ ] Yes  [ ] No |
| 10 | Server powered on; POST completed without errors | [ ] Yes  [ ] No |
| 11 | Post-maintenance iDRAC/iLO health status confirms all components healthy | [ ] Yes  [ ] No |
| 12 | Hardware maintenance checklist completed with part serial numbers and actions | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |