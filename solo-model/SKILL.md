---
name: solo-model
description: >
  Decide HOW a one-founder business makes money before building it — choose a revenue model that
  captures value early and remains sustainable under founder-directed AI engineering, then set
  initial pricing. Use this skill when a solopreneur, indie hacker, or bootstrapper asks "how should I make
  money from this", "what business model fits a solo founder", "should this be SaaS or a service or
  a product", "how do I price this", "how do I monetize my idea", "what's the smallest thing I can
  charge for", or hands off a validated idea / PRD from ideakit-validate and now needs a commercial
  model. It is the FIRST stage of the solo build-a-business pipeline. It is NOT for generating or
  validating the idea itself (use the ideakit skills), NOT for raising capital (use solo-fund), NOT
  for customer acquisition/sales/growth (use solo-distribute, solo-sell, or solo-grow), and NOT for
  long-term operations (use solo-sustain).
---

# Solo — Model (idea → how it makes money)

Read `../ai-engineering-foundation.md` now. Treat directed AI engineering capacity as the default for
software and do not choose a business model by imposing a human implementation-hours ceiling.

Take a validated idea — ideally a PRD/`PLAN.md` from `ideakit-validate`, or just a clear concept —
and decide the **revenue model and starting price a founder-directed business can actually run.** Output is a
short, concrete *business-model decision*: the model, the price, the path to first revenue, and the
explicit trade-offs — not a 40-page business plan.

## The governing principle (read first)

**Pick the model that captures value soon and sustains founder attention; do not minimize the product
merely to match human coding hours.**

A founder's binding constraint is consequential attention, external access, and operating risk—not
personal implementation throughput. For software, assume the founder directs an AI engineering team
under `../ai-engineering-foundation.md`. Choose the model for value capture, time to evidence or cash,
and sustainable operation while preserving credible ambition. Three consequences follow:

1. **Evidence and cashflow before unsupported scale.** A paid proof beats a long speculative build,
   but it need not become a permanent service or small product. A broad SaaS is valid when the AI
   engineering control plane is credible and the external proof justifies the next tranche of scope.
2. **Size to a reachable audience, not a TAM slide.** A small number of reachable buyers at a price
   supported by comparable products is a real solo business; "1% of a $10B market" is a fantasy a
   single person can't capture. Cite current comps before quoting buyer-count or price benchmarks.
3. **Every unresolved operational burden consumes founder attention.** AI coders can absorb build and
   maintenance work only where direction, verification, and escalation are explicit. Support,
   fulfillment, onboarding, refunds, trust, and exceptions remain model costs until designed away.

## Where this sits in the pipeline

```
ideakit-validate (PRD/PLAN.md)  →  solo-model (THIS)  →  solo-fund  →  solo-distribute  →  solo-sell  →  solo-grow  →  solo-sustain
                                   how it makes money     fund it       get attention       close deals    automate     run it solo
```

The `solo-*` family is the **commercial track** — it runs alongside the `forge-*` build track, not
after it. You decide the model here *before or in parallel with* building, because the model dictates
what's even worth building first.

- If the user has **no validated idea yet**, this is the wrong tool — point them to the ideakit family.
- If the model is already clear and they need money to build it, go to `solo-fund`.
- This stage ends when the user has picked a model + a starting price and approved the trade-offs.

## Host capability mapping

Use capabilities by intent, not by product-specific tool name:

- **User input**: ask one concise question at a time; use the host's structured-choice UI if present.
- **Research**: use the host's web/search/browser to check how comparable products/services monetize
  and at what price points; use connected CRM/analytics if the user already has traffic or customers.
- **No live research**: proceed from the PRD and the user's knowledge, but mark all price and
  willingness-to-pay claims as assumptions to test (and route the test to `solo-distribute`).
- **File output**: write the model decision to a file/artifact if supported; otherwise deliver it in
  chat and say no file was written.

**Grounding:** before stating any external fact (price benchmarks, market rates, who-pays norms),
follow `../solo-grounding.md` if present — source-or-tag every such claim and re-fetch time-sensitive
numbers. It strengthens the honesty guards already here; it does not make you less decisive about the
price you set.

## Workflow

Four steps: **Intake → Choose the model → Set the starting price → Name the trade-offs.**

### Step 1 — Intake (what constrains the model)

