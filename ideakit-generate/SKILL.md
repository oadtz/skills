---
name: ideakit-generate
description: >
  Generate new business and startup ideas from scratch by scanning trends and mining real
  problems, then rank them with proven evaluation criteria. Use this skill whenever the user
  wants to FIND, GENERATE, or BRAINSTORM business or startup ideas but does NOT yet have a
  specific idea in hand — triggers include "what should I build", "give me startup ideas",
  "help me find a business idea", "I want to start a company but don't know what", "ideas for
  [industry/market]", "what business could I start with [skill/budget]", "where are the
  opportunities in [space]", or any request for idea generation, opportunity discovery, or
  "what's worth building right now". This is the UPSTREAM idea-sourcing skill: it produces a
  ranked table of raw ideas. It is NOT for refining an idea you already have (hand off to
  ideakit-validate for that) and NOT for general product-feature brainstorming on an existing product
  (use ideakit-explore).
metadata:
  version: "1.0.0"
---

# Ideakit — Generate (idea sourcing)

Generate fresh business/startup ideas for someone who does **not** yet have an idea, then
rank the best ones and hand the winner off for deep validation. The user brings *constraints
and direction* (an industry, their skills, a business model, a budget) — not an idea. The
skill brings the ideas.

## Why this skill exists (and what it must guard against)

Large language models are, per recent research, genuinely good at producing **novel** ideas —
in a Stanford human study (Si, Yang & Hashimoto, 2024) LLM-generated research ideas were rated
*more* novel than those of expert researchers. But the same body of work shows two consistent
weaknesses this skill is explicitly designed to counter:

1. **Weaker on feasibility.** LLM ideas score lower on "can this actually be done." → This skill
   never claims an idea is validated. It scores feasibility honestly and routes the winner to
   `ideakit-validate` for deep validation, with the human making the final go/kill call.
2. **Low diversity at scale — ideas converge into near-duplicates.** Naively asking for "20
   ideas" produces a cluster of variations on one theme. → This skill enforces diversity
   structurally by partitioning the idea space *before* generating (see `references/diversity.md`).
   Do not skip this; it is the single biggest quality lever.

Keep these two facts in mind throughout. The skill's value is novel idea *sourcing*; rigor and
feasibility come from the downstream steps and the human.

## The pipeline this skill sits in

```
[user: constraints]  →  ideakit-generate (THIS)  →  ideakit-explore  →  ideakit-validate  →  build
                         generate + rank        expand + challenge        validate + PRD
```

`ideakit-generate` is the front of the line. Its job ends when it hands a ranked shortlist forward.

## Workflow

Five steps: **Frame → Scan → Generate → Score → Rank & Hand off.** Do not skip Scan or the
diversity partition inside Generate — those are what separate this from a generic brainstorm.

### Step 1 — Frame (gather constraints, not ideas)

Use the `AskUserQuestion` tool (or plain questions if the user is mid-conversation) to pin down
direction. Ask only what's missing; infer the rest from context. Cover:

- **Domain / industry** the user knows or cares about (their "edge" — where they live closer to
  the future than most people).
- **Unfair advantage**: specific skills, audience, network, or experience they already have.
- **Business model preference**: SaaS, AI-native service, marketplace, SMB/local, content, etc.
- **Resource envelope**: rough budget, time, solo vs. team, technical or not.
- **Constraints / no-gos**: things they will not do (industries, models, geographies).

If the user gives almost nothing ("just give me ideas"), pick a sensible default frame, state it
in one line, and proceed — don't stall. You can widen later.

### Step 2 — Scan (build raw signal)

Generate ideas *from evidence*, not from thin air. Pull current signal with `WebSearch` and any
connected tools. See `references/trend-sources.md` for the source list and ready-made query
patterns. At minimum, run several **parallel** searches across:

- Trend/authority sources (YC Requests for Startups, a16z Big Ideas, etc.) for where the puck
  is going.
