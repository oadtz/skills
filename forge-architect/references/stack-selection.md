# Stack selection — choosing tech when AI writes most of the code

This is the governing principle applied to the stack: **default boring.** Boring ≠ outdated — it means
stable, predictable, with known failure modes, and (critically, now) better AI output. Use this in
Step 2 of forge-architect.

## The innovation-token rule

You get roughly **three "innovation tokens"** for a new project (Dan McKinley, *Choose Boring
Technology*). Spend them only on the parts that make the product *genuinely* unique. Everything else —
language, framework, database, queue, hosting — defaults to proven, mainstream, well-understood tech.

- Spending a token means taking on "unknown unknowns" — the failure modes you can't anticipate.
- For AI-built products there's a **second cost**: agents write measurably worse code in exotic
  languages/frameworks (thin training data → more hallucination and incorrect code). An exotic stack
  costs you twice: thinner human help *and* weaker AI help.
- So the bar for novelty is higher than it used to be. "It's interesting" is not a token spend.
  "Our core differentiator requires it" is.

Source: https://mcfunley.com/choose-boring-technology

## Criteria, in priority order

1. **Boring + proven + stable failure modes.** Postgres over the trendy new database; a mainstream web
   framework over the framework-of-the-month.
2. **High training-data volume for the language.** Mainstream languages (JS/TS, Python, Java, Go,
   PHP) get more reliable AI output than niche ones. This is now a first-class selection criterion.
3. **Test the specific library–model pair, don't trust popularity.** A single (un-peer-reviewed,
   Python-only) preprint found up to 84% quality differences between functionally-equivalent libraries,
   the "best" library *changed with the model* in 86% of pairs, and a model's coding-leaderboard rank
   barely correlated with its actual per-library code quality. Treat the exact percentages as
   directional, not settled — but the underlying move is sound: when the AI will write most of the code
   against a library, try a representative task with the host's model before committing.
4. **Readable and judgeable by a human.** AI assistance only works if someone can tell when the AI is
   wrong. Pick a stack the user (or a reviewer) can actually read.
5. **State it explicitly.** Under-specification hands the choice to the model's training-data default
   (often React + TypeScript + Tailwind + Postgres on Vercel). That default is *usually fine* — the
   risk is that it's unexamined. Make it a recorded decision, not a reflex.

Sources: https://arxiv.org/html/2509.11132v1 (library–model proficiency — a single Python-only
preprint, treat as directional); ThoughtWorks, "Spec-driven development" (Dec 2025) — on higher
code quality from explicit technical specs:
https://www.thoughtworks.com/en-us/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices

## A sane default stack for an AI-built web MVP

Not prescriptive — a reasonable starting point to deviate from *with a reason*:

- **Language**: TypeScript (full-stack) or Python (if data/ML-heavy).
- **Frontend**: React + Tailwind + shadcn/ui + Radix (see forge-design).
- **Backend**: a mainstream framework in the chosen language; modular monolith (see
  `architecture-patterns.md`).
- **Data**: Postgres with a type-safe schema/ORM layer (one source-of-truth schema file).
- **Auth**: a managed auth provider over hand-rolled auth for v1 — auth is a classic place AI
  introduces vulnerabilities.
- **Hosting**: a managed PaaS (see forge-ship `ci-deploy.md`).

Each of these is a place to spend — or pointedly *not* spend — an innovation token. Record the ones
that are hard to reverse (language, data store, auth) as ADRs.

## Anti-patterns to flag

- **Novelty for its own sake.** A trendy stack the team can't debug and the model can't write well.
- **Microservices from day one.** An MVP architecture mistake — see `architecture-patterns.md`.
- **Choosing by GitHub stars / leaderboard rank.** Neither predicts AI codegen quality for *your*
  model on *that* library.
- **Letting the agent pick silently.** A default is fine; an *unexamined* default is the start of
  drift.
