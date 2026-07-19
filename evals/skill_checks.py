#!/usr/bin/env python3
"""Shared structural checks for skill families.

These go beyond keyword presence: they assert that a SKILL.md still has its
required sections, that it has not been hollowed out, that its frontmatter name
matches its directory, and that its reference files still carry real content.
Keyword-only checks cannot tell a rewritten skill from a gutted one.
"""

from __future__ import annotations

import re
from pathlib import Path


# A skill stripped below this is a stub, not a skill.
MIN_SKILL_LINES = 60
# A reference file below this has been gutted.
MIN_REFERENCE_LINES = 25
MIN_REFERENCE_HEADINGS = 2


def headings(text: str) -> list[str]:
    return [line.strip().lstrip("#").strip().lower() for line in text.splitlines() if line.startswith("#")]


def check_skill_file(
    label: str,
    path: Path,
    root: Path,
    prefix: str,
    required_terms: list[str],
    required_headings: list[str],
    failures: list[str],
    require_foundation: bool = True,
    extra_required_refs: list[str] | None = None,
) -> str:
    """Structural + content checks for one SKILL.md. Returns its text ('' if missing)."""
    if not path.exists():
        failures.append(f"{label}: missing {path.relative_to(root)}")
        return ""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if len(lines) >= 500:
        failures.append(f"{label}: SKILL.md must stay below 500 lines")
    if len(lines) < MIN_SKILL_LINES:
        failures.append(
            f"{label}: SKILL.md is {len(lines)} lines — below the {MIN_SKILL_LINES}-line floor "
            "(hollowed out or truncated?)"
        )
    if text.count("```") % 2:
        failures.append(f"{label}: unbalanced fenced code blocks")

    # Frontmatter must exist, be terminated, and name the skill after its directory.
    match = re.match(r"^---\nname: (" + prefix + r"[a-z-]+)\ndescription:", text)
    if not match:
        failures.append(f"{label}: malformed or unexpected frontmatter")
    else:
        if match.group(1) != path.parent.name:
            failures.append(
                f"{label}: frontmatter name {match.group(1)!r} does not match directory {path.parent.name!r}"
            )
        if text.count("\n---\n") < 1 or len(text.split("\n---\n")) < 2:
            failures.append(f"{label}: frontmatter is not terminated")

    if require_foundation and "`../ai-engineering-foundation.md`" not in text:
        failures.append(f"{label}: does not reference ../ai-engineering-foundation.md")
    for ref in extra_required_refs or []:
        if f"`{ref}`" not in text:
            failures.append(f"{label}: does not reference {ref}")

    lowered = text.lower()
    for term in required_terms:
        if term.lower() not in lowered:
            failures.append(f"{label}: missing contract term {term!r}")

    present = headings(text)
    for heading in required_headings:
        if not any(heading.lower() in h for h in present):
            failures.append(f"{label}: missing required section heading {heading!r}")

    # Local markdown references must resolve, and referenced files must not be gutted.
    for raw_ref in re.findall(r"`((?:\.\./|references/)[^`\n]+\.md)`", text):
        target = (path.parent / raw_ref).resolve()
        if not target.exists():
            failures.append(f"{label}: broken local reference {raw_ref!r}")
            continue
        if raw_ref.startswith("references/"):
            check_reference_file(label, target, failures)

    return text


def check_reference_file(label: str, target: Path, failures: list[str]) -> None:
    ref_text = target.read_text(encoding="utf-8")
    ref_lines = ref_text.splitlines()
    if len(ref_lines) < MIN_REFERENCE_LINES:
        failures.append(
            f"{label}: reference {target.name} is {len(ref_lines)} lines — below the "
            f"{MIN_REFERENCE_LINES}-line floor (gutted?)"
        )
    if len(headings(ref_text)) < MIN_REFERENCE_HEADINGS:
        failures.append(
            f"{label}: reference {target.name} has fewer than {MIN_REFERENCE_HEADINGS} headings "
            "(gutted?)"
        )


def check_readme_mentions(readme_path: Path, names: list[str], failures: list[str]) -> None:
    if not readme_path.exists():
        failures.append(f"{readme_path.name}: missing")
        return
    readme = readme_path.read_text(encoding="utf-8")
    for name in names:
        if name not in readme:
            failures.append(f"{readme_path.name}: does not mention {name}")