- Problem/complaint sources (Reddit, Hacker News, GitHub issues, review sites, niche forums)
  for pain people express in their own words.
- The user's specific domain, to ground ideas in their edge.

Capture raw problems and signals verbatim before interpreting. Quantify pain where you can
("47 GitHub issues asking for X", "top complaint in r/foo").

### Step 3 — Generate (with enforced diversity)

**Before generating, partition the idea space.** Read `references/diversity.md` and lay out the
dimensions you'll vary across (market segment, mechanism, business model, wedge, who-you-replace).
Then generate **10–20 raw ideas that deliberately spread across those partitions**, applying the
generation lenses in `references/frameworks.md` (Live-in-the-future, Jobs-to-be-Done,
First-Principles, SCAMPER, Inversion). Aim for genuine spread — if three ideas are variations on
one theme, collapse them to one and generate a structurally different one.

Each raw idea is one or two sentences: *who* has *what* pain, and the *shape* of the solution.
Don't polish yet.

### Step 4 — Score

Score every idea against the rubric in `references/scoring.md`. The six dimensions:

1. **Pain** (urgent, deep, real?) — Paul Graham
2. **Market / Starving Crowd** (hungry, able to pay, reachable, growing?) — Hormozi
3. **Secret** (what do you see that others don't yet believe?) — Thiel
4. **Job** (what is the customer hiring this to do?) — Christensen
5. **Survivability** (if ChatGPT/Claude ships this natively tomorrow, why do you still win?) — 2026 reality
6. **Feasibility** (riskiest assumption, and how cheaply it can be tested?) — Lean Startup

Be honest on feasibility and survivability especially — that's where LLM-generated ideas tend to
be over-optimistic. A low score is useful information, not a failure.

### Step 5 — Rank & hand off

Produce a ranked table of the top 3–5 ideas. Use this exact structure:

```
## ไอเดียที่คัดมาแล้ว (Ranked shortlist)

| # | ไอเดีย (1 ประโยค) | ตลาด/ฝูงชน | Secret / ทำไมตอนนี้ | คะแนนรวม | สมมติฐานเสี่ยงสุด |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | X/30 | ... |
...

### เหตุผลของอันดับ 1–3
- **#1 [name]** — why it leads, its main risk, cheapest next test.
- ...

### ตัวที่ตัดทิ้งและเหตุผล
- [idea] — killed because [reason].
```

Then offer the hand-off explicitly: *"อยากให้ส่งอันดับ 1 (หรือตัวที่คุณเลือก) ต่อให้ `ideakit-validate`
ทำ deep validation แล้วออกมาเป็น PRD ไหม? หรืออยากเอาเข้า `ideakit-explore` เพื่อขยาย/ท้าทายก่อน?"*

The human chooses what advances. This skill recommends but never decides go/kill.

## Operating principles

- **Constraints in, ideas out.** If the user already has a specific idea, this is the wrong
  skill — point them to `ideakit-validate` and stop.
- **Evidence beats cleverness.** Every idea should trace to a real signal from Step 2, not to a
  clever-sounding phrase. Cite sources inline where you can.
- **Diversity is a feature, not noise.** A spread of structurally different ideas is more
  valuable than five polished variations of the same one.
- **Honest scoring.** Don't inflate feasibility or survivability to make an idea look good. The
  downstream steps and the user depend on a truthful read.
- **Hand off, don't hoard.** The skill's output is a shortlist plus a recommendation to advance —
  not a finished plan.

## Reference files

- `references/frameworks.md` — generation lenses and scoring frameworks, with how-to-apply notes.
- `references/diversity.md` — the partition method that keeps generated ideas from converging
  (read this every run before Step 3).
- `references/scoring.md` — the six-dimension scoring rubric with a 0–5 scale per dimension.
- `references/trend-sources.md` — where to scan and copy-ready search query patterns.
