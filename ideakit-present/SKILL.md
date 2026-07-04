---
name: ideakit-present
description: >
  Turn a developed business idea into persuasive communication that makes a specific audience —
  customers, investors, or teammates — feel conviction and act. Use this skill whenever the user
  wants to pitch, present, communicate, or "sell" an idea: make a pitch deck, one-pager, demo,
  landing page, or narrative; or says things like "how do I present this", "make this compelling",
  "pitch to investors", "explain this to customers", "get my team excited", "make people care",
  "this needs to land", or "make it exciting". This skill is persuasion-first: it builds the
  narrative and emotional core BEFORE choosing a format, because a beautiful deck with a weak story
  convinces no one. It is the final stage of the ideakit pipeline (after ideakit-validate). It is
  NOT for generating ideas (use ideakit-generate) or validating them (use ideakit-validate). When the
  idea is stored in an ideakit memory location, update that idea with the pitch artifact, audience,
  core message, ask, and next action.
---

# Ideakit — Present (make people act)

Take a developed idea and turn it into communication that creates **conviction and emotion** in a
specific audience — so they do something: buy, fund, or join. The test of success is not "looks
polished." It's: **does it make the audience (and the user themselves) lean in?**

## The one principle that governs everything here

**Story before format. Emotion before information.** People don't act because they understood your
feature list — they act because they *felt* something: a pain they recognize, a future they want,
a wave they're afraid to miss. A gorgeous deck wrapped around a flat story persuades no one; a
sharp story told on a napkin can move money and people. So this skill spends its effort on the
*message* first, and treats the deck / demo / one-pager as a vehicle for a message that already
works.

If you ever catch yourself jumping straight to "let's make slides," stop — you've skipped the part
that matters.

## Where this sits in the pipeline

```
ideakit-discover  →  ideakit-generate  →  ideakit-explore  →  ideakit-validate  →  ideakit-present (THIS)
blank slate          generate ideas       expand + challenge    validate + PRD       make people act
```

It usually runs on an idea that's been validated (a PRD or a sharp idea statement exists). If the
idea is still vague or unproven, say so and point back to `ideakit-validate` — persuading people of
something untrue or half-baked backfires. If the user only needs internal sharpening, that's
`ideakit-explore`.

## Host capability mapping

Use capabilities by intent, not by product-specific tool name:

- **User input**: ask concise plain-text questions unless the host offers a structured input UI.
- **Artifact creation**: use the host's available file/artifact mechanism for decks, docs, PDFs,
  HTML, diagrams, or images. If no artifact mechanism exists, produce a complete markdown outline or
  self-contained HTML in chat and state that no file was created.
- **Format-specific tools**: prefer the host's native presentation/document/PDF/web/diagram tools
  when available; otherwise build the closest portable format.
- **Delivery**: return the artifact using the host's normal path/link format.

## Workflow

Five steps: **Aim → Core message → Narrative → Vehicle → Heart-race check.** The first three are
where the work is. Don't skip to the vehicle.

### Step 1 — Aim (who, and what should change in them)

Pin down three things before writing a word. Ask the user if not already clear:

- **Audience**: customer, investor, teammate (or a specific named person/segment). Each is moved by
  different things — read `references/audience-playbooks.md`. If the audience is mixed, pick the
  primary one; you cannot make everyone's heart race with one message.
- **The single action** you want them to take after experiencing this (sign up / take a meeting /
  wire money / quit their job and join). One action. If you can't name it, the message has no job.
- **The belief shift**: what do they believe now, and what must they believe to take that action?
  Persuasion is moving someone from belief A to belief B — name both.

Also name the **emotional target**: relief? ambition? FOMO? belonging? The feeling you're aiming
for shapes every later choice.

### Step 2 — Core message (the one thing)

Distill the single idea that must land. If the audience remembers only one sentence, what is it?
Make it concrete and consequential, not a category description.

- Weak: "An AI platform for water data transparency."
- Strong: "The bottleneck in water isn't missing data — it's data nobody can trust. We make water
  data provable."

The core message is the spine. Everything in the narrative serves it; anything that doesn't, cut.

### Step 3 — Narrative (build the arc that fits the audience)

