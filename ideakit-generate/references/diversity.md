# Diversity enforcement — read before Step 3, every run

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

- **Market segment** — e.g. enterprise vs. SMB vs. prosumer vs. consumer; or distinct verticals.
- **Mechanism / wedge** — automation vs. marketplace vs. data/insight vs. tooling vs. service.
- **Business model** — SaaS subscription vs. usage-based vs. take-rate vs. done-for-you service.
- **Who you replace** — incumbent software vs. an agency/outsourcer vs. a manual internal process
  vs. a spreadsheet.
- **Time horizon** — works today vs. bets on a capability arriving in 12–18 months.

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
- at least one "bets on near-future capability" idea and one "works today" idea.

If the set fails this check, that's the signal to regenerate the missing kinds — not to proceed.

## Anti-patterns
- Asking for "20 ideas" in one breath and taking whatever comes — guarantees clustering.
- Twenty wrappers on the same LLM feature for twenty industries — that's one idea, not twenty.
- Diversity of *wording* without diversity of *structure* — rename-only variants don't count.
