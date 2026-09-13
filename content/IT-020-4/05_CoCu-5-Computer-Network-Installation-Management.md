# CoCu 5: Computer Network Installation Management (L4, 240 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) |
| LEVEL | L4 | L4 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 5: Computer Network Installation Management (Pengurusan Pemasangan Rangkaian Komputer) | CoCu 5: Computer Network Installation Management (Pengurusan Pemasangan Rangkaian Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE COMPUTER NETWORK SET-UP SPECIFICATION · PLAN COMPUTER NETWORK INSTALLATION · MANAGE COMPUTER NETWORK INSTALLATION WORK · PRODUCE COMPUTER NETWORK INSTALLATION MANAGEMENT REPORT | ANALYSE COMPUTER NETWORK SET-UP SPECIFICATION · PLAN COMPUTER NETWORK INSTALLATION · MANAGE COMPUTER NETWORK INSTALLATION WORK · PRODUCE COMPUTER NETWORK INSTALLATION MANAGEMENT REPORT |
| NO. CODE | IT-020-4:2013 - CoCu 5 / P(5/6) | PAGE: 93 - 112 |


| SET-UP CONTEXT | SINGLE-SITE LAN INSTALLATION | MULTI-SITE / CAMPUS NETWORK INSTALLATION |
|----------------|-------------------------------|------------------------------------------|
| Network scope | Single-site local area network (LAN) with one server rack, standard topology (star), wired and basic wireless coverage. SLA and security policy are straightforward. | Multi-site or campus network spanning several buildings or floors, with WAN links, multiple racks, VLANs, redundant paths, and advanced wireless (WIMAX, enterprise WIFI). SLA includes uptime guarantees and SLG penalties. |
| Equipment and planning | Standard equipment: managed switch, single router, access point, patch panel, UTP cabling, RJ-45. Installation plan uses a simple work breakdown structure and timeline with one installation team. | Extended equipment: multiple switches, routers, firewalls, fibre patch panels, MDF/IDF racks, spectrum analyser, cable certifier. Installation plan requires a detailed Gantt chart, budget, multi-team coordination, and contractor management. |
| Testing and reporting | Basic connectivity tests: ping, speed test, print-out test, internet browsing test. UAT with single department sign-off. Report covers job checklist, expenses, and team details. | Full interconnectivity testing suite: stress test, stability test, frequency scanning, power load test, remote test, tracert, wireless authentication test. UAT across multiple departments. Report includes job variance analysis, rectification log, and consolidated expenses. |


| Type | Description |
|------|-------------|
| Network topology (star, bus, mesh, hybrid, ring, tree) | The arrangement of nodes and connections in a network that determines how devices communicate and how cabling is routed. Star topology is the most common for modern LANs -- all devices connect to a central switch, making fault isolation simple since a single cable failure only affects one device. Bus topology uses a single backbone cable with terminators at each end and is largely obsolete due to collision and single-point-of-failure issues. Mesh topology provides maximum redundancy by connecting every node to every other node; full mesh is used in critical data centre interconnects while partial mesh balances cost and redundancy. Ring topology passes data in one direction through each node sequentially and is still found in legacy Token Ring and some SONET/SDH fibre deployments. Tree topology extends star by connecting multiple star networks in a hierarchy, suitable for campus buildings with MDF-to-IDF distribution. Hybrid topology combines two or more of these arrangements to meet specific requirements -- for example, a star-mesh hybrid in a multi-floor office. Each topology has different cable requirements: star requires a home-run cable from every device to the switch (typically Cat5e/Cat6 UTP up to 100 m), mesh requires exponentially more cables as nodes increase (n(n-1)/2 links for full mesh), and tree requires both horizontal and backbone cabling. Scalability must be considered during planning -- star scales easily by adding switch ports, while bus and ring become bottlenecks as devices increase. The administrator must interpret the required topology from the network specification and plan cabling, equipment placement, and rack layout accordingly. |
| Network encryption (WEP, WPA/WPA2, AES, RADIUS, TKIP) | Security protocols and mechanisms that protect wireless network traffic from eavesdropping, tampering, and unauthorised access. WEP (Wired Equivalent Privacy) uses a static 40-bit or 104-bit RC4 key and is considered obsolete -- it can be cracked in minutes using freely available tools and must never be used in any production environment. TKIP (Temporal Key Integrity Protocol) was introduced with WPA as a transitional improvement over WEP, adding per-packet key mixing and a message integrity check, but it is also deprecated due to known vulnerabilities. WPA2 with AES-CCMP (Advanced Encryption Standard in Counter Mode with CBC-MAC Protocol) is the current minimum standard for enterprise wireless; it uses 128-bit AES encryption and provides strong confidentiality and integrity. WPA3 is the latest generation, adding Simultaneous Authentication of Equals (SAE) to resist offline dictionary attacks, but adoption is still in progress. WPA2-Enterprise (802.1X) requires a RADIUS server (such as FreeRADIUS, Microsoft NPS, or Cisco ISE) that authenticates each user individually with unique credentials rather than a shared passphrase. In a WPA2-Enterprise deployment, the access point acts as an authenticator, forwarding EAP (Extensible Authentication Protocol) messages between the wireless client (supplicant) and the RADIUS server; common EAP methods include EAP-TLS (certificate-based, most secure), PEAP-MSCHAPv2 (username/password with server certificate), and EAP-TTLS. The RADIUS server can integrate with Active Directory or LDAP for centralised user management and can enforce policies such as VLAN assignment per user group, session timeouts, and accounting (logging who connected, when, and for how long). The administrator must match encryption and authentication requirements to the company security policy, configure access points with the correct SSID-to-security mapping, deploy and maintain RADIUS server certificates, and verify that all client devices support the chosen EAP method. |
| Network installation equipment (switch, router, AP, firewall, patch panel, MDF) | Active and passive components required for a complete network installation, spanning switching, routing, wireless, security, and structured cabling infrastructure. Switches connect devices within a LAN segment and forward frames based on MAC addresses; enterprise models from Cisco (Catalyst series), HPE Aruba, or Juniper offer managed features such as VLANs, spanning tree, and SNMP. Routers connect different networks or subnets and direct packets based on IP addresses; common enterprise choices include Cisco ISR series and MikroTik RouterBOARD. Access points provide wireless coverage and may be standalone or controller-managed; enterprise-grade APs from Cisco Meraki, Ubiquiti UniFi, or Aruba Instant support multi-SSID, band steering, and centralised management. Firewalls inspect and filter traffic based on security rules; next-generation firewalls (NGFW) from Fortinet FortiGate, Palo Alto, or pfSense add application-layer inspection, intrusion prevention, and VPN. Patch panels provide a central termination point for horizontal cables running from wall outlets to the MDF or IDF, enabling organised and maintainable connections between the structured cabling plant and active switch ports. The MDF (main distribution frame) is the primary wiring hub for the building, while IDF (intermediate distribution frame) rooms serve individual floors or wings. Racks are selected based on equipment count and environment -- standard 42U floor-standing racks for server rooms, 19U wall-mount cabinets for IDF closets, and open-frame relay racks for high-density cabling. All equipment must be matched to the network specification, site survey findings, rack capacity, power and cooling requirements, and approved budget. |
| IP addressing and subnetting (IP, subnet mask, gateway, DNS) | The logical addressing scheme that allows devices to communicate on a network, forming the foundation of all IP-based connectivity. Each device requires a unique IP address within its subnet; duplicate addresses cause intermittent connectivity and are difficult to trace. The subnet mask defines the network boundary and determines how many hosts a subnet can hold -- for example, a /24 (255.255.255.0) mask supports 254 hosts, while a /22 (255.255.252.0) supports 1,022 hosts. CIDR (Classless Inter-Domain Routing) notation is the modern standard for expressing subnet size (e.g. 192.168.10.0/24) and replaces the legacy Class A/B/C scheme. Subnet planning methodology involves documenting the number of required subnets, the number of hosts per subnet, growth projections, and reserved ranges for servers, printers, management interfaces, and DHCP pools. The default gateway is the router IP address for traffic destined outside the local subnet; if misconfigured, devices can communicate locally but cannot reach other subnets or the internet. DNS (Domain Name System) resolves human-readable hostnames to IP addresses and is required for Active Directory, web browsing, email, and virtually all application-layer services. IPv6 awareness is increasingly important as IPv4 address exhaustion drives adoption; IPv6 uses 128-bit addresses in hexadecimal notation (e.g. 2001:db8::1/64), supports auto-configuration via SLAAC (Stateless Address Auto-Configuration), and may run in dual-stack alongside IPv4 during transition. The administrator must document the complete IP addressing plan -- including VLAN-to-subnet mapping, DHCP scopes, static reservations, and DNS zone entries -- and verify the configuration during installation testing. Incorrect IP configuration (wrong subnet mask, duplicate address, missing gateway, or wrong DNS) is among the most common causes of installation failures. |
| User Acceptance Test (UAT) | A formal, structured test performed after network installation to verify that the completed network meets all functional and performance requirements agreed in the SLA and network specification. The UAT is organised into specific test procedures, each with defined steps, expected results, and pass/fail criteria. Connectivity tests include pinging the default gateway, DNS server, and external hosts from every subnet, as well as running tracert to verify correct routing paths; a pass requires 0% packet loss and round-trip times within the SLA threshold. Application tests verify that end-user workflows function correctly -- this includes web browsing through the proxy or firewall, printing to network printers, accessing file shares, sending and receiving email, and connecting to business applications; each test is marked pass only if the application responds within acceptable time. Performance tests measure throughput using tools such as iPerf or LAN Speed Test to confirm that the network delivers the bandwidth specified (e.g. minimum 900 Mbps on a Gigabit link), and stability tests run a continuous ping or data transfer over an extended period (e.g. 24 hours) to detect intermittent failures. For wireless networks, the UAT includes signal strength verification at defined locations (minimum -67 dBm for VoIP, -70 dBm for data), roaming tests between access points, and authentication tests with WPA2-Enterprise credentials. Each test case is documented on a UAT form with the tester name, date, device tested, result (pass/fail), and remarks. Failed tests trigger a rectification action, re-test, and updated documentation. The completed UAT is signed by the user representative or department head and included as a key section of the installation management report. |
| Work breakdown structure (WBS) and Gantt chart | Project management tools used to plan, schedule, and track network installation projects from initiation to completion. The WBS decomposes the entire installation scope into hierarchical, manageable tasks -- Level 1 might include phases such as Site Preparation, Cabling, Equipment Installation, Configuration, Testing, and Handover; Level 2 breaks each phase into specific activities (e.g. under Cabling: cable pathway survey, cable pulling, termination, labelling, testing). Each WBS task is assigned a duration estimate using techniques such as expert judgement (based on experience from similar projects), analogous estimation (referencing past project data), or three-point estimation (optimistic, most likely, pessimistic durations averaged to reduce risk). The Gantt chart maps these WBS tasks against a calendar timeline and visually shows start dates, end dates, task durations, and dependencies (finish-to-start, start-to-start). The critical path is the longest sequence of dependent tasks that determines the minimum project duration -- any delay on a critical-path task directly delays the project completion date. Tasks not on the critical path have float (slack) and can be delayed without affecting the overall deadline. Milestones are key checkpoints (e.g. "cabling complete", "UAT passed", "handover signed") that mark the completion of major phases. Resource allocation is tracked alongside the Gantt chart to ensure that installation teams, equipment, and materials are available when scheduled. Both the WBS and Gantt chart are included in the installation management plan, presented to management for approval, and updated throughout the project to monitor progress, control expenses, identify variances between planned and actual timelines, and trigger corrective actions when tasks fall behind schedule. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 25% | 60 | Analyse computer network set-up specification | 18.0 | 42.0 | 60.0 |
| 25% | 60 | Plan computer network installation | 18.0 | 42.0 | 60.0 |
| 30% | 72 | Manage computer network installation work | 21.6 | 50.4 | 72.0 |
| 20% | 48 | Produce computer network installation management report | 14.4 | 33.6 | 48.0 |
| **100%** | **240** | | **72.0** | **168.0** | **240.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) | IT-020-4:2013 COMPUTER SYSTEMS ADMINISTRATION (Pentadbiran Sistem Komputer) |
| LEVEL | L4 | L4 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 5: Computer Network Installation Management (Pengurusan Pemasangan Rangkaian Komputer) | CoCu 5: Computer Network Installation Management (Pengurusan Pemasangan Rangkaian Komputer) |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE COMPUTER NETWORK SET-UP SPECIFICATION · PLAN COMPUTER NETWORK INSTALLATION · MANAGE COMPUTER NETWORK INSTALLATION WORK · PRODUCE COMPUTER NETWORK INSTALLATION MANAGEMENT REPORT | ANALYSE COMPUTER NETWORK SET-UP SPECIFICATION · PLAN COMPUTER NETWORK INSTALLATION · MANAGE COMPUTER NETWORK INSTALLATION WORK · PRODUCE COMPUTER NETWORK INSTALLATION MANAGEMENT REPORT |
| NO. CODE | IT-020-4:2013 - CoCu 5 / P(5/6) | PAGE: 113 - 128 |


