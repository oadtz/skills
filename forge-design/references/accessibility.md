# Accessibility baseline — a generation constraint, not a retrofit

This is the governing principle applied to inclusivity: bake accessibility in as a **constraint at
generation time**, because it's cheap up front and expensive as a remediation pass. Use in Step 5 of
forge-design, and keep it in the brief for every UI generation in the build.

## Why up front

AI tools default to small icon buttons, low-contrast text, and missing focus states unless told
otherwise. Fixing accessibility after dozens of screens exist is a slow audit-and-rework pass; stating
it as a constraint in the brief costs nothing. The Radix/shadcn component foundation (see the main
SKILL) already provides ARIA, focus management, and keyboard nav for free — so most of the work is
*not undoing that* and covering the visual/layout rules.

## The WCAG 2.2 AA baseline to require

State these in the brief and check them in review:

- **Target size (2.5.8, new in 2.2):** interactive targets ≥ **24×24 CSS px**, or sufficient spacing
  (24px-diameter circles centered on each target must not intersect). Padding counts toward the size
  even if the icon glyph is smaller. (Zoom doesn't change CSS pixels, so this is a real layout
  constraint.)
- **Visible focus indicator** on every interactive element — never `outline: none` without a
  replacement. (WCAG 2.2 also adds Focus Not Obscured, 2.4.11.)
- **Contrast:** normal text ≥ 4.5:1, large text ≥ 3:1, UI components/graphics ≥ 3:1.
- **Keyboard operable:** every action reachable and operable by keyboard, in a logical order; no
  keyboard traps.
- **Semantic structure:** real landmarks (`header`/`nav`/`main`), labelled form controls, alt text on
  meaningful images, correct heading order.

Sources: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html ,
https://www.w3.org/TR/WCAG22/

## How to enforce it

- **In the brief:** "WCAG 2.2 AA; 24px minimum targets; visible focus; AA contrast; accessible
  primitives only." Add it to the reusable anti-slop brief so it rides along every generation.
- **In review:** run the **`web-design-guidelines`** skill (if installed in your environment) as the
  accessibility/UX gate (it reviews UI code against Web Interface Guidelines). Treat its findings as
  blocking for HITL slices, the same way `forge-ship` treats security findings.
- **Lean on the foundation:** prefer Radix/shadcn primitives over hand-rolled controls precisely
  because they ship the hard parts (focus, ARIA, keyboard) correctly.

## Anti-pattern to flag

Treating accessibility as a launch-blocking audit at the end. By then it's a remediation project. It's
a generation constraint — set it once, in the system, and it's mostly free.
