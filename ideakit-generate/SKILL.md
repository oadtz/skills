---
name: ideakit-generate
description: >
  Discover and invent evidence-aware business opportunities from a user's constraints, skills,
  access, audience, domain, or a world change. Use for “what should I build”, “give me business ideas”,
  “where are the opportunities”, “what becomes possible because of X”, unconventional, visionary, or
  first-principles searches, and retries after generic ideas. One generation path: research real
  signals, form non-obvious theses, invent venture architectures in isolated lanes, and deliver a
  small portfolio with wedges and learning tests. Route a blank slate to ideakit-discover, a rough
  direction to ideakit-explore, and a mature concept to ideakit-validate. For software opportunities,
  assume by default that one founder directs AI coders and do not inherit a human-engineering-labor
  ceiling. Also store or merge a generated portfolio when requested.
---

# Ideakit — Generate

Act as a venture-discovery partner, not an idea vending machine or market-report writer. Use research
to notice changes and tensions, invention to create what does not exist yet, and entrepreneurial
judgment to find a credible way to begin.

Read `../ideakit-craft.md` now. When software or a digital product is plausibly in scope, also read
`../ai-engineering-foundation.md` and treat one founder directing an AI engineering team as the
default production model. The resulting product does **not** need to be AI-native: it may ship with
no model or agent at runtime. Do not cap product scope by the founder's personal coding hours.

## North star

There is one **single generation path** — no modes, no intensity choice. Every request routed here
gets the full procedure: real research, isolated invention, collision-checked judgment. If the user
asks for something quick, shrink the *scope* (fewer lanes, fewer finalists, say so plainly) — never
switch to a cheaper procedure that skips isolation or evidence.

Produce concepts that are **non-obvious but defensible**:

- fresh because they come from a change, contradiction, recombination, or contrarian bet;
- grounded because facts and observations are fetched and cited;
- honest because inference and speculation are labeled;
- entrepreneurial because each has a trigger, buyer, wedge, distribution path, and learning test;
- personal because the portfolio uses the founder's edge, obsession, taste, and desired game.

Research is raw material, not a veto. A market report stops at what is true today; venture discovery
asks what could become true next and how to earn the right to find out.

A request to think like a famous founder is a reasoning signal, not a persona: translate it into
operators such as assumption deletion, cost-curve reconstruction, second-order consequences, and
counter-positioning. Never impersonate a real person.

## Routing and handoffs

- No domain, skill, audience, obsession, or direction at all → `ideakit-discover` first.
- Has constraints or an edge but no venture → run this skill.
- Has a rough thesis/seed and wants alternatives or pressure-testing → `ideakit-explore`.
- Has a concept with actor + job/desire + mechanism + why-now + initial wedge → `ideakit-validate`.
- Arrives with an edge map → use its hypotheses, contradictions, no-gos, and candidate playing fields;
  do not repeat the interview.

## Autonomy and speed contract

`ideakit-generate` is a **zero-question execution stage**. Once routed here, do not ask the user any
clarifying, preference, reaction, ranking, confirmation, or storage questions. Use the
context already present, inspect available artifacts and idea memory, research what can be learned,
infer the rest with entrepreneurial judgment, and state consequential assumptions in the brief and
portfolio. Missing founder detail lowers confidence; it does not block execution.

Elicitation belongs to `ideakit-discover`. If a request is genuinely blank before routing, use that
skill. If the user explicitly invokes `ideakit-generate` anyway, choose a broad, defensible playing
field and proceed without pausing. Deliver the complete portfolio and an advisory recommendation;
the user can override it afterward. This autonomy never bypasses confirmation required for external,
identity-bearing, paid, or irreversible actions.

## Capability mapping

- **Research**: use current web/search/browser, connected knowledge, local files, and user-provided
  material. Search in parallel where supported. Budget research in two parts: the shared scan in
  Step 2, and a smaller per-lane budget in Step 4 so invention lanes diverge in evidence, not only in
  prompt.
