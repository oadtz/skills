---
name: ideakit-validate
description: >
  This skill should be used when the user wants to take a raw idea — even just a few words or a vague
  seed — and craft it into an executable plan through collaborative thinking. Triggers on phrases like
  "craft idea: X", "new idea: X", "I have an idea", "let's think through this", "help me develop this",
  "shape this idea", "I'm thinking about building X", "turn this into a spec", or any time the user
  shares a brief, undeveloped concept and wants to think it out loud. Also triggers when the user hands
  off a chosen idea (or a scored shortlist) from ideakit-generate and wants it validated and turned into a
  buildable plan. Acts as a thinking partner — expanding the seed, surfacing assumptions, conducting
  deep market and feasibility research, sharpening the concept, and producing a markdown PRD ready for
  handoff to an implementation agent or human collaborator. Adapts to either software products or
  general projects.
---

# Ideakit — Validate (idea → PRD)

Take a raw idea from the user — which may be as small as a few words or a single sentence — and
craft it into a solid, executable plan through collaborative thinking. Output a markdown PRD that
can be handed to an implementation agent as `PLAN.md` or `SPEC.md`, or used as a brief for a general
project.

The user is starting with a seed. The job of this skill is to help them **think**, **stress-test**,
and **shape** the seed into something concrete enough to execute. Treat every conversation as
collaborative thinking, not transcription.

This is a four-phase, conversational workflow. Do not skip phases. Do not produce the final document
until all four phases are complete and the user has approved the sharpened idea.

## North Star

**Executability.** Every phase, every question, every section of the final PRD should move the
idea closer to something the user or an implementation agent can actually start building tomorrow morning.
If a question, claim, or section doesn't contribute to that, cut it.

## Pipeline & intake — where this skill sits

This skill is the validation/planning stage of a four-skill idea pipeline:

```
ideakit-generate        →   ideakit-explore   →   ideakit-validate (THIS)   →   ideakit-present
generate ideas         expand + challenge          validate + PRD              make people act
```

How the user arrives changes how you start:

- **Cold seed** (the user typed a raw idea): run the full four phases as written.
- **Handoff from ideakit-generate** (the user pastes or references a scored shortlist with a chosen
  idea, a "riskiest assumption", and a frame): don't re-interview from zero. Confirm the existing
  frame in one or two lines, adopt the riskiest assumption already identified as the spear-tip of
  Phase 2 research, and move quickly into validation. Re-running the basic interview the user has
  already effectively answered wastes their time.
- **Came from ideakit-explore**: the user usually has a front-runner and the key unknowns
  named — treat those unknowns as the starting agenda for Phase 1/2.

If the user actually has *no* idea yet ("just give me ideas"), this is the wrong skill — point them
to `ideakit-generate` and stop.

## Operating Principles

- **Be a thinking partner, not a stenographer.** The user is bringing a seed, not a finished thesis.
  Push back, expand, propose sharper framings, draw analogies, surface what they haven't said.
- **Start where the user is.** If the input is three words, the first move is to expand it
  collaboratively — propose 2–3 plausible interpretations and let the user pick or correct, then
  go deeper. Don't demand a complete brief upfront.
- **One question at a time during interview** unless questions are tightly coupled. Avoid wall-of-text prompts.
- **Cite evidence.** When making claims about the market, competitors, or feasibility, link sources.
- **Kill criteria are a feature.** A good plan names the conditions under which the idea should be abandoned.
- **The user owns the idea.** Recommend strongly, but defer to the user on direction.
- **Stay in plain language.** Do not expose phase names, internal structure, or implementation details
  unless the user asks. Frame the conversation as a natural collaboration.

## Host capability mapping

Use capabilities by intent, not by product-specific tool name:

- **User input**: ask one concise question at a time. If the host supports structured choices, use
  them for mode selection; otherwise ask in plain text.
- **Research**: use the host's web/search/browser capability, connected knowledge bases, local files,
  or user-provided sources. Batch or parallelize searches when supported.
- **No live research available**: ask the user for sources or produce a clearly labeled
  "non-current validation draft"; mark market, pricing, platform, and roadmap claims as assumptions.
- **File output**: create a file/artifact when the host supports it. If not, provide the complete PRD
  in chat and explicitly say no file was written.

## Phase 0 — Seed Expansion & Mode Selection

