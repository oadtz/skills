# Forge — a 4-skill PRD → product pipeline

A loosely-coupled set of skills that take a validated idea (a PRD / `PLAN.md`) and turn it into a
**running, production-worthy product** — with a deliberate architecture, a real design system, a
verified build, and CI-enforced quality and security gates.

Forge is the *downstream sibling* of [ideakit](ideakit-README.md). Where ideakit ends — a PRD ready
for an implementation agent — forge begins. They share nothing but a handoff: ideakit decides *what*
to build and *why*; forge builds it *well*.

```
ideakit-generate → ideakit-explore → ideakit-validate → │ → forge-architect → forge-design → forge-build → forge-ship
  (what to build, validated into a PRD)                 │     decide the      design the    build it      harden +
                                                        │     system          experience                  release
                                              PRD / PLAN.md handoff
```

(`ideakit-present` is a side-branch off validation for packaging/sharing the idea, not an upstream
step into forge — so it's omitted from the build line above.)

## The four skills

| Order | Skill | Use it when… | Output |
|---|---|---|---|
| 1 | **forge-architect** | you have a PRD and need to turn it into a sound technical foundation | stack decision, data model, API contract, ADRs, scaffolded repo + agent rules |
| 2 | **forge-design** | you need a real UI/UX, not generic "AI slop" | design-token system, core user flows, accessible component foundation |
| 3 | **forge-build** | the foundation exists and it's time to write the product | a working, tested product built skeleton-first then slice-by-slice |
| 4 | **forge-ship** | the product runs and needs to be production-ready and released | CI guardrails, security + eval gates, deployment with rollback + observability |

## How to use

- **Full journey**: hand a PRD to `forge-architect`; let each stage hand off to the next, ending at a
  deployed product. Each skill states where it sits and points to its neighbors.
- **Jump in anywhere**: already have an architecture? go straight to `forge-build`. Just need to make
  an existing UI not look AI-generated? use `forge-design` alone. Just hardening before launch? go
  straight to `forge-ship`.

## The one idea behind the whole family

**AI makes code cheap to produce but quietly raises duplication, churn, and insecurity — and the
human reviewing it is measurably overconfident.** (Stanford CCS 2023: people with an AI assistant
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

## Design notes

- **Single responsibility + loose coupling.** Each skill does one stage well; the handoff text in each
  `SKILL.md` is the connective tissue. This keeps every skill under the ~500-line norm and lets you
  iterate on them independently — the same design DNA as ideakit.
- **Runtime-agnostic.** Skills name capabilities by intent — research, user input, file/artifact
  output, *code-writing / build orchestration* — instead of hard-coding one agent's tool names.
  Host-specific tools (Claude Code, Cursor, a CI provider, a PaaS) are adapters, not the workflow.
- **Evidence-driven and skeptical.** Every default is justified by 2024–2026 practice and flags hype
  (e.g. "prompt-to-production" is a myth; ~45% of AI code carries an OWASP Top 10 issue; ~1 in 5
  AI-suggested packages don't exist). The human always makes the ship/no-ship call.
- **Composes with skills in your environment.** When the `frontend-design`, `tailwind-design-system`,
  and `web-design-guidelines` plugin skills are installed, forge-design drives them rather than
  re-deriving UI guidance (forge-ship does the same with `security-review` / `code-review` / `verify` /
  `run`). These are installed plugin skills, not files in this repo — forge references them by name and
  degrades gracefully if they're absent. forge-build can also hand heavy execution to an external
  agent system (e.g. GSD) if the user prefers.

## Recommended companion: ponytail

forge treats code minimalism as a *principle* woven through its stages (YAGNI with a security
carve-out, "default boring", refactor-while-green, anti-duplication). [**ponytail**](https://github.com/DietrichGebert/ponytail)
— a third-party skill — *enforces* it per edit via a "lazy senior dev" decision ladder (does this need
to exist? → stdlib → native → installed dep → one line → minimum that works), and is "lazy, not
negligent" (it never cuts security, accessibility, or data-loss handling). It's a clean complement to
`forge-build`, so forge **composes with it rather than vendoring a copy** (a copied fork would go
stale). Install it and forge-build will defer minimalism enforcement to it:

```
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

Skeptical note (true to the family's DNA): ponytail's headline metrics (~54% less code, etc.) are
self-reported from a single repo — directional, not validated. The decision-ladder discipline is the
real value; the percentages are a claim.

## Optional next step

If you want a single "PRD to deployed product" entry point, add a thin orchestrator command
(e.g. `/prd-to-product`) that calls the four stages in sequence — without merging them.