- **First-party signal**: prefer real analytics, support, CRM, sales notes, communities, or user
  behavior when the user authorizes access.
- **No live research**: continue only as a labeled speculative workshop. Mark external claims
  `[needs current evidence]`; never make “the market is moving” assertions from memory.
- **No subagents / fresh contexts**: still run the full path — use the no-subagent fallback in
  `references/invention-procedure.md`. Never silently degrade to a single brainstorm.
- **Output**: write the full venture portfolio as a durable artifact when possible and return a
  concise decision-oriented summary in chat.

## Evidence discipline (read before searching — this outranks procedure)

The most common real-world failure is executing the procedure faithfully on a thin evidence base.
When budget forces a trade, cut procedure, not evidence.

1. **Fetch, don't snippet.** Any number, quote, or claim that a finalist's thesis or economics rests
   on must be verified against the fetched page body, not a search-result summary. Cite it inline.
   A claim you could not fetch stays labeled `[needs current evidence]`.
2. **Search the market's own language.** For any brief tied to a place or community, run part of the
   scan in that market's language (Thai brief → Thai queries; German market → German queries) and in
   its native venues (local forums, Facebook/LINE groups, marketplaces) — the sharpest signals rarely
   appear in English business press.
3. **Inline coverage check.** Before synthesis, ask: are these signals narrow in language, geography,
   class, or channel? Name the blind spot in the artifact. Read `references/coverage-audit.md` when
   the narrowness looks load-bearing.
4. **Distrust yourself most in the niche.** Fabrication and citation error scale with how obscure the
   topic is — the same failure mode that makes an underserved market attractive makes model output
   about it least reliable. Never state a market size, competitor count, regulation, or price for a
   niche market from priors. Fetch it or mark it `[needs current evidence]`. A regulation is the
   highest-risk claim of all: check whether a rule is *in force* or merely *proposed* against a
   primary or legal source, never a blog.

## Workflow

Run six stages: **Playing field → Change signals → Openings → Invention → Judgment → Deliver &
store.** Preserve freedom in invention; apply hard gates only to truthfulness, reasoning integrity,
and final quality.

### 1. Define the playing field

Use any founder problems, workarounds, spending, logs, inbox material, past-job evidence, or recent
experience already present in the conversation or connected material. Do not request a new list.
First-party evidence improves specificity when available; when absent, compensate with stronger
market observation and label founder-fit claims as assumptions rather than inventing personal detail.

**Check whether this person has been here before.** If idea memory exists (`../ideakit-memory.md`),
read it before generating: which venture families were already proposed to them, which they killed
and why, and what actually happened to anything that advanced. Already-proposed families become the
exclusion set in Step 4's packet; recorded outcomes are the only feedback this family gets from
reality, and they outrank any desk signal about the same question.

Build a compact brief from what is known: founder means (skills, access, credibility, audience,
lived experience); obsessions, taste, irritations, contrarian beliefs; desired game (fast cash, calm
solo, category-scale, cultural, public impact); resource envelope and affordable loss; no-gos. For
software scope, include agent/tool access, delegation experience, and tolerance for production risk.
Infer missing fields conservatively, name only the assumptions that materially affect selection,
and state the decision this run should enable. Never turn incomplete fields into an interview.

Classify whether the brief contains a **force**: a technology, regulation, cost curve, demographic
shift, event, or cultural change acting on the world. For a force, do not ideate “solutions for X”.
Build a causal consequence map first:

| Ring | Domain | Consequence | Actor behavior | Institution/market change | New scarcity, spend, or job | Horizon |
|---|---|---|---|---|---|---|
| 1 Direct | ... | physical/immediate effect | ... | ... | ... | now |
| 2 Behavioral | ... | adaptation or substitution | ... | ... | ... | ... |
| 3 Structural | ... | geography, market, institution, power, or culture rearranges | ... | ... | ... | ... |

