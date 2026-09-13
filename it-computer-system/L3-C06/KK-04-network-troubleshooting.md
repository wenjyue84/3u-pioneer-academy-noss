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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C06 COMPUTER NETWORK CONNECTIVITY SET-UP |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER NETWORK CONFIGURATION SPECIFICATION<br>2. CARRY OUT COMPUTER NETWORK CONFIGURATION<br>3. PERFORM COMPUTER NETWORK CONNECTIVITY TEST<br>4. CARRY OUT COMPUTER NETWORK TROUBLESHOOT<br>5. PREPARE COMPUTER NETWORK CONNECTIVITY REPORT |
| NO. KOD | IT-020-3:2013-C06/KK(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-04-network-troubleshooting

**TUJUAN:** Kertas rujukan untuk KK-04-network-troubleshooting.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

By the end of this work activity, trainees will be able to:

1. Apply a systematic troubleshooting methodology to diagnose network connectivity faults.
2. Use diagnostic tools (ping, tracert, ipconfig, nslookup, show commands) to isolate faults.
3. Identify and rectify common network faults including misconfigured IP addresses, incorrect VLAN assignments, faulty cables, and routing errors.
4. Document the fault, diagnosis process, and corrective action taken.

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Network lab setup with pre-introduced faults (or Packet Tracer / GNS3 scenario) | 1 |
| 2 | Computer / laptop with console and network access | 1 per trainee |
| 3 | Network troubleshooting worksheet | 1 |
| 4 | Cable tester | 1 |
| 5 | Approved network configuration specification (correct baseline) | 1 |
| 6 | Terminal emulator software (e.g., PuTTY) | Installed |

---

## Langkah Keselamatan / Safety Precautions

- Before modifying any device configuration, record the current (faulty) configuration — this preserves evidence for the fault report.
- Do not apply fixes to a device until the root cause is confirmed — changing multiple settings simultaneously makes diagnosis unreliable.
- Do not swap physical hardware (cables, patch panels) without first confirming the fault is at the physical layer.
- Inform the instructor before applying any corrective action that may disrupt connectivity to other trainees' lab segments.
- Power off devices before replacing cables on non-hot-swap ports.

---

## Prosedur / Procedure

| Langkah / Step | Arahan / Instruction |
|----------------|----------------------|
| 1 | Receive the fault scenario from the instructor. Read the fault description carefully. Record the reported symptom(s) in the troubleshooting worksheet (e.g., "PC-A cannot reach PC-B", "DHCP addresses not being assigned"). |
| 2 | Apply the OSI model troubleshooting approach — begin at Layer 1 (Physical) and work upward unless the symptom clearly points to a higher layer. |
| 3 | **Layer 1 — Physical:** Check cable connections at both ends. Verify link LEDs on switch ports are active. Use a cable tester to check for open circuits or crossed pairs. Record findings. |
| 4 | **Layer 2 — Data Link:** On the switch, run `show interfaces <port>` to check for errors (input errors, CRC, runts, giants). Run `show mac address-table` to verify MAC addresses are being learned. Check VLAN assignments: `show vlan brief`. Record findings. |
| 5 | **Layer 3 — Network:** On each affected device, run `ipconfig /all` (Windows) or `ip addr` (Linux) to verify IP address, subnet mask, and default gateway. Compare against the specification. Run `ping 127.0.0.1` (loopback), then `ping <gateway>`. Record findings. |
| 6 | On the router, run `show ip interface brief` to confirm all interfaces are up/up and have the correct IP addresses. Run `show ip route` to verify the routing table contains expected entries. Record findings. |
| 7 | **Layer 7 — Application (DNS/DHCP):** If IP is auto-assigned, run `ipconfig /release` then `ipconfig /renew`. Check the router's DHCP binding table: `show ip dhcp binding`. Test DNS: `nslookup <hostname>`. Record findings. |
| 8 | Based on findings, identify the root cause. Record the root cause clearly in the worksheet: state the layer, device, interface, and exact misconfiguration or fault (e.g., "Switch port Fa0/3 assigned to VLAN 20 instead of VLAN 10"). |
| 9 | Apply the corrective action. Make only the minimum change required to fix the identified fault. Record the exact command(s) or physical action taken. |
| 10 | Re-test connectivity using the same test cases from KK-03. Confirm the fault is resolved. Record the post-fix test results. |
| 11 | If the fault is not resolved after the corrective action, return to Step 2 and re-examine — the initial diagnosis may have been incomplete. Do not apply additional changes without re-diagnosing. |
| 12 | Save the corrected configuration on all affected devices: `copy running-config startup-config`. |
| 13 | Complete the troubleshooting worksheet: symptom, OSI layer analysis, root cause, corrective action, post-fix test results, and conclusion. Submit to instructor. |

---

## Hasil Dijangka / Expected Outcome

Upon completion, trainees will have:

- Successfully diagnosed the fault(s) introduced in the lab scenario using the OSI-layer approach.
- Applied a targeted corrective action to restore connectivity.
- Verified the fix by re-running connectivity tests.
- Produced a completed troubleshooting worksheet documenting the full diagnostic process.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Fault symptom correctly identified and recorded | [ ] Yes  [ ] No |
| 2 | OSI layer troubleshooting sequence applied | [ ] Yes  [ ] No |
| 3 | Physical layer checked (cable, LEDs, cable tester) | [ ] Yes  [ ] No |
| 4 | Data link layer checked (`show interfaces`, `show vlan brief`) | [ ] Yes  [ ] No |
| 5 | Network layer checked (`ipconfig`, `ping`, `show ip route`) | [ ] Yes  [ ] No |
| 6 | DHCP/DNS functionality tested where applicable | [ ] Yes  [ ] No |
| 7 | Root cause correctly identified at the appropriate OSI layer | [ ] Yes  [ ] No |
| 8 | Corrective action applied (minimum change, documented) | [ ] Yes  [ ] No |
| 9 | Post-fix connectivity tests confirm fault is resolved | [ ] Yes  [ ] No |
| 10 | Configuration saved and troubleshooting worksheet submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |