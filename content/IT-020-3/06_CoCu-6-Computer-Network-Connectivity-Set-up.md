# CoCu 6: Computer Network Connectivity Set-up (120 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 6: Computer Network Connectivity Set-up (Persediaan Sambungan Rangkaian Komputer) | CoCu 6: Computer Network Connectivity Set-up (Persediaan Sambungan Rangkaian Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE COMPUTER NETWORK CONFIGURATION SPECIFICATION · CARRY OUT COMPUTER NETWORK CONFIGURATION · PERFORM COMPUTER NETWORK CONNECTIVITY TEST · CARRY OUT COMPUTER NETWORK TROUBLESHOOT · PREPARE COMPUTER NETWORK CONNECTIVITY REPORT | ANALYSE COMPUTER NETWORK CONFIGURATION SPECIFICATION · CARRY OUT COMPUTER NETWORK CONFIGURATION · PERFORM COMPUTER NETWORK CONNECTIVITY TEST · CARRY OUT COMPUTER NETWORK TROUBLESHOOT · PREPARE COMPUTER NETWORK CONNECTIVITY REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 6 / P(6/7) | PAGE: 133 - 138 |


| SET-UP CONTEXT | WIRED LAN / NEW OFFICE SET-UP | WIRELESS / EXTENSION TO EXISTING NETWORK |
|----------------|-------------------------------|------------------------------------------|
| Job order | New wired LAN installation for an office floor. Configuration specification includes number of drops, cable type (Cat6), IP scheme (static or DHCP), subnet mask, gateway, DNS, switch port assignments, and VLAN if required. Equipment list: switch, patch panel, patch cords, RJ45 faceplates. | Adding wireless access points to extend coverage in an existing network. Specification includes SSID, security (WPA2/WPA3), channel allocation, access point placement, and authentication method. Existing IP scheme (DHCP) and VLAN are reused or extended. |
| Tools and parts | Crimping tool, cable tester, punch-down tool, screwdriver set, cable ties, label maker. Parts: UTP Cat6 cable reels, RJ45 connectors, patch panel, faceplates, managed switch, patch cords. | Wireless site survey tool (app or hardware), cable tester, screwdriver set, PoE injector or PoE switch. Parts: access points, mounting brackets, Cat6 patch cords, PoE cables. |
| Report | Network connectivity report with IP scheme, switch port map, cable test results, ping and traceroute test results, UAT sign-off, and network diagram. | Connectivity report with access point placement map, SSID configuration, wireless coverage test results (signal strength per area), authentication test results, and UAT sign-off. |


