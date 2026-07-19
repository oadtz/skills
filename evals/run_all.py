#!/usr/bin/env python3
"""Run every deterministic eval for the skill families and summarize."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    ("ai-engineering-foundation", ROOT / "evals/check_ai_engineering_foundation.py"),
    ("ideakit-regression", ROOT / "evals/ideakit/run_regression.py"),
    ("forge-contracts", ROOT / "evals/forge/check_contracts.py"),
    ("solo-contracts", ROOT / "evals/solo/check_contracts.py"),
]


def main() -> int:
    results: dict[str, object] = {}
    all_passed = True
    for name, script in CHECKS:
        completed = subprocess.run(
            [sys.executable, str(script)], cwd=ROOT, text=True, capture_output=True
        )
        passed = completed.returncode == 0
        all_passed = all_passed and passed
        entry: dict[str, object] = {"passed": passed}
        if not passed:
            try:
                payload = json.loads(completed.stdout)
                entry["failures"] = payload.get("failures", payload)
            except json.JSONDecodeError:
                entry["output"] = completed.stdout.strip()
                entry["stderr"] = completed.stderr.strip()
        results[name] = entry

    print(json.dumps({"passed": all_passed, "checks": results}, indent=2, ensure_ascii=False))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
