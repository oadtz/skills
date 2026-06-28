---
name: forge-ship
description: >
  Make a built product production-ready and release it — CI-enforced quality and security gates,
  dependency-integrity checks, evals for any AI features, observability, and a deployment with
  rollback. Use this skill whenever a product is built and the user is preparing for production, or
  says things like "is this production-ready", "harden this", "add security", "set up CI/CD", "review
  for vulnerabilities", "add tests/evals", "deploy this", "ship it", "set up monitoring", "prepare for
  launch", or hands off from forge-build. It is the FINAL stage of the forge pipeline: it makes the
  guardrails blocking and gets the product out the door safely. It is NOT for choosing the architecture
  (use forge-architect), the design system (use forge-design), or writing the feature code itself (use
  forge-build).
---

# Forge — Ship (working product → production-ready release)

Take a built, tested product and make it **safe to put in front of real users**, then release it. The
work is the safety net: turn the quality and security checks into *blocking, external* CI gates, add
the minimum observability and rollback to operate it, and deploy lean. Output is a hardened, monitored,
deployed product — and the gates that keep it that way.

## The governing principle (read first)

**The human is overconfident and the agent grades itself generously — so the gates must be blocking
and external.**

The evidence is consistent and uncomfortable: AI-generated and AI-assisted code repeatedly shows
security, dependency, and overconfidence failure modes. Re-check the current figures in
`references/security-gates.md` before quoting numbers. You cannot close this gap with discretion — a
reviewer who is overconfident won't choose to check. So:

1. **Gates are blocking, in CI.** Lint, type-check, test, secret-scan, SAST, and dependency checks run
   on every change and *block merge* — not "we'll review it." Branch protection on the main branch is
   the single most important control for AI-built code.
2. **Gates are external.** The check is run by the pipeline and a fresh reviewer, not graded by the
   agent that wrote the code. Verify behavior and real scan output, not the agent's word.
3. **Ship lean, fail safe.** Managed hosting, immutable deploys, one-click rollback, isolated
   per-environment secrets, a staging gate, and error tracking from day one. Skip the heavy
   infrastructure until scale actually demands it.

## Where this sits in the pipeline

```
forge-architect  →  forge-design  →  forge-build  →  forge-ship (THIS)
decide the system   design the UX    build it       harden + ship
```

- If the product **isn't built yet**, that's `forge-build` — don't harden a skeleton.
- This stage can also run standalone on an existing codebase the user wants to make production-ready.
- This stage ends when the gates are enforced, observability is live, and the product is deployed with
  a rollback path — and the user makes the final ship/no-ship call.

## Compose, don't re-derive

Review/verification capabilities may be available in the host. If present, use them as the engine:

- **Security/code review capability** (for example `security-review` / `code-review`) — run it as the
  review gate, not a hand-rolled checklist.
- **Accessibility/UX review capability** (for example `web-design-guidelines`) — use it as the UI gate.
- **App-verification capability** (for example `verify` / `run`) — drive the real app to confirm
  behavior before release.

## Host capability mapping

- **Code / config writing**: use the host's coding capability to add CI config, scanners, eval
  harnesses, and deploy config.