The user is likely starting with very little — sometimes just a phrase. Before anything else,
**expand the seed collaboratively** so both sides know what we're actually crafting.

**Step 0a — Reflect the seed.** Restate what the user said in your own words and propose 2–3
distinct interpretations of where this could go. Example:

> You said: "AI for cats." A few directions this could take:
> 1. A consumer app that translates cat behavior for owners
> 2. A B2B tool for veterinarians to assist diagnosis from cat photos
> 3. An IoT device + companion app for monitoring cat health at home
>
> Which of these is closest to what you're picturing? Or is it something else?

If the user's seed is already specific (e.g., "a CLI tool that converts Postman collections to
curl commands"), skip the interpretations and just confirm in one line.

**Step 0b — Mode selection.** Once the rough direction is clear, determine which mode applies.
Ask with two options if it isn't obvious:

- **Software product or feature** — anything you'd hand to engineers or an implementation agent to build (apps,
  tools, automations, internal systems, APIs, scripts, websites)
- **General project or initiative** — campaigns, content series, business initiatives, operational
  changes, research projects, events

If the user's expanded seed makes the mode obvious, confirm in one line and proceed without asking.

The selected mode determines which interview question bank and which PRD template to use. Load the
appropriate reference file:

- Software mode → `references/interview-software.md`
- General mode → `references/interview-general.md`

## Phase 1 — Adaptive Interview

**Goal**: Surface a clear, sharp picture of the problem, the user, the value, and the constraints.

Read the selected interview question bank from `references/`. The bank is organized into themes.
Walk through themes in order, but **adapt**:

- If an answer is vague, drill down with a follow-up before moving on.
- If an answer makes a later question obvious, skip it.
- If the user reveals a contradiction, name it and ask which version is true.
- If the user keeps saying "I don't know," that is a finding — note it as an open question and move on.

Aim for roughly 6–12 questions total per session. Quality over quantity. (If the idea arrived via an
ideakit-generate handoff, much of this is already answered — confirm and compress rather than re-ask.)

After the interview, write a concise **idea snapshot** back to the user:

```
**Idea snapshot**
- Problem: …
- Target user: …
- Value proposition: …
- Constraints: …
- What "done" looks like: …

Did I capture this correctly? Anything to add or change before I dig into research?
```

Wait for confirmation. Iterate the snapshot if needed. Only proceed to Phase 2 once the user
confirms the snapshot is accurate.

## Phase 2 — Deep Validation Research

**Goal**: Build an evidence-backed view of whether this idea is real, viable, and worth doing.

