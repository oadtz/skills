# UX flows & screen inventory — derive from jobs, not features

This is the governing principle applied to scope: **derive screens from jobs, not features**, and plan
the unglamorous 90% from the start. Use in Step 4 of forge-design.

## Map the product before drawing pages

### Information architecture (lean)
IA is the structural backbone — how content and actions are organized so users can find things and
complete the core task. For an MVP, prioritize **clarity over completeness**: the user should
immediately see where to start and how to reach the main outcome. A 2025 MVP has to *feel usable and
human*, not merely function — UX is the product, not decoration.

Sources: https://www.parallelhq.com/blog/mvp-ux-design , https://maze.co/blog/mvp-ux-design/ ,
https://bricxlabs.com/blogs/information-architecture-in-ux

### Core flow first
Map the **one flow that delivers the primary value** end to end (sign-up → first success), and lean the
IA around it. Everything else is secondary until that flow is clean. This is the UI analogue of the
walking skeleton in `forge-build`.

### Screen inventory from Jobs-to-be-Done
Derive each screen from a **user job + its success state**, not from a feature list:

> "When [situation], the user wants to [job], so they can [outcome]." → the screen that delivers that
> outcome, and what 'success' looks like on it.

This gives the build a concrete success criterion per screen and keeps the UI anchored to outcomes the
user is "hiring" the product for.

## Plan the 90% (states, not just the happy path)

The clickable happy path is ~**10%** of the real product; the other 90% — empty, loading, error states
— is what sinks builds when real data arrives. For **every screen and component**, define up front:

- **Empty state** — no data yet: what the user sees and the call to action that fills it.
- **Loading state** — and make it *smart*: don't full-page-spinner on every fetch; keep context visible
  (e.g. an inline indicator on a table during pagination so the UI doesn't flash and disappear).
- **Error state** — failed fetch, validation failure, permission denied: a clear recovery path.
- **Populated state** — proven against **real data**, not a tidy mock (real data breaks layouts that
  looked fine with placeholders).

**Standardize state handling as a pattern**, don't hand-craft per screen — dozens of pages each need
consistent empty/loading/error handling. Test against slow connections too.

Sources: https://blog.logrocket.com/ui-design-best-practices-loading-error-empty-state-react/ ,
https://www.uxpin.com/studio/blog/ux-best-practices-designing-the-overlooked-empty-states/

## MVP vs MLP — decide deliberately

- **MVP (Minimum Viable Product):** the minimum to validate viability; users *tolerate* it while you
  iterate.
- **MLP (Minimum Lovable Product):** the minimum to be *loved* — differentiated, with an emotional hook;
  needs UX involvement from the start.

Because AI collapses the cost of polish, the historical excuse for an ugly MVP is weaker — **MLP is
increasingly the right default**, especially in competitive markets where the first impression decides
retention. Pick one explicitly and say why; it changes how much the build invests per screen.

Sources: https://www.aha.io/blog/minimum-viable-product-vs-minimum-lovable-product ,
https://www.eleken.co/blog-posts/mlp-vs-mvp

## Output of this step

- A lean IA / site map.
- The core flow mapped end to end.
- A screen inventory: each screen with its job, success state, and the four states (empty/loading/
  error/populated) planned.
- An explicit MVP-vs-MLP call.

This is what `forge-build` turns into slices — each screen-with-states maps cleanly to a vertical
slice.
