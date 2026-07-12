#!/usr/bin/env python3
"""Deterministic structural checks for the Ideakit skill family."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILLS = {
    "discover": ROOT / "ideakit-discover/SKILL.md",
    "generate": ROOT / "ideakit-generate/SKILL.md",
    "explore": ROOT / "ideakit-explore/SKILL.md",
    "validate": ROOT / "ideakit-validate/SKILL.md",
    "name": ROOT / "ideakit-name/SKILL.md",
    "present": ROOT / "ideakit-present/SKILL.md",
}


def require(text: str, terms: list[str], label: str, failures: list[str]) -> None:
    lowered = text.lower()
    for term in terms:
        if term.lower() not in lowered:
            failures.append(f"{label}: missing contract term {term!r}")


def forbid(text: str, patterns: list[str], label: str, failures: list[str]) -> None:
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE | re.DOTALL):
            failures.append(f"{label}: forbidden pattern matched {pattern!r}")


def main() -> int:
    failures: list[str] = []
    texts: dict[str, str] = {}

    for name, path in SKILLS.items():
        if not path.exists():
            failures.append(f"{name}: missing {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        texts[name] = text
        if len(text.splitlines()) >= 500:
            failures.append(f"{name}: SKILL.md must stay below 500 lines")
        if text.count("```") % 2:
            failures.append(f"{name}: unbalanced fenced code blocks")
        if not re.match(r"^---\nname: ideakit-[a-z-]+\ndescription:", text):
            failures.append(f"{name}: malformed or unexpected frontmatter")
        for raw_ref in re.findall(r"`((?:\.\./|references/)[^`\n]+\.md)`", text):
            target = (path.parent / raw_ref).resolve()
            if not target.exists():
                failures.append(f"{name}: broken local reference {raw_ref!r}")

    require(texts.get("discover", ""), ["provisional", "contrarian", "desired game", "none of these", "contradictions", "minimum viable edge map", "3–5 useful questions"], "discover", failures)
    require(texts.get("generate", ""), ["observed", "inferred", "bet", "opportunity theses", "venture architectures", "affordable loss", "do not sort by one total score", "causal consequence map", "query-escape", "opportunity landscape", "source consequence", "causal ring"], "generate", failures)
    require(texts.get("generate", ""), ["breakthrough mode by default", "standard mode only", "opt-out", "references/breakthrough-mode.md"], "generate breakthrough routing", failures)
    require(texts.get("explore", ""), ["known", "inferred", "imagined", "maturity", "venture architecture", "counter-case", "source consequence", "causal ring"], "explore", failures)
    require(texts.get("validate", ""), ["maturity gate", "selected", "go / reframe / park / kill", "do not insert generic claude/chatgpt/mcp/quantum tables", "evidence level", "e0 thesis", "e4 repeatability"], "validate", failures)
    require(texts.get("name", ""), ["random simple noun", "negative baseline", "contextually", "unregistered at", "provisional shortlist", "handle appears unused"], "name", failures)
    require(texts.get("present", ""), ["fact", "inference", "ambition", "no startup theater", "decision-response check", "never use fomo"], "present", failures)

    forbid(texts.get("generate", ""), [r"score every idea.*six dimensions", r"spread gate.*do not proceed", r"use \*\*standard mode\*\* for an ordinary opportunity search"], "generate", failures)
    forbid(texts.get("validate", ""), [r"platform replication risk.*mandatory", r"future trajectory.*mandatory"], "validate", failures)
    forbid(texts.get("name", ""), [r"first ~?10.?15 names.*discard", r"throw it away"], "name", failures)

    craft = (ROOT / "ideakit-craft.md").read_text(encoding="utf-8")
    require(craft, ["reasoning integrity", "venture originality", "editorial anti-slop", "never invent", "force/event brief", "institutional/economic/cultural rearrangement"], "craft", failures)

    breakthrough_path = ROOT / "ideakit-generate/references/breakthrough-mode.md"
    breakthrough = ""
    if not breakthrough_path.exists():
        failures.append("generate breakthrough routing: missing references/breakthrough-mode.md")
    else:
        breakthrough = breakthrough_path.read_text(encoding="utf-8")
    require(
        texts.get("generate", "") + "\n" + breakthrough,
        [
            "independent invention",
            "obvious baseline",
            "revelation",
            "why others miss it",
            "solo entry",
            "value capture",
            "venture-family",
            "paid commitment",
            "delivered value",
            "killer risk",
        ],
        "generate breakthrough contract",
        failures,
    )

    cases = json.loads((ROOT / "evals/ideakit/cases.json").read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "evals/ideakit/pairwise-rubric.json").read_text(encoding="utf-8"))
    expected = {f"ideakit-{name}" for name in SKILLS}
    covered = {case["expected_skill"] for case in cases}
    if expected - covered:
        failures.append(f"cases: missing routing coverage for {sorted(expected - covered)}")
    default_generate_cases = [case for case in cases if case.get("id") == "domain-opportunities"]
    if len(default_generate_cases) != 1 or "breakthrough by default" not in default_generate_cases[0].get("quality_focus", []):
        failures.append("cases: domain-opportunities must exercise default breakthrough generation")
    breakthrough_cases = [case for case in cases if case.get("id") == "breakthrough-retry"]
    if len(breakthrough_cases) != 1 or breakthrough_cases[0].get("expected_skill") != "ideakit-generate":
        failures.append("cases: expected one breakthrough-retry route to ideakit-generate")
    elif not {
        "revelation surprise",
        "inevitable in hindsight",
        "solo entry",
        "value capture",
        "paid commitment",
        "delivered value",
        "killer risk",
        "venture-family merge",
        "cliche and duplicate collision",
    }.issubset(set(breakthrough_cases[0].get("quality_focus", []))):
        failures.append("cases: breakthrough-retry is missing quality-focus contracts")
    if len(rubric.get("dimensions", [])) < 12 or not rubric.get("hard_failures"):
        failures.append("pairwise rubric: expected at least 12 dimensions and explicit hard failures")
    rubric_dimensions = {item.get("name") for item in rubric.get("dimensions", [])}
    required_breakthrough_dimensions = {
        "revelation_surprise",
        "inevitable_in_hindsight",
        "solo_enterability",
        "value_capture",
        "collision_resistance",
    }
    if not required_breakthrough_dimensions.issubset(rubric_dimensions):
        failures.append(
            "pairwise rubric: missing breakthrough dimensions "
            f"{sorted(required_breakthrough_dimensions - rubric_dimensions)}"
        )
    if set(rubric.get("mode_dimensions", {})) != set(SKILLS):
        failures.append("pairwise rubric: expected mode-specific dimensions for every skill")

    required_fixtures = {
        "contract-pass-breakthrough-generate.md",
        "contract-fail-breakthrough-generic.md",
    }
    fixture_names = {path.name for path in (ROOT / "evals/ideakit/fixtures").glob("*.md")}
    if required_fixtures - fixture_names:
        failures.append(f"fixtures: missing {sorted(required_fixtures - fixture_names)}")

    if failures:
        print(json.dumps({"passed": False, "failures": failures}, indent=2))
        return 1
    print(json.dumps({"passed": True, "skills": len(SKILLS), "routing_case_coverage": len(cases), "routing_predictions_tested": 0, "rubric_dimensions": len(rubric["dimensions"]), "mode_rubrics": len(rubric["mode_dimensions"]), "failures": []}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
