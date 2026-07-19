#!/usr/bin/env python3
"""Deterministic structural + section checks for the Solo skill family."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from skill_checks import check_readme_mentions, check_skill_file  # noqa: E402


ROOT = Path(__file__).resolve().parents[2]
SKILLS = {
    "model": ROOT / "solo-model/SKILL.md",
    "fund": ROOT / "solo-fund/SKILL.md",
    "distribute": ROOT / "solo-distribute/SKILL.md",
    "sell": ROOT / "solo-sell/SKILL.md",
    "grow": ROOT / "solo-grow/SKILL.md",
    "sustain": ROOT / "solo-sustain/SKILL.md",
    "operate": ROOT / "solo-operate/SKILL.md",
}

REQUIRED_TERMS = {
    "model": ["evidence level", "first-revenue", "kill criteria"],
    "fund": ["lowest rung", "verify current terms", "solo-craft.md"],
    "distribute": ["one channel", "Mom Test", "willingness to pay"],
    "sell": ["commitment", "E2", "Mom Test", "solo-operate"],
    "grow": ["retention before acquisition", "payback"],
    "sustain": ["burnout", "single point of failure"],
    "operate": [
        "merchant of record",
        "PDPA",
        "dunning",
        "monthly",
        "exit interview",
        "not legal, tax, or financial advice",
    ],
}

# Sections whose loss would silently remove a stage's real work.
REQUIRED_HEADINGS = {
    "model": ["where this sits", "workflow", "intake", "execution"],
    "fund": ["where this sits", "workflow", "execution"],
    "distribute": ["where this sits", "workflow", "execution"],
    "sell": ["where this sits", "workflow", "execution"],
    "grow": ["where this sits", "workflow", "execution"],
    "sustain": ["where this sits", "workflow", "execution"],
    "operate": ["where this sits", "workflow", "duty 1", "duty 3", "duty 5", "execution"],
}


def main() -> int:
    failures: list[str] = []
    for name, path in SKILLS.items():
        check_skill_file(
            label=name,
            path=path,
            root=ROOT,
            prefix="solo-",
            required_terms=REQUIRED_TERMS[name],
            required_headings=REQUIRED_HEADINGS[name],
            failures=failures,
            extra_required_refs=["../solo-grounding.md"],
        )

    check_readme_mentions(ROOT / "solo-README.md", [f"solo-{n}" for n in SKILLS], failures)
    check_readme_mentions(ROOT / "README.md", [f"solo-{n}" for n in SKILLS], failures)

    # The shared grounding contract must name every skill it governs.
    grounding = ROOT / "solo-grounding.md"
    if not grounding.exists():
        failures.append("solo-grounding.md: missing")
    else:
        text = grounding.read_text(encoding="utf-8")
        for name in SKILLS:
            if f"solo-{name}" not in text:
                failures.append(f"solo-grounding.md: does not cover solo-{name}")

    if failures:
        print(json.dumps({"passed": False, "failures": failures}, indent=2, ensure_ascii=False))
        return 1
    print(json.dumps({"passed": True, "skills": len(SKILLS), "failures": []}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
