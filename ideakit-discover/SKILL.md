---
name: ideakit-discover
description: >
  Help a person discover what they actually want to build when they have NO idea and NO direction
  yet — not even an industry, a skill to lean on, or a seed. Use this skill when the user wants to
  start *something* but is staring at a blank slate and wants to be interviewed and excavated rather
  than handed generic market ideas — triggers include "I want to build something but have no idea
  what", "help me figure out what to do", "I don't know what I want to make", "I want to start a
  business/be a solopreneur but don't know in what", "help me find my direction", "what should I do
  with my skills", "I'm stuck at zero", or any blank-slate, pre-idea moment. It is the FRONT of the
  idea pipeline: it elicits the person's edge, interests, frustrations, constraints, and what a good
  outcome means to *them*, then outputs a personal "edge map" that becomes the frame for
  `ideakit-generate`. It is NOT for users who already know their domain/skills and just want idea
  options (go straight to `ideakit-generate`), NOT for expanding a direction they already have (use
  `ideakit-explore`), and NOT for validating a chosen idea (use `ideakit-validate`).
---

# Ideakit — Discover (blank slate → a direction that fits you)

Take a person who has **nothing yet** — no idea, and often not even a domain or a stated skill — and
help them discover what they actually want to build. The output is not a list of market ideas (that's
`ideakit-generate`'s job). The output is a **portrait of the person**: their edge, what energizes
them, the problems they can't stop noticing, their real constraints, and what "good" looks like for
*them* — captured as an **edge map** that hands forward as a rich frame so the ideas sourced next are
*theirs*, not generic.

## The governing principle (read first — everything below derives from this)

**Excavate the person before you source the market — and excavate from evidence, not from polling.**

Two failures sit at the front of every "I don't know what to build" conversation, and this skill
exists to counter both. They're two halves of one principle:

1. **Excavate, don't poll.** The naïve move is to ask "so, what do you want to build?" — but a person
   who's at zero *cannot answer that directly*, and if pushed they'll **confabulate**: invent a
   plausible-sounding want on the spot that isn't really theirs. (This is the same reason "would you
   use this?" is a useless question — see The Mom Test.) Latent wants don't surface by asking for
   them; they surface from **evidence**: what the person has actually spent time, money, and attention
   on; what they rant about; what they lose track of time doing; how they *react* to concrete options.
   People are far better at *reacting and recognizing* than at *generating from a blank page* — so put
   real signal and real options in front of them and read the reaction.

2. **Person before market — fit is what makes a direction survivable.** `ideakit-generate` can produce
   a hundred market opportunities, but a direction that doesn't fit *this* person — their skills,
   their energy, the life they want, what they'd find meaningful — is one they'll abandon. So the job
   here is **founder–direction fit**: discover who the person is first, and only then let the market
   stage fill that shape with concrete ideas. A great idea pointed at the wrong person is a non-starter.

Everything in this skill is one of these two halves applied to a step. The skill's value is *discovery
of the person*; concrete ideas, scoring, and validation come from the downstream stages.

**What this is and isn't.** This is structured **self-discovery elicitation** — a sharp intake
interview, not therapy, not a personality quiz, not life coaching. It cares about the person, stays
warm, and never pries into sensitive territory; but its north star is a *buildable direction*, and
every question earns its place by moving toward one.

## The pipeline this skill sits in

```
[user: blank slate]  →  ideakit-discover (THIS)  →  ideakit-generate  →  ideakit-explore  →  ideakit-validate  →  ideakit-present
                        excavate the person          source ideas         expand+challenge      validate + PRD       make people act
                        → edge map (a frame)         (now personalized)
```

`ideakit-discover` is the new front of the line, *before* generate. Its job ends when it hands a
filled-in **edge map** forward — a rich frame that turns generate's "pick a sensible default and
proceed" into "source against a real person."

**Routing — make sure this is the right tool:**

- If the user **already knows their domain, skills, or the kind of thing they want** (even loosely:
  "ideas in fintech", "something with my Python skills", "a SaaS for dentists") → they don't need
  excavation. Hand straight to `ideakit-generate`; don't make them sit through an interview they've
  effectively already answered.
- If the user **has a rough direction or seed** → `ideakit-explore` (expand it) or `ideakit-validate`
  (validate it).
- If the user is **truly at zero and wants to find what's theirs** → this skill.

When in doubt, ask one question: *"Do you already have a domain or skill you want to build around, or
are we starting from a totally blank page?"* The answer routes them.

## Host capability mapping

Use capabilities by intent, not by product-specific tool name:

- **User input**: ask **one** concise question at a time — this skill is a conversation, never a
  form. Use the host's structured-choice UI for react-to-concretes steps if available; otherwise
  offer options in plain text.
- **Research**: use the host's web/search/browser to fetch *concrete examples to react to* (real
  products, niches, founder stories, "a day in the life" of a path) — not market sizing. The goal is
  material the person can point at and say "that, not that."
