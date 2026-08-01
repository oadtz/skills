#!/usr/bin/env python3
"""Heuristic scorer for temporary Ideakit artifacts; never treats them as factual truth."""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path


SLOP = [
    "unlock", "unleash", "empower", "elevate", "seamless", "game-changing",
    "revolutionize", "in today's fast-paced world", "ปลดล็อกศักยภาพ",
    "ยกระดับอย่างไร้รอยต่อ", "ครบ จบ ในที่เดียว",
]

MODE_MARKERS = {
    "discover": {
        "behavioral_evidence": [r"behavioral trail|past behavior|actually (did|spent|built)", r"energy|lights you up|drains"],
        "provisional_identity": [r"provisional", r"contradiction"],
        "decision_frame": [r"desired game", r"affordable loss|risk & resources|risk and resources"],
        "recognition": [r"reaction|react[- ]to[- ]concretes|attraction|recoil", r"none of these|what is missing|combine"],
        "handoff": [r"candidate playing fields", r"wrong if|riskiest hypotheses"],
    },
    "generate": {
        "epistemic_chain": [r"observed", r"inferred", r"\bbet\b"],
        "venture_mechanics": [r"wedge", r"first[- ]?10|first (users|customers)", r"distribution", r"compound|power"],
        "entrepreneurial_judgment": [r"counter[- ]?case|wrong if|disconfirm", r"affordable[- ]loss|cheapest.*test"],
    },
    "explore": {
        "epistemic_lanes": [r"known", r"inferred", r"imagined"],
        "alternatives": [r"architecture|reframe|alternative", r"counter[- ]?case|assumption"],
        "learning": [r"cheapest.*test|would change.*mind|critical uncertainty"],
    },
    "validate": {
        "decision": [r"go|reframe|park|kill", r"recommend"],
        "evidence": [r"observed", r"inferred", r"\bbet\b", r"source|evidence"],
        "execution": [r"wedge|pilot|v1", r"kill criteria|kill signal|reframe signal"],
        "evidence_level": [r"evidence level", r"\bE[0-4]\b", r"next costly signal|next commitment|next transaction"],
    },
    "name": {
        "brief": [r"audience", r"evoke|personality|point of view", r"\.com|tld|domain"],
        "centroid_escape": [r"baseline|centroid|generic", r"venture[- ]specific|point of view|category tension"],
        "screening": [r"rdap|whois", r"trademark|wipo|uspto|tmview", r"handle", r"collision"],
        "honest_status": [r"unregistered at|registered|premium|reserved|unknown", r"provisional|passed screening", r"screening.*legal clearance|not legal clearance"],
        "recommendation": [r"top pick|provisional lead|shortlist", r"watch[- ]outs|unresolved"],
    },
    "present": {
        "epistemics": [r"fact", r"inference", r"ambition"],
        "decision": [r"audience", r"ask|action", r"belief shift|decision"],
        "argument": [r"observation|evidence", r"consequence|stakes", r"mechanism|response"],
        "credibility": [r"uncertainty|reason not to|counter", r"source|evidence"],
    },
}

BREAKTHROUGH_MARKERS = {
    "revelation": [
        r"(?m)^\s*(?:[-*]\s*)?(?:\*\*|`)?revelation(?:\*\*|`)?\s*:\s*(?:\*\*|`)?",
        r"(?m)^\s*(?:[-*]\s*)?(?:\*\*|`)?why others miss it(?:\*\*|`)?\s*:\s*(?:\*\*|`)?",
    ],
    "solo_entry": [
        r"(?m)^\s*(?:[-*]\s*)?(?:\*\*|`)?solo entry(?:\*\*|`)?\s*:\s*(?:\*\*|`)?",
        r"paid|pilot|manual|founder hours|hours per week|affordable[- ]loss|cheapest.*test",
    ],
    "value_capture": [
        r"(?m)^\s*(?:[-*]\s*)?(?:\*\*|`)?value capture(?:\*\*|`)?\s*:\s*(?:\*\*|`)?",
        r"pay|price|fee|budget|revenue|margin|contribution|retainer|subscription",
    ],
    "paid_and_delivered": [
        r"(?m)^\s*(?:[-*]\s*)?(?:\*\*|`)?paid commitment(?:\*\*|`)?\s*:\s*(?:\*\*|`)?",
        r"(?m)^\s*(?:[-*]\s*)?(?:\*\*|`)?delivered value(?:\*\*|`)?\s*:\s*(?:\*\*|`)?",
    ],
    "killer_risk": [
        r"(?m)^\s*(?:[-*]\s*)?(?:\*\*|`)?killer (?:risk|objection)(?:\*\*|`)?\s*:\s*(?:\*\*|`)?",
        r"wrong if|disconfirm|kill signal|would fail|failure",
    ],
}