| Network Equipment | Description |
|--------------------|-------------|
| Switch (managed / unmanaged) | A network device that connects multiple devices within a LAN segment and forwards Ethernet frames based on MAC addresses stored in its CAM (Content Addressable Memory) table. Managed switches support VLANs (IEEE 802.1Q tagging), port mirroring for traffic analysis, QoS (Quality of Service) for prioritising voice and video traffic, and SNMP monitoring for centralised management -- these features are required for enterprise networks. Enterprise switches are available in standard port counts of 24-port and 48-port configurations, with Gigabit (1 Gbps) or 10-Gigabit uplink ports; common models include the Cisco Catalyst 9200/9300 series, HPE Aruba 2930F/6300, and Juniper EX2300/EX4300. PoE (Power over Ethernet) switches supply electrical power to connected devices such as IP phones, access points, and security cameras over the Ethernet cable itself, eliminating the need for separate power adapters; PoE standards include IEEE 802.3af (15.4 W per port), 802.3at/PoE+ (30 W), and 802.3bt/PoE++ (60-90 W for high-power devices). Switch stacking allows multiple physical switches to be managed as a single logical unit using dedicated stacking cables or ports, simplifying administration and providing redundancy. Spanning Tree Protocol (STP, IEEE 802.1D) or its faster variant Rapid STP (RSTP, IEEE 802.1w) prevents broadcast loops in networks with redundant switch connections by automatically blocking redundant paths and activating them only when a primary path fails. Unmanaged switches are plug-and-play with no configuration capability and are suitable only for small, non-critical segments. The administrator selects the switch type, port count, PoE capability, and stacking requirements based on the network specification, device inventory, and growth plan. |
| Router | Connects different networks or subnets and routes packets based on IP addresses using routing tables that map destination networks to next-hop addresses and egress interfaces. Provides essential services including NAT (Network Address Translation) for sharing a single public IP among many internal devices, DHCP server or relay for automatic IP assignment, and sometimes integrated firewall and VPN functions. Routing can be configured as static routes (manually defined, suitable for simple or stub networks) or dynamic routing protocols such as OSPF (Open Shortest Path First), which automatically discovers and adapts to topology changes in multi-router networks by exchanging link-state advertisements. QoS (Quality of Service) configuration on the router prioritises latency-sensitive traffic such as VoIP and video conferencing over bulk data transfers using mechanisms like traffic shaping, queuing, and DSCP marking. Common enterprise routers include the Cisco ISR 1000/4000 series (feature-rich, widely deployed), MikroTik RouterBOARD/CCR series (cost-effective, powerful RouterOS with extensive L3 features), and Juniper SRX series (combined routing and security). In a multi-site installation, routers connect LANs across WAN links using technologies such as MPLS, site-to-site VPN (IPsec), or SD-WAN. Configuration includes setting gateway IP addresses, defining static or dynamic routes, configuring ACLs (Access Control Lists) to permit or deny traffic flows, and enabling logging for troubleshooting and compliance. The administrator must verify routing convergence, test failover paths if redundant WAN links exist, and document all routing configurations in the network installation report. |
| Access Point (AP) | Provides wireless network coverage for WIFI-capable devices by bridging wireless clients to the wired LAN infrastructure. Enterprise-grade APs support multiple SSIDs (e.g. separate SSIDs for staff, guests, and IoT devices), WPA2/WPA3-Enterprise authentication with RADIUS, and advanced radio management features such as band steering (automatically directing dual-band clients to the less congested 5 GHz band), client load balancing, and airtime fairness. Modern APs comply with IEEE 802.11ax (Wi-Fi 7) or Wi-Fi 6E (6 GHz band), offering higher throughput, better performance in dense environments through OFDMA and MU-MIMO, and improved power efficiency for battery-operated devices via Target Wake Time (TWT). APs can be deployed in two architectures: controller-based, where a centralised wireless LAN controller (WLC) manages all APs, pushes configurations, handles roaming, and aggregates monitoring (e.g. Cisco 9800 WLC, Aruba Mobility Controller); or standalone/cloud-managed, where each AP operates independently or is managed through a cloud dashboard (e.g. Ubiquiti UniFi Controller, Cisco Meraki Dashboard, Aruba Central). Leading enterprise AP brands include Cisco Catalyst/Meraki (MR series), Ubiquiti UniFi (U6 Pro/Enterprise), and HPE Aruba Instant On/500 series. Proper AP placement requires a wireless site survey -- either predictive (using software like Ekahau or iBwave with floor plans) or active (walking the site with a survey tool) -- to determine optimal mounting locations, channel assignments (non-overlapping channels 1, 6, 11 on 2.4 GHz), and transmit power levels to maximise coverage while minimising co-channel interference. The administrator documents AP locations, channel plans, SSID-to-VLAN mappings, and RADIUS server settings in the installation plan. |
| Firewall | Inspects and filters network traffic based on security rules that permit or deny traffic by source/destination IP address, port number, and protocol. Traditional stateful firewalls track connection states and enforce rules at Layers 3-4 (network and transport), while next-generation firewalls (NGFW) add deep packet inspection at Layer 7 (application layer), enabling the firewall to identify and control specific applications (e.g. allowing Zoom but blocking BitTorrent) regardless of the port used. NGFW features also include built-in Intrusion Prevention System (IPS) that detects and blocks known attack signatures and anomalous behaviour, URL filtering and web content categorisation, SSL/TLS inspection (decrypting encrypted traffic for analysis), sandboxing for zero-day malware detection, and integrated VPN (both site-to-site IPsec and remote access SSL VPN). Common enterprise firewall models include Fortinet FortiGate (60F/100F for SME, 600F/1000F for enterprise), Palo Alto PA-400/PA-800 series, Cisco Firepower 1000/2100 series, and open-source pfSense/OPNsense for budget-conscious deployments. Firewalls are placed at the network perimeter between the internal LAN and external WAN/internet, and may also be deployed between internal zones (e.g. separating the server VLAN from the user VLAN). Configuration includes defining security zones (WAN, LAN, DMZ), creating rule sets with proper ordering (most specific rules first), configuring NAT policies, and setting up VPN tunnels for remote sites or users. Misconfiguration -- such as overly permissive rules, incorrect zone assignments, or missing NAT -- can either block legitimate business traffic or expose the network to threats. The administrator must test firewall rules thoroughly during installation and document all policies in the network installation report. |
| Patch panel and rack (42U, 19U, open frame, relay rack) | Passive infrastructure components that organise cable terminations and house active equipment in a structured cabling system compliant with TIA/EIA-568 standards. Patch panels provide a central termination point where horizontal cables from wall outlets are punched down on the rear using 110-style or LSA-Plus IDC (Insulation Displacement Contact) blocks, and the front presents RJ-45 ports that connect to switch ports via short patch cords. This separation between permanent cabling and active equipment simplifies moves, adds, and changes (MACs) -- the administrator reconnects patch cords at the panel without disturbing the permanent cable runs in walls and ceilings. Patch panels are available in 24-port and 48-port configurations for Cat5e, Cat6, and Cat6a, and must match the cable category to maintain certified performance. Cable certification (using a certifier such as Fluke DSX-5000 or DSX-8000) tests each terminated link against the relevant standard (TIA Cat6: up to 250 MHz, Cat6a: up to 500 MHz) and produces a pass/fail report; this certification is required for manufacturer warranty coverage on the structured cabling system and should be completed before the patch panel is connected to active equipment. Racks house switches, routers, patch panels, UPS units, and cable management accessories in a standard 19-inch wide frame. Rack types include 42U floor-standing enclosed cabinets (most common for server rooms and MDF, providing physical security, cable management, and controlled airflow), 19U or smaller wall-mount cabinets (used in IDF closets or small offices where floor space is limited), and open-frame relay racks (used in data centres or wiring rooms where maximum airflow and easy access are prioritised over physical security). Proper labelling of every patch panel port, cable, and switch port -- using a consistent naming scheme documented in the network installation plan -- is critical for ongoing maintenance, troubleshooting, and future expansion. |
| Network cable tester / certifier | Instruments used to verify the physical integrity and performance of installed network cabling, ranging from basic continuity testers to full cable certification systems. A basic cable tester (such as the Fluke Networks MicroScanner or equivalent) checks that all eight wires in a UTP cable are correctly terminated with proper pin-to-pin mapping (T568A or T568B), detects open circuits, short circuits, crossed pairs, and split pairs, and verifies cable length using TDR (Time Domain Reflectometry). A cable certifier is a significantly more advanced instrument that tests the installed link against published standards -- the Fluke Networks DSX-5000 CableAnalyzer certifies to Cat5e and Cat6 standards (up to 250 MHz), while the DSX-8000 certifies to Cat6a (500 MHz) and Cat8 (2000 MHz). Certification tests measure parameters including insertion loss (attenuation), near-end crosstalk (NEXT), power-sum NEXT (PS-NEXT), return loss, alien crosstalk (for Cat6a), and propagation delay; each parameter must meet or exceed the TIA/EIA-568 limits for the cable category, and the certifier issues a definitive pass or fail result for each link. A passing certification report is required by structured cabling manufacturers (e.g. Panduit, CommScope, Belden) as a condition of their extended product and application warranties, which can cover 20-25 years. All certification results are saved digitally on the certifier and exported as PDF or CSV reports, which are included in the network installation documentation and handed over during UAT. The administrator must ensure that every installed cable link is tested and certified before connecting active equipment, as undetected cabling faults are a leading cause of intermittent network issues that are difficult to diagnose after the installation is complete. |

