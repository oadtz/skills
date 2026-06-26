---
name: ideakit-generate
description: >
  Generate new business and startup ideas from scratch by scanning trends and mining real
  problems, then rank them with proven evaluation criteria. Use this skill whenever the user
  wants to FIND, GENERATE, or BRAINSTORM business or startup ideas but does NOT yet have a
  specific idea in hand — triggers include "what should I build", "give me startup ideas",
  "help me find a business idea", "I want to start a company but don't know what", "ideas for
  [industry/market]", "what business could I start with [skill/budget]", "where are the
  opportunities in [space]", "give me ideas where the money is", "most lucrative ideas",
  "follow the money", "where's the money in [space]", or any request for idea generation,
  opportunity discovery, or "what's worth building right now". This is the UPSTREAM idea-sourcing
  skill: it produces a
  ranked table of raw ideas. It is NOT for refining an idea you already have (hand off to
  ideakit-validate for that) and NOT for general product-feature brainstorming on an existing product
  (use ideakit-explore).
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

## The governing principle (read first — everything below derives from this)

Every blind spot this skill has ever had — suppressing desire markets, ignoring non-Western signal,
chasing fads, judging on one criterion — is the *same* failure wearing different clothes: **a fixed
frame.** A generator reasons through a frame (which sources it scans + which lens it scores with),
and a frame is simultaneously what lets it see *and* what blinds it. You cannot out-checklist this by
adding one special-case rule per blind spot; that's an endless patch chase. There is one principle
instead, with two halves:

