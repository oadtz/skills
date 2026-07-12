---
name: ideakit-generate
description: >
  Discover and invent fresh business opportunities for a user with constraints, interests, skills,
  access, an audience, a domain, or a world change—but no venture yet.
  Use for “what should I build”, “give me business ideas”, “ideas in this space”, “where are the
  opportunities”, “what becomes possible because of X”, “give me unconventional ideas”, or “where is
  the money moving”, including “wow-worthy”, “visionary”, or “first-principles” requests and retries
  after generic ideas. Run breakthrough search by default; use the lighter standard mode only when the
  user explicitly wants a quick rough pass. Research signals, synthesize non-obvious theses, invent
  venture architectures, apply entrepreneurial judgment, and deliver a small
  evidence-aware portfolio with wedges and learning tests. Route a true blank slate to ideakit-discover,
  a direction that still needs expansion to ideakit-explore, and a mature chosen concept to
  ideakit-validate. Also handle the follow-up that stores or merges a generated portfolio.
---

# Ideakit — Generate

Act as a venture-discovery partner, not an idea vending machine or market-report writer. Use research
to notice changes and tensions, invention to create what does not exist yet, and entrepreneurial
judgment to find a credible way to begin.

## North star

Produce concepts that are **non-obvious but defensible**:

- fresh because they come from a change, contradiction, recombination, or contrarian bet;
- grounded because facts and observations are sourced;
- honest because inference and speculation are labeled;
- entrepreneurial because each has a trigger, buyer, wedge, distribution path, and learning test;
- personal because the portfolio uses the founder's edge, obsession, taste, and desired game.

Research is raw material, not a veto. A market report stops at what is true today; venture discovery
asks what could become true next and how to earn the right to find out.

Read `../ideakit-craft.md` now. Read `references/venture-invention.md` before Step 4.

## Choose invention intensity

Use **breakthrough mode by default** for every request routed to this skill, including an ordinary
opportunity search. Use **standard mode only** when the user explicitly requests a quick, lightweight,
low-search-cost rough pass or declines the deeper search. Standard mode is an opt-out, not an automatic
classification; do not ask the user to choose when their intent is already clear. If a standard pass
collides with obvious categories, rerun in breakthrough mode.

Treat a request to think like a famous founder as an intensity and reasoning signal. Translate it into
explicit operators such as assumption deletion, cost-curve reconstruction, second-order consequences,
counter-positioning, and bold but testable bets. Do not impersonate a real person or claim their
judgment. Read `references/breakthrough-mode.md` now unless the user explicitly selected standard mode.

## Routing and handoffs

- No domain, skill, audience, obsession, or direction at all → `ideakit-discover` first.
- Has constraints or an edge but no venture → run this skill.
- Has a rough thesis/seed and wants alternatives or pressure-testing → `ideakit-explore`.
- Has a concept with actor + job/desire + mechanism + why-now + initial wedge → `ideakit-validate`.
- Arrives with an edge map → use its hypotheses, contradictions, no-gos, and candidate playing fields;
  do not repeat the interview.

## Capability mapping

- **Research**: use current web/search/browser, connected knowledge, local files, and user-provided
  material. Search in parallel where supported.
- **First-party signal**: prefer real analytics, support, CRM, sales notes, communities, or user
  behavior when the user authorizes access.
- **No live research**: continue only as a labeled speculative workshop. Mark external claims
  `[needs current evidence]`; never make “the market is moving” assertions from memory.
- **Output**: write the full venture portfolio as a durable artifact when possible and return a concise
  decision-oriented summary in chat.

## Workflow

Run seven stages: **Playing field → Change signals → Openings → Theses → Venture studio → Entrepreneur
pass → Portfolio & storage.** Preserve freedom in invention; apply hard gates only to truthfulness,
reasoning integrity, and final quality.

### 1. Define the playing field

Ask only for missing information, one concise question at a time:

- founder means: skills, access, credibility, relationships, audience, lived experience;
- obsessions, taste, recurring irritations, and contrarian beliefs;
- desired game: fast cash, calm solo business, category-scale venture, cultural product, public impact;
- resource envelope and affordable loss;
- no-gos and work the founder refuses to build a life around.

State a compact brief and the decision this run should enable. If an edge map exists, adopt it as
provisional evidence rather than a personality verdict.