| Type of Tools and Equipment | Description |
|-----------------------------|-------------|
| Crimping tool and RJ45 connectors | Used to terminate UTP cable with RJ45 connectors. The crimping tool presses the connector contacts onto the cable wires. Correct wire order (T568A or T568B) must be followed; inconsistent termination causes connectivity failures. Always test the cable after crimping. |
| Cable tester / LAN tester | Used to verify that each wire pair in a UTP or patch cable is correctly terminated and can carry signal. Tests for open circuits, short circuits, crossed pairs, and split pairs. Essential for every new cable run and for troubleshooting existing connections. |
| Punch-down tool | Used to terminate cable wires onto patch panels and keystone jacks (faceplates). The tool seats the wire into the IDC (insulation displacement contact) and trims the excess. Correct colour code (T568A or T568B) must match the patch panel and faceplate. |
| Managed network switch | The central device that connects all network drops. Managed switches allow VLAN configuration, port speed settings, and monitoring. During set-up, configure port assignments, enable or disable ports, and set trunk links to other switches or the router. |
| Router / gateway | Connects the local network to the WAN or internet. Configured with the gateway IP address, NAT, DHCP scope (if used), and firewall rules. The router is the default gateway for all devices on the network. |
| Wireless access point (AP) | Provides Wi-Fi connectivity for wireless devices. Configured with SSID, security protocol (WPA2/WPA3), channel, and transmit power. Placement affects coverage and signal quality; a wireless site survey helps determine optimal positions. PoE (Power over Ethernet) simplifies installation by delivering power and data over one cable. |
| Label maker and cable tags | Used to label every cable run, patch panel port, faceplate, and switch port with a unique identifier. Labels match the network documentation and make troubleshooting faster. Labelling must be done during installation, not after. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 20% | 24 | Analyse computer network configuration specification | 7.2 | 16.8 | 24.0 |
| 25% | 30 | Carry out computer network configuration | 9.0 | 21.0 | 30.0 |
| 20% | 24 | Perform computer network connectivity test | 7.2 | 16.8 | 24.0 |
| 25% | 30 | Carry out computer network troubleshoot | 9.0 | 21.0 | 30.0 |
| 10% | 12 | Prepare computer network connectivity report | 3.6 | 8.4 | 12.0 |
| **100%** | **120** | | **36.0** | **84.0** | **120.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) | IT-020-3:2013 COMPUTER SYSTEM OPERATION (Operasi Sistem Komputer) |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 6: Computer Network Connectivity Set-up (Persediaan Sambungan Rangkaian Komputer) | CoCu 6: Computer Network Connectivity Set-up (Persediaan Sambungan Rangkaian Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE COMPUTER NETWORK CONFIGURATION SPECIFICATION · CARRY OUT COMPUTER NETWORK CONFIGURATION · PERFORM COMPUTER NETWORK CONNECTIVITY TEST · CARRY OUT COMPUTER NETWORK TROUBLESHOOT · PREPARE COMPUTER NETWORK CONNECTIVITY REPORT | ANALYSE COMPUTER NETWORK CONFIGURATION SPECIFICATION · CARRY OUT COMPUTER NETWORK CONFIGURATION · PERFORM COMPUTER NETWORK CONNECTIVITY TEST · CARRY OUT COMPUTER NETWORK TROUBLESHOOT · PREPARE COMPUTER NETWORK CONNECTIVITY REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 6 / P(6/7) | PAGE: 139 - 144 |


| Hardware Component | Description |
|--------------------|-------------|
| Network Interface Card (NIC) | The adapter that connects a computer or peripheral to the network. NICs may be built into the motherboard (onboard) or added as an expansion card. Each NIC has a unique MAC address. During set-up, install the NIC driver, configure the IP address (static or DHCP), subnet mask, gateway, and DNS. Check the NIC LED: green steady = link up, blinking = traffic, no light = no connection. |
| UTP cable (Cat5e / Cat6 / Cat6a) | Unshielded twisted pair cable used for Ethernet LAN connections. Cat5e supports up to 1 Gbps at 100 m; Cat6 supports up to 10 Gbps at 55 m; Cat6a supports 10 Gbps at 100 m. Straight-through wiring (T568B both ends) is standard for PC-to-switch connections. Crossover wiring is used for like-to-like connections, though most modern devices support auto-MDI/MDIX. |
| Fibre optic cable (single-mode / multi-mode) | Used for long-distance runs or high-speed backbone connections between switches, floors, or buildings. Single-mode uses a narrow core for distances up to 40 km; multi-mode uses a wider core for up to 550 m. Connector types include LC, SC, and ST — they must match the switch transceiver or SFP module. Handle with care; do not bend below the minimum bend radius. |
| Patch panel | A passive device mounted in the network rack that terminates all cable runs from wall faceplates. Each port on the patch panel connects to a switch port via a short patch cord. Patch panels organise cabling, simplify moves and changes, and reduce wear on switch ports. Label every port to match the faceplate and switch port. |
| RJ45 faceplate and keystone jack | Mounted on the wall at each network drop location. The keystone jack terminates the cable from the patch panel; the faceplate provides a neat, accessible connection point for the user's patch cord. Wire colour code must match the patch panel (T568A or T568B). |
| Main Distribution Frame (MDF) and rack | The central location where all network cabling terminates and active equipment (switches, routers, patch panels, UPS) is housed. The rack provides organised mounting; cable management trays and power distribution units (PDUs) keep the installation tidy and maintainable. Environmental control (ventilation or air conditioning) prevents overheating. |

![Common Network Topologies](images/network-topologies.png)

| Software / Configuration Area | Description |
|-------------------------------|-------------|
| IP addressing and subnetting | Assigning IP addresses to devices using a static scheme or DHCP server. The subnet mask defines the network boundary; the gateway is the router's IP for traffic outside the subnet; DNS servers resolve domain names. Common private ranges: 192.168.x.x, 10.x.x.x, 172.16-31.x.x. Plan the IP scheme before configuration to avoid conflicts. |
| VLAN configuration | Virtual LANs segment the physical network into logical groups (e.g. by department, function, or security level). VLANs are configured on managed switches by assigning ports to VLAN IDs. Trunk ports carry traffic for multiple VLANs between switches. VLAN tagging follows IEEE 802.1Q. VLANs improve security and reduce broadcast traffic. |
| Network connectivity testing tools | Standard tools for verifying connectivity: **ping** (tests reachability to gateway, DNS, and external hosts), **tracert / traceroute** (shows the path packets take and identifies where delays or failures occur), **ipconfig / ifconfig** (displays current IP configuration), and **browser test** (confirms internet access). Print and scan tests verify peripheral connectivity. All results are documented in the connectivity report. |
| Network security configuration | Basic security settings applied during network set-up: setting the switch management password, disabling unused ports, enabling port security (MAC address limiting), and configuring wireless security (WPA2/WPA3 with strong passphrase). These settings protect the new network from unauthorised access before it is handed over to the user. |

![RJ45 Cable Wiring Standards (T568A / T568B)](images/cable-wiring-t568.png)

| Common Fault During Network Set-up | Cause | Action |
|-------------------------------------|-------|--------|
| No link light on NIC or switch port | Cable not connected, faulty cable termination, NIC not seated, or switch port disabled | Check cable connections at both ends; test cable with LAN tester; reseat NIC; verify switch port is enabled in management interface |
| Ping to gateway fails (no connectivity) | Wrong IP address, subnet mask, or gateway; NIC driver not installed; cable fault | Run ipconfig to verify settings; compare with the configuration specification; reinstall NIC driver; test with a known-good cable |
| Can ping gateway but not external hosts | DNS misconfigured, router/firewall blocking traffic, or ISP issue | Check DNS settings; try pinging an external IP (e.g. 8.8.8.8) to isolate DNS vs routing; check router NAT and firewall rules |
| Wireless device connects but no internet | Wrong SSID security key, DHCP scope exhausted, AP channel interference, or VLAN mismatch | Verify SSID and security settings; check DHCP lease pool; change AP channel to avoid interference; confirm VLAN assignment matches the wired network |
| Intermittent connection drops | Damaged cable, electromagnetic interference, faulty NIC, or switch port flapping | Replace suspect cable; relocate cable away from power lines or fluorescent lights; test NIC in another slot; check switch port error counters and logs |
| Print or scan test fails over network | Printer/scanner not on same subnet, firewall blocking port, or driver not installed | Verify printer/scanner IP is on the correct subnet; check Windows Firewall or security software; install correct print/scan driver and configure port |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse computer network configuration specification | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Carry out computer network configuration | Know procedures and troubleshooting techniques | Execute procedures and resolve issues | Practical demonstration; problem-solving observed | Completed task log; troubleshooting notes; final working state |
| Perform computer network connectivity test | Know testing procedures and acceptance criteria | Execute tests and document results | Practical test execution; result documentation | Test results log; signed-off test report |
| Carry out computer network troubleshoot | Know procedures and troubleshooting techniques | Execute procedures and resolve issues | Practical demonstration; problem-solving observed | Completed task log; troubleshooting notes; final working state |
| Prepare computer network connectivity report | Know tools, parts, and materials needed | Gather and organize tools, parts, and materials | Practical observation of tool/material preparation; checklist verification | Photo/log of prepared toolkit; materials checklist |

## Practical Exercises

The following hands-on lab exercises develop the practical competencies required for Computer Network Connectivity Set-up. Each exercise is designed for L3 operational-level technicians and includes step-by-step procedures, required equipment, and assessment criteria aligned with NOSS standards.

### Lab 1: Analyse computer network configuration specification

**Objective:** Perform analyse computer network configuration specification correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for analyse computer network configuration specification
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of analyse computer network configuration specification with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 2: Carry out computer network configuration

**Objective:** Perform carry out computer network configuration correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for carry out computer network configuration
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of carry out computer network configuration with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 3: Perform computer network connectivity test

**Objective:** Perform perform computer network connectivity test correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for perform computer network connectivity test
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of perform computer network connectivity test with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 4: Carry out computer network troubleshoot

**Objective:** Perform carry out computer network troubleshoot correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for carry out computer network troubleshoot
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of carry out computer network troubleshoot with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete

### Lab 5: Prepare computer network connectivity report

**Objective:** Perform prepare computer network connectivity report correctly according to NOSS standards

**Duration:** 60 minutes

**Equipment Required:** Standard technician tools and components appropriate to the activity

**Procedures:**
1. Follow established procedures for prepare computer network connectivity report
2. Complete the activity according to job specifications
3. Verify the work meets quality standards
4. Document the completion and any issues encountered

**Expected Outcome:**
Successful completion of prepare computer network connectivity report with no errors

**Assessment Checklist:**
- [ ] Activity completed according to procedure
- [ ] Quality standards met
- [ ] No safety incidents
- [ ] Documentation complete



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Activity:** Prepare network connectivity report
- **Mapping:** Document configuration settings and test results; explain network setup to users; communicate connectivity issues and recommendations

### 2. Teamwork & Collaboration
- **All activities in shared network environment**
- **Mapping:** Coordinate with network managers on IP and VLAN allocation; work with switch/router administrators; support end-users with connectivity troubleshooting

### 3. Problem-solving
- **All activities involving diagnosis and testing**
- **Mapping:** Troubleshoot connectivity failures; isolate hardware vs configuration vs external issues; diagnose DNS, VLAN, and wireless problems

### 4. Initiative & Self-reliance
- **Cable installation and configuration activities**
- **Mapping:** Work independently on cabling and IP configuration; take responsibility for proper cable termination and testing; verify connectivity before handover

### 5. Planning & Organizing
- **Cable planning and installation**
- **Mapping:** Plan cable routes and termination points; organize patch panels logically; document IP addressing scheme and VLAN assignments

### 6. Self-management & Safety Awareness
- **Cable handling and MDF work**
- **Mapping:** Handle cables properly (avoid min bend radius); work safely in network infrastructure; follow proper cable management practices; manage time to meet connectivity deadlines

### 7. Technology Use & Technical Proficiency
- **All activities using network hardware and configuration tools**
- **Mapping:** Install NICs and configure IP settings; terminate cables to T568A/B standard; use LAN testers and network diagnostic tools; configure VLANs and wireless security

### 8. Learning Skills & Continuous Improvement
- **All activities; especially new cabling standards and network technologies**
- **Mapping:** Stay current on cabling standards (Cat5e/6/6a); learn new VLAN and wireless configuration methods; improve troubleshooting efficiency


## Attitude, Safety and Environmental

### Workplace Safety
- **Cable Management and Trip Hazards:** Route all network and power cables through cable trays, conduits, or floor ducts to prevent trip hazards in walkways and workspaces. Avoid bundling excessive cables together, as tightly packed bundles restrict airflow and increase fire risk. Secure loose cables immediately during installation.
- **Fibre Optic Safety:** Never look directly into the end of a fibre optic cable or connector, as laser light can cause permanent eye damage. Wear safety glasses when cleaving or splicing fibre; handle bare fibre carefully to avoid glass splinter injuries. Dispose of fibre offcuts in a designated sharps container, not in general waste.
- **Working at Height:** Use approved ladders, scaffolding, or access platforms when running cables through ceiling voids or elevated cable trays. Follow organisational working-at-height procedures, including the use of a spotter or buddy system. Inspect equipment before use and never overreach.
- **Electrical Safety with PoE and Crimping Tools:** Exercise caution when working with Power over Ethernet (PoE) equipment, as PoE switches deliver up to 90 W per port. Disconnect cables from PoE ports before crimping or terminating. Use crimping and punch-down tools correctly to avoid hand injuries; keep cutting blades away from fingers and replace dull blades promptly.

### Environmental Considerations
- **E-waste Management:** Properly dispose of defective hardware components, circuit boards, and packaging materials through authorised e-waste recycling centres. Never dispose of electronics in regular trash or landfill.
- **Energy Efficiency:** Configure systems to use power-saving modes and efficient power supplies. Avoid unnecessary idle time and follow organisational energy conservation policies.

### Professional Attitudes
- **Punctuality and Reliability:** Complete network connectivity set-up work on schedule to meet user handover deadlines and support business operations.
- **Integrity in Documentation:** Prepare accurate and complete network connectivity reports with all hardware details, software versions, and test results. Honest documentation supports future troubleshooting and maintains system integrity.
- **Teamwork and Support:** Collaborate with help desk staff and other technicians; share knowledge about system configurations and troubleshooting techniques to improve overall technical capability.
- **Attention to Detail:** Verify every connection, configuration setting, and test result to ensure network connectivity is correctly set up and systems function as intended.

## References

**Official Standards and Frameworks:**

- NOSS IT-020-3:2013 Computer System Operation Syllabus
- IEEE 802.3 Ethernet Standard and Cable Specifications (Cat6A, Cat7, Cat8)
- IEEE 802.11ac/ax Wireless LAN (Wi-Fi 6/7) Technical Specifications
- Cisco Networking Academy – Introduction to Networking and IPv4/IPv6 Protocols
- RFC 791 – Internet Protocol Version 4 (IPv4) Specification

**Technical References and Best Practices:**

- RFC 8200 – Internet Protocol Version 6 (IPv6) Specification
- Malaysian Registry of Internet Numbers (MYNIC) – IPv4 and IPv6 Allocation
- CompTIA Network+ Certification Guide – Network Installation and Configuration
- Dell Networking Switch Configuration – S-Series and Z-Series Switches
- Network Cabling Standards and Best Practices – TIA-568 Color Code Standards

**Contact hour:** [[00_Contact-hour_IT-020-3-L3-Operation]]


---

↑ [README](../../README.md) · **IT-020-3** > CoCu 6 - Computer Network Connectivity Set-up

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-3-L3-Operation.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Computer-System-Set-up.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Maintenance.md) · [03_CoCu-3](03_CoCu-3-Computer-System-Repair.md) · [04_CoCu-4](04_CoCu-4-Server-Installation.md) · [05_CoCu-5](05_CoCu-5-Server-Maintenance.md) · [07_CoCu-7](07_CoCu-7-Mobile-Device-Configuration.md)

**Other levels:** [IT-020-4 (L4)](../IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
