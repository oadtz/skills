---
name: solo-fund
description: >
  Decide HOW to fund building an idea as a solo founder while giving up as little ownership and as
  few obligations as possible — compare bootstrapping, pre-sales/crowdfunding, revenue-based
  financing, bootstrapper-friendly investors, accelerators, and grants, then produce a concrete funding
  plan. Use when a solopreneur asks "how do I fund this", "raise without giving up control", "bootstrap
  or raise", "how do I pay to build this", "what funding options exist", "is my idea fundable", or
  hands off a chosen model from `solo-model`. It is NOT for choosing the revenue model (use
  `solo-model`), acquisition/sales/growth (use `solo-distribute`, `solo-sell`, or `solo-grow`), or
  operations (use `solo-sustain`). It gives general information, not financial/legal advice.
---

# Solo — Fund (how to pay to build it, with minimal dilution)

Take a chosen business model — ideally from `solo-model` — and decide **how to fund the build while
keeping the cap table and the obligations as empty as the business allows.** Output is a concrete
funding plan: the primary path, the amount and what it buys, the cost (equity / repayment / strings),
and the trigger that would justify the *next* tier of funding.

This skill provides general information and trade-offs so the founder can decide. It is not financial,
investment, tax, or legal advice; for a specific deal, the user should consult a qualified
professional and read the actual terms.

## The governing principle (read first)

**Keep the cap table and the obligations as empty as the business allows; take outside money only to
buy speed or reach you genuinely can't get otherwise.**

For a solo founder, capital is rarely the real constraint — *time and leverage* are. Most solo
businesses can and should be funded by the founder's own runway plus early revenue, because every
external dollar carries a cost that compounds: equity is permanent, debt and revenue-share are
obligations that must be serviced from cashflow you may not have yet, and investor money imports
expectations (growth, exit) that can quietly convert a calm solo business into a startup that *must*
hyper-scale. Three consequences, all the same principle:

1. **Default to bootstrapping.** It is the cheapest capital that exists and the only kind with zero
   strings. Exhaust founder runway + revenue + non-dilutive options before considering dilution.
2. **Climb the cost ladder only when a tier is justified.** Funding sources rank by cost-to-the-
   founder: personal runway → revenue/pre-sales → grants → revenue-based financing → shared-earnings →
   priced equity. Move up one rung only when a specific, named need (speed, a build you can't
   self-fund, a window that closes) justifies the added cost — never for vanity or "because you can."
3. **Match the funding to the model's shape.** Recurring revenue can service revenue-based financing;
   a one-off product can't. A SaaS with growth potential fits TinySeed; a calm lifestyle business
   doesn't. The right instrument depends on what `solo-model` chose — don't force a mismatch.

## Where this sits in the pipeline

```
solo-model (model + price)  →  solo-fund (THIS)  →  solo-distribute  →  solo-sell  →  solo-grow  →  solo-sustain
                               how to fund it        get attention       close deals   automate     run it solo
```

- If the user hasn't chosen a **revenue model** yet, send them to `solo-model` first — the model
  determines which funding instruments even fit.
- If the user is already funded (or committed to pure bootstrapping) and needs customers, go to
  `solo-distribute`.
- This stage ends when the user has a primary funding path, knows its cost, and approves it.

## Host capability mapping

- **User input**: ask one concise question at a time; use structured choices if the host supports them.
- **Research**: use the host's web/search/browser to check *current* terms, eligibility, and whether a
  named program (a specific accelerator, fund, RBF provider, or grant) still exists and is open —
  these change constantly, so verify rather than assert from memory.
- **No live research**: present the option types and their general trade-offs, and explicitly tell the
  user to verify current terms and availability before acting.
- **File output**: write the funding plan to a file/artifact if supported; else deliver it in chat.

**Grounding:** before stating any funding term, rate, equity stake, or program (RBF %, SEAL cap,
accelerator equity, grant eligibility, whether a named program still exists), follow
`../solo-grounding.md` if present — source-or-tag every claim and re-fetch these constantly-changing
facts, never assert a remembered term as current. It generalizes the "verify current terms" rule this
skill already holds; it does not make you less decisive about the primary path you recommend.

## Workflow

Four steps: **Assess the need → Map options to the model → Recommend a primary path → State the cost
and the next-tier trigger.**

### Step 1 — Assess the real need (do you need outside money at all?)

Many solo founders raise when they shouldn't. Establish:

- **How much, and for what specifically?** "To build the MVP" is vague — break it into the few real
  cash costs (your living runway, any unavoidable tooling/contractor spend). Most software MVPs need
  far less cash than founders assume; the main cost is the founder's time.
- **Runway**: months the founder can self-fund. **Time**: full-time vs nights/weekends.
- **Can the model pay for itself early?** If `solo-model` chose a service or pre-sellable product, the
  business may fund its own build — flag this before discussing any external money.

If the honest answer is "I can bootstrap this," say so plainly and skip to the plan. Don't manufacture
a funding need.

### Step 2 — Map options to the model

Read `references/funding-options.md`. Walk the cost ladder from cheapest to most expensive and keep
only the options that *fit the model and stage*:

