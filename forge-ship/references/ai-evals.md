# Evals for AI features — a different discipline from testing code

This applies only when **the product itself uses an LLM** at runtime. Testing AI-*written* code
(deterministic; see `forge-build/references/build-loop.md`) is a different problem from evaluating AI
*features* (non-deterministic). Conflating them is the most common mistake. Use in Step 3 of forge-ship.

## The root cause evals fix

Unsuccessful LLM products share one root cause: **no robust eval system** (Hamel Husain, "Your AI
Product Needs Evals"). Without evals you're guessing whether a prompt or model change helped or
regressed. Build the eval system as part of shipping, not after.

Source: https://hamel.dev/blog/posts/evals/

## The three levels

1. **L1 — assertion / unit evals (conquer most here first).** Cheap, code-based checks that run on
   every change in CI: does the output contain/avoid X, parse as valid JSON, call the right tool, stay
   within length, etc. Build **domain-specific** assertions — generic off-the-shelf metric suites are
   overrated; the metrics that matter are specific to your product.
2. **L2 — human + LLM-as-judge (on a cadence).** For qualities you can't assert in code. Requires a
   judge calibrated to a human (below) and tooling to view/label data.
3. **L3 — A/B testing (mature products).** Real user outcomes; only once L1/L2 are solid.

## Build the golden dataset from real failures

Start with **20–50 tasks drawn from actual failures**, not synthetic happy paths. Real failure modes
are where the signal is. Grow it as new failures appear in production (your observability — see
`ci-deploy.md` — feeds this).

## LLM-as-judge — only after calibrating to a human

Don't trust an uncalibrated judge. Hamel's "Critique Shadowing":

1. One **domain expert** defines "good," labels data **binary pass/fail**, and writes a short critique
   for each.
2. Build the judge prompt **from those critiques**.
3. **Measure the judge's agreement with the human using precision/recall** (not raw accuracy).

Use **binary pass/fail, never a 1–5 Likert score** — "tracking 1–5 scores is often a sign of a bad eval
process." Anthropic concurs: judges must be closely calibrated to human experts.

Sources: https://hamel.dev/blog/posts/llm-judge/index.html ,
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ,
https://eugeneyan.com/writing/evals/

## Wire it into CI

- Keep **two suites**: **capability** evals (is it good enough?) and **regression** evals (did this
  change break something that worked?). Run both on **every prompt or model change** and every model
  upgrade.
- Handle non-determinism with **multiple trials**: report **pass@k** for discovery ("can it ever do
  this?") and **pass^k** for reliability-critical behavior ("does it do this every time?").
- Three grader types: code-based, LLM-based (calibrated), human.

## Tooling (you usually need two)

- A lightweight framework for **CI gating**: Promptfoo (OSS CLI, gating + red-teaming), DeepEval
  (pytest-native), Ragas (RAG metrics: faithfulness, context precision/recall).
- A platform for **annotation + regression tracking**: Braintrust, LangSmith (if on LangChain),
  Langfuse (OSS).

## Security for AI features — OWASP LLM Top 10

If the product calls an LLM, map against the **OWASP Top 10 for LLM Applications 2025**:
- **LLM01 Prompt Injection** + **LLM05 Improper Output Handling** — mandatory for any tool-calling
  build (treat model output as untrusted input to downstream systems).
- **LLM06 Excessive Agency** — for autonomous actions; constrain what the agent can do without
  confirmation.
- Treat **every MCP server / tool as a trust boundary** — least-privilege scopes, sandboxing, no token
  passthrough.

Sources: https://genai.owasp.org/llm-top-10/ ,
https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices

## Hype to avoid

- Generic metric suites and public leaderboards rarely predict *your* product's quality.
- A 1–5 quality score signals a weak process — use binary.
- An uncalibrated LLM-judge is an untested instrument; calibrate before you trust it.
