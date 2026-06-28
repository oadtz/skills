---
name: ideakit-name
description: >
  Generate strong product / brand / company names AND screen them for availability — so a name isn't
  just catchy but actually usable (the domain is gettable, no obvious trademark conflict, the social
  handles are free, and nobody in the market already owns it). Use this skill whenever the user wants
  to "name a product / brand / company", "come up with names for", "brainstorm names", "help me name
  this", "find an available name", "is [name] taken", "check if [name] is available", "check the
  domain / trademark / handles for [name]", or needs naming for something they're building. It pairs
  mixed name types + SMILE/SCRATCH with a real availability gauntlet: RDAP/WHOIS domains, WIPO/USPTO/
  TMview trademarks, social handles, and web collision. It usually runs after `ideakit-validate` and
  feeds `ideakit-present` / `forge-*` / `solo-*`. It is NOT idea generation (use `ideakit-generate`)
  and does NOT give legal clearance — it screens and flags; a trademark attorney clears.
---

# Ideakit — Name (brand/product naming + availability screening)

Produce names that are both **good** (memorable, on-brand, the right kind of name) and **usable** (the
`.com` or key TLD is gettable, no glaring trademark conflict, handles are free, the market isn't already
crowded with the name). A name that fails the availability gauntlet is not a shortlist candidate, no
matter how clever — so this skill *checks*, it doesn't just brainstorm.

## The governing principle (read first)

**A name is only as good as it is *available* — so generate freely, then screen ruthlessly, and never
claim a name is free without actually checking.** Two halves:

1. **Good *and* gettable, in that order of effort but not of importance.** Brainstorm widely across
   name types first (cleverness is cheap), but treat **availability as a hard gate**, not a footnote.
   The most common naming failure isn't an uninspired name — it's falling in love with a name whose
   `.com` is parked at $40k, that collides with a registered trademark, or that a competitor already
   uses. Screen before anyone gets attached.
2. **Check, don't assume (anti-hallucination, hard rule).** **Never state that a domain is available, a
   handle is free, or a name is trademark-clear without a real check performed *this run*.** Guessing
   availability is the exact place this skill would hallucinate and waste the founder's money/time. If
   a check couldn't be run, label it **"not yet verified"** — never present an unchecked name as clear.
   And availability screening is **not legal clearance** (see the boundary below).

Everything below is these two applied.

## Where this sits in the pipeline

```
ideakit-discover → generate → explore → validate → [ideakit-name] → present  →  forge-* / solo-*
                                                     name + screen     pitch       build / brand it
```

Naming is a **utility stage**: it usually runs once there's a validated product to name, and its output
(a cleared name + the secured-able domain/handles) flows into the pitch (`ideakit-present`), the build
(`forge-*`), and the brand/GTM (`solo-distribute`/`solo-model`). It can also run standalone any time
someone just needs a name checked.

## Host capability mapping

- **User input**: ask one concise question at a time to build the naming brief; use structured choices
  if supported.
- **Research / checks (this skill is check-heavy — use real tools):**
  - **Connector/plugin registry** — first, check whether a domain-registrar, trademark, or naming MCP
    is connected; if so, prefer it.
  - **Domain availability** — RDAP (modern, JSON; public via the IANA RDAP bootstrap) and/or WHOIS, with
    a DNS lookup as a fast first check; or a domain-availability API if available. Verify the current
    endpoint at runtime — don't hardcode.
  - **Trademark** — search the free databases: **WIPO Global Brand Database**, **EUIPO TMview**, and the
    **USPTO Trademark Search** (the old TESS was retired). No single source covers every office.
  - **Social handles** — check key platforms for the target audience (and tools like Namechk/KnowEm via
    the browser if no API).
  - **Market/web collision** — web search for existing companies/products using the name.
- **No live checks available**: generate and evaluate names, but mark **every** availability field
  "not yet verified" and tell the user exactly what to check where — never fabricate a result.
- **File output**: write the shortlist + availability table to a file/artifact when supported.

## Workflow

Five steps: **Brief → Generate (mixed types) → Filter (SMILE/SCRATCH) → Availability gauntlet → Shortlist.**

### Step 1 — Naming brief

