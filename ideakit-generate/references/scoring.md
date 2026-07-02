# Scoring rubric — Step 4

This rubric is the governing principle applied to *judgment*: six dimensions exist so no idea is
judged on one criterion (criteria variety), and the honesty rules below keep scores provisional
(reflexivity). Score **every idea generated in Step 3** — not a pre-picked few — on six dimensions,
0–5 each (max 30). The scores are what *produce* the shortlist; do not hand-pick a shortlist first
and score only that. Be honest, especially on Feasibility and Survivability — LLM-generated ideas
systematically over-score there. A low total is useful information that saves the user weeks; it is
not a failure of the skill.

Give a one-line justification per dimension, not just a number. The number orders the shortlist;
the justification is what the user actually reasons with.

## The six dimensions

### 1. Pull — Pain *or* Desire (Graham, expanded)
How strong is the pull toward this? Pull comes in two forms — score whichever is **stronger**, and
never down-score one form for not being the other:
- **Painkiller pull:** how urgent, deep, recurring, and expensive is the *problem*?
- **Desire pull:** how intense, frequent, and identity-driven is the *want*? — entertainment,
  fandom, status, belonging, beauty, play, self-expression. A "starving crowd" can be starving for
  *delight*, not only relief.

Scale:
- 0–1: weak either way — a mild nice-to-have, or a want too faint/rare to drive spending.
- 2–3: real but moderate — an annoyance people work around, OR a want people indulge occasionally.
- 4–5: intense and recurring — expensive pain people actively hunt to fix, OR a deep desire people
  return to compulsively and spend money *or time* on (re-watch, re-buy, follow, collect, belong).

> Desire/identity markets (BL/Y-series, K-pop & fandom, games, creator content, fashion, IP,
> collectibles, wellness-as-lifestyle) are real and often enormous. Do **not** dock them just
> because "nobody loses sleep" — that bias is exactly how this skill historically missed whole
> categories. Measure intensity × frequency of the want instead.

### 2. Market / Starving Crowd (Hormozi)
Is there a hyper-specific crowd in pain *or craving*, able and willing to pay (with money **or**
attention/time), reachable, and growing?
- 0–1: vague "everyone", no clear buyer, or no budget/attention.
- 2–3: identifiable segment, moderate willingness to pay or engage.
- 4–5: specific hungry crowd with budget (or intense, sustained attention) and an existing habit of
  paying for relief *or delight*; growing.

### 3. Secret (Thiel)
Does the idea rest on a true insight most people don't yet believe?
- 0–1: consensus idea; everyone already agrees it's good (so it's crowded or already built).
- 2–3: mild contrarian edge.
- 4–5: a real "secret" — a defensible belief about the world that, if right, is a big advantage.

### 4. Job (Christensen)
Is there a clear job the customer is hiring this to do, and does it beat what they fire?
- 0–1: solution looking for a problem; unclear job.
- 2–3: plausible job, unclear it's better than the status quo.
- 4–5: crisp job, clearly better than what it replaces, on a dimension the customer cares about.

### 5. Survivability / Power (current platform reality)
If a dominant AI platform ships this natively tomorrow, why does this still win? Don't accept a vague
"we have a moat" — **name the durable power** using Hamilton Helmer's *Seven Powers*: Scale
Economies, Network Economies, Counter-Positioning (a model the incumbent won't copy because it would
damage their existing business), Switching Costs, Branding, Cornered Resource (exclusive access — IP,
data, talent, supply), Process Power. If you can't name which power applies, the idea is fragile.
- 0–1: thin wrapper, no nameable power — a platform absorbs it by default.
- 2–3: a plausible power but contestable or not yet built (e.g. switching costs you'd have to earn).
- 4–5: a credible, specific power you can name and defend — proprietary/cornered data or IP, deep
  vertical workflow + switching costs, regulated trust, network/scale effects, brand & community/
  fandom loyalty, or counter-positioning a big platform structurally won't chase. (For desire-driven
  ideas the power is usually Branding + Cornered Resource (owned IP) + Network/community — not data.)

### 6. Feasibility (Ries)
Can the riskiest assumption be tested cheaply and soon, given the user's resources?
- 0–1: requires capital/tech/time the user doesn't have; risk untestable for months.
- 2–3: buildable but the core risk is moderately expensive to test.
- 4–5: smallest version is testable within weeks at low cost; riskiest assumption has an obvious
  cheap experiment.

## Output of scoring
For each idea, record: the six sub-scores, the total /30, and — most important — the **single
riskiest assumption** and the **cheapest next test** of it. Those two fields are what the
downstream `ideakit-validate` validation and the user's go/kill decision hang on.

## Reading the totals
- Don't treat the total as a verdict — treat it as a sort key. A 22/30 with a cheap, decisive next
  test can beat a 25/30 whose riskiest assumption takes six months to test.
- Flag any idea that scores 4–5 on Pull + Market but ≤2 on Survivability: it's a real problem (or a
  real desire) worth serving but needs reframing for a moat before anyone builds. For desire-driven
  ideas that moat is usually brand/IP/community, not data — say so explicitly.

## Fad vs. durable — the second axis (don't fold it into Pull)

Pull measures *how strong* the demand is; it does **not** measure *how long it lasts*. Judge that
separately, or you'll mistake a viral spike for a business. Tag each idea **Painkiller / Vitamin /
Candy**: Painkiller = needed; Vitamin = good, habitual, recurring; Candy = instant but fleeting.
Candy is the fad risk. Apply the **Lindy test**: is the demand rooted in an enduring human drive
(status, belonging, care, meaning, health, safety, play) — which tends to persist — or in a
platform-specific moment that will pass? Keep a Candy idea only with a credible path to becoming a
Vitamin, otherwise discount it. Note: desire ≠ fad — fandom, pets, and faith are desire markets that
are deeply Lindy-durable; and painkillers can be fads too.

## Portfolio balance — reflexivity at synthesis (Step 5)

Scoring ranks individual ideas; the shortlist as a *set* must still have requisite variety. Before
finalizing, declare the mix on two independent axes — **value type** (painkiller↔desire) and
**durability** (durable↔emerging) — plus, for force briefs, the **order-of-effect ring spread**
(ring-2/3 ideas score lower on Feasibility by nature; don't let the sort silently purge them) — and
justify the weighting against the brief and the user's edge.
No axis should be all-one unless the brief demands it: an all-painkiller, all-desire, or all-fad
shortlist is a frame failure, not a result.