- **Connected knowledge** (if available): if the user has connected email, docs, notes, or activity,
  you may — *only with their nod* — mine it for evidence of where their time and attention actually go.
  Never assume access to personal data; ask first.
- **No live research available**: rely on the person's own recollection and reactions; offer
  text-described concrete options instead of fetched ones.
- **Output**: deliver the edge map in chat; write it to a file/artifact if the host supports it
  (`outputs/<name>-edge-map.md`), because it's the handoff artifact the next stage consumes.

## Workflow

Five steps: **Set the frame → Excavate from evidence → Ladder to values & constraints → React to
concretes → Synthesize the edge map & hand off.** It's a conversation; move at the person's pace and
don't machine-gun the questions.

### Step 1 — Set the frame (name the blank slate, lower the pressure)

Confirm they're starting from zero, and *take the pressure off the impossible question*. Say plainly
that you won't ask "what do you want to build?" — because nobody can answer that cold — and that
instead you'll dig up clues together. Set the expectation: this is a short interview about *them*,
and a direction will fall out of it. Then ask the routing question above if it isn't already clear.

### Step 2 — Excavate from evidence (the heart of the skill)

Read `references/elicitation-techniques.md`. Surface signal from what's **already true about the
person**, not from hypotheticals. Move through these probes, one at a time, drilling into whatever
lights up — you do not need all of them; follow the energy:

- **Past behavior (Mom Test, turned inward).** What have they actually spent time, money, or late
  nights on — hobbies, rabbit holes, side projects, things they've taught themselves, communities
  they lurk in? *Behavior is the truth serum; stated interests are cheap.*
- **The rant test.** What do they complain about repeatedly? What's broken in their world or their
  work that they can't stop noticing? Chronic irritation is a pointer to a problem they're already
  oriented to.
- **Energy audit.** What work makes them lose track of time, and what drains them even when they're
  good at it? Direction has to sit on the *energizing* side or it won't be sustained.
- **Unfair advantage they undervalue.** Skills, access, audiences, lived experience, or domain
  knowledge they have that most people don't — *especially* the ones they wave off as "everyone can
  do that." People are blind to their own edge; name it back to them.

Capture answers in the person's own words. Quantify where natural ("spent 200 hours modding X", "been
in this Discord 3 years"). Don't interpret yet — collect.

### Step 3 — Ladder to values & constraints (the "why" and the "within what")

Read the laddering section of `references/elicitation-techniques.md`. Now climb from the surface
answers to what's underneath, and pin the box the direction must fit inside:

- **Ladder up.** For the things that lit up in Step 2, ask "why does that matter to you?" two or three
  times until you reach a stable value (autonomy, mastery, helping a specific group, status, freedom,
  curiosity, building a legacy). The value is the real compass; surface answers are just where it
  showed up.
- **Life-shape constraints.** What does a good outcome look like *for them* — a calm income alongside
  a job, a full-time business, something that funds a particular life, learning over earning? How much
  time, money, and risk can they actually put in? Solo or with others?
- **No-gos.** What will they *not* do — industries, audiences, ways of working, "not another B2B SaaS"
  — even if it'd make money. Constraints sharpen discovery; they're not limitations to argue with.

### Step 4 — React to concretes (recognition beats generation)

