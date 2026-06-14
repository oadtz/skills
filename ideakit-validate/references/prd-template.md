# PRD Template — Claude Code Handoff

This is the structure for the final markdown PRD produced in Phase 4. The file should be saved
as `outputs/<short-slug>-PLAN.md` (or `SPEC.md` if the user asked for a spec).

There are two variants — one for software mode, one for general mode. Use the template that
matches the mode selected in Phase 0.

The PRD must be **complete and self-contained**. A future Claude Code session (or a human
collaborator) should be able to read this file and start work without needing the conversation
that produced it.

---

## Variant A — Software Product / Feature

```markdown
# [Idea Name] — Plan

> One-sentence elevator pitch.

## 1. Problem

What problem we're solving, who has it, and why it matters now. Concrete examples preferred over
abstract description.

## 2. Target User

Specific persona(s). Include:
- Who they are (role, context)
- What they do today instead
- The cost of the status quo to them

## 3. Value Proposition

What changes for the user when this exists. The "before / after" picture.

**Differentiation**: in one sentence, why this rather than [main alternative from research].

## 4. Scope (v1)

**In scope:**
- [Concrete capability 1]
- [Concrete capability 2]
- ...

**Explicitly out of scope for v1:**
- [Thing tempting to add but won't]
- ...

## 5. User Stories

Format: As a [user], I can [action] so that [outcome].

- [Story 1]
- [Story 2]
- ...

## 6. Acceptance Criteria

Testable conditions for v1 to be considered done. Each criterion should be objectively verifiable.

- [ ] [Criterion 1]
- [ ] [Criterion 2]
- ...

## 7. Technical Considerations

Concrete recommendations based on the research. Not generic advice.

**Suggested stack:**
- Language / framework: [choice + 1-line rationale]
- Key dependencies: [list with purpose]
- Data storage: [choice + rationale]
- Hosting / deployment: [choice + rationale]
- External APIs: [list]

**Architecture sketch:**
[2–4 sentences or a small ASCII diagram describing how the pieces fit together.]

**Build vs. buy decisions:**
- [Component]: [build / buy / wrap an existing thing] — [rationale]

**Known hard parts:**
- [Hard part 1] — [why it's hard, possible approach]

## 8. Success Metrics

**Leading indicators (early signal):**
- [Metric] — [target / direction]

**Lagging indicators (real success):**
- [Metric] — [target / direction]

## 9. Risks & Assumptions

| # | Assumption | Confidence | How to validate |
|---|------------|-----------|-----------------|
| 1 | [Assumption] | High/Med/Low | [Cheap test] |
| 2 | ... | ... | ... |

## 10. Kill Criteria

If any of the following are true, abandon or fundamentally rework the idea:
- [Concrete signal 1]
- [Concrete signal 2]

## 11. Open Questions

Things that came up during interview or research that need resolution before or during build.
- [ ] [Question 1]
- [ ] [Question 2]

## 12. Competitive Landscape

Snapshot from the research. Include URLs.

| Competitor | What they do | Key gap | Pricing |
|------------|--------------|---------|---------|
| [Name](url) | ... | ... | ... |

## 13. Platform Replication Risk Assessment

**This section is mandatory.** Document the dominant platforms in this space and the survivability
of this idea against each.

| Platform | Already shipped adjacent? | On roadmap? | Replication risk | Mitigation |
|---|---|---|---|---|
| [e.g. Claude Cowork] | [yes/no/details] | [details] | High/Med/Low | [pivot to plugin / build moat / etc.] |
| [e.g. ChatGPT GPTs] | [yes/no/details] | [details] | High/Med/Low | ... |
| ... | ... | ... | ... | ... |

**Survivability statement**: If the dominant platform launches this natively tomorrow, this
product still wins because [specific moat — distribution, vertical depth, regulatory advantage,
community, etc.]. If you cannot write a compelling statement, fix the wedge before proceeding.

## 14. Future Trajectory & 18-Month Outlook

**This section is mandatory.** Document where the world is heading and how this idea survives.

| Force | Direction (18mo) | Source | Effect on idea |
|---|---|---|---|
| LLM cost / capability | [direction] | [source] | ✅ ⚠️ ❌ |
| Open protocol adoption (MCP, etc.) | [direction] | [source] | ✅ ⚠️ ❌ |
| Funding / M&A in category | [direction] | [source] | ✅ ⚠️ ❌ |
| Regulation | [draft / passing / unclear] | [source] | ✅ ⚠️ ❌ |
| Demographic / cultural shift | [direction] | [source] | ✅ ⚠️ ❌ |
| Adjacent disruption | [tech + timeline] | [source] | ✅ ⚠️ ❌ |

**Three scenarios at 18 months:**

- **Best case**: [Tailwinds materialize. Looks like:] [...]
- **Middle case (most likely)**: [Looks like:] [...]
- **Worst case**: [Biggest threat materializes. Looks like:] [...]

If the worst case includes "the underlying problem disappears" or "the value evaporates because
the tech becomes free as a default," fold this into kill criteria as a time-bound condition
(e.g., "Abandon if [trigger] occurs before [date]").

## 15. Suggested First Steps for Claude Code

A concrete, ordered list of the first 3–5 things Claude Code should do when handed this PRD.
This makes the handoff actionable.

1. Scaffold project with [stack]
2. Implement [first feature] following [pattern]
3. ...

## Sources

- [Source 1](url)
- [Source 2](url)
- ...
```

---

## Variant B — General Project / Initiative

```markdown
# [Initiative Name] — Plan

> One-sentence elevator pitch.

## 1. Outcome

What's different in the world (or in the business) when this is done. Specific and measurable.

## 2. Audience / Beneficiary

Who needs to notice, change behavior, or benefit. Include:
- Who they are
- What they currently believe or do
- What we want them to believe or do

## 3. Approach

The shape of how we'll execute. (Campaign, content series, event, process change, partnership, etc.)
Include why this approach vs. obvious alternatives.

## 4. Scope (v1)

**In scope:**
- [Activity 1]
- ...

**Explicitly out of scope for v1:**
- ...

## 5. Key Activities

Ordered list of concrete activities required to deliver v1.

1. [Activity] — owner: [TBD or named] — timeline: [rough]
2. ...

## 6. Success Metrics

**Leading indicators:**
- [Metric] — [target]

**Lagging indicators:**
- [Metric] — [target]

## 7. Risks & Assumptions

| # | Assumption | Confidence | How to validate |
|---|------------|-----------|-----------------|
| 1 | ... | ... | ... |

## 8. Kill Criteria

If any of the following are true, abandon or rework:
- ...

## 9. Open Questions

- [ ] ...

## 10. Comparable Efforts (from research)

What others have done in this space, what worked, what didn't. Include sources.

## 11. Resources Required

- People / roles: ...
- Budget (rough): ...
- Tools / vendors: ...
- Timeline: ...

## 12. Replication & Future Trajectory

**Replication risk** (will a larger entity absorb this initiative?)
| Entity | Already done similar? | On their roadmap? | Risk | Mitigation |
|---|---|---|---|---|
| ... | ... | ... | High/Med/Low | ... |

**18-month outlook** (does this still matter in 18 months?)
- Best case: ...
- Middle case (most likely): ...
- Worst case: ...

If the worst case is structural, add as time-bound kill criterion above.

## 13. Suggested First Steps

Concrete first 3–5 actions to kick this off.

## Sources

- [Source 1](url)
- ...
```
