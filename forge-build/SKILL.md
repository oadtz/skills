---
name: forge-build
description: >
  Drive a coding agent to actually build the product from a technical foundation and design system —
  skeleton-first, then vertical slice by vertical slice, each one test-first with a verification gate
  the building agent cannot edit. Use this skill whenever the foundation exists and it's time to write
  the product, or the user says things like "build it", "implement this PRD", "start coding", "let's
  build the MVP", "turn this plan into a working app", "build the next feature", or hands off from
  forge-architect / forge-design. It is the THIRD stage of the forge pipeline and the one that writes
  real code via the host's coding capability. It is NOT for choosing the stack/architecture (use
  forge-architect), NOT for the design system (use forge-design), and NOT for production hardening,
  security gates, or deployment (use forge-ship).
---

# Forge — Build (foundation → working product)

Drive the host's coding capability to build the product **incrementally and verifiably** — prove the
architecture end-to-end with a thin skeleton, then add vertical slices, each built test-first and
checked by a gate the building agent doesn't control. Output is working, tested code, plus a durable
on-disk record of progress.

## The governing principle (read first)

**The agent stops when the work looks done — only an external check it can't edit closes the loop.**

This is the load-bearing fact of agentic building. "Looks done" is the only signal an unsupervised
agent has, so it stops at ~70% (the last 30% — edge cases, error handling, security — is as hard as
ever). Worse, when tests are the reward, agents *game* them — deleting checks, weakening assertions,
special-casing test inputs (METR observed >50% cheating on impossible tasks). So the build is
structured so failure modes are hard to reach:

1. **Thin slice first.** Build the *walking skeleton* — the thinnest build-deploy-test-end-to-end path
   — to prove the architecture and deployment while the codebase is empty and integration is cheap.
   Then add **vertical slices** (each cutting through UI → logic → data), never horizontal layers. A
   slice gives the agent *locality of reference*: the whole feature's context in one pass, so it
   doesn't hallucinate dependencies.
2. **Verify every step, externally.** Every unit of work gets a machine-readable pass/fail gate
   (test/build/lint/screenshot), and **the agent that wrote the code is not the agent that grades
   it** — a separate verifier or a stop condition the implementer can't modify. If you can't verify
   it, it isn't done.
3. **One thing per loop; state on disk.** Build one slice per loop, with fresh-enough context. The
   plan, progress, and decisions live in files — the agent's durable memory across resets and
   compaction — not in a marathon session that rots.

## Where this sits in the pipeline

```
forge-architect  →  forge-design  →  forge-build (THIS)  →  forge-ship
decide the system   design the UX    build it              harden + ship
```

- If there's **no foundation** (stack, data model, scaffold), get one from `forge-architect` first —
  building without it means the agent invents the architecture mid-stream.
- If there's a **UI but no design system**, `forge-design` first, or the slices will drift visually.
- This stage produces working code; production hardening and the real deploy are `forge-ship`. The
  boundary on CI/deploy: forge-build stands up only the **minimal** pipeline the walking skeleton needs
  to prove it deploys (a basic test/lint/build + a throwaway deploy target); `forge-ship` then makes
  those gates **blocking**, adds the security/eval gates, and does the production deployment. If the
  skeleton's deploy target isn't ready yet, prove the skeleton end-to-end locally and defer the deploy
  half to `forge-ship` — don't block building on it.

## Delegation option

forge-build can drive the host's coding capability directly, **or** hand the slice plan to a dedicated
execution system (e.g. GSD) if the user runs one. The workflow below — skeleton, dependency-ordered
slices, test-first, external verification, on-disk state — is the same either way; only the executor
changes. Ask the user's preference if a heavier execution system is available.

## Companion: ponytail (code minimalism)