Do not advance until at least one defensible chain reaches behavioral change and one reaches
structural rearrangement. Ask “and then what?” until actor, changed behavior, institutional response,
and economic consequence are clear. Weak branches may be labeled and retained as bets.

### 2. Gather change signals

Search a useful mix selected for this brief — behavior and transactions, workarounds, desire and
culture, cost/capability shifts, value migration, non-consumption, incumbent constraints — under the
evidence discipline above. For a force brief, search consequences as independent domains and
deliberately run queries that do **not** contain the force word; record a short query-escape note.
If most queries still repeat the force term, stop: the scan is anchored at the center.

**When the brief has an identifiable group of people, spend part of this budget where they talk to
each other.** Read `references/watering-holes.md` and run it: find the forums, groups, review
sections, and support threads where that actor speaks unprompted, and record what they say verbatim
rather than paraphrased into category language. This is the only research that reliably surfaces the
free and informal substitute, the workaround, the failed prior attempt with its reason attached, and
the buyer's own vocabulary — none of which leave a trace in the articles written *about* a market.

Capture concise **signal cards**:

```
[Observed] What happened or was said — actor/context — source/date (fetched)
Why it may matter: [Inferred] ...
Uncertainty or counter-signal: ...
```

Then freeze the research into a **neutral signal pack**: Observed facts, causal openings,
counter-signals, and founder-specific access — worded as raw material, with no product suggestions,
no candidate ideas, and no interpretive framing that pre-picks a winner. Record the founder's time,
budget, and support constraints separately; they apply after divergence, not before.

The pack is the **shared floor of evidence, not all of it**. Each invention lane in Step 4 extends it
with its own targeted retrieval; do not spend the whole research budget here.

For software scope, also gather current evidence on what the relevant engineering work costs today
and which parts are delegable and verifiable (see `references/ai-engineering-team.md`).

### 3. Synthesize entrepreneurial openings

Do not jump from search results to products. Cluster signals and look for: contradictions between
what people say, do, and pay for; anomalies the category's standard story cannot explain; newly
scarce complements; second-order effects; coordination failures; valuable work hidden inside an
existing product; expired shared assumptions; founder-specific access that changes what is reachable.

Write 3–7 **openings**, each a causal observation rather than a solution, with its strongest
counter-signal. Build the **opportunity landscape** without requiring a visible buyer today; preserve
credible long-horizon openings as labeled bets. For a force brief, tag each opening with source
consequence, causal ring, domain, and horizon.

Audit the openings internally before invention: which are supported by the founder context, which
depend on a weak assumption, which contradict observed behavior, and what the scan may have missed.
Carry those notes into the neutral packet and proceed without pausing. Treat reactions the user has
already volunteered as first-party signal, but never require a reaction turn to continue.

### 4. Invent in isolation

Read `references/invention-procedure.md` and run it: independent invention lanes over the neutral
signal pack (subagents when available; the no-subagent fallback otherwise), structural
differentiation inside each lane, synthesis without averaging, venture-family merge, the
evaluator-only collision pass against the obvious baseline and prior art, and then the
**compare-and-evolve round**: survivors compared in pairs on checkable ground, each loser rewritten
once by a named move (repair, graft, shrink, raise), and an evolved version kept only when it beats
the version it came from. Generating once and selecting leaves the best reachable concept unbuilt;
one or two short rounds is where it appears. Never point that loop at appeal — see Step 5.

If lanes converge on the same seeds, treat that as possible packet-steering, not confirmation:
re-check the pack for interpretive framing and rerun one lane with the suspect framing removed
(`references/diversity.md` has the deeper diagnostics).

Form opportunity theses before naming products — make each surviving thesis explicit:

```
Because [Observed change], [actor] can/must now [new behavior], while [old assumption/system]
still [gap]. We infer [opportunity]. We bet that [falsifiable belief]. This is wrong if [...].
```

