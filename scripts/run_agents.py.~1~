"""
Multi-Agent NOSS Reviewer — Runs 7 agent personas in parallel to review content.
Each agent reviews from their professional perspective and produces structured feedback.

Usage: uv run --with requests scripts/run_agents.py [--file <path>] [--level 3|4|5|all]
"""

import json
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

PROJECT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_DIR / "content"
PROMPTS_DIR = PROJECT_DIR / "scripts" / "agent_prompts"
LOG_DIR = PROJECT_DIR / "logs"

AGENT_ROLES = [
    "assessor",
    "trainer",
    "trainee",
    "internal_verifier",
    "external_verifier",
    "domain_expert",
    "government_officer",
]

# Delegation CLIs in priority order (cheapest/fastest first)
DELEGATION_CLIS = [
    {"name": "qwen", "cmd": "qwen", "timeout": 30},
    {"name": "gemini", "cmd": "gemini", "timeout": 60},
]


def load_agent_prompt(role):
    """Load the system prompt for an agent role."""
    prompt_file = PROMPTS_DIR / f"{role}.md"
    if prompt_file.exists():
        return prompt_file.read_text(encoding="utf-8")
    return f"You are a NOSS {role}. Review the content for quality and compliance."


def build_review_prompt(role, system_prompt, file_content, file_name):
    """Build the full prompt for an agent review."""
    return f"""{system_prompt}

---

## File to Review: {file_name}

```markdown
{file_content[:8000]}
```

Review this NOSS CoCu file from your perspective as a {role.replace('_', ' ')}.
Return your review as JSON with these fields:
- file: the filename
- role: your role name
- score: 0-100
- issues: list of issues found
- suggestions: list of improvement suggestions
- auto_fixes: list of objects with "line", "replacement", "reason"

Return ONLY the JSON, no other text."""


def run_agent_review(role, file_path):
    """Run a single agent review using available delegation CLI."""
    system_prompt = load_agent_prompt(role)
    file_content = file_path.read_text(encoding="utf-8")
    prompt = build_review_prompt(role, system_prompt, file_content, file_path.name)

    # Try each delegation CLI
    for cli in DELEGATION_CLIS:
        try:
            result = subprocess.run(
                [cli["cmd"], prompt],
                capture_output=True,
                text=True,
                timeout=cli["timeout"],
                cwd=str(PROJECT_DIR),
            )
            if result.returncode == 0 and result.stdout.strip():
                output = result.stdout.strip()
                # Try to parse JSON from output
                try:
                    # Find JSON in output
                    json_match = output
                    if "```json" in output:
                        json_match = output.split("```json")[1].split("```")[0]
                    elif "```" in output:
                        json_match = output.split("```")[1].split("```")[0]
                    elif "{" in output:
                        start = output.index("{")
                        end = output.rindex("}") + 1
                        json_match = output[start:end]

                    review = json.loads(json_match)
                    review["cli_used"] = cli["name"]
                    return review
                except (json.JSONDecodeError, ValueError):
                    # Return raw output as a review
                    return {
                        "file": file_path.name,
                        "role": role,
                        "score": 50,
                        "issues": [f"Could not parse structured review from {cli['name']}"],
                        "suggestions": [output[:500]],
                        "auto_fixes": [],
                        "cli_used": cli["name"],
                        "raw_output": output[:1000],
                    }
        except (subprocess.TimeoutExpired, FileNotFoundError):
            continue

    # All CLIs failed — return a placeholder
    return {
        "file": file_path.name,
        "role": role,
        "score": 0,
        "issues": ["No delegation CLI available for review"],
        "suggestions": [],
        "auto_fixes": [],
        "cli_used": "none",
    }


