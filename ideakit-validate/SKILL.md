---
name: ideakit-validate
description: >
  Validate a mature venture or project concept and turn it into an executable markdown plan or PRD.
  Use when the concept already has a coherent target actor, job or desire, value mechanism, why-now,
  and initial wedge—or when a chosen concept arrives from ideakit-generate or ideakit-explore. Research
  demand, alternatives, distribution, economics, feasibility, dependencies, timing, and kill criteria
  selectively according to the concept's mode; sharpen or kill the concept, then write a buildable
  plan. Do not use for a vague seed with multiple plausible interpretations: use ideakit-explore first.
  Update idea memory when validating a stored idea.
---

# Ideakit — Validate

Read `../ai-engineering-foundation.md` now and apply its default to every software or digital product
concept; validate founder control and external bottlenecks instead of human coding capacity.

Turn a mature concept into an evidence-aware decision and executable plan. Validation is not a ritual
that every idea passes; it should strengthen, reframe, park, or kill the venture.

Read `../ideakit-craft.md` first. Preserve the distinction between **Observed**, **Inferred**, and
**Bet** throughout the research and PRD.

Validation is a level of evidence, not the name of this workflow. Desk research can justify a next
test, reframe, or decision to stop; it cannot by itself prove willingness to switch or pay.

## Maturity gate

Before starting validation, confirm that the concept has:

1. a target actor and triggering situation;
2. a meaningful job, desire, obligation, or changed behavior;
3. a proposed value mechanism—not only a technology or category label;
4. a why-now change, insight, or explicit timeless demand;
5. an initial wedge or plausible first manifestation;
6. at least one falsifiable critical assumption.

If several structurally different interpretations remain plausible, route to `ideakit-explore`. If
there is no venture yet, route to `ideakit-generate`. Do not use PRD structure to manufacture clarity.

## Arrival modes

- **From generate** — adopt its Observed → Inferred → Bet chain, counter-case, wedge, and learning
  test. Verify rather than re-interview.
- **From explore** — begin with its front-runner, alternatives, and uncertainties.
- **Cold but mature concept** — confirm the six maturity fields in a compact snapshot.
- **Existing PRD revision** — start from sharpening and validate only claims or assumptions that are
  new, stale, or decision-critical.

## Capability mapping

- Use current web/search/browser, first-party connected knowledge, local artifacts, and user-provided
  sources. Prefer observed behavior, spend, workarounds, commitments, and failed attempts over survey
  enthusiasm.
- If live research is unavailable, produce a clearly labeled non-current draft and mark external
  claims `[needs evidence]`.
- Write the final PRD/plan as a real artifact when possible; otherwise provide it completely in chat.

## Workflow

Run: **Decision frame → Select research dimensions → Evidence & disconfirmation → Sharpen/kill →
Plan.** Ask one concise question at a time and keep user approval at the snapshot and sharpened-concept
gates.

### 1. Confirm the decision frame

Capture:

```
Actor + trigger:
Job/desire:
Mechanism:
Why now:
Initial wedge:
Critical bet:
Affordable loss / resource constraint:
Decision this validation must enable:
```

Confirm it with the user. Do not re-run a long interview when upstream artifacts already answer it.
For software use `references/interview-software.md` only for missing build-critical details; for a
general initiative use `references/interview-general.md` selectively.

### 2. Select decision-changing research dimensions

Read `references/validation-playbook.md`, then choose only dimensions that could change go/reframe/
park/kill. Explain the selection briefly.

Core candidates:

- **Demand and behavior** — frequency, stakes, workarounds, spend, non-consumption, commitments.
- **Alternatives** — direct competitors, substitutes, internal/manual solutions, doing nothing.
- **Distribution** — reachable first users, trust path, channel constraints, acquisition behavior.
- **Economics** — buyer, budget, value created/captured, gross-margin or operational reality.
- **Execution** — technical, operational, regulatory, supply, capability, and founder constraints.
- **Dependency/platform** — only where a platform, supplier, marketplace, model provider, or policy
  controls the wedge.
- **Timing/trajectory** — only forces that materially affect the concept: capability/cost curve,
  regulation, culture, demographics, funding, infrastructure, or competitor response.
- **Compounding power** — whether the wedge can accumulate brand, data, network, process, switching
  cost, scale, cornered resource, or counter-positioning.

Do not insert generic Claude/ChatGPT/MCP/quantum tables into unrelated ventures. For an AI-native
software concept, platform replication may be mandatory; for an event, service, consumer brand, or
general project, use its real dependencies.

