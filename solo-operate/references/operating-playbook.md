# Operating playbook — mechanics per duty

Point-in-time defaults (fees, thresholds, laws change): fetch current facts in the founder's
market before quoting, per `../../solo-grounding.md`. Named providers are examples, not
endorsements.

## PSP vs merchant of record (Duty 1)

| | PSP (Stripe, Omise/Opn, …) | Merchant of record (Paddle, Lemon Squeezy, …) |
|---|---|---|
| Who sells legally | the founder | the MoR resells your product |
| Global VAT/sales tax | founder's problem (registrations, filings) | absorbed by the MoR |
| Fees | lower per-transaction | higher (the tax service is the product) |
| Payouts/currencies | broad | check founder's country support first |
| Control (checkout, invoicing, disputes) | full | constrained to their flow |
| Right default | local-market sales, services, high volume | solo software sold across borders |

Decision inputs: where customers are (tax exposure), product type (SaaS/digital fits MoR; services
usually don't), founder's appetite for tax admin, and whether the founder's country is supported
for payouts. Verify current fees and country lists this run. Whichever rail: separate business
account, automated monthly export, one reconciliation slot on the calendar.

## Entity and registration framing (Duty 2 — general information, not legal advice)

Stay simple until a trigger fires: meaningful liability exposure, a customer/contract that
requires an entity, hiring, outside investment, or the local VAT-registration threshold
approaching (Thailand: registered-business VAT threshold — fetch the current figure). Present:
sole proprietor vs company (liability shield, credibility, cost/admin overhead, tax treatment),
then route to one paid hour with a local accountant with the founder's numbers prepared. Do not
default to a US Delaware framing for a non-US founder; a US entity is a deliberate choice with
ongoing costs, made for specific reasons (US customers demanding it, US investors, US platforms).

## Terms + privacy floors (Duty 2)

**Terms of service**: what the product does and doesn't promise, acceptable use, payment/refund
policy (must match Duty 1), termination, liability limitation, governing law (founder's
jurisdiction unless there's a reason otherwise — note that consumer-protection law in the customer's
country often overrides both the chosen forum and liability caps). Draft from the real product, not
a template dump.

**Privacy**: start from the actual data inventory (analytics events, accounts, payment data,
support emails). Policy states: what's collected, why, where it's stored/processed, retention, how
to request deletion, contact. Regimes: PDPA applies to a Thai business; GDPR applies when offering
goods or services to people **in the EU** (it turns on where the data subject is, not nationality or
residency); add others only when the market mix says so. Solo-sized compliance: honest policy,
consent where required, a working deletion path, breach-notification awareness — not an enterprise
program. Flag high-risk data (health, minors, payments stored yourself) for professional review.

## Feedback tagging and prioritization (Duty 3)

Tag every item: `value` (product doesn't deliver/deliver enough) · `message` (wrong expectation
set) · `price` (worth-it doubt) · `bug` (works wrong) · `ops` (billing/policy friction). Count
recurrence per tag and segment; weight by segment worth, not loudness. Monthly output: top theme
per tag, one routed action each, and what was told back to the customers who raised it. Interview
rules: recent real behavior only ("walk me through the last time…"), no feature polls, the
cancellation interview is two questions ("what led you to cancel?" · "what would have had to be
true to stay?").

## Dunning and cancellation (Duty 4)

Dunning: rely on the provider's smart retries, then 2–3 emails over ~2 weeks (payment failed →
easy update link → access pauses on date X), written in the founder's voice per
`../../solo-craft.md` — most low-volume churn is failed cards. Cancellation: reason question
(taxonomy: involuntary / value / price / temporary) → one honest save offer matched to the reason
(pause for temporary, downgrade for price, a fix-commitment for value) → instant clean cancel +
confirmation. No guilt copy, no hidden buttons; exit experience is marketing to a future
returner.

## Monthly review template (Duty 5)

```
Month · MRR/revenue: [number, ±change] · New/expansion vs churned: [numbers]
Churn by reason: involuntary _ / value _ / price _ / temporary _
Cash: [balance] · Runway: [months] · Spend vs ceiling: [ok/over — cause]
Feedback themes: [top theme per tag → routed action]
Evidence level: E_ → E_ [what real payments/retention earned]
THE decision this month: [one loop-back: model / distribute / sell / grow / sustain / forge / none]
```

One page, thirty minutes, every month. If the founder skips two in a row, that's a solo-sustain
signal, not a paperwork failure.
