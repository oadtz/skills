# Live-system playbook — mechanics per duty

Point-in-time defaults; verify current tool facts before quoting them. Named tools are examples,
not dependencies.

## Analytics event design (Duty 1)

Instrument decisions, not everything. Start from the PRD's success signals and write one event per
decision the founder must make: activation (did they reach the core value once?), the core action
(the thing the product exists for), conversion (paid), return (came back in week 2+). Five to ten
events, named in plain language (`report_delivered`, not `btn_click_37`). Prefer a
privacy-respecting tool (e.g. PostHog, Plausible + custom events) and note what personal data is
collected — this feeds solo-operate's privacy-policy floor. Review events when the wedge changes;
delete dead ones.

## Cost guards (Duty 1)

Set hard billing alerts (not just emails to an unread inbox) on: the PaaS, the database, object
storage, and every LLM/API key (per-key limits where the provider supports them). Write the monthly
ceiling in `operations.md`. LLM keys deserve two limits: monthly spend and per-day anomaly.

## Backup and restore drill (Duty 1, then periodic)

Confirm what the managed database actually provides (PITR window, snapshot cadence, retention) —
read the current dashboard, don't assume. Then prove it: restore to a scratch instance, run the
smoke suite against it, record the date and duration in `operations.md`. Repeat the drill on a
calendar cadence (quarterly is a sane default) and after any provider/plan change. Cover the
non-database state too: uploaded files, secrets/env vars (documented recovery path), DNS/domain
registrar access.

## Migration patterns (Duty 3)

- Use the stack's migration tool (e.g. Prisma Migrate, Drizzle Kit, Alembic, Rails migrations);
  migrations are versioned files in the repo, applied by the deploy pipeline.
- **Lock safety first.** A "safe" migration takes the site down when it holds a lock: set a short
  `lock_timeout` (and retry) so a blocked migration fails fast instead of queueing every query,
  build indexes concurrently where the engine supports it (Postgres `CREATE INDEX CONCURRENTLY`),
  and check whether adding a column with a default rewrites the table on your engine/version before
  running it against a large table. Rehearse the migration against the restored scratch instance
  from the backup drill — that is what the scratch instance is for.
- **Expand–contract** for anything touching live data: (1) expand — add new column/table/shape,
  nullable or with an engine-safe default; (2) migrate — backfill in batches, dual-write if needed; (3) switch —
  point reads at the new shape behind the normal release; (4) contract — remove the old shape at
  least one release later, when rollback no longer needs it.
- Every data-touching migration ships with: a fresh backup check, a rollback note (what undoes it —
  and if nothing cleanly does, say so and gate on the founder's explicit go), and a row-count or
  checksum sanity check after backfill.
- Never hand-run SQL against production; if an emergency truly requires it, write the statement
  into the incident record verbatim.

## Smoke suite scope (Duty 3)

A handful of end-to-end tests (e.g. Playwright) that answer "is the product alive as a user?":
sign-up/sign-in, the single core action, payment/checkout if any, and any integration the product
dies without. Run on every release and after every restore drill. Keep it under a few minutes;
depth lives in the unit/behavioral tests from forge-build.

## Incident runbook template (Duty 4)

Keep this filled-in in `operations.md`:

```
Severity: S1 all-users/data/payment down · S2 core degraded · S3 partial/cosmetic
Detection: [what pages the founder, and where]
First moves: rollback command: [exact command, last drilled: date] · status page/channel: [where]
Comms: user-facing note within [X min] for S1/S2 — what broke, impact, next update time
Afterwards (blameless, 5 lines): what happened · impact · cause · fix · prevention
```

Drill the rollback once before you need it. Compose with an installed incident-response capability
when present.

## Dependency policy (Duty 5)

Auto-merge patch/minor updates that pass the full CI gate (tests + build + lint + security scans).
Batch majors into a weekly review slot; read the changelog before merging, and treat any dependency
with a security advisory as a hotfix. If the update queue exceeds a screen, schedule a slice to
clear it — a rotting queue is how supply-chain risk and upgrade cliffs accumulate.

## The monthly learning review (Duty 6)

One page, written into `operations.md` or the idea's memory:

```
Period · Users/usage vs. the PRD's success signals (numbers, not adjectives)
Assumption scoreboard: [each critical assumption → supported / contradicted / still unknown]
Evidence level: E_ → E_ [what earned or blocked the change]
Decision: double down / adjust wedge / route to ideakit-explore / trigger kill criteria
One operational drift to fix: [cost, latency, queue, support load]
```

The review exists to force the loop shut: production behavior updates the idea, or the idea's kill
criteria fire. Both are wins over drifting.
