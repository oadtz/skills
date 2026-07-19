# Executable plan template

Adapt this floor to the concept. Omit irrelevant sections rather than filling them ceremonially. Keep
Observed / Inferred / Bet distinctions visible where they affect decisions.

## Variant A — software product or venture

```markdown
# [Name] — Plan

## Decision and venture thesis
Carry over the confirmed sharpened-concept block from Step 4 **verbatim** (it already contains
actor/trigger, mechanism, why now, wedge, Observed/Inferred/Bet, recommendation, and evidence
level). It is the plan's single canonical statement — every later section must add new
information, never restate these fields.

## Alternatives and differentiation
What users do today, why switching may happen, and the specific mechanism that differs.

## v1 scope and non-goals
The smallest valuable wedge, explicit exclusions, and expansion hypotheses that are not v1 commitments.

## User/operating flow
Primary flow plus empty, failure, recovery, and manual-operations paths where relevant.

## Business and distribution hypothesis
Buyer, budget/value pool, pricing assumption, first-10 reachability, trust path, and affordable loss.

## Acceptance criteria and success signals
Testable behavior plus leading learning signals and lagging business outcomes.

## Technical decisions needed now
Only concrete stack, dependency, data, privacy, build-vs-buy, or integration choices necessary for
handoff. Defer architecture decisions that belong in forge-architect.

## AI engineering handoff (software concepts — fill what the validation learned)
The fields `forge-architect` consumes so it never re-interviews (see
`../../ai-engineering-foundation.md`):
- Product AI dependency: none / build-time only / optional runtime / core runtime
- Founder control surface: [decisions and boundaries the founder retains]
- Verification loop: [how correct work will be distinguished from plausible work]
- Human attention budget: [recurring decisions/reviews/exceptions the founder can afford]
- External bottleneck: [the constraint more generated code cannot remove]
- Failure containment: [permissions, blast-radius limits, recovery expectations]
- Delegation architecture: [how work splits across agents/components, if already known]
- Scope made feasible: [what the AI engineering model unlocks for this concept]

## Evidence ledger
| Claim | Label | Evidence/source | Freshness | Confidence | Counter-signal |

## Critical assumptions, tests, and kill criteria
| Assumption | Confidence | Cheapest informative test | Kill/reframe signal |

State the next costly signal needed to advance the evidence level. Do not call desk-supported demand
validated.

## Selected dependency and trajectory risks
Include platform replication only when a platform controls the wedge. Include only forces that can
change the decision.

## Open questions

## First implementation/learning steps
```

## Variant B — general project or initiative

```markdown
# [Name] — Plan

## Decision and thesis
Carry over the confirmed sharpened-concept block from Step 4 verbatim (beneficiary/actor + trigger,
desired change, mechanism/approach, why now, initial pilot, Observed/Inferred/Bet, recommendation,
evidence level). Later sections add new information only.

## Current behavior and alternatives

## Pilot scope and non-goals

## Stakeholders, distribution, and operating flow
Who must participate, how they are reached, dependencies, owners, and sequence.

## Activities and resources

## Evidence ledger
| Claim | Label | Evidence/source | Freshness | Confidence | Counter-signal |

## Success signals
Leading learning indicators and measurable outcomes.

## Critical assumptions, tests, risks, and kill criteria

## Open questions

## First actions
```

The plan must be self-contained enough for a collaborator to act without the preceding conversation.
