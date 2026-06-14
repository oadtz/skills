# Formats — choose the vehicle, then build it well

Read this in Step 4, AFTER the narrative works. The format carries the story; it never replaces it.
Match the vehicle to the audience and context, then build it so the narrative arc (Step 3) drives
the structure — not a generic template.

## Choosing the vehicle

| Vehicle | Best for | Why |
|---|---|---|
| **Interactive demo / landing page** (HTML) | customers; technical audiences; when the product *is* the argument | "show, don't tell" — a clickable thing beats describing a thing |
| **Pitch deck** (pptx) | investors; live board meetings | the room expects it; paces a spoken narrative |
| **Vision one-pager** (PDF/HTML) | async share; busy stakeholders; teasers | forces ruthless focus to a single page |
| **Narrative memo** (docx/md) | read-first cultures (Amazon-style); nuanced cases | prose carries reasoning visuals can't |
| **Vision / architecture diagram** (SVG) | a supporting visual inside any of the above | signals systems thinking; makes the abstract legible |

When unsure: a live customer/technical pitch → interactive demo; an investor meeting → deck +
one-pager leave-behind; a recruit → memo or a short narrative call, not slides.

## How to build each (and which tool)

These are output-format skills/tools available in the environment — read the relevant one when you
build:

- **Interactive demo / landing page** → build a self-contained HTML artifact, or use the `visualize`
  widget for an inline interactive. Make the hero action obvious and clickable. Mock real data
  (e.g., a real region/number from the idea) so it feels alive, not lorem-ipsum.
- **Pitch deck** → use the `pptx` skill. 10–12 slides, one idea per slide, big visuals, few words.
  Slide order should follow the chosen narrative arc, not "problem/solution/team/ask" by rote.
- **One-pager / PDF** → use the `pdf` skill (or HTML→PDF). One page. A headline that is the core
  message, a vivid before/after, one proof point, one CTA.
- **Narrative memo** → use the `docx` skill (or markdown). Lead with the strategic narrative; let
  prose do the persuading; keep it to ~1.5–2 pages.
- **Diagram** → use the `visualize` tool (SVG). One concept, sparse, labeled — the architecture or
  the "before/after" flow. A supporting actor, never the whole pitch.

## Universal build rules

- **The narrative drives the structure.** Build the outline from Step 3's arc first, then fill it.
  If a slide/section doesn't advance the arc or serve the core message, delete it.
- **One idea per unit.** One point per slide, per section, per page.
- **Open with the hook, end with the ask.** First impression = the shift/pain/stakes; last
  impression = the single action you want.
- **Concrete assets.** Use the real numbers, names, and examples surfaced in validation. Specificity
  is what makes it feel true.
- **Less text, more weight.** Persuasion dies under bullet soup. Cut words until only the load-
  bearing ones remain.
- **Always deliver the file via `present_files`** so the user can open and share it, then offer a
  tightening pass.
