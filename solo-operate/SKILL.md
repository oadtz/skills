---
name: solo-operate
description: >
  Run the business side of a live product professionally — the commercial Day-2 layer. Use when the
  founder needs payments/checkout set up (Stripe vs merchant-of-record and the cross-border tax
  consequence), the legal floor (entity, terms of service, privacy policy, data-protection duties
  like PDPA/GDPR), a customer feedback loop (post-purchase interviews, support-ticket mining, churn
  exit interviews, feature prioritization), churn operations (dunning, cancellation flow, save
  offers), or a monthly business review (P&L, MRR, runway, decision). Triggers: "how do I take
  payments", "do I need a company / terms / privacy policy", "customers are cancelling", "what
  should I build next based on feedback", "how is the business actually doing". It is NOT for
  choosing the model (solo-model), getting attention (solo-distribute), closing deals (solo-sell),
  scaling acquisition (solo-grow), or founder workload/burnout (solo-sustain). It gives general
  information and localized defaults, not legal, tax, or financial advice.
---

# Solo — Operate (money plumbing, legal floor, feedback loop, monthly truth)

Read `../ai-engineering-foundation.md` if not already in context, and `../solo-grounding.md` before
stating any external fact — payment fees, tax thresholds, and legal requirements change constantly
and vary by country. Read `../solo-craft.md` before writing any copy a customer will read
(cancellation flows and dunning emails are customer-facing copy).

A business that earns money but runs on a personal bank account, no terms, no privacy policy, no
feedback loop, and no monthly numbers is a hobby with revenue. This skill installs the boring
professional layer that makes it a business — sized for one founder, in the founder's own country.

## The governing principle

**Professional is a floor, not a bureaucracy — and every rule is local.** Install the minimum
plumbing that protects money, data, and trust; automate it; review it monthly. Never assume the US
default: payments, taxes, entities, and privacy law depend on the founder's market (for a Thai
founder: Thai entity forms, VAT registration thresholds, and PDPA — not Delaware and CCPA). This
skill gives general information and defaults, then routes real legal/tax calls to a professional in
the founder's jurisdiction — clearly, without hedging away the useful defaults.

## Where this sits

```
solo-model → solo-fund → solo-distribute → solo-sell → solo-grow → solo-sustain
                                   └──────────── solo-operate (THIS) ────────────┘
     runs underneath the whole track from first revenue onward · forge-operate owns the technical twin
```

- First real revenue approaching (from solo-sell's pre-sell or solo-model's first-revenue path) →
  set up the money plumbing *before* the first invoice, not after.
- Churn or confused feedback appearing in solo-grow's retention gate → run the feedback loop here,
  then route what it finds: value problem → `ideakit-explore` / `forge-build`; message problem →
  `solo-distribute` / `solo-sell`; price/packaging problem → `solo-model`.
- Operating load from support, bookkeeping, and reviews → feeds `solo-sustain`'s time map.
- Evidence from real payments and retention → write back to the idea's plan/memory (E-levels rise
  or kill criteria fire on production truth, per `../ideakit-memory.md` when a location exists).

## Capability mapping

User input for jurisdiction/stage facts; web research (mandatory, per grounding) for current fees,
thresholds, and legal summaries in the founder's country; file output for the operating doc,
policies draft, and monthly review; connectors (payment provider, support inbox, analytics) when
available. Read `references/operating-playbook.md` for the mechanics of whichever duty runs.

## Workflow

Five duties. Run Duty 1–2 once at first revenue (then on change); Duties 3–5 are the standing loop.

### Duty 1 — Money plumbing (before the first invoice)

1. **How money arrives.** Decide payment rails deliberately: a PSP (e.g. Stripe, Omise/Opn for
   Thailand) where the founder is the merchant and owns tax duties, versus a **merchant of record**
   (e.g. Paddle, Lemon Squeezy) that resells the product and absorbs global VAT/sales-tax
   compliance — usually the right default for a solo founder selling software across borders, at
   the cost of higher fees and less control. Check current fees, payout currencies, and country
   support this run; the trade changes with the founder's product type and market mix.