![Common Network Topologies](images/network-topologies.png)


| Software / Protocol | Description |
|----------------------|-------------|
| DHCP (Dynamic Host Configuration Protocol) | Automatically assigns IP addresses, subnet masks, gateways, and DNS servers to devices on the network. Reduces manual configuration errors. The DHCP server (or router) maintains a pool of addresses and lease times. Scope, exclusions, and reservations must be configured according to the network plan. |
| DNS (Domain Name System) | Resolves human-readable hostnames (e.g. server1.company.local) to IP addresses. Required for Active Directory, email, web browsing, and most network services. Internal DNS zones are configured on the server; external DNS is provided by the ISP. Incorrect DNS configuration is a common cause of connectivity issues where devices appear connected but cannot browse. |
| Network monitoring (ping, tracert, speed test) | Tools used to verify connectivity and diagnose problems during and after installation. Ping tests reachability; tracert shows the path packets take through routers; speed test measures throughput. These tools are used during inter-connectivity testing and included in the UAT checklist. |
| SNMP and network monitoring platforms | SNMP (Simple Network Management Protocol) is the standard protocol for collecting performance and status data from network devices. SNMP-enabled switches, routers, firewalls, and APs expose management data through MIBs (Management Information Bases), which monitoring platforms poll at regular intervals. Enterprise network monitoring platforms include Nagios (open-source, highly customisable with plugins for device and service monitoring), PRTG Network Monitor (Paessler, auto-discovery with sensor-based licensing, suitable for SMEs), Zabbix (open-source, supports SNMP, agent-based, and IPMI monitoring with advanced alerting and visualisation), and SolarWinds Network Performance Monitor (enterprise-grade with automated network mapping, NetFlow analysis, and intelligent alerting). These platforms provide real-time dashboards showing device status, bandwidth utilisation, error rates, and latency; generate alerts via email, SMS, or integration with ticketing systems when thresholds are exceeded; and produce historical reports for capacity planning and SLA compliance. During network installation, the administrator configures SNMP community strings (v2c) or user credentials (v3 with authentication and encryption), adds all installed devices to the monitoring platform, defines alert thresholds based on the SLA, and verifies that monitoring is operational before handover. |
| Wireless controller and management software | Centralised platforms that manage, configure, and monitor multiple wireless access points from a single interface, eliminating the need to configure each AP individually. Controller-based solutions include the Cisco 9800 Wireless LAN Controller (hardware or virtual appliance managing Catalyst APs), which provides centralised policy enforcement, seamless roaming via CAPWAP tunnels, rogue AP detection, and RF management. Cloud-managed solutions include Ubiquiti UniFi Controller (free, self-hosted or UniFi Cloud, managing UniFi APs with an intuitive dashboard for site-wide configuration, guest portal, and traffic statistics), Cisco Meraki Dashboard (fully cloud-managed with zero-touch provisioning, automatic firmware updates, and built-in analytics), and Aruba Central (cloud-based management for Aruba Instant APs with AI-driven RF optimisation and client troubleshooting). These platforms handle firmware deployment across all APs simultaneously, enforce consistent SSID and security configurations, provide heat maps of wireless coverage and client density, and enable rapid troubleshooting through per-client connection logs and packet capture. During installation, the administrator deploys the controller (physical, virtual, or cloud), adopts all installed APs into the controller, configures WLAN profiles (SSID, security, VLAN mapping), tunes RF settings, and verifies roaming and coverage before UAT. |
| Network documentation tools | Software and systems used to create, maintain, and share accurate records of the network installation including physical topology diagrams, logical network maps, IP address plans, cable schedules, and equipment inventories. Microsoft Visio is the traditional industry-standard tool for creating network diagrams using stencils for switches, routers, firewalls, servers, and cabling; it supports layered diagrams and integrates with Microsoft 365. draw.io (also known as diagrams.net) is a free, open-source alternative that runs in the browser or as a desktop application, supports Visio import/export, and can store diagrams in Google Drive or SharePoint. NetBox is an open-source infrastructure resource modelling (IRM) tool originally developed by DigitalOcean that serves as a network source of truth -- it maintains a database of sites, racks, devices, interfaces, IP addresses, VLANs, circuits, and cable connections, with a REST API for integration with automation tools. Cable management databases (whether built into NetBox, maintained in spreadsheets, or managed by dedicated tools) track every cable run from patch panel port to wall outlet to switch port, including cable type, length, certification status, and label. Accurate and up-to-date network documentation is essential for ongoing maintenance, troubleshooting, change management, and handover to operations staff; the installation management report must include complete as-built documentation that reflects the actual installed state of the network. |


| Common Fault During Installation | Cause | Action |
|-----------------------------------|-------|--------|
| No network connectivity after cabling | Cable not terminated correctly; wrong cable type (crossover vs straight-through); patch cord not connected to correct port | Test cable with tester; re-terminate if faulty; verify patch schedule against network diagram |
| Device gets IP but cannot reach gateway | Incorrect subnet mask or gateway configured; VLAN mismatch between switch port and device | Verify IP configuration (ipconfig / ifconfig); check switch port VLAN assignment; confirm gateway address |
| Wireless clients cannot authenticate | Wrong encryption type or passphrase configured on AP; RADIUS server unreachable or certificate expired | Verify AP encryption settings match policy; check RADIUS connectivity and certificate validity; test with known-good credentials |
| Intermittent connectivity or slow speed | Cable exceeds 100 m limit; interference on wireless channel; switch port speed/duplex mismatch | Re-run cable or add a switch to shorten run; change wireless channel or AP placement; set switch port to auto-negotiate |
| VLAN trunk misconfiguration | Native VLAN mismatch between connected switches (e.g. one side uses VLAN 1, the other uses VLAN 99); trunk not formed because port is set to access mode instead of trunk mode; allowed VLAN list does not include the required VLANs; inter-VLAN routing not configured on the Layer 3 switch or router | Verify trunk status on both ends using show interface trunk or equivalent; ensure native VLAN matches on both sides of the trunk link; confirm port mode is set to trunk (not access); check the allowed VLAN list includes all required VLANs; verify that a Layer 3 interface (SVI or router sub-interface) exists for each VLAN that needs inter-VLAN routing; test by pinging between VLANs after correction |
| DHCP scope exhaustion or conflict | DHCP scope is too small for the number of devices on the subnet (e.g. /24 scope with 300 devices); overlapping DHCP scopes from multiple servers or a rogue DHCP server assigning incorrect addresses; lease time set too short causing excessive renewals, or too long preventing address reuse | Check DHCP server statistics for scope utilisation and available addresses; expand the scope or reduce the lease time to free addresses faster; use DHCP snooping on managed switches to block rogue DHCP servers; scan the network with a tool such as Wireshark or dhcp_probe to identify unauthorised DHCP responses; ensure only one authorised DHCP server (or DHCP relay) serves each subnet; verify that DHCP exclusion ranges do not overlap with static assignments |


## Learning Outcome Matrix

| Work Activity | Knowledge Outcome | Performance Outcome | Assessment Method | Evidence Required |
|---|---|---|---|---|
| Analyse computer network set-up specification | Identify and interpret requirements | Analyse requirements and extract key priorities | Written test on requirement analysis; oral questions on decision criteria | Completed analysis checklist; documented decision rationale |
| Plan computer network installation | Understand installation procedures and configuration options | Successfully install and configure software or systems | Practical installation; verification of correct configuration | Installation log; system configuration screenshots; test results |
| Manage computer network installation work | Understand installation procedures and configuration options | Successfully install and configure software or systems | Practical installation; verification of correct configuration | Installation log; system configuration screenshots; test results |
| Produce computer network installation management report | Understand installation procedures and configuration options | Successfully install and configure software or systems | Practical installation; verification of correct configuration | Installation log; system configuration screenshots; test results |

## Practical Exercises

The following administrative and supervisory exercise scenarios develop the competencies required for Computer Network Installation Management. Each exercise is designed for L4 administrative/supervisory professionals and includes simulation scenarios, planning templates, documentation requirements, and assessment criteria aligned with NOSS standards.

### Analyse computer network set-up specification

**Objective:** Execute analyse computer network set-up specification according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for analyse computer network set-up specification
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear

### Plan computer network installation

**Objective:** Execute plan computer network installation according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for plan computer network installation
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear

### Manage computer network installation work

**Objective:** Execute manage computer network installation work according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for manage computer network installation work
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear

### Produce computer network installation management report

**Objective:** Execute produce computer network installation management report according to L4 administrative standards

**Duration:** 90 minutes

**Resources Required:** Templates, documentation, planning tools appropriate to the activity

**Procedures:**
1. Review requirements and planning templates
2. Complete planning and analysis for produce computer network installation management report
3. Document decisions and create implementation plan
4. Present recommendations to stakeholders for approval

**Expected Outcome:**
Approved plan with documented analysis and stakeholder sign-off

**Assessment Checklist:**
- [ ] Requirements clearly understood
- [ ] Analysis completed and documented
- [ ] Plan covers all relevant areas
- [ ] Recommendations justified with evidence
- [ ] Stakeholder approval obtained
- [ ] Documentation complete and clear



## Employability Skills

This CoCu develops the following employability skills through the work activities:

### 1. Communication Skills
- **Mapping:** Document network design specifications and installation plans; present network topology and addressing schemes to management; communicate installation progress and test results to project stakeholders

### 2. Teamwork & Collaboration
- **Mapping:** Lead network installation teams across single-site or multi-site deployments; coordinate with cabling, server, and security teams; manage contractor and vendor involvement during installation

