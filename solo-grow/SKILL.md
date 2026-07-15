---
name: solo-grow
description: >
  Build an automatic, scalable customer-acquisition + growth engine for a one-person business — a
  self-serve funnel, activation/onboarding, retention, a growth loop, lifecycle automation, and paid
  acquisition governed by unit economics — so growth compounds without the founder selling each
  customer by hand. Use for "get customers automatically", "scale acquisition", "grow without manual
  sales", "should I run ads", "CAC / LTV", "growth loop", "self-serve / product-led growth",
  "automate marketing", or "growth is stuck". It is NOT organic channel/audience building (use
  `solo-distribute`), manual founder-led sales (use `solo-sell`), revenue model/price (use
  `solo-model`), or long-term operations (use `solo-sustain`).
---

# Solo — Grow (the automatic, scalable growth engine)

Read `../ai-engineering-foundation.md` now. Treat AI engineering as default build capacity while
keeping acquisition, retention, support, and exception load as real operating constraints.

Take a product that already has *some* paying customers (won manually via `solo-sell`, or found via
`solo-distribute`) and turn acquisition into **an engine that compounds without the founder in the
loop**: a self-serve funnel, an activation experience that delivers value automatically, retention
that holds the bucket, a growth loop that feeds itself, and — only when the math allows — paid
acquisition. Output is a concrete growth-engine plan a single person can run and instrument.

## The governing principle (read first)

**Don't pour acquisition into a leaky bucket, and don't buy growth you can't afford — for a solo, the
engine must compound (a loop) and pay for itself (LTV > CAC, fast).** Three consequences, all the same
principle:

1. **Retention before acquisition — fix the bucket first.** Pouring traffic into a product people
   don't keep using is lighting money on fire. The famous AARRR order (Acquisition first) is misleading;
   practitioners flip it — **retention and activation come first**, because a solo cannot out-acquire
   churn by hand. If the retention curve doesn't flatten, *stop acquiring* and fix the product (loop
   back to `solo-model`/`forge`). (Pirate Metrics: Dave McClure, 2007.)
2. **Loops compound; funnels don't.** A funnel is linear — more spend in, proportionally more out, no
   compounding. A **growth loop** is a closed system where the output of one cohort (content, referrals,
   revenue to reinvest) becomes the input that acquires the next. The automatic engine *is* a loop, not
   a funnel. (Brian Balfour / Reforge.)
3. **For a solo, free/product loops before paid — and paid only when the unit economics clear.** Paid
   acquisition is "automatic" but it's a cash incinerator unless **LTV > CAC** with a **payback period
   short enough that your cash survives**. A solo usually can't float a long payback, so default to
   product/content/referral loops; switch on paid only after the math is proven (see `references/growth-engine.md`).

The point of "automatic" is leverage — the founder builds the engine once, not sells once per customer.

## Is this even your lane? (route honestly)

`solo-grow` assumes a **low-touch, self-serve, repeatable** motion. That fits products where customers
can discover, activate, and pay without a founder-led call (a self-serve app, API, or digital product).
It does **not** fit
high-touch, high-ACV deals — those are won by hand, so route to `solo-sell` and don't try to automate
a sales motion that needs a human. Many solo businesses run **both**: `solo-sell` for the few big
deals, `solo-grow` for the self-serve long tail. If the product has no self-serve path at all, this is
the wrong skill until one exists.

## Where this sits in the pipeline

```
solo-model → solo-fund → solo-distribute → solo-sell → solo-grow (THIS) → solo-sustain
                          get attention      close by hand   automate + scale     run it solo
```

It follows `solo-sell` on purpose: **do things that don't scale first (sell by hand, learn the motion),
then systematize the part that repeats into an engine.** It runs alongside `solo-distribute` (organic
attention) and feeds `solo-sustain` (keep the engine runnable solo).

- If the product **isn't retained** yet, this is premature — back to `solo-model`/`forge` to fix value.
- If the motion is **high-touch sales**, use `solo-sell`, not this.
- This stage ends when there's a working, instrumented loop with sound unit economics the founder can run.

## Host capability mapping

- **User input**: ask one concise question at a time; use structured choices if supported.
- **Research / tooling**: use the host's web/search/browser and the connector/plugin registry to find
  the right analytics, lifecycle/email, ad, and automation tools; use connected analytics to read the
  *actual* funnel, retention curve, and CAC/LTV rather than guessing.
- **No live research**: reason from the founder's described numbers; mark every benchmark and tool fact
  as "verify current."
- **File output**: write the growth-engine plan to a file/artifact if supported; else deliver in chat.

**Grounding:** before stating any external fact (CAC/LTV benchmarks, channel/conversion stats, tool
capabilities or pricing), follow `../solo-grounding.md` if present — source-or-tag every claim and
re-fetch dated figures (these benchmarks drift). It does not make you less decisive about the loop you
pick or the retention gate you enforce.

## Workflow

Five steps: **Fix retention & activation → Know your unit economics → Pick the loop → Build the
self-serve funnel + automation → Instrument & iterate.**

### Step 1 — Fix retention & activation first (the gate)

Before any acquisition, confirm the bucket holds water. Read `references/growth-engine.md`.

- **Define the Aha moment** (the first action where the user experiences core value) and the **North
  Star Metric** (the one metric capturing value delivered — e.g. "accounts with the key action in week 1").
