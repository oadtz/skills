#!/usr/bin/env python3
"""Run deterministic Ideakit contract and artifact-fixture regressions."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EVAL = ROOT / "evals/ideakit"
SCORER = EVAL / "score_artifact.py"
FIXTURES = EVAL / "fixtures"

CASES = [
    ("discover-pass", "discover", "contract-pass-discover.md", False, True),
    ("discover-flattery-fail", "discover", "contract-fail-discover-flattery.md", False, False),
    ("generate-pass", "generate", "contract-pass-generate.md", False, True),
    ("generate-fail", "generate", "contract-fail-generate.md", False, False),
    ("generate-force-pass", "generate", "contract-pass-force-generate.md", True, True),
    ("generate-force-direct-fail", "generate", "contract-fail-force-direct-only.md", True, False),
    ("explore-force-pass", "explore", "contract-pass-force-explore.md", True, True),
    ("explore-force-flattened-fail", "explore", "contract-fail-force-explore-flattened.md", True, False),
    ("validate-pass", "validate", "contract-pass-validate.md", False, True),
    ("validate-desk-go-fail", "validate", "contract-fail-validate-desk-go.md", False, False),
    ("name-pass", "name", "contract-pass-name.md", False, True),
    ("name-overclaim-fail", "name", "contract-fail-name-overclaim.md", False, False),
    ("present-pass", "present", "contract-pass-present.md", False, True),
    ("present-theater-fail", "present", "contract-fail-present-theater.md", False, False),
]


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, text=True, capture_output=True)


def main() -> int:
    failures: list[dict[str, object]] = []
    contract = run([sys.executable, str(EVAL / "check_contracts.py")])
    if contract.returncode:
        failures.append({"case": "contracts", "output": contract.stdout, "stderr": contract.stderr})

    results: list[dict[str, object]] = []
    for case_id, mode, filename, force, should_pass in CASES:
        command = [sys.executable, str(SCORER), mode, str(FIXTURES / filename)]
        if force:
            command.append("--force")
        completed = run(command)
        passed = completed.returncode == 0
        try:
            payload = json.loads(completed.stdout)
        except json.JSONDecodeError:
            payload = {"raw": completed.stdout, "stderr": completed.stderr}
        result = {
            "case": case_id,
            "expected": "pass" if should_pass else "fail",
            "actual": "pass" if passed else "fail",
            "score": payload.get("score_100"),
            "warnings": payload.get("warnings", []),
        }
        results.append(result)
        if passed != should_pass:
            failures.append({**result, "details": payload})

    summary = {
        "passed": not failures,
        "contract_check": "pass" if contract.returncode == 0 else "fail",
        "artifact_cases": len(CASES),
        "routing_predictions_tested": 0,
        "results": results,
        "failures": failures,
        "note": "Deterministic regressions only; run evaluate_routing.py with blind model predictions for routing accuracy.",
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
