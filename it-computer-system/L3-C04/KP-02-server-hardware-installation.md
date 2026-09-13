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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-3:2013-C04 SERVER INSTALLATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE JOB ORDER/CHANGE REQUEST<br>2. EXECUTE HARDWARE INSTALLATION<br>3. CARRY OUT SOFTWARE INSTALLATION<br>4. PERFORM SERVER FUNCTIONALITY TEST<br>5. PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. KOD | IT-020-3:2013-C04/KP(2/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-02-server-hardware-installation

**TUJUAN:** Kertas rujukan untuk KP-02-server-hardware-installation.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify server form factors and rack infrastructure components
2. Safely mount a rack-mount server into a server rack using rail kits
3. Install server internal components — processors, memory, storage drives, RAID controllers, and expansion cards — according to vendor specifications
4. Configure RAID levels appropriate to the server's operational requirements
5. Connect power, network, and management cabling in accordance with data centre standards
6. Apply electrostatic discharge (ESD) precautions and safe handling procedures throughout hardware installation

---

## 1.0 Server Form Factors

Server hardware comes in several physical configurations. The form factor determines how the server is housed and mounted.

| Form Factor | Description | Typical Use Case |
|-------------|-------------|-----------------|
| Tower server (Pelayan menara) | Upright cabinet resembling a desktop PC tower; standalone | Small office, single-server deployments; no rack required |
| Rack-mount server (Pelayan rak) | Horizontal chassis designed to slide into a standard 19-inch equipment rack; measured in rack units (U, 1U = 44.45 mm height) | Data centres, server rooms with multiple servers |
| 1U server | One rack unit high (~44 mm); compact, high density; limited expansion | Web hosting, edge computing, high-density deployments |
| 2U server | Two rack units high (~89 mm); more drive bays and PCIe slots | General-purpose enterprise server, file server, virtualisation host |
| 4U server | Four rack units high (~178 mm); maximum expansion capacity | High-performance computing, large storage arrays |
| Blade server (Pelayan bilah) | Individual server modules inserted into a shared blade chassis; chassis provides shared power, cooling, and networking | Large enterprise data centres; high-density, high-efficiency |

---

## 2.0 Rack Infrastructure

A **server rack (rak pelayan)** is a standardised 19-inch open frame or enclosed cabinet that houses rack-mount servers and network equipment.

### 2.1 Rack Components

| Component | Function |
|-----------|----------|
| Rack frame / cabinet | Structural enclosure; standard widths: 19 inches (EIA-310); common heights: 12U, 24U, 42U |
| Rack unit (U) markings | Numbered positions on the rack vertical rails; used to specify server placement (e.g. U12–U13 for a 2U server) |
| Rail kit (Kit rel) | Slides that attach to the rack and support the server chassis; allows the server to slide out for maintenance without full removal |
| Cable management arm (CMA) | Articulated arm that routes cables behind the server and maintains cable organisation when the server slides out |
| Power Distribution Unit (PDU) | Rack-mounted power strip that distributes mains power to server PSUs; may be basic (non-metered) or intelligent (metered/switched) |
| Patch panel | Centralised termination point for network cables; links server NIC ports to the network switch |
| KVM switch | Keyboard-Video-Mouse switch that allows one keyboard, monitor, and mouse to manage multiple servers |
| Blank panel (Panel kosong) | Fills unused U positions to maintain airflow direction through the rack |

### 2.2 Rack Airflow Principles

Server racks use a **front-to-back (hadapan-ke-belakang)** airflow pattern:

- Cool air enters from the **front** of the rack (cold aisle / lorong sejuk)
- Hot exhaust air exits from the **rear** of the rack (hot aisle / lorong panas)
- Blank panels must fill all empty U positions to prevent hot air recirculation
- Heavier equipment (UPS, high-density storage) is mounted at the **bottom** of the rack to lower the centre of gravity

---

## 3.0 Pre-Installation Safety and ESD Procedures

Before handling any server component:

1. **Power down** the server completely and disconnect all power cables from the PDU.
2. **Wear an ESD wrist strap (gelang anti-statik)** connected to a grounded ESD mat or the server chassis ground point. ESD can permanently damage processors, RAM, and storage controllers without any visible sign.
3. **Work on an ESD mat** when handling components outside the chassis.
4. **Handle PCBs and drives by their edges.** Do not touch exposed circuitry, connector pins, or solder joints.
5. **Store removed components in anti-static bags** until needed.
6. **Allow the server to cool** for at least 5 minutes after powering down before opening the chassis.
7. **Verify the rack load rating.** Do not exceed the rack's maximum weight capacity per shelf or total rack load.

---

## 4.0 Rack-Mount Server Installation Procedure

### 4.1 Rail Kit Installation

Rail kits vary by vendor (Dell PowerEdge, HPE ProLiant, Lenovo ThinkSystem). Always refer to the vendor rail kit installation guide. The general procedure is:

| Step | Action |
|------|--------|
| 1 | Identify the target rack unit (U) positions from the job order |
| 2 | Attach the inner rail sections to the server chassis side panels using the provided screws |
| 3 | Attach the outer rail sections to the rack vertical posts at the correct U position; most tool-less rails clip directly onto square-hole or round-hole rack posts |
| 4 | Ensure both outer rails are level (use a spirit level) and at the same U position on both sides |
| 5 | Slide the server chassis into the outer rails until it clicks into the retention latch |
| 6 | Secure the server to the rack with the supplied M6 rack screws through the server front ears (at least 2 screws) |
| 7 | Attach the cable management arm (CMA) if provided; route power and network cables through the CMA |

### 4.2 Tower Server Placement

For tower servers:

- Place on a stable, flat surface with adequate clearance on all sides for airflow (minimum 15 cm at front and rear)
- Do not place inside enclosed cabinets without active ventilation
- Connect to a UPS (Uninterruptible Power Supply) for power protection

---

## 5.0 Internal Component Installation

### 5.1 Processor (CPU) Installation

Server processors use high pin-count sockets (e.g. Intel LGA4189 for Xeon Scalable 3rd Gen; AMD SP3 for EPYC). The procedure differs from desktop CPUs:

| Step | Action |
|------|--------|
| 1 | Open the server chassis; locate the processor socket(s) on the motherboard |
| 2 | Lift the socket retention lever(s) as directed by the vendor guide |
| 3 | Remove the protective cover (socket dust cap / Protective Install Bracket, PIB) — keep it for potential return/warranty use |
| 4 | Align the processor with the socket; match the alignment key (notch or arrow marker) |
| 5 | Lower the processor gently into the socket — do not press or rock; it should seat by gravity |
| 6 | Close and lock the retention lever(s) in sequence as specified |
| 7 | Apply thermal interface material (TIM / thermal paste) to the processor IHS (Integrated Heat Spreader) if not pre-applied |
| 8 | Mount the heat sink / cooling solution and tighten in a cross pattern to the specified torque |

**Important:** Server processors have a very high pin count and are extremely expensive. Never force a processor. If it does not seat smoothly, recheck alignment.

### 5.2 Memory (RAM) Installation

Server memory uses ECC (Error-Correcting Code) modules to detect and correct single-bit memory errors — essential for data integrity in server workloads.

| Memory Type | Description |
|-------------|-------------|
| UDIMM (Unbuffered DIMM) | Entry-level; limited to low capacity configurations; used in small/tower servers |
| RDIMM (Registered DIMM) | Buffered; supports higher capacities and more DIMMs per channel; standard for enterprise rack servers |
| LRDIMM (Load-Reduced DIMM) | Uses a memory buffer chip to reduce electrical load; enables very high total memory (1 TB+) |
| NVDIMM (Non-Volatile DIMM) | Retains data on power loss; used for database acceleration and persistent memory |

**Memory population rules:**

- Consult the motherboard or server vendor memory population guide before installing
- Most servers require DIMMs to be installed in **matching pairs or sets of four** to enable dual/quad-channel memory operation
- Always populate the slots specified as "first populated slots" in the vendor guide — incorrect population reduces bandwidth or prevents boot
- Mix of RDIMM and LRDIMM in the same server is **not supported** — use one type only
- ECC DIMMs from the server vendor's Qualified Vendor List (QVL) are strongly recommended

Installation steps:

1. Open the DIMM slot retention clips on both ends
2. Align the DIMM notch with the slot key
3. Press down firmly and evenly until both retention clips click closed
4. Verify all DIMMs are fully seated (no gap between DIMM and slot)

### 5.3 Storage Drive Installation

Server storage uses SAS (Serial Attached SCSI), SATA, or NVMe drives depending on performance requirements.

| Interface | Typical Speed | Use Case |
|-----------|--------------|----------|
| SAS HDD (Hard Disk Drive) | 12 Gb/s interface; 10,000–15,000 RPM | High-reliability sequential workloads; backup targets |
| SAS SSD (Solid State Drive) | 12 Gb/s interface | High-IOPS enterprise workloads (databases, virtualisation) |
| SATA HDD | 6 Gb/s interface; 7,200 RPM | Cost-effective bulk storage; archive |
| SATA SSD | 6 Gb/s interface | General-purpose OS drive, light workloads |
| NVMe SSD (U.2 / M.2 / PCIe AIC) | PCIe Gen 4 × 4: up to 7,000 MB/s | Latency-critical workloads; database primary storage |

**Hot-swap vs cold-swap drives:**

- **Hot-swap (tukar panas):** Drive can be inserted or removed while the server is powered on (requires RAID or HBA support). Most rack servers support hot-swap SAS/SATA drives.
- **Cold-swap (tukar sejuk):** Server must be powered down before changing the drive. M.2 NVMe drives are typically cold-swap.

Drive installation steps:

1. Identify the correct drive bay from the job order (e.g. "bays 0–3 for OS, bays 4–7 for data")
2. Insert the drive into its carrier/caddy; secure with the caddy screws
3. Slide the drive carrier into the bay until the latch clicks
4. Confirm the drive activity LED illuminates (amber/green depending on vendor)

### 5.4 RAID Controller Installation

A **RAID controller (pengawal RAID)** is a hardware component (PCIe card or onboard chip) that manages multiple physical drives as a single logical volume and provides data redundancy.

**Common RAID levels for servers:**

| RAID Level | Minimum Drives | Description | Fault Tolerance | Usable Capacity | Typical Use Case |
|------------|---------------|-------------|-----------------|----------------|-----------------|
| RAID 0 (Striping) | 2 | Data striped across drives for maximum performance; no redundancy | None | 100% | Temporary/scratch data only — not recommended for production |
| RAID 1 (Mirroring) | 2 | Data mirrored exactly on two drives | 1 drive failure | 50% | OS boot drive; critical small-capacity data |
| RAID 5 (Striping with parity) | 3 | Data and single parity distributed across drives | 1 drive failure | (N–1)/N | General-purpose file and application servers |
| RAID 6 (Striping with dual parity) | 4 | Data with two parity sets distributed across drives | 2 drive failures | (N–2)/N | High-availability storage where rebuild risk is unacceptable |
| RAID 10 (1+0, Mirror + Stripe) | 4 | Mirrored pairs then striped; combines performance and redundancy | 1 drive per mirrored pair | 50% | Database servers, virtualisation hosts — high performance + redundancy |

**Hardware RAID controller installation:**

1. Power off the server; open the chassis
2. Insert the RAID controller card into the specified PCIe slot (refer to motherboard guide for primary PCIe slot recommendation)
3. Secure with the PCIe slot screw/retention clip
4. Connect the SAS/SATA data cables (mini-SAS HD SFF-8643 or SFF-8087) from the controller to the drive backplane
5. Connect the RAID controller battery backup unit (BBU) or capacitor pack if supplied — the BBU protects write cache data during a power failure
6. Connect the RAID controller management cable to the server management bus if required

**RAID configuration** is performed during the server's first boot via the RAID controller BIOS utility (e.g. Ctrl+R for Dell PERC, Ctrl+A for Adaptec, F8 for HPE Smart Array) or post-OS via vendor RAID management software.

### 5.5 Network Interface Card (NIC) Installation

| Step | Action |
|------|--------|
| 1 | Select the correct PCIe slot as specified in the job order (verify slot generation and lane width match the NIC requirements) |
| 2 | Remove the slot cover bracket from the chassis rear |
| 3 | Insert the NIC into the PCIe slot; press firmly until fully seated |
| 4 | Secure with the PCIe slot screw |
| 5 | Install the NIC driver after OS installation (pre-loading may be required if the OS installation media does not include the driver) |

---

## 6.0 Cabling

### 6.1 Power Cabling

- Connect each server PSU to a separate PDU circuit where possible (provides redundancy)
- Use **IEC 60320 C13/C14** connectors for standard 1U/2U servers (rated 10 A / 250 V)
- Use **IEC 60320 C19/C20** connectors for high-power servers (rated 16 A / 250 V)
- Label all power cables at both ends with rack ID and equipment name

### 6.2 Network Cabling

| Cable Type | Standard | Max Length | Use Case |
|------------|----------|------------|----------|
| Cat6A UTP | TIA-568-C.2 | 100 m | 10GbE server-to-switch connections |
| Cat6A STP | TIA-568-C.2 | 100 m | 10GbE in high-EMI environments |
| OM3 multimode fibre | TIA-492AAAC | 300 m (10GbE) | Longer in-building runs; SFP+ transceivers |
| OM4 multimode fibre | TIA-492AAAD | 400 m (10GbE) | Extended multimode runs |
| Single-mode fibre | OS2 | kilometres | Inter-building; WAN links |
| Direct Attach Copper (DAC) | — | 1–7 m | Short rack-to-switch 10GbE/25GbE connections; cost-effective |

- Patch cables should be a different colour from cross-connect cables for easy identification
- Leave sufficient slack for the cable management arm to articulate without strain
- Label all network cables at both ends with server name, port, and switch port

### 6.3 Management Cabling (Out-of-Band Management)

Modern servers include a **Baseboard Management Controller (BMC)** — a dedicated microcontroller that provides remote management independent of the server OS. Common implementations:

| Vendor | BMC Implementation Name |
|--------|------------------------|
| Dell | iDRAC (Integrated Dell Remote Access Controller) |
| HPE | iLO (Integrated Lights-Out) |
| Lenovo | XCC (XClarity Controller) |
| Supermicro | IPMI / BMC |

Connect the dedicated BMC/iDRAC/iLO management port to the management network using a separate VLAN from the production network. This allows the server to be powered on, rebooted, or recovered remotely even when the OS has crashed.

---

## 7.0 Post-Hardware Installation Verification

Before proceeding to OS installation, verify the hardware installation:

| Check | Method |
|-------|--------|
| Power-on self-test (POST) completes without error | Power on the server; observe front panel LEDs and POST screen |
| All processors detected | Enter BIOS/UEFI setup; verify CPU count and core count |
| All memory detected at full capacity | Enter BIOS/UEFI setup; verify total RAM and check for memory error alerts |
| All drives detected | Enter RAID controller BIOS or UEFI storage management; verify all drives appear |
| RAID array status is optimal | RAID controller BIOS shows array status as "Optimal" or "Ready" |
| Network ports detected | BIOS/UEFI or NIC configuration utility shows all NIC ports |
| BMC/iDRAC accessible | Connect from a management PC to the BMC IP address; verify web interface loads |
| No hardware error LEDs | Front panel health LED is green (no amber/red fault indicators) |

---

## 8.0 Common Errors in Server Hardware Installation

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Incorrect rail kit orientation | Server cannot slide into rack or rails damage chassis | Match rail kit left/right and front/rear orientation markings before mounting |
| Mixing RDIMM and LRDIMM | Server fails to boot or runs in degraded memory mode | Use one DIMM type only; verify against vendor QVL |
| Incorrect DIMM slot population | Single-channel operation instead of dual/quad-channel; reduced performance or boot failure | Follow vendor memory population guide exactly |
| Forgetting to connect RAID BBU | Write cache disabled; severe performance reduction or data loss on power failure | Connect BBU before powering on; verify BBU status in RAID BIOS |
| ESD damage to components | Silent component failure or intermittent system instability | Always wear ESD wrist strap; use ESD mat and bags |
| Over-tightening rack screws | Stripped rack nuts or bent chassis ears | Use correct torque; finger-tighten then quarter-turn with screwdriver |
| Incorrect RAID level for workload | Data loss (RAID 0), insufficient performance (RAID 5 for write-intensive DB) | Confirm RAID level with job order and workload requirements before configuring |
| Skipping blank panel installation | Hot air recirculation overheats servers; premature hardware failure | Install blank panels in all empty U positions before commissioning |

---

## Rujukan / References

- NOSS IT-020-3:2013 Computer System Operation — CoCU 4: Server Installation
- Dell Technologies PowerEdge Installation and Service Manual (applicable model)
- HPE ProLiant Server Installation Guide (applicable model)
- CompTIA Server+ Study Guide (SK0-005) — Chapter on Server Hardware
- RAID Advisory Board: RAID Level Reference
- TIA-942 Data Centre Infrastructure Standard
- EIA-310 Standard for Cabinets, Racks, Panels, and Associated Equipment