- **Bootstrapping** (founder runway + reinvested revenue) — cheapest, zero strings; the default.
- **Pre-sales / crowdfunding** (presell, lifetime deals, Kickstarter) — funding + validation at once,
  no dilution; best when there's something concrete to promise. Often the smartest first "raise."
- **Grants / competitions + platform/AI credits** (gov, foundation, platform funds; in Thailand e.g.
  depa, NIA, NSTDA; US SBIR/STTR) — non-dilutive cash; and **stack free AI/cloud credits** (AWS/Google/
  Azure/NVIDIA) for runway, which in an AI-heavy build can beat a small raise.
- **Invoice financing / factoring** — borrow against unpaid B2B invoices; non-dilutive cashflow bridge
  for slow-paying (enterprise/gov) clients. Not growth capital.
- **Revenue-based financing (RBF)** — capital repaid as a % of revenue; no equity. Needs *existing,
  fairly steady* revenue, so it's an accelerant, not a starter. Mismatched to one-off products.
- **MRR/ARR-backed credit facilities & venture debt** — borrow against recurring revenue at scale
  (cheaper than RBF, more institutional); needs steady MRR. Debt, not equity (venture debt adds warrants).
- **Shared-earnings (SEAL, e.g. Earnest-Capital-style)** — investor capital repaid from profit before
  founder pay, with a capped buy-back; designed for bootstrappers who don't plan a classic exit.
- **Bootstrapper accelerators (TinySeed-style)** — modest capital for a small permanent equity stake,
  built for SaaS aiming at 7–8 figures (not lifestyle-scale businesses).
- **Equity crowdfunding (Reg CF / Reg A+)** — sell equity to the crowd via a platform (WeFunder/
  StartEngine); dilutive but no single VC gatekeeper. Needs a consumer-relatable story + an audience.
- **Priced equity (angel/VC)** — most expensive in control and expectations; imports a growth/exit
  mandate. Rarely the right fit for a true solo/lifestyle business; appropriate only when the plan is
  genuinely venture-scale and the founder wants that path.

(See `references/funding-options.md` for the full 0–9 ladder with costs, requirements, and watch-outs,
including the niche web3/RetroPGF route.)

### Step 3 — Recommend a primary path (+ a backup)

Recommend **one** primary path that's the lowest rung clearing the real need from Step 1, with a
one-line rationale, plus a backup. Be explicit when the answer is "you don't need to raise — bootstrap
it." If recommending an external instrument, point the user to verify current terms and eligibility
and to read the actual agreement (and get professional advice) before signing.

### Step 4 — State the cost and the next-tier trigger

Spell out what the path actually costs and when the *next* rung becomes justified:

> **Primary path**: [option] · **Amount / what it buys**: [x → the specific thing it unblocks]
> **Cost**: [equity % / repayment terms / time + strings] · **Backup**: [option]
> **Next-tier trigger**: "Consider [next rung] only once [specific, measurable condition]."
> Reminder: verify current terms/eligibility and read the agreement; this isn't financial or legal advice.
>
> Want me to hand this to **solo-distribute** to get the first customers (often the best "funding"
> there is), or back to **solo-model** if the model needs rethinking to be fundable/self-funding?

The user approves the funding path before moving on.

## Operating principles

- **Bootstrapping is the default, not the fallback.** It's the cheapest capital and the only kind with
  no strings; treat raising as the exception that must be justified.
- **Revenue is the best funding.** A paying customer is non-dilutive capital *plus* validation —
  always weigh "go get revenue" against "go raise money," and usually prefer the former.
- **Non-dilutive before dilutive.** Pre-sales and grants give you money without giving up the company;
  exhaust them before equity.
- **Dilution and obligations are mostly irreversible.** You can't un-sell equity or un-sign a
  repayment obligation. Treat the cap table like an architectural decision (see `forge-architect`'s
  "record irreversibly"): cheap to defer, expensive to undo.
- **Investor money imports a mandate.** Equity (and to a degree accelerators) expect growth and an
  exit. If the user wants a calm solo business, that mandate is a hidden cost — name it.
- **Honesty:** terms, eligibility, and even the existence of specific programs change constantly —
  verify current details, never present a remembered term as a current fact, and don't dress a costly
  instrument as "free money." Flag clearly that this is general information, not tailored advice.

## Execution

**Don't stop at the plan — execute it.** Once the founder has made the decisions this skill is built
around, build the real deliverables with the right tool (write the actual copy/spec/script/doc/asset,
run the analysis, do the research) instead of handing back advice. Stage anything that spends money,
acts from the founder's accounts, or is irreversible for their one-click approval. Full contract:
`../solo-execution.md`.

## Reference files

- `../solo-grounding.md` — the `solo-*` family's shared anti-hallucination guard: **read before
  stating any funding term, rate, or program**. Source-or-tag every claim, re-fetch
  constantly-changing terms, stay decisive. This is general information, not financial/legal advice.
- `references/funding-options.md` — the funding cost ladder for solo founders: each instrument, what
  it costs, what it requires, which revenue models it fits, and the watch-outs.
