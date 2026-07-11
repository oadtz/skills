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
    "generate": {
        "epistemic_chain": [r"observed", r"inferred", r"\bbet\b"],
        "venture_mechanics": [r"wedge", r"first[- ]?10|first (users|customers)", r"distribution", r"compound|power"],
        "entrepreneurial_judgment": [r"counter[- ]?case|wrong if|disconfirm", r"affordable loss|cheapest.*test"],
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
    },
    "present": {
        "epistemics": [r"fact", r"inference", r"ambition"],
        "persuasion": [r"audience", r"ask|action", r"uncertainty|reason not to|counter"],
    },
}


def group_passes(text: str, patterns: list[str]) -> bool:
    return all(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=sorted(MODE_MARKERS))
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()

    text = args.artifact.read_text(encoding="utf-8")
    groups = {name: group_passes(text, patterns) for name, patterns in MODE_MARKERS[args.mode].items()}
    slop_hits = [term for term in SLOP if term.lower() in text.lower()]
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

    score = round(structural + editorial + integrity, 1)
    result = {
        "mode": args.mode,
        "score_100": score,
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
