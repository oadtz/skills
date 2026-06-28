# Solo — Grounding & anti-hallucination contract

Read this before stating any external fact in `solo-model`, `solo-fund`, `solo-distribute`,
`solo-sell`, `solo-grow`, or `solo-sustain`. It is the family-level guard that keeps the commercial
advice honest: the `solo-*`
skills hand founders **numbers that move money** — prices, funding terms, channel benchmarks, tool
features, program eligibility — and those are exactly the claims a model is most likely to invent or
to remember as stale. This file is self-contained on purpose; the `solo-*` family carries its own
guard and does not depend on any other skillset.

## The one rule

**Every external factual claim is either backed by a source you fetched this run, or it is visibly
tagged as an assumption. There is no third category.** A confident sentence with no source and no tag
is the failure mode this contract exists to kill.

## Grounding is not hedging — stay decisive

This contract makes claims *honest*, not *timid*. It must not turn the `solo-*` skills into
fence-sitters. Keep the decisiveness they're designed for:

- **Still commit.** Pick the concrete price, the one channel, the primary funding path — don't retreat
  to "it depends" or a vague range to dodge being wrong. Grounding governs *facts*, not *recommendations*:
  your judgment call stays a confident call.
- **Tag, don't suppress.** When evidence is thin, *label* the claim `[assumption]` and proceed — do
  **not** withhold the recommendation or stall the workflow waiting for perfect data. A tagged
  assumption the founder can act on and test beats silence.
- **Don't over-tag.** The founder's own inputs, your reasoning, and your recommendations are not
  external facts and need no source. Only genuinely checkable, founder-actionable external claims
  (prices, programs, stats, tool/platform facts) carry the source-or-tag rule.

The bar is: *be just as decisive as before, and now also honest about which parts are sourced.*

## What counts as a claim that must be grounded

Anything a founder could act on and be wrong about:

- **Prices / benchmarks** — "comparable tools charge $X–$Y/mo", "B2B tolerates higher", market rates.
- **Funding terms / programs** — RBF revenue-share %, SEAL caps, accelerator equity, grant eligibility,
  whether a named program (depa, NIA, NSTDA, TinySeed, a specific RBF provider) still exists and is open.
- **Channel / distribution stats** — "distribution is the #1 cited failure", typical conversion or
  traction numbers, where a specific buyer gathers.
- **Tool / platform facts** — what an automation or no-code tool can do, platform fees, API limits.
- **Burnout / market research figures** — any "surveys say X%", "most founders…", trend direction.

Founder-specific inputs (their runway, their skills, their stated goal) are not external claims — use
them directly. The user's own numbers are theirs to own.

## How to ground each claim

1. **Fetch, then state.** Use the host's web/search/browser for the claim, and put the source link
   right beside it. Prefer primary sources (the program's own page, the actual pricing page, the raw
   survey) over secondary summaries.
2. **Quantify from real signal, not vibes.** "Top complaint in r/X", "47 reviews mention Y", "this
   RBF provider's published rate is Z%" — not "people generally feel…".
3. **Demand evidence = behavior, not opinion (Mom Test).** For willingness-to-pay and channel-fit,
   weigh what people *did* (paid, switched, pre-ordered, churned) over what they *say* they'd do. Mark
   any "they said they'd pay" as unproven until real money confirms it.
4. **Separate the three voices.** Make it obvious which sentences are **fact** (sourced), which are
   **assumption** (to test), and which are **recommendation** (your judgment). Don't let a
   recommendation borrow the authority of an unsourced fact.

## Freshness — never serve a remembered number as a current fact

Time-sensitive claims must be **re-fetched every run**, never recalled from training:

- prices, fees, and willingness-to-pay benchmarks,
- funding instrument terms, eligibility, and **whether the program still exists**,
- platform/tool capabilities, limits, and pricing,
- "what's working now" channel tactics and any dated statistic.

If you state one of these, it carries a source from *this* run or an explicit `[verify current]` tag
with the date you'd expect it to drift. `solo-fund` already says it for funding terms — this
generalizes it to the whole family.

## When live research is unavailable

Do not fill the gap from memory. Instead:

- Label the whole output a **"non-current draft"** in one line at the top.
- Tag **every** price, funding, channel, tool, and market claim as `[assumption — verify before
  acting]`.
- Tell the user plainly what to verify and where, and route demand/price tests to `solo-distribute`
  (a small real experiment) rather than asserting.

## Verification gate (run before final output)

Before presenting the model decision / funding plan / GTM plan / operating plan, check:

- [ ] Every external number or named program has a **source link from this run** OR an `[assumption]`
      / `[verify current]` tag — no bare confident facts.
- [ ] Fact vs. assumption vs. recommendation is visually distinguishable.
- [ ] Willingness-to-pay and channel-fit are marked as hypotheses unless real behavior backs them.
- [ ] No remembered term, price, or eligibility is presented as current without a fresh check.
- [ ] (`solo-fund`) the "general information, not financial/legal advice" reminder is present.

If any box fails, fix it before sending — a smaller, honestly-hedged answer beats a confident wrong one.

## Not advice

The `solo-*` skills give general information and trade-offs to inform the founder's own decision. They
do not give individualized financial, investment, tax, or legal advice. For a specific deal, tell the
user to read the actual terms and consult a qualified professional.