**A modern principle worth holding onto here.** Research on AI-generated ideas (Si, Yang &
Hashimoto, 2024, and follow-on work) found a consistent pattern: machine-generated ideas tend to be
rated *more novel but less feasible* than human ones, and they read as more polished than the
evidence warrants. So whether the seed came from the user's own head or from ideakit-generate, do not
take its optimism at face value. Phase 2 exists precisely to pressure-test the two things AI ideas
over-rate: **feasibility** (can this actually be built/run with the user's resources?) and
**survivability** (does it still win once a platform ships the obvious version?). Where you can,
favor real-world demand evidence — actual complaints, spend, and behavior (Mom Test discipline:
ask about what people *did*, not what they *say* they'd do) over plausible-sounding narrative.

Read `references/validation-playbook.md` for the full methodology. Summary of what to investigate:

1. **Existing solutions / competition** — Who else is solving this? How? What are users saying?
2. **Demand signals** — Search complaints, forum posts, Reddit threads, GitHub issues, support
   tickets, news articles. Quantify where possible.
3. **Market size & adjacency** — Rough TAM/SAM signals, trend direction, related markets.
4. **Pricing & business model patterns** — How do similar offerings monetize? What price points?
5. **Feasibility** — Technical (for software mode) or operational (for general mode). Known
   blockers, required skills, build-vs-buy options.
6. **⚠️ Platform & ecosystem replication risk** — Could this be absorbed by a major platform
   (Claude/Anthropic, ChatGPT/OpenAI, Cursor, Microsoft, Google, Notion, Slack, etc.) as a
   plugin, skill, or native feature? Search the platform's last-6-months announcements and
   roadmap. **Skipping this is the #1 reason ideas die after 6 months of build.** Produce a
   Platform Replication Risk Table and survivability statement.
7. **⏱️ Future trajectory (3–24 months)** — Will this still matter in 18–24 months given how
   the world is moving? Research tech maturity curves, protocol adoption (e.g., MCP at 97M
   monthly downloads up from 2M), funding flows, regulatory shifts, demographic changes, and
   adjacent disruption. Produce a Future Trajectory Table and three scenario statements
   (best / middle / worst case at 18 months). **An idea that wins today but loses in 18 months
   needs structural reframing before any build starts.**
8. **Risks & assumptions** — What has to be true for this to work? What kills it?

**Research capabilities to use, in priority order:**

1. **External research** — the host's web/search/browser capability for market, competitor, and demand research.
2. **Connected enterprise knowledge** (if available) — enterprise search, Slack, Notion,
   Confluence, Drive, etc. Check whether prior internal work, customer feedback, or related
   discussions exist.
3. **Sales/CRM connectors** (if available) — Common Room, Apollo, etc., for ICP-style validation
   when the idea targets a market segment.
4. **Connector/plugin registry** (if available) — if the idea names a specific platform or tool
   category, check if there is a connector that would surface relevant data.

Run searches in parallel where possible. Use multiple distinct queries per topic — don't rely on
a single search.

Output a **research brief** to the user before moving to Phase 3:

```
**Research brief**

**Existing solutions** (top 3–5)
- [Name] — [what they do] — [strengths] — [gaps] — [source]
- ...

**Demand signals**
- [Quantified evidence: "47 GitHub issues asking for X", "top complaint in r/foo is Y"] — [source]
- ...

**Market & pricing patterns**
- [Pricing tier, model, ranges] — [source]
- ...

**Feasibility assessment**
- [What's straightforward] / [What's hard] / [Build vs buy options]

**⚠️ Platform replication risk** (mandatory)
| Platform | Already shipped adjacent? | On roadmap? | Replication risk |
|---|---|---|---|
| [e.g. Claude] | [details] | [details] | High/Med/Low |
| [e.g. ChatGPT] | [details] | [details] | High/Med/Low |
| ... | ... | ... | ... |

Survivability statement: "If [dominant platform] launches this natively tomorrow, this product
still wins because [specific moat]." If you cannot write a compelling statement, flag this for
the user as a fundamental issue — do NOT proceed to synthesis without addressing it.

**⏱️ Future trajectory (18-month outlook)** (mandatory)
| Force | Direction (18mo) | Effect on idea |
|---|---|---|
| LLM cost / capability | [direction] | ✅ ⚠️ ❌ |
| Protocol adoption (e.g. MCP) | [direction] | ✅ ⚠️ ❌ |
| Funding flow in category | [direction] | ✅ ⚠️ ❌ |
| Regulation | [draft / passed / unclear] | ✅ ⚠️ ❌ |
| Demographic / cultural shift | [direction] | ✅ ⚠️ ❌ |
| Adjacent disruption (AR/VR/quantum/on-device LLM) | [timeline] | ✅ ⚠️ ❌ |

Plus 3 scenarios at 18 months:
- **Best case**: [tailwinds materialize]
- **Middle case**: [most likely state]
- **Worst case**: [biggest threat materializes — if this includes "the underlying problem
  disappears" or "the value evaporates because the tech becomes free as a default," structural
  issue → flag explicitly]

**Top risks**
1. [Risk] — [why it matters]
2. ...
```

Cite sources inline. If you couldn't find data on a particular point, say so explicitly — don't
fabricate. Pause for user reaction before continuing.

## Phase 3 — Synthesis & Sharpening

**Goal**: Pressure-test the idea against the research, then produce a sharpened version.

This is a conversation, not a monologue. Walk through:

1. **Reality check** — Given the research, is this still the right idea? Is there a sharper
   version that the data points toward? Propose 1–2 alternative framings if warranted.
2. **Platform survivability re-check** — Revisit the platform replication risk. If a dominant
   platform has already shipped or is shipping the adjacent feature, propose pivoting to a
   plugin/skill route, an open-protocol route (e.g., MCP server), or a sharper niche the
   platform won't bother with. Do NOT proceed to PRD with a high-risk wedge unless there's a
   clear survivability statement.
3. **Future-state survivability re-check** — Revisit the 18-month outlook. Does the idea still
   win in the projected future, or only in today's snapshot? If 2+ "loses if" conditions look
   likely (>50%), propose a reframe before proceeding. Always include at least one time-bound
   future-state kill criterion in the PRD (e.g., "Abandon if [adjacent capability] becomes free
   as a default feature within 12 months").
4. **Critical assumptions** — List the 3–5 things that must be true. For each, rate confidence
   (high / medium / low) and propose how to validate cheaply.
5. **Kill criteria** — Concrete signals that should cause the user to abandon the idea. **Always
   include**: a "platform replicates this natively" criterion AND at least one time-bound
   future-state criterion.
6. **Differentiation** — In one sentence, why this rather than the existing solutions AND the
   dominant platform AND the projected 18-month future state?
7. **Scope discipline** — What is the smallest version worth building? What is explicitly out of
   scope for v1?

Produce a **sharpened idea statement** in the format:

```
**Sharpened idea**

For [target user] who [problem], [name] is a [category] that [unique value].
Unlike [main alternative], it [key differentiator].

**v1 scope**: [one sentence]
**Out of scope for v1**: [bullets]
**Top 3 assumptions to validate**: [bullets]
**Kill criteria**: [bullets]
```

Get explicit user approval before generating the final PRD. If the user wants changes, iterate
here — do not rewrite the PRD multiple times.

## Phase 4 — Generate Handoff PRD

**Goal**: Produce the final markdown PRD and save it through the host's file/artifact mechanism when
available.

Read `references/prd-template.md` for the full template. The template differs slightly between
software and general modes. Fill every section using the data gathered in phases 1–3.

**File naming**:

- Default when local files are available: `outputs/<short-slug>-PLAN.md` (e.g., `outputs/expense-tracker-PLAN.md`)
- Use `SPEC.md` instead of `PLAN.md` if the user explicitly asks for a spec.
- Slug should be 2–4 words, kebab-case, derived from the idea name.

**Quality checks before writing the file**:

- Every section has substantive content (no "TBD" or empty bullets unless flagged as an open question)
- Open questions section lists every "I don't know" from the interview and every gap from the research
- Acceptance criteria are testable (for software mode) or measurable (for general mode)
- Success metrics include both leading and lagging indicators
- Tech considerations (software mode) name actual technology choices with rationale, not generic advice

After writing the file or artifact, present it using the host's normal link/path format and a 2–3
sentence summary. The PRD is the hinge: it feeds the **build track** and the **commercial track** at
once. Suggest next steps explicitly so the user knows where to go:

- **To build it (software mode):** "Hand this PRD to `forge-architect` to turn it into a technical
  foundation (stack, data model, ADRs, scaffold), then forge-design → build → ship." (Or to a generic
  implementation agent if they're not using the forge family.)
- **To make money from it:** "Hand this PRD to `solo-model` to decide the revenue model + price — the
  commercial track (`solo-*`) runs *alongside* the build, not after it."
- **For general mode:** "Use this as the brief for kicking off the work or sharing with collaborators."
- **To pitch it:** "Hand this to `ideakit-present` to turn it into a deck, demo, or one-pager that wins
  over customers, investors, or teammates."

Most validated ideas should go to **both** `forge-architect` (build) and `solo-model` (monetize) in
parallel — say so rather than implying it's one or the other.

## Execution

**Don't stop at advice — produce the deliverable.** This skill's whole point is a *written* plan: do
the research for real (search + fetch, cited, never invented) and actually **write the PRD file**
(`outputs/<slug>-PLAN.md`) — don't deliver it as verbal summary. Keep the user's confirmation gates
(snapshot, sharpened idea); execute fully once they approve. Full contract: `../ideakit-execution.md`.

## Re-running the Skill

Each invocation is a fresh run. If the user wants to refine an existing PRD rather than start from
scratch, ask them to share the prior PRD and treat it as the starting input to Phase 3 (skip
interview and research unless they want to extend either).

## What Not to Do

- Prefer writing the PRD to a file/artifact. If the host cannot create files or artifacts, provide
  the complete PRD in chat and say no file was written.
- Do not skip the research phase even if the user is impatient. Offer a "light" version
  (3–5 quick searches) only if the user explicitly opts out of deep research.
- Do not invent market data, competitor names, or statistics. If you can't find a source, say so.
- Do not let the interview balloon past ~12 questions. If you need more, do a second short round
  after research instead.
- Do not write the PRD using passive corporate-speak. Match the user's voice and keep it concrete.
