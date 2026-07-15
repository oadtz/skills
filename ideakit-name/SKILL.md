---
name: ideakit-name
description: >
  Generate strong product / brand / company names AND screen them for availability — so a name isn't
  just catchy but usable. Use when the user wants to name a product, brand, company, or project;
  asks to "come up with names", "brainstorm names", "help me name this", "find an available name",
  "is [name] taken", or "check the domain / trademark / handles". It pairs mixed name types and
  SMILE/SCRATCH with an availability gauntlet: RDAP/WHOIS domains, WIPO/USPTO/TMview trademarks,
  social handles, and web collision. It usually runs after ideakit-validate and feeds
  ideakit-present / forge-* / solo-*. It is NOT idea generation and does NOT give legal clearance.
  When naming a stored ideakit idea, update that idea memory with the naming artifact, shortlist,
  top pick, and availability watch-outs.
---

# Ideakit — Name (brand/product naming + availability screening)

Read `../ai-engineering-foundation.md` now. Do not introduce AI naming or positioning merely because
AI coders are the product's engineering team.

Produce names that are both **good** (memorable, on-brand, the right kind of name) and **usable** (the
`.com` or key TLD is gettable, no glaring trademark conflict, handles are free, the market isn't already
crowded with the name). A name that fails the availability gauntlet is not a shortlist candidate, no
matter how clever — so this skill *checks*, it doesn't just brainstorm.

## The governing principle (read first)

**A name is only as good as it is *obtainable* — so generate freely, then screen ruthlessly, and never
claim a name can be obtained without actually checking.** Two halves:

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

Use exact screening statuses rather than a green check that hides uncertainty:

- **unregistered at [timestamp]** — no registration record found by the authoritative lookup used;
- **registered** — registration record found; note whether active, parked, or offered aftermarket;
- **premium/reserved** — registry or seller makes it obtainable only under special pricing/terms;
- **no identical mark found** — exact-match screen only, never “trademark clear”;
- **possible similar conflict** — related name/class needs professional review;
- **unknown / check blocked** — the source could not be queried reliably;
- **handle appears unused** — page/search observation only, not proof it can be claimed.

Record source, method, target market/class, and check time. A DNS miss alone never earns
“unregistered,” and a missing public profile never earns “handle available.”

## Workflow

Five steps: **Brief → Generate (mixed types) → Filter (SMILE/SCRATCH) → Availability gauntlet → Shortlist.**

### Step 1 — Naming brief

Pin down what the name must do (pull from `ideakit-validate`'s output if available; ask only what's
missing): the product/what it does, the brand values/personality, the target audience, what the name
should *evoke*, any name-type preference, and the **hard requirements** (which TLD matters — `.com`?
`.ai`? — and which handles are non-negotiable). Note any words/associations to avoid.

### Step 2 — Generate across name types (and escape the AI centroid)

Read `references/naming-and-clearance.md` **and `references/anti-cliche.md`** — the second is what keeps
output from reading as generic AI slop, which is the #1 complaint about machine-generated names.

The trap is two centroids: generic startup compounds and the newer “random simple noun” response to
anti-slop prompting. Avoid both. A distinctive name must express tension or a point of view specific
to this venture, not merely look unlike a SaaS name.

1. **Generate an obvious batch as a negative baseline.** Do not advance a name merely because it is
   familiar, and do not discard a strong contextual name solely because it appeared early. Record why
   each baseline name is generic, collided, or unusually earned.
2. **Flag tells contextually.** Treat slop suffixes, epic abstractions, buzzword mash-ups, god names,
   and Get/Try/i-/[X]AI patterns as strong warnings, not lexical law. A deliberate exception needs a
   venture-specific story and category-distance rationale.
3. **Use real technique to get distinctiveness** — empty-vessel real words used as unexpected metaphors
   (Stripe/Slack/Nest), the random-word trigger, deliberate category-*tension* (a name slightly "wrong"
   for the space), **borrowing a simple word from another language** (Volvo, Audi), and sound symbolism.
4. **Stay legible in the actual target markets.** When the venture is cross-border, bias toward names
   a non-native speaker can **read, say, and spell after hearing once**.
   Distinctiveness should come from the *unexpected use of a simple word*, NOT from a harder/obscure or
   archaic word. Simple-but-surprising beats clever-but-obscure. If a borrowed word is used, plan to run
   the linguistic check in Step 4.
5. **Still mix name types** — Descriptive, Suggestive/Metaphorical, Coined/Neologism, Compound/Hybrid,
   Lexical-tweak. Variety is where the gettable winner hides (descriptive `.com`s are all taken anyway).