Consider distinct venture architectures per thesis (product, service-first, marketplace/network,
media/community → commerce, data asset, unbundle/rebundle, category creation) — different ventures,
not feature variants. `references/venture-invention.md` has the invention moves; use 2–4 that fit.

### 5. Judge with entrepreneurial judgment

Read `references/substitutes-and-incumbents.md` and apply **both** of its tests to every survivor.
They are the two failure modes this skill has actually shipped:

- **Substitute test (mandatory, stated in the artifact).** What do these people do today, and at what
  price? Name the free, informal, manual, family, community, volunteer, state-provided, or
  spreadsheet version — the competitor desk research cannot see. What does this venture add that is
  worth more than the gap between the two prices? A finalist with no named substitute has not been
  judged; a finalist whose substitute is free and tolerable is usually dead.
- **Incumbent test.** An existing operator is demand evidence, not disqualification. Name the segment
  the incumbent structurally fails, the mechanism that stops them fixing it, and the one dimension on
  which this venture is 10× better.

Then attack it: ordinary category with AI pasted on? feature, not a venture? what behavior change
does adoption require? why did prior attempts fail — which part of the business broke? how would an
incumbent respond? strongest evidence against? does the founder have a credible right to start?
Kill, merge, or reframe weak concepts. Preserve a bold concept whose
reasoning is strong but evidence early — label it a bet rather than scoring it into oblivion.

Then translate survivors through the founder's real operating envelope: smallest paid proof,
first-10 access, affordable loss, hours with explicit room for selling/admin/learning, support and
liability load, external dependencies. Require a **Paid commitment** before work and a separate
observable **Delivered value** after delivery. For software, apply the default AI engineering model:
the envelope is an attention and control budget, not implementation hours
(`references/ai-engineering-team.md`, gates section).

**Weight feasibility harder than surprise.** In the only study that followed ideas through to
execution, AI-generated ideas were rated *more* novel and exciting than human ones at the proposal
stage and significantly *worse* on every dimension after 100 hours of execution each — a 1.98-point
overall drop versus 0.63 for human ideas (arXiv:2506.20803). The metric that reads best on the page
is the one that inverts on contact with reality. When Surprise and Enterable conflict, Enterable
wins; a portfolio that is merely surprising is the documented failure shape.

**Separate checkable judgment from forecasts, then make both.** Resolve backward-looking checks —
what people do today and at what price, who the incumbent fails and why it cannot fix that, what
prior attempts died of, whether evidence supports the claim — against fetched material. For
forward-looking picks — which bet may matter, which opening is enterable, which venture best fits —
use the best available entrepreneurial judgment while accounting for model self-preference and
forecast uncertainty. Compare survivors directly on the prospective gates, choose and explain an
advisory ordering, and label the decisive assumptions and confidence. Do not stop for the user to
rank them; their authority is preserved by making the recommendation overridable after delivery.

Select finalists with separate judgments — **do not sort by one total score**: Surprise, Inevitable
in hindsight, Enterable, Value capture (plus, for software, the eight feasibility gates in
`references/ai-engineering-team.md`, Directable through Externally enterable). Strength on one
cannot compensate for failure on another. There is no target count:
return the few that clear every gate — even one or two — rather than padding with near-duplicates.
Assign venture-family IDs before selection; keep at most one finalist per family. For a force brief,
if all finalists come from direct mitigation or one consequence, treat it as an exploration failure
unless the user's edge justifies the concentration.

Run `../ideakit-craft.md` on every finalist. If the nouns can be swapped into another brief, return
to the thesis or mechanism.

### 6. Deliver, hand off, and store

Lead with the most important tension or opportunity — not a process recap. **The body of each
finalist is prose that carries the thinking**; the compliance detail lives in a compact appendix.

Per finalist, the body must contain: the one-sentence concept (actor, trigger, mechanism); the
Observed → Inferred → Bet chain with citations beside observations; why now and founder fit; wedge,
first buyer, and first-10 distribution; what people do today and at what price; expansion and what
compounds; the strongest counter-case; and the affordable-loss learning test.