forge-build's weakest lever is minimalism — it *tells* the agent to refactor and avoid duplication,
but doesn't gate it. The [`ponytail`](https://github.com/DietrichGebert/ponytail) skill closes that
gap: it's a "lazy senior dev" discipline that runs a decision ladder before every edit (does this need
to exist? → stdlib → native → installed dep → one line → minimum that works), and is "lazy, not
negligent" — it never cuts security, accessibility, data-loss handling, or trust-boundary validation,
so it composes cleanly with this skill's verification gates rather than fighting them.

If it's installed, **defer minimalism enforcement to it** instead of re-deriving the same ladder:
- it auto-triggers each session at its configured intensity (`/ponytail [lite|full|ultra|off]`,
  default `full`);
- run `/ponytail-review` on a slice's diff as part of the verification gate (Step 4), and
  `/ponytail-audit` across the repo before handing off to `forge-ship`;
- `/ponytail-debt` harvests any deferred shortcuts into a ledger — fold those into `decisions.md`.

forge **composes with ponytail; it does not vendor a copy.** If it isn't installed, forge-build's own
refactor-while-green step (below) covers the minimalism baseline. Skeptical note: ponytail's headline
metrics are self-reported on one repo — use the discipline, treat the percentages as a claim.

## Host capability mapping

- **Code writing / build orchestration**: use the host's coding agent / file-edit / shell capability
  to write code, run tests, and run builds. This is the core capability this skill needs.
- **Verification**: run tests, type-checks, linters, and builds; capture real output (not the agent's
  claim). Use a separate verification pass / subagent where the host supports it.
- **User input**: confirm slice ordering and surface HITL slices for review.
- **File output**: maintain `plan.md` / `progress.md` / `decisions.md` and per-slice todo state.
- **No coding capability available**: produce the dependency-ordered slice plan + per-slice acceptance
  criteria and test specs as artifacts, and say the host must execute them elsewhere.

## Workflow

Five steps: **Plan slices → Walking skeleton → Slice loop → Verify (externally) → Integrate & track.**

### Step 1 — Decompose the PRD into dependency-ordered slices

Read `references/build-loop.md`. Break the product into **vertical slices**, each:

- spanning all layers (schema → logic → API → UI → tests) for one user-facing capability,
- independently **demoable / verifiable**, and small (≈≤2–3 days of work),
- sequenced so a finished slice **unblocks** the next without requiring other features first,
- tagged **HITL** (needs human review before merge) or **AFK** (agent can complete unattended).

Write the ordered slice list to `plan.md`. Each slice gets **testable acceptance criteria** in
EARS-style `WHEN [condition] THE SYSTEM SHALL [behavior]` — concrete enough to write a test against.
Vague criteria are the #1 cause of agent drift.

### Step 2 — Build the walking skeleton first

Before any feature breadth, build the thinnest slice that goes **end to end and deploys**: one trivial
request flowing through every architectural layer and a real (if empty) deployment + CI run. This
forces the hard integration and deployment problems while the codebase is almost empty, and gives
every later slice a proven path to plug into. Confirm it builds, tests, and deploys green before
proceeding.

### Step 3 — The slice loop (test-first, one thing per loop)

For each slice, in dependency order, run the loop in `references/build-loop.md`:

1. **Write the tests first**, from the slice's acceptance criteria. No mock implementation yet.
2. **Confirm the tests fail** (red) — proves they test something.
3. **Commit the failing tests as a checkpoint** — so any later edit to them shows up in the diff.
4. **Implement until green** — *without modifying the tests to pass.* The agent will sometimes try to
   weaken or delete tests; that's reward hacking, and the committed checkpoint + external verify catch
   it.
5. **Refactor** while green — actively, because AI code skews toward duplication and churn; this is
   where you pay down the copy-paste tax. If `ponytail` is installed, this is where it earns its keep —
   run `/ponytail-review` on the slice diff to catch over-engineering before the gate.

Keep context curated per slice (see `references/context-engineering.md`): a tight rules file, a repo
map for orientation, ADRs linked for the *why*, and clearing context / starting a fresh session (e.g.
`/clear`) on task switches. One slice per loop beats a marathon session.

