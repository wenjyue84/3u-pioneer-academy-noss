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
| KOD DAN NAMA PROGRAM | IT-020-4:2013 PENTADBIRAN SISTEM KOMPUTER |
| TAHAP | 4 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C02 COMPUTER SYSTEM SECURITY CONTROL |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY SECURITY REQUIREMENTS<br>2. IMPLEMENT ACCESS CONTROL AND AUTHENTICATION<br>3. CONFIGURE FIREWALL AND NETWORK SECURITY<br>4. MANAGE PATCHES AND SECURITY UPDATES<br>5. DOCUMENT SECURITY CONFIGURATION AND INCIDENTS |
| NO. KOD | IT-020-4:2013-C02/KT(3/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | MERAH JAMBU (Pink) |

**TAJUK:** KT-03-configure-firewall-network-security

**TUJUAN:** Kertas rujukan untuk KT-03-configure-firewall-network-security.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Arahan / Instructions

Answer ALL questions in ALL sections. Refer to KP(3/5) for guidance. Write your answers clearly in the answer booklet provided. This assignment is formative.

**Masa / Duration:** 1 hour

---

## Bahagian A: Soalan Pelbagai Pilihan / Section A: Multiple Choice (20 marks — 4 marks each)

**A1.** A stateful inspection firewall differs from a packet filter firewall because it:

- (a) Only inspects the destination IP address
- (b) Tracks the state of active connections and allows legitimate return traffic
- (c) Inspects application-layer content such as HTTP URLs
- (d) Only works with TCP traffic

**A2.** A DMZ (Demilitarised Zone) in network design is used to:

- (a) Store encrypted backups of internal servers
- (b) House public-facing servers in a zone separated from the internal LAN
- (c) Provide wireless access to guest users
- (d) Replace the internal firewall

**A3.** Which of the following protocols should be DISABLED and replaced with a secure alternative because it transmits credentials in cleartext?

- (a) HTTPS
- (b) SSH
- (c) Telnet
- (d) SFTP

**A4.** The principle of attack surface reduction means:

- (a) Enabling all available services to maximise functionality
- (b) Disabling all services including critical ones
- (c) Disabling all services and closing all ports that are not required
- (d) Installing a firewall on the internet router only

**A5.** An Intrusion Prevention System (IPS) differs from an Intrusion Detection System (IDS) because the IPS:

- (a) Only generates alerts without taking action
- (b) Actively blocks suspicious traffic in real time
- (c) Only monitors internal network segments
- (d) Uses only signature-based detection

---

## Bahagian B: Soalan Jawapan Pendek / Section B: Short Answer (30 marks)

**B1.** Compare and contrast THREE (3) types of firewalls. For each type, describe how it works and state one advantage and one limitation. (12 marks)

**B2.** Explain what a VLAN is and describe how VLAN segmentation improves network security. Provide an example of a VLAN design for a company with the following departments: IT Admin, Finance, General Staff, and Guest Wi-Fi. (9 marks)

**B3.** List FOUR (4) network protocols that pose a security risk and state the secure alternative for each. (4 marks)

**B4.** Describe the difference between signature-based and anomaly-based IDS/IPS detection. State one advantage and one disadvantage of each. (5 marks)

---

## Bahagian C: Soalan Situasi / Section C: Situational Question (50 marks)

**C1.** You are the systems administrator for an e-commerce company. The network consists of:
- Internal LAN with 50 staff workstations and 3 internal servers (file, email, database)
- One internet-facing web server handling customer orders
- One internet-facing payment gateway server

A recent penetration test report found the following issues:
- RDP (port 3389) is open and accessible from any IP address on the internet
- Telnet service is running and accessible on all servers
- All servers are on the same flat network with no segmentation
- No egress (outbound) filtering is applied
- The web server and payment gateway are on the same network segment as internal servers

(a) For each of the five issues identified in the penetration test report, explain the specific security risk it creates and recommend the corrective action to take. (25 marks)

(b) Design a segmented network architecture for this company using VLANs and a DMZ. Draw or describe the network zones, what devices belong in each zone, and what inter-zone traffic rules you would apply. (15 marks)

(c) Write the PowerShell commands to create the following Windows Defender Firewall rules on the web server: (i) Allow HTTPS (TCP 443) from Any; (ii) Allow RDP (TCP 3389) from the admin workstation IP 192.168.50.10 only; (iii) Block Telnet (TCP 23) from Any — inbound. (10 marks)

---

## Skema Jawapan / Answer Scheme

*To be provided by the instructor after submission.*

---

## Kriteria Penilaian / Assessment Criteria

| Section | Marks | Passing Standard |
|---------|-------|-----------------|
| A — Multiple Choice | 20 | Minimum 12/20 |
| B — Short Answer | 30 | Minimum 18/30 |
| C — Situational | 50 | Minimum 30/50 |
| **Total** | **100** | **Minimum 60/100** |