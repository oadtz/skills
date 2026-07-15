---
name: forge-architect
description: >
  Turn a PRD or product spec into a sound technical foundation BEFORE any feature code is written —
  choose the tech stack, design the data model and API contracts, decide the architecture (default:
  modular monolith), lock irreversible decisions in ADRs, and scaffold the repo with agent-readable
  conventions. Use this skill whenever the user has a plan and is about to start building and asks
  things like "how should I architect this", "what stack should I use", "set up the project", "design
  the data model / API", "scaffold the repo", "turn this PRD into a buildable foundation", "what's the
  right architecture for this MVP", or hands off a PRD/PLAN.md from ideakit-validate. It is the FIRST
  stage of the forge build pipeline. It is NOT for generating or validating the idea (use the ideakit
  skills), NOT for designing the UI (use forge-design), and NOT for writing the feature code itself
  (use forge-build).
---

# Forge — Architect (PRD → technical foundation)

Read `../ai-engineering-foundation.md` now. Architect for one founder directing an AI engineering team:
explicit boundaries, agent-readable context, verification, permissions, and escalation are defaults.

Take a validated idea — usually a PRD or `PLAN.md` — and turn it into a **foundation an agent can
build on without quietly inventing your architecture for you.** You decide the stack, the data model,
the contracts, and the shape; you write the irreversible decisions down; you scaffold the repo so
every later slice inherits a consistent frame. Output is a small set of durable artifacts, not code.

## The governing principle (read first)

**Decide explicitly, default boring, record irreversibly.**

When you under-specify, the agent fills the gap from its training-data priors — and an *unexamined*
default is the root of most architectural drift. (One study found three phrasings of the *same*
prompt produced a 5.9× difference in generated code size, purely from specificity.) So this stage
does three things, and they are all this one principle:

1. **Decide explicitly.** Name the stack, the architecture style, and the module boundaries — don't
   let the model pick by omission. Specify *boundaries and contracts*, not exhaustive implementation
   detail (over-specification is its own antipattern — it revives waterfall and produces
   unmaintainable structure).
2. **Default boring.** Bias to mainstream, proven, high-training-data technology. Boring ≠ outdated —
   it means stable, known failure modes, *and* better AI output (agents write measurably more correct
   code in high-training-data languages). Spend your ~3 "innovation tokens" only on what makes the
   product genuinely unique.
3. **Record irreversibly.** Whatever is hard to reverse — stack, data model, architecture style,
   auth approach — goes in a lightweight, in-repo, immutable ADR, then is *linked* (not pasted) from
   the agent rules file. ADRs are the memory that stops agents re-litigating or violating past
   decisions across sessions. This is the carve-out to YAGNI: defer features freely, but never defer
   a hard-to-reverse decision.

## Where this sits in the pipeline

```
ideakit-validate (PRD/PLAN.md)  →  forge-architect (THIS)  →  forge-design  →  forge-build  →  forge-ship
                                   decide the system          design the UX    build it       harden + ship
```

- If the user has **no PRD yet**, this is the wrong tool — point them to the ideakit family.
- If the user already has a solid architecture and just wants to build, skip to `forge-build`.
- This stage ends when the foundation artifacts exist and the user approves them.

## Host capability mapping

Use capabilities by intent, not by product-specific tool name:

- **User input**: ask one concise question at a time; use the host's structured choice UI if present,
  else plain text.
- **Research**: use the host's web/search/browser and any connected knowledge to check stack maturity,
  library/model fit, and reference architectures. Batch searches when supported.
- **File output**: write the foundation artifacts (ADRs, data model, API contract, agent rules,
  scaffold) through the host's file/artifact mechanism. If none exists, output them in chat and say so.
- **No live research**: proceed from the PRD, but mark stack-maturity and library-fit claims as
  assumptions to verify.

## Workflow

Five steps: **Intake → Decide the stack → Design the contracts → Lock decisions (ADRs) → Scaffold.**
Do not write feature code here — that's `forge-build`.

### Step 1 — Intake (read the PRD, extract the constraints)

Read the PRD/`PLAN.md`. Pull out what constrains the architecture: the core entities and flows, the
non-functional needs (scale, latency, compliance, offline), the founder control surface and AI
engineering envelope (direction, verification, tool/compute budget, permissions, escalation), any
platform the product must live in, and the initial scope vs explicit
out-of-scope. If the PRD came from `ideakit-validate`, its "v1 scope", "kill criteria", and platform
risk are gold — don't re-derive them. Ask only what's genuinely missing.

### Step 2 — Decide the stack (boring on purpose)

Read `references/stack-selection.md`. Propose a concrete stack with a one-line rationale per choice,
biased to mainstream + proven + high-training-data. The rules:

- **Justify every non-default choice as an innovation-token spend.** If a choice isn't the boring
  default, say *why this product needs it*. No free novelty.
- **The agent's default (often React + TypeScript + Tailwind + Postgres) is usually fine** — the risk
  is that it's *unexamined*, not that it's wrong. Make it a decision, not a reflex.
- **Pick a stack the user (or a reviewer) can actually read and judge.** AI assistance only works if
  someone can tell when the AI is wrong.
- **Don't pick libraries by popularity alone** when the AI will write most of the code — per-library
  codegen quality varies sharply and isn't predicted by stars or leaderboards. Prefer libraries the
  host's model demonstrably handles well.

