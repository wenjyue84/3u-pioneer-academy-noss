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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/KP(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** Block inbound Telnet (port 23)

**TUJUAN:** New-NetFirewallRule -DisplayName "Block Telnet Inbound" `

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the function and types of firewalls used in computer system security
2. Configure Windows Defender Firewall with Advanced Security using inbound and outbound rules
3. Describe network segmentation strategies including VLANs and DMZ
4. Identify and disable unnecessary network services and ports to reduce the attack surface
5. Explain the role of Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS) in network security

---

## 1.0 Introduction to Firewall and Network Security

A firewall (tembok api) is a network security device or software that monitors and controls incoming and outgoing network traffic based on predefined security rules. It establishes a boundary between trusted internal networks and untrusted external networks (such as the internet).

Network security extends beyond the firewall to include the design of the network itself — how it is segmented, what services are exposed, and how traffic between zones is controlled. A systems administrator at Level 4 must be able to configure both host-based and network-level controls.

---

## 2.0 Types of Firewalls

| Type | Malay | How It Works | Advantages | Limitations |
|------|-------|-------------|------------|-------------|
| Packet Filter | Penapis Paket | Inspects each packet's source/destination IP, port, and protocol against a ruleset | Fast; low overhead | Cannot inspect packet contents or application layer |
| Stateful Inspection | Pemeriksaan Keadaan | Tracks active connections; allows return traffic for established sessions | More intelligent than packet filter; blocks unsolicited inbound | Higher resource usage |
| Application Layer (Proxy) | Lapisan Aplikasi | Inspects full application-layer content (HTTP, FTP, DNS); can block specific content | Deep inspection; content filtering possible | Slower; may break some applications |
| Next-Generation Firewall (NGFW) | Tembok Api Generasi Baharu | Combines stateful inspection + application awareness + IPS + user identity | Comprehensive; integrates multiple functions | Higher cost; complex configuration |
| Host-Based Firewall | Tembok Api Berasaskan Hos | Software firewall running on an individual host (e.g. Windows Defender Firewall) | Protects individual machine regardless of network position | Must be managed on each host |

---

## 3.0 Windows Defender Firewall with Advanced Security

Windows Defender Firewall with Advanced Security (WDFAS) is the host-based firewall built into Windows Server and Windows desktop operating systems. It is managed via the `wf.msc` console, Group Policy, or PowerShell.

### 3.1 Rule Types

| Rule Type | Direction | Purpose |
|-----------|-----------|---------|
| Inbound Rule | Traffic entering the host | Block or allow traffic from the network to the local machine |
| Outbound Rule | Traffic leaving the host | Block or allow traffic from the local machine to the network |
| Connection Security Rule | Both | Configure IPsec between endpoints (authentication, encryption of traffic) |

### 3.2 Creating a Firewall Rule (Windows)

**Via GUI (wf.msc):**

| Step | Action |
|------|--------|
| 1 | Open `wf.msc` → Inbound Rules → New Rule |
| 2 | Select Rule Type: Port / Program / Predefined / Custom |
| 3 | Specify protocol (TCP/UDP) and port number(s) |
| 4 | Select action: Allow / Block / Allow if Secure (IPsec) |
| 5 | Select profiles: Domain / Private / Public |
| 6 | Name the rule descriptively (e.g. "Block Telnet Port 23 Inbound") |

**Via PowerShell:**

```powershell
# Block inbound Telnet (port 23)
New-NetFirewallRule -DisplayName "Block Telnet Inbound" `
    -Direction Inbound -Protocol TCP -LocalPort 23 `
    -Action Block -Profile Domain,Private,Public

# Allow RDP only from admin subnet
New-NetFirewallRule -DisplayName "Allow RDP from Admin VLAN" `
    -Direction Inbound -Protocol TCP -LocalPort 3389 `
    -RemoteAddress 192.168.10.0/24 -Action Allow -Profile Domain
```

### 3.3 Common Firewall Rules for a Server

| Rule | Direction | Protocol | Port | Action | Justification |
|------|-----------|----------|------|--------|---------------|
| Allow DNS | Inbound | UDP/TCP | 53 | Allow from internal only | Name resolution for internal clients |
| Allow HTTPS | Inbound | TCP | 443 | Allow | Web service access |
| Allow RDP from admin VLAN | Inbound | TCP | 3389 | Allow (restricted source) | Remote administration |
| Block Telnet | Inbound | TCP | 23 | Block | Cleartext protocol; use SSH instead |
| Block SMB from internet | Inbound | TCP | 445 | Block (external source) | Prevent WannaCry-type attacks |
| Allow Windows Update | Outbound | TCP | 443 | Allow to Microsoft IPs | Patch management |

---

## 4.0 Network Segmentation

### 4.1 Purpose of Segmentation

Network segmentation (pembahagian rangkaian) divides a network into smaller, isolated zones. This limits lateral movement — if one zone is compromised, the attacker cannot easily reach other zones.

### 4.2 Virtual LAN (VLAN)

A VLAN (Virtual Local Area Network) is a logical network created on a managed switch that groups devices regardless of their physical location.

| VLAN | Example Devices | Traffic Policy |
|------|----------------|---------------|
| VLAN 10 — Management | Servers, network devices | Accessible only from admin workstations (VLAN 50) |
| VLAN 20 — Users | Staff workstations, laptops | Internet access; restricted access to servers |
| VLAN 30 — Printers | Network printers | Print traffic only; no internet access |
| VLAN 40 — Guest | Visitor Wi-Fi | Internet only; isolated from internal VLANs |
| VLAN 50 — Admin | IT administrator workstations | Full access to all VLANs |

### 4.3 DMZ (Demilitarised Zone)

A DMZ (zon neutralisasi) is a network segment that sits between the internet and the internal network. Public-facing servers (web, email, DNS) are placed in the DMZ so that if they are compromised, the attacker cannot directly reach the internal network.

```
Internet → [External Firewall] → DMZ (Web/Mail/DNS servers) → [Internal Firewall] → Internal LAN
```

---

## 5.0 Reducing the Attack Surface

### 5.1 Disable Unnecessary Services

Every running service is a potential entry point. The principle of attack surface reduction (pengurangan permukaan serangan) requires disabling all services that are not needed.

**Common services to review on Windows Server:**

| Service | Default State | Action |
|---------|--------------|--------|
| Telnet | Disabled | Leave disabled; use SSH |
| FTP Server | Disabled | Leave disabled; use SFTP or FTPS |
| Remote Registry | Running | Disable unless specifically required |
| Print Spooler (on non-print servers) | Running | Disable (PrintNightmare vulnerability) |
| NetBIOS over TCP/IP | Enabled | Disable on modern AD environments |

**PowerShell — Disable a service:**
```powershell
Set-Service -Name "TlntSvr" -StartupType Disabled
Stop-Service -Name "TlntSvr"
```

### 5.2 Close Unnecessary Ports

Use `netstat -an` or `Get-NetTCPConnection` (PowerShell) to list listening ports. Any port that is not required by a documented and approved service should be closed via firewall rule or by stopping the associated service.

### 5.3 Network Protocols — Security Best Practice

| Protocol | Issue | Secure Alternative |
|----------|-------|-------------------|
| Telnet (port 23) | Cleartext; credentials visible in network capture | SSH (port 22) |
| FTP (port 21) | Cleartext file transfer | SFTP (port 22) or FTPS (port 990) |
| HTTP (port 80) | Unencrypted web traffic | HTTPS (port 443) with valid TLS certificate |
| SNMP v1/v2c | Community string transmitted in cleartext | SNMP v3 with authentication and encryption |
| NTLMv1 | Weak authentication protocol; relay attacks | Disable NTLMv1; enforce NTLMv2 or Kerberos |

---

## 6.0 Intrusion Detection and Prevention Systems

| System | Malay | Function |
|--------|-------|----------|
| IDS (Intrusion Detection System) | Sistem Pengesanan Pencerobohan | Monitors traffic and generates alerts when suspicious patterns are detected; does NOT block traffic |
| IPS (Intrusion Prevention System) | Sistem Pencegahan Pencerobohan | Monitors traffic and actively blocks suspicious traffic in real time |

### 6.1 IDS/IPS Detection Methods

| Method | Description |
|--------|-------------|
| Signature-based | Matches traffic against a database of known attack signatures; fast but cannot detect new attacks |
| Anomaly-based | Establishes a baseline of normal traffic and alerts on deviations; can detect unknown attacks but may generate false positives |
| Policy-based | Alerts when traffic violates a defined security policy (e.g. forbidden protocol used) |

### 6.2 Placement in the Network

- **Network IDS/IPS** — Deployed inline or in monitoring mode at network chokepoints (e.g. between the internet and DMZ)
- **Host-based IDS (HIDS)** — Installed on individual servers; monitors system calls, file changes, and local logs

---

## 7.0 Common Errors in Firewall and Network Security Configuration

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Using "Allow All" default rules | All traffic passes; firewall provides no protection | Set default rule to Deny All; add explicit allow rules only |
| Not restricting RDP to admin subnet | RDP exposed to the internet; brute-force and exploit risk | Restrict RDP source to admin VLAN or VPN; use MFA |
| Leaving unused ports open | Increases attack surface unnecessarily | Audit open ports monthly; close all ports without an approved service |
| No egress (outbound) filtering | Malware can freely communicate with command-and-control servers | Apply outbound rules; allow only known-good destinations |
| Firewall rules not documented | Rogue rules accumulate; purpose of old rules unknown | Maintain a firewall rule register with justification and review date for every rule |
| Ignoring host-based firewall | Network firewall bypassed via internal attacker or compromised machine | Enable and configure host-based firewall on all servers; enforce via GPO |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer System Security Control — CoCu 2
- Microsoft Documentation: Windows Defender Firewall with Advanced Security
- CIS Benchmark: Windows Server 2022 — Firewall and Network Configuration
- NIST SP 800-41 Rev 1: Guidelines on Firewalls and Firewall Policy
- CompTIA Security+ Study Guide — Domain: Architecture and Design (Network Security)
- Cisco: Introduction to VLANs and Network Segmentation