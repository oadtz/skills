# Deploy & observability — ship lean, fail safe

This is the governing principle applied to release: **ship lean, fail safe.** The MVP minimum is
rollback + isolation + error tracking — not a Kubernetes cluster. Use in Steps 4–5 of forge-ship.

## Observability minimum (Step 4)

- **Error tracking from day one** (e.g. Sentry) — the highest signal-per-effort instrument. Wire it
  before first release so you see real failures, not user complaints.
- **Structured logging** (JSON, with request id + user id) and a **health/uptime check** at first
  release. Metrics and traces can follow soon after.
- **If AI is core to the product, add LLM tracing at launch** (Langfuse — OSS, OTel-aligned; Helicone —
  fastest to integrate; LangSmith — if on LangChain): trace prompt→response, tokens, cost, latency,
  tool calls. This is also what feeds the eval golden dataset (see `ai-evals.md`). Anchor on the
  **OpenTelemetry GenAI semantic conventions** to avoid lock-in (still stabilizing).

Sources: https://sentry.io/ , https://langfuse.com/ ,
https://github.com/open-telemetry/semantic-conventions-genai

## Deploy lean (Step 5)

- **Managed PaaS over self-managed infra:**
  - frontend-heavy → Vercel / Netlify / Cloudflare;
  - full-stack with a DB → Render / Railway / Fly;
  - AWS/GCP/Azure only when a specific compliance or scale need demands it.
- **Immutable deploys + one-click rollback** — the MVP minimum. Every deploy is a new immutable
  artifact; rolling back is selecting the previous one, not a redeploy scramble.
- **Feature flags** for risky features, so you can disable without redeploying.
- **Per-environment secret isolation:** never commit secrets; `.env` local-only with a checked-in
  `.env.example`; staging gets *test* keys; prod fetches from a secret store. A **staging gate** before
  prod.

## What to skip (premature scaling is the #1 startup killer)

Defer until scale actually demands it — building it now is cost with no benefit:
- Kubernetes / container orchestration.
- Canary / blue-green / multi-region deployments.
- Microservices and service meshes (see `forge-architect/references/architecture-patterns.md`).
- Custom autoscaling, multi-DB sharding, read replicas.

Prematurely-scaled startups wrote ~3.4× more code in discovery and none passed 100k users (Startup
Genome). "Design for 10×, expect to rewrite before 100×."

## App builder off-ramp (if the MVP started in v0 / Lovable / Bolt / Replit)

"Prompt to production" is a myth — the failure mode is the **data/security layer**, not UI quality. An
audit specifically of apps built on vibe-coding platforms found ~88% had row-level security disabled
and a large share carried high-impact vulnerabilities (consistent with the ~45% OWASP-issue rate for
AI-generated code generally in `security-gates.md` — this is the app-builder-specific slice of the same
problem). So if the product was scaffolded in an app builder:

1. **Export to GitHub early** to preserve ownership and escape lock-in.
2. Put it through the real engineering gates (`security-gates.md`): auth, DB access policies (RLS),
   secrets, tests, CI.
3. Only then put it in front of real users.

Replit and exported GitHub code give the cleanest off-ramp.

Sources:
https://securityboulevard.com/2025/10/methodology-how-we-discovered-over-2k-high-impact-vulnerabilities-in-apps-built-with-vibe-coding-platforms/ ,
https://startupgenome.com/insights/a-deep-dive-into-the-anatomy-of-premature-scaling

## Pre-release checklist

- [ ] CI gates blocking on main (lint/type/test/build + security — see `security-gates.md`).
- [ ] Secrets isolated per environment; none in code or agent config.
- [ ] Error tracking live; health check responding.
- [ ] LLM tracing live (if AI is core).
- [ ] Immutable deploy + verified one-click rollback path.
- [ ] Staging gate passed; behavior verified on a preview (`verify` / `run` skills).
- [ ] Residual risk reported to the user — what's covered, what's deferred, what they're accepting by
      shipping. The user makes the final ship/no-ship call.
