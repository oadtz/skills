# Forge — Execution contract (build it, don't just spec it)

Read this in every `forge-*` skill. Forge is already the most hands-on family — but make the bias
explicit: **produce the real foundation, design, code, and release configuration with the right tool**,
not a description of them. This file is the family-level execution guard; it's self-contained so
`forge-*` stays standalone.

## The principle

**Build, don't just plan.** Each forge stage has a buildable output — a scaffolded foundation, a design
system, working sliced code, a shippable release. Once the decisions are made, **make them real** with
the appropriate tool and verify externally, rather than handing back a plan.

## What "executing" looks like per skill

- **forge-architect** → write the actual ADRs, the schema/contract files, and **scaffold the repo** —
  not a description of the stack. Record decisions as real files.
- **forge-design** → produce the real design tokens, component specs, and flow definitions (machine-
  readable where the pipeline expects it), not a written description of a design system.
- **forge-build** → actually **write the code, the tests, and run them**; build skeleton-first then
  slice by slice, verifying each externally. The deliverable is working software, not a slice list.
- **forge-ship** → actually set up the CI gates, the security/eval checks, and the deploy/rollback
  configuration as real files/config — not a checklist of what to configure.

## Pick the right tool for the job

- **File tools + code/shell** — write and run the real code, tests, configs, and scripts; drive the
  host's coding capability where available.
- **External verification** — actually run the linters, scanners, tests, and the app itself; capture
  real output. The author doesn't grade the work (a fresh check does).
- **Web research** — for current library/version/security facts (under the grounding/anti-slopsquatting
  discipline — verify packages exist; don't hallucinate dependencies).
- **Connectors / MCP** (GitHub, CI, observability, etc.) — to *read* state and *prepare* changes,
  subject to the boundary below.
- **Share the result** — surface the real diffs, test output, and artifacts.

## Keep the human-judgment gates

Keep the decision points: the stack/data-store choice (architect), the ship/no-ship call (ship), and
any irreversible architectural decision get the user's sign-off. Execution means building fully once the
call is made — not making irreversible calls for the user.

## The hard boundary (never cross without explicit, per-action confirmation)

Prepare, but don't autonomously perform:

- **Deploying to production**, **pushing to shared branches**, **merging**, or **releasing**.
- **Provisioning paid infrastructure** or anything that **spends money**.
- **Destructive operations** (dropping data, force-pushes, deleting resources) and anything
  **irreversible**.
- **Acting on external accounts** (publishing packages, opening public PRs from the user's identity).

Stage these — write the config, prepare the PR, set up the deploy — then hand the user the final
deploy/merge/publish step with a clear summary and the rollback path (per `forge-ship`).

## In short

Write and run the real code/config, verify externally, keep the user on the irreversible calls — and
stage any deploy, spend, or destructive action for their explicit approval.