### 3. Research evidence and the counter-case

Search with multiple query shapes and dates. Maintain an evidence ledger:

| Claim | Label | Evidence/source | Freshness | Confidence | Counter-signal |
|---|---|---|---|---|---|
| ... | Observed / Inferred / Bet | ... | ... | ... | ... |

Rules:

- cite observations beside the claim;
- do not cite a source as if it made your inference;
- quantify only when the underlying source supports the number;
- seek failed products, negative reviews, low adoption, channel friction, and contrary behavior;
- state the strongest disconfirming finding near the top, not inside a ceremonial risk appendix;
- if no direct demand evidence exists, say whether this is non-consumption, a new category, or simply
  an unsupported bet.

Assign the concept an **evidence level** based on the strongest relevant proof actually obtained:

| Level | Evidence | Permitted conclusion |
|---|---|---|
| E0 Thesis | coherent reasoning or desk signals only | worth researching / unsupported |
| E1 Behavior | observed workaround, spend, switching attempt, or repeated past behavior | problem/desired progress exists |
| E2 Commitment | buyer shares data, time, access, LOI, deposit, or another costly signal | testable demand with named conditions |
| E3 Transaction | paid pilot, preorder, signed contract, or sustained real use | locally validated wedge |
| E4 Repeatability | multiple independent buyers repeat the behavior or transaction | early repeatability, not market certainty |

Do not upgrade indirect market statistics, complaints, interviews, or survey enthusiasm into E2/E3.
State which dependency remains unvalidated even when another dimension reaches a higher level.

Return a concise research brief organized around the chosen dimensions, not a fixed template. Ask for
reaction before synthesis only when the evidence creates a directional choice the user has not already
authorized. Otherwise continue and flag the choice in the recommendation.

### 4. Sharpen, reframe, park, or kill

Make a recommendation and show its reasoning:

- Which observations survived?
- Which inference changed?
- Is the bet still worth its affordable loss?
- Is the wedge narrow enough to win yet connected to a meaningful expansion?
- Does a different actor, payer, mechanism, or architecture fit the evidence better?
- What must happen before investing more?

Produce the sharpened concept:

```
For [actor] in [trigger], [venture] enables [outcome] through [mechanism].
Why now: [change or timeless demand]
Initial wedge: [narrow outcome + first users]
Expansion path: [what opens next]
Observed: [...]
Inferred: [...]
Bet: [...] — wrong if [...]
Recommendation: go / reframe / park / kill
Evidence level: E0 / E1 / E2 / E3 / E4 — [what earned it]
```

Define 3–5 critical assumptions with confidence and tests. Kill criteria must be specific to the
venture; include platform replication only when platform dependency is real. Get explicit approval
before writing the final plan only when the sharpened direction materially changes the actor, promise,
business model, cost, or risk the user authorized. Otherwise write the plan and make the change visible.

### 5. Write the executable plan

Read `references/prd-template.md`. Adapt the template to software or general-project mode. Include:

- decision context and epistemic labels;
- target actor, trigger, job/desire, and alternatives;
- v1 wedge and explicit non-goals;
- user journey or operating flow;
- business/distribution hypothesis when this is a venture;
- acceptance criteria or measurable outcomes;
- critical assumptions, learning plan, and kill criteria;
- current evidence level and the next costly signal required to advance it;
- dependencies, risks, open questions, and evidence links;
- expansion path as a hypothesis, not committed scope.

Every section must contribute to execution or a decision. Do not fill irrelevant sections with “TBD”.
Name actual technology only when the choice is needed at this stage and can be supported.

Default filename: `outputs/<short-slug>-PLAN.md`; use `SPEC.md` only when requested.

## Handoff and memory

After delivery, recommend only relevant next steps:

- build → `forge-architect` or another implementation workflow;
- business model/pricing → `solo-model`;
- name → `ideakit-name`;
- persuade an audience → `ideakit-present`;
- unresolved invention → return to `ideakit-explore`.

If the idea has a storage location, follow `../ideakit-memory.md` and record evidence, decision,
assumptions, kill criteria, plan link, and stage (`validated`, `reframed`, `parked`, or `killed`). If no
location is known, ask one concise storage question after delivering.

## Execution

Actually perform the selected research and write the plan. Follow `../ideakit-execution.md`, keep the
user in charge of directional choices, and never fabricate evidence to make the document look complete.