- **Look at the retention curve.** Does it *flatten* (a stable base keeps coming back) or decay to
  zero? A flattening curve is the green light. If it decays, **stop** — acquisition will only scale the
  leak; loop back to `solo-model`/`forge` to fix value/activation.
- **Fix activation** so a new user reaches the Aha moment *on their own*, without you onboarding them by
  hand (that's the founder-in-the-loop you're trying to remove).

### Step 2 — Know your unit economics (the licence to scale)

You cannot run an automatic engine you can't measure. Establish:

- **CAC** (fully-loaded cost to acquire a customer per channel), **LTV** (gross-margin lifetime value),
  **LTV:CAC** (target **≥ 3:1**; thinner means you're buying unprofitable customers), and **CAC payback
  period** (months to recover CAC — for a solo, it must fit the cash you can float; **< 12 months** is a
  common healthy bar, and long paybacks are how solos run out of runway). *These benchmarks are
  point-in-time — see `references/growth-engine.md` and verify.*
- **Rule:** no paid scaling until LTV > CAC with an affordable payback. Loops that are ~free (content,
  referral) can run before the math is perfect; paid cannot.

### Step 3 — Pick the loop (the engine, one of them)

Choose the **one** growth loop that fits the product and the founder, and instrument it (full menu in
`references/growth-engine.md`):

- **Content/SEO loop** — content ranks → attracts users → who create more indexable value/links.
- **Viral/referral loop** — users invite users (track the **k-factor**); works only if the product has
  a natural reason to share.
- **Paid loop** — revenue funds ads that acquire customers whose revenue funds more ads (only when Step
  2's math clears).
- **Sales-assisted self-serve** — self-serve signup with light, automated nudges (not manual selling).

One loop, deep and measured — not five half-built ones (the same "one channel deep" discipline as
`solo-distribute`; Bullseye/Traction picks the channel, this scales the automatable one).

### Step 4 — Build the self-serve funnel + automation (remove the founder)

Make the path run without you:

- **Self-serve funnel:** landing → signup → activation → paid conversion, each step measured and
  frictionless. Self-serve checkout, no human required.
- **Lifecycle automation:** onboarding sequences, activation nudges, trial-conversion and win-back
  emails — the automated equivalent of the follow-ups a founder would do by hand.
- **Automation is the leverage** (ties to `solo-sustain`): every step you automate is a customer you
  didn't have to personally sell.

### Step 5 — Instrument & iterate

Run the AARRR metrics + the North Star; find the **single biggest constraint** in the loop (the step
leaking the most value), fix that one thing, and repeat. Then present:

> **Aha moment / North Star**: [the value action / the one metric]
> **Retention**: [curve flattens? y/n — if n, fix before acquiring]
> **Unit economics**: CAC [x] · LTV [y] · LTV:CAC [r] · payback [m months] → [licence to scale paid? y/n]
> **The loop**: [the one loop + why it fits]
> **Self-serve funnel + automation**: [the path + the lifecycle sequences that remove you]
> **Biggest constraint now**: [the one step to fix next]
>
> Want me to hand this to `solo-sustain` to keep the engine runnable without burning out? If retention
> is the problem, back to `solo-model`/`forge`; if the real motion is high-touch, `solo-sell`.

The founder owns the calls; this skill builds and instruments the engine.

## Operating principles

- **Retention is the foundation.** Acquisition into a leaky bucket is malpractice. Fix the curve first;
  a solo cannot out-acquire churn by hand.
- **Loops over funnels.** Build something that compounds (each cohort brings the next), not a linear
  spend-in-traffic-out pipe. Linear growth caps at your budget; loops compound.
- **Don't buy growth you can't afford.** Paid only when LTV > CAC with a payback your cash can float.
  Free/product loops first; paid is an amplifier of working economics, never a fix for broken ones.
- **Automate the founder out of the path.** The whole point is leverage — the engine sells while you
  don't. Manual onboarding/selling at scale is `solo-sell`, not this.
- **One loop, deep and instrumented.** Five half-built channels is five ways to leak. Master and
  measure one before adding another.
- **Honesty:** if the retention curve decays, say so plainly and refuse to scale acquisition — scaling
  a leaky product wastes the founder's scarcest resources. If the motion is genuinely high-touch, say
  it isn't a self-serve growth problem and route to `solo-sell`. Mark CAC/LTV benchmarks and tool facts
  as point-in-time until verified.

## Execution

**Don't stop at the plan — execute it.** Build the real deliverables with the right tool (write the
funnel/landing copy, the lifecycle/onboarding email sequences, and a CAC/LTV/retention tracking spec or
a script to compute it from the founder's data) instead of handing back advice. All landing and
lifecycle copy passes `../solo-craft.md` — no marketing-tell centroid; emails read like a helpful human
wrote them once, not like a drip tool generated them forever. Stage anything that
runs/pays for ads, sends from the founder's accounts, or spends money for their one-click approval.
Full contract: `../solo-execution.md`.

## Reference files

- `../solo-grounding.md` — the `solo-*` family's shared anti-hallucination guard: **read before stating
  any external fact** (CAC/LTV benchmarks, channel/conversion stats, tool capabilities/pricing).
  Source-or-tag every claim, re-fetch dated figures, stay decisive.
- `references/growth-engine.md` — the engine in detail: AARRR/Pirate Metrics, retention curves &
  activation/Aha moment, growth loops vs funnels, the loop types, unit economics (CAC, LTV, LTV:CAC,
  payback) with current benchmarks and sources, and the self-serve funnel + lifecycle-automation playbook.