# Labels may appear as inline lines ("Label: ...") or as rows of the control-plane appendix
# table ("| Label | ... |"), which is the preferred format.
def _label(name: str) -> str:
    return r"(?m)^\s*\|?\s*(?:[-*]\s*)?(?:\*\*|`)?" + name + r"(?:\*\*|`)?\s*[:|]\s*(?:\*\*|`)?"


AI_ENGINEERING_TEAM_MARKERS = {
    "engineering_capacity": [
        _label("ai engineering work absorbed"),
        _label("product ai dependency"),
        _label("previously required organization"),
    ],
    "founder_control": [
        _label("founder control surface"),
        _label("delegation architecture"),
    ],
    "verification": [
        _label("verification loop"),
        r"test|eval|review|observability|rollback",
    ],
    "attention_and_bottleneck": [
        _label("human attention budget"),
        _label("external bottleneck"),
    ],
    "containment_and_expansion": [
        _label("failure containment"),
        _label("scope made feasible"),
    ],
    "founder_directed_entry": [
        _label("founder[- ]directed entry"),
        r"external|control[- ]plane|right[- ]to[- ]build|paid|commitment|proof",
    ],
}

HUMAN_LABOR_CEILING_PATTERNS = [
    r"because (?:you|the founder) (?:are|is) solo[^.\n]*(?:one feature|tiny|micro[- ]saas|manual service)",
    r"(?:must|should) (?:only )?build what (?:you|one person|the founder) can code",
    r"(?:limit|reduce|shrink)[^.\n]*(?:to|into) (?:one feature|a tiny app|a micro[- ]saas|a manual service)[^.\n]*(?:weekend|after work|solo founder|one person)",
]

# These catch only explicit generic shells. They are not a novelty metric; a semantically
# derivative idea can easily avoid the phrases, and a strong idea can still use a category noun.
GENERIC_BREAKTHROUGH_PATTERNS = [
    r"\bAI[- ]powered\s+(?:platform|marketplace|dashboard|assistant|app|solution)\b",
    r"\b(?:all[- ]in[- ]one|one[- ]stop)\s+(?:platform|solution|app)\b",
    r"\b(?:uber|airbnb|tinder)\s+for\s+[a-z0-9-]+",
]


