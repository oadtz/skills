# Forge — a 5-skill PRD → product → live-system pipeline

A loosely-coupled set of skills that take a validated idea (a PRD / `PLAN.md`) and turn it into a
**running, production-worthy product that stays alive** — with a deliberate architecture, a real
design system, a verified build, CI-enforced quality and security gates, and a Day-2 operating
loop for the shipped system.

Forge is the *downstream sibling* of [ideakit](ideakit-README.md). Where ideakit ends — a PRD ready
for an implementation agent — forge begins. They share nothing but a handoff: ideakit decides *what*
to build and *why*; forge builds it *well*.

```
ideakit-generate → ideakit-explore → ideakit-validate → │ → forge-architect → forge-design → forge-build → forge-ship → forge-operate ⟲
  (what to build, validated into a PRD)                 │     decide the      design the    build it      harden +     run, fix,
                                                        │     system          experience                  release      iterate, learn
                                              PRD / PLAN.md handoff                            features loop: operate → build → ship
```

(`ideakit-present` is a side-branch off validation for packaging/sharing the idea, not an upstream
step into forge — so it's omitted from the build line above.)

## The five skills

| Order | Skill | Use it when… | Output |
|---|---|---|---|
| 1 | **forge-architect** | you have a PRD and need to turn it into a sound technical foundation | stack decision, data model, API contract, ADRs, scaffolded repo + agent rules |
| 2 | **forge-design** | you need a real UI/UX, not generic "AI slop" | design-token system, core user flows, accessible component foundation |
| 3 | **forge-build** | the foundation exists and it's time to write the product | a working, tested product built skeleton-first then slice-by-slice |
| 4 | **forge-ship** | the product runs and needs to be production-ready and released | CI guardrails, security + eval gates, deployment with rollback + observability |
| 5 | **forge-operate** | the product is live and must be run, fixed, iterated, and learned from | Day-2 loop: analytics + monitoring + cost guards, safe migrations, backups + restore drill, incident runbook, monthly learning review |

## How to use

- **Full journey**: hand a PRD to `forge-architect`; let each stage hand off to the next, ending at a
  deployed product. Each skill states where it sits and points to its neighbors.
- **Jump in anywhere**: already have an architecture? go straight to `forge-build`. Just need to make
  an existing UI not look AI-generated? use `forge-design` alone. Just hardening before launch? go
  straight to `forge-ship`.

## The one idea behind the whole family

**One founder directs an AI engineering team by default; Forge is the control plane that makes this
capacity directable, parallelizable, verifiable, integrable, and safe to operate.** The product may be
ordinary deterministic software with no runtime AI. Cheap code still raises duplication, churn, and
insecurity—and the human reviewing it can be overconfident. (Stanford CCS 2023: people with an AI assistant
wrote *less* secure code yet believed it was *more* secure.) So forge's real job is not "prompt the
agent to build it" — it's to be the **harness that makes the known failure modes hard to reach**:
under-specified architecture, generic UI, agents that stop at "looks done," tests the agent quietly
rewrites to pass, hallucinated dependencies, and unreviewed code shipped on overconfidence.

Each skill is one application of that idea to a stage:

| Stage | The failure it guards against | The governing principle |
|---|---|---|
| forge-architect | the model silently picking your architecture from its training-data defaults | *Decide explicitly, default boring, record irreversibly.* |
| forge-design | generic centered-card / purple-gradient "AI slop" | *Constrain before you generate; define the system before the screens.* |
| forge-build | the agent declaring victory at 70% and reward-hacking its own tests | *Only an external check the agent can't edit closes the loop.* |
| forge-ship | overconfident humans shipping insecure, duplicated AI code | *Gates are blocking and external — verify behavior, not the agent's word.* |
| forge-operate | the pipeline ending at first deploy while the live product rots unowned | *A live system is a loop: observe → triage → change safely → verify → learn.* |

## Design notes

- **Single responsibility + loose coupling.** Each skill does one stage well; the handoff text in each
  `SKILL.md` is the connective tissue. This keeps every skill under the ~500-line norm and lets you
  iterate on them independently — the same design DNA as ideakit.
- **Runtime-agnostic.** Skills name capabilities by intent — research, user input, file/artifact
  output, *code-writing / build orchestration* — instead of hard-coding one agent's tool names.
  Host-specific tools (Claude Code, Cursor, a CI provider, a PaaS) are adapters, not the workflow.
- **Evidence-driven and skeptical.** Defaults are grounded in current practice and the reference files
  carry point-in-time evidence; re-check dated security/package claims before quoting numbers. The human
  always makes the ship/no-ship call.
- **Design quality = functional quality (a first-class gate).** Look-and-feel and UX *feel* matter as
  much as the product working, so design is enforced, not just briefed: `forge-design` sets the
  anti-slop brief + visual-craft bar, `forge-build` checks design fidelity + anti-slop per slice, and
  `forge-ship` runs a blocking Design/UX quality gate. "Looks/feels like generic AI slop" is a defect
  that fails the build, exactly like a failing test (see `forge-design/references/visual-craft.md`).
- **Composes with capabilities in your environment.** When UI design, design-system, accessibility,
  security-review, code-review, or app-verification capabilities are installed, forge drives them rather
  than re-deriving their guidance. Named skills such as `frontend-design`, `tailwind-design-system`,
  `web-design-guidelines`, `security-review`, `code-review`, `verify`, or `run` are examples, not hard
  dependencies; degrade gracefully if they're absent. forge-build can also hand heavy execution to a
  dedicated external execution system (e.g. an external multi-agent execution framework — link yours
  if you use one) if the user prefers.

## Recommended companion: ponytail

Optional: [**ponytail**](https://github.com/DietrichGebert/ponytail) enforces code minimalism per edit;
forge composes with it rather than vendoring a copy — see `forge-build`'s *Companion* section
(canonical) for what it does, install steps, and the skeptical note on its self-reported metrics.

## Optional next step

If you want a single "PRD to deployed product" entry point, add a thin orchestrator command
(e.g. `/prd-to-product`) that calls the five stages in sequence — without merging them.
