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
| NO. KOD | IT-020-3:2013-C06/KP(1/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-analyse-network-config-spec

**TUJUAN:** Kertas rujukan untuk KP-01-analyse-network-config-spec.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and components of a network configuration specification document.
2. Identify network topology, IP addressing scheme, and device roles from a specification.
3. Verify IP address consistency and subnet correctness within a given scheme.
4. Describe common network topologies and their application in organisational environments.
5. Document specification gaps and non-compliant items for escalation.

---

## 1.0 Introduction to Network Configuration Specifications

A **network configuration specification** (also known as a network design document or network plan) is the formal reference that describes how a computer network is to be built and operated. It is produced by the network designer or IT administrator and must be thoroughly analysed by the technician before any physical or logical configuration work begins.

Analysing the specification correctly ensures that:
- All devices are configured with the correct IP addresses, subnet masks, and gateway settings.
- The correct network topology is implemented.
- Required network services (DHCP, DNS, VPN, NAT) are provisioned on the correct devices.
- Security and organisational policies are met.

Errors discovered during the analysis stage are far less costly than errors discovered after cables are laid or devices are configured.

---

## 2.0 Components of a Network Configuration Specification

A complete specification document typically contains the following sections:

| Component | Description |
|-----------|-------------|
| Project overview | Purpose of the network, site location, intended number of users, and scope of work |
| Network topology diagram | Physical and logical layout of all devices and connections |
| IP addressing scheme | Network address, subnet mask, CIDR notation, usable host range, broadcast address, default gateway, DNS servers |
| Device inventory | List of all routers, switches, access points, firewalls, servers, and end-user devices with hostnames, roles, and assigned IP addresses |
| VLAN plan | VLAN IDs, names, associated ports, and inter-VLAN routing method |
| Network services | Which device provides DHCP, DNS, NAT, or VPN; scope/pool details |
| Cabling plan | Cable type (Cat5e, Cat6, fibre), runs, patch panel locations, and labelling convention |
| Security requirements | Password policies, port security, wireless encryption standard, firewall rules |
| Bandwidth requirements | Uplink capacity, QoS priority classes |
| Acceptance criteria | Tests and results that must be achieved before handover |

---

## 3.0 Network Topologies

A **network topology** describes how devices are interconnected. The technician must identify the topology from the specification before planning cable runs and device placement.

### 3.1 Common Physical Topologies

| Topology | Description | Common Use |
|----------|-------------|------------|
| Star | All end devices connect to a central switch or hub. The switch is the single point of failure, but failures are isolated to one link. | Most common in LAN environments — offices, schools, computer labs |
| Extended Star (Hierarchical) | A core switch connects to multiple distribution switches, which in turn connect to access switches and end devices. | Medium-to-large organisations with multiple floors or buildings |
| Bus | All devices share a single backbone cable. A break in the cable disrupts the entire network. | Legacy networks; rarely deployed today |
| Ring | Devices connect in a closed loop. Token-based transmission prevents collisions. | FDDI, older Token Ring networks; rarely deployed today |
| Mesh | Every device has a direct link to every other device. Provides high redundancy. | WAN links between sites; critical infrastructure |
| Hybrid | Combination of two or more topologies. | Large enterprise environments |

### 3.2 Logical vs Physical Topology

- **Physical topology** — the actual layout of cables and devices in the building.
- **Logical topology** — how data flows through the network regardless of physical layout. For example, a network wired as a star may operate logically as a bus (Ethernet) or ring (Token Ring).

The specification must define both. The technician must draw or verify both diagrams during the analysis.

---

## 4.0 IP Addressing and Subnetting

Understanding IP addressing is essential for analysing and verifying the specification's addressing scheme.

### 4.1 IPv4 Address Classes

| Class | Range | Default Subnet Mask | Typical Use |
|-------|-------|---------------------|-------------|
| A | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 (/8) | Very large organisations |
| B | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 (/16) | Medium organisations |
| C | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 (/24) | Small offices, SOHO |

### 4.2 Private IP Address Ranges (RFC 1918)

Devices on a LAN use private addresses. These are not routable on the public internet.

| Range | CIDR | Usable Hosts |
|-------|------|--------------|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | 16,777,214 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | 1,048,574 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | 65,534 |

### 4.3 Subnet Mask and CIDR Notation

The **subnet mask** determines which portion of an IP address identifies the network and which identifies the host.

| CIDR | Subnet Mask | Usable Hosts | Common Use |
|------|-------------|--------------|------------|
| /24 | 255.255.255.0 | 254 | Small office LAN |
| /25 | 255.255.255.128 | 126 | Department subnet |
| /26 | 255.255.255.192 | 62 | Small workgroup |
| /27 | 255.255.255.224 | 30 | Server segment |
| /30 | 255.255.255.252 | 2 | Point-to-point WAN link |

**Formula:** Usable hosts = 2^(32 − prefix length) − 2

The network address (all host bits = 0) and broadcast address (all host bits = 1) are reserved and cannot be assigned to devices.

### 4.4 IP Address Verification Steps

When verifying an IP addressing scheme in a specification:

1. Confirm the network address and prefix length.
2. Calculate the usable host range and broadcast address.
3. Check that every assigned IP address falls within the usable host range.
4. Check that no IP address is duplicated (conflicts cause network instability).
5. Confirm that the default gateway address is within the same subnet as the hosts it serves.
6. Confirm that DNS server addresses are reachable (either within the LAN or via a correctly configured uplink).

**Example:**
- Network: 192.168.10.0/24
- Subnet mask: 255.255.255.0
- Usable host range: 192.168.10.1 – 192.168.10.254
- Broadcast: 192.168.10.255
- Default gateway assigned: 192.168.10.1 (router interface) ✓
- DHCP pool: 192.168.10.100 – 192.168.10.200 ✓ (within usable range, gateway excluded)

---

## 5.0 Network Device Roles

The specification will list devices by role. The technician must understand each role to verify that the specification is logical and complete.

| Device | Role | Key Configuration Parameters |
|--------|------|------------------------------|
| Router | Connects different networks; forwards packets between subnets or to the internet; may provide NAT and DHCP | WAN IP, LAN IP/gateway, routing protocol, NAT, DHCP scope |
| Layer 3 Switch | Performs inter-VLAN routing within the LAN; faster than a router for internal traffic | VLAN interfaces (SVIs), IP addresses per VLAN, routing table |
| Layer 2 Switch | Forwards frames within a VLAN based on MAC address; provides port segmentation | VLAN membership per port, trunk/access port mode, STP |
| Wireless Access Point (AP) | Extends LAN connectivity to wireless clients via 802.11 standards | SSID, security mode (WPA2/WPA3), channel, IP address |
| Firewall | Controls traffic between network zones based on rules; protects against unauthorised access | Interface zones (LAN/WAN/DMZ), rules, NAT, VPN |
| Server | Provides centralised services (file sharing, DHCP, DNS, authentication) | Static IP, services enabled, firewall exceptions |
| End-user device | Desktop, laptop, or workstation that consumes network services | IP (static or DHCP), subnet mask, gateway, DNS |

---

## 6.0 Network Services

The specification must identify which device hosts each service and the configuration parameters for each service.

### 6.1 DHCP (Dynamic Host Configuration Protocol)

DHCP automatically assigns IP configuration to client devices, eliminating manual configuration errors.

| Parameter | Description | Example |
|-----------|-------------|---------|
| Scope / Pool | Range of IP addresses available for assignment | 192.168.10.100 – 192.168.10.200 |
| Subnet mask | Mask assigned to clients | 255.255.255.0 |
| Default gateway | Router address assigned to clients | 192.168.10.1 |
| DNS server(s) | DNS servers assigned to clients | 192.168.10.10, 8.8.8.8 |
| Lease duration | How long an address assignment is valid | 8 hours (default), 24 hours |
| Exclusions | Addresses within the scope withheld from dynamic assignment (used for static devices) | 192.168.10.1 – 192.168.10.99 |

### 6.2 DNS (Domain Name System)

DNS resolves human-readable hostnames (e.g., `fileserver.office.local`) to IP addresses. The specification should state:
- Internal DNS server IP address.
- DNS forwarder address (for resolving internet names, e.g., 8.8.8.8 or 1.1.1.1).
- DNS zone name (e.g., `office.local`).

### 6.3 NAT (Network Address Translation)

NAT allows multiple private IP addresses to share one or more public IP addresses when accessing the internet. The router performs the translation. The specification should identify the NAT type (overload / PAT is most common for small organisations) and the outside interface.

---

## 7.0 VLAN (Virtual Local Area Network) Planning

VLANs segment a physical LAN into multiple logical networks, improving security and performance.

| Concept | Description |
|---------|-------------|
| VLAN ID | Numeric identifier (1–4094). VLAN 1 is the default and should not carry user traffic. |
| Access port | Switch port assigned to a single VLAN; used for end devices |
| Trunk port | Switch port that carries traffic for multiple VLANs; used between switches and between switch and router |
| Native VLAN | The VLAN carried untagged on a trunk port (must match on both ends) |
| Inter-VLAN routing | Routing between VLANs via a Layer 3 switch or a router-on-a-stick configuration |

When analysing a VLAN plan, verify:
- Each VLAN has a unique ID and a descriptive name (e.g., VLAN 10 = Management, VLAN 20 = Staff, VLAN 30 = Guest).
- Each VLAN has its own subnet.
- Trunk links are correctly identified between switches and between the switch and router.
- The inter-VLAN routing method is specified and the gateway IP for each VLAN is stated.

---

## 8.0 Structured Cabling Standards

The specification must reference the cabling standard used. Technicians must verify that cable type, run lengths, and connector types comply.

| Standard | Description |
|----------|-------------|
| TIA/EIA-568 | Commercial building telecommunications cabling standard; defines cable categories, connector types (RJ-45), and maximum run lengths |
| Cat5e | Supports up to 1 Gbps at 100 MHz over 100 m |
| Cat6 | Supports up to 10 Gbps at 250 MHz over 55 m (10GBase-T); 1 Gbps over 100 m |
| Cat6A | Supports 10 Gbps at 500 MHz over 100 m |
| Single-mode fibre | Long-distance runs (>2 km); used for building-to-building links |
| Multi-mode fibre | Short-distance runs (up to 550 m at 10 Gbps); used within a building |
| Patch panel | Centralises cable terminations in the network rack; labelling convention must be stated in the specification |

Maximum horizontal cable run (patch panel to wall outlet): **90 m** (with 10 m total for patch cables on both ends).

---

## 9.0 Specification Gap Analysis

After reading the specification, the technician must check for completeness and consistency. Common gaps include:

| Gap / Issue | Description | Action |
|-------------|-------------|--------|
| Missing device IP | A device is listed in the topology but has no assigned IP address | Flag to network administrator for assignment before configuration |
| Overlapping subnets | Two VLANs are given subnets that overlap (e.g., 192.168.10.0/24 and 192.168.10.128/25) | Alert administrator; subnets must not overlap |
| Duplicate IP assignment | Two devices are assigned the same IP address | Flag immediately; will cause ARP conflict and intermittent connectivity failures |
| Gateway outside subnet | The gateway IP listed for a subnet does not fall within that subnet | Specification error; clarify with administrator |
| Trunk port not specified | Uplinks between switches are not designated as trunk ports | Verify with administrator; switches default to access mode if not configured |
| DNS server unreachable | DNS IP is on a different subnet with no routing path | Check routing table; add a static route or default route if missing |
| Unlabelled cables | Cabling plan does not include a labelling convention | Request a labelling scheme before cabling begins |
| Security standard not stated | Wireless specification does not state encryption mode | Default to WPA2-AES minimum; escalate if not confirmed |

---

## 10.0 Common Errors in Specification Analysis

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Skipping the topology diagram | Incorrect device placement and cabling | Always draw or verify the topology before physical work |
| Not calculating subnet ranges | Assigning host IPs outside the valid range | Use subnet calculation: 2^(32−prefix) − 2 for usable hosts |
| Ignoring VLAN plan | End devices on wrong VLANs; inter-VLAN routing fails | Map every switch port to its VLAN during analysis |
| Not checking for duplicate IPs | Two devices cannot communicate reliably; ARP conflict | Build an IP address register and verify uniqueness |
| Assuming DHCP scope covers gateway | Gateway is assigned from the dynamic pool and can change | Always exclude the gateway from the DHCP scope |
| Overlooking fibre vs copper | Wrong SFP or transceiver ordered; cable run cannot meet spec | Confirm cable type and transceiver compatibility early |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCu 6
- TIA/EIA-568-C Commercial Building Telecommunications Cabling Standard
- Cisco Networking Academy — CCNA: Introduction to Networks (Modules 11–13: IP Addressing)
- CompTIA Network+ Certification Study Guide — Chapter on Network Design and Documentation
- Microsoft Learn — DHCP Server Configuration for Windows Server
- Tanenbaum, A.S. & Wetherall, D.J. (2011). *Computer Networks* (5th ed.). Pearson. Chapter 5: Network Layer