1. **Requisite Variety** (Ashby's Law: *only variety absorbs variety*; Munger's *latticework* — "to a
   man with a hammer, everything is a nail"). The opportunity space is wildly varied, so the
   generator must hold a matching variety of **inputs, lenses, and judgment criteria**. Insufficient
   internal variety → guaranteed systematic blind spots.
2. **Reflexivity** (*the map is not the territory*). The frame is always provisional. So the skill
   must make its own frame explicit, deliberately scan and generate *against* it, and treat its own
   scores as estimates, not verdicts.

Everything in this skill is one of these two applied to a stage — not a separate invention:

| Stage | What it is | Which half it serves |
|---|---|---|
| Coverage audit (Step 2) | vary your **inputs**; name & counter your source bias | Variety + Reflexivity |
| Diversity partitions (Step 3) | vary your **generative lenses**; spread, don't cluster | Requisite Variety |
| Multi-dimension rubric, incl. Pull = pain *or* desire (Step 4) | vary your **judgment criteria**; never score on one axis | Requisite Variety |
| Portfolio balance + fad check (Step 5) | **synthesize** varied bets; declare the mix; don't monoculture | Variety + Reflexivity |
| Honest scoring & "human decides" | scores are provisional; the frame can be wrong | Reflexivity |

**The rule that ends the patch chase:** when a *new* blind spot appears, do **not** add a new
special-case rule. Ask only — *which half was thin?* Was it missing input variety (fix via the
coverage audit's axes), lens variety (add/rotate a generative lens), judgment variety (was a whole
criterion absent?), or reflexivity (did we mistake our frame for the territory)? Strengthen the
*general* mechanism, and the specific blind spot dissolves along with its whole class.

## The pipeline this skill sits in

```
ideakit-discover  →  [user: constraints]  →  ideakit-generate (THIS)  →  ideakit-explore  →  ideakit-validate  →  ideakit-present/build
(blank slate → edge map)                      generate + rank        expand + challenge        validate + PRD
```

`ideakit-generate` turns *constraints* into ranked ideas. Its job ends when it hands a ranked
shortlist forward.

**Intake — make sure the user actually has constraints to work from:**

- If the user **has any direction at all** — a domain, a skill to lean on, an audience, a business
  model preference — proceed; that's all this skill needs.
- If the user is at a **true blank slate** ("I don't even know what I want to do", no domain, no
  skill named), don't just default-frame and produce generic market ideas. Point them to
  `ideakit-discover` first — it excavates the person and returns an **edge map** that makes the ideas
  here personal instead of generic.
- If the user **arrives with an edge map** from `ideakit-discover`, use it directly as the Step 1
  frame: its candidate directions become your diversity partitions (Step 3) and its no-gos become
  hard filters. Don't re-interview what discover already established.

## Host capability mapping

Use capabilities by intent, not by product-specific tool name:

- **User input**: ask one concise question; if the host supports structured question UI, use it,
  otherwise ask in plain text.
- **Research**: use the host's available web/search/browser/connected-knowledge capability. Batch or
  parallelize searches when the host supports it.
- **No live research available**: ask the user for sources or continue only as a clearly labeled
  "non-current draft"; mark market, trend, and platform claims as assumptions.
- **Output**: return the ranked shortlist in chat; if the host supports artifacts/files, use them only
  for optional supporting notes, not as a substitute for the summary.

## Workflow

Five steps: **Frame → Scan (+ coverage audit) → Generate → Score → Synthesize & Hand off.** Do not skip
the coverage audit inside Scan or the diversity partition inside Generate — those two guards are what
separate this from a generic brainstorm and what keep it from quietly missing whole markets.

**Money-first framing (optional).** If the user asks for "ideas where the money is" (most lucrative /
follow the money), read `references/money-first.md` first. It doesn't change the five steps — it
re-points Scan toward money evidence (funding flows, budgets, pricing, WTP), re-weights scoring toward
Market/Starving Crowd + solo-reachability, and binds you to one hard rule: **every "the money is here"
claim must cite real evidence fetched this run — never vibes; if you can't source it, it's a hypothesis,
not a fact.** It rests on named principles (Hormozi's Starving Crowd, Profit Pools, Value Migration,
painkiller-vs-vitamin) and carries the solo correction: money is *reachable, fast-paying* buyers, not
the biggest TAM.

### Step 1 — Frame (gather constraints, not ideas)

**If an `ideakit-discover` edge map is in hand, the frame is already built** — adopt it: the edge map's
"who you are" and no-gos fill the fields below, and its candidate directions seed Step 3's partitions.
Confirm it in a line and move to Step 2 rather than re-interviewing.

Otherwise, ask one concise question at a time to pin down direction. Use the host's structured question
UI if available; otherwise ask in plain text. Ask only what's missing; infer the rest from context. Cover:

- **Domain / industry** the user knows or cares about (their "edge" — where they live closer to
  the future than most people).
- **Unfair advantage**: specific skills, audience, network, or experience they already have.
- **Business model preference**: SaaS, AI-native service, marketplace, SMB/local, content, etc.
- **Resource envelope**: rough budget, time, solo vs. team, technical or not.
- **Constraints / no-gos**: things they will not do (industries, models, geographies).

If the user gives almost nothing ("just give me ideas") but *does* have a domain or skill, pick a
sensible default frame, state it in one line, and proceed — don't stall. You can widen later. But if
the user is at a true blank slate with no domain, skill, or direction to name, that's the signal to
route them to `ideakit-discover` first (see Intake above) rather than default-framing into generic ideas.

### Step 2 — Scan (build raw signal)

Generate ideas *from evidence*, not from thin air. Pull current signal with the host's available
research capability: web/search/browser, connected knowledge bases, local files, or user-provided
sources. See `references/trend-sources.md` for the source list and ready-made query patterns. At
minimum, run several batched/parallel searches when the host supports it across:

- Trend/authority sources (YC Requests for Startups, a16z Big Ideas, etc.) for where the puck
  is going.
- Problem/complaint sources (Reddit, Hacker News, GitHub issues, review sites, niche forums)
  for pain people express in their own words.
- Culture/desire sources (TikTok, X, Wattpad/Webtoon, streaming & app-store charts, fandom subs,
  Google Trends) for what people *want, love, and rally around* — the desire-driven markets the
  first two source types are blind to. Don't skip this; it's how the skill historically missed
  whole categories like the BL/Y-series boom.
- The user's specific domain, to ground ideas in their edge.

Capture raw problems and signals verbatim before interpreting. Quantify pain or desire where you can
("47 GitHub issues asking for X", "top complaint in r/foo", "12k fan works around Y"). Keep source
links beside each signal.

**Then run the coverage self-audit before generating.** The source list above still has a horizon —
any fixed list does. Read `references/coverage-audit.md` and walk the *axes of blindness* (value
type, geography/culture, who-pays, buyer sophistication, trend trigger, maturity, time horizon):
locate where your scan is skewed, then deliberately run 1–2 extra searches at the opposite ends most
relevant to the brief. This is the general mechanism that catches *unknown* unknowns — not just the
desire/fandom gap we already named, but whatever this particular brief is blind to. Note in one line
what you additionally scanned (recording "found nothing" is fine — it proves the axis was checked).

### Step 3 — Generate (with enforced diversity)

**Before generating, partition the idea space.** Read `references/diversity.md` and lay out the
dimensions you'll vary across (market segment, mechanism, business model, wedge, who-you-replace).
Then generate **10–20 raw ideas that deliberately spread across those partitions** (target ~12–15
across the cells you pick — one or more per cell is fine), applying the
generation lenses in `references/frameworks.md` (Live-in-the-future, Jobs-to-be-Done + Forces of
Progress, First-Principles, SCAMPER, Inversion, the Desire/Fandom lens, and Blue Ocean/ERRC +
Category Creation for net-new demand). Aim for genuine spread — if three ideas are variations on
one theme, collapse them to one and generate a structurally different one.

Each raw idea is one or two sentences: *who* has *what* pain **or want**, and the *shape* of the
solution. Don't polish yet.

**Spread gate — do not proceed to Step 4 until all are true** (this is the main guard against
regressing to a B2B/painkiller monoculture; full detail in `references/diversity.md` §5):

- [ ] at least **two different customer types**, AND
- [ ] at least **two different mechanisms/wedges**, AND
- [ ] at least one **"works today"** idea and one **"bets on a near-future capability"** idea, AND
- [ ] at least one **desire/identity-driven** idea (not only painkiller/utility) — *unless* the brief
  is explicitly a pure-utility domain.

If any box fails, regenerate the missing kind — don't proceed. An all-utility set almost always means
the culture/desire sources or the coverage audit were skipped; go back to Step 2.

### Step 4 — Score

Score every idea against the rubric in `references/scoring.md`. The six dimensions:

1. **Pull — Pain *or* Desire** (urgent problem? OR intense, identity-driven want?) — Paul Graham, expanded
2. **Market / Starving Crowd** (hungry, able to pay, reachable, growing?) — Hormozi
3. **Secret** (what do you see that others don't yet believe?) — Thiel
4. **Job** (what is the customer hiring this to do?) — Christensen
5. **Survivability / Power** (if ChatGPT/Claude ships this natively tomorrow, why do you still win?) — name the durable power behind the moat using Helmer's *Seven Powers*
6. **Feasibility** (riskiest assumption, and how cheaply it can be tested?) — Lean Startup

Be honest on feasibility and survivability especially — that's where LLM-generated ideas tend to
be over-optimistic. A low score is useful information, not a failure.

### Step 5 — Synthesize as a portfolio, then rank & hand off

Ranking is *synthesis*, not just sorting — apply the governing principle one last time so the
shortlist has requisite variety and you stay reflexive about the mix. Before writing the table:

- **Declare the mix.** State the shortlist's spread on two independent axes: **value type**
  (painkiller ↔ desire) and **durability of demand** (durable ↔ emerging/fad). These are *different*
  axes — a desire market can be centuries-durable (fandom, pets, faith) and a painkiller can be a
  fad. Don't conflate "desire" with "risky".
- **Balance, don't monoculture — but don't force 50/50.** Weight the mix by the *evidence* and the
  user's *edge*, and justify the weighting in one line. The rule is only: no axis should be all-one
  unless the brief explicitly demands it. An all-painkiller *or* all-desire shortlist is a frame
  failure; so is an all-fad one.
- **Flag fads explicitly (Painkiller / Vitamin / Candy + Lindy).** Tag each idea: *Painkiller*
  (needed), *Vitamin* (good, habitual, recurring), or *Candy* (instant but fleeting). Candy is the
  fad risk — keep it only if its demand is rooted in an enduring human drive (status, belonging,
  care, meaning, health, safety → Lindy-durable), otherwise discount it or pair it with a durability
  plan. This governs against trend-chasing without suppressing desire.

Produce a ranked table of the top 3–5 ideas. **Produce it in the user's language** — the template
below is illustrative (shown in Thai). The table is a *summary*; the full six sub-scores and the
one-line justification per dimension (required by `scoring.md`) live in the per-idea reasoning below
the table, not in the table itself.

```
## ไอเดียที่คัดมาแล้ว (Ranked shortlist)

**สมดุลของพอร์ต:** painkiller:desire = [x:y] · durable:emerging = [x:y] — ถ่วงแบบนี้เพราะ [เหตุผลตาม brief/edge].

| # | ไอเดีย (1 ประโยค) | ชนิด (P/V/C) | ตลาด/ฝูงชน | Evidence signal + source | คะแนนรวม | สมมติฐานเสี่ยงสุด |
|---|---|---|---|---|---|---|
| 1 | ... | P/V/C | ... | [signal](url) | X/30 | ... |
...

### เหตุผลของอันดับ 1–3 (ต้องมี sub-scores ครบ 6 มิติ)
- **#1 [name]** — Pull x/5, Market x/5, Secret x/5, Job x/5, Survivability x/5, Feasibility x/5.
  ทำไมนำ; source หลัก; สมมติฐานเสี่ยงสุด; วิธีเทสต์ที่ถูกที่สุด.
- ...

### ตัวที่ตัดทิ้งและเหตุผล
- [idea] — killed because [reason] (e.g. "Candy — demand was a platform-specific spike, not Lindy-durable").
```

Then offer the hand-off explicitly: *"อยากให้ส่งอันดับ 1 (หรือตัวที่คุณเลือก) ต่อให้ `ideakit-validate`
ทำ deep validation แล้วออกมาเป็น PRD ไหม? หรืออยากเอาเข้า `ideakit-explore` เพื่อขยาย/ท้าทายก่อน?"*

The human chooses what advances. This skill recommends but never decides go/kill.

## Operating principles

All of these are the governing principle (Requisite Variety + Reflexivity) applied — not a flat list
of rules to memorize. They're grouped so you can see which half each serves.

**Requisite Variety** — hold enough variety to match a varied world:
- **Diversity is a feature, not noise.** A spread of structurally different ideas beats five polished
  variations of one theme.
- **Vary every stage, not just one.** Variety of inputs (sources), of lenses (generation), and of
  criteria (scoring) — a single rich stage can't compensate for a narrow one.
- **Desire ranks with pain; durability is a separate axis.** Score the intensity of the *want*, not
  only the depth of the *problem*; then ask separately whether that demand is durable or a fad.

**Reflexivity** — never mistake your frame for the territory:
- **Audit your own blind spots, generically.** Every run, ask what your sources *and* rubric can't
  see and scan against that bias (`coverage-audit.md`) — catch unknown unknowns, don't re-list known
  ones.
- **Don't silently filter by profile.** The user's background is a *preference to surface against*,
  not a pre-filter. Put options on the table and let the user cut them.
- **Honest, provisional scoring.** Don't inflate feasibility/survivability; treat totals as a sort
  key, not a verdict. The human makes the go/kill call.

**Operating constraints** (unchanged):
- **Constraints in, ideas out.** If the user already has a specific idea, hand off to
  `ideakit-validate` and stop.
- **Evidence beats cleverness.** Every idea traces to a real signal from Step 2; cite it.
- **Hand off, don't hoard.** Output is a shortlist + recommendation to advance, not a finished plan.

## Execution

**Don't stop at advice — produce the deliverable.** Actually *run* the searches (don't describe the
scan), then build the ranked shortlist with cited evidence as a real file/table. Do the research for
real under the grounding rule (cite or mark as assumption; never invent market data). Full contract:
`../ideakit-execution.md`.

## Reference files

Each is the governing principle applied to one stage:

- `references/trend-sources.md` — *input variety*: where to scan + copy-ready query patterns.
- `references/money-first.md` — *optional "where the money is" framing*: re-points Scan/Score toward
  cited money evidence (Starving Crowd, Profit Pools, Value Migration), with the hard no-fabrication
  rule and the solo correction (reachable fast-paying buyers, not biggest TAM). Read when the user
  asks for the most lucrative ideas / to follow the money.
- `references/coverage-audit.md` — *reflexivity on inputs*: scan against your own source/rubric bias
  to catch unknown unknowns (run inside Step 2, every run).
- `references/diversity.md` — *lens variety*: partition the idea space so ideas don't converge
  (read every run before Step 3); now includes the value-type axis and portfolio synthesis.
- `references/frameworks.md` — the actual generation lenses and scoring foundations (the "latticework").
- `references/scoring.md` — *criteria variety + reflexivity*: the six-dimension rubric (0–5 each) plus
  the fad/Lindy and balance flags.
