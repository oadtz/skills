#!/usr/bin/env python3
"""Check that AI engineering is a shared default across the local skill families."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "ai-engineering-foundation.md"
PREFIXES = ("ideakit-", "solo-", "forge-")


def require(text: str, terms: list[str], label: str, failures: list[str]) -> None:
    lowered = text.lower()
    for term in terms:
        if term.lower() not in lowered:
            failures.append(f"{label}: missing {term!r}")


def main() -> int:
    failures: list[str] = []
    if not FOUNDATION.exists():
        failures.append("missing ai-engineering-foundation.md")
        foundation = ""
    else:
        foundation = FOUNDATION.read_text(encoding="utf-8")

    require(
        foundation,
        [
            "one founder can direct an AI engineering team",
            "AI-developed product",
            "AI-native product",
            "no model or agent at runtime",
            "founder direction + AI engineering capacity + verification + operational control",
            "Directability",
            "Verifiability",
            "Founder attention",
            "External bottlenecks",
            "Do not reject or shrink a product solely because one founder could not code it manually",
            "Do not require customer-facing or runtime AI",
        ],
        "foundation",
        failures,
    )

    skills = sorted(
        path
        for path in ROOT.glob("*/SKILL.md")
        if path.parent.name.startswith(PREFIXES)
    )
    if len(skills) != 16:
        failures.append(f"expected 16 Ideakit/Solo/Forge skills, found {len(skills)}")

    for path in skills:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if "`../ai-engineering-foundation.md`" not in text:
            failures.append(f"{rel}: does not read shared foundation")
        if len(text.splitlines()) >= 500:
            failures.append(f"{rel}: exceeds 499-line skill limit")

    combined = "\n".join(path.read_text(encoding="utf-8") for path in skills)
    forbidden = {
        "conditional mode": r"activate ai engineering team mode|ai engineering team mode when applicable",
        "human build minimization": r"pick the model that pays the soonest with the least to build",
        "missing-team ceiling": r"don['’]t model for a team you don['’]t have",
        "human-day packet ceiling": r"small \(≈?≤?2[–-]3 days",
        "automatic tiny surface": r"keep the product surface small \(every feature is forever-support\)",
    }
    for label, pattern in forbidden.items():
        if re.search(pattern, combined, re.IGNORECASE):
            failures.append(f"skillset: forbidden {label} pattern {pattern!r}")

    generate = (ROOT / "ideakit-generate/SKILL.md").read_text(encoding="utf-8")
    require(
        generate,
        [
            "Apply the default AI engineering model",
            "For every software or digital product brief",
            "Product AI dependency",
            "Founder control surface",
            "Human attention budget",
            "Scope made feasible",
        ],
        "ideakit-generate",
        failures,
    )

    solo_model = (ROOT / "solo-model/SKILL.md").read_text(encoding="utf-8")
    require(
        solo_model,
        [
            "directed AI engineering capacity",
            "founder-directed business",
            "Model for directed capacity you control",
        ],
        "solo-model",
        failures,
    )

    forge_build = (ROOT / "forge-build/SKILL.md").read_text(encoding="utf-8")
    require(
        forge_build,
        [
            "AI coding capabilities as an engineering team",
            "one bounded packet per agent",
            "Parallelism follows interfaces",
            "isolated worktrees",
        ],
        "forge-build",
        failures,
    )

    result = {
        "passed": not failures,
        "foundation": str(FOUNDATION.relative_to(ROOT)),
        "skills_checked": len(skills),
        "families": list(PREFIXES),
        "failures": failures,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