def group_passes(text: str, patterns: list[str]) -> bool:
    return all(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=sorted(MODE_MARKERS))
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--force", action="store_true", help="Apply force-brief causal-depth gates")
    parser.add_argument("--breakthrough", action="store_true", help="Apply breakthrough-output contract gates")
    parser.add_argument("--ai-engineering-foundation", action="store_true", help="Apply the default one-founder-directed AI engineering gates for software")
    args = parser.parse_args()

    if args.breakthrough and args.mode != "generate":
        parser.error("--breakthrough is only valid for generate artifacts")
    if args.ai_engineering_foundation and args.mode != "generate":
        parser.error("--ai-engineering-foundation is only valid for generate artifacts")

    text = args.artifact.read_text(encoding="utf-8")
    groups = {name: group_passes(text, patterns) for name, patterns in MODE_MARKERS[args.mode].items()}
    if args.breakthrough:
        groups.update({name: group_passes(text, patterns) for name, patterns in BREAKTHROUGH_MARKERS.items()})
    if args.ai_engineering_foundation:
        groups.update({name: group_passes(text, patterns) for name, patterns in AI_ENGINEERING_TEAM_MARKERS.items()})
    if args.force:
        groups.update({
            "causal_map": group_passes(text, [r"ring 1|1 direct", r"ring 2|2 behavioral", r"ring 3|3 structural"]),
            "causal_provenance": group_passes(text, [r"source consequence", r"causal ring", r"domain", r"time horizon|horizon"]),
            "query_escape": group_passes(text, [r"query[- ]escape|without (?:the )?force (?:word|vocabulary)|independent domain language"]),
        })
    # Editorial checks should inspect prose, not citation destinations. A source URL may
    # legitimately contain terms such as "unlocking" without the author using generator dialect.
    editorial_text = re.sub(r"\]\(https?://[^)]+\)", "]", text)
    slop_hits = [term for term in SLOP if term.lower() in editorial_text.lower()]
    generic_wrapper_hits = []
    if args.breakthrough:
        generic_wrapper_hits = [
            match.group(0)
            for pattern in GENERIC_BREAKTHROUGH_PATTERNS
            if (match := re.search(pattern, editorial_text, re.IGNORECASE))
        ]
    unsupported_precision = len(re.findall(r"\b\d+(?:\.\d+)?%\b|\b\d{2,}\+? (?:users|customers|complaints|people)\b", text, re.IGNORECASE))
    # Count distinct real registrable domains, whether markdown-linked or bare. Placeholder hosts
    # (example.com, .invalid, localhost) must not satisfy the evidence floor.
    PLACEHOLDER_HOSTS = re.compile(
        r"^(?:localhost|(?:www\.)?example\.(?:com|org|net)|.*\.(?:invalid|test|local|example))$",
        re.IGNORECASE,
    )
    hosts = set()
    for url in re.findall(r"https?://([^\s/)\"'>\]]+)", text):
        host = url.split("@")[-1].split(":")[0].lower()
        if not PLACEHOLDER_HOSTS.match(host):
            hosts.add(host)
    cited_links = len(hosts)
    labeled_observations = len(re.findall(r"\bObserved\b", text, re.IGNORECASE))

    structural = sum(groups.values()) / max(len(groups), 1) * 70
    editorial = max(0, 20 - 5 * len(slop_hits))
    integrity = 10
    warnings: list[str] = []
    if unsupported_precision and cited_links < labeled_observations:
        integrity = 0
        warnings.append("precise claims may lack nearby source coverage; inspect manually")
    if not labeled_observations and args.mode in {"generate", "validate"}:
        integrity = 0
        warnings.append("no Observed labels found")
    # Evidence must scale with the claim surface. An artifact that grows without gaining sources is
    # the shape LLM judges systematically over-reward (length bias), so the floor rises with length
    # instead of being a fixed count.
    word_count = len(text.split())
    # A run with no research capability is a legitimate labelled mode, not a thin artifact. It is
    # exempt only while it stays honest: every external claim marked, and no precise figures asserted.
    declared_speculative = bool(
        re.search(r"speculative workshop|no live research|research (?:was )?unavailable", text, re.IGNORECASE)
        and re.search(r"needs current evidence", text, re.IGNORECASE)
        and not unsupported_precision
    )
    if args.mode in {"generate", "validate"} and not declared_speculative:
        expected_hosts = min(6, max(1, math.ceil(word_count / 450)))
        if cited_links < expected_hosts:
            warnings.append(
                f"evidence does not scale with length: {word_count} words rest on {cited_links} distinct "
                f"fetched sources (expected at least {expected_hosts}) — added length without added "
                "evidence is the failure shape automated judges reward and reality does not"
            )
    if generic_wrapper_hits:
        warnings.append(
            "breakthrough artifact uses an obvious generic wrapper phrase; inspect the canonical idea core "
            "and collision set manually"
        )
    if args.breakthrough and cited_links < 3:
        warnings.append(
            "portfolio has fewer than 3 fetched citations; complete labels over a thin evidence base "
            "indicate form-filling — verify the evidence layer manually"
        )
    if args.mode == "generate":
        # Gate zero: what does the target do today, and at what price? The competitor that kills a
        # solo venture is usually free and informal, and leaves no trace in search results.
        if not re.search(
            r"substitute|do(?:es)? today|already (?:do|does|solve|handle|cover)|free (?:alternative|version|substitute|option)"
            r"|status quo|informal|ทดแทน|ทำเองอยู่แล้ว",
            text,
            re.IGNORECASE,
        ):
            warnings.append(
                "no substitute test found: the artifact never states what the target does today or at "
                "what price, so free, informal, family, volunteer, or state-provided competitors are unexamined"
            )
        # Prior art must be reasoned about, not merely detected. A run that kills candidates because a
        # competitor exists, without naming who that competitor fails, is applying the wrong rule.
        mentions_prior_art = re.search(
            r"prior art|incumbent|existing (?:player|operator|offering|solution)|competitor|already (?:exists|operating)",
            text, re.IGNORECASE,
        )
        reasons_about_it = re.search(
            r"fails? to serve|does not serve|cannot (?:serve|follow|fix|match)|structurally (?:cannot|can't)"
            r"|underserved|cannibalis|cannibaliz|10x|10×|why (?:they|it) can(?:not|'t)",
            text, re.IGNORECASE,
        )
        if mentions_prior_art and not reasons_about_it:
            warnings.append(
                "prior art is named but not reasoned about: state which segment the incumbent structurally "
                "fails and why it cannot fix that, rather than treating existence as a kill signal"
            )
        # Template theater: many labeled lines over few fetched sources is the highest-fidelity slop
        # this family produces, because it satisfies every structural marker check above.
        label_lines = len(re.findall(
            r"(?mi)^\s*\|?\s*(?:[-*]\s*)?(?:\*\*|`)?"
            r"(?:revelation|why others miss it|solo entry|value capture|paid commitment|delivered value"
            r"|killer risk|source consequence|causal ring|time horizon)"
            r"(?:\*\*|`)?\s*[:|]", text))
        if label_lines >= 6 and cited_links < label_lines / 3:
            warnings.append(
                f"template theater risk: {label_lines} labeled lines against {cited_links} distinct fetched "
                "sources — labels are a floor for information, not a substitute for evidence or legibility"
            )
    if args.ai_engineering_foundation:
        human_labor_ceiling_hits = [
            match.group(0)
            for pattern in HUMAN_LABOR_CEILING_PATTERNS
            if (match := re.search(pattern, editorial_text, re.IGNORECASE))
        ]
        if human_labor_ceiling_hits:
            warnings.append(
                "software artifact violates the default AI engineering foundation with a human implementation-hours ceiling: "
                + "; ".join(human_labor_ceiling_hits)
            )
    if args.mode == "validate":
        levels = {int(x) for x in re.findall(r"\bE([0-4])\b", text)}
        recommends_go = bool(re.search(r"recommend(?:ation)?\s*[:|]\s*go\b", text, re.IGNORECASE))
        if recommends_go and levels and max(levels) == 0:
            warnings.append("validate artifact recommends go on E0 desk/thesis evidence only")
    if args.mode == "name":
        required_unknown = bool(re.search(r"(?:domain|trademark|handle)[^\n|]*(?:unknown|not yet verified|blocked)", text, re.IGNORECASE))
        if required_unknown and not re.search(r"provisional", text, re.IGNORECASE):
            warnings.append("name artifact has an unknown required check but is not labeled provisional")
        if re.search(r"trademark[- ]clear|legally safe", text, re.IGNORECASE):
            warnings.append("name artifact overclaims legal clearance")
    if args.mode == "present":
        theater = re.findall(r"inevitable wave|promised land|winners and losers|\bFOMO\b", editorial_text, re.IGNORECASE)
        if theater:
            warnings.append("present artifact contains startup-theater framing: " + ", ".join(sorted(set(x.lower() for x in theater))))
    if args.force:
        label_prefix = r"(?:\*\*)?"
        label_suffix = r"(?:\*\*)?"
        finalist_rings = set(re.findall(
            label_prefix + r"causal ring\s*[:|]" + label_suffix + r"\s*(?:ring\s*)?([123])",
            text,
            re.IGNORECASE,
        ))
        source_consequences = set(re.findall(
            label_prefix + r"source consequence\s*[:|]" + label_suffix + r"\s*([^\n|]+)",
            text,
            re.IGNORECASE,
        ))
        domains = set(re.findall(
            r"^\s*" + label_prefix + r"domain\s*:" + label_suffix + r"\s*([^\n]+)",
            text,
            re.IGNORECASE | re.MULTILINE,
        ))
        if not ({"2", "3"} & finalist_rings):
            warnings.append("force portfolio has no finalist tagged ring 2 or ring 3")
        if args.mode == "generate" and len(source_consequences) < 2:
            warnings.append("force portfolio finalists do not show multiple source consequences")
        if args.mode == "generate" and len(domains) < 2:
            warnings.append("force portfolio finalists do not show domain breadth")

    structural_score = round(structural + editorial + integrity, 1)
    # Warnings are hard gates, so a structurally complete artifact must not display a passing
    # headline score while failing for overclaiming, causal collapse, or theater.
    score = min(structural_score, 79.0) if warnings else structural_score
    result = {
        "mode": args.mode,
        "force_brief": args.force,
        "breakthrough_mode": args.breakthrough,
        "ai_engineering_foundation": args.ai_engineering_foundation,
        "score_100": score,
        "structural_score_100": structural_score,
        "passed": score >= 80 and not warnings,
        "contract_groups": groups,
        "slop_hits": slop_hits,
        "generic_wrapper_hits": generic_wrapper_hits,
        "cited_links": cited_links,
        "word_count": word_count,
        "declared_speculative": declared_speculative,
        "labeled_observations": labeled_observations,
        "warnings": warnings,
        "note": (
            "Heuristic contract screen only. Marker and cliché regex cannot measure true novelty, "
            "inevitability in hindsight, or venture truth; use blind pairwise review and verify claims."
        ),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if score >= 80 and not warnings else 1


if __name__ == "__main__":
    raise SystemExit(main())
