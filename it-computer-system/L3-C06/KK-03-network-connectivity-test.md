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
| NO. KOD | IT-020-3:2013-C06/KK(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-03-network-connectivity-test

**TUJUAN:** Kertas rujukan untuk KK-03-network-connectivity-test.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

By the end of this work activity, trainees will be able to:

1. Use standard networking tools to verify IP reachability between network nodes.
2. Test DHCP, DNS, and default gateway functionality.
3. Verify inter-VLAN and WAN connectivity as applicable.
4. Record test results systematically and compare against expected outcomes.

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Configured network (lab hardware or Packet Tracer / GNS3 simulation) | 1 |
| 2 | Computer / laptop (end-user node) | 1 per trainee |
| 3 | Network connectivity test record sheet | 1 |
| 4 | Approved network configuration specification (for reference) | 1 |
| 5 | Command prompt / terminal access on all test nodes | Required |

---

## Langkah Keselamatan / Safety Precautions

- Do not execute flood-ping or stress tests on live production networks — test only within the designated lab environment.
- Do not modify any device configuration during the testing phase; testing is read-only.
- Record all test commands and outputs accurately — do not alter or selectively omit failed results.
- Report any unexpected network behaviour (e.g., routing loops, broadcast storms) to the instructor immediately.

---

## Prosedur / Procedure

| Langkah / Step | Arahan / Instruction |
|----------------|----------------------|
| 1 | Prepare the connectivity test record sheet. List every test case to be performed, the source node, destination node, expected result, and a column for actual result. |
| 2 | On each end-user device, open a command prompt. Verify the IP configuration: `ipconfig /all` (Windows) or `ip addr show` (Linux). Confirm IP address, subnet mask, default gateway, and DNS server match the specification. Record findings. |
| 3 | Test loopback on each device: `ping 127.0.0.1`. A successful reply confirms the TCP/IP stack is operational. Record pass/fail for each device. |
| 4 | Test connectivity to the default gateway from each end-user device: `ping <gateway IP>`. Record the number of packets sent, received, and lost, and average round-trip time (RTT). |
| 5 | Test connectivity between end-user devices within the same subnet: `ping <peer IP>`. Perform this for at least two pairs of devices. Record results. |
| 6 | If VLANs are configured, test inter-VLAN connectivity: from a device in VLAN A, `ping` a device in VLAN B. Verify that the router (Layer 3 switch or router-on-a-stick) correctly routes between VLANs. Record results. |
| 7 | Test DHCP functionality: on a device set to obtain an address automatically, release and renew the IP: `ipconfig /release` then `ipconfig /renew` (Windows). Verify a new IP is assigned from the correct pool. Record the assigned address. |
| 8 | Test DNS resolution: `nslookup <hostname or domain>` or `ping <hostname>`. Verify the correct IP address is returned by the DNS server. Record results. |
| 9 | Test WAN / internet reachability (if applicable): `ping 8.8.8.8` (external IP), then `ping www.google.com` (DNS + routing). Record results separately to distinguish routing failures from DNS failures. |
| 10 | Use `tracert <destination>` (Windows) or `traceroute <destination>` (Linux) to trace the path to the gateway and to an external host. Verify the path matches the expected routing. Record hop count and any anomalies. |
| 11 | Compare all actual results against the expected results in the test record sheet. Mark each test case as Pass or Fail. For any Fail, note the observed behaviour and the likely cause. |
| 12 | Submit the completed connectivity test record sheet to the instructor. |

---

## Hasil Dijangka / Expected Outcome

Upon completion, trainees will have produced:

- A fully completed connectivity test record sheet with pass/fail results for every test case.
- Verified that all in-scope network nodes are reachable from each other as specified.
- Confirmed DHCP, DNS, and gateway functionality.
- Identified any connectivity failures with an initial diagnosis noted.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | IP configuration verified on all devices (`ipconfig /all`) | [ ] Yes  [ ] No |
| 2 | Loopback test passed on all devices | [ ] Yes  [ ] No |
| 3 | Gateway reachability confirmed from all end-user devices | [ ] Yes  [ ] No |
| 4 | Intra-subnet ping tests completed and recorded | [ ] Yes  [ ] No |
| 5 | Inter-VLAN connectivity tested (if VLANs configured) | [ ] Yes  [ ] No |
| 6 | DHCP release/renew tested and address allocation verified | [ ] Yes  [ ] No |
| 7 | DNS resolution tested using `nslookup` | [ ] Yes  [ ] No |
| 8 | WAN/internet reachability tested (if applicable) | [ ] Yes  [ ] No |
| 9 | `tracert`/`traceroute` used to verify routing path | [ ] Yes  [ ] No |
| 10 | All results recorded in test record sheet and submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |