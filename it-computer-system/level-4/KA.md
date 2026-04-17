# PENILAIAN PENGETAHUAN (Knowledge Assessment)

**Kod / Code:** IT-020-4:2013/KA
**Kertas Warna / Paper Colour:** MERAH JAMBU (Pink)

---

| | |
|---|---|
| **Kod Program / Programme Code** | IT-020-4:2013 |
| **Nama Program / Programme Name** | Computer System Management (Pengurusan Sistem Komputer) |
| **Tahap / Level** | 4 |
| **Topik / Topic** | Network Infrastructure Diagnostics (Diagnostik Infrastruktur Rangkaian) |
| **Tempoh / Duration** | 2 hours |
| **Jumlah Markah / Total Marks** | 50 |
| **Markah Lulus / Pass Mark** | 60% |

---

## Arahan / Instructions

Answer ALL scenarios. Each scenario presents a real-world network fault. For each scenario, identify the root cause, describe diagnostic steps, and propose a resolution. Partial credit is awarded per rubric.

**Standards Reference:** RFC 2328 (OSPF), RFC 4301 (IPSec), RFC 7296 (IKEv2), RFC 3022 (NAT), RFC 8446 (TLS), IEEE 802.1D (STP), IEEE 802.1Q (VLAN/Trunking), IEEE 802.3ad (LACP)

**IT-020 Bilingual Terms:** Switch (Suis) · Router (Penghala) · Firewall (Tembok Api) · VPN (Rangkaian Persendirian Maya) · VLAN (Rangkaian Kawasan Setempat Maya) · Trunk (Trunk) · Gateway (Pintu Masuk) · Subnet (Sub-rangkaian)

---

## BAHAGIAN D: SENARIO DIAGNOSTIK RANGKAIAN / SECTION D: NETWORK DIAGNOSTIC SCENARIOS (50 marks)

---

<!-- SCENARIO type="switching" -->
### Scenario 1: Trunk Port Enters `err-disabled` State

**Context (Konteks):** An access switch (Suis Capaian) trunk port linking to the distribution switch enters `err-disabled` state after a new IP phone is plugged into a nearby access port. VLAN 10 (voice) and VLAN 20 (data) traffic is interrupted.

**(a)** Identify TWO likely causes of `err-disabled` on a trunk port. `[1.0 pt]`
**(b)** Write the IOS commands to diagnose the error and re-enable the port. `[1.0 pt]`
**(c)** State ONE preventive configuration to stop recurrence. `[0.5 pt]`

