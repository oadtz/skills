#!/usr/bin/env python3
"""Heuristic scorer for temporary Ideakit artifacts; never treats them as factual truth."""

from __future__ import annotations

import argparse
import json
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


def group_passes(text: str, patterns: list[str]) -> bool:
    return all(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=sorted(MODE_MARKERS))
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--force", action="store_true", help="Apply force-brief causal-depth gates")
    args = parser.parse_args()

    text = args.artifact.read_text(encoding="utf-8")
    groups = {name: group_passes(text, patterns) for name, patterns in MODE_MARKERS[args.mode].items()}
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
    unsupported_precision = len(re.findall(r"\b\d+(?:\.\d+)?%\b|\b\d{2,}\+? (?:users|customers|complaints|people)\b", text, re.IGNORECASE))
    cited_links = len(re.findall(r"\[[^\]]+\]\(https?://[^)]+\)", text))
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
        "score_100": score,
        "structural_score_100": structural_score,
        "passed": score >= 80 and not warnings,
        "contract_groups": groups,
        "slop_hits": slop_hits,
        "cited_links": cited_links,
        "labeled_observations": labeled_observations,
        "warnings": warnings,
        "note": "Heuristic screen only; use blind human/agent pairwise review for originality and truth.",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if score >= 80 and not warnings else 1


if __name__ == "__main__":
    raise SystemExit(main())
