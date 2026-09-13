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

## KERTAS PENERANGAN

| Medan | Nilai |
| --- | --- |
| KOD DAN NAMA PROGRAM | IT-020-3:2013 OPERASI SISTEM KOMPUTER |
| TAHAP | 3 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C06 COMPUTER NETWORK CONNECTIVITY SET-UP |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER NETWORK CONFIGURATION SPECIFICATION<br>2. CARRY OUT COMPUTER NETWORK CONFIGURATION<br>3. PERFORM COMPUTER NETWORK CONNECTIVITY TEST<br>4. CARRY OUT COMPUTER NETWORK TROUBLESHOOT<br>5. PREPARE COMPUTER NETWORK CONNECTIVITY REPORT |
| NO. KOD | IT-020-3:2013-C06/KP(4/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-04-network-troubleshooting

**TUJUAN:** Kertas rujukan untuk KP-04-network-troubleshooting.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Apply a structured troubleshooting methodology to diagnose network faults.
2. Identify and resolve common Layer 1 (physical), Layer 2 (data link), and Layer 3 (network) faults.
3. Use diagnostic commands (`ping`, `ipconfig`, `tracert`, `nslookup`, `arp`) to isolate the fault layer.
4. Diagnose and resolve DHCP, DNS, and wireless connectivity problems.
5. Document each troubleshooting step and the resolution in a fault record.

---

## 1.0 Introduction to Network Troubleshooting

**Network troubleshooting** is the systematic process of identifying, isolating, and resolving faults that prevent network devices from communicating as intended. Effective troubleshooting is not guesswork — it follows a defined methodology that narrows the problem space efficiently.

A skilled technician:
- Gathers information before making changes.
- Forms a hypothesis about the cause.
- Tests the hypothesis with the least disruptive action first.
- Documents every step and the outcome.
- Verifies that the fix resolves the original problem without creating new ones.

---

## 2.0 Troubleshooting Methodologies

Three structured approaches are widely used. The technician selects the most appropriate method based on the nature of the reported fault.

### 2.1 Bottom-Up (OSI Layer 1 → Layer 7)

Start at the physical layer and work upward. Best when the fault is unknown or when physical connectivity is in doubt.

| Step | Layer | Check |
|------|-------|-------|
| 1 | Physical (L1) | Cable connected? LED indicators on? Port active? |
| 2 | Data Link (L2) | Correct VLAN? Port mode (access/trunk)? MAC address in switch table? |
| 3 | Network (L3) | Correct IP/mask/gateway? Routing table correct? ARP entry present? |
| 4 | Transport (L4) | Firewall blocking port? ACL denying traffic? |
| 5 | Application (L7) | Service running? Correct DNS name? Correct credentials? |

### 2.2 Top-Down (OSI Layer 7 → Layer 1)

Start at the application layer and work downward. Best when a specific application fails but others work (suggests application-layer or transport-layer issue).

### 2.3 Divide and Conquer

Start at the middle (Layer 3) and work in the direction indicated by the result. If Layer 3 is functional, move up; if not, move down. Best for experienced technicians who can make an educated guess about the fault layer.

---

## 3.0 Layer 1 — Physical Layer Faults

### 3.1 Indicators

- Link LED on switch port or NIC is off or amber (should be green for an active link).
- `ipconfig` shows "Media disconnected."
- `ping` to all targets fails, including the loopback address **127.0.0.1** (this indicates a TCP/IP stack issue, not cabling).
- A specific port on the switch has no active link LED.

### 3.2 Common Physical Faults and Resolutions

| Fault | Symptom | Resolution |
|-------|---------|------------|
| Unplugged or loose cable | Link LED off; "Media disconnected" in `ipconfig` | Reseat the RJ-45 connector; replace the patch cable |
| Wrong cable type | No link or link but no data (in very old equipment) | Straight-through cable for PC-to-switch; crossover for PC-to-PC (modern NICs auto-detect — MDI/MDIX) |
| Damaged cable (kink, crush, or cut) | Intermittent connectivity or no link | Use a cable tester to identify the faulty segment; replace the cable |
| Port speed/duplex mismatch | Very slow throughput; high collisions; CRC errors | Set both ends to auto-negotiate, or manually match speed and duplex on both ends |
| NIC failure | Permanent "Media disconnected"; no link LED on switch | Test with a known-good NIC; check Device Manager for errors |
| Faulty switch port | Only one device has no link despite working cable | Move device to a different port; test the original port with a known-good device |
| Cable run exceeds 100 m | Intermittent connectivity; high error rate | Re-route cable; add a switch or repeater at the midpoint |
| PoE insufficient | Wireless AP powers on and off repeatedly | Verify PoE switch port provides adequate wattage (802.3af = 15.4 W; 802.3at = 30 W) |

### 3.3 Using a Cable Tester

A cable tester sends a signal on each conductor and verifies continuity. Common results:

| Result | Meaning |
|--------|---------|
| All pins pass | Cable is correctly wired and continuous |
| Open circuit on pin N | Wire N is broken or not connected at one end |
| Short circuit between pins M and N | Two wires are making contact — crimping error or crush damage |
| Reversed pair | Pair wired correctly but reversed end-to-end — communication may still work for some speeds but will fail at others |
| Wrong wiring pattern | Cable crimped to wrong standard (mix of T568A and T568B) — rewire one end |

---

## 4.0 Layer 2 — Data Link Layer Faults

### 4.1 Common Layer 2 Faults

| Fault | Symptom | Diagnostic Command | Resolution |
|-------|---------|-------------------|------------|
| Wrong VLAN on access port | Device cannot reach gateway or other devices on the same subnet | `show vlan brief` (switch); `arp -a` (PC — no gateway entry) | Assign the correct VLAN to the port: `switchport access vlan <id>` |
| Trunk port not configured | Devices on different switches cannot communicate; inter-VLAN routing fails | `show interfaces trunk` — port missing from trunk list | Configure the uplink port as a trunk: `switchport mode trunk` |
| Native VLAN mismatch | Spanning-tree CDP error message; native VLAN traffic dropped | `show cdp neighbors detail` — check native VLAN mismatch warning | Set the same native VLAN on both ends of the trunk |
| Port in err-disabled state | Device cannot connect; port LED is amber; `show interfaces` shows `err-disabled` | `show interfaces FastEthernet0/1` | Identify the cause (port security violation, BPDU guard); fix the cause; then `shutdown` / `no shutdown` on the port |
| Spanning Tree loop | Extremely slow network or broadcast storm; high CPU on switches | `show spanning-tree` — look for ports in forwarding state where they should be blocking | Verify STP is enabled; check for rogue switches; configure PortFast on access ports |
| MAC address table full | New devices cannot communicate; switch floods all ports | `show mac address-table count` | Investigate cause; enable port security to limit MAC addresses per port |

### 4.2 Checking the MAC Address Table

```
SW1# show mac address-table
          Mac Address Table
-------------------------------------------
Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
  20    00aa.bbcc.ddee    DYNAMIC     Fa0/1
  20    00aa.bbcc.ddef    DYNAMIC     Fa0/2
```

If a device's MAC address does not appear in the table on the port it is connected to, the switch is not receiving frames from that device — the physical connection or NIC is faulty.

---

## 5.0 Layer 3 — Network Layer Faults

### 5.1 IP Address Configuration Errors

| Fault | Symptom | Diagnostic | Resolution |
|-------|---------|------------|------------|
| Incorrect IP address | Cannot reach other devices; wrong subnet | `ipconfig /all` — compare to specification | Reconfigure IP address to match specification |
| Incorrect subnet mask | Can reach some devices on the subnet but not others; gateway unreachable | `ipconfig /all` — verify mask | Correct the subnet mask |
| Missing or incorrect default gateway | Can reach devices on the same subnet but not other subnets or internet | `ping <gateway>` fails; `ipconfig` shows wrong or no gateway | Set the correct gateway IP |
| APIPA address (169.254.x.x) | Cannot reach DHCP server; no valid IP assigned | `ipconfig /all` — shows APIPA; DHCP server unreachable | Check DHCP server status; verify switch VLAN assignment; check DHCP scope |
| Duplicate IP address | Intermittent connectivity; Windows shows "IP address conflict" warning | `arp -a` — two devices respond to the same IP | Assign a unique IP to the conflicting device; add IP to DHCP exclusions |

### 5.2 Routing Faults

| Fault | Symptom | Diagnostic | Resolution |
|-------|---------|------------|------------|
| Missing route | Cannot reach a specific subnet; all other subnets reachable | `tracert <destination>` — fails at the router; `show ip route` — route missing | Add a static route: `ip route <network> <mask> <next-hop>` |
| Incorrect static route | Traffic sent to the wrong next-hop | `tracert` shows unexpected path | Delete incorrect route; add correct route |
| NAT not configured | Internal hosts cannot reach the internet; external ping works to router WAN IP | `ping 8.8.8.8` from internal host fails; `ping 8.8.8.8` from router succeeds | Verify NAT access list and `ip nat inside`/`ip nat outside` on interfaces |
| Default route missing | Cannot reach the internet | `show ip route` — no `0.0.0.0/0` entry | Add default route: `ip route 0.0.0.0 0.0.0.0 <ISP next-hop>` |

---

## 6.0 DHCP Troubleshooting

| Fault | Symptom | Diagnostic | Resolution |
|-------|---------|------------|------------|
| DHCP scope exhausted | New clients get APIPA address; existing clients keep their address | Check DHCP server — pool statistics show 0 available | Expand the pool; reduce lease duration; identify IP hoarders |
| Gateway not excluded from pool | Gateway device receives a dynamic IP; routing fails intermittently | Check DHCP pool configuration | Add `ip dhcp excluded-address <gateway-ip>` |
| DHCP server stopped/service down | All clients get APIPA; `ipconfig /renew` fails | Check DHCP server services panel; `show running-config` | Start the DHCP service; verify the pool is not deleted |
| DHCP relay not configured (multi-subnet) | Clients on a remote subnet cannot get a DHCP address | `ipconfig /renew` times out; DHCP server on a different subnet | Configure `ip helper-address <DHCP-server-IP>` on the router interface facing the client subnet |
| Wrong DNS server in DHCP scope | Clients get an IP but cannot resolve hostnames | `nslookup` fails or returns wrong server; `ipconfig /all` — check DNS | Update DHCP scope DNS to the correct server address |
| DHCP conflict after static assignment | Client with DHCP occasionally gets an IP already used by a static device | Duplicate IP warning | Add all static IPs to `ip dhcp excluded-address` list |

---

## 7.0 DNS Troubleshooting

| Fault | Symptom | Diagnostic | Resolution |
|-------|---------|------------|------------|
| DNS server unreachable | `nslookup` times out; can `ping 8.8.8.8` but not `ping www.google.com` | `ping <DNS server IP>` — fails | Check DNS server status and firewall rules (allow UDP/TCP port 53) |
| Wrong DNS server configured | `nslookup` contacts wrong server; cannot resolve internal names | `nslookup` output — server address does not match specification | Correct DNS server address in IP configuration or DHCP scope |
| DNS forwarder not set | Internal names resolve but external names fail | `nslookup www.google.com` — fails; `nslookup fileserver.office.local` — succeeds | Configure the DNS forwarder to an external resolver (e.g., 8.8.8.8) |
| Stale DNS cache | Old IP address returned for a hostname that has changed | `nslookup <hostname>` returns old IP | Run `ipconfig /flushdns` on the client; clear DNS cache on the server |
| Missing DNS record for internal host | Internal hostname cannot be resolved | `nslookup fileserver.office.local` — "Non-existent domain" | Add the A record in the DNS server for the host |

---

## 8.0 Wireless Connectivity Troubleshooting

| Fault | Symptom | Diagnostic | Resolution |
|-------|---------|------------|------------|
| SSID not visible | Client cannot find the wireless network | Check AP — SSID broadcast enabled? AP powered on and associated? | Enable SSID broadcast; verify AP has power and is associated to the controller |
| Wrong passphrase | Client connects but authentication fails | Client shows "Incorrect password" or "Authentication failed" | Verify passphrase on AP; re-enter on client |
| IP not obtained after Wi-Fi connection | Client connected to SSID but shows "No Internet"; APIPA address | `ipconfig /all` on client — APIPA; `ping` DHCP server fails | Check DHCP scope for the wireless VLAN; check VLAN assignment on AP port |
| Weak signal / intermittent connection | Slow speeds; frequent disconnection | Check signal strength indicator; move client closer to AP | Reposition AP; reduce interference; select non-overlapping channel |
| Channel interference | Slow speeds in crowded environments (offices, malls) | Use Wi-Fi analyser app to see channel usage | Change AP channel to a less congested channel (1, 6, or 11 for 2.4 GHz) |
| Wrong security mode | Cannot connect; authentication error | Check AP security setting | Match security mode on AP and client — use WPA2-AES |
| IP address pool not covering wireless clients | Wired clients work; wireless clients get APIPA | Check DHCP pool size vs. number of wireless clients | Expand pool or create a dedicated pool for the wireless VLAN |

---

## 9.0 Fault Documentation — Fault Record

Every troubleshooting session must be documented. The fault record provides a history for pattern analysis and a reference for recurrence.

| Field | Content |
|-------|---------|
| Fault ID | Unique identifier (e.g., FLT-2026-001) |
| Date and time reported | When the fault was first reported |
| Reported by | Name and department of the person who reported the fault |
| Affected device(s) | Hostname, IP address, location |
| Fault description | What the user observed ("cannot access the internet", "cannot see shared folder") |
| Initial diagnostic steps | Commands run and results observed |
| Root cause identified | The specific misconfiguration or hardware failure that caused the fault |
| Resolution applied | Exact change made (e.g., "corrected VLAN 20 assignment on Fa0/3"; "replaced patch cable from PC-01 to patch panel port 3") |
| Verification | How it was confirmed that the fix resolved the problem (e.g., `ping 8.8.8.8` — 4 replies, 0% loss) |
| Time to resolve | Duration from report to resolution |
| Technician name | Who performed the troubleshooting |
| Sign-off | User or supervisor signature confirming resolution |

---

## 10.0 Common Errors in Troubleshooting

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Making multiple changes at once | Cannot identify which change fixed the problem; may introduce new faults | Make one change at a time; test after each change |
| Not gathering information before acting | Time wasted on the wrong layer | Ask the user what has changed recently; run `ipconfig` and `ping` before touching any device |
| Fixing symptoms, not the root cause | Fault recurs after a short time | Always confirm the root cause before closing the fault record |
| Forgetting to save configuration after fix | Fix is lost on device reboot | Run `copy running-config startup-config` after every configuration change |
| Not documenting the resolution | Same fault takes as long to resolve next time | Complete the fault record immediately after resolution while details are fresh |
| Overlooking the host firewall | Fault persists despite correct network configuration | Test with host firewall temporarily disabled; re-enable after testing |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCu 6
- Cisco Networking Academy — CCNA: Enterprise Networking, Security, and Automation (Troubleshooting modules)
- CompTIA Network+ Certification Study Guide — Chapter on Network Troubleshooting Methodology
- Microsoft Learn — Troubleshoot TCP/IP connectivity in Windows
- Tanenbaum, A.S. & Wetherall, D.J. (2011). *Computer Networks* (5th ed.). Pearson. Chapter 5: Network Layer
- Odom, W. (2020). *CCNA 200-301 Official Cert Guide Volume 1*. Cisco Press. Part III: Implementing VLANs and STP