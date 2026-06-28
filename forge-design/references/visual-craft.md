# Visual craft & anti-slop — making it look *and feel* designed, not AI-generated

Look-and-feel is not decoration laid on top of a working product — for most products it **is** half the
product, and it must be treated as a first-class quality bar equal to functionality. This file is the
positive craft (what *good* looks/feels like) plus the **anti-slop checklist** that the build and ship
gates verify. Great UI is systems, not talent (Refactoring UI) — so these are checkable, not vibes.

## A. The look-and-feel craft principles (Refactoring UI + heuristics)

Grounded in *Refactoring UI* (Adam Wathan & Steve Schoger) and Jakob Nielsen's usability heuristics —
established, not invented.

**Visual craft (the "look"):**
- **Hierarchy first.** Guide the eye with size, weight, color, and placement; one clear primary action
  per screen. If everything is emphasized, nothing is. ([Refactoring UI](https://refactoringui.com/))
- **Design in grayscale first.** Establish spacing, contrast, and size before color — it forces real
  hierarchy instead of leaning on color to fake it.
- **Give it room to breathe.** Generous, consistent spacing is the fastest way to look professional;
  crowding is the fastest way to look amateur. Use a constrained spacing scale, not arbitrary px.
- **Constrained scales = consistency.** Pick limited scales for spacing, type, color, and shadow
  (the tokens from `design-tokens.md`) and never deviate ad hoc. Consistency *is* the polish.
- **Depth with intent.** Use a deliberate elevation/shadow scale for layering — not a glow on everything.
- **Typography does heavy lifting.** A real type scale, good line-height/measure, and one distinctive
  typeface beat default fonts at default sizes.

**The "feel" (interaction & UX quality — Nielsen's 10 heuristics):**
- Visibility of **system status** (loading, saving, success — never a dead pause).
- **Match the real world** (user's language, not system jargon).
- **User control & freedom** (undo, back, cancel, escape hatches).
- **Consistency & standards** (same thing looks/behaves the same everywhere).
- **Error prevention** + clear, recoverable **error messages**.
- **Recognition over recall** (show options; don't make users remember).
- **Flexibility & efficiency** (shortcuts for power users, simple for new ones).
- **Aesthetic & minimalist** (every element earns its place).
- **Help users recover from errors**, and **help/docs** where needed.
  ([NN/g heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/))

**Motion & micro-interactions (the polish that makes it feel alive):**
- Subtle, fast, purposeful (≈150–250ms); animate to communicate (state change, spatial continuity),
  never to decorate. Respect `prefers-reduced-motion`. Hover/focus/active/disabled states on every
  interactive element. Optimistic UI + skeletons over spinners where it fits.

**Responsive craft:** design the small screen too (not a desktop mock squeezed); use at least 24px touch
targets and prefer 44px for primary touch controls; test real breakpoints; content reflows sensibly, no
horizontal scroll, no overlap.

## B. Common AI-slop tells — auto-flag these

AI tools interpolate the median, so they often converge on the same recognizable look. These patterns
are not banned in every context, but when they appear by default they read as AI slop — **flag and fix**
(sources: [Developers Digest](https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it),
[925 Studios](https://www.925studios.co/blog/ai-slop-web-design-guide)):

**Color / surface:**
- Blue→purple / violet gradients; cyan-on-dark; dark background with colored box-shadow *glows*; the
  reflexive cream/beige "tasteful" page background.
- **Gradient text** on headings or metrics (also hurts readability).

**Type:**
- **Inter** (or Roboto) as the default everywhere. Pick a distinctive typeface (e.g. Geist, Söhne,
  Untitled Sans, a real serif) on purpose.

**Layout / components:**
- Uniform 16px border-radius on everything; the **stock shadcn/ui default look** and **glassmorphism**
  (the two dominant AI "CSS fingerprints"); the centered hero card; the three-/four-icon feature grid;
  oversized hero with a vague headline ("Build the future", "Supercharge your workflow").

**Copy (look-and-feel includes words):**
- Generic SaaS filler: *streamline, empower, supercharge, world-class, enterprise-grade, seamless,
  unlock, elevate*. More than the occasional em-dash is an AI cadence tell. Emoji-bullet lists.

## C. The fix: commit to one strong point of view

The cheapest, highest-impact way out of slop, especially solo/resource-constrained: **make 2–3
deliberate, non-default choices and commit to them throughout** — a non-lavender palette (earth tones,
high-contrast black-and-bright, an unexpected accent), a non-Inter typeface, and **one** strong layout
primitive repeated everywhere (not five card styles). *An opinionated page with a clear point of view
beats a generic, "tasteful" page with none.* The brief (`anti-slop-brief.md`) sets the POV; this file
checks the build kept it.

## D. The gate checklist (used by forge-build per slice and forge-ship before release)

Design quality is **blocking**, equal to tests. For the built UI, verify (with real screenshots across
breakpoints, driving the actual app):

- [ ] **System fidelity** — uses the tokens/components; no hardcoded one-off values; consistent.
- [ ] **Hierarchy & spacing** — clear primary action; breathing room; constrained scales held.
- [ ] **All states built** — empty / loading / error / populated (not just the happy path).
- [ ] **Feel** — status feedback, recoverable errors, hover/focus/active states, sensible motion.
- [ ] **Responsive** — works at real breakpoints; targets big enough; no overflow/overlap.
- [ ] **Accessibility** — WCAG 2.2 AA (see `accessibility.md`): contrast, focus, keyboard, labels.
- [ ] **No AI slop** — none of the §B tells; the §C point of view is present and consistent.

If any box fails, it's not done — fix it before the slice/ship is accepted, exactly as a failing test
would block. "Looks/feels like generic AI output" is a defect, not a matter of taste.
