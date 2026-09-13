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
| NO. KOD | IT-020-3:2013-C06/KK(2/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | BIRU (Blue) |

**TAJUK:** KK-02-network-configuration

**TUJUAN:** Kertas rujukan untuk KK-02-network-configuration.

**ARAHAN:** Pelatih dikehendaki melaksanakan tugasan/kerja mengikut prosedur yang ditetapkan dalam kertas ini. Rujuk pensyarah sekiranya perlu penjelasan lanjut.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif / Objectives

By the end of this work activity, trainees will be able to:

1. Configure IP addresses, subnet masks, and default gateways on network devices.
2. Set up and configure a network switch including VLAN assignment.
3. Configure a router for LAN-to-LAN and LAN-to-WAN connectivity.
4. Enable and configure network services (DHCP, DNS) as specified.
5. Save and verify device configurations.

---

## Peralatan / Equipment Required

| No. | Item | Kuantiti / Quantity |
|-----|------|---------------------|
| 1 | Computer / laptop | 1 per trainee |
| 2 | Managed network switch (or Cisco Packet Tracer / GNS3 simulation) | 1 |
| 3 | Router (or simulation) | 1 |
| 4 | Console cable and USB-to-serial adapter | 1 set |
| 5 | Ethernet patch cables (Cat 5e or Cat 6) | As required |
| 6 | Approved network configuration specification document | 1 |
| 7 | Terminal emulator software (e.g., PuTTY) | Installed |

---

## Langkah Keselamatan / Safety Precautions

- Power off devices before inserting or removing cables unless hot-swap is supported.
- Use ESD (electrostatic discharge) precautions when handling network hardware.
- Do not alter configurations on live production devices — use only the designated lab equipment or simulation environment.
- Keep console session credentials confidential; do not share passwords with other trainees.
- Save a backup of the existing configuration before making any changes.

---

## Prosedur / Procedure

| Langkah / Step | Arahan / Instruction |
|----------------|----------------------|
| 1 | Review the approved network configuration specification. Confirm all IP addresses, subnet masks, VLAN IDs, and service settings to be applied before touching any device. |
| 2 | Connect the console cable from the management PC to the router's console port. Open PuTTY (or equivalent), select **Serial**, set the correct COM port, baud rate 9600, 8 data bits, no parity, 1 stop bit. |
| 3 | Log in to the router. Enter privileged EXEC mode: `enable`. Back up the current configuration: `copy running-config startup-config` (or note the existing config before changes). |
| 4 | Enter global configuration mode: `configure terminal`. Set the hostname as specified: `hostname <name>`. |
| 5 | Configure each router interface per the specification. For each interface: `interface <type> <slot/port>`, `ip address <IP> <subnet mask>`, `no shutdown`. Repeat for all interfaces. |
| 6 | Configure the default route or static routes as specified: `ip route <destination> <mask> <next-hop>`. If dynamic routing is required, configure the appropriate routing protocol (e.g., OSPF, RIP). |
| 7 | If the router provides DHCP, configure the DHCP pool: `ip dhcp pool <name>`, `network <network address> <mask>`, `default-router <gateway IP>`, `dns-server <DNS IP>`. Exclude reserved addresses: `ip dhcp excluded-address <start> <end>`. |
| 8 | Save the router configuration: `copy running-config startup-config`. Exit to privileged EXEC mode. |
| 9 | Connect to the managed switch via console. Log in and enter global configuration mode. Set the hostname. |
| 10 | Create VLANs as specified: `vlan <ID>`, `name <VLAN name>`. Repeat for each VLAN. |
| 11 | Assign switch ports to VLANs: for each access port, `interface <type> <slot/port>`, `switchport mode access`, `switchport access vlan <ID>`. Configure trunk ports: `switchport mode trunk`. |
| 12 | Configure the switch management IP on the management VLAN interface: `interface vlan <management VLAN ID>`, `ip address <IP> <mask>`, `no shutdown`. Set the default gateway: `ip default-gateway <gateway IP>`. |
| 13 | Save the switch configuration: `copy running-config startup-config`. |
| 14 | Configure IP addresses on all end-user devices (static or DHCP as specified). Verify each device shows the correct IP, subnet mask, gateway, and DNS settings via `ipconfig` (Windows) or `ip addr` (Linux). |
| 15 | Document all applied configurations in the configuration record sheet: device name, interface, IP address, subnet mask, gateway, VLAN, and any service enabled. Submit record to instructor. |

---

## Hasil Dijangka / Expected Outcome

Upon completion, trainees will have:

- All network devices configured with correct IP addresses, subnet masks, and gateways.
- VLANs created and ports assigned as specified.
- DHCP pool operational and allocating addresses to end-user devices.
- All device configurations saved to non-volatile memory.
- A completed configuration record sheet submitted to the instructor.

---

## Senarai Semak Penilaian / Assessment Checklist

| No. | Kriteria / Criteria | Pematuhan / Compliance |
|-----|---------------------|------------------------|
| 1 | Router interfaces configured with correct IP addresses and subnet masks | [ ] Yes  [ ] No |
| 2 | Default route or static/dynamic routing configured correctly | [ ] Yes  [ ] No |
| 3 | DHCP pool configured with correct range, gateway, and DNS | [ ] Yes  [ ] No |
| 4 | VLANs created and ports assigned correctly on switch | [ ] Yes  [ ] No |
| 5 | Switch management IP configured and reachable | [ ] Yes  [ ] No |
| 6 | End-user devices obtain correct IP settings | [ ] Yes  [ ] No |
| 7 | All configurations saved to startup-config | [ ] Yes  [ ] No |
| 8 | Configuration record sheet completed and submitted | [ ] Yes  [ ] No |

**Pengesahan Pengajar / Instructor Verification:**

| | Nama / Name | Tandatangan / Signature | Tarikh / Date |
|---|-------------|-------------------------|---------------|
| Pelatih / Trainee | | | |
| Pengajar / Instructor | | | |