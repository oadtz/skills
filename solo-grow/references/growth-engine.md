# The growth engine in detail

The "how" behind `solo-grow`. Spine: **retention before acquisition; loops over funnels; and paid only
when the unit economics clear.** Everything here rests on named, established frameworks — don't invent
benchmarks or assert "this channel works" without evidence (see `../solo-grounding.md`).

## Contents

- AARRR / Pirate Metrics
- Activation and the Aha moment
- Retention
- Growth loops vs funnels
- Unit economics
- Self-serve funnel and lifecycle automation
- How to iterate

## AARRR / Pirate Metrics (the map)

Dave McClure's framework (500 Startups, 2007): the five metrics a product-led business tracks —
**Acquisition, Activation, Retention, Referral, Revenue** ([ProductPlan](https://www.productplan.com/glossary/aarrr-framework)).
It's the shared vocabulary for the funnel. **But the acronym's order misleads:** the fastest-growing
solo products fix **Activation + Retention first**, then turn on Acquisition — because acquisition into
a product people don't keep is wasted spend. Use AARRR to *measure*; use the order below to *act*.

## Step-zero: Activation & the Aha moment

- **Aha moment** — the first action where the user experiences the product's core value (Dropbox: put a
  file in a synced folder; a habit app: log day 1). Find it by looking at what early actions separate
  users who stick from those who churn.
- **North Star Metric** — the single metric that best captures value delivered (e.g. "accounts that
  hit the key action in week 1"), a *leading* indicator of retained revenue, not a vanity count
  ([Amplitude](https://amplitude.com/blog/product-north-star-metric)).
- **Activation** = getting a new user to the Aha moment **on their own**, via onboarding/UX — not via
  the founder hand-holding each signup. Automating activation is what removes the founder from the loop.

## Retention: the gate (read the curve)

Plot the retention curve (% of a cohort still active over time). Two shapes:

- **Flattens to a stable plateau** → you have a retained base; acquisition will compound. *Green light.*
- **Decays toward zero** → a leaky bucket; acquisition only scales the leak. **Stop and fix the
  product/value** (loop back to `solo-model`/`forge`).

For a solo this gate is non-negotiable: you cannot manually plug churn at scale. Retention is the
highest-leverage growth work *and* the cheapest — it costs nothing to acquire a customer you keep.

## Growth loops vs funnels

A **funnel** is linear: spend in → proportional output → no compounding. A **growth loop** is a closed
system where the output of one cohort becomes the input that acquires the next, so growth compounds
([Reforge / Brian Balfour](https://www.reforge.com/blog/growth-loops)). The automatic engine is a loop.

**Loop types (pick one to start):**

- **Content / SEO loop** — you (or users) create content → it ranks/gets shared → attracts users → who
  create more indexable content or links → which attracts more. Slow to start, compounds, ~free; great
  solo default.
- **Viral / referral loop** — users invite users. Measured by the **k-factor** (invites sent ×
  conversion rate); k > 1 is self-sustaining (rare), but even k = 0.3 meaningfully lowers blended CAC.
  Only works if there's a *natural* reason to share or invite.
- **Paid loop** — revenue funds ads → acquire customers → their revenue funds more ads. "Automatic" and
  fast, but only viable when the unit economics below clear; otherwise it burns cash.
- **Sales-assisted self-serve** — self-serve signup with light *automated* nudges and occasional human
  touch on the biggest accounts (the bridge between `solo-grow` and `solo-sell`).

Channel selection itself (which channel to even try) is the Bullseye/Traction job (Weinberg & Mares,
*Traction*, 2015: brainstorm 19 channels → test 3–4 cheaply → focus on the winner) — largely
`solo-distribute`'s domain. `solo-grow` takes the *automatable* winner and turns it into a measured loop.

## Unit economics (the licence to scale paid)

You cannot run an engine you can't measure. The core numbers:

- **CAC** — fully-loaded cost to acquire one paying customer in a channel (ad spend + tools + your time
  if relevant), per channel.
- **LTV** — gross-margin lifetime value of a customer (margin × average lifetime). Use *gross margin*,
  not revenue.
- **LTV:CAC** — the efficiency ratio. **Benchmark ≈ 3:1 minimum** (reported median B2B SaaS ~3.2–3.6:1;
  elite 4–5:1+). Below ~3:1, you're acquiring unprofitable customers
  ([Fiscallion](https://www.fiscallion.io/blog/ltv-to-cac-ratio-for-saas-what-good-looks-like-and-what-to-do-when-it-doesnt)).
- **CAC payback period** — months to recover CAC from a customer. **< 12 months** is a common healthy
  bar; 12–18 acceptable for high-LTV/enterprise; > 18 signals broken economics. (2025 private-B2B-SaaS
  *median* reportedly ~20 months, up from the historical 12–14 — i.e. the bar has gotten harder)
  ([Proven SaaS](https://proven-saas.com/blog/saas-cac-benchmarks-2025)).

> **For a solo specifically:** payback matters more than the ratio, because you fund CAC from *your own
> cash*. A 5:1 LTV:CAC with a 24-month payback can still bankrupt a solo who can't float the gap. Keep
> payback inside the runway you can actually carry.
>
> *All figures above are point-in-time benchmarks from this research and vary by source/segment —
> re-verify before relying on them, and never present a remembered number as a current fact.*

**The rule:** free/product loops (content, referral) can run before the math is perfect; **paid
acquisition only switches on once LTV > CAC with an affordable payback.** Paid amplifies working
economics — it never fixes broken ones.

## The self-serve funnel + lifecycle automation

Remove the founder from the path:

- **Funnel:** landing → signup → activation (Aha) → paid conversion → expansion. Measure conversion at
  each step; fix the biggest leak first.
- **Lifecycle automation:** automated onboarding sequence, activation nudges, trial-conversion emails,
  dunning (failed-payment recovery), and win-back — the automated version of the follow-ups a founder
  would otherwise do by hand. This is where solo leverage compounds (see `solo-sustain`).
- **Self-serve checkout:** the customer can buy without talking to you. If they can't, it's not a
  self-serve growth motion — it's `solo-sell`.

## How to iterate

Instrument AARRR + the North Star, find the **one** step leaking the most value (the binding
constraint), fix it, re-measure, repeat. One constraint at a time beats ten half-fixes — the same
focus discipline as everywhere else in the solo track.
