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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C01 SERVER CONFIGURATION |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE SERVER CONFIGURATION REQUIREMENTS<br>2. PLAN SERVER ROLES AND SERVICES<br>3. CONFIGURE SERVER HARDWARE AND STORAGE<br>4. CONFIGURE SERVER OS AND ROLES<br>5. IMPLEMENT SERVER SECURITY SETTINGS<br>6. DOCUMENT SERVER CONFIGURATION |
| NO. KOD | IT-020-4:2013-C01/KP(3/6) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-03-server-hardware-and-storage-configuration

**TUJUAN:** Kertas rujukan untuk KP-03-server-hardware-and-storage-configuration.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Identify enterprise server hardware components and explain their function
2. Configure BIOS/UEFI settings appropriate for a production server environment
3. Design and implement a RAID storage configuration matched to the workload's performance and redundancy requirements
4. Configure server storage subsystems including SAN, NAS, and local DAS
5. Verify hardware configuration integrity using out-of-band management tools
6. Apply physical installation best practices for rack-mounted servers

---

## 1.0 Enterprise Server Hardware Overview

Enterprise servers (Pelayan Gred Perusahaan) differ from desktop workstations in several key areas:

| Feature | Desktop Workstation | Enterprise Server |
|---------|--------------------|--------------------|
| **CPU** | 1 socket, consumer grade | 1–4 sockets, Xeon / EPYC, ECC support |
| **RAM** | Non-ECC DDR5 | ECC RDIMM / LRDIMM DDR5, up to TBs |
| **Storage** | Consumer NVMe / SATA | Enterprise NVMe, SAS, RAID controller |
| **Power Supply** | Single PSU | Dual redundant PSU (hot-swap) |
| **Cooling** | Airflow fan | Hot-swap redundant fan modules |
| **Management** | None / basic BIOS | iDRAC (Dell), iLO (HPE), BMC (Supermicro) |
| **Form factor** | Tower | Rack-mount (1U–4U), blade |
| **Availability** | Best-effort | 99.9%+ design target |
| **Certification** | Consumer | ISV-certified (VMware HCL, Windows Server logo) |

---

## 2.0 Server CPU Configuration

### 2.1 CPU Selection Criteria

| Criterion | Consideration |
|-----------|--------------|
| **Socket type** | Must match motherboard: Intel LGA4677 (Xeon Scalable 4th Gen), AMD SP5 (EPYC Genoa) |
| **Core count** | More cores benefit multi-threaded workloads (virtualisation, database); fewer high-clock cores for single-threaded apps |
| **TDP (Thermal Design Power)** | Determines cooling and power supply requirements |
| **ECC support** | Error-Correcting Code memory support — mandatory for production servers |
| **PCIe lanes** | Number of PCIe lanes available for storage controllers, NICs, and GPUs |

### 2.2 NUMA Configuration

Non-Uniform Memory Access (NUMA) applies to multi-socket servers. Each CPU socket has its own local memory bank; accessing remote memory (across sockets) incurs latency penalty.

- Configure VMs or application processes to be NUMA-local (bound to one socket and its associated memory)
- Check NUMA topology with: `numactl --hardware` (Linux) or `Get-NUMANode` (PowerShell)
- Avoid crossing NUMA nodes unless the workload explicitly requires it

---

## 3.0 Server RAM Configuration

### 3.1 ECC Memory (Ingatan ECC)

Error-Correcting Code (ECC) RAM detects and automatically corrects single-bit memory errors and detects double-bit errors. Production servers must use ECC RAM.

- **RDIMM (Registered DIMM):** Standard server RAM; register buffer reduces electrical load on CPU memory controller; supports more DIMMs per channel
- **LRDIMM (Load-Reduced DIMM):** Extends maximum capacity per slot; used in memory-intensive deployments (large databases, high-density virtualisation)

### 3.2 Memory Population Rules

- Populate DIMMs symmetrically across channels for optimal bandwidth
- Consult the motherboard/server QVL (Qualified Vendor List) before purchasing RAM
- Mixed DIMM populations (different speeds) will downgrade all DIMMs to the lowest speed

---

## 4.0 BIOS/UEFI Configuration for Production Servers

After hardware assembly, the administrator must configure BIOS/UEFI settings before OS installation:

| Setting | Recommended Value | Reason |
|---------|------------------|--------|
| **Boot mode** | UEFI (not Legacy/CSM) | Required for GPT disks > 2 TB; supports Secure Boot |
| **Secure Boot** | Enabled | Prevents loading of unsigned bootloaders/rootkits |
| **Hyper-Threading** | Enabled (default) | Increases throughput for multi-threaded workloads |
| **Virtualisation Technology (VT-x/AMD-V)** | Enabled | Required for hypervisor deployment |
| **VT-d / AMD-Vi (IOMMU)** | Enabled | Required for PCI passthrough in virtualisation |
| **Turbo Boost / Precision Boost** | Enabled | Allows CPU to exceed base clock during bursts |
| **C-States / Power Management** | Set to "OS Controlled" or "Maximum Performance" | Prevents CPU sleep states that add latency for latency-sensitive workloads |
| **NUMA** | Enabled | Ensures NUMA topology is presented correctly to OS |
| **Memory speed** | Set to rated speed (XMP/JEDEC profile) | RAM runs at rated speed, not default JEDEC minimum |
| **Boot order** | 1. Network PXE (for provisioning), 2. USB, 3. Local disk | Allows PXE deployment; disable unnecessary boot devices |
| **IPMI / BMC / iDRAC** | Configure IP address, credentials, alert email | Enables out-of-band management |
| **System Event Log (SEL)** | Enabled | Records hardware faults (fan failure, memory error, voltage alert) |

---

## 5.0 RAID Configuration

RAID (Redundant Array of Independent Disks / Tatasusunan Cakera Bebas yang Berlebihan) combines multiple physical disks into a logical volume to provide data redundancy, improved performance, or both.

### 5.1 Common RAID Levels

| RAID Level | Minimum Disks | Fault Tolerance | Read Performance | Write Performance | Usable Capacity | Recommended Use |
|-----------|--------------|----------------|-----------------|------------------|----------------|----------------|
| **RAID 0** | 2 | None (no redundancy) | High | High | 100% of raw | Temporary/scratch data only — NOT for production |
| **RAID 1** | 2 | 1 disk failure | High (mirrored reads) | Same as single disk | 50% | OS drive, small critical data |
| **RAID 5** | 3 | 1 disk failure | High | Moderate (parity write penalty) | (N−1)/N | General-purpose file, application storage |
| **RAID 6** | 4 | 2 disk failures | High | Lower than RAID 5 | (N−2)/N | Large arrays where rebuild time is long |
| **RAID 10** | 4 | 1 disk per mirror pair | Very high | High | 50% | Database, high-IOPS production workloads |

**Selection guide for Level 4 administrators:**

| Workload | Recommended RAID |
|---------|-----------------|
| OS / boot volume | RAID 1 |
| Database (high IOPS, low latency) | RAID 10 |
| File server (large capacity, lower IOPS) | RAID 5 or RAID 6 |
| Backup storage (capacity-optimised) | RAID 6 |
| Virtualisation datastore | RAID 10 (performance) or RAID 5/6 (capacity) |

### 5.2 Hardware RAID vs Software RAID

| Feature | Hardware RAID Controller | Software RAID (OS) |
|---------|------------------------|--------------------|
| **CPU overhead** | None (dedicated RAID processor) | Moderate (uses host CPU) |
| **Battery-backed write cache** | Yes (BBWC / flash-backed) | No |
| **Performance** | Higher | Lower for parity RAID |
| **Vendor lock-in** | Yes (proprietary metadata) | No |
| **Cost** | Higher | No additional cost |
| **Recommended for** | Production servers | Dev/test or when budget is constrained |

Enterprise RAID controllers (Dell PERC, HPE Smart Array, LSI MegaRAID) include a battery-backed or flash-backed write cache (FBWC) that safely buffers write operations during power loss, significantly improving write performance.

### 5.3 RAID Configuration Procedure

1. Access the RAID controller configuration utility during POST (e.g. Ctrl+R for PERC, F5 for Smart Array)
2. Identify all physical disks and verify disk health (no pre-existing errors)
3. Select the RAID level based on the Server Role Plan
4. Assign hot spare disks (at least 1 hot spare for arrays of 4+ disks)
5. Set the stripe size: 64 KB for general workloads; 256 KB or 1 MB for sequential streaming (backup); 64 KB for random I/O (database)
6. Name the logical drive (e.g. "OS-RAID1", "DATA-RAID10")
7. Initialise the array (Fast Init for new disks; Full Init for reused disks to zero-fill)

