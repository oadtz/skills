# Edge map — the output, and how it feeds `ideakit-generate`

The edge map is the deliverable of `ideakit-discover`. It is a **set of provisional founder-edge
hypotheses plus candidate playing fields** — not a personality verdict or list of ideas. It exists to become a
rich, evidence-backed **frame** that turns generate's "pick a sensible default and proceed" into
"source ideas against a real, specific person." Keep it tight (it's a frame, not a dossier) and make
every line trace to something the person actually said or did.

## The template

```
## Edge map — [name/handle]   ·   [date]

**Edge hypotheses**
- [skill / access / taste / obsession / lived experience — behavioral trail — confidence]
- [include at least one advantage the person undervalued — the "everyone can do that" ones]

**Energy**
- Lights you up: [the lose-track-of-time work] — build toward this
- Drains you: [competent-but-draining work] — don't put the core here

**Problems you can't stop noticing** (in your words)
- "[the rant, quoted]"
- ...

**Contrarian beliefs worth testing**
- [belief — experience behind it — what would change your mind]

**Desired game**
- [fast cash / calm solo / category-scale / cultural product / public impact / craft]

**What "good" looks like for you**
- Life-shape: [calm income alongside a job / full-time business / fund a specific life / learn over earn]
- Risk & resources: time [x/week], money [rough], horizon [when it needs to pay], solo or with others

**Core values driving this (laddered)**
- [autonomy / mastery / helping group X / freedom / curiosity / status / legacy] — the compass

**No-gos**
- [industries, audiences, ways of working they won't do — even if profitable]

**Contradictions**
- [e.g. highly capable at X but consistently drained by doing it]

### Candidate playing fields (frames for sourcing — NOT finished ideas)
1. **[field]** — fits because [evidence]. Opportunity lens: [access · taste · change · belief]. Wrong if [...].
2. **[direction]** — fits because [...]. Shape: [...].
3. **[direction]** — fits because [...]. Shape: [...].

**Riskiest hypotheses about you:** [open question + how to learn]
```

## What "good" looks like (quality bar)

- **Every field is evidence-backed and provisional.** No field is filled with a flattering guess. Edge lines
  cite the behavioral trail; "problems" are quoted; directions name *why* the evidence points there.
- **Playing fields are frames, not ideas.** "Tools for indie game modders" is a field; "a Discord bot
  that auto-tags mod files" is an idea — that's generate's output, not yours. If you've named a
  specific product, you've gone too far.
- **At least one undervalued edge and one contradiction are surfaced.** If the session didn't reflect back an advantage the
  person dismissed, it probably under-delivered on the one thing this skill is best at.
- **Constraints and no-gos are concrete.** "Some budget" is weak; "≤5 hrs/week, ~$500 to start, can't
  quit the job for 12 months, won't do client services" is a usable frame.
- **The open question is named.** Discovery rarely ends fully resolved; say what's still fuzzy rather
  than papering over it.

## How it maps onto `ideakit-generate`'s Step 1 frame

`ideakit-generate`'s playing-field step needs founder means, obsession/taste, desired game, affordable
loss, no-gos, and candidate fields. The edge map fills that frame from evidence:

| generate's Step 1 needs | comes from this edge-map field |
|---|---|
| Playing field | Edge hypotheses + Problems you can't stop noticing |
| Founder means | Edge hypotheses (including undervalued ones) |
| Desired game | Desired game + What "good" looks like + Core values |
| Affordable loss | Risk & resources |
| Constraints / no-gos | No-gos + life-shape constraints |
| Where to discover ventures | Candidate playing fields |

The handoff is: *“Use these playing fields as starting positions, the edge hypotheses as provisional
leverage, and the constraints/no-gos as hard filters.”* This keeps venture discovery personal without
treating the map as identity truth.

## Handoff

After confirming the edge map with the person, offer the next move explicitly:

- **To discover opportunity theses and venture architectures in these fields** → hand to `ideakit-generate` with the
  edge map as the frame.
- **To sit with one direction and pressure-test it before sourcing** → `ideakit-explore`.
- **If a single direction already feels obviously right and specific enough to validate** → it may be
  ready for `ideakit-validate` — but most blank-slate sessions should go through generate first.

The person picks what advances. The edge map travels with them as the frame at every subsequent stage.