Pin down what the name must do (pull from `ideakit-validate`'s output if available; ask only what's
missing): the product/what it does, the brand values/personality, the target audience, what the name
should *evoke*, any name-type preference, and the **hard requirements** (which TLD matters — `.com`?
`.ai`? — and which handles are non-negotiable). Note any words/associations to avoid.

### Step 2 — Generate across name types

Read `references/naming-and-clearance.md`. Generate a wide set (aim ~15–30) deliberately **mixing name
types** — Descriptive, Suggestive/Metaphorical, Coined/Neologism, Compound/Hybrid, Lexical-tweak,
(occasionally) Acronym/Place/Person. Don't cluster on one type; variety is where the gettable winner
usually hides (the descriptive `.com`s are all taken, so coined/compound names clear more often).

### Step 3 — Filter with SMILE / SCRATCH

Score candidates with Alexandra Watkins' test (detail in the reference):

- **SMILE** (keep/raise): Suggestive, Memorable, Imagery, Legs, Emotional.
- **SCRATCH** (drop): Spelling-challenged, Copycat, Restrictive, Annoying, Tame, Curse-of-knowledge,
  Hard-to-pronounce.

Cut the SCRATCH failures and the dead ones; carry the strongest ~8–12 into the gauntlet (checking all 30
is wasteful).

### Step 4 — The availability gauntlet (the real work — check, don't assume)

For each surviving name, **actually run** the checks and record evidence:

- **Domain** — target TLD(s): is `.com` (and any required TLD) registered? (RDAP/WHOIS/DNS.) Note if
  it's premium/parked.
- **Trademark** — search WIPO + USPTO + TMview for identical *and* similar marks; note the Nice
  class(es) and any conflict in a related class.
- **Social handles** — the required platforms: free or taken?
- **Market/web collision** — does an existing company/product already use this name (especially in an
  adjacent space)?

Produce a table — **name × domain × trademark × handles × collision** — with each cell backed by a
check (or marked "not yet verified"). A name failing the **hard** gates (required domain taken, clear TM
conflict in the same class) is out, regardless of SMILE score.

### Step 5 — Shortlist + honest verdict

Present the top 3–5 that clear the gauntlet:

```
## Name shortlist

| Name | Type | SMILE | .com / [TLD] | Trademark (class) | Handles | Market collision |
|---|---|---|---|---|---|---|
| ... | coined | strong | ✅ available | no identical (cls 42) ⚠️ verify similar | @x free | none found |
| ... | ... | ... | ... | ... | ... | ... |

**Top pick:** [name] — [why it wins on brand + availability].
**Watch-outs:** [the ⚠️ items still to verify].
**Before you commit:** screening ≠ legal clearance — have a trademark attorney run a full clearance in
your filing class(es) before filing or investing in the brand. Then register the domain/handles
yourself (this skill prepares; you buy).
```

The user picks the name and performs the real-money/legal actions; this skill names, screens, and stages.

## Operating principles

All of these are the governing principle applied.

- **Availability is a hard gate, not a tiebreaker.** A brilliant name you can't own is not a candidate.
  Screen before anyone falls in love.
- **Check, never assume.** No "this is probably available" — run the check or write "not yet verified."
  This is the one place the skill must not hallucinate.
- **Mix name types to win the gauntlet.** Coined/compound names clear domains and trademarks far more
  often than descriptive ones — generate for *clearable*, not just clever.
- **Screening ≠ legal clearance.** Always flag that similar (not just identical) marks can conflict, and
  route a real clearance to a trademark attorney before filing or heavy brand spend.
- **Prepare, don't purchase.** Stage the domain/handle registration and the TM-clearance step; the
  founder spends the money and makes the legal call (see the boundary).

## Execution

**Don't stop at a name list — run the checks for real.** Actually query domain availability
(RDAP/WHOIS/DNS), search the trademark databases, check the handles, and run the web-collision search,
then write the shortlist + evidence table to a file. **Hard boundary:** *registering a domain, buying a
handle, or filing a trademark* spends money / is a legal act — stage it and hand the founder the final
"buy / file" step. Full contract: `../ideakit-execution.md`.

## Reference files

- `references/naming-and-clearance.md` — the name types + the Naming Matrix, the full SMILE/SCRATCH
  rubric, and the availability toolkit (RDAP vs WHOIS vs DNS; WIPO Global Brand Database / USPTO
  Trademark Search / EUIPO TMview; Namechk/KnowEm; web collision) with the screening-not-clearance line.
