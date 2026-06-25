# Solo — a 4-skill solopreneur business pipeline

A loosely-coupled set of skills that take a validated idea and turn it into a **one-person business
that makes money and lasts** — by deciding how it earns, funding it with minimal dilution, getting
the first customers, and running it solo without burning out.

Solo is the **commercial sibling** of [ideakit](ideakit-README.md) and [forge](forge-README.md).
Where ideakit decides *what* to build and forge builds it *well*, solo answers the business
questions neither of them touches: *how does this make money, how do I pay to build it, how do people
find it, and how do I run it alone for years?* It runs **alongside** the forge build track, not after
it — you figure out the model and start distribution while the product is still being built.

```
ideakit-generate → explore → validate → │ → forge-architect → design → build → ship   (build the product)
                                         │
                              PRD/PLAN.md │ → solo-model → solo-fund → solo-distribute → solo-sustain
                                         │     how it       fund it      get             run it
                                         │     earns        (min         customers       solo,
                                         │                  dilution)                    long-term
```

## The four skills

| Order | Skill | Use it when… | Output |
|---|---|---|---|
| 1 | **solo-model** | you have a validated idea and need to decide how it makes money | revenue model + starting price + first-revenue path |
| 2 | **solo-fund** | you need to pay to build it and want to give up as little as possible | a funding plan on the cheapest justified rung |
| 3 | **solo-distribute** | you need the first paying customers and a repeatable channel | one-channel go-to-market + audience motion + weekly cadence |
| 4 | **solo-sustain** | running it alone is becoming (or will become) unsustainable | operating plan: leverage list, calm-company defaults, guardrails |

## How to use

- **Full journey**: hand a PRD from `ideakit-validate` to `solo-model`, then climb model → fund →
  distribute → sustain. Each skill states where it sits and points to its neighbors.
- **Jump in anywhere**: already know the model and just need money? go to `solo-fund`. Built it but no
  one's buying? go to `solo-distribute`. Drowning in support/ops? go to `solo-sustain`.
- **Loop, don't just flow**: `solo-sustain` is a maintenance loop you return to, and several
  sustainability or fundability problems are really *model* problems — so the track loops back to
  `solo-model` on purpose.

## The one idea behind the whole family

**For a solo founder the binding constraint is not ideas or even capital — it is the founder's own
finite time, leverage, and stamina.** So every solo decision is chosen to maximize leverage per
founder-hour and to avoid irreversible commitments (dilution, headcount, burnout). The two facts that
anchor the whole track: **distribution — not product — is the #1 reason solo products fail**, and
**burnout is the #1 predictor of solo-founder failure.** Each skill is one application of that idea:

| Stage | The failure it guards against | The governing principle |
|---|---|---|
| solo-model | building something that's slow to pay or impossible to run solo | *Pick the model that pays the soonest with the least to build and operate.* |
| solo-fund | giving up control/cash you didn't need to, for money you didn't need | *Keep the cap table and obligations as empty as the business allows.* |
| solo-distribute | a great product no one ever finds | *Distribution is the product's twin; one channel deep beats five shallow.* |
| solo-sustain | the founder burning out and taking the business with them | *The founder is the single point of failure — protect the asset; systems before headcount.* |

## Design notes

- **Single responsibility + loose coupling.** Each skill does one job; the handoff text in each
  `SKILL.md` is the connective tissue. Same design DNA as ideakit and forge — each stays under the
  ~500-line norm and is iterable independently.
- **Evidence-driven and skeptical.** Defaults are grounded in documented solopreneur/indie-hacker
  practice (Stairstep, bootstrapper funding instruments, distribution-as-#1-problem, burnout as the
  top failure predictor) and the human always makes the call. Funding terms and named programs change
  constantly, so `solo-fund` tells you to verify current terms rather than trusting a remembered fact.
- **Runtime-agnostic.** Skills name capabilities by intent — user input, research, file/artifact
  output, connector/registry lookups — not one agent's tool names. Host-specific tools are adapters.
- **Care for the person.** `solo-sustain` treats founder wellbeing as a first-class operational
  concern and never endorses self-destructive overwork — a calm, durable business is the goal.
- **Naming.** `solo-<role>` — role-based so order and function are obvious at a glance, matching the
  `ideakit-<role>` / `forge-<role>` convention. These local copies are the source of truth.

## Optional next step

If you want a single "validated idea → running solo business" entry point, add a thin orchestrator
command (e.g. `/idea-to-solo-business`) that calls the four stages in sequence — without merging them.
