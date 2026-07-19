#!/usr/bin/env python3
"""Deterministic structural + section checks for the Forge skill family."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from skill_checks import check_readme_mentions, check_skill_file  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
SKILLS = {
    "architect": ROOT / "forge-architect/SKILL.md",
    "design": ROOT / "forge-design/SKILL.md",
    "build": ROOT / "forge-build/SKILL.md",
    "ship": ROOT / "forge-ship/SKILL.md",
    "operate": ROOT / "forge-operate/SKILL.md",
}

REQUIRED_TERMS = {
    "architect": ["default boring", "ADR", "no feature code", "migration tooling", "escalation triggers"],
    "design": ["anti-slop", "design token", "re-theme"],
    "build": ["walking skeleton", "vertical slice", "reward hacking", "AFK", "permission level"],
    "ship": ["branch protection", "slopsquatting", "rollback", "review gate", "billing", "forge-operate"],
    "operate": ["expand–contract", "restore test", "smoke suite", "operations.md", "evidence level"],
}

# Sections whose loss would silently remove a stage's real work.
REQUIRED_HEADINGS = {
    "architect": ["where this sits", "workflow", "intake", "scaffold"],
    "design": ["where this sits", "workflow", "execution"],
    "build": ["where this sits", "workflow", "verify", "execution"],
    "ship": ["where this sits", "workflow", "quality gates", "security", "observability", "deploy"],
    "operate": ["where this sits", "workflow", "duty 1", "duty 3", "duty 4", "duty 6", "execution"],
}


def main() -> int:
    failures: list[str] = []
    for name, path in SKILLS.items():
        check_skill_file(
            label=name,
            path=path,
            root=ROOT,
            prefix="forge-",
            required_terms=REQUIRED_TERMS[name],
            required_headings=REQUIRED_HEADINGS[name],
            failures=failures,
        )

    check_readme_mentions(ROOT / "forge-README.md", [f"forge-{n}" for n in SKILLS], failures)
    check_readme_mentions(ROOT / "README.md", [f"forge-{n}" for n in SKILLS], failures)

    # Day-2 mechanics live in the playbook; assert the load-bearing ones survive edits.
    playbook = ROOT / "forge-operate/references/live-system-playbook.md"
    if not playbook.exists():
        failures.append("forge-operate: missing references/live-system-playbook.md")
    else:
        text = playbook.read_text(encoding="utf-8").lower()
        for term in ["lock_timeout", "concurrently", "expand–contract", "rollback", "restore"]:
            if term.lower() not in text:
                failures.append(f"forge-operate playbook: missing mechanic {term!r}")

    if failures:
        print(json.dumps({"passed": False, "failures": failures}, indent=2, ensure_ascii=False))
        return 1
    print(json.dumps({"passed": True, "skills": len(SKILLS), "failures": []}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
