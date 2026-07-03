# Diversity enforcement — read before Step 3, every run

This is the governing principle (*requisite variety*) applied to **generation**: partition the idea
space so the lenses you run actually produce structurally different ideas, and synthesize the result
as a balanced portfolio rather than a monoculture.

## Why this matters

Research on LLM idea generation (Si, Yang & Hashimoto 2024, and follow-on work on diversity
barriers) found a stubborn failure mode: when you ask a model for many ideas, it does **not**
keep producing genuinely new ones. After a handful, output collapses into near-duplicates and
minor variations on a single theme. Scaling generation up does not fix this — the model lacks the
"knowledge partitioning" humans use to think from different vantage points.

The fix is not "try harder to be creative." The fix is **structural**: partition the idea space
*before* generating, then deliberately place ideas into different partitions. Do this every run.

## The method

### 1. Pick 2–3 partition axes
Choose axes along which ideas can differ *structurally* (not cosmetically). Good axes:

- **Value type** — *painkiller/utility* (solves a problem) vs. *desire/identity* (entertainment,
  fandom, status, belonging, beauty, play, IP, community). Most generators cluster entirely in the
  painkiller corner and never produce a desire-driven idea. Deliberately target both ends.
- **Market segment** — e.g. enterprise vs. SMB vs. prosumer vs. consumer vs. fandom/community; or
  distinct verticals.
- **Mechanism / wedge** — automation vs. marketplace vs. data/insight vs. tooling vs. service vs.
  **content / IP / media / community** (the mechanism behind most desire-driven businesses).
- **Business model** — SaaS subscription vs. usage-based vs. take-rate vs. done-for-you service vs.
  audience/creator monetization (ads, membership, merch, IP licensing).
- **Route-to-market archetype** — B2B SaaS / enterprise sales vs. consumer/DTC brand vs.
  prosumer/creator tool vs. community/media/IP vs. marketplace vs. public/NGO/grant vs. service-first.
  This is separate from business model. A set can look varied on paper while every idea still sells to
  an operations buyer through B2B SaaS; that is a route-to-market monoculture.
- **Who you replace OR what you create** — incumbent software / agency / manual process / spreadsheet
  to *replace*; OR a brand-new desire, category, community, or cultural product you *create* from
  nothing (these don't "replace" anything — the displacement frame can't see them).
- **Time horizon** — works today vs. bets on a capability arriving in 12–18 months.
- **Order of effect (required when the brief is a force/event, not a domain)** — *ring 1*: mitigate
  the force directly ("heatwave -> cooling"; "new regulation -> compliance tooling") vs. *ring 2*:
  serve a behavior the force changes ("heatwave -> sleepless nights -> sleep economy"; "remote work ->
  the home becomes an office -> home-office fit-out") vs. *ring 3*: serve a structure that rearranges
  once behaviors shift ("remote work -> workers leave cities -> small-town revival services";
  "aging society -> fewer working hands -> care automation"). Generators cluster hard at ring 1;
  historically the largest businesses of a big force sit at rings 2-3 (electricity -> nightlife and
  suburbs, not only light bulbs; air conditioning -> the entire Sun Belt).
- **Consequence domain (required for force/event briefs)** — generate from the consequence map's
  domains, not from the literal force word. A force should fan out across domains such as water,
  food, work schedules, city operations, insurance, retail, care, mobility, home routines, and
  leisure. If every idea still says the force word in the idea sentence, you have not escaped the
  prompt's literal frame.
- **Changed spending / new job** — who now pays, saves, delays, substitutes, insures, monitors,
  coordinates, or cares differently because of the force? This catches opportunities that are not
  named by the force itself. "Heatwave -> water allocation compliance for property managers" is more
  structurally different from cooling than another heat-alert app.

### 2. Build a small grid
Cross two axes into a grid (e.g. 3 segments × 3 mechanisms = 9 cells). You don't need to fill
every cell, but you should hit a *spread* of cells, not cluster in one corner.

### 3. Generate one idea per targeted cell
For each cell you target, generate a single best idea that genuinely belongs in that cell, rotating
through the generation lenses in `frameworks.md`. This forces structural variety because each cell
constrains the idea to a different shape.

### 4. Dedupe / collapse
Review the set. If two ideas would have the same customer doing the same job via the same
mechanism, they're duplicates — keep the stronger one and generate a replacement in an empty cell.
A useful test: "Could the same team pivot from idea A to idea B in a week without changing
customers or mechanism?" If yes, they're too close.

### 5. Sanity check the spread
Before scoring, confirm the shortlist isn't all one theme. You want at least:
- two different customer types, AND
- two different mechanisms/wedges, AND
- at least **three route-to-market archetypes** across the raw set, AND
- for broad prompts or "big / million-scale" prompts, at least **one non-B2B idea** stays in the
  scored set even if it is riskier, AND
- at least one "bets on near-future capability" idea and one "works today" idea, AND
- at least one **desire/identity-driven** idea, not only painkiller/utility ones (unless the user
  has explicitly constrained the brief to a pure-utility domain), AND
- for a **force/event brief**: at least one ring-2 AND one ring-3 idea (order-of-effect axis above)
  — a set that only mitigates the force directly has missed where the big consequences land, AND
- for a **force/event brief**: at least two ideas that do **not** name the literal force or direct
  mitigation in the idea sentence, AND
- for a **force/event brief**: at least three consequence domains represented, AND
- for a **force/event brief**: at least one idea driven by changed spending or a newly created job,
  not just a painful condition.

If the set fails this check, that's the signal to regenerate the missing kinds — not to proceed.
If every idea is a B2B/utility tool, you have almost certainly skipped the culture/desire sources in
`trend-sources.md` — go back and scan them.

## Anti-patterns
- Asking for "20 ideas" in one breath and taking whatever comes — guarantees clustering.
- Twenty wrappers on the same LLM feature for twenty industries — that's one idea, not twenty.
- Diversity of *wording* without diversity of *structure* — rename-only variants don't count.
- **Painkiller monoculture** — every idea is a B2B tool that "solves a problem." Desire-driven
  markets (entertainment, fandom, IP, community, lifestyle) are missing entirely. This is the
  single most common blind spot; the Value-type axis above exists to break it.
- **B2B route monoculture** — every idea sells through enterprise/B2B SaaS, even if the customers or
  domains differ. This often happens when the prompt says "big", "fundable", or "where the money is".
  Keep at least one credible consumer/DTC, prosumer/creator, community/media/IP, marketplace,
  public/NGO, or service-first path alive long enough to score it.
- **Literal-force lock** — every idea is a direct mitigation of the force ("heatwave -> cooling",
  "regulation -> compliance checklist", "remote work -> video calls"). For force briefs, this is the
  same failure as near-duplication: the ideas differ in wording, but all sit in ring 1. Go back to the
  consequence map and generate from ring-2/3 domains and changed spending.
- **Silent profile-filtering** — letting the user's background ("I'm technical", "needs to be
  fundable") quietly delete whole market classes before generation. Surface the desire/culture
  options *and let the user cut them*, rather than pre-filtering them away.