Pull from the PRD (don't re-derive what `ideakit-validate` already established): the target user, the
core value, the v1 scope, and any platform the product lives in. Then establish the three things the
model actually turns on, asking only what's missing:

- **Runway & attention**: how many months can the user fund themselves, and how much consequential
  review, customer work, and escalation can they sustain? This sets how fast the model must produce
  evidence or cash.
- **Directed engineering capacity**: what can the AI engineering team build and maintain under explicit
  interfaces, verification, permissions, observability, and rollback? Do not convert nights/weekends
  into a feature-count ceiling.
- **Buyer & frequency**: who pays, how often is the problem felt, and is it a business expense
  (easier, higher price) or out of personal pocket (harder, price-sensitive)?

### Step 2 — Choose the model (read the patterns)

Read `references/business-models.md`. Propose **one primary model** with a one-line rationale, and
name the Stairstep path out of it. The main solo-viable models:

- **Productized service** — fixed scope, fixed price, repeatable. Useful when service delivery is the
  fastest informative paid proof; do not make it the automatic precondition for software.
- **SaaS / software product** — recurring or usage-based software from a narrow tool to a broad system.
  Judge it by value capture, distribution, directability, verification, operational control, support,
  uptime, and churn—not by what one human could code.
- **One-off digital product** — template, course, tool, plugin, ebook. Near-zero marginal cost, but
  no recurring revenue — you resell to new buyers forever (a Stairstep "step 1").
- **Marketplace / community / paid newsletter** — monetize an audience directly. Only viable if the
  user already has or will build distribution (hand the build to `solo-distribute`).
- **Usage / API / "tool behind an API"** — sell a capability metered by use. Clean solo economics if
  the value is automatable and self-serve.

**Apply the principle, don't just match a label:** if two models fit, prefer the one that resolves the
critical business uncertainty and captures value with sustainable founder attention. Recommend a
Stairstep only when it is the best evidence or funding path, not because a solo founder is presumed
unable to direct a large software build.

### Step 3 — Design the offer & set the starting price

Read `references/pricing-playbook.md` — it now covers **offer design** (Hormozi's Value Equation +
Grand Slam Offer — raise perceived value and reverse risk so the same deliverable commands more),
**value-based price research** (Van Westendorp PSM to find the range, Gabor-Granger to set the tier),
and **growing price over time**. Price is judged *inside an offer*, so shape the offer first, then set a
concrete starting price — not a range to "figure out later." Rules:

- **Price on value and on who pays, not on cost.** Cost-plus is the classic solo mistake — your
  marginal cost is ~zero, so cost-plus underprices drastically.
- **Start higher than feels comfortable.** Underpricing is the more common and more dangerous error
  for solo founders: it attracts the highest-maintenance customers and starves your runway. You can
  discount; you can rarely raise on existing customers without pain.
- **Pick a model that doesn't tie revenue to your hours** where possible (flat/tiered/seat/usage over
  pure hourly), so income isn't capped by a single person's calendar.
- **B2B tolerates far higher prices than B2C.** A $200/mo B2B tool is an easy expense; a $200/mo
  consumer app is a hard sell. Let the buyer type set the floor.

### Step 4 — Name the trade-offs (be honest)

State plainly what this model costs the founder: time-to-first-dollar, operational load (support,
fulfillment, churn), how income scales (or doesn't) with one person's time, and the main risk. Then
present the decision:

> **Model**: [primary model] · **Starting price**: [concrete number/structure]
> **First revenue path**: [the smallest sellable thing → who buys it → roughly when]
> **Stairstep**: [step 1 now → step 2 later → step 3 dream], if applicable
> **Trade-offs**: time-to-cash [x], operational load [low/med/high], scales-with-time [yes/no], main risk [y]
>
> Want me to hand this to **solo-fund** (fund the build with minimal dilution), **solo-distribute**
> (build the channel that gets attention), or **solo-sell** (turn that attention into closed,
> paying deals)?

The user picks the model and approves the trade-offs before moving on.

## Operating principles

- **Cashflow is oxygen; ambition is not the enemy.** Bias ties toward faster evidence and viable cash,
  but retain a large architecture when its affordable-loss path and control plane are credible.
- **Charge from day one.** "Free until it's perfect" is how solo products die — free users don't
  validate a business, and you learn the real price only by asking for money. The cost of building
  the wrong thing is low now (AI); the cost of *believing* the wrong thing for 6–18 months is not.
- **Operational load is a cost, even when it doesn't show on the P&L.** It's paid in the founder's
  hours and attention — the scarcest resource. Prefer low-touch, asynchronous, high-margin revenue.
- **Model for directed capacity you control.** AI engineering capacity counts when it is directable,
  verifiable, integrable, operable, and containable. Do not assume human headcount is required, and do
  not pretend generated code removes customer, legal, support, or exception work.
- **Honesty:** if the only viable model is operationally heavy or slow to pay, say so plainly — don't
  dress a hard model as an easy one. Flag willingness-to-pay as an assumption until real money proves it.

## Execution

**Don't stop at the plan — execute it.** Once the founder has made the decisions this skill is built
around, build the real deliverables with the right tool (write the actual copy/spec/script/doc/asset,
run the analysis, do the research) instead of handing back advice. Stage anything that spends money,
acts from the founder's accounts, or is irreversible for their one-click approval. Full contract:
`../solo-execution.md`. Craft bar for the offer's wording (buyer-world outcomes, not category
language): `../solo-craft.md`.

## Reference files

- `../solo-grounding.md` — the `solo-*` family's shared anti-hallucination guard: **read before
  stating any external fact**. Source-or-tag every claim, re-fetch time-sensitive numbers, stay
  decisive. Strengthens honesty without adding hedging.
- `references/business-models.md` — the solo-viable revenue models, their economics, time-to-cash,
  operational load, and the Stairstep paths between them.
- `references/pricing-playbook.md` — value-based pricing for solo founders, common underpricing
  traps, B2B vs B2C floors, and starting-price heuristics by model.
