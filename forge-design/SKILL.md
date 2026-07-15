---
name: forge-design
description: >
  Turn a PRD plus a technical foundation into a real product design — a design-token system, the core
  user flows, and an accessible component foundation — instead of generic, AI-generated "slop." Use
  this skill whenever the user is building a product UI and asks things like "design the UI/UX", "set
  up a design system", "make this not look AI-generated", "why does my app look generic", "establish
  design tokens", "map the user flows", "make it look distinctive / on-brand", "add accessibility", or
  hands off from forge-architect. It is the SECOND stage of the forge build pipeline. It builds the
  design SYSTEM and flows that forge-build then implements screen by screen. It is NOT for idea
  generation or validation (use the ideakit skills), NOT for backend architecture (use
  forge-architect), and NOT for writing the full application code (use forge-build).
---

# Forge — Design (foundation → design system + flows)

Read `../ai-engineering-foundation.md` now. Design a system that an AI engineering team can implement
consistently without implying that the shipped product needs runtime or customer-facing AI.

Take the PRD and the technical foundation and produce the **design system and user flows the build
will inherit** — so every screen is consistent, accessible, and distinctive instead of the median of
every Tailwind tutorial. Output is a token system, a flow map, and an accessible component foundation
— not a pile of finished screens (those come in `forge-build`).

## The governing principle (read first)

**Constrain before you generate; define the system before the screens.**

Generic "AI slop" UI — the centered hero card, the purple-on-white gradient, the three-icon grid,
Inter everywhere — is **a constraint problem, not a capability problem.** LLMs interpolate the median
of their training data; with no constraints they return that median. The fix is not a better model,
it's a tighter brief and a system defined up front:

1. **Constrain before you generate.** Every UI generation carries an explicit *anti-slop brief* —
   negative constraints (what to avoid), 3–5 described references (what good looks like, and *why*),
   and persona priming. This is the highest-leverage, nearly-free lever in the whole family.
2. **Define the system before the screens.** Establish design tokens (color, type, spacing) and an
   accessible component foundation *first*; derive screens from those. A system defined once stops the
   agent re-inventing inconsistent values on every screen.
3. **Derive screens from jobs, not features.** Each screen comes from a user job and its success
   state — and must handle the unglamorous 90% (empty, loading, error states) from the start, not just
   the happy-path mock.

**Look-and-feel is a first-class quality bar, equal to functionality — and it's *enforced*, not just
briefed.** The visual craft and the *feel* (interaction polish, motion, the UX heuristics) matter as
much as the product working, and "looks/feels like generic AI slop" is a **defect, not a taste
preference.** The brief you set here is verified downstream as a blocking gate — `forge-build` checks
design fidelity + anti-slop per slice, and `forge-ship` runs a Design/UX quality gate before release,
equal to the test/security gates (see `references/visual-craft.md`).

## Where this sits in the pipeline

```
forge-architect  →  forge-design (THIS)  →  forge-build  →  forge-ship
decide the system   design the experience   build it       harden + ship
```

- If there's **no PRD or foundation yet**, get one first (ideakit / forge-architect).
- If the user only needs a backend/CLI with no meaningful UI, this stage is light — produce the flow
  map and skip the visual system. Say so rather than over-producing.
- This stage ends when the token system, flows, and component foundation exist and the user approves.

## Compose, don't re-derive

UI/design capabilities may be available in the host. If present, use them as the engine and let
forge-design orchestrate them for the *product* context:

- **Visual-direction capability** (for example `frontend-design`) — distinctive, anti-slop UI craft.
- **Design-system capability** (for example `tailwind-design-system`) — design tokens, component
  libraries, responsive patterns.
- **Accessibility/UX review capability** (for example `web-design-guidelines`) — review UI for
  accessibility / Web Interface Guidelines compliance.

forge-design's job is to set the *constraints and system* for the specific product, then drive any
available capability — not to duplicate its content or require one host's exact skill names.

## Host capability mapping

- **User input**: ask concise questions; use structured choice UI if available.
- **Research / references**: use the host's web/browser to gather and *describe* visual references
  (layout, type pairing, color relationships) — references are described in words the model can act on,
  not just linked.
- **Artifact creation**: write the token definitions, flow map, and component foundation through the
  host's file/artifact mechanism; produce a clickable preview if the host supports it.
- **No live research**: proceed from the PRD and an explicit brand brief from the user; mark visual
  reference choices as proposals to confirm.

## Workflow

Five steps: **Brand & brief → Tokens → Component foundation → Flows & screens → Accessibility pass.**
Tokens before screens — don't jump to generating pages.

### Step 1 — Brand & anti-slop brief

Read `references/anti-slop-brief.md`. Pin down the visual intent and write the reusable brief:

- **Audience & feeling**: who uses this and what should it feel like (trustworthy, playful, premium,
  utilitarian)? This shifts every later choice.
- **References**: gather 3–5 references and describe *why each works* — layout, type, color
  relationships, spacing, density. Described references transfer concrete taste; "make it beautiful"
  does not.