### 3. Problem-solving
- **Mapping:** Diagnose network connectivity, VLAN, and DHCP issues during installation; resolve IP addressing conflicts and routing problems; troubleshoot switch and access point configuration faults

### 4. Initiative & Self-reliance
- **Mapping:** Take responsibility for network installation quality and testing; proactively verify configuration against specifications before handover; identify potential capacity or performance issues early in deployment

### 5. Planning & Organizing
- **Mapping:** Plan network installation sequences including switch configuration, IP addressing, and VLAN assignments; organize equipment staging, cabling coordination, and testing schedules; manage project timelines for multi-site rollouts

### 6. Self-management & Safety Awareness
- **Mapping:** Follow change management procedures for network cutover and migration; manage risk of service disruption during installation in live environments; ensure compliance with network security policies during deployment

### 7. Technology Use & Technical Proficiency
- **Mapping:** Configure managed switches, routers, wireless access points, and DHCP/DNS services; use network testing and monitoring tools; implement VLANs, trunking, and inter-VLAN routing

### 8. Learning Skills & Continuous Improvement
- **Mapping:** Stay current on network equipment, protocols, and installation best practices; analyze installation reports to improve future deployment procedures; learn from connectivity issues to refine testing checklists



## Attitude, Safety and Environmental

### Workplace Safety
- **Change Management and Approval:** Always follow formal change management procedures before implementing server configurations or updates. Obtain required approvals and communicate changes to stakeholders to avoid unexpected downtime.
- **Risk Management:** Assess security risks when configuring server roles and implement hardening measures to protect against known vulnerabilities and attack vectors.
- **Data Protection Compliance:** Handle server security configuration in accordance with data protection regulations (e.g., PDPA, GDPR) and organisational security policies. Ensure proper access controls and audit logging are in place.
- **Documentation and Knowledge Sharing:** Maintain comprehensive documentation of all server configurations, changes, and troubleshooting procedures to support team knowledge and ensure continuity during staff transitions.

