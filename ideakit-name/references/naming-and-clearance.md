# Naming & clearance — the method and the toolkit

The "how" behind `ideakit-name`. Two parts: (A) how to generate and evaluate names, and (B) how to
*actually check* availability. Part B is the part that must never be faked — **check, don't assume.**

## A. Generating names

### Name types (mix them — don't cluster)

The two-axis **Naming Matrix**: *Descriptive ↔ Abstract* and *Real ↔ Coined*. Practical types:

- **Descriptive** — says what it does ("PayPal", "General Motors"). Clear, but the good `.com`s are
  almost all taken and it's hard to trademark broadly.
- **Suggestive / Metaphorical** — evokes a quality or feeling ("Amazon", "Nike", "Stripe"). Strong
  brand legs; a sweet spot.
- **Coined / Neologism** — invented word ("Kodak", "Google", "Xerox"). Clears domains/trademarks most
  easily; needs more marketing to attach meaning.
- **Compound / Hybrid** — two words fused ("Facebook", "Netflix", "Salesforce"). Clears often; reads well.
- **Lexical tweak** — a real word respelled ("Lyft", "Flickr", "Tumblr"). Distinctive + ownable, but
  watch the "spelling-challenged" SCRATCH flag.
- **Acronym / Place / Person / Numeric** — situational; usually weaker for a new solo brand.

**Rule of thumb:** the gettable winner is usually coined, compound, or a lexical tweak — because
descriptive/real-word `.com`s and marks are mostly gone. Generate ~15–30 across types.

## B. Evaluating — SMILE & SCRATCH (Alexandra Watkins)

A 12-point filter: **SMILE** = the qualities of a sticky name; **SCRATCH** = deal-breakers.

**SMILE — a strong name has:**
- **S**uggestive — evokes something about the brand
- **M**emorable — makes a familiar/sticky association
- **I**magery — paints a picture that aids memory
- **L**egs — extends into a theme/story for the long run
- **E**motional — moves people

**SCRATCH — scratch it off if:**
- **S**pelling-challenged — looks like a typo / has to be spelled out loud
- **C**opycat — resembles competitors' names
- **R**estrictive — boxes you in (geography, a single product) and limits growth
- **A**nnoying — feels forced or gimmicky
- **T**ame — flat, descriptive, forgettable
- **C**urse of knowledge — only makes sense to insiders
- **H**ard to pronounce — confuses people

Cut every SCRATCH failure; rank survivors by SMILE before spending checks on them.

## C. The availability gauntlet (check for real)

### 1. Domain

- **DNS lookup** — fastest first signal (does it resolve?), but *not* authoritative for "registered"
  (a registered domain may have no DNS records).
- **RDAP** — the modern replacement for WHOIS: structured JSON, public, mapped per-TLD via the **IANA
  RDAP bootstrap** registry. Preferred for programmatic checks.
- **WHOIS** — older free-text protocol, more heavily rate-limited; use as fallback/confirmation.
- **APIs** (if a key is available): WhoisJSON, WhoisFreaks, WhoisXML — bulk + multi-TLD.
- Best practice: **DNS fast-check → RDAP/WHOIS confirm.** Flag premium/parked/aftermarket domains (an
  "available" name can still cost five figures).
- Report **unregistered at [timestamp] via [source]**, not “available.” Registration status can change
  immediately, and registry-reserved or premium terms may still apply.

### 2. Trademark (search several — no single source is complete)

- **WIPO Global Brand Database** — 70M+ records across ~73 national/regional offices, free; includes
  Madrid-filed marks; has APIs via the WIPO IP API catalog.
- **EUIPO TMview** — 75M+ marks across EU + partner offices, free.
- **USPTO Trademark Search** — the U.S. source of truth (the old **TESS** tool was retired; it's now a
  cloud search system).
- Search for **identical *and* similar** marks, and note the **Nice class(es)** — a conflict only counts
  if it's in a related class for related goods/services, but *similar* marks in the same class can block
  you, so flag them.

### 3. Social handles

- Check the platforms that matter for the audience. Tools: **Namechk** (36 domains + 100+ platforms),
  **KnowEm** (500+ networks; also checks the USPTO trademark DB) — via the browser if no clean API.
- Public-page absence is weak evidence because platforms rate-limit, reserve names, and hide accounts.
  Use “appears unused; claimability unknown” unless an authoritative claim flow confirms otherwise.

### 4. Market / web collision

- Web-search the name + the category: is there already a company/product using it, especially in an
  adjacent space? Even with no registered trademark, an established user creates confusion and risk.

## D. The hard line: screening ≠ legal clearance

Automated checks are **screening**, not a legal opinion. Trademark law turns on *likelihood of
confusion* (similar marks, related goods, the specific class) — not just exact-match. A clean automated
pass can still hide a real conflict. So:

- Present results as "passed screening," never "legally safe to use."
- If any required lookup is blocked or incomplete, label the entire shortlist **provisional** and list
  the unresolved gate, source attempted, and timestamp.
- Always recommend a **full clearance by a trademark attorney** in the intended filing class(es) before
  filing the mark or spending heavily on the brand.
- And per the execution boundary: **registering the domain/handles and filing the trademark are the
  founder's actions** (money + legal) — the skill stages them; the founder executes.
