"""Add new enhancement stories to prd.json."""
import json
from pathlib import Path

prd_path = Path("C:/Users/Jyue/Documents/1-projects/NOSS/prd.json")
d = json.loads(prd_path.read_text(encoding="utf-8"))
max_id = max(int(s["id"].split("-")[1]) for s in d["userStories"])

new_stories = [
    {
        "id": f"US-{max_id+1:03d}",
        "title": "Add practical exercise worksheets to each L3 CoCu",
        "description": "Each L3 CoCu needs a ## Practical Exercises section with 2-3 hands-on lab exercises per work activity. Include: objective, required equipment, step-by-step instructions, expected outcome, assessment checklist.",
        "priority": "high",
        "acceptanceCriteria": [
            "All 7 L3 CoCu files have ## Practical Exercises section",
            "Each work activity has at least 1 hands-on exercise",
            "Exercises specify required equipment and expected outcomes",
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-3/01_CoCu-1-Computer-System-Set-up.md",
            "content/IT-020-3/02_CoCu-2-Computer-System-Maintenance.md",
            "content/IT-020-3/03_CoCu-3-Computer-System-Repair.md",
            "content/IT-020-3/04_CoCu-4-Server-Installation.md",
            "content/IT-020-3/05_CoCu-5-Server-Maintenance.md",
            "content/IT-020-3/06_CoCu-6-Computer-Network-Connectivity-Set-up.md",
            "content/IT-020-3/07_CoCu-7-Mobile-Device-Configuration.md",
        ],
        "estimatedComplexity": "large",
        "tags": ["exercises", "l3", "content-depth"],
        "epicId": "E-1",
    },
    {
        "id": f"US-{max_id+2:03d}",
        "title": "Add practical exercise worksheets to each L4 CoCu",
        "description": "Each L4 CoCu needs ## Practical Exercises with hands-on labs for administration level. Include network configuration labs, security audits, procurement scenarios.",
        "priority": "high",
        "acceptanceCriteria": [
            "All 6 L4 CoCu files have ## Practical Exercises section",
            "Exercises reflect L4 administrative competencies",
        ],
        "dependencies": [f"US-{max_id+1:03d}"],
        "passes": False,
        "filesTouch": [
            "content/IT-020-4/01_CoCu-1-Server-Configuration.md",
            "content/IT-020-4/02_CoCu-2-Computer-System-Security-Control.md",
            "content/IT-020-4/03_CoCu-3-System-Network-Procurement.md",
            "content/IT-020-4/04_CoCu-4-Network-Cabling-Management.md",
            "content/IT-020-4/05_CoCu-5-Computer-Network-Installation-Management.md",
            "content/IT-020-4/06_CoCu-6-Computer-System-Maintenance-Management.md",
        ],
        "estimatedComplexity": "large",
        "tags": ["exercises", "l4", "content-depth"],
        "epicId": "E-2",
    },
    {
        "id": f"US-{max_id+3:03d}",
        "title": "Add practical exercise worksheets to each L5 CoCu",
        "description": "Each L5 CoCu needs ## Practical Exercises with management-level exercises: case studies, scenario planning, policy drafting, budget estimation, risk assessment.",
        "priority": "high",
        "acceptanceCriteria": [
            "All 7 L5 CoCu files have ## Practical Exercises section",
            "Exercises include case studies and strategic scenarios",
        ],
        "dependencies": [f"US-{max_id+1:03d}"],
        "passes": False,
        "filesTouch": [
            "content/IT-020-5/01_CoCu-1-Management-Overview.md",
            "content/IT-020-5/02_CoCu-2-Computer-System-Asset-Management.md",
            "content/IT-020-5/03_CoCu-3-Computer-System-Security-Management.md",
            "content/IT-020-5/04_CoCu-4-Disaster-Recovery-Management.md",
            "content/IT-020-5/05_CoCu-5-Computer-System-Network-Project-Management.md",
            "content/IT-020-5/06_CoCu-6-SOP-Development-And-Implementation.md",
            "content/IT-020-5/07_CoCu-7-Server-Scripting.md",
        ],
        "estimatedComplexity": "large",
        "tags": ["exercises", "l5", "content-depth"],
        "epicId": "E-3",
    },
    {
        "id": f"US-{max_id+4:03d}",
        "title": "Add references and recommended reading to each CoCu",
        "description": "Each CoCu should have ## References listing: official NOSS references, relevant textbooks, online resources, industry standards (ISO, IEEE), and manufacturer documentation.",
        "priority": "medium",
        "acceptanceCriteria": [
            "All 20 CoCu files have ## References section",
            "References are specific to each CoCu topic",
            "Includes mix of official standards, textbooks, online resources",
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-3/01_CoCu-1-Computer-System-Set-up.md",
            "content/IT-020-4/01_CoCu-1-Server-Configuration.md",
            "content/IT-020-5/01_CoCu-1-Management-Overview.md",
        ],
        "estimatedComplexity": "large",
        "tags": ["references", "content-depth"],
        "epicId": "E-4",
    },
    {
        "id": f"US-{max_id+5:03d}",
        "title": "Add tools and equipment list appendix per level",
        "description": "Create consolidated ## Tools and Equipment List appendix in each contact hour file listing ALL tools, software, and equipment required across all CoCu units. Include quantities, specs, estimated costs.",
        "priority": "medium",
        "acceptanceCriteria": [
            "L3, L4, L5 contact hour files each have Tools and Equipment appendix",
            "Lists are consolidated from all CoCu units",
            "Includes specifications and quantities",
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-3/00_Contact-hour_IT-020-3-L3-Operation.md",
            "content/IT-020-4/00_Contact-hour_IT-020-4-L4-Administration.md",
            "content/IT-020-5/00_Contact-hour_IT-020-5-L5-Management.md",
        ],
        "estimatedComplexity": "medium",
        "tags": ["equipment", "appendix"],
        "epicId": "E-4",
    },
    {
        "id": f"US-{max_id+6:03d}",
        "title": "Update key terms with 2024-2025 technology references",
        "description": "Review and update all key terms/tools tables to reference current technology: Windows 11/Server 2025, DDR5, NVMe Gen5, Wi-Fi 7, USB4, AI-assisted tools. Remove outdated references.",
        "priority": "high",
        "acceptanceCriteria": [
            "All key terms tables reference current technology (2024-2025)",
            "No references to deprecated hardware/software",
            "Includes modern tools like AI-assisted diagnostics",
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-3/01_CoCu-1-Computer-System-Set-up.md",
            "content/IT-020-4/01_CoCu-1-Server-Configuration.md",
            "content/IT-020-5/01_CoCu-1-Management-Overview.md",
        ],
        "estimatedComplexity": "large",
        "tags": ["technology-update", "accuracy"],
        "epicId": "E-4",
    },
    {
        "id": f"US-{max_id+7:03d}",
        "title": "Add learning outcome matrices per CoCu",
        "description": "Each CoCu should have ## Learning Outcome Matrix table mapping: Work Activity -> Knowledge Outcome -> Performance Outcome -> Assessment Method -> Evidence Required. Key JPK requirement.",
        "priority": "critical",
        "acceptanceCriteria": [
            "All 20 CoCu files have ## Learning Outcome Matrix table",
            "Every work activity mapped to knowledge and performance outcomes",
            "Assessment methods and evidence types specified",
        ],
        "dependencies": [],
        "passes": False,
        "filesTouch": [
            "content/IT-020-3/01_CoCu-1-Computer-System-Set-up.md",
            "content/IT-020-4/01_CoCu-1-Server-Configuration.md",
            "content/IT-020-5/01_CoCu-1-Management-Overview.md",
        ],
        "estimatedComplexity": "large",
        "tags": ["learning-outcomes", "compliance", "jpk"],
        "epicId": "E-4",
    },
    {
        "id": f"US-{max_id+8:03d}",
        "title": "Update generate_docx.py to render new sections",
        "description": "Update generate_docx.py to properly render: Practical Exercises, References, Learning Outcome Matrix, Tools and Equipment appendix. Ensure proper formatting and page breaks.",
        "priority": "high",
        "acceptanceCriteria": [
            "All new sections render correctly in .docx output",
            "Proper page breaks between sections",
            "Tables are properly formatted",
        ],
        "dependencies": [f"US-{max_id+1:03d}", f"US-{max_id+4:03d}", f"US-{max_id+7:03d}"],
        "passes": False,
        "filesTouch": ["scripts/generate_docx.py"],
        "estimatedComplexity": "medium",
        "tags": ["generator", "formatting"],
        "epicId": "E-5",
    },
]

d["userStories"].extend(new_stories)
prd_path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

passed = sum(1 for s in d["userStories"] if s.get("passes"))
total = len(d["userStories"])
print(f"Added {len(new_stories)} new stories (US-{max_id+1:03d} to US-{max_id+8:03d})")
print(f"Total: {passed}/{total} passed ({100*passed//total}%)")