### Step 4 — Verify externally (the agent doesn't grade its own work)

After implementing a slice, close the loop with a check the building agent **does not own**:

- Run the full gate: tests + type-check + lint + build, and capture the **actual output**.
- **For UI slices, design quality is part of the gate — equal to functional tests.** Verify behavior
  with observable evidence (a screenshot across breakpoints, a real request/response, a running
  process), then run the **look-and-feel + anti-slop checklist** in `forge-design/references/visual-craft.md`
  against that screenshot: design-system fidelity, hierarchy/spacing, all states (empty/loading/error),
  interaction feel, responsive, accessibility, and **none of the AI-slop tells** (purple/cyan gradients,
  Inter default, stock-shadcn look, glassmorphism, gradient text, generic SaaS copy…). "Looks/feels like
  generic AI output" is a **defect** that fails the slice, exactly like a failing test — fix it before
  the slice is accepted. Design must not silently erode during the build.
- Where the host supports it, use a **separate verifier subagent** with fresh context to try to
  *refute* the result, and have a human review the *test diffs* (not just that tests are green) for
  HITL slices.
- Triage rule: is the expected value derivable from code the agent can read, or from a spec it never
  saw? Tests grounded only in the agent's own code can pass while the product is wrong.

A slice is done only when the external gate is green and (for HITL) a human has reviewed the diff.

### Step 5 — Integrate & track

- Merge the slice in a **small, reviewable** change (multiple small PRs beat one giant one — small
  batches are what separate teams where AI *helps* delivery from teams where it hurts stability).
- Update `progress.md` (what's done, what's next) and `decisions.md` (any deviation from the plan and
  why). These survive context resets and are how the next loop knows where it is.
- Re-check the next slice's dependencies are still satisfied; re-order if a slice revealed something.

When the slices that make up v1 are built and green, offer the handoff:

> v1 is built and the suite is green. Want me to hand this to **forge-ship** to add the production
> guardrails (security + eval gates, CI, observability) and deploy it?

## Operating principles

**Thin slice first:**
- **Walking skeleton before features.** Prove integration and deployment on an empty codebase.
- **Vertical slices, never horizontal layers.** Locality of reference is why agents build them well.

**Verify every step, externally:**
- **The writer is not the grader.** A separate check the agent can't edit is the single highest-value
  anti-failure mechanism.
- **Verify behavior, not claims.** Real output, screenshots, running processes — not "it works."
- **Review test diffs, not just green checks.** Reward hacking hides in the test edits.

**One thing per loop; state on disk:**
- **Context is a finite resource you curate.** Drift over a long build is mostly a context-hygiene
  failure.
- **Persist plan/progress/decisions to files.** Fresh context each loop beats a rotting marathon.

**Quality as you go:**
- **Refactor while green.** AI code arrives duplicated and under-refactored; pay it down per slice,
  not "later." Defer to `ponytail` for this if it's installed (see *Companion* above).
- **The best code is the code you never wrote.** Run the minimalism ladder *before* writing — skip,
  reuse stdlib/native/existing deps, or one line — before reaching for the minimum that works.
- **Small batches.** Many small reviewable changes, not one heroic merge.

## Execution

**Don't stop at a slice list — write the code.** Actually write the code and the tests and **run them**;
build skeleton-first then slice by slice, verifying each externally with real output. The deliverable is
working, tested software. Stage anything that pushes to shared branches, merges, or runs destructive ops
for the user's approval. Full contract: `../forge-execution.md`.

## Reference files

- `references/build-loop.md` — *thin slice + verify*: walking skeleton, vertical-slice decomposition,
  EARS acceptance criteria, the test-first loop, and the external verification gate.
- `references/context-engineering.md` — *one thing per loop, state on disk*: rules files, repo maps,
  ADR linking, session isolation, and persisting progress to survive resets.