Apply two tests to every candidate: *“Would 50 other generators output this?”* and *“Could this random
noun name 50 unrelated ventures?”* Cut either failure unless the naming brief supplies a specific,
defensible reason. Aim for ~15–30 serious candidates after the baseline.

### Step 3 — Filter with SMILE / SCRATCH

Score candidates with Alexandra Watkins' test (detail in the reference):

- **SMILE** (keep/raise): Suggestive, Memorable, Imagery, Legs, Emotional.
- **SCRATCH** (drop): Spelling-challenged, Copycat, Restrictive, Annoying, Tame, Curse-of-knowledge,
  Hard-to-pronounce.

Cut the SCRATCH failures and the dead ones; carry the strongest ~8–12 into the gauntlet (checking all 30
is wasteful). **Treat any leftover centroid/AI-slop name as an automatic SCRATCH** (it fails Tame and
usually Copycat) and treat arbitrary-word cleverness with no venture connection as Tame too.

### Step 4 — The availability gauntlet (the real work — check, don't assume)

For each surviving name, **actually run** the checks and record evidence:

- **Domain** — target TLD(s): is `.com` (and any required TLD) registered? (RDAP/WHOIS/DNS.) Note if
  it's premium/parked.
- **Trademark** — search WIPO + USPTO + TMview for identical *and* similar marks; note the Nice
  class(es) and any conflict in a related class.
- **Social handles** — the required platforms: free or taken?
- **Market/web collision** — does an existing company/product already use this name (especially in an
  adjacent space)?
- **Linguistic / cross-language** — is it pronounceable for non-native speakers, and does it carry no
  odd/offensive meaning in the major target-market languages? (A web search per language usually
  suffices for a solo; see `references/anti-cliche.md`.) Flag anything off; mark unchecked languages
  "not verified."

Produce a table — **name × domain × trademark × handles × collision** — with each cell backed by a
check (or marked unknown). A name failing the **hard** gates (required domain registered and
unobtainable, or a likely similar mark conflict in a related class) is out, regardless of SMILE score.
When any required gate is unknown, carry the candidate only as **provisional**; do not say it cleared
the gauntlet.

### Step 5 — Shortlist + honest verdict

Present the top 3–5 that clear the gauntlet. If no candidate has every required check, present a
**provisional shortlist** ordered by naming quality and unresolved risk instead of manufacturing a
winner:

```
## Name shortlist

| Name | Type | SMILE | .com / [TLD] | Trademark (class) | Handles | Market collision | Checked at / sources |
|---|---|---|---|---|---|---|---|
| ... | coined | strong | unregistered at [time] via RDAP | no identical found (cls 42); similar search pending | appears unused; claimability unknown | none found in scoped search | [time + sources] |
| ... | ... | ... | ... | ... | ... | ... |

**Top pick / provisional lead:** [name] — [why it wins on brand + screening status].
**Watch-outs:** [the ⚠️ items still to verify].
**Before you commit:** screening ≠ legal clearance — have a trademark attorney run a full clearance in
your filing class(es) before filing or investing in the brand. Then register the domain/handles
yourself (this skill prepares; you buy).
```

The user picks the name and performs the real-money/legal actions; this skill names, screens, and stages.

## Operating principles

- **Availability is a hard gate, not a tiebreaker.** A brilliant name you cannot obtain is not a final
  candidate; a name with blocked checks remains provisional. Screen before anyone falls in love.
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
"buy / file" step. If this names a stored idea or the user names an idea location, read
`../ideakit-memory.md` and update the matching idea memory with the naming artifact link, shortlist,
top pick, and unresolved availability/legal watch-outs. Full contract: `../ideakit-execution.md`.
(`references/anti-cliche.md` is the family craft bar — `../ideakit-craft.md` — specialized for names.)

## Reference files

- `references/naming-and-clearance.md` — the name types + the Naming Matrix, the full SMILE/SCRATCH
  rubric, and the availability toolkit (RDAP vs WHOIS vs DNS; WIPO Global Brand Database / USPTO
  Trademark Search / EUIPO TMview; Namechk/KnowEm; web collision) with the screening-not-clearance line.
- `references/anti-cliche.md` — **how to escape the AI naming centroid**: the banned tells (slop
  suffixes, epic abstract words, buzzword mash-ups, god-names, gimmick prefixes), the distinctive-naming
  techniques (empty-vessel, random-word trigger, category-tension, unexpected sources, sound symbolism),
  and the "would 50 other AI tools output this?" smell test. Read every run before generating.