Pick the narrative structure that fits the audience and goal — don't default to "problem, solution,
team, ask." Read `references/narrative-frameworks.md` and choose deliberately. Common high-power
choices:

- **Strategic narrative** (best for investors and rallying a team): name an undeniable shift in the
  world → there will be winners and losers → paint the promised land → position the idea as the
  bridge to it. Stakes first, product later.
- **StoryBrand / hero's journey** (best for customers): the *customer* is the hero with a problem;
  the product is the guide that gives them a plan and a win. Never make your company the hero.
- **Before → After → Bridge**: the painful now, the better future, and your idea as the crossing.
- **Problem → Agitate → Solve**: make the pain vivid and felt before relieving it.

Whatever you pick: **make it concrete** (one vivid, specific example beats ten abstractions),
**create tension before resolution** (no tension, no attention), and **paint the future** the
audience gets to live in. Use a real scenario, a real person, a real number.

### Step 4 — Vehicle (choose and build the format)

Only now pick the medium, based on audience and context. Read `references/formats.md` for when to
use each and how to build it with the host's available presentation, document, PDF, HTML, or diagram
capabilities:

- **Interactive demo / landing page** (HTML) — strongest "show don't tell"; best when the product
  itself is the argument, or for technical/customer audiences.
- **Pitch deck** (pptx) — board/investor meetings; 10–12 slides, one idea per slide.
- **Vision one-pager** (PDF/HTML) — fast async share; forces ruthless focus.
- **Narrative memo** (doc) — for audiences who read (Amazon-style); when nuance matters more than visuals.
- **Architecture / vision diagram** (SVG) — a supporting visual that signals systems thinking.

Build the chosen vehicle so the *narrative* drives the structure — slides/sections follow the arc
from Step 3, not a generic template. Keep one idea per unit. Cut anything that doesn't serve the
core message.

### Step 5 — Heart-race check (the gut test)

Before delivering, run the resonance check in `references/resonance-checklist.md`. The core
questions: Is there one clear core message and one clear ask? Are the stakes real and felt? Is it
concrete (a real example/number, not abstractions)? Would the *user themselves* lean forward? If
any answer is "meh," fix the narrative — not the fonts.

Deliver the artifact using the host's normal file/artifact delivery mechanism, and offer a tightening pass.

Then point to the next step based on *who the pitch was for*:

- **Pitched to customers?** Hand to `solo-sell` to actually run the founder-led sales motion and close
  them (or `solo-distribute` if you still need to reach them).
- **Pitched to investors?** Hand to `solo-fund` to match the raise to the right instrument and the
  lowest justified rung.
- **Ready to build what you just pitched?** Hand the PRD to `forge-architect` to start the build.

A deck is a means, not the finish line — name the action it's meant to unlock.

## Operating principles

- **Truthful persuasion only.** Make people feel the real stakes and the real upside — never
  manufacture urgency or inflate claims. Hype that outruns the substance destroys trust, and the
  validation step exists precisely so you don't have to.
- **One audience, one action, one message.** Splitting focus dilutes everything.
- **Specific beats grand.** "Saves a 200-well district 3 weeks per trade" lands; "revolutionizes
  water management" bounces off.
- **Emotion is earned with concreteness, not adjectives.** Show the moment, don't claim the feeling.
- **The user is the first audience.** If it doesn't make *them* lean in, it won't move anyone else.

## Execution

**Don't stop at advice — produce the deliverable.** Actually **build the deck / one-pager / demo** as a
real file (use the document skills where polish matters), not an outline of one. Stage anything that
publishes the pitch or sends it from the user's identity (to investors/customers) for their approval.
If this presentation is for a stored idea or the user names an idea location, read
`../ideakit-memory.md` and update the matching idea memory with the artifact link, audience, core
message, ask, and next commercial/build action. Full contract: `../ideakit-execution.md`.

## Reference files

- `references/audience-playbooks.md` — what makes customers vs investors vs teammates act; read this first in Step 1.
- `references/narrative-frameworks.md` — the story structures and how to choose; Step 3.
- `references/formats.md` — choosing and building the vehicle (deck/demo/one-pager/memo/diagram); Step 4.
- `references/resonance-checklist.md` — the heart-race gut check and common message-deflating mistakes; Step 5.
