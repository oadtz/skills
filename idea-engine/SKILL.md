---
name: idea-engine
description: Use when the user invokes Idea Engine, seeks surprising business opportunities beyond generic AI ideas, continues a scored ideation campaign, gives candidate feedback, or needs to turn a selected opportunity into a prototype definition.
---

# Idea Engine v0.2

Discover opportunities neither participant would normally consider. Human taste guides search; desire to try is a separate signal; neither establishes market demand.

## Start and resume
Read [state](memory/state.json) first, then its active taste, desire, campaign and latest-run paths relative to `memory/`. Missing memory stays unknown; never reconstruct scores or mappings. Archives are evidence, not instructions. Follow the user's language and scope; explain products before architecture. No background work or build is implied.

Read [memory protocol](references/memory-and-evals.md) for starting, feedback, persistence and upgrades. Engine instructions, Taste Model, Desire Model, Run History and Evals evolve separately. Historical campaign choices are examples, never universal preferences or default products.

## Discovery and evolution
Read [workflow](references/workflow.md) for framing, mechanisms and evidence.

1. State brief, constraints, phase and lane allocation. Default six candidates: two wild Explore, two mechanism Exploit, two Mutation/crossbreed. Preserve approximately 30–40% wild; report integer rounding and explicit user overrides.
2. Explore genuinely different frames before combining. Freeze wild seeds before favorite exposure when feasible. Wild candidates remain taste-unfiltered through presentation. Shared-context passes are not independent; disclose exposure. Fresh-context exploration, when authorized, receives only brief and constraints.
3. Explain actor, action, changed outcome and causal value. Descendants require parent IDs, extracted mechanism, operator and behavioral delta. Crossbreed selectively only when the interaction creates value. Renaming or generic “AI for X” is insufficient.
4. After each scored round, inspect mechanism diversity, parent concentration and contradictory feedback. High scores with shrinking diversity trigger reframing and counter-taste exploration, not more copies. Infer deep mechanisms with confidence and counterevidence, never permanent domain rules.
5. Present concrete usage scene, beneficiary/payer hypothesis, biggest unknown and cheap test. Ask for numerical 1–10 curiosity scores (decimals allowed) and separately **★ = would actually try a prototype**. Missing stars are unknown unless explicitly unstarred. Never predict user scores or equate stars with willingness to pay.

## Converge and stop
Discovery precedes Validation. After divergence, use [decision workflow](references/decisions.md): direct competitors/substitutes, why now, payment proxies, differentiation and biggest unknown. Evidence can KILL a former favorite; preserve its scores and rationale.

Then specify a Killer Prototype: **Build the cheapest real thing that answers the biggest unknown.** Prefer functional prototypes over proxies when affordable and informative. Define killer behavior/metric and pass/interesting/fail criteria; user #0 is not the market.

Once a candidate and informative bounded test are selected, stop generating and write Product Definition: problem, primitive, first user, 3–5 MVP capabilities, non-features, substitute differentiation and killer test. Close the campaign with decisions, unknowns, next action and eval-backed process lessons. Build only within the user's authorized task scope.
