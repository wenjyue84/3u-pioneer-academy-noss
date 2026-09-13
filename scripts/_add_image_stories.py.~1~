"""Add image-related enhancement stories to prd.json."""
import json
from pathlib import Path

prd_path = Path("C:/Users/Jyue/Documents/1-projects/NOSS/prd.json")
d = json.loads(prd_path.read_text(encoding="utf-8"))
max_id = max(int(s["id"].split("-")[1]) for s in d["userStories"])

new_stories = [
    {
        "id": f"US-{max_id+1:03d}",
        "title": "Download hardware component diagrams for L3 CoCu 1-3",
        "description": "Download relevant images from the web for L3 CoCu 1 (Computer System Set-up), CoCu 2 (Maintenance), and CoCu 3 (Repair). Images needed: motherboard layout diagram, CPU socket types (LGA/AM5), RAM slot diagram, PSU connector types, HDD vs SSD vs NVMe comparison, anti-static wrist strap usage, multimeter usage for PSU testing, thermal paste application. Save images to content/IT-020-3/images/ and add markdown image references (![description](images/filename.png)) in the relevant CoCu .md files next to the hardware descriptions.",
        "priority": "high",
        "acceptanceCriteria": [
            "At least 3 images per CoCu file for CoCu 1-3",
            "Images saved in content/IT-020-3/images/ directory",
            "Markdown image references added in .md files next to relevant descriptions",
            "Images are labeled with descriptive alt text",
            "Images are relevant technical diagrams (not stock photos)"
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-3/01_CoCu-1-Computer-System-Set-up.md",
            "content/IT-020-3/02_CoCu-2-Computer-System-Maintenance.md",
            "content/IT-020-3/03_CoCu-3-Computer-System-Repair.md"
        ],
        "estimatedComplexity": "large",
        "tags": ["images", "l3", "visual-content"],
        "epicId": "E-1",
    },
    {
        "id": f"US-{max_id+2:03d}",
        "title": "Download server and network diagrams for L3 CoCu 4-7",
        "description": "Download relevant images for L3 CoCu 4 (Server Installation), CoCu 5 (Server Maintenance), CoCu 6 (Network Connectivity), CoCu 7 (Mobile Device). Images needed: server rack layout, RAID configurations diagram, network topology types (star/bus/ring/mesh), RJ45 cable crimping steps, Cat6 vs Cat6A comparison, Wi-Fi standards chart, mobile device management diagram, BIOS/UEFI screenshot. Save to content/IT-020-3/images/.",
        "priority": "high",
        "acceptanceCriteria": [
            "At least 2 images per CoCu file for CoCu 4-7",
            "Images saved in content/IT-020-3/images/",
            "Markdown image references added in .md files",
            "Images include network topology diagrams and server layouts"
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-3/04_CoCu-4-Server-Installation.md",
            "content/IT-020-3/05_CoCu-5-Server-Maintenance.md",
            "content/IT-020-3/06_CoCu-6-Computer-Network-Connectivity-Set-up.md",
            "content/IT-020-3/07_CoCu-7-Mobile-Device-Configuration.md"
        ],
        "estimatedComplexity": "large",
        "tags": ["images", "l3", "visual-content"],
        "epicId": "E-1",
    },
    {
        "id": f"US-{max_id+3:03d}",
        "title": "Download administration and security diagrams for L4 CoCu files",
        "description": "Download relevant images for all 6 L4 CoCu files. Images needed: server configuration flowchart, Active Directory structure, firewall architecture diagram, network security zones, structured cabling diagram (TIA-568), patch panel layout, VLAN segmentation diagram, backup strategy (3-2-1 rule) visual, ITIL service management framework. Save to content/IT-020-4/images/.",
        "priority": "high",
        "acceptanceCriteria": [
            "At least 2 images per L4 CoCu file",
            "Images saved in content/IT-020-4/images/",
            "Images include security architecture and network infrastructure diagrams",
            "Markdown references added in correct locations within .md files"
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-4/01_CoCu-1-Server-Configuration.md",
            "content/IT-020-4/02_CoCu-2-Computer-System-Security-Control.md",
            "content/IT-020-4/03_CoCu-3-System-Network-Procurement.md",
            "content/IT-020-4/04_CoCu-4-Network-Cabling-Management.md",
            "content/IT-020-4/05_CoCu-5-Computer-Network-Installation-Management.md",
            "content/IT-020-4/06_CoCu-6-Computer-System-Maintenance-Management.md"
        ],
        "estimatedComplexity": "large",
        "tags": ["images", "l4", "visual-content"],
        "epicId": "E-2",
    },
    {
        "id": f"US-{max_id+4:03d}",
        "title": "Download management and strategic diagrams for L5 CoCu files",
        "description": "Download relevant images for all 7 L5 CoCu files. Images needed: IT governance framework (COBIT), risk management matrix, disaster recovery architecture, BCP lifecycle diagram, project management Gantt chart example, WBS breakdown example, ISO 27001 ISMS framework, PDCA cycle diagram, SOP document workflow, server scripting pipeline diagram. Save to content/IT-020-5/images/.",
        "priority": "high",
        "acceptanceCriteria": [
            "At least 2 images per L5 CoCu file",
            "Images saved in content/IT-020-5/images/",
            "Images include management frameworks and strategic planning visuals",
            "Markdown references added in correct locations"
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-5/01_CoCu-1-Management-Overview.md",
            "content/IT-020-5/02_CoCu-2-Computer-System-Asset-Management.md",
            "content/IT-020-5/03_CoCu-3-Computer-System-Security-Management.md",
            "content/IT-020-5/04_CoCu-4-Disaster-Recovery-Management.md",
            "content/IT-020-5/05_CoCu-5-Computer-System-Network-Project-Management.md",
            "content/IT-020-5/06_CoCu-6-SOP-Development-And-Implementation.md",
            "content/IT-020-5/07_CoCu-7-Server-Scripting.md"
        ],
        "estimatedComplexity": "large",
        "tags": ["images", "l5", "visual-content"],
        "epicId": "E-3",
    },
    {
        "id": f"US-{max_id+5:03d}",
        "title": "Update generate_docx.py to embed images in .docx output",
        "description": "The current generate_docx.py does not handle markdown image references. Update it to: (1) detect ![alt](path) patterns in .md content, (2) resolve image paths relative to the content directory, (3) embed images in the .docx using python-docx document.add_picture() with appropriate sizing (max width 15cm to fit A4 margins), (4) add image captions below each image.",
        "priority": "high",
        "acceptanceCriteria": [
            "generate_docx.py detects and embeds all ![alt](path) image references",
            "Images display correctly in generated .docx files",
            "Images are sized appropriately for A4 pages (max 15cm width)",
            "Missing images produce a warning but don't crash the generator",
            "Image captions are rendered below each image"
        ],
        "dependencies": [f"US-{max_id+1:03d}"],
        "passes": False,
        "filesTouch": ["scripts/generate_docx.py"],
        "estimatedComplexity": "medium",
        "tags": ["images", "generator"],
        "epicId": "E-5",
    },
    {
        "id": f"US-{max_id+6:03d}",
        "title": "Add step-by-step procedure screenshots for L3 practical exercises",
        "description": "For each L3 practical exercise, download or create annotated screenshots showing: BIOS/UEFI setup screens, Windows installation steps, disk partitioning dialog, device manager, network adapter configuration, IP address configuration dialog, command prompt showing ipconfig/ping/tracert output. These visual guides help trainees follow along during hands-on sessions.",
        "priority": "medium",
        "acceptanceCriteria": [
            "At least 5 procedure screenshots for L3 exercises",
            "Screenshots are annotated with step numbers or arrows where needed",
            "Saved in content/IT-020-3/images/procedures/",
            "Referenced in the Practical Exercises sections of relevant CoCu files"
        ],
        "dependencies": [f"US-{max_id+1:03d}"],
        "passes": False,
        "filesTouch": [
            "content/IT-020-3/01_CoCu-1-Computer-System-Set-up.md",
            "content/IT-020-3/04_CoCu-4-Server-Installation.md",
            "content/IT-020-3/06_CoCu-6-Computer-Network-Connectivity-Set-up.md"
        ],
        "estimatedComplexity": "large",
        "tags": ["images", "screenshots", "l3", "procedures"],
        "epicId": "E-1",
    },
]

d["userStories"].extend(new_stories)
prd_path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

passed = sum(1 for s in d["userStories"] if s.get("passes"))
total = len(d["userStories"])
print(f"Added {len(new_stories)} image stories (US-{max_id+1:03d} to US-{max_id+6:03d})")
print(f"Total: {passed}/{total} ({100*passed//total}%)")