> **Rubric:** Causes (1.0 pt) · Diagnostic commands (1.0 pt) · Prevention (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="switching" -->
### Scenario 2: STP Topology Change Causing Broadcast Flooding

**Context:** After replacing a failed access switch (Suis), a technician notices excessive broadcast traffic (Trafik Penyiaran) and intermittent connectivity. `show spanning-tree` shows frequent TCN flags on the root port.

**(a)** Explain why TCN flags cause MAC table flushing and broadcast flooding. `[1.0 pt]`
**(b)** Identify the IOS command to verify and configure PortFast and BPDU Guard per IEEE 802.1D. `[1.0 pt]`
**(c)** Describe how to confirm STP has converged after applying the fix. `[0.5 pt]`

> **Rubric:** TCN explanation (1.0 pt) · PortFast/BPDU Guard (1.0 pt) · Convergence check (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="switching" -->
### Scenario 3: 802.1Q Trunk VLAN Pruning Mismatch

**Context:** VLAN 30 (server farm) is reachable from some switches but not others. The inter-switch Trunk (Trunk) link shows VLAN 30 in the VLAN database but traffic does not pass. No physical errors on the link.

**(a)** Explain how allowed VLAN lists on 802.1Q trunk links cause selective VLAN blackout. `[1.0 pt]`
**(b)** Write the IOS commands to verify and correct the allowed VLAN list on both ends. `[1.0 pt]`
**(c)** State the difference between `switchport trunk allowed vlan add` and `switchport trunk allowed vlan`. `[0.5 pt]`

> **Rubric:** VLAN pruning explanation (1.0 pt) · Correction commands (1.0 pt) · Command difference (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="switching" -->
### Scenario 4: EtherChannel LACP Mode Mismatch

**Context:** Two aggregated uplinks (IEEE 802.3ad LACP) between the access and distribution layer show as individual links rather than a bundle. The port-channel interface is absent in `show interfaces`.

**(a)** List THREE LACP mode combinations that form a valid channel-group and ONE that does not. `[1.0 pt]`
**(b)** Write IOS commands to check LACP negotiation status and reconfigure both sides. `[1.0 pt]`
**(c)** Describe the load-balancing method you would configure and justify your choice. `[0.5 pt]`

> **Rubric:** LACP modes (1.0 pt) · Diagnostic/fix commands (1.0 pt) · Load-balancing justification (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="switching" -->
### Scenario 5: Port-Security Sticky MAC Table Overflow

**Context:** A student lab switch (Suis) shows multiple ports in `secure-shutdown` state after a network mapping exercise. The port-security sticky table is full and legitimate users cannot connect.

**(a)** Explain how sticky MAC learning works and why a `maximum 1` policy caused this fault. `[1.0 pt]`
**(b)** Write IOS commands to clear the violation, recover the ports, and adjust the policy. `[1.0 pt]`
**(c)** Recommend a port-security policy suitable for a lab environment. `[0.5 pt]`

> **Rubric:** Sticky MAC explanation (1.0 pt) · Recovery commands (1.0 pt) · Policy recommendation (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="routing" -->
### Scenario 6: OSPF Neighbor Stuck in ExStart State

**Context:** Two routers (Penghala) running OSPFv2 (RFC 2328) on a point-to-point link cannot form a full adjacency. `show ip ospf neighbor` shows both routers stuck in `ExStart` state indefinitely.

**(a)** Identify TWO causes of an OSPF neighbor remaining in ExStart. `[1.0 pt]`
**(b)** Write the `debug` and `show` commands needed to isolate the root cause. `[1.0 pt]`
**(c)** Explain how MTU mismatch causes ExStart and state the IOS fix. `[1.0 pt]`

> **Rubric:** Root causes (1.0 pt) · Debug/show commands (1.0 pt) · MTU explanation and fix (1.0 pt) · **Total: 3.0 pts** <!-- RUBRIC-TOTAL: 3.0 -->

---

<!-- SCENARIO type="routing" -->
### Scenario 7: Missing Default Route Causing Internet Failure

**Context:** LAN-to-LAN communication works perfectly, but users report no internet access. The edge router (Penghala Tepi) has a default route `0.0.0.0/0` pointing to the ISP but it is not present in branch routers' routing tables.

**(a)** Explain how OSPF distributes the default route and what command on the ABR causes redistribution. `[1.0 pt]`
**(b)** Write `show ip route` output interpretation: differentiate `O*E2` from `O*IA` default routes. `[1.0 pt]`
**(c)** Describe how to verify end-to-end connectivity after fix. `[0.5 pt]`

> **Rubric:** OSPF default propagation (1.0 pt) · Route type interpretation (1.0 pt) · Verification (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="routing" -->
### Scenario 8: Route Summarization Creating a Black-Hole

**Context:** After enabling OSPF route summarization on an ABR, some hosts in the 192.168.16.0–192.168.31.0 range are unreachable. A `show ip route` on the ABR shows a `Null0` entry for the summary.

**(a)** Explain why IOS automatically installs a Null0 discard route when summarization is configured. `[1.0 pt]`
**(b)** Identify which specific subnets in the range would be black-holed and why. `[1.0 pt]`
**(c)** Describe TWO strategies to mitigate unintended traffic drops from summarization. `[0.5 pt]`

> **Rubric:** Null0 explanation (1.0 pt) · Black-hole identification (1.0 pt) · Mitigation strategies (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="routing" -->
### Scenario 9: Administrative Distance Conflict

**Context:** A static route (Laluan Statik) `192.168.50.0/24 via 10.1.1.1` was configured as a backup path. After OSPF redistributes the same prefix with a better metric, both routes appear but traffic still uses the static route.

**(a)** Explain how Administrative Distance (Jarak Pentadbiran) determines route preference between static and OSPF. `[1.0 pt]`
**(b)** Calculate: if the static route has AD=1 and OSPF has AD=110, which wins? How do you make OSPF preferred? `[1.0 pt]`
**(c)** Describe the concept of a "floating static route" and write the IOS command for this scenario. `[0.5 pt]`

> **Rubric:** AD explanation (1.0 pt) · AD calculation and fix (1.0 pt) · Floating static (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="vpn" -->
### Scenario 10: IKEv2 Phase 1 SA Negotiation Failure

**Context:** A site-to-site IPSec VPN (Rangkaian Persendirian Maya) between HQ and branch cannot establish. `show crypto ikev2 sa` shows `DELETED` state. The peer IP is reachable via `ping`. Per RFC 7296, Phase 1 uses IKE_SA_INIT exchange.

**(a)** List FOUR parameters that must match exactly between IKEv2 peers for Phase 1 to succeed. `[1.0 pt]`
**(b)** Write the IOS `debug crypto ikev2` command and identify the key error message that indicates a pre-shared key mismatch. `[1.0 pt]`
**(c)** Explain the difference between IKEv1 Main Mode and IKEv2 IKE_SA_INIT in terms of round trips. `[0.5 pt]`

> **Rubric:** Phase 1 parameters (1.0 pt) · Debug and error identification (1.0 pt) · IKEv1 vs IKEv2 comparison (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="vpn" -->
### Scenario 11: IPSec Phase 2 Transform-Set PFS Mismatch

**Context:** IKEv1 Phase 1 completes successfully (`MM_ACTIVE`) but Phase 2 fails. `show crypto ipsec sa` shows 0 encaps/decaps. Both peers show different `perfect-forward-secrecy` (PFS) group settings per RFC 4301.

**(a)** Explain what PFS (Perfect Forward Secrecy) protects against and which DH groups are considered secure. `[1.0 pt]`
**(b)** Write IOS commands to display and align the transform-set and PFS settings on both peers. `[1.0 pt]`
**(c)** State why mismatched PFS group causes Phase 2 failure rather than using the Phase 1 DH key. `[0.5 pt]`

> **Rubric:** PFS explanation and DH groups (1.0 pt) · Transform-set commands (1.0 pt) · PFS failure reason (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="vpn" -->
### Scenario 12: Crypto Map ACL Mismatch on Site-to-Site VPN

**Context:** HQ can ping branch servers but branch cannot initiate traffic to HQ. The IPSec tunnel shows active SAs but only HQ-to-branch packets are encrypted. `show crypto ipsec sa` shows `#pkts encrypt: 0` on the branch router.

**(a)** Explain how a crypto ACL (Senarai Kawalan Capaian) defines the "interesting traffic" and why asymmetric definitions cause one-way VPN. `[1.0 pt]`
**(b)** Write the IOS commands to display and correct the crypto map ACL on the branch router. `[1.0 pt]`
**(c)** Describe the mirror-image rule for crypto ACLs in site-to-site IPSec. `[0.5 pt]`

> **Rubric:** Interesting traffic explanation (1.0 pt) · Diagnosis and correction (1.0 pt) · Mirror-image rule (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="vpn" -->
### Scenario 13: SSL VPN Certificate Expired Causing Client Rejection

**Context:** Remote workers suddenly cannot connect via the SSL VPN (RFC 8446/TLS). Browsers display "Certificate Not Trusted" and VPN client shows `TLS handshake failed`. The gateway certificate expired 3 days ago.

**(a)** Describe the TLS certificate validation steps a VPN client performs per RFC 8446. `[1.0 pt]`
**(b)** Outline the immediate workaround and the proper long-term fix for an expired gateway certificate. `[1.0 pt]`
**(c)** State what a Certificate Revocation List (CRL) is and when it is checked during the handshake. `[0.5 pt]`

> **Rubric:** TLS validation steps (1.0 pt) · Workaround and fix (1.0 pt) · CRL explanation (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="firewall" -->
### Scenario 14: ACL Sequence Order Blocking Legitimate Traffic

**Context:** A new `permit` ACE was added to allow HR workstations (172.16.10.0/24) to reach the payroll server (10.0.5.10). Users still cannot connect. `show ip access-lists` shows zero matches on the new permit entry.

**(a)** Explain ACL top-down processing and how a broader `deny` ACE above the new `permit` causes shadowing. `[1.0 pt]`
**(b)** Write the IOS commands to resequence the ACL so the specific `permit` appears before the broader `deny`. `[1.0 pt]`
**(c)** Describe the impact of the implicit `deny any` at the end of every IOS ACL. `[0.5 pt]`

> **Rubric:** Top-down processing explanation (1.0 pt) · Resequence commands (1.0 pt) · Implicit deny impact (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="firewall" -->
### Scenario 15: NAT Overload (PAT) Port Exhaustion

**Context:** An office of 500 users shares a single public IP via NAT overload (PAT) per RFC 3022. During peak hours, some users cannot establish new internet connections. `show ip nat translations` shows entries near the 65535-port limit.

**(a)** Explain how PAT (Port Address Translation / Terjemahan Alamat Port) maps multiple private IPs to one public IP using port numbers. `[1.0 pt]`
**(b)** Describe TWO solutions to resolve PAT port exhaustion in this scenario. `[1.0 pt]`
**(c)** Write the IOS command to verify the current NAT translation table and count active sessions. `[0.5 pt]`

> **Rubric:** PAT explanation (1.0 pt) · Solutions (1.0 pt) · Verification command (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="firewall" -->
### Scenario 16: Zone-Based Policy Blocking Established Return Traffic

**Context:** A zone-based firewall (Tembok Api) allows traffic from the INSIDE zone to OUTSIDE. Return traffic from web servers is dropped. Users initiate HTTP requests but no responses arrive. `show policy-map type inspect zone-pair` shows drops on the return path.

**(a)** Explain how stateful inspection tracks TCP sessions and why zone-based firewalls require a return-traffic policy. `[1.0 pt]`
**(b)** Write the zone-pair policy commands to permit established TCP/UDP return traffic from OUTSIDE to INSIDE. `[1.0 pt]`
**(c)** Distinguish between `inspect` and `pass` actions in a zone-based policy-map. `[0.5 pt]`

> **Rubric:** Stateful inspection explanation (1.0 pt) · Return-traffic policy commands (1.0 pt) · inspect vs pass distinction (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

<!-- SCENARIO type="firewall" -->
### Scenario 17: Asymmetric Routing Causing Stateful Firewall RST Injection

**Context:** Two firewalls (Tembok Api) in an active-passive cluster are connected to two ISPs. Under asymmetric load, TCP sessions are established through Firewall A but return traffic arrives via Firewall B. Users experience random TCP resets (RST).

**(a)** Explain why asymmetric routing breaks stateful inspection on a single firewall. `[1.0 pt]`
**(b)** Describe TWO network designs that eliminate asymmetric routing in a dual-ISP firewall setup. `[1.0 pt]`
**(c)** Explain the role of session synchronization in a firewall active-active cluster and how it mitigates RST injection. `[0.5 pt]`

> **Rubric:** Asymmetric routing impact (1.0 pt) · Design solutions (1.0 pt) · Session sync role (0.5 pt) · **Total: 2.5 pts** <!-- RUBRIC-TOTAL: 2.5 -->

---

## TAMAT / END OF PAPER

*Answer scheme is provided as a separate instructor document.*
*Marking reference: RFC 2328, RFC 4301, RFC 7296, RFC 3022, RFC 8446, IEEE 802.1D, IEEE 802.1Q, IEEE 802.3ad*
