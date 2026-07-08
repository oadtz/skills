# Solo — a 6-skill solopreneur business pipeline

A loosely-coupled set of skills that take a validated idea and turn it into a **one-person business
that makes money and lasts** — by deciding how it earns, funding it with minimal dilution, getting
attention, closing paying customers, automating growth, and running it solo without burning out.

Solo is the **commercial sibling** of [ideakit](ideakit-README.md) and [forge](forge-README.md).
Where ideakit decides *what* to build and forge builds it *well*, solo answers the business
questions neither of them touches: *how does this make money, how do I pay to build it, how do people
find it, and how do I run it alone for years?* It runs **alongside** the forge build track, not after
it — you figure out the model and start distribution while the product is still being built.

```
ideakit-generate → explore → validate → │ → forge-architect → design → build → ship   (build the product)
                                         │
                              PRD/PLAN.md │ → solo-model → solo-fund → solo-distribute → solo-sell → solo-grow → solo-sustain
                                         │     how it       fund it      get             close       automate    run it
                                         │     earns        (min         attention       deals       + scale     solo,
                                         │                  dilution)                                             long-term
```

## The six skills

| Order | Skill | Use it when… | Output |
|---|---|---|---|
| 1 | **solo-model** | you have a validated idea and need to decide how it makes money | revenue model + offer + starting price + first-revenue path |
| 2 | **solo-fund** | you need to pay to build it and want to give up as little as possible | a funding plan on the cheapest justified rung |
| 3 | **solo-distribute** | you need attention and a repeatable channel to be found | one-channel go-to-market + audience motion + weekly cadence |
| 4 | **solo-sell** | people see it but don't buy — you need to close the first paying deals by hand | founder-led sales motion + objection answers + a repeatable playbook |
| 5 | **solo-grow** | you want acquisition to scale automatically, without selling each customer | a growth engine: loop + self-serve funnel + unit economics |
| 6 | **solo-sustain** | running it alone is becoming (or will become) unsustainable | operating plan: leverage list, calm-company defaults, guardrails |

## How to use

- **Full journey**: hand a PRD from `ideakit-validate` to `solo-model`, then climb model → fund →
  distribute → sell → grow → sustain. Each skill states where it sits and points to its neighbors.
- **Jump in anywhere**: already know the model and just need money? go to `solo-fund`. No one's finding
  it? `solo-distribute`. People look but don't buy? `solo-sell`. Want acquisition to run itself?
  `solo-grow`. Drowning in support/ops? `solo-sustain`.
- **The three acquisition lanes** (distribute / sell / grow): `solo-distribute` gets the right people to
  *find* you (organic channel/audience); `solo-sell` *converts* them *by hand* (founder-led sales, for
  high-touch deals); `solo-grow` makes acquisition *automatic and scalable* (self-serve funnel, growth
  loop, unit economics, for low-touch/high-volume). Do things that don't scale first (sell), then
  systematize what repeats into an engine (grow).
- **Loop, don't just flow**: `solo-sustain` is a maintenance loop you return to, and several
  sustainability or fundability problems are really *model* problems — so the track loops back to
  `solo-model` on purpose.

## The one idea behind the whole family

**For a solo founder the binding constraint is not ideas or even capital — it is the founder's own
finite time, leverage, and stamina.** So every solo decision is chosen to maximize leverage per
founder-hour and to avoid irreversible commitments (dilution, headcount, burnout). Two recurring
failure modes anchor the whole track: **a product nobody finds or buys**, and **a founder whose
operating load becomes unsustainable**. Re-fetch current survey figures before quoting them. Each skill
is one application of that idea:

| Stage | The failure it guards against | The governing principle |
|---|---|---|
| solo-model | building something that's slow to pay or impossible to run solo | *Pick the model that pays the soonest with the least to build and operate.* |
| solo-fund | giving up control/cash you didn't need to, for money you didn't need | *Keep the cap table and obligations as empty as the business allows.* |
| solo-distribute | a great product no one ever finds | *Distribution is the product's twin; one channel deep beats five shallow.* |
| solo-sell | attention that never converts to paying customers | *Selling is learning sold one conversation at a time; chase repeatability, not one-off revenue.* |
| solo-grow | pouring acquisition into a leaky bucket / buying growth you can't afford | *Retention before acquisition; loops compound where funnels don't; paid only when LTV > CAC pays back fast.* |
| solo-sustain | the founder burning out and taking the business with them | *The founder is the single point of failure — protect the asset; systems before headcount.* |

## Design notes

- **Single responsibility + loose coupling.** Each skill does one job; the handoff text in each
  `SKILL.md` is the connective tissue. Same design DNA as ideakit and forge — each stays under the
  ~500-line norm and is iterable independently.
- **Evidence-driven and skeptical.** Defaults are grounded in documented solopreneur/indie-hacker
  practice (Stairstep, bootstrapper funding instruments, distribution as a recurring failure mode,
  burnout as an operating risk) and the human always makes the call. Funding terms and named programs
  change constantly, so `solo-fund` tells you to verify current terms rather than trusting a remembered
  fact.
- **Shared anti-hallucination guard.** All six skills read **[solo-grounding.md](solo-grounding.md)**
  before stating any external fact (prices, funding terms, channel/market stats, tool facts):
  source-or-tag every claim, re-fetch time-sensitive numbers, stay decisive. It's the family's own
  guard — self-contained, not shared across other skillsets — so `solo-*` stays standalone.
- **Shared craft bar for customer-facing words.** Grounding keeps the facts honest;
  **[solo-craft.md](solo-craft.md)** keeps the words human. The skills that draft copy a prospect
  will read (`solo-model`'s offer, `solo-distribute`'s posts, `solo-sell`'s outreach, `solo-grow`'s
  funnel/lifecycle emails) run it before delivering: no cold-email or marketing-copy centroid, real
  personalization or none, and the read-aloud test — copy the founder would actually say out loud.
- **Runtime-agnostic.** Skills name capabilities by intent — user input, research, file/artifact
  output, connector/registry lookups — not one agent's tool names. Host-specific tools are adapters.
- **Care for the person.** `solo-sustain` treats founder wellbeing as a first-class operational
  concern and never endorses self-destructive overwork — a calm, durable business is the goal.
- **Naming.** `solo-<role>` — role-based so order and function are obvious at a glance, matching the
  `ideakit-<role>` / `forge-<role>` convention. These local copies are the source of truth.

## Optional next step

If you want a single "validated idea → running solo business" entry point, add a thin orchestrator
command (e.g. `/idea-to-solo-business`) that calls the six stages in sequence — without merging them.
