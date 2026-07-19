---
name: forge-operate
description: >
  Own the live product after first release — the Day-2 engineering loop. Use when a shipped product
  needs a bug fixed, a feature added to an existing codebase, a schema/data migration, backups and a
  restore test, an incident handled, dependency updates triaged, runaway hosting/LLM costs contained,
  or product analytics wired so post-launch behavior can advance the idea's evidence level. Triggers:
  "my product is live", "users found a bug", "add a feature to the running app", "change the database
  schema", "we got paged / site is down", "set up analytics", "hosting bill spiked". It is NOT for the
  first build (forge-build), first hardening/release (forge-ship), or business operations
  (solo-sustain / solo-operate).
---

# Forge — Operate (the Day-2 loop: run, fix, iterate, learn)

Read `../ai-engineering-foundation.md` if it is not already in context. The live system is still one
founder directing an AI engineering team — but now with real users, real data, and real blast radius.

First release is the start of the job, not the end. Most of a product's life — and most of a
technical co-founder's value — is Day 2: observing reality, fixing what breaks, iterating on what
users actually do, and never losing their data. This skill owns that loop.

## The governing principle

**A live system is a loop, not a conveyor: observe → triage → change safely → verify → learn.**
Every change now happens against real users and real data, so the discipline inverts from
forge-build's greenfield freedom: data safety before speed, small reversible changes before big
ones, and evidence from production before opinions from anyone.

## Where this sits

```
forge-architect → forge-design → forge-build → forge-ship → forge-operate (THIS) ⟲
                                      ↑______________________________|
                                       features & fixes loop back through build
```

- New feature or non-trivial fix → define it as a slice and run it through `forge-build`'s loop
  (brownfield rules below), then release through the existing gates.
- Architecture no longer fits (scale, cost, or model change) → return to `forge-architect` with the
  production evidence.
- Recurring human operating load (support, monitoring attention, content) → hand the load map to
  `solo-sustain`; commercial operations (billing, churn, feedback interviews) belong to
  `solo-operate`.
- Usage and retention evidence → write back to the idea's PLAN/memory so its evidence level (E0–E4)
  reflects reality, per `../ideakit-memory.md` when an idea location exists.

## Capability mapping

Use capabilities by intent: code-writing/build orchestration for fixes and slices, shell/CI for
migrations and deploys, web research for current tool/security facts, file output for runbooks and
the operations log. Compose with installed capabilities instead of re-deriving them — e.g. an
incident-response, code-review, or security-review skill, a monitoring MCP, or the host's deploy
integration. Degrade gracefully when absent.

## Workflow

Six duties. On first entry, run Setup (Duty 1) once; afterwards enter at whichever duty the
situation calls for. Read `references/live-system-playbook.md` for the mechanics of whichever duty
you are executing.

### Duty 1 — Instrument reality (one-time setup, then maintained)

If forge-ship's gates left any of these missing, close them now — the loop cannot run blind:

1. **Error monitoring** wired and alerting to a channel the founder actually reads.
2. **Product analytics** instrumenting the PRD's success signals (the leading learning signals and
   lagging outcomes the plan defined) — without this, the evidence level can never advance past
   launch. Prefer a privacy-respecting default; keep events few and named after decisions.
3. **Uptime/health check** with an alert threshold that pages the founder.
4. **Cost guards**: billing alerts on the PaaS, database, and any LLM API; a monthly spend ceiling
   the founder set on purpose.
5. **Backups verified**: confirm the managed database has PITR/daily backups **and run one restore
   test** — an unverified backup is a hope, not a backup. Schedule a periodic restore drill.

Record the setup in `operations.md` at the repo root: what watches what, who gets paged, spend
ceilings, backup/restore evidence and date.

### Duty 2 — Triage what reality reports

For each bug, alert, or user report, decide once, quickly:

- **Hotfix now** (data loss, security, payment, or all-users breakage): smallest safe change,
  through CI, deploy, verify, then backfill a regression test.
- **Slice** (real but not burning): write it as a forge-build slice with acceptance criteria; batch
  into the normal loop.
- **Won't fix / by design**: record the decision and the reason in `operations.md`.

Never let the agent redefine a bug as expected behavior to close it — the reporter's experience is
the acceptance criterion.

### Duty 3 — Change a live system safely (brownfield rules)

forge-build's loop still runs the work, with three overrides:

1. **No unattended greenfield patterns on a live codebase** — every change lands through the
  existing CI gates on a branch; the founder's merge click stays.
2. **Schema changes use expand–contract**: add the new shape, migrate data, switch reads, then
   remove the old shape in a later release. Migrations are versioned files run by the deploy, never
   hand-run SQL. Any migration touching existing rows gets a rollback note and a fresh backup check
   before it ships.
3. **A persistent smoke suite guards the core flow**: a handful of end-to-end tests (sign-in, the
   one action the product exists for, payment if any) that run in CI on every release — screenshots
   from the build phase are evidence, not protection.

### Duty 4 — Handle incidents like a professional

Keep a one-page runbook in `operations.md` (template in the playbook): severity levels, the
rollback command (drilled, not theoretical), where status gets communicated to users, and what gets
written down afterwards (a blameless five-line postmortem: what happened, impact, cause, fix,
prevention). If an incident-response capability is installed, drive it instead of improvising.

### Duty 5 — Keep the platform healthy

- **Dependency updates**: auto-merge patch/minor updates that pass the full gate; batch-review
  majors weekly. Never let the queue rot — stale dependencies are the slow incident.
- **Cost review**: check spend against the ceiling monthly; investigate any step change.
- **Performance/scale signals**: watch the few metrics that predict pain (p95 latency, DB
  connections, queue depth). "Design for 10×, rewrite before 100×" — when production evidence says
  the architecture is out of runway, go back to `forge-architect` with the numbers, not vibes.

### Duty 6 — Learn, then write it back

Monthly (or after every meaningful release): read the analytics against the PRD's success signals
and the assumptions/kill criteria it defined. Three honest outcomes:

- **Signal confirms** → advance the evidence level in the plan/idea memory; double down.
- **Signal contradicts** → the plan's kill/reframe criteria apply — route the product question to
  `ideakit-explore`/`solo-operate`'s feedback loop, not another feature guess.
- **No signal** → the instrumentation or the wedge is wrong; fix whichever it is first.

This duty is what makes the whole skillset a loop instead of a pipeline: production behavior is the
final validator of the idea.

## Execution

Do the work, don't describe it: actually wire the monitoring/analytics, actually write and run the
migration, actually run the restore test, actually add the smoke tests, and record it all in
`operations.md`. Hard boundary per `../forge-execution.md`: deploys to production, destructive data
operations, and anything spending real money get an explicit founder confirmation — prepare
everything up to that click.

## Reference files

- `references/live-system-playbook.md` — mechanics per duty: migration patterns (expand–contract,
  tooling by stack), backup/restore drill, incident runbook template, smoke-suite scope, dependency
  policy, cost-guard setup, analytics event design, and the monthly learning review format.