def review_file(file_path, roles=None):
    """Run all agent reviews on a single file in parallel."""
    roles = roles or AGENT_ROLES
    reviews = []

    print(f"  Reviewing: {file_path.name} ({len(roles)} agents)")

    with ThreadPoolExecutor(max_workers=min(len(roles), 4)) as executor:
        futures = {
            executor.submit(run_agent_review, role, file_path): role
            for role in roles
        }
        for future in as_completed(futures):
            role = futures[future]
            try:
                review = future.result()
                reviews.append(review)
                score = review.get("score", 0)
                issues = len(review.get("issues", []))
                cli = review.get("cli_used", "?")
                print(f"    [{role}] Score: {score}, Issues: {issues} (via {cli})")
            except Exception as e:
                print(f"    [{role}] ERROR: {e}")
                reviews.append({
                    "file": file_path.name,
                    "role": role,
                    "score": 0,
                    "issues": [str(e)],
                    "suggestions": [],
                    "auto_fixes": [],
                    "error": True,
                })

    return reviews


def apply_auto_fixes(file_path, reviews):
    """Apply auto-fixes from agent reviews."""
    text = file_path.read_text(encoding="utf-8")
    fixes_applied = 0

    for review in reviews:
        for fix in review.get("auto_fixes", []):
            old = fix.get("line", "")
            new = fix.get("replacement", "")
            if old and new and old in text and old != new:
                text = text.replace(old, new, 1)
                fixes_applied += 1

    if fixes_applied > 0:
        file_path.write_text(text, encoding="utf-8")
        print(f"  Applied {fixes_applied} auto-fixes to {file_path.name}")

    return fixes_applied


def review_level(level_num):
    """Review all CoCu files for a level."""
    level_dir = CONTENT_DIR / f"IT-020-{level_num}"
    if not level_dir.exists():
        print(f"[SKIP] {level_dir} not found")
        return []

    cocu_files = sorted([
        f for f in level_dir.glob("*.md")
        if f.name[:2].isdigit() and "cocu" in f.name.lower()
    ])

    all_reviews = []
    for cocu_file in cocu_files:
        reviews = review_file(cocu_file)
        all_reviews.extend(reviews)

        # Apply auto-fixes
        apply_auto_fixes(cocu_file, reviews)

    return all_reviews


def main():
    """Main entry point."""
    level_arg = "all"
    target_file = None

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--level" and i + 1 < len(args):
            level_arg = args[i + 1]
            i += 2
        elif args[i] == "--file" and i + 1 < len(args):
            target_file = Path(args[i + 1])
            i += 2
        else:
            i += 1

    LOG_DIR.mkdir(parents=True, exist_ok=True)

    print("NOSS Multi-Agent Reviewer")
    print(f"Agents: {', '.join(AGENT_ROLES)}")
    print()

    all_reviews = []

    if target_file:
        # Review a single file
        if target_file.exists():
            reviews = review_file(target_file)
            all_reviews.extend(reviews)
            apply_auto_fixes(target_file, reviews)
        else:
            print(f"[ERROR] File not found: {target_file}")
            sys.exit(1)
    else:
        # Review by level
        levels = ["3", "4", "5"] if level_arg == "all" else [level_arg]
        for level in levels:
            print(f"[L{level}] Reviewing IT-020-{level}...")
            reviews = review_level(level)
            all_reviews.extend(reviews)
            print()

    # Save review report
    report = {
        "timestamp": datetime.now().isoformat(),
        "total_reviews": len(all_reviews),
        "reviews": all_reviews,
    }

    report_path = LOG_DIR / f"agent-reviews-{datetime.now().strftime('%Y-%m-%d-%H%M')}.json"
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    # Summary
    print("=" * 60)
    print("REVIEW SUMMARY")
    print("=" * 60)

    avg_scores = {}
    for review in all_reviews:
        role = review.get("role", "unknown")
        score = review.get("score", 0)
        if role not in avg_scores:
            avg_scores[role] = []
        avg_scores[role].append(score)

    for role, scores in sorted(avg_scores.items()):
        avg = sum(scores) / len(scores) if scores else 0
        print(f"  {role}: avg {avg:.0f}% ({len(scores)} reviews)")

    total_issues = sum(len(r.get("issues", [])) for r in all_reviews)
    total_fixes = sum(len(r.get("auto_fixes", [])) for r in all_reviews)
    print(f"\nTotal issues: {total_issues}")
    print(f"Total auto-fixes available: {total_fixes}")
    print(f"Report: {report_path}")


if __name__ == "__main__":
    main()
