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
| KOD DAN TAJUK UNIT KOMPETENSI | IT-020-5:2013-E01 SERVER SCRIPTING |
| NO. DAN PERNYATAAN AKTIVITI KERJA | 1. ASSESS SERVER SCRIPTING REQUIREMENT<br>2. DEVELOP SERVER SCRIPT<br>3. EXECUTE AND DEPLOY SERVER SCRIPT<br>4. PREPARE SERVER SCRIPT DOCUMENTATION |
| NO. KOD | IT-020-5:2013-E01/KP(1/4) |
| Muka Surat | 1/1 |
| WARNA KERTAS | PUTIH (White) |

**TAJUK:** KP-01-server-scripting-requirements-assessment

**TUJUAN:** Kertas rujukan untuk KP-01-server-scripting-requirements-assessment.

<!-- /JPK_ENVELOPE_v1 -->
## Objektif Pembelajaran / Learning Objectives

Upon completion of this Information Sheet, trainees shall be able to:

1. Define server scripting and explain its role in enterprise systems management
2. Identify and classify server scripting requirements from organisational and technical inputs
3. Select appropriate scripting languages and platforms based on server environment and task requirements
4. Perform a structured scripting requirements assessment and document findings

---

## 1.0 Introduction to Server Scripting

Server scripting (pengskrip pelayan) refers to the development of automated scripts that execute on server infrastructure to perform administrative, configuration, monitoring, deployment, and maintenance tasks without manual intervention. Unlike client-side scripts, server scripts run in privileged environments and interact directly with the operating system, file system, network services, and application stacks.

At Level 5 of the Computer Systems Management competency, practitioners are expected to design and deploy scripts that operate at scale — automating tasks across multiple servers, integrating with enterprise tools, and ensuring reliability through error handling, logging, and version control.

**Common server scripting use cases:**

| Use Case | Description |
|----------|-------------|
| System administration | User account management, disk quota enforcement, log rotation |
| Configuration management | Applying OS and application settings consistently across server fleet |
| Deployment automation | Deploying application packages, updating dependencies, restarting services |
| Monitoring and alerting | Health checks, threshold-based alerts, automated remediation |
| Scheduled maintenance | Backup jobs, certificate renewal, database maintenance routines |
| Security compliance | Audit log collection, patch status reporting, hardening verification |

---

## 2.0 Scripting Languages and Platform Selection

Choosing the correct scripting language is the first technical decision in a requirements assessment. The choice depends on the target operating system, existing infrastructure tooling, team expertise, and task complexity.

### 2.1 PowerShell (Windows and Cross-Platform)

PowerShell is the primary scripting environment for Windows Server administration and is the preferred choice for Microsoft ecosystem environments. PowerShell 7+ (PowerShell Core) runs cross-platform on Linux and macOS, making it suitable for hybrid environments.

**Strengths:**
- Native integration with Active Directory, Exchange, Azure, and Microsoft 365 via modules
- Object-based pipeline — cmdlets pass structured objects, not text strings
- Remoting via `Enter-PSSession` and `Invoke-Command` for multi-server execution
- Consistent error handling with `try/catch/finally` blocks

**Version considerations:**

| Version | Environment | Key Features |
|---------|-------------|--------------|
| Windows PowerShell 5.1 | Windows only | Legacy; pre-installed on Windows Server 2016/2019 |
| PowerShell 7.x (Core) | Cross-platform | Parallel execution (`ForEach-Object -Parallel`), improved error handling |

### 2.2 Bash (Linux/Unix)

Bash (Bourne Again Shell) is the default shell scripting language on most Linux server distributions (Ubuntu, RHEL, Debian, Rocky Linux). It is the correct choice for Linux-native server environments.

**Strengths:**
- Direct access to all POSIX system calls and utilities (`grep`, `awk`, `sed`, `find`, `cron`)
- Lightweight — no additional runtime required
- Universally available on Linux servers
- Well-suited for pipeline-based text processing and file operations

### 2.3 Python

Python is appropriate when scripts require complex logic, data processing, API integration, or cross-platform compatibility beyond what shell scripting offers efficiently.

**Strengths:**
- Rich standard library (`os`, `subprocess`, `pathlib`, `logging`, `json`, `requests`)
- Excellent for REST API interaction, data transformation, and report generation
- Cross-platform by design
- Third-party ecosystem (Ansible, Fabric, Paramiko) for server automation

### 2.4 Selection Decision Matrix

| Criterion | PowerShell | Bash | Python |
|-----------|-----------|------|--------|
| Target OS: Windows Server | ★★★ | ★ | ★★ |
| Target OS: Linux | ★★ | ★★★ | ★★ |
| Complex data processing | ★★ | ★ | ★★★ |
| API integration | ★★ | ★ | ★★★ |
| AD/Azure/M365 | ★★★ | ✗ | ★★ |
| Cron/Task Scheduler | ★★ | ★★★ | ★★ |
| Team familiarity (typical IT shop) | ★★ | ★★ | ★★★ |