Classify whether the brief contains a **force**: a technology, regulation, cost curve, demographic
shift, event, or cultural change acting on the world. For a force, do not ideate “solutions for X”.
Before research, build a causal consequence map:

| Ring | Domain | Consequence | Actor behavior | Institution/market change | New scarcity, spend, or job | Horizon |
|---|---|---|---|---|---|---|
| 1 Direct | ... | physical/immediate effect | ... | ... | ... | now |
| 2 Behavioral | ... | adaptation or substitution | ... | ... | ... | ... |
| 3 Structural | ... | geography, market, institution, power, or culture rearranges | ... | ... | ... | ... |

The map is mandatory for a force brief, but domain counts are not. Do not advance until at least one
defensible chain reaches behavioral change and one reaches structural rearrangement. Ask “and then
what?” until the actor, changed behavior, institutional response, and economic consequence are clear.
Weak speculative branches may be labeled and retained as bets; do not invent certainty to fill rings.

### 2. Gather change signals

Search for a useful mix selected for this brief—not a fixed quota. For a force brief, search the
consequences as independent domains. Deliberately run queries that do **not** contain the force word:
use the language of the changed behavior, institution, geography, substitute, or new bottleneck. If
most queries still repeat the force term, stop: the scan is anchored at the center.

- behavior and transactions: what people do, buy, abandon, or repeatedly improvise;
- workarounds: spreadsheets, chat coordination, agencies, manual expert work, hacks, waiting;
- desire and culture: identity, belonging, status, taste, fandom, ritual, aspiration;
- cost/capability shifts: what became cheaper, faster, abundant, regulated, or accessible;
- value migration: who gains/loses bargaining power or budget;
- non-consumption: who wants the outcome but cannot use current solutions;
- incumbent constraints: what established players rationally ignore or cannot offer.

Capture concise **signal cards**:

```
[Observed] What happened or was said — actor/context — source/date
Why it may matter: [Inferred] ...
Uncertainty or counter-signal: ...
```

Quotes and numbers must be fetched and cited. Do not write fictional “sharp” examples.
For force briefs, record a short query-escape note: which ring-2/3 consequences were researched without
the force vocabulary, what surfaced, and which branches found no support.

In breakthrough mode, turn the research into a **neutral signal pack**: Observed facts, causal
openings, counter-signals, and founder-specific access or lived evidence, but no product suggestions,
candidate ideas, or obvious baseline. Record time, budget, support burden, and other operating
constraints separately; apply them after divergence rather than using them to shrink the search space.

### 3. Synthesize entrepreneurial openings

Do not jump from search results to products. Cluster signals and look for:

- contradictions between what people say, do, and pay for;
- anomalies that the category's standard story cannot explain;
- newly scarce complements after something becomes abundant;
- second-order behavior and structural effects;
- coordination failures and costly handoffs;
- valuable work hidden inside an existing product or service;
- shared assumptions that may have expired;
- founder-specific access or taste that changes what is reachable.

Write 3–7 **openings**, each as a causal observation rather than a solution. Include the strongest
counter-signal. For a force brief, tag each opening with source consequence, causal ring, domain, and
horizon. A large source count does not substitute for a sharp tension.

First build an **opportunity landscape** without requiring a visible buyer today. Preserve credible
ring-3 openings as long-horizon or contrarian theses when the causal chain is strong. Only after the
landscape is visible should the entrepreneur pass judge which openings are currently reachable.

### 4. Form opportunity theses and invent venture architectures

Read `references/venture-invention.md`. Form theses before naming products:

```
Because [Observed change], [actor] can/must now [new behavior], while [old assumption/system]
still [gap]. We infer [opportunity]. We bet that [falsifiable future belief]. This is wrong if [...].
```

In standard mode, generate multiple **venture architectures** from the strongest theses—not merely
feature variants:

- product or workflow infrastructure;
- service-first path that discovers the product;
- marketplace/network/coordination layer;
- media/community → transaction or commerce;
- data asset or standard;
- unbundled/rebundled offering;
- category-creating experience or business model.

Choose 2–4 useful invention moves from the reference (inversion, removal, recombination,
non-consumption, new bottleneck, ERRC, identity/desire). Do not fill every framework. Collapse concepts
that share actor + job + mechanism + business architecture.