- **Negative constraints**: name what to avoid explicitly (no Inter/Roboto default, no purple gradient
  on white, no centered hero card, no three-icon-box grid). Negation actively lowers the probability
  weight of the default patterns — this is why anti-slop briefs work.
- **MVP vs MLP**: decide deliberately. AI collapses the cost of polish, so a Minimum *Lovable* Product
  is increasingly the right default over a barely-tolerable MVP — but say which you're targeting and
  why.

### Step 2 — Design tokens (the system, before any screen)

Read `references/design-tokens.md`. Establish a three-tier token system **before generating screens**,
in this order: **color → type → spacing**, then the rest:

- **Primitive tokens** (raw values: `blue-500`, `space-4`).
- **Semantic / alias tokens** (`action-color`, `text-secondary`, `surface`) — named for *role*, so
  they survive a rebrand. Semantics point only to primitives.
- **Component tokens** (button bg, card radius, input padding) — point to semantics.

Tokens are the **shared contract between design and code**: change the token, every consumer updates;
the agent inherits one source of truth instead of inventing values per screen. Use a standard format
(the W3C Design Tokens format is now stable) so the pipeline (e.g. Style Dictionary → Tailwind config /
CSS variables) needs no custom glue.

### Step 3 — Component foundation

Establish the primitive component layer before composing screens. Default stack: **shadcn/ui + Radix
(or Base UI) + Tailwind** — you *own* the source (copy-paste, not a black-box dependency), the
primitives are accessible by default (ARIA, focus management, keyboard nav handled), and the markup is
predictable for an LLM to extend. Wire the components to the semantic tokens from Step 2 so styling is
centralized.

### Step 4 — Flows & screen inventory (jobs, not features)

Read `references/ux-flows.md`. Map the product before drawing pages:

- **Information architecture**: a lean structure — where the user starts and how they reach the core
  outcome without confusion. Clarity over completeness for an MVP.
- **Core user flow first**: map the one flow that delivers the product's primary value end to end;
  lean the IA around it.
- **Screen inventory from JTBD**: derive each screen from a user job + its success state, giving the
  build a clear success criterion per screen.
- **Plan the 90%**: for every screen/component, require empty / loading / error / populated states
  defined up front. The clickable happy path is ~10% of the real product; the omitted states are what
  sink builds when real data arrives. Standardize state handling as a pattern, don't hand-craft per
  screen.

### Step 5 — Accessibility pass (a constraint, not a retrofit)

Read `references/accessibility.md`. Bake WCAG 2.2 AA in as a generation constraint — it's cheap up
front and expensive to remediate later: 24×24px minimum target sizes, visible focus indicators,
sufficient contrast, full keyboard operability, semantic landmarks/labels. The Radix/shadcn foundation
gives most of this for free; the brief must still demand it because AI tools default to tiny icon
buttons and miss contrast unless told. Run the available accessibility/UX review capability as the
check (for example `web-design-guidelines` if installed).

Then present the design system and offer the handoff:

> The design system is set: tokens, an accessible component foundation, the core flows, and a screen
> inventory with all states planned. Want me to hand this to **forge-build** to implement it
> screen by screen?

## Operating principles

**Constrain before you generate:**
- **Negative constraints + described references beat adjectives.** "Make it beautiful" returns the
  median; "no purple gradient, like Linear's density, Stripe's type scale" returns intent.
- **Ask for 3 directions, not 1.** Exploring the solution space beats converging on the first (often
  generic) local maximum.

**Define the system before the screens:**
- **Tokens are the source of truth.** Never let a screen hardcode a value a token should own.
- **Own your component source** so you can diverge from the default look without fighting an API.

**Derive screens from jobs:**
- **Every screen has a job and a success state.** A screen with no named job is decoration.
- **Plan the 90%.** Empty/loading/error states are part of the design, not a build afterthought.

**Honesty:** AI provides speed and execution; the human provides taste and the constraints. Don't
ship a generic screen and call it done — name where it still looks AI-generated and fix the brief.

## Execution

**Don't stop at a spec — build it.** Produce the real design tokens, component specs, and flow
definitions (machine-readable where the pipeline expects it) with the right tool, not a written
description of a design system. Build the actual assets the brief calls for. Full contract:
`../forge-execution.md`.

## Reference files

- `references/anti-slop-brief.md` — *constrain before you generate*: the reusable brief (negative
  constraints + described references + persona priming) and why negation works.
- `references/visual-craft.md` — *the look-and-feel quality bar*: the craft principles (Refactoring UI
  hierarchy/spacing/scales, Nielsen heuristics, motion/micro-interactions, responsive), the current
  **AI-slop tells to auto-flag**, the "commit to one point of view" fix, and **the gate checklist** that
  forge-build and forge-ship enforce. Read every run.
- `references/design-tokens.md` — *define the system first*: the three-tier token system, ordering,
  and tokens as the design↔code contract.
- `references/ux-flows.md` — *derive from jobs*: IA, core-flow-first, JTBD screen inventory, and
  planning empty/loading/error states.
- `references/accessibility.md` — *constraint not retrofit*: the WCAG 2.2 AA baseline to bake in.
