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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-4:2013-C03 COMPUTER SYSTEM & NETWORK PROCUREMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. IDENTIFY PROCUREMENT REQUIREMENTS<br>2. PREPARE SPECIFICATIONS AND TENDER DOCUMENTS<br>3. EVALUATE QUOTATIONS AND VENDORS<br>4. MANAGE PROCUREMENT AND DELIVERY<br>5. DOCUMENT PROCUREMENT RECORDS |
| NO. KOD | IT-020-4:2013-C03/KP(1/5) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-identify-procurement-requirements

**TUJUAN:** Kertas rujukan untuk KP-01-identify-procurement-requirements.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Explain the purpose and legal framework of ICT procurement in Malaysian organisations
2. Identify and categorise hardware, software, and network requirements from organisational needs
3. Distinguish between open tender, limited tender, direct purchase, and quotation methods under government procurement regulations
4. Prepare a procurement needs assessment document aligned with organisational ICT policy

---

## 1.0 Introduction to ICT Procurement

Procurement (perolehan) is the formal process by which an organisation acquires goods, services, or works from external suppliers. In the context of ICT systems administration, procurement covers the acquisition of computer hardware, network equipment, licensed software, and related services.

At Level 4, the systems administrator must not only understand technical specifications but also navigate the regulatory, budgetary, and organisational governance frameworks that govern procurement. Poor requirements identification at this stage results in misaligned purchases, budget overruns, and non-compliance with government or corporate procurement regulations.

In Malaysia, government ICT procurement is governed primarily by:
- **Arahan Perbendaharaan (AP)** — Treasury Instructions on procurement procedures
- **Pekeliling Perbendaharaan** — Treasury Circulars issued periodically to update procurement limits and methods
- **MyGovIS / MyICMS** — MAMPU guidelines on government ICT procurement planning

---

## 2.0 Types of Procurement Need

ICT procurement requirements arise from several organisational triggers:

| Trigger | Description | Example |
|---------|-------------|---------|
| New project / expansion | Organisation grows or opens new site requiring new infrastructure | New branch office requiring 20 workstations and network switches |
| Replacement cycle | Aging hardware reaches end-of-life or end-of-support | PCs older than 5 years scheduled for replacement under ICT asset refresh plan |
| Capacity upgrade | Existing systems cannot meet performance demands | Server RAM upgrade to support additional virtualised services |
| Regulatory / compliance | New legal or security requirements mandate upgraded systems | Data centre firewall upgrade to comply with PDPA or ISO 27001 requirements |
| Disaster / fault replacement | Hardware failure requires emergency replacement | UPS failure requiring immediate purchase to restore power protection |

---

## 3.0 Procurement Methods in Malaysia

The method of procurement depends on the estimated value of the purchase and the regulatory threshold applicable at the time:

| Method | Malay Term | Typical Threshold | Key Feature |
|--------|-----------|------------------|-------------|
| Direct purchase (Pembelian terus) | Pembelian Terus | Up to RM50,000 | Single supplier; no quotation required |
| Quotation (Sebut harga) | Sebut Harga | RM50,001 – RM500,000 | Minimum 3 written quotations required |
| Limited tender | Tender Terhad | RM500,001 – RM5,000,000 | Invited from pre-qualified suppliers; MOF registration required |
| Open tender | Tender Terbuka | Above RM5,000,000 | Public advertisement; evaluated by tender committee |

> **Note:** Thresholds are subject to revision by Treasury Circulars (Pekeliling Perbendaharaan). Always verify the current applicable limit before initiating procurement.

---

## 4.0 Needs Assessment Process

A structured needs assessment ensures that procurement requirements are complete, accurate, and justified before progressing to specification or tender stages.

### Step 1: Identify the Business Need

Work with department heads and end users to understand:
- What problem or opportunity is driving the procurement
- How many users or locations are affected
- The required operational timeline (when must the system be ready)

### Step 2: Inventory Current Assets

Review the existing ICT asset register to determine:
- What is currently deployed (hardware model, age, warranty status)
- What can be retained, upgraded, or repurposed
- What must be fully replaced

### Step 3: Define Functional Requirements

Translate business needs into functional requirements (what the system must do):

| Category | Examples |
|----------|---------|
| Hardware | Number of workstations, server specifications, network switches, UPS |
| Software | Operating system licensing model, productivity suite, security software |
| Network | Bandwidth requirements, VPN, Wi-Fi coverage, firewall rules |
| Services | Installation, training, warranty, maintenance contract |

### Step 4: Define Non-Functional Requirements

| Requirement | Description |
|-------------|-------------|
| Performance | Minimum processor speed, RAM, storage I/O performance |
| Scalability | Capacity for future growth (e.g. additional users in 2 years) |
| Security | Compliance with ISMS, data encryption, access control |
| Compatibility | Interoperability with existing systems and software versions |
| Warranty & support | Minimum warranty period, SLA response time |

### Step 5: Obtain Budget Allocation

Confirm budget availability and approval level required:
- Below RM50,000: Head of Department approval
- RM50,001 and above: Finance Division and/or Procurement Committee
- Government agencies: must align with Annual ICT Procurement Plan (Rancangan Tahunan Perolehan ICT)

### Step 6: Document the Needs Assessment

Produce a formal Needs Assessment Report containing:
- Business justification
- Current state description
- Required functionality
- Preliminary budget estimate
- Recommended procurement method
- Approval signatures

---

## 5.0 ICT Procurement Policy Compliance

All procurement activities must comply with internal ICT policy and external regulatory requirements:

| Requirement | Detail |
|-------------|--------|
| MOF supplier registration | Vendors must be registered with Kementerian Kewangan (MOF) for government contracts |
| Bumiputera participation | Government procurement at certain thresholds requires consideration of Bumiputera vendors (see current AP/Pekeliling) |
| Green procurement | Energy Star or equivalent energy efficiency certification for hardware where applicable |
| Data security | Procurement of systems handling personal data must comply with Personal Data Protection Act 2010 (PDPA) |
| Cybersecurity | Critical systems must conform to NACSA guidelines and CIS benchmarks |

---

## 6.0 Common Errors in Requirements Identification

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Vague requirements (e.g. "fast computer") | Non-comparable quotations; wrong equipment purchased | Use measurable specifications (e.g. "Intel Core i7 Gen 13, 16 GB RAM") |
| Ignoring compatibility with existing systems | New equipment cannot integrate with current network or software | Conduct compatibility review before finalising requirements |
| Underestimating quantity | Insufficient units procured; repeat procurement required | Verify head count and spares policy with department |
| Omitting services from scope | Installation, training, or warranty not covered | Include services as line items in the requirements document |
| Failing to obtain budget approval before tendering | Procurement cancelled after tender; wasted time and resources | Confirm approved budget allocation before issuing any tender |

---

## Rujukan / References

- Arahan Perbendaharaan Malaysia (AP) — latest edition
- Pekeliling Perbendaharaan berkaitan perolehan ICT — Kementerian Kewangan Malaysia
- MAMPU — Garis Panduan Perolehan ICT Sektor Awam
- NOSS IT-020-4:2013 Computer Systems Administration — CoCu 3
- Personal Data Protection Act 2010 (PDPA) — Malaysia