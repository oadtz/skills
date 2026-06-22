# ADR guide — record irreversible decisions, feed them to agents

This is the governing principle applied to memory: **record irreversibly.** ADRs are the durable
rationale that stops agents (and humans) re-litigating or unknowingly violating past decisions across
sessions. Use in Step 4 of forge-architect — and keep adding ADRs in `forge-build` whenever a
significant decision is made.

## What an ADR is

A short markdown file capturing one architectural decision and *why*. Use the lightweight **Nygard
format**:

```
# NNNN. <short title of the decision>

## Status
Accepted   (or: Proposed / Superseded by ADR-00XX / Deprecated)

## Context
The forces at play — the problem, constraints, and options considered. What makes this decision
necessary, in a few sentences.

## Decision
The choice, stated plainly. "We will use Postgres as the primary datastore."

## Consequences
What becomes easier and what becomes harder as a result. The trade-offs you're accepting.
```

- **Numbered** monotonically: `0001-use-postgres.md`, `0002-modular-monolith.md`.
- **In-repo**, in `docs/adr/` (source control, not a wiki — so ADRs diff alongside the code).
- **Immutable** once Accepted. Don't edit a decision — write a *new* ADR that supersedes it and link
  back. The history is the point.
- Keep it to ~1–2 pages. Use the heavier MADR format (adds "Considered Options" with pros/cons) only
  for genuinely multi-option decisions; it's over-ceremony for simple ones.

Sources: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions ,
https://martinfowler.com/bliki/ArchitectureDecisionRecord.html ,
https://www.thoughtworks.com/en-us/radar/techniques/lightweight-architecture-decision-records (Adopt
ring, with the "source control not wiki" rule), https://adr.github.io/madr/ (the heavier variant).

## What deserves an ADR

The decisions that are **hard to reverse** — the YAGNI carve-out:

- The language and core framework.
- The architecture style (modular monolith vs alternatives).
- The data store and the data-modeling approach.
- The authentication / authorization approach.
- Any load-bearing third-party dependency or platform you're betting on.
- Any deliberate deviation from a forge default (e.g. "why we chose microservices anyway").

Don't ADR reversible, low-stakes choices — that's just noise.

## Feeding ADRs to agents (without burning context)

The agent rules file (`CLAUDE.md` / `AGENTS.md`) loads on *every* invocation, so inlining ADR bodies
burns the context window on every turn. Instead:

- **Link, don't inline.** Reference the `docs/adr/` directory from the rules file ("Architectural
  decisions are recorded in `docs/adr/` — consult before changing data model, auth, or service
  boundaries"). The agent pulls the specific ADR on demand.
- **The ADR-first loop:** for a significant decision — define it → write the ADR → hand to the agent →
  implement → review → clear context → next. ADRs reinject the *intention* agents otherwise lose
  between sessions.
- ADRs pair naturally with the C4 diagram (the "what") — the ADR carries the "why" the diagram and the
  code can't express.

Sources: https://blog.buildbetter.ai/agents-md-vs-cursorrules-vs-claude-skills-2026-comparison/ ,
https://medium.com/devops-ai/vibe-adr-building-with-intention-in-the-age-of-ai-d01e93f36696

## Caution

- The qualitative problem ADRs solve (agents drift and re-litigate decisions across sessions) is well
  attested; specific productivity figures floating around ("teams burn N hours/week reconciling AI
  output") are unsourced marketing — don't cite them as fact.
- Regex-based ADR-enforcement tooling exists but is early-stage and catches only *syntactic*
  violations — useful, but don't rely on it for semantic drift. The durable mechanism is a short ADR a
  human and the agent both read, not an enforcement gadget.
