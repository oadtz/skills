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
    require(texts.get("generate", ""), ["single generation path", "no-subagent fallback", "references/invention-procedure.md", "fetch, don't snippet", "market's own language"], "generate single-path contract", failures)
    require(texts.get("explore", ""), ["known", "inferred", "imagined", "maturity", "venture architecture", "counter-case", "source consequence", "causal ring"], "explore", failures)
    require(texts.get("validate", ""), ["maturity gate", "selected", "go / reframe / park / kill", "do not insert generic claude/chatgpt/mcp/quantum tables", "evidence level", "e0 thesis", "e4 repeatability"], "validate", failures)
    require(texts.get("name", ""), ["random simple noun", "negative baseline", "contextually", "unregistered at", "provisional shortlist", "handle appears unused"], "name", failures)
    require(texts.get("present", ""), ["fact", "inference", "ambition", "no startup theater", "decision-response check", "never use fomo"], "present", failures)

    forbid(texts.get("generate", ""), [r"score every idea.*six dimensions", r"spread gate.*do not proceed", r"standard mode", r"invention intensity", r"breakthrough mode"], "generate", failures)
    forbid(texts.get("validate", ""), [r"platform replication risk.*mandatory", r"future trajectory.*mandatory"], "validate", failures)
    forbid(texts.get("name", ""), [r"first ~?10.?15 names.*discard", r"throw it away"], "name", failures)

    craft = (ROOT / "ideakit-craft.md").read_text(encoding="utf-8")
    require(craft, ["reasoning integrity", "venture originality", "editorial anti-slop", "never invent", "force/event brief", "institutional/economic/cultural rearrangement"], "craft", failures)

    procedure_path = ROOT / "ideakit-generate/references/invention-procedure.md"
    procedure = ""
    if not procedure_path.exists():
        failures.append("generate single-path contract: missing references/invention-procedure.md")
    else:
        procedure = procedure_path.read_text(encoding="utf-8")
    require(
        procedure,
        ["no-subagent fallback", "neutral", "packet-steering", "obvious baseline"],
        "generate invention procedure",
        failures,
    )
    require(
        texts.get("generate", "") + "\n" + procedure,
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

    # Lanes must diverge in evidence, not only in prompt: a shared frozen pack produces correlated
    # output however well the contexts are isolated.
    require(
        texts.get("generate", "") + "\n" + procedure,
        ["retrieval mandate", "per-lane", "shared floor", "exclusion set"],
        "generate lane retrieval contract",
        failures,
    )
    # The user reacts to openings before invention, and owns the ordering of forecasting gates.
    require(
        texts.get("generate", ""),
        ["put the openings in front of the user", "the ordering is theirs", "model-made and unconfirmed"],
        "generate human-in-the-loop contract",
        failures,
    )
    # Generate-once-then-select leaves the best reachable concept unbuilt; the loop only sharpens
    # checkable ground, never appeal.
    require(
        texts.get("generate", "") + "\n" + procedure,
        ["compare-and-evolve", "beat its parent", "meta-review", "checkable ground"],
        "generate evolution contract",
        failures,
    )
    watering_path = ROOT / "ideakit-generate/references/watering-holes.md"
    watering = watering_path.read_text(encoding="utf-8") if watering_path.exists() else ""
    if not watering:
        failures.append("generate watering-hole research: missing references/watering-holes.md")
    require(
        watering,
        ["verbatim", "unprompted", "i ended up just", "no watering hole is itself a finding", "blind spot"],
        "generate watering-hole research",
        failures,
    )
    require(texts.get("generate", ""), ["references/watering-holes.md"], "generate watering-hole routing", failures)

    scoring_path = ROOT / "ideakit-generate/references/scoring.md"
    scoring = scoring_path.read_text(encoding="utf-8") if scoring_path.exists() else ""
    if not scoring:
        failures.append("generate judgment split: missing references/scoring.md")
    require(scoring, ["who judges which gate", "the user ranks these"], "generate judgment split", failures)

    memory_path = ROOT / "ideakit-memory.md"
    memory = memory_path.read_text(encoding="utf-8") if memory_path.exists() else ""
    if not memory:
        failures.append("idea memory: missing ideakit-memory.md")
    require(
        memory,
        ["already-proposed families", "record what actually happened", "outcome yyyy-mm-dd", "never infer an outcome"],
        "idea memory outcome contract",
        failures,
    )

    ai_engineering_path = ROOT / "ideakit-generate/references/ai-engineering-team.md"
    ai_engineering = ""
    if not ai_engineering_path.exists():
        failures.append("generate AI engineering team routing: missing references/ai-engineering-team.md")
    else:
        ai_engineering = ai_engineering_path.read_text(encoding="utf-8")
    require(
        texts.get("generate", "") + "\n" + procedure + "\n" + ai_engineering,
        [
            "one founder directing an AI engineering team",
            "product does **not** need to be AI-native",
            "no model or agent at runtime",
            "product AI dependency",
            "engineering cost curve",
            "organizational-compression",
            "founder control surface",
            "delegation architecture",
            "verification loop",
            "AI engineering work absorbed",
            "scope made feasible",
            "human attention budget",
            "external bottleneck",
            "failure containment",
            "founder-directed entry",
            "do not cap product scope",
        ],
        "generate AI engineering team contract",
        failures,
    )

    cases = json.loads((ROOT / "evals/ideakit/cases.json").read_text(encoding="utf-8"))
    rubric = json.loads((ROOT / "evals/ideakit/pairwise-rubric.json").read_text(encoding="utf-8"))
    expected = {f"ideakit-{name}" for name in SKILLS}
    covered = {case["expected_skill"] for case in cases}
    if expected - covered:
        failures.append(f"cases: missing routing coverage for {sorted(expected - covered)}")
    default_generate_cases = [case for case in cases if case.get("id") == "domain-opportunities"]
    if len(default_generate_cases) != 1 or "single-path invention" not in default_generate_cases[0].get("quality_focus", []):
        failures.append("cases: domain-opportunities must exercise the single generation path")
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
    ai_engineering_cases = [case for case in cases if case.get("id") == "ai-engineering-default"]
    if len(ai_engineering_cases) != 1 or ai_engineering_cases[0].get("expected_skill") != "ideakit-generate":
        failures.append("cases: expected one ai-engineering-default route to ideakit-generate")
    elif not {
        "engineering cost-curve reconstruction",
        "organizational compression",
        "founder-directed entry",
        "directability",
        "verification loop",
        "human attention budget",
        "failure containment",
        "external bottleneck",
        "no human-labor ceiling",
        "product need not be AI-native",
    }.issubset(set(ai_engineering_cases[0].get("quality_focus", []))):
        failures.append("cases: ai-engineering-default is missing quality-focus contracts")
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
    required_ai_engineering_dimensions = {
        "engineering_cost_curve_reconstruction",
        "founder_directability",
        "verification_and_operational_control",
    }
    if not required_ai_engineering_dimensions.issubset(rubric_dimensions):
        failures.append(
            "pairwise rubric: missing AI engineering team dimensions "
            f"{sorted(required_ai_engineering_dimensions - rubric_dimensions)}"
        )
    required_judging_dimensions = {
        "retrieval_divergence",
        "evidence_scaling",
        "user_signal_and_ownership",
        "verbatim_customer_language",
        "evolution_evidence",
    }
    if not required_judging_dimensions.issubset(rubric_dimensions):
        failures.append(
            "pairwise rubric: missing judging-integrity dimensions "
            f"{sorted(required_judging_dimensions - rubric_dimensions)}"
        )
    required_protocol = {"both_orderings", "judge_independence", "length_normalization", "who_decides"}
    if not required_protocol.issubset(set(rubric.get("protocol", {}))):
        failures.append(
            "pairwise rubric: missing judging protocol keys "
            f"{sorted(required_protocol - set(rubric.get('protocol', {})))}"
        )
    if set(rubric.get("mode_dimensions", {})) != set(SKILLS):
        failures.append("pairwise rubric: expected mode-specific dimensions for every skill")

    required_fixtures = {
        "contract-pass-breakthrough-generate.md",
        "contract-fail-breakthrough-generic.md",
        "contract-pass-ai-engineering-team.md",
        "contract-fail-ai-engineering-human-ceiling.md",
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