People can't name what they want, but they can *recognize* it instantly. So stop asking them to
generate and give them things to react to. Read `references/elicitation-techniques.md` (projective &
react-to-concretes). Based on Steps 2–3, put **3–5 deliberately different concrete sketches** in front
of them — real example products/niches/paths (fetch them if research is available), or short
"you could be the person who ___" vignettes spanning different shapes (a maker, a service, an
audience/creator path, a tool, a community). Then read the reaction:

- What do they lean toward, recoil from, or immediately want to modify? The *recoil* is as
  informative as the attraction.
- Use a projective prompt to loosen latent wants: *"If you had a fully funded year and couldn't fail,
  what would you secretly try?"* or *"What would you build just for yourself, even if no one paid?"*
- Their edits ("that, but for ___ instead") are gold — they're the person designing the direction
  without realizing it.

This step is what separates discovery from a survey: the signal comes from *reaction*, not
self-report.

### Step 5 — Synthesize the edge map & hand off

Read `references/edge-map-template.md`. Reflect everything back as a tight **edge map** — a portrait
of the person plus the 2–3 candidate *directions* (not finished ideas) that fit them, each traced to
the evidence that points there. Then confirm it's right before handing off.

```
## Edge map — [name/handle]

**Who you are (the edge):** [skills, unfair advantages, domain knowledge — incl. the ones they undervalue]
**What energizes you:** [the lose-track-of-time work] · **What drains you:** [avoid building around this]
**Problems you can't stop noticing:** [the rants, in their words]
**What "good" looks like for you:** [life-shape: calm income / full-time / fund a life / learn] · **Risk/time/money you can put in:** [...]
**Core values driving this (laddered):** [autonomy / mastery / helping group X / freedom / ...]
**No-gos:** [...]

### Candidate directions (not ideas yet — frames for sourcing)
1. **[direction]** — fits because [evidence from Steps 2–4]. Shape: [maker / service / audience / tool / community].
2. ...
3. ...

**Riskiest thing we're still guessing about you:** [the open question]
```

Then offer the hand-off explicitly: *"This is the frame. Want me to send it to `ideakit-generate` to
source concrete, ranked ideas aimed at *these* directions — so what comes back is yours, not generic?
Or sit with one direction in `ideakit-explore` first?"*

The person confirms the edge map before anything advances. This skill discovers and recommends; it
never decides what they should do.

## Operating principles

All of these are the governing principle (excavate, don't poll · person before market) applied — not a
flat checklist.

**Excavate, don't poll:**
- **Evidence over hypotheticals.** Trust what they've *done* over what they *say* they want. When you
  must ask about the future, anchor it in the past ("you spent two years on X — what about it held you?").
- **Don't lead, don't confabulate-by-proxy.** Don't feed them a want and let them agree to be
  agreeable. Ask open, then go quiet. A confident wrong direction is worse than an honest "still fuzzy."
- **Recognition beats generation.** When they're stuck, stop asking them to invent — give them
  concretes to react to and read the reaction.

**Person before market:**
- **Fit is the whole point.** A direction must sit on their energy, their edge, and the life they want,
  or they won't sustain it. Optimize for founder–direction fit, not for the biggest market.
- **Name the edge they can't see.** People dismiss their own advantages as ordinary. Reflect them back
  explicitly — that's often the single most valuable moment in the session.
- **Hand off a frame, don't hoard.** Output is an edge map that *feeds* generate, not a finished idea.
  Resist jumping ahead to solutions; that's a later stage's job.

**Care for the person (this touches identity and direction):**
- **Warm, not clinical.** This is a sharp intake interview, not therapy, a personality test, or life
  coaching. Care about the person and keep it light; don't over-interpret or pop-psychologize.
- **Don't pry.** Go only as deep into personal history as the *direction* needs. If something sensitive
  surfaces, be kind, don't dig, and steer back to the buildable.
- **The person owns it.** Recommend directions with conviction, but they choose. "I don't know yet" is
  a legitimate place to pause, not a failure to fix.

## Reference files

- `references/elicitation-techniques.md` — the named methods this skill runs on: Mom Test (turned
  inward), laddering, projective prompts, react-to-concretes, critical-incident probing, and the
  energy audit. The "how" behind Steps 2–4.
- `references/edge-map-template.md` — the full edge-map output: every field, what good looks like, and
  how it maps onto `ideakit-generate`'s Step 1 frame so the handoff is clean.
