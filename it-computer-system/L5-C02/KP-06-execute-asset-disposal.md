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
| KOD DAN NAMA PROGRAM | IT-020-5:2013 PENGURUSAN SISTEM KOMPUTER |
| TAHAP | 5 |
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-C02 COMPUTER SYSTEM ASSET MANAGEMENT |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ANALYSE COMPUTER SYSTEM ASSET INVENTORY<br>2. DEFINE OPERATIONAL STATUS OF ASSETS<br>3. ESTIMATE COSTS AND SPACE REQUIREMENTS<br>4. DETERMINE ASSET MANAGEMENT SYSTEMS<br>5. MONITOR ASSET TAGGING AND LABELLING<br>6. EXECUTE ASSET DISPOSAL<br>7. PREPARE ASSET MANAGEMENT REPORTS |
| NO. KOD | IT-020-5:2013-C02/KP(6/7) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-06-execute-asset-disposal

**TUJUAN:** Kertas rujukan untuk KP-06-execute-asset-disposal.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Describe the legal and regulatory framework for IT asset disposal in Malaysia
2. Identify the criteria that trigger the asset disposal process
3. Explain the approved methods of IT asset disposal
4. Describe secure data destruction standards and techniques
5. Execute the disposal workflow including documentation and authorisation requirements
6. Explain e-waste management obligations under Malaysian environmental law

---

## 1.0 Introduction to IT Asset Disposal

Asset disposal is the final stage of the IT asset lifecycle. Improper disposal creates risks across three dimensions:

| Risk Dimension | Example |
|---------------|---------|
| **Data security** | Confidential data recovered from insufficiently wiped hard drives |
| **Legal and regulatory** | E-waste dumped in violation of Environmental Quality Act 1974 |
| **Financial** | Asset written off incorrectly; disposal proceeds not recorded; assets disposed without authorisation |

At Level 5, the asset manager is responsible for managing the end-to-end disposal process, ensuring that every disposal is authorised, data is securely destroyed, e-waste is handled by a licensed contractor, and all records are updated accordingly.

---

## 2.0 Legal and Regulatory Framework

### 2.1 Malaysian Regulations

| Regulation | Relevance |
|-----------|----------|
| **Environmental Quality Act 1974 (EQA)** and **Environmental Quality (Scheduled Wastes) Regulations 2005** | IT equipment containing hazardous materials (CRT monitors, batteries, mercury-containing devices) is classified as scheduled waste (SW 110); must be disposed of through a licensed scheduled waste contractor |
| **Pekeliling Perbendaharaan Malaysia (Treasury Circular)** | Public sector organisations must obtain approval from the Lembaga Pelupusan Aset (Asset Disposal Board) before disposing of government assets |
| **Personal Data Protection Act 2010 (PDPA)** | Any device storing personal data must have that data securely destroyed before disposal; data controller is liable for breaches |
| **Communications and Multimedia Act 1998** | Licenced equipment (radio, communications devices) must be deregistered with MCMC before disposal |
| **Companies Act 2016** | Asset disposals must be recorded accurately in financial statements; directors may be liable for improper write-offs |

### 2.2 International Standards for Data Destruction

| Standard | Scope |
|---------|-------|
| NIST SP 800-88 Rev.1 | Guidelines for Media Sanitisation — defines Clear, Purge, and Destroy methods |
| DoD 5220.22-M | US Department of Defense standard for overwriting magnetic media; 3-pass and 7-pass methods |
| ISO/IEC 27001 | Information security management — includes media disposal as a control |
| IEEE 2883-2022 | Sanitising storage standard for flash/SSD media |

---

## 3.0 Disposal Trigger Criteria

An asset enters the disposal workflow when it meets one or more of the following criteria:

| Trigger | Evidence Required |
|---------|-----------------|
| Age threshold exceeded | Purchase date + useful life period has passed (e.g. ≥ 5 years for desktop PCs) |
| End-of-support (EOS) | Manufacturer has announced end-of-support; asset cannot run a supported OS or application |
| Uneconomical to repair | Repair quotation ≥ 50% of current replacement value |
| Irreparable damage | Technical report confirming damage beyond economical repair |
| Technologically obsolete | Asset cannot meet current performance requirements; confirmed by IT manager |
| Lease expiry | Operating lease period ended and asset returned to lessor |
| Surplus after redeployment review | Idle asset confirmed surplus after exhausting redeployment options |

---

## 4.0 Asset Disposal Methods

| Method | Description | Suitable For | Considerations |
|--------|-------------|-------------|----------------|
| **Public Auction (Lelongan Awam)** | Assets sold to highest bidder through a licensed auctioneer | Assets with residual commercial value; good cosmetic condition | Proceeds credited to organisation; auctioneer fee applies |
| **Direct Sale / Tender** | Assets offered at a fixed price or through competitive tender to interested buyers | Specific assets with known market value | Requires management approval; transparent process |
| **Trade-in** | Old assets surrendered to vendor as part-exchange when purchasing new equipment | Vendor willing to accept trade-in; reduces net procurement cost | Vendor must confirm data destruction or the organisation must wipe before trade-in |
| **Donation** | Assets donated to schools, NGOs, or government agencies | Functional assets that are too old for organisational use but still useful | Data must be destroyed; donee must acknowledge receipt; deed of gift required |
| **Scheduled Waste Disposal** | Hazardous IT assets handed over to a licensed scheduled waste contractor | CRT monitors, batteries, mercury lamps, PCB-containing equipment | Contractor must hold DOE licence; Consignment Note (CN) required |
| **Recycling (E-waste)** | Non-hazardous IT equipment sent to a licensed e-waste recycler | Non-CRT end-of-life equipment; plastic, metal recovery | Contractor must be registered with KPKT or DOE |
| **Destruction** | Physical destruction of the asset to prevent any re-use | Highly confidential media; damaged equipment with no residual value | Witnessed destruction; destruction certificate issued |

---

## 5.0 Secure Data Destruction

Before any asset containing storage media is disposed of, data must be securely destroyed. The method chosen depends on the sensitivity classification of the data stored and the type of media.

### 5.1 Data Sensitivity Classification

| Classification | Description | Minimum Destruction Method |
|---------------|-------------|--------------------------|
| Public | Non-sensitive data; already publicly available | Clear (single overwrite) |
| Internal | Organisation's internal business data | Purge (multi-pass overwrite or cryptographic erase) |
| Confidential | Personnel data, financial data, client data | Purge or Destroy |
| Restricted / Secret | Regulatory data, security-related information | Physical destruction |

### 5.2 Data Destruction Methods

| Method | Applicable Media | Description | Standard |
|--------|----------------|-------------|---------|
| **Overwriting (Software Wipe)** | HDDs, USB drives, SD cards | Software tool overwrites every sector with zeros, ones, or random patterns | NIST 800-88 Clear; DoD 5220.22-M (3 or 7 pass) |
| **Cryptographic Erase** | SSDs, NVMe drives, self-encrypting drives (SED) | Erase the encryption key; all stored data becomes unreadable | NIST 800-88 Purge; IEEE 2883 |
| **ATA Secure Erase** | SATA/NVMe SSDs | Native drive command that erases all storage cells; faster than overwriting | NIST 800-88 Purge |
| **Degaussing** | Magnetic HDDs, magnetic tapes | Strong magnetic field destroys magnetic orientation; data unrecoverable; drive physically inoperable after | NIST 800-88 Purge |
| **Physical Shredding** | HDDs, SSDs, optical media, USB drives | Industrial shredder reduces media to fragments ≤ 2 mm | NIST 800-88 Destroy |
| **Incineration** | All media types | Controlled high-temperature incineration | NIST 800-88 Destroy; requires DOE permit |

**Recommended tools for software wiping:**
- DBAN (Darik's Boot and Nuke) — free; for HDDs
- Blancco Drive Eraser — commercial; certified; generates audit-ready certificate
- Eraser — free; Windows-based; for specific files or full drive wipe
- hdparm — Linux command-line; ATA Secure Erase for SSDs

### 5.3 Data Destruction Certificate

Every media sanitisation or destruction event must produce a Data Destruction Certificate containing:

- Organisation name
- Asset ID and serial number of every device
- Method of destruction used
- Standard applied (NIST 800-88, DoD)
- Name and signature of the person performing the destruction
- Date of destruction
- Witness name and signature (for physical destruction)
- Contractor name and licence number (if outsourced)

---

## 6.0 Disposal Workflow and Authorisation

| Step | Action | Responsible Party | Document |
|------|--------|------------------|---------|
| 1 | Asset manager identifies assets meeting disposal criteria; prepares disposal list | Asset Manager | Disposal Candidate List |
| 2 | Technical assessment confirms asset condition and data destruction requirement | IT Technician | Technical Assessment Report |
| 3 | Data destruction carried out; destruction certificate issued | IT Technician / Contractor | Data Destruction Certificate |
| 4 | Disposal list submitted to approving authority (e.g. Lembaga Pelupusan Aset / Board of Directors) | Asset Manager | Disposal Approval Form |
| 5 | Approving authority reviews and signs the disposal approval | Approving Authority | Signed Disposal Approval Form |
| 6 | Disposal method executed (auction, recycling, destruction) | Asset Manager / Vendor | Auction Receipt / Recycling Certificate / Destruction Certificate |
| 7 | Disposal proceeds recorded (if any) | Finance Department | Official Receipt / Cheque |
| 8 | Asset records updated in ITAM system: status set to "Disposed"; disposal date and method recorded | Asset Manager | ITAM System update |
| 9 | Asset removed from asset register and insurance schedule | Asset Manager / Finance | Updated Asset Register |
| 10 | Disposal report submitted to management and filed | Asset Manager | Disposal Report |

---

## 7.0 E-Waste Management Obligations

IT equipment falls under e-waste (Sisa Elektrik dan Elektronik) regulations in Malaysia. Key obligations:

| Obligation | Detail |
|-----------|--------|
| Use licensed contractors | E-waste contractor must hold a valid licence from the Department of Environment (DOE) or be registered under KPKT's e-waste recycling programme |
| Retain consignment notes | For scheduled waste: Consignment Note (CN) from DOE must be retained for a minimum of 3 years |
| No open burning or illegal dumping | Offence under Environmental Quality Act 1974; fine up to RM 500,000 or imprisonment |
| Battery disposal | Lithium-ion batteries from laptops and UPS units must be disposed of separately as scheduled waste |
| CRT monitor disposal | CRT monitors contain lead and must be handled as scheduled waste; hand over to licensed contractor only |

---

## 8.0 Common Errors in Asset Disposal

| Error | Consequence | Prevention |
|-------|-------------|------------|
| Disposing without management approval | Audit finding; potential fraud allegation; staff disciplinary action | Enforce approval workflow; no asset may leave premises without signed approval |
| Inadequate data destruction | Data breach; PDPA liability; reputational damage | Apply NIST 800-88 standards; obtain and retain destruction certificate |
| Using unlicensed e-waste contractor | DOE enforcement action; fine; organisation liable for illegal dumping | Verify contractor's DOE licence before engaging; keep copy of licence |
| Not updating ITAM system after disposal | Asset appears as "Active" in register; ghost asset count increases | Asset Manager must update ITAM record as part of disposal checklist |
| No record of disposal proceeds | Finance irregularity; audit finding | All proceeds credited to correct account; official receipt retained |

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCu 2
- Environmental Quality Act 1974 — Scheduled Wastes Regulations 2005
- Personal Data Protection Act 2010 (PDPA) — Malaysia
- NIST Special Publication 800-88 Rev.1 — Guidelines for Media Sanitisation
- Pekeliling Perbendaharaan Malaysia — Tatacara Pengurusan Pelupusan Aset Alih Kerajaan
- Jabatan Alam Sekitar (DOE) Malaysia — Scheduled Waste Management: https://www.doe.gov.my
- IEEE 2883-2022 — Standard for Sanitising Storage