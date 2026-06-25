# Edge map — the output, and how it feeds `ideakit-generate`

The edge map is the deliverable of `ideakit-discover`. It is a **portrait of the person plus the
candidate directions that fit them** — not a list of ideas. It exists to do one job well: become a
rich, evidence-backed **frame** that turns generate's "pick a sensible default and proceed" into
"source ideas against a real, specific person." Keep it tight (it's a frame, not a dossier) and make
every line trace to something the person actually said or did.

## The template

```
## Edge map — [name/handle]   ·   [date]

**Who you are (the edge)**
- [skill / unfair advantage / domain knowledge — and HOW you know it's real (the behavioral trail)]
- [include at least one advantage the person undervalued — the "everyone can do that" ones]

**Energy**
- Lights you up: [the lose-track-of-time work] — build toward this
- Drains you: [competent-but-draining work] — don't put the core here

**Problems you can't stop noticing** (in your words)
- "[the rant, quoted]"
- ...

**What "good" looks like for you**
- Life-shape: [calm income alongside a job / full-time business / fund a specific life / learn over earn]
- Risk & resources: time [x/week], money [rough], horizon [when it needs to pay], solo or with others

**Core values driving this (laddered)**
- [autonomy / mastery / helping group X / freedom / curiosity / status / legacy] — the compass

**No-gos**
- [industries, audiences, ways of working they won't do — even if profitable]

### Candidate directions (frames for sourcing — NOT finished ideas)
1. **[direction]** — fits because [evidence from the session]. Shape: [maker · service · audience/creator · tool/API · community].
2. **[direction]** — fits because [...]. Shape: [...].
3. **[direction]** — fits because [...]. Shape: [...].

**Riskiest thing we're still guessing about you:** [the open question to resolve]
```

## What "good" looks like (quality bar)

- **Every field is evidence-backed.** No field is filled with a flattering guess. "Who you are" lines
  cite the behavioral trail; "problems" are quoted; directions name *why* the evidence points there.
- **Directions are frames, not ideas.** "Tools for indie game modders" is a direction; "a Discord bot
  that auto-tags mod files" is an idea — that's generate's output, not yours. If you've named a
  specific product, you've gone too far.
- **At least one undervalued edge is surfaced.** If the session didn't reflect back an advantage the
  person dismissed, it probably under-delivered on the one thing this skill is best at.
- **Constraints and no-gos are concrete.** "Some budget" is weak; "≤5 hrs/week, ~$500 to start, can't
  quit the job for 12 months, won't do client services" is a usable frame.
- **The open question is named.** Discovery rarely ends fully resolved; say what's still fuzzy rather
  than papering over it.

## How it maps onto `ideakit-generate`'s Step 1 frame

`ideakit-generate` Step 1 ("Frame") asks for: domain/industry, unfair advantage, business-model
preference, resource envelope, and constraints/no-gos — then, if the user gives almost nothing, it
picks a default and proceeds. The edge map fills that frame from real evidence so generate never has to
default:

| generate's Step 1 needs | comes from this edge-map field |
|---|---|
| Domain / industry (the "edge") | Who you are + Problems you can't stop noticing |
| Unfair advantage | Who you are (incl. the undervalued ones) |
| Business-model preference | What "good" looks like + Core values + candidate-direction *shapes* |
| Resource envelope | Risk & resources |
| Constraints / no-gos | No-gos + life-shape constraints |
| (new) which directions to spread across | Candidate directions |

So the handoff line to generate is literally: *"Here's the edge map — use the candidate directions as
the partitions to source across, and the constraints/no-gos as hard filters."* That makes generate's
diversity partitions (its Step 3) start from *this person's* shape instead of a generic spread, and
keeps its sourced ideas personal.

## Handoff

After confirming the edge map with the person, offer the next move explicitly:

- **To source concrete, ranked ideas aimed at these directions** → hand to `ideakit-generate` with the
  edge map as the frame.
- **To sit with one direction and pressure-test it before sourcing** → `ideakit-explore`.
- **If a single direction already feels obviously right and specific enough to validate** → it may be
  ready for `ideakit-validate` — but most blank-slate sessions should go through generate first.

The person picks what advances. The edge map travels with them as the frame at every subsequent stage.