---

## 6.0 Storage Subsystem Types

### 6.1 Direct-Attached Storage (DAS — Storan Lampiran Terus)

Storage physically attached to the server via internal SATA, SAS, or NVMe.

- **Advantages:** Low latency, no network dependency, easy to manage
- **Disadvantages:** Not shareable between servers; scaling requires server downtime

### 6.2 Network-Attached Storage (NAS — Storan Lampiran Rangkaian)

A dedicated file server accessible over Ethernet using SMB (Windows) or NFS (Linux/Unix) protocols.

- **Advantages:** Centralised, shared access; easy capacity expansion
- **Disadvantages:** Subject to network latency; performance limited by network throughput

### 6.3 Storage Area Network (SAN — Rangkaian Kawasan Storan)

A dedicated high-speed network connecting servers to shared block-level storage arrays using Fibre Channel (FC) or iSCSI.

- **Advantages:** Block-level access (server sees SAN LUN as a local disk); high performance; supports clustering and live VM migration
- **Disadvantages:** Higher cost and complexity; requires FC HBAs or iSCSI initiators; dedicated SAN switches (for FC)

| Feature | DAS | NAS | SAN |
|---------|-----|-----|-----|
| Protocol | SATA / SAS / NVMe | SMB / NFS | FC / iSCSI |
| Access type | Block | File | Block |
| Shareable | No | Yes | Yes |
| Latency | Lowest | Medium | Low (FC) / Medium (iSCSI) |
| Cost | Low | Medium | High |
| Typical use | Single server | File sharing | Virtualisation, clustering, database |

---

## 7.0 Out-of-Band Management (Pengurusan Luar-Band)

Enterprise servers include a dedicated management controller (BMC) accessible independently of the main OS:

| Vendor | Management Controller | Protocol |
|--------|----------------------|---------|
| Dell | iDRAC (Integrated Dell Remote Access Controller) | HTTPS, IPMI, Redfish |
| HPE | iLO (Integrated Lights-Out) | HTTPS, IPMI, Redfish |
| Supermicro | IPMI BMC | HTTPS, IPMI |
| Lenovo | XClarity Controller | HTTPS, IPMI, Redfish |

Out-of-band management allows the administrator to:
- Power on/off/reset the server remotely
- Access the virtual console (KVM-over-IP) even when the OS is unresponsive
- Monitor hardware health (temperature, fan speed, voltage, disk status)
- Update firmware remotely
- View the System Event Log (SEL) for hardware fault history

**Configuration:** Assign a static IP address on the management VLAN; configure LDAP authentication; enable email alerts for critical events.

---

## 8.0 Common Errors in Hardware and Storage Configuration

| Error | Consequence | Prevention |
|-------|-------------|------------|
| **Wrong RAID level for workload** — RAID 5 on database | Write penalty causes severe database performance degradation | Use RAID 10 for high-IOPS random write workloads |
| **No hot spare configured** | RAID array at risk during rebuild after disk failure | Always configure at least 1 hot spare for arrays with 4+ disks |
| **BBWC disabled or battery flat** | Write cache defaults to write-through; performance drops dramatically | Check BBWC/FBWC health in RAID controller console before go-live |
| **Mixed disk types in RAID array** | Array operates at slowest disk's speed | Use identical disk model, capacity, and RPM/type within an array |
| **Enabling C-States on latency-sensitive server** | CPU parks cores during idle, adding wake-up latency to transactions | Disable C-States or set power profile to Maximum Performance in BIOS |
| **iDRAC/iLO left on default credentials** | Management interface accessible with default password; critical security risk | Change default BMC credentials immediately; isolate on management VLAN |

---

## Rujukan / References

- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 1: Server Configuration
- Dell PowerEdge BIOS and UEFI Reference Guide
- HPE ProLiant Gen11 Server User Guide
- VMware vSAN Design and Sizing Guide
- CompTIA Server+ Exam Objectives — Storage and RAID
- Intel Xeon Scalable Processor Technical Overview