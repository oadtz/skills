# Ideakit — Idea memory contract

Use this from any `ideakit-*` skill that receives, changes, validates, names, pitches, or otherwise
advances an idea after `ideakit-generate`.

## Principle

**The selected idea location is the source of truth.** Chat and one-off artifacts are not enough once
the user has chosen a place to keep ideas. Every later stage should preserve that location's existing
convention and update the matching idea, not create a parallel memory.

## When to apply

Apply this when any of these are true:

- the user names an idea repository, vault, notes folder, or `ideas/` path
- the incoming artifact says `Storage status`, links an idea card, or references an idea index
- the task is clearly a continuation of a generated/stored idea
- the user asks to maintain, update, capture, file, or merge idea information

If no idea location is known, still write the skill's normal artifact to `outputs/` when possible and
ask one concise question for the storage destination. Do not invent a location.

## Scan

Before writing into a non-empty idea location:

- list files with `rg --files` or the host's fastest file search
- read the index plus the smallest useful sample: 2-3 idea cards/notes and any README/template
- look for frontmatter, tags, backlinks, Dataview fields, stage names, folder conventions, and
  artifact-link conventions
- if the destination is a git repo, check status first; do not stage, commit, or push unless asked

## Match

Find the current idea by normalized name, aliases, source artifact, backlink, or concept overlap.

- exact/same concept: update the existing card/note
- adjacent concept: add related links if the convention supports them
- uncertain match: write to `inbox/` or `ideas/inbox/` and say the merge is conservative
- no match: create a new card using the destination's convention, or the portable card format from
  `ideakit-generate/references/storage.md` if no convention exists

Never overwrite or delete existing idea memory to fit a new structure.

## Read before you write

Idea memory is an input, not just a destination. Before a run that generates or expands ideas for
someone who already has a location, read it for two things:

- **Already-proposed families** — what this person has been shown before, so a new run explores a
  different neighborhood instead of re-deriving the same one under new wording. Pass them forward as
  an exclusion set, never as examples.
- **Recorded outcomes** — what happened to anything that advanced. That is the only feedback this
  family receives from reality; a killed-in-market concept outranks any desk signal that still says
  the opening is open.

## Update by stage

- **ideakit-explore**: append known/inferred/imagined lanes, theses and venture architectures
  considered, assumptions, front-runner, counter-case, and learning tests. Keep stage `shaped` unless
  the user parks/kills it.
- **ideakit-validate**: append PRD/PLAN link, research summary, evidence links, top assumptions, kill
  criteria, go/reframe/park/kill recommendation, and stage update (`validated`, `reframed`, `parked`,
  or `killed`).
- **ideakit-name**: append naming artifact link, shortlist, top pick, availability watch-outs, and
  legal-clearance reminder. Do not mark a name as final unless the user chooses it.
- **ideakit-present**: append pitch/deck/demo/one-pager link, audience, core message, ask, and next
  commercial/build action.

For meaningful choices, also write a dated decision note when the location has `decisions/` or an
equivalent convention.

## Record what actually happened

The idea family judges concepts on how good they look on the page, and the one study that followed
ideas through execution found that measure inverts on contact with reality. The only defence is
writing the result back. Whenever a stored idea reaches a real event — a build started or abandoned,
a first paid customer or a failure to find one, a launch, a shutdown, a pivot — append a dated line:

```
Outcome YYYY-MM-DD: [what happened, observable] — [what it disconfirmed or confirmed]
```

Do this whether the news is good or bad, and record what the run had predicted so the two can be
compared later. Ask for it explicitly when a user returns to an idea that has been sitting at
`prototype` or `active`: *"what happened with it?"* is a cheap question and the answer is the most
valuable evidence in the location. Never infer an outcome; if it is unknown, say unknown.

## Confirm

When done, report the artifact path and the idea-memory path(s) updated. If no durable memory update
was possible, say why plainly and leave the normal artifact in `outputs/`.