2. **Separation.** A business bank account (or at minimum a fully separated account) from day one;
   every business flow goes through it.
3. **Invoicing and records.** Whatever the rail, ensure compliant invoices/receipts for the
   founder's country (Thai customers often need tax invoices) and a bookkeeping habit the founder
   will actually keep: automated export from the payment provider + a monthly reconciliation slot.
4. **Pricing localization hygiene.** Currency display, tax-inclusive vs exclusive pricing by
   market, and refund policy written down (it belongs in the terms below).

### Duty 2 — The legal floor (general information, not legal advice)

Install the minimum, in this order, localized to the founder's jurisdiction:

1. **Entity and registration** — when staying a sole proprietor is fine, when a company protects
   the founder (liability, contracts, hiring, investment), and what the local VAT/tax registration
   threshold is. Present the trade-off table, then: *verify with a local accountant before acting.*
2. **Terms of service + refund policy** — draft from what the product actually does (limits of
   liability, acceptable use, termination, refunds matching Duty 1's policy).
3. **Privacy** — inventory what personal data the product actually collects (forge-operate's
   analytics notes feed this), then draft a privacy policy that matches reality and the applicable
   regime: **PDPA** for a Thai-based business, **GDPR** when serving the EU, and the customer-side
   regimes the market mix implies. Consent, retention, deletion-request handling — sized to a solo
   product, not an enterprise program.
4. **The professional checkpoint** — one paid hour with a local accountant/lawyer to review the
   above beats weeks of forum research; stage the questions so that hour is efficient.

### Duty 3 — The feedback loop (what to build/fix next, from evidence)

Retention numbers say *that* something is wrong; only customers say *what*. Run a standing loop:

- **Listen where signal already exists**: support tickets, refund reasons, sales-call objections
  (from solo-sell), reviews, and usage analytics (from forge-operate) — mine and tag monthly.
- **Ask at the two honest moments**: shortly after value delivery ("what almost stopped you from
  buying?") and at cancellation (a two-question exit interview beats a survey). Mom Test rules from
  solo-sell apply — past behavior, not opinions about the future.
- **Prioritize by evidence, not loudness**: tag findings value / message / price / bug, count
  recurrence, weigh by segment worth, then route each to its owner (forge-build slice, distribute
  message, model pricing, operate policy). Write the decision down; tell the customers who asked.

### Duty 4 — Churn operations

- **Dunning**: automated retry + payment-update emails (craft bar applies — human, not threatening;
  most "churn" at low volume is failed cards, not decisions).
- **Cancellation flow**: one honest save offer (pause, downgrade, or fix-the-problem), the
  two-question exit interview, then a clean, instant cancel — dark patterns destroy the trust a
  solo brand runs on.
- **Churn taxonomy**: record every cancellation as involuntary / value / price / temporary; the
  monthly review reads this, not anecdotes.

### Duty 5 — The monthly truth (one page, one decision)

Once a month, produce the one-page review from the playbook: revenue/MRR and movement, churn by
reason, cash and runway, cost vs ceiling (with forge-operate's numbers), feedback-loop themes, and
**one decision** — the loop-back this month feeds (model, distribute, sell, grow, sustain, or
forge). Update the idea memory's evidence level from real payment and retention data. A business
the founder reads monthly cannot silently die.

## Execution

Install things, don't describe them: actually configure the payment provider (up to the
final go-live/spend click, which is the founder's), actually draft the terms/privacy documents as
files, actually set up the dunning emails and exit interview, actually write the monthly review.
Hard boundary per `../solo-execution.md`: contracts, filings, payments, and anything legally or
financially binding get explicit founder confirmation — prepare everything up to the signature.
Honesty per `../solo-grounding.md`: every fee, threshold, or legal claim is fetched this run or
tagged; jurisdiction-specific conclusions carry the "verify with a local professional" line.

## Reference files

- `references/operating-playbook.md` — mechanics: PSP vs merchant-of-record decision table,
  bookkeeping cadence, entity/registration trade-off framing, ToS/privacy drafting floors
  (PDPA/GDPR pointers), feedback tagging and prioritization, dunning/cancellation flows, and the
  monthly review template.