- **Verification / review**: run tests, scanners, and an independent review pass (separate from the
  code's author) capturing real output.
- **Research**: check current advisories, the host platform's deploy docs, and OWASP references.
- **File output**: write CI workflows, eval datasets, runbooks, and deploy config as real files.
- **No CI/deploy capability**: produce the CI workflow, gate definitions, eval suite, and a deploy
  runbook as artifacts, and say the user must wire them into their provider.

## Workflow

Five steps: **Quality gates → Security & dependency gates → Evals (if AI) → Observability → Deploy.**
The first two make the existing checks *blocking*; the rest make it operable and out the door.

### Step 1 — Make quality gates blocking (CI)

Read `references/security-gates.md`. Stand up the CI pipeline and turn discretion into enforcement:

- On every PR: **lint → type-check → test → build**; on merge: deploy. Pin CI actions to a commit SHA,
  use OIDC not long-lived credentials, least-privilege permissions.
- **Branch protection on main** — every change (including every agent change) goes through review +
  passing checks. This is the highest-leverage single control.
- **Preview/PR deployments** so reviewers check *behavior*, not just diffs.
- A **Definition of Done** that counteracts AI's biases: tests pass in CI, lint/type clean, no new
  duplicated blocks, change small enough to review in one sitting, behavior verified on a preview,
  errors instrumented. A human reviews every AI diff.

### Step 2 — Security & dependency-integrity gates

Read `references/security-gates.md`. Add the security net (all free/low-cost tier):

- **Secret scanning**: pre-commit (e.g. Gitleaks) + push protection. Confirm `.env` is git-ignored and
  secrets live in a per-environment store, never in code or MCP config files.
- **SAST**: a fast scanner on every PR (e.g. Semgrep) + a deep scan scheduled / pre-release (e.g.
  CodeQL).
- **Dependency integrity vs slopsquatting** ⚠️: ~1 in 5 AI-suggested packages don't exist, *and the
  fake names repeat* — so attackers pre-register them. Never auto-install AI-suggested packages;
  verify each exists + check publisher and registration date; enforce lockfiles + hash pinning;
  enable automated dependency updates (e.g. Dependabot).
- **Security review gate**: run the available security/code review capability (for example
  `security-review`) on changes touching auth, data access, input handling, or external calls. Map
  against **OWASP Top 10:2021 + ASVS Level 1** as the MVP floor — with **input validation / output
  encoding first**. Prioritize broken access control (e.g. confirm row-level security is actually on);
  re-check current incident/audit figures before quoting them.

### Step 3 — Evals for AI features (only if the product itself uses an LLM)

Read `references/ai-evals.md`. Testing AI-*written* code (Step 1) is a different problem from
evaluating AI *features* at runtime (non-deterministic). If the product uses an LLM:

- Build a **golden dataset from 20–50 real failures**, not synthetic happy paths.
- **Assertion / unit evals in CI** as the first line — cheap, code-based, run every change.
- An **LLM-as-judge only after calibrating it to a human**: one domain expert labels data **binary
  pass/fail** with critiques, build the judge from those, and measure agreement with precision/recall.
  Use binary, never a 1–5 Likert score (a sign of a weak eval process).
- Two CI suites — **capability** + **regression** — run on every prompt/model change. Handle
  non-determinism with multiple trials (pass@k for discovery, pass^k for reliability).
- Map against **OWASP Top 10 for LLM Applications** (prompt injection + improper output handling for
  any tool-calling build; excessive agency for autonomous actions).

### Step 4 — Observability (the minimum to operate)

- **Error tracking from day one** (e.g. Sentry) — highest signal per effort.
- **Structured logging** (request id, user id) and a health/uptime check at first release.
- If AI is core to the product, add **LLM tracing** at launch (e.g. Langfuse/Helicone) — prompt→
  response, tokens, cost, latency, tool calls — anchored on OpenTelemetry GenAI conventions to avoid
  lock-in.

### Step 5 — Deploy (lean, with a rollback path)

Read `references/ci-deploy.md`. Ship on the lightest infra that fits:

- **Managed PaaS** (e.g. Vercel/Netlify/Cloudflare for frontend-heavy; Render/Railway/Fly for
  full-stack-with-DB). AWS/Kubernetes only when a specific compliance or scale need demands it.
- **Immutable deploys + one-click rollback** as the MVP minimum; feature flags for risky features.
- **Per-environment secret isolation** — staging gets *test* keys; prod fetches from a secret store; a
  staging gate before prod.
- **Skip** Kubernetes, canary, blue-green, multi-region until scale actually demands it — that's
  premature scaling, the #1 startup killer.

Then confirm the release and the rollback path, and report what's gated, what's monitored, and what
was deliberately deferred. The user makes the final ship/no-ship call.

Shipping is the end of the *build* track, not the journey — point to the **commercial track** next:

> The product is live. Want me to hand this to the `solo-*` track to make it earn? — `solo-distribute`
> to get attention, `solo-sell` to close the first paying customers, or `solo-sustain` to keep a live
> product runnable solo without burning out. (If the revenue model isn't settled yet, start at
> `solo-model`.)

A shipped product that nobody finds or buys isn't done — name the next move toward revenue.

## Operating principles

**Gates are blocking, in CI:**
- **Branch protection is non-negotiable** for AI-built code.
- **A Definition of Done that fights AI's biases** — small batches, no new duplication, human review of
  every diff. AI raises duplication, churn, and instability unless work is chunked small.

**Gates are external:**
- **The author doesn't grade the work.** Independent scanners + a fresh reviewer; capture real output.
- **Verify behavior before release.** Drive the real app; don't trust "it works."

**Ship lean, fail safe:**
- **Rollback before scale.** One-click rollback and a staging gate matter at v1; Kubernetes doesn't.
- **Secrets isolated per environment**, never in code, never in agent config.

**Honesty:** report the residual risk plainly — what's covered, what's deferred, and what the user is
choosing to accept by shipping. Never present an unreviewed build as production-ready.

## Execution

**Don't stop at a checklist — configure it.** Actually set up the CI gates, security/eval checks, and
deploy/rollback configuration as real files, and run the scanners/tests for real. **Hard stop:**
deploying to production, merging/releasing, provisioning paid infra, and destructive ops are the user's
call — stage them and hand over the final deploy/merge step with the rollback path. Full contract:
`../forge-execution.md`.

## Reference files

- `references/security-gates.md` — *blocking + external*: CI gates, the Definition of Done, the
  security baseline (OWASP Top 10 + ASVS L1), and the slopsquatting dependency gate.
- `references/ai-evals.md` — *for AI features*: golden datasets, assertion evals, calibrated
  LLM-as-judge, capability + regression suites, and the OWASP LLM Top 10.
- `references/ci-deploy.md` — *ship lean, fail safe*: managed-PaaS deployment, immutable deploys +
  rollback, per-environment secrets, observability minimum, and what to defer.
