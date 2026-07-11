# Ideakit — a 5-stage idea pipeline (+ a naming utility)

A loosely-coupled set of skills that take you from "I don't even know what I want to do" to
"buildable plan" to "people act on it."
They share the `ideakit-` prefix so they're easy to spot as a family, but each works standalone
and triggers on its own intent — they're connected by handoffs, not merged into one monolith.

## The skills

| Order | Skill | Use it when… | Output |
|---|---|---|---|
| 0 | **ideakit-discover** | you have *no flag at all* — not even a domain or skill — and want to find what's yours | an evidence-backed **edge map** (a frame) |
| 1 | **ideakit-generate** | you have constraints/edge/change signals and want venture opportunities | opportunity theses + venture portfolio + storage prompt |
| 2 | **ideakit-explore** | you have a direction and want to expand / stress-test it | sharpened options + key unknowns |
| 3 | **ideakit-validate** | you have a chosen idea and want it validated + turned into a plan | a PRD / PLAN.md + idea-memory update |
| 4 | **ideakit-present** | you need to win customers, investors, or teammates over | persuasive deck / demo / one-pager / memo + idea-memory update |
| — | **ideakit-name** *(utility)* | you need to name the product/brand and check it's actually usable | a screened name shortlist + idea-memory update |

```
ideakit-discover  →  ideakit-generate  →  ideakit-explore  →  ideakit-validate  →  ideakit-present
 excavate the          generate ideas       expand + challenge    validate + PRD       make people act
 person → edge map     (now personalized)            ↳ ideakit-name (name + screen availability) ↲
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
- **Venture discovery, not idea vending.** `ideakit-discover` excavates provisional founder-edge
  hypotheses from behavior; `ideakit-generate` turns change signals and contradictions into opportunity
  theses, venture architectures, wedges, and learning tests; `ideakit-explore` expands unresolved
  theses; `ideakit-validate` tests only mature concepts. The human owns every directional decision.
- **Person before market.** `ideakit-discover` exists because a market idea that doesn't fit the
  founder's edge, energy, and constraints gets abandoned. It discovers founder–direction fit first and
  hands generate an edge map, so sourced ideas are personalized rather than generic.
- **Runtime-agnostic.** Skills name capabilities by intent — research, user input, file/artifact
  output, deck/document creation — instead of hard-coding a single agent's tool names. Host-specific
  tools are adapters, not the core workflow.
- **Idea memory is shared, not copied.** Once `ideakit-generate` stores an idea set, later skills use
  `ideakit-memory.md` to update the same idea location with exploration notes, validation outcomes,
  naming decisions, pitch artifacts, and next actions.
- **Invention freedom, evidence discipline.** Research claims are strict (Observed / Inferred / Bet;
  never fabricate), while the invention phase uses selected lenses rather than a mandatory framework
  march. `ideakit-craft.md` rejects interchangeable concepts, unsupported novelty, quota-filling, and
  generator prose at every stage.
- **Persuasion is story-first.** `ideakit-present` builds the narrative and emotional core before
  choosing a format (deck/demo/one-pager), because a polished deck around a weak story convinces
  no one. It only sells what validation made true — never hype past the substance.
- **Names are screened, not just brainstormed.** `ideakit-name` treats *availability* (domain,
  trademark, handles, market collision) as a hard gate and **checks for real** — it never claims a name
  is free without a live check, and flags that screening isn't legal clearance. It's a utility that
  slots in after validate and feeds present/forge/solo.
- **Naming.** `ideakit-<role>` — role-based so the order and function are obvious at a glance.
  These local copies supersede the similarly-named installed plugin skills; keep one source active
  to avoid double-triggering.

## Optional next step

If you want a single "run the whole pipeline" entry point, add a thin orchestrator command
(e.g. `/idea-to-prd`) that calls the five stages in sequence — without merging them.
