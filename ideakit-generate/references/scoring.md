# Scoring rubric — Step 4

Score each shortlisted idea on six dimensions, 0–5 each (max 30). Be honest, especially on
Feasibility and Survivability — LLM-generated ideas systematically over-score there. A low total
is useful information that saves the user weeks; it is not a failure of the skill.

Give a one-line justification per dimension, not just a number. The number orders the shortlist;
the justification is what the user actually reasons with.

## The six dimensions

### 1. Pain (Graham)
How urgent, deep, and real is the problem?
- 0–1: nice-to-have; nobody loses sleep.
- 2–3: real annoyance, worked around today.
- 4–5: urgent, recurring, expensive pain people actively seek solutions for.

### 2. Market / Starving Crowd (Hormozi)
Is there a hyper-specific crowd in pain, able and willing to pay, reachable, and growing?
- 0–1: vague "everyone", no clear buyer, or no budget.
- 2–3: identifiable segment, moderate willingness to pay.
- 4–5: specific hungry crowd with budget and an existing habit of paying for relief; growing.

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

### 5. Survivability vs. platforms (2026 reality)
If a dominant AI platform ships this natively tomorrow, why does this still win?
- 0–1: it's literally a thin wrapper a platform will absorb by default.
- 2–3: some moat (data, workflow depth, distribution) but contestable.
- 4–5: a credible, specific moat — proprietary data, deep vertical workflow, regulated trust, or a
  distribution the platform won't bother to chase.

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
- Flag any idea that scores 4–5 on Pain + Market but ≤2 on Survivability: it's a real problem worth
  solving but needs reframing for a moat before anyone builds. Say so explicitly.