### Environmental Considerations
- **Sustainable IT Practices:** Plan for efficient resource utilisation (power, cooling, storage) when configuring server environments. Consider virtualisation and consolidation to reduce physical hardware footprint and energy consumption.
- **Responsible Asset Disposal:** Ensure decommissioned servers and storage devices are securely wiped and responsibly recycled through certified e-waste facilities.

### Professional Attitudes
- **Ethical Decision-Making:** Make recommendations based on technical merit and organisational benefit, not vendor preferences or personal convenience. Maintain transparency with stakeholders about trade-offs and costs.
- **Continuous Learning:** Stay current with new server technologies, security standards, and industry best practices to make informed decisions about infrastructure improvements.
- **Team Leadership:** Lead technical teams with respect and clear communication; ensure team members understand the rationale behind decisions and have opportunity to contribute expertise.
- **Accountability:** Take responsibility for system stability and performance; proactively monitor configurations and respond quickly to issues that could impact business operations.

## References

**Official Standards and Frameworks:**

- NOSS IT-020-4:2013 Computer System Administration Syllabus
- Cisco CCNA Routing and Switching – Network Installation and Management
- Juniper Networks JNCIS-ENT Certification Guide – Enterprise Routing and Switching
- CompTIA Network+ Extended Objectives – Advanced Network Administration
- RFC 3021 – Using 31-Bit Prefixes on IPv4 Point-to-Point Links

**Technical References and Best Practices:**

- Border Gateway Protocol (BGP) Administration and Configuration (RFC 4271)
- OSPF Dynamic Routing Protocol Configuration and Optimization (RFC 2328)
- EIGRP Configuration and Best Practices for Enterprise Networks
- Network Device Configuration Management – SNMP, NetFlow, sFlow Protocols
- Redundancy and High Availability Protocols – HSRP, VRRP, GLBP Configuration

**Contact hour:** [[00_Contact-hour_IT-020-4-L4-Administration]]


---

↑ [README](../../README.md) · **IT-020-4** > CoCu 5 - Computer Network Installation Management

**In this level:** [00_Contact-hour](00_Contact-hour_IT-020-4-L4-Administration.md) · [00_standard-practice](00_standard-practice.md) · [01_CoCu-1](01_CoCu-1-Server-Configuration.md) · [02_CoCu-2](02_CoCu-2-Computer-System-Security-Control.md) · [03_CoCu-3](03_CoCu-3-System-Network-Procurement.md) · [04_CoCu-4](04_CoCu-4-Network-Cabling-Management.md) · [06_CoCu-6](06_CoCu-6-Computer-System-Maintenance-Management.md)

**Other levels:** [IT-020-3 (L3)](../IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md) · [IT-020-5 (L5)](../IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md)
