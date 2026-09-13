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
| NO. KOD | IT-020-3:2013-C06/KP(2/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** View current IP settings

**TUJUAN:** ip addr show

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the sequence for configuring network devices according to a specification.
2. Configure IP addresses, subnet masks, and default gateway on routers, switches, and end devices.
3. Configure VLANs, trunk ports, and access ports on a managed switch.
4. Set up a DHCP scope on a router or server.
5. Configure a wireless access point with correct SSID, security, and channel settings.
6. Apply basic switch and router security (passwords, SSH, port security).

---

## 1.0 Introduction to Network Configuration

**Network configuration** is the process of setting the parameters on each network device so that it operates according to the approved specification. It follows the analysis stage and precedes testing. Every configuration action must be traceable — the technician records each parameter applied so that the configuration can be verified, replicated, or rolled back if necessary.

Configuration is carried out in a logical sequence:
1. Core and distribution layer devices first (routers, core switches).
2. Access layer devices next (access switches, wireless APs).
3. End-user devices last (desktops, laptops, printers).

This sequence ensures that the infrastructure is ready before end devices attempt to join the network.

---

## 2.0 OSI Model — Relevance to Configuration

Network configuration maps directly to the OSI (Open Systems Interconnection) model layers. Understanding the layer at which a parameter operates helps the technician configure devices correctly and diagnose problems efficiently.

| OSI Layer | Layer Name | Network Element | Configuration Parameters |
|-----------|-----------|-----------------|--------------------------|
| Layer 1 | Physical | Cables, NICs, ports | Cable type, connector, port speed (10/100/1000 Mbps), duplex (full/half/auto) |
| Layer 2 | Data Link | Switches, MACs | VLAN, trunk/access mode, STP, MAC address table, port security |
| Layer 3 | Network | Routers, Layer 3 switches | IP address, subnet mask, default gateway, routing table, NAT |
| Layer 4 | Transport | Firewall, ACL | TCP/UDP port filtering, ACL rules |
| Layer 7 | Application | Servers | DHCP scope, DNS zone, web proxy |

When a configuration issue arises, the technician troubleshoots from Layer 1 upward — verify physical connectivity before checking IP settings.

---

## 3.0 Router Configuration

A router connects different networks and forwards packets between them. In a small office or lab environment, the router typically also provides NAT, DHCP, and WAN connectivity.

### 3.1 Router Configuration Sequence

1. Connect the console cable (RJ-45 to DB-9 or USB-to-serial) from the router's console port to the technician's laptop.
2. Open a terminal emulator (e.g., PuTTY) with settings: **9600 baud, 8 data bits, no parity, 1 stop bit, no flow control**.
3. Enter privileged EXEC mode: `enable`
4. Enter global configuration mode: `configure terminal`
5. Set the hostname: `hostname <name>`
6. Configure the LAN interface (e.g., GigabitEthernet0/0):
   ```
   interface GigabitEthernet0/0
   ip address 192.168.10.1 255.255.255.0
   no shutdown
   ```
7. Configure the WAN interface (if applicable):
   ```
   interface GigabitEthernet0/1
   ip address dhcp          ! or static WAN IP
   no shutdown
   ```
8. Configure NAT (if required — see Section 3.2).
9. Configure DHCP (if required — see Section 3.3).
10. Save the configuration: `copy running-config startup-config`

### 3.2 NAT Configuration (PAT / Overload)

NAT overload (Port Address Translation) allows all LAN hosts to share a single public IP address.

```
! Define inside and outside interfaces
interface GigabitEthernet0/0
 ip nat inside

interface GigabitEthernet0/1
 ip nat outside

! Create an access list to identify inside hosts
access-list 1 permit 192.168.10.0 0.0.0.255

! Enable NAT overload
ip nat inside source list 1 interface GigabitEthernet0/1 overload
```

### 3.3 DHCP Configuration on a Router

```
! Exclude static addresses from the pool
ip dhcp excluded-address 192.168.10.1 192.168.10.99

! Create the DHCP pool
ip dhcp pool OFFICE_LAN
 network 192.168.10.0 255.255.255.0
 default-router 192.168.10.1
 dns-server 192.168.10.10 8.8.8.8
 lease 0 8 0        ! 0 days, 8 hours, 0 minutes
```

---

## 4.0 Switch Configuration

A **managed switch** allows the technician to configure VLANs, port modes, and security. Unmanaged switches require no configuration but offer no control.

### 4.1 Switch Configuration Sequence

1. Connect via console cable using the same terminal settings as the router (9600 baud, 8N1).
2. Enter privileged EXEC mode and global configuration mode.
3. Set the hostname.
4. Create VLANs and name them.
5. Assign access ports to VLANs.
6. Configure trunk ports.
7. Set the management IP (on the management VLAN interface).
8. Set the default gateway so the switch can be managed remotely.
9. Save the configuration.

### 4.2 VLAN Creation and Port Assignment

```
! Create VLANs
vlan 10
 name MANAGEMENT
vlan 20
 name STAFF
vlan 30
 name GUEST

! Assign access ports
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 20

interface FastEthernet0/2
 switchport mode access
 switchport access vlan 30
```

### 4.3 Trunk Port Configuration

A trunk port carries traffic for multiple VLANs between switches or between a switch and a router.

```
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
 switchport trunk native vlan 10
```

**Important:** The native VLAN must match on both ends of the trunk link. A mismatch causes a CDP/spanning-tree warning and drops native VLAN traffic.

### 4.4 Switch Virtual Interface (SVI) for Management

```
interface Vlan10
 ip address 192.168.10.2 255.255.255.0
 no shutdown

ip default-gateway 192.168.10.1
```

This allows the network administrator to Telnet or SSH into the switch from any device on VLAN 10.

### 4.5 Port Security

Port security limits the number of MAC addresses allowed on a port, preventing unauthorised devices from connecting.

```
interface FastEthernet0/1
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
```

| Violation Mode | Action |
|----------------|--------|
| `protect` | Drops packets from unknown MACs; no alert |
| `restrict` | Drops packets; increments violation counter; generates syslog |
| `shutdown` | Disables the port (err-disabled state); requires manual recovery |

---

## 5.0 IP Address Configuration on End Devices

### 5.1 Static IP Configuration (Windows)

1. Open **Control Panel → Network and Sharing Centre → Change adapter settings**.
2. Right-click the network adapter → **Properties**.
3. Select **Internet Protocol Version 4 (TCP/IPv4)** → **Properties**.
4. Select **Use the following IP address** and enter:
   - IP address: (as per specification)
   - Subnet mask: (as per specification)
   - Default gateway: (router LAN IP)
5. Select **Use the following DNS server addresses** and enter primary and secondary DNS.
6. Click **OK** → **Close**.
7. Verify: open Command Prompt, run `ipconfig /all` and confirm the values.

### 5.2 DHCP Configuration (Windows)

1. Follow steps 1–3 above.
2. Select **Obtain an IP address automatically**.
3. Select **Obtain DNS server address automatically**.
4. Click **OK** → **Close**.
5. Verify: run `ipconfig /all` and confirm the DHCP-assigned address, lease obtained, and lease expires values.
6. To force immediate renewal: `ipconfig /release` then `ipconfig /renew`.

### 5.3 IP Configuration on Linux/Ubuntu

```bash
# View current IP settings
ip addr show

# Set a static IP (temporary — lost on reboot)
sudo ip addr add 192.168.10.50/24 dev eth0
sudo ip route add default via 192.168.10.1

# Permanent static IP — edit /etc/netplan/00-installer-config.yaml
network:
  ethernets:
    eth0:
      dhcp4: no
      addresses: [192.168.10.50/24]
      gateway4: 192.168.10.1
      nameservers:
        addresses: [192.168.10.10, 8.8.8.8]
  version: 2

sudo netplan apply
```

---

## 6.0 Wireless Access Point Configuration

A wireless access point (AP) extends the wired LAN to wireless clients using the IEEE 802.11 standard.

### 6.1 AP Configuration Parameters

| Parameter | Description | Recommended Setting |
|-----------|-------------|---------------------|
| SSID | Service Set Identifier — the network name visible to wireless clients | Descriptive name (e.g., `OFFICE_STAFF`); do not broadcast SSID for sensitive networks |
| Security mode | Encryption and authentication method | WPA2-Personal (AES/CCMP) minimum; WPA3 preferred on newer devices |
| Passphrase | Pre-shared key for WPA2/WPA3-Personal | Minimum 12 characters; mix of letters, numbers, and symbols |
| Channel | Radio frequency channel | 2.4 GHz: channels 1, 6, or 11 (non-overlapping); 5 GHz: any non-DFS channel |
| Frequency band | 2.4 GHz or 5 GHz (or dual-band) | 5 GHz for speed; 2.4 GHz for range |
| AP IP address | Management IP of the AP itself | Static IP within management subnet; excluded from DHCP pool |
| VLAN | Which VLAN the SSID maps to | Match SSID to the correct VLAN in the specification |

### 6.2 802.11 Standards Summary

| Standard | Maximum Speed | Frequency | Common Use |
|----------|--------------|-----------|------------|
| 802.11b | 11 Mbps | 2.4 GHz | Legacy; not recommended |
| 802.11g | 54 Mbps | 2.4 GHz | Legacy; not recommended |
| 802.11n (Wi-Fi 4) | 600 Mbps | 2.4 / 5 GHz | Still widely deployed |
| 802.11ac (Wi-Fi 5) | 6.9 Gbps | 5 GHz | Common in offices |
| 802.11ax (Wi-Fi 6) | 9.6 Gbps | 2.4 / 5 / 6 GHz | Current standard for new deployments |

### 6.3 AP Configuration Procedure (Web-based GUI)

1. Connect the AP to a switch port with PoE (Power over Ethernet, IEEE 802.3af/at) or connect a power adapter.
2. Connect a laptop to the AP's management port or the same LAN segment.
3. Open a web browser and navigate to the AP's default management IP (refer to vendor documentation; commonly `192.168.1.1` or `10.0.0.1`).
4. Log in with the default credentials (change immediately after login).
5. Configure the management IP to match the specification (static, within the management VLAN).
6. Set the SSID, security mode, and passphrase.
7. Select the correct channel and band.
8. Map the SSID to the correct VLAN if the AP supports VLAN tagging.
9. Save and reboot the AP.

---

## 7.0 Basic Device Security Configuration

Every device must be secured before being placed into production.

| Security Measure | Cisco CLI Command / Action | Purpose |
|------------------|---------------------------|---------|
| Set enable secret | `enable secret <password>` | Protects privileged EXEC mode with an encrypted password |
| Set console password | `line console 0` → `password <pw>` → `login` | Requires password for console access |
| Enable SSH (disable Telnet) | `ip domain-name office.local` → `crypto key generate rsa modulus 2048` → `line vty 0 4` → `transport input ssh` | Encrypts remote management sessions |
| Set VTY password | `line vty 0 4` → `password <pw>` → `login local` | Secures remote login lines |
| Encrypt passwords in config | `service password-encryption` | Prevents plaintext passwords in `show running-config` |
| Set banner MOTD | `banner motd # Authorised users only. #` | Displays legal warning before login |
| Disable unused ports | `interface range Fa0/10 - 24` → `shutdown` | Prevents unauthorised device connections |
| Set management VLAN | Configure SVI on management VLAN only | Limits management traffic to a dedicated VLAN |

---

## 8.0 Common Errors in Network Configuration

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Entering wrong subnet mask | Hosts cannot communicate with each other or the gateway | Double-check mask against specification before saving |
| Forgetting `no shutdown` on an interface | Interface stays administratively down; no connectivity | Always enter `no shutdown` after configuring an interface |
| Native VLAN mismatch on trunk | Spanning-tree generates error; native VLAN traffic dropped | Verify native VLAN matches on both ends of every trunk |
| Assigning gateway IP from DHCP pool | Gateway address may be given to a client; routing fails | Exclude gateway IP using `ip dhcp excluded-address` |
| Using WEP or WPA-TKIP on wireless | Encryption broken; network is insecure | Use WPA2-AES (CCMP) or WPA3 minimum |
| Not saving configuration | Configuration lost on reboot | Always run `copy running-config startup-config` after changes |
| Console speed mismatch | Garbled characters in terminal; cannot enter commands | Match terminal baud rate to device default (9600 for most Cisco devices) |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCu 6
- Cisco Networking Academy — CCNA: Switching, Routing, and Wireless Essentials
- CompTIA Network+ Certification Study Guide — Chapters on Network Configuration and Wireless Networking
- IEEE 802.11ax (Wi-Fi 6) Standard Overview — Wi-Fi Alliance
- Microsoft Learn — Configure IP Settings in Windows
- Tanenbaum, A.S. & Wetherall, D.J. (2011). *Computer Networks* (5th ed.). Pearson. Chapters 4–5