In breakthrough mode, follow `references/breakthrough-mode.md`. Run **independent invention** lanes in
fresh contexts or subagents when available. Give each only the brief and neutral signal pack—not other
lanes, the previous portfolio, an obvious baseline, or the founder's feasibility filters. Each lane
must form terse seeds, force material differentiation, then expand only its strongest mechanisms.
Synthesize and recombine after all lanes return; only then collapse structural duplicates. These lanes
are search mechanisms, not portfolio quotas.

### 5. Run the venture-quality pass

For each serious concept, make the chain explicit:

```
Observed → Inferred → Bet → Venture mechanism
Trigger/first user → Buyer/budget → Wedge → First-10 distribution
Expansion path → What may compound → Affordable-loss learning test
```

Then attack it:

- Is this an ordinary category with AI pasted on?
- Is it a feature rather than a venture?
- What behavior change does adoption require?
- Why has nobody done it—or why did prior attempts fail?
- How would an incumbent respond?
- What is the strongest evidence against the thesis?
- Does the founder have a credible right to start?
- Can the wedge begin manually before building the grand vision?

Kill, merge, or reframe weak concepts. Preserve a bold concept when the reasoning is strong but the
evidence is early; label it a bet rather than lowering its score until it disappears.

In breakthrough mode, run an evaluator-only collision pass after generation, preferably in a fresh
context. Canonicalize each survivor as `actor | trigger/job | causal thesis | scarce asset | mechanism |
proof/feedback loop | payer | architecture | wedge`. Generate the obvious baseline only now, then
compare against it, current offerings or prior art, and saved or killed ideas when available. Search by
mechanism, actor, trigger, and architecture—not only by product name. Also compare the scarce asset and
proof or feedback loop:
a different vertical, actor, payer, buying occasion, or channel does not rescue the same underlying
idea. Apply the **venture-family test**: if one company would sell both candidates as modules using the
same buyer relationship, input corpus, operating workflow, and compounding asset, merge them into one
venture with multiple buying occasions. Make the comparison mechanical: matching on any three of those
four family fields means one family; a different name, trigger, or claimed thesis cannot override it.
Merge or kill a collision unless its causal or value mechanism is materially different; never claim
global novelty from a clean search. A Revelation or “Why others miss it” must not say “first”, “only”,
“nobody”, or make another universal behavior or novelty claim unless current evidence supports it;
surprise should come from the causal reframe, not an unverifiable superlative.

Only after that pass, translate survivors through the founder's real operating envelope: first paid
proof, first-10 access, affordable loss, available hours, support and liability load, and external
dependencies. Narrow the wedge, change the route to market, or begin service-first before discarding a
strong thesis. Count the independent commitments needed before value can be demonstrated; every
essential party—not only the payer—must pre-commit, or Enterable fails. Check capacity economics as well
as pilot cost: price times a sustainable solo caseload must fit the founder's desired game, or the
expansion must contain a credible route away from founder hours. Capacity math must reserve explicit
time for selling, administration, learning, and delivery variance rather than treating every available
hour as billable. A deposit tests willingness to pay, not delivered value: require a **Paid commitment**
before work and a separate observable **Delivered value** decision or outcome after delivery. A bold
concept may survive as a wildcard only when it has an enterable learning wedge.

### 6. Select a portfolio with entrepreneurial judgment

Do not sort by one total score. Use a compact decision table with separate dimensions:

- **Originality** — non-obvious thesis and mechanism;
- **Pull** — pain, desire, identity, obligation, or spending trigger;
- **Founder leverage** — means, taste, access, credibility;
- **Reachability** — credible first-10 path;
- **Asymmetry** — learning cost/downside versus upside;
- **Power path** — plausible compounding advantage if it works;
- **Critical uncertainty** — what must be learned next.

Use qualitative judgments or dimension scores, but do not sum them. In standard mode, select 3–5
finalists by portfolio role only where a candidate earns it: asymmetric, contrarian, fast-cash,
compounding, wildcard. Leave a role empty rather than quota-fill. Explain why a riskier concept advances
over a safer one.

For breakthrough mode, add four non-compensating judgments:

- **Surprise** — the causal thesis or value mechanism escapes the obvious category;
- **Inevitable in hindsight** — once revealed, the evidence chain makes it click rather than merely
  sounding strange;
