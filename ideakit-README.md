# Ideakit — a 3-skill idea pipeline

A loosely-coupled set of skills that take you from "I have no idea" to "buildable plan."
They share the `ideakit-` prefix so they're easy to spot as a family, but each works standalone
and triggers on its own intent — they're connected by handoffs, not merged into one monolith.

## The three skills

| Order | Skill | Use it when… | Output |
|---|---|---|---|
| 1 | **ideakit-generate** | you have *no* idea yet — only constraints (industry, skills, budget) | ranked shortlist of raw ideas |
| 2 | **ideakit-explore** | you have a direction and want to expand / stress-test it | sharpened options + key unknowns |
| 3 | **ideakit-validate** | you have a chosen idea and want it validated + turned into a plan | a PRD / PLAN.md ready for Claude Code |
| 4 | **ideakit-present** | you need to win customers, investors, or teammates over | persuasive deck / demo / one-pager / memo |

```
ideakit-generate  →  ideakit-explore  →  ideakit-validate  →  ideakit-present
 generate ideas       expand + challenge    validate + PRD       make people act
```

## How to use

- **Full journey**: start at `ideakit-generate`, let it hand the winner to `ideakit-explore`,
  then to `ideakit-validate`, then to `ideakit-present` to pitch it.
- **Jump in anywhere**: already have an idea? go straight to `ideakit-validate`. Just want a
  sparring partner? use `ideakit-explore` alone. Need to pitch an idea you've already shaped? go
  straight to `ideakit-present`. Each skill knows where it sits and will point you to the right neighbor.

## Design notes

- **Single responsibility + loose coupling.** Each skill does one job well; the handoff text in
  each `SKILL.md` is the connective tissue. This keeps every skill under the ~500-line best-practice
  limit and lets you iterate/evaluate them independently.
- **Evidence-driven.** `ideakit-generate` sources ideas from real trends and complaints;
  `ideakit-validate` pressure-tests the two things AI-generated ideas over-rate (feasibility and
  platform survivability). The human always makes the go/kill call.
- **Persuasion is story-first.** `ideakit-present` builds the narrative and emotional core before
  choosing a format (deck/demo/one-pager), because a polished deck around a weak story convinces
  no one. It only sells what validation made true — never hype past the substance.
- **Naming.** `ideakit-<role>` — role-based so the order and function are obvious at a glance.
  These local copies supersede the similarly-named installed plugin skills; keep one source active
  to avoid double-triggering.

## Optional next step

If you want a single "run the whole pipeline" entry point, add a thin orchestrator command
(e.g. `/idea-to-prd`) that calls the three in sequence — without merging them.
