# Ideakit — a 5-skill idea pipeline

A loosely-coupled set of skills that take you from "I don't even know what I want to do" to
"buildable plan" to "people act on it."
They share the `ideakit-` prefix so they're easy to spot as a family, but each works standalone
and triggers on its own intent — they're connected by handoffs, not merged into one monolith.

## The five skills

| Order | Skill | Use it when… | Output |
|---|---|---|---|
| 0 | **ideakit-discover** | you have *no flag at all* — not even a domain or skill — and want to find what's yours | an evidence-backed **edge map** (a frame) |
| 1 | **ideakit-generate** | you have constraints (industry, skills, budget) and want idea options | ranked shortlist of raw ideas |
| 2 | **ideakit-explore** | you have a direction and want to expand / stress-test it | sharpened options + key unknowns |
| 3 | **ideakit-validate** | you have a chosen idea and want it validated + turned into a plan | a PRD / PLAN.md ready for an implementation agent |
| 4 | **ideakit-present** | you need to win customers, investors, or teammates over | persuasive deck / demo / one-pager / memo |

```
ideakit-discover  →  ideakit-generate  →  ideakit-explore  →  ideakit-validate  →  ideakit-present
 excavate the          generate ideas       expand + challenge    validate + PRD       make people act
 person → edge map     (now personalized)
```

## How to use

- **Full journey**: start at `ideakit-discover` if you're at zero, let it hand an edge map to
  `ideakit-generate`, then the winner to `ideakit-explore`, then `ideakit-validate`, then
  `ideakit-present`.
- **Jump in anywhere**: already know your domain/skills? skip discover and start at
  `ideakit-generate`. Already have an idea? go straight to `ideakit-validate`. Just want a sparring
  partner? use `ideakit-explore` alone. Each skill knows where it sits and points you to the right
  neighbor.
- **The blank-slate distinction**: "no idea but I know my domain/skills" → `ideakit-generate`.
  "no flag at all, help me find what I even want" → `ideakit-discover` first; it excavates *you* and
  feeds generate so the ideas come back personal, not generic.

## Design notes

- **Single responsibility + loose coupling.** Each skill does one job well; the handoff text in
  each `SKILL.md` is the connective tissue. This keeps every skill under the ~500-line best-practice
  limit and lets you iterate/evaluate them independently.
- **Evidence-driven.** `ideakit-discover` excavates the person from real behavior (not "what do you
  want?" polling, which produces confabulation); `ideakit-generate` sources ideas from real trends and
  complaints; `ideakit-validate` pressure-tests the two things AI-generated ideas over-rate
  (feasibility and platform survivability). The human always makes the go/kill call.
- **Person before market.** `ideakit-discover` exists because a market idea that doesn't fit the
  founder's edge, energy, and constraints gets abandoned. It discovers founder–direction fit first and
  hands generate an edge map, so sourced ideas are personalized rather than generic.
- **Runtime-agnostic.** Skills name capabilities by intent — research, user input, file/artifact
  output, deck/document creation — instead of hard-coding a single agent's tool names. Host-specific
  tools are adapters, not the core workflow.
- **Persuasion is story-first.** `ideakit-present` builds the narrative and emotional core before
  choosing a format (deck/demo/one-pager), because a polished deck around a weak story convinces
  no one. It only sells what validation made true — never hype past the substance.
- **Naming.** `ideakit-<role>` — role-based so the order and function are obvious at a glance.
  These local copies supersede the similarly-named installed plugin skills; keep one source active
  to avoid double-triggering.

## Optional next step

If you want a single "run the whole pipeline" entry point, add a thin orchestrator command
(e.g. `/idea-to-prd`) that calls the five stages in sequence — without merging them.