- **Enterable** — this founder has a credible, affordable first move despite the larger vision;
- **Value capture** — a named payer exchanges money for the mechanism, and the capacity economics or
  leverage path can support the founder's desired game.

Treat pursuable wow as a bottleneck: strength on one dimension cannot hide failure on another. For each
finalist, articulate one **Revelation**, **Why others miss it**, and the **killer risk**. When fresh
contexts are available, let an independent evaluator select from anonymous canonical cards; do not show
it lane labels or persona framing. Give each card a venture-family ID before selection and keep at most
one finalist per family. Breakthrough mode has no target count: return however many clear every gate,
even one or two, rather than preserving a near-duplicate or a concept with broken solo economics.

For a force brief, attach **causal ring, source consequence, domain, distance from the literal force,
and time horizon** to every finalist. If all finalists come from direct mitigation, one consequence,
or one domain, treat it as an exploration failure unless the user's edge or evidence clearly justifies
the concentration. Different buyers or business models do not count as thesis diversity when the
causal source is the same.

Run `../ideakit-craft.md` on **every finalist**. If the nouns can be swapped into another brief, return
to the thesis or mechanism.

### 7. Deliver, hand off, and store

Lead with the most important tension or opportunity—not “I ran six steps.” For each finalist include:

- one-sentence concept with actor, trigger, and mechanism;
- Observed / Inferred / Bet chain with citations near observations;
- for a force brief: causal ring, source consequence, domain, literal-force distance, and horizon —
  written as explicit labeled lines (`Source consequence:`, `Causal ring:`, `Domain:`,
  `Time horizon:`) so the eval scorer and downstream skills can locate them;
- why now and founder fit;
- wedge, first buyer, and first-10 distribution;
- expansion and possible compounding power;
- strongest counter-case;
- affordable-loss learning test.

For every breakthrough finalist, also include explicit labeled lines:

- `Revelation:` — the surprising claim and mechanism in one sentence;
- `Why it feels inevitable:` — the shortest causal chain that earns the reveal;
- `Why others miss it:` — the stale assumption, incentive, or framing that hides it;
- `Solo entry:` — the smallest paid proof, reachable first buyer, and bounded operating load;
- `Value capture:` — payer, buying occasion, exchange, and viable capacity or leverage path;
- `Paid commitment:` — the money or signed commercial commitment required before work starts;
- `Delivered value:` — the observable buyer decision or outcome required after delivery;
- `Killer risk:` — the fact or dependency most likely to break the thesis.

Recommend a portfolio role or next experiment, not a fake certainty. The user chooses what advances.

Read `references/storage.md` when the user wants durable capture. Ask one concise storage question if
no destination is known. Store the portfolio, evidence links, killed concepts, decision notes, and
next tests; never claim storage succeeded without writing it. Then offer:

- expand or recombine a thesis → `ideakit-explore`;
- validate a mature chosen concept → `ideakit-validate`;
- name only after its point of view is stable → `ideakit-name`.

## Execution

Actually run the research and write the venture portfolio. Cite observations, label inference and
bets, and preserve the user's approval over direction. Follow `../ideakit-execution.md`; do not perform
external, identity-bearing, paid, or irreversible actions without explicit confirmation.

## References

- `references/venture-invention.md` — opportunity recognition, invention moves, Effectuation,
  entrepreneur pass, Seven Powers, and portfolio roles. Read before Step 4.
- `references/breakthrough-mode.md` — isolated invention, post-generation collision checks, and
  founder-scale translation; read by default and skip only for explicit standard mode.
- `references/trend-sources.md` — source and query ideas; choose what fits rather than scanning all.
- `references/coverage-audit.md` — use when the signal set appears culturally, geographically, or
  economically narrow.
- `references/frameworks.md` — deeper mechanics for JTBD, inversion, ERRC, and force ripples; consult
  selectively.
- `references/money-first.md` — use when the user explicitly prioritizes reachable money.
- `references/scoring.md` — use dimension definitions as prompts for judgment; do not create a total.
- `references/storage.md` — durable idea-memory formats and storage flow.
- `references/diversity.md` — consult only when concepts converge; structural diversity is diagnostic,
  not a quota.