Present the stack and get a thumbs-up before designing contracts.

### Step 3 — Design the contracts (design before code)

Read `references/architecture-patterns.md`. Design the structure in this order — each artifact becomes
machine-readable context that narrows the agent's search space in `forge-build`:

1. **Architecture shape.** Default to a **modular monolith** — single deployable, clean internal
   module boundaries. Do not infer microservices from product size, AI-agent count, or the human team
   a conventional company would need. Use independent services only when deployment, security,
   reliability, scaling, or ownership boundaries require them. Any deviation needs an ADR.
2. **Domain model + ubiquitous language.** Name the core entities and their precise definitions so the
   agent and the humans share one vocabulary. Identify bounded contexts if the domain warrants it.
3. **Data model / schema.** Design the data schema (e.g. one source-of-truth schema file). A
   type-safe schema constrains both humans and agents and stops hallucinated columns.
4. **API contract.** Define the contract (e.g. OpenAPI) for anything with a client/server or
   service boundary — *if the contract is relatively stable*. Generate stubs/types/mocks from it so
   front and back can't drift. Skip this ceremony for a tiny single-surface app.

Keep it to **boundaries and contracts, not implementation detail.** Apply YAGNI: design for ~10× the
expected load, not 1000×; don't build presumptive features.

### Step 4 — Lock decisions in ADRs

Read `references/adr-guide.md`. For each hard-to-reverse decision (stack, architecture style, data
store, auth, key third-party dependency), write a lightweight ADR — Nygard format (Title, Status,
Context, Decision, Consequences), numbered, in-repo (`docs/adr/`), immutable once accepted (supersede,
never edit). These are short. Then reference the `docs/adr/` directory from the agent rules file
rather than inlining the bodies.

### Step 5 — Scaffold the repo + agent rules

Produce the minimal scaffold the build stage will inherit:

- **Repo skeleton**: directory layout matching the architecture (organize toward *vertical slices* /
  features, not deep horizontal layers — see `forge-build`), config, lockfile, `.gitignore` with
  `.env` ignored **before** the first commit.
- **Agent rules file** (`CLAUDE.md` / `AGENTS.md`): short — aim ~80–120 lines, hard ceiling well
  under 200. Include build/test/lint commands, conventions, the stack, "always/never" rules, and a
  *link* to `docs/adr/`. Reference canonical example files; do not paste code (prevents staleness).
  Document only what agents commonly get wrong — bloated rules files *lower* success and raise cost.
- **AI engineering control plane**: record work-packet boundaries, stable interfaces, source-of-truth
  context, acceptance and external-verification commands, permission limits, parallel-work rules,
  integration order, stop conditions, and founder escalation triggers.
- **An architecture sketch**: a C4 **Context + Container** diagram is enough for an MVP (skip the Code
  level — it drifts instantly). Diagrams-as-code (e.g. Mermaid) in-repo so it versions with the code.

Then present the foundation and offer the handoff:

> The foundation is set: [stack], [architecture], [N] ADRs, schema + contract, AI engineering control
> plane, and a scaffolded repo with agent rules. Want me to hand this to **forge-design** to build the design system and core
> flows, or straight to **forge-build** to start building?

The user approves the foundation before any building begins.

## Operating principles

**Decide explicitly:**
- **Specify boundaries and contracts, not exhaustive detail.** Over-specification revives waterfall.
- **No choice by omission.** If you didn't decide it, the model's default decided it for you.

**Default boring:**
- **Innovation tokens are scarce.** Novelty must earn its place against the build risk and the thinner
  AI support an exotic stack carries.
- **Modular monolith until proven otherwise.** Microservices are an MVP anti-pattern.

**Record irreversibly:**
- **ADRs for anything hard to reverse** — then link, don't inline.
- **YAGNI, with the carve-out.** Defer features and scale; never defer code health or irreversible
  architectural decisions. The optional [`ponytail`](https://github.com/DietrichGebert/ponytail)
  companion enforces this YAGNI/minimalism discipline per edit through the build — if it's installed,
  let it, and don't re-litigate the same ladder here. (Install and command details, plus the skeptical
  note on its self-reported metrics, are in the forge-README and `forge-build`'s *Companion* section.)

**Honesty:** flag where the stack is unproven for the host's model, where scale assumptions are
guesses, and where a decision is reversible vs not. Don't present a guess as a finding.

## Execution

**Don't stop at a spec — build it.** Write the actual ADRs, schema/contract files, and **scaffold the
repo** with the right tool, not a description of the stack. Keep the user's sign-off on the
stack/data-store and any irreversible call; execute fully once decided. Stage anything that provisions
paid infra or pushes to shared branches for their approval. Full contract: `../forge-execution.md`.

## Reference files

- `references/stack-selection.md` — *default boring*: criteria for choosing a stack when AI writes
  most of the code; the innovation-token rule; library-vs-model fit.
- `references/architecture-patterns.md` — *decide explicitly*: modular monolith vs alternatives,
  design-before-code ordering (domain → schema → API contract), what to NOT over-build.
- `references/adr-guide.md` — *record irreversibly*: the lightweight ADR format and how to feed ADRs
  to agents without burning context.
