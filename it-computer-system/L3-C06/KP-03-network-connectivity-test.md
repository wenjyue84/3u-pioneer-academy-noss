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
| NO. KOD | IT-020-3:2013-C06/KP(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-network-connectivity-test

**TUJUAN:** Kertas rujukan untuk KP-03-network-connectivity-test.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose of network connectivity testing after configuration.
2. Use `ping`, `ipconfig`/`ifconfig`, `tracert`/`traceroute`, `nslookup`, and `netstat` to verify connectivity.
3. Interpret the output of each diagnostic command to confirm or deny successful connectivity.
4. Apply a structured testing methodology from Layer 1 to Layer 7.
5. Document connectivity test results in a structured test record.

---

## 1.0 Introduction to Connectivity Testing

Network connectivity testing is performed after configuration to verify that every device can communicate as specified. Testing is not optional — it is a mandatory step before handing over the network to the end user or client.

A structured testing approach follows the **bottom-up OSI model methodology**: verify physical connectivity first, then data link, then network, and so on. This approach prevents wasted time — there is no point testing IP reachability if the cable is unplugged.

Testing must be performed:
- After initial configuration (baseline test).
- After any change to the network (change verification test).
- Before formal handover (acceptance test).

All test results must be recorded — pass, fail, or partial — with the date, tester name, and any notes.

---

## 2.0 Testing Tools Overview

### 2.1 Command-Line Diagnostic Tools

| Tool | Operating System | Function |
|------|-----------------|----------|
| `ipconfig` | Windows | Displays IP address, subnet mask, default gateway, DNS, and DHCP lease information for all network adapters |
| `ifconfig` / `ip addr` | Linux/macOS | Displays and configures network interface IP settings |
| `ping` | Windows, Linux, macOS | Tests reachability of a host by sending ICMP Echo Request packets and measuring the response |
| `tracert` | Windows | Traces the path packets take to reach a destination, showing each router hop and round-trip time |
| `traceroute` | Linux/macOS | Same function as `tracert` |
| `nslookup` | Windows, Linux, macOS | Queries DNS servers to resolve hostnames to IP addresses and vice versa |
| `netstat` | Windows, Linux, macOS | Displays active connections, listening ports, and network statistics |
| `arp -a` | Windows, Linux | Displays the ARP (Address Resolution Protocol) cache — IP-to-MAC address mappings |
| `pathping` | Windows | Combines `ping` and `tracert`; shows packet loss at each hop over multiple rounds |

---

## 3.0 `ipconfig` — Verifying IP Configuration

`ipconfig` is the first tool used after configuring a Windows device. It confirms that the correct IP address, subnet mask, gateway, and DNS server have been applied.

### 3.1 Command Syntax

| Command | Description |
|---------|-------------|
| `ipconfig` | Shows IP address, subnet mask, and default gateway for all adapters |
| `ipconfig /all` | Shows full details including MAC address, DHCP enabled/disabled, DHCP server, DNS servers, lease obtained, and lease expires |
| `ipconfig /release` | Releases the current DHCP-assigned IP address |
| `ipconfig /renew` | Requests a new IP address from the DHCP server |
| `ipconfig /flushdns` | Clears the local DNS resolver cache |
| `ipconfig /displaydns` | Shows the contents of the local DNS cache |

### 3.2 Interpreting `ipconfig /all` Output

```
Ethernet adapter Local Area Connection:
   Connection-specific DNS Suffix . : office.local
   Physical Address. . . . . . . . . : 00-1A-2B-3C-4D-5E
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.10.105 (Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Lease Obtained. . . . . . . . . . : Monday, 23 June 2026 08:00:00
   Lease Expires . . . . . . . . . . : Monday, 23 June 2026 16:00:00
   Default Gateway . . . . . . . . . : 192.168.10.1
   DHCP Server . . . . . . . . . . . : 192.168.10.1
   DNS Servers . . . . . . . . . . . : 192.168.10.10
                                       8.8.8.8
```

**Verification checklist:**
- IP address is within the expected subnet and DHCP pool range. ✓
- Subnet mask matches the specification. ✓
- Default gateway is the router LAN interface IP. ✓
- DHCP server is the expected device. ✓
- DNS servers are the specified addresses. ✓
- Lease duration is as configured. ✓

**Red flags:**
- IP address starts with `169.254.x.x` — APIPA (Automatic Private IP Addressing) address assigned when DHCP fails. The device cannot reach the DHCP server.
- Gateway is `0.0.0.0` — no gateway assigned; device cannot communicate beyond its subnet.

---

## 4.0 `ping` — Testing Reachability

`ping` sends **ICMP (Internet Control Message Protocol) Echo Request** packets to a target host and waits for **Echo Reply** packets. It measures:
- Whether the target is reachable.
- Round-trip time (RTT) in milliseconds.
- Packet loss percentage.

### 4.1 Command Syntax (Windows)

| Command | Description |
|---------|-------------|
| `ping 192.168.10.1` | Sends 4 ICMP echo requests to the specified IP |
| `ping -t 192.168.10.1` | Continuous ping until stopped with Ctrl+C |
| `ping -n 10 192.168.10.1` | Sends 10 packets |
| `ping -l 1000 192.168.10.1` | Sends packets of 1000 bytes (tests for MTU / fragmentation issues) |
| `ping -a 192.168.10.1` | Resolves IP to hostname before pinging |

### 4.2 Structured Ping Test Sequence

Ping tests must follow a structured sequence from local to remote:

| Step | Target | Purpose |
|------|--------|---------|
| 1 | `ping 127.0.0.1` | Loopback test — verifies TCP/IP stack is functional on the local device |
| 2 | `ping <own IP>` | Verifies NIC and driver are correctly installed |
| 3 | `ping <default gateway>` | Verifies Layer 3 connectivity to the router on the local subnet |
| 4 | `ping <device on same subnet>` | Verifies intra-subnet communication via the switch |
| 5 | `ping <device on different subnet>` | Verifies inter-VLAN routing or routing between subnets |
| 6 | `ping <DNS server>` | Verifies reachability of the DNS server |
| 7 | `ping 8.8.8.8` | Verifies internet reachability via NAT/WAN (use a known public IP) |
| 8 | `ping www.google.com` | Verifies DNS resolution and internet connectivity together |

### 4.3 Interpreting `ping` Output

**Successful ping:**
```
Reply from 192.168.10.1: bytes=32 time=1ms TTL=64
Reply from 192.168.10.1: bytes=32 time=1ms TTL=64
Reply from 192.168.10.1: bytes=32 time=1ms TTL=64
Reply from 192.168.10.1: bytes=32 time=1ms TTL=64
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

**Failed ping:**
```
Request timed out.
Request timed out.
Packets: Sent = 4, Received = 0, Lost = 4 (100% loss)
```

**Possible causes of `Request timed out`:**
- Target device is offline or powered off.
- Firewall on the target is blocking ICMP.
- Incorrect IP address or subnet mask on either device.
- Missing or incorrect default gateway.
- Routing problem between subnets.
- Physical connectivity failure (cable, port, NIC).

**TTL (Time to Live):** Each router hop decrements TTL by 1. An initial TTL of 64 (Linux/macOS) or 128 (Windows) that appears low in a ping reply indicates many hops to the destination or a routing loop.

---

## 5.0 `tracert` / `traceroute` — Tracing the Path

`tracert` (Windows) and `traceroute` (Linux/macOS) reveal the path packets take to reach a destination. Each line represents one router hop, showing the hop number, IP address of the router interface, and the round-trip time for three probes.

### 5.1 Command Syntax

| Command | Description |
|---------|-------------|
| `tracert 8.8.8.8` | Traces path to Google's DNS server (Windows) |
| `tracert -d 8.8.8.8` | Does not resolve IP addresses to hostnames (faster) |
| `traceroute 8.8.8.8` | Linux equivalent |

### 5.2 Interpreting `tracert` Output

```
Tracing route to 8.8.8.8 over a maximum of 30 hops:

  1    1 ms    1 ms    1 ms   192.168.10.1         ← Default gateway (office router)
  2   12 ms   11 ms   12 ms   10.0.0.1             ← ISP router
  3   15 ms   14 ms   15 ms   172.16.0.1           ← ISP core
  4   20 ms   19 ms   21 ms   8.8.8.8              ← Destination
```

**Interpreting `* * *` (asterisks):**
- Indicates no response at that hop — the router may block ICMP Time Exceeded messages.
- Does not necessarily mean a failure — the connection may still succeed beyond the asterisk.
- If all hops from a certain point show `* * *` and the final destination is unreachable, there is a routing or firewall problem at that hop.

**Use case:** If `ping 8.8.8.8` fails, run `tracert 8.8.8.8` to identify at which hop packets stop — this pinpoints the failing device or link.

---

## 6.0 `nslookup` — DNS Resolution Testing

`nslookup` (Name Server Lookup) queries DNS servers to verify that hostname-to-IP and IP-to-hostname resolution is working correctly.

### 6.1 Command Syntax

| Command | Description |
|---------|-------------|
| `nslookup www.google.com` | Resolves hostname to IP using the default DNS server |
| `nslookup 8.8.8.8` | Reverse lookup — resolves IP to hostname |
| `nslookup www.google.com 8.8.8.8` | Queries a specific DNS server (8.8.8.8) |
| `nslookup fileserver.office.local` | Resolves an internal hostname |

### 6.2 Interpreting `nslookup` Output

**Successful resolution:**
```
Server:  192.168.10.10
Address:  192.168.10.10

Non-authoritative answer:
Name:    www.google.com
Addresses:  142.250.195.100
```
- **Server** — the DNS server that responded (should match the specification).
- **Non-authoritative answer** — the DNS server provided the answer from its cache or via forwarding (normal for external queries).

**Failed resolution:**
```
Server:  192.168.10.10
Address:  192.168.10.10

*** 192.168.10.10 can't find www.google.com: Server failed
```
- The DNS server is reachable but cannot resolve the name — check the forwarder configuration.

```
DNS request timed out.
timeout was 2 seconds.
*** Request to 192.168.10.10 timed-out
```
- The DNS server is not reachable — check IP configuration and firewall rules on the DNS server.

---

## 7.0 `netstat` — Viewing Active Connections

`netstat` displays active TCP/UDP connections and listening ports. It is useful for verifying that a service is running and for identifying unexpected connections.

| Command | Description |
|---------|-------------|
| `netstat -a` | Shows all active connections and listening ports |
| `netstat -n` | Shows addresses as IP:port numbers (no hostname resolution) |
| `netstat -an` | Combines above — all connections, numeric format |
| `netstat -b` | Shows the executable associated with each connection (Windows; requires admin) |
| `netstat -r` | Displays the local routing table |

**Example use case:** After configuring a DHCP server, run `netstat -an` and look for UDP port 67 (DHCP server) in LISTENING state — this confirms the DHCP service is active.

---

## 8.0 `arp -a` — Verifying Layer 2 Reachability

The **ARP cache** maps IP addresses to MAC addresses on the local subnet. After a successful ping, the target's MAC address should appear in the ARP cache.

```
C:\> arp -a

Interface: 192.168.10.105 --- 0x4
  Internet Address      Physical Address      Type
  192.168.10.1          00-aa-bb-cc-dd-ee     dynamic
  192.168.10.10         00-11-22-33-44-55     dynamic
```

**Use:** If `ping` to the gateway succeeds but no entry appears in `arp -a`, there may be a Layer 2 problem (wrong VLAN, trunk misconfiguration, or switch loop).

**`arp -d *`** (Windows) — clears the ARP cache. Useful when you suspect a stale ARP entry is causing a connectivity issue after an IP address change.

---

## 9.0 Structured Connectivity Test Record

All test results must be recorded. A structured test record provides evidence that the network was verified and serves as a reference for future troubleshooting.

| Test No. | Test Description | Command Used | Expected Result | Actual Result | Pass / Fail | Notes |
|----------|-----------------|--------------|-----------------|---------------|-------------|-------|
| 1 | Loopback test on PC-01 | `ping 127.0.0.1` | 4 replies, 0% loss | 4 replies, 0% loss | Pass | |
| 2 | PC-01 own IP test | `ping 192.168.10.105` | 4 replies, 0% loss | 4 replies, 0% loss | Pass | |
| 3 | PC-01 to gateway | `ping 192.168.10.1` | 4 replies, 0% loss | 4 replies, 0% loss | Pass | |
| 4 | PC-01 to DNS server | `ping 192.168.10.10` | 4 replies, 0% loss | Request timed out | Fail | Firewall blocking ICMP on server — verified DNS resolution works via nslookup |
| 5 | DNS resolution — internal | `nslookup fileserver.office.local` | Returns 192.168.10.10 | Returns 192.168.10.10 | Pass | |
| 6 | DNS resolution — external | `nslookup www.google.com` | Returns valid IP | Returns 142.250.195.100 | Pass | |
| 7 | Internet reachability | `ping 8.8.8.8` | 4 replies, 0% loss | 4 replies, 0% loss | Pass | |
| 8 | Path trace to internet | `tracert 8.8.8.8` | Reaches 8.8.8.8 in ≤10 hops | 4 hops | Pass | |
| 9 | PC-01 to PC-02 (same VLAN) | `ping 192.168.10.106` | 4 replies, 0% loss | 4 replies, 0% loss | Pass | |
| 10 | PC-01 to Server-VLAN (inter-VLAN) | `ping 192.168.20.10` | 4 replies, 0% loss | 4 replies, 0% loss | Pass | Inter-VLAN routing via Layer 3 switch confirmed |
| 11 | Wireless client connectivity | `ping 192.168.10.1` from laptop | 4 replies, 0% loss | 4 replies, 0% loss | Pass | WPA2-AES authenticated |

---

## 10.0 Common Errors in Connectivity Testing

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Pinging by hostname when DNS is not yet verified | Failure misdiagnosed as connectivity problem (is actually DNS problem) | Always ping by IP first; test DNS separately with `nslookup` |
| Not following the structured test sequence | Root cause hard to identify | Always test from loopback outward (Steps 1–8 in Section 4.2) |
| Concluding failure from one `ping` packet loss | Transient congestion misdiagnosed as permanent failure | Use `-t` for continuous ping; accept ≤1% loss as acceptable on a LAN |
| Ignoring firewall as a cause of `ping` failure | Misconfiguration left in place | Test with `nslookup` and `netstat` if `ping` fails — ICMP may be blocked by host firewall |
| Not recording test results | No evidence for handover or future troubleshooting | Use a structured test record for every connectivity test |
| Testing only the directly connected device | Downstream connectivity failures missed | Test end-to-end — from the furthest end device to the internet |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCu 6
- Microsoft Learn — `ipconfig`, `ping`, `tracert`, `nslookup`, `netstat` command references
- Cisco Networking Academy — CCNA: Introduction to Networks (Module 17: Build a Small Network)
- CompTIA Network+ Certification Study Guide — Chapter on Network Troubleshooting Tools
- Forouzan, B.A. (2013). *Data Communications and Networking* (5th ed.). McGraw-Hill. Chapter on ICMP