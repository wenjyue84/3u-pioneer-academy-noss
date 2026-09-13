---
title: "CoCu 4: Server Installation (240 hrs)"
date: 2026-02-07
tags:
  - project
  - education
  - noss
project: "NOSS"
status: active
---

# CoCu 4: Server Installation (240 hrs)


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION | IT-020-3:2013 COMPUTER SYSTEM OPERATION |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 4: Server Installation | CoCu 4: Server Installation |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE JOB ORDER/CHANGE REQUEST · EXECUTE HARDWARE INSTALLATION · CARRY OUT SOFTWARE INSTALLATION · PERFORM SERVER FUNCTIONALITY TEST · PREPARE SERVER INSTALLATION SET-UP REPORT | ANALYSE JOB ORDER/CHANGE REQUEST · EXECUTE HARDWARE INSTALLATION · CARRY OUT SOFTWARE INSTALLATION · PERFORM SERVER FUNCTIONALITY TEST · PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 4 / P(4/7) | PAGE: 73 - 92 |


| Server Type | Tower Server | Rack Server |
|-------------|--------------|-------------|
| Form factor | Standalone chassis similar to a desktop tower. Placed on the floor or in a cabinet. Easier to access for small sites. | Mounted in a rack (1U, 2U, etc.) with rails. Saves space and allows many servers in one location. Requires rack, power, and cooling. |
| Hardware installation | Install components (CPU, RAM, drives, RAID card) similar to a desktop but with server-grade parts. Redundant PSU optional. | Same component types but in a compact chassis. Rails and cable management arms are used. Hot-swap drives and PSUs in many models. |
| Use case | Small business, branch office, or first server. | Data centre, server room, or when many servers are needed. |


| % | Hrs | Work activity | Knowledge 30% | Performance 70% | Total |
|---|-----|---------------|---------------|-----------------|-------|
| 15% | 36 | Analyse job order/change request | 10.8 | 25.2 | 36.0 |
| 40% | 96 | Execute hardware installation | 28.8 | 67.2 | 96.0 |
| 30% | 72 | Carry out software installation | 21.6 | 50.4 | 72.0 |
| 10% | 24 | Perform server functionality test | 7.2 | 16.8 | 24.0 |
| 5% | 12 | Prepare server installation set-up report | 3.6 | 8.4 | 12.0 |
| **100%** | **240** | | **72.0** | **168.0** | **240.0** |


|  |  |  |
| PROGRAM CODE AND NAME | IT-020-3:2013 COMPUTER SYSTEM OPERATION | IT-020-3:2013 COMPUTER SYSTEM OPERATION |
| LEVEL | L3 | L3 |
| NO. AND UNIT TITLE OF COMPETENCY | CoCu 4: Server Installation | CoCu 4: Server Installation |
| NO. AND WORK ACTIVITY STATEMENT | ANALYSE JOB ORDER/CHANGE REQUEST · EXECUTE HARDWARE INSTALLATION · CARRY OUT SOFTWARE INSTALLATION · PERFORM SERVER FUNCTIONALITY TEST · PREPARE SERVER INSTALLATION SET-UP REPORT | ANALYSE JOB ORDER/CHANGE REQUEST · EXECUTE HARDWARE INSTALLATION · CARRY OUT SOFTWARE INSTALLATION · PERFORM SERVER FUNCTIONALITY TEST · PREPARE SERVER INSTALLATION SET-UP REPORT |
| NO. CODE | IT-020-3:2013 - CoCu 4 / P(4/7) | PAGE: 93 - 112 |


| Hardware Component | Description |
|--------------------|-------------|
| Server chassis / form factor | Rack (1U, 2U, etc.) or tower. Rack servers require rails and correct mounting in the rack; cooling and power distribution differ from desktop. Cable management arms and labelling are used for serviceability. |
| Redundant power supply (PSU) | Dual or hot-swap PSUs for availability. Both are connected to different circuits or PDUs where specified so that a single failure does not shut down the server. |
| RAID | Redundant array of disks for capacity and/or redundancy (e.g. RAID 1, 5, 10). Configured in BIOS/UEFI or via a RAID card before installing the OS. The OS is installed after the array is created and recognised. |
| Network interfaces | One or more NICs; IP and VLAN are set as per job order. Cables are connected to the correct switch ports and labelled. |
| Out-of-band management | iLO, iDRAC, or similar for remote console and power. Configure management IP and credentials per job order so that the server can be managed even when the OS is down. |


| Software Type | Description |
|---------------|-------------|
| Server OS | Windows Server or Linux (e.g. CentOS, Ubuntu Server). Installation media and licence or activation as per job order. Roles and features are selected during or after install. |
| Roles and features | E.g. file server, DNS, DHCP, Active Directory, Hyper-V. Installed and configured as specified in the change request. Dependencies (e.g. AD before file server) are followed. |
| Patches and updates | Security and cumulative updates applied after base install. Reboots are scheduled as required; downtime is communicated. |


| Server Installation Report | Required Information |
|----------------------------|----------------------|
| Asset and location | Server name, asset ID, rack position or location. |
| Hardware | Model, CPU, RAM, storage (RAID config), NICs, management IP. |
| Software | OS version, roles and features, key applications. |
| Network | IP addresses, VLAN, gateway, DNS. |
| Sign-off | Installer name and date; acceptance by requester or supervisor. |


**Contact hour:** [[00_Contact-hour_IT-020-3-L3-Operation]]