---

## 3.0 Requirements Assessment Process

A structured requirements assessment prevents scope creep, wrong language selection, and unmet stakeholder expectations. The assessment follows six phases:

### Phase 1: Stakeholder Identification

Identify all parties who will be affected by or who will use the script:

- **Requestor:** The person or team requesting the automation (e.g. IT Operations, Security team)
- **Owner:** The person responsible for the server(s) the script will run on
- **End users:** Those who will trigger or rely on script output (e.g. reports, notifications)
- **Approver:** Management or change advisory board authorising production deployment

### Phase 2: Functional Requirements Gathering

Collect the detailed technical requirements:

| Requirement Type | Questions to Answer |
|-----------------|---------------------|
| Task description | What exactly must the script do? (Input → Process → Output) |
| Trigger | How is the script initiated? (Manual, scheduled, event-driven?) |
| Target systems | Which servers, OS versions, and environments (Dev/UAT/Prod)? |
| Input sources | Files, databases, API endpoints, user parameters? |
| Expected output | Files, emails, database entries, console output, return codes? |
| Error handling | How should failures be reported and handled? |
| Logging | What events must be logged? Where (local file, SIEM, Event Log)? |

### Phase 3: Non-Functional Requirements

| Requirement | Consideration |
|-------------|---------------|
| Performance | Maximum acceptable execution time; impact on server load |
| Security | Minimum privilege principle; credential storage; encryption |
| Maintainability | Coding standards, comments, version control repository |
| Portability | Will the script run on multiple OS versions or distributions? |
| Auditability | Is a full audit trail required for compliance? |

### Phase 4: Constraint Analysis

Identify limitations that constrain the solution:

- **Security policies:** Are there restrictions on execution policy (PowerShell), sudo access (Linux), or interpreter versions (Python)?
- **Network restrictions:** Can the script reach external endpoints (APIs, update servers)?
- **Licensing:** Are required modules/packages available and licensed?
- **Change freeze periods:** Are there blackout windows during which the script must not execute?

### Phase 5: Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Script runs with excessive privilege | Medium | High | Apply principle of least privilege; use dedicated service accounts |
| Unhandled exception causes data loss | Medium | High | Implement comprehensive error handling and dry-run mode |
| Hardcoded credentials in script | High | Critical | Use credential stores (Windows Credential Manager, vault) |
| Script fails silently on one of many target servers | Medium | Medium | Implement per-server result tracking and summary reporting |

### Phase 6: Documentation and Sign-Off

Produce a **Scripting Requirements Document (SRD)** containing:

1. Executive summary (purpose, scope, stakeholders)
2. Functional requirements table
3. Non-functional requirements table
4. Constraint and risk register
5. Recommended scripting language and platform
6. Proposed schedule and milestones
7. Approval signatures

---

## 4.0 Sample Requirements Assessment Scenario

**Scenario:** The IT Operations team at a company running 20 Windows Server 2022 nodes needs an automated script to check disk space on all servers every morning and email a report to the IT Manager if any drive is above 85% capacity.

**Assessment output:**

| Field | Detail |
|-------|--------|
| Requestor | IT Operations Manager |
| Target systems | 20 × Windows Server 2022 nodes |
| Trigger | Scheduled — daily at 06:00 |
| Input | WMI/CIM query for disk space on each server |
| Output | Email report to IT Manager; log file on management server |
| Error handling | If a server is unreachable, log the failure and include in report |
| Language selected | PowerShell 7 (native Windows, remoting, built-in email cmdlets) |
| Execution account | Domain service account with WMI read access (read-only, no admin) |
| Risk identified | Hardcoded credentials — mitigated by Windows Credential Manager |
| Approver | IT Manager + Change Advisory Board |

---

## 5.0 Checklist: Requirements Assessment Completion

Before proceeding to script development, confirm:

- [ ] Functional requirements documented and approved by stakeholder
- [ ] Non-functional requirements (performance, security, audit) defined
- [ ] Scripting language and version confirmed against target environment
- [ ] Execution account and privilege level agreed and provisioned
- [ ] Error handling and logging strategy defined
- [ ] Version control repository identified
- [ ] Change request or approval obtained for production scope

---

## Rujukan / References

- NOSS IT-020-5:2013 Computer Systems Management — CoCU E01 Server Scripting
- Microsoft Documentation: PowerShell 7 Overview — https://learn.microsoft.com/en-us/powershell/
- GNU Bash Reference Manual — https://www.gnu.org/software/bash/manual/
- Python Documentation: os, subprocess, logging modules — https://docs.python.org/3/
- NIST SP 800-53: Security and Privacy Controls — Least Privilege (AC-6)