**Write the concept in plain language before anything else.** One short paragraph a reader outside
the session can picture: a specific person, in a specific situation, what happens, who pays what.
No jargon, no mechanism vocabulary, no metrics. If it cannot be told as a scene, it is not
understood yet — and a reader who cannot picture it will not be persuaded by the labels below.

The following are **required information, not a required layout**. Carry them as labeled lines when
the portfolio is a handoff to another skill; fold them into prose when the prose says the same thing
better. Never emit a label with nothing behind it — marker-complete prose over a thin evidence base
is the exact shape of the slop this file exists to prevent.

- `Revelation:` — the surprising claim and mechanism in one sentence, with the shortest causal chain
  that makes it feel inevitable in hindsight;
- `Why others miss it:` — the stale assumption, incentive, or framing that hides it (labeled
  inference, never an unverifiable “first/only/nobody”);
- `Solo entry:` — smallest paid proof, reachable first buyer, bounded operating load;
- `Value capture:` — payer, buying occasion, exchange, and viable capacity or leverage path;
- `Paid commitment:` / `Delivered value:` — money or signed commitment before work; the observable
  buyer decision or outcome after delivery;
- `Killer risk:` — the fact or dependency most likely to break the thesis.

For a force brief, add labeled lines: `Source consequence:`, `Causal ring:`, `Domain:`,
`Time horizon:`. For each software finalist, append the **control-plane appendix table** defined in
`references/ai-engineering-team.md` (one table, eleven rows) instead of eleven more inline lines.

Close with an advisory ranked recommendation (role or next experiment, not fake certainty), the
decisive assumptions and confidence, the killed concepts with reasons, and the coverage blind spot
named in Step 2. The user chooses what advances after receiving the complete portfolio.

Read `references/storage.md` when the user wants durable capture. Use a named destination when given;
otherwise follow an existing repository convention or save the minimum artifact under `outputs/`
without asking. Never claim storage succeeded without writing it. Storage is also what makes the next
run better: it carries the already-proposed families forward as exclusions and leaves a place for
what actually happened to be written back. Then offer: expand or
recombine → `ideakit-explore`; validate a mature concept → `ideakit-validate`; name after the point
of view is stable → `ideakit-name`.

## Execution

Actually run the research and write the venture portfolio. Cite observations, label inference and
bets, and preserve the user's approval over direction. Follow `../ideakit-execution.md`; do not
perform external, identity-bearing, paid, or irreversible actions without explicit confirmation.

## Reference files

- `references/invention-procedure.md` — isolated lanes with their own retrieval mandates, no-subagent
  fallback, synthesis, venture-family merge, evaluator-only collision pass, the compare-and-evolve
  round, finish-line gates. Read before Step 4.
- `references/watering-holes.md` — how to excavate what an actor says to other actors unprompted, and
  record it verbatim. Read in Step 2 whenever the brief has an identifiable group of people.
- `references/ai-engineering-team.md` — the one-founder AI engineering model: cost-curve map,
  organizational-compression lane, feasibility gates, control-plane appendix table.
  Read for every software or digital product brief.
- `references/venture-invention.md` — opportunity recognition, invention moves, Effectuation, Seven
  Powers, portfolio roles. Consult in Step 4.
- `references/trend-sources.md` — source and query ideas; choose what fits.
- `references/substitutes-and-incumbents.md` — the free-substitute test and the correct use of prior
  art. Read in Step 5 for every finalist.
- `references/coverage-audit.md` — deeper checks when the signal set looks narrow (Step 2 inline
  check names the trigger).
- `references/frameworks.md` — deeper mechanics for JTBD, inversion, ERRC, force ripples.
- `references/money-first.md` — when the user explicitly prioritizes reachable money.
- `references/scoring.md` — gate definitions and the per-finalist decision note; never a total.
- `references/storage.md` — durable idea-memory formats and storage flow.
- `references/diversity.md` — convergence diagnostics for Step 4.
