#!/usr/bin/env python3
"""Emit blind routing prompts or score predictions from an external model run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("predictions", nargs="?", type=Path, help="JSON object mapping case id to predicted skill")
    args = parser.parse_args()
    cases = json.loads((HERE / "cases.json").read_text(encoding="utf-8"))

    if args.predictions is None:
        print(json.dumps([
            {"id": case["id"], "prompt": case["prompt"], "allowed_skills": sorted({c["expected_skill"] for c in cases})}
            for case in cases
        ], indent=2, ensure_ascii=False))
        return 0

    predictions = json.loads(args.predictions.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        predicted = predictions.get(case["id"])
        results.append({
            "id": case["id"],
            "expected": case["expected_skill"],
            "predicted": predicted,
            "passed": predicted == case["expected_skill"],
        })
    passed = sum(item["passed"] for item in results)
    payload = {"passed": passed == len(results), "accuracy": passed / len(results), "results": results}
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
