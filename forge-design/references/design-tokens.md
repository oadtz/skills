# Design tokens — define the system before the screens

This is the governing principle applied to consistency: **define the system before the screens.**
Tokens established up front stop the agent re-inventing inconsistent values on every screen, and become
the shared contract between design and code. Use in Step 2 of forge-design.

## The three-tier token system

Establish tokens **before generating any screen**, in this order of priority: **color → typography →
spacing**, then radius, shadow, motion.

1. **Primitive tokens** — raw values. `blue-500: #3B82F6`, `space-4: 16px`, `font-size-lg: 18px`.
   The full palette and scale, named by what they *are*.
2. **Semantic / alias tokens** — named by **role**, pointing only to primitives. `action-color →
   blue-500`, `text-secondary → gray-600`, `surface → gray-50`, `danger → red-500`. Role-naming is
   what lets a rebrand happen by repointing semantics, without touching screens.
3. **Component tokens** — named by component part, pointing to semantics. `button-bg → action-color`,
   `card-radius → radius-md`, `input-padding → space-3`.

Screens and components consume **semantic and component tokens only** — never raw primitives, never
hardcoded values. Change a token, every consumer updates.

Sources: https://www.contentful.com/blog/design-token-system/ ,
https://www.figma.com/resource-library/design-tokens/ (recommends color/type/spacing first)

## Tokens as the design↔code contract

Tokens are the single mechanism that keeps a rapidly-iterating AI build consistent across dozens of
screens. When design and code share token *names*, handoff is unambiguous — a dev (or agent) seeing
`spacing.lg` knows the exact value with no measuring, and one change propagates everywhere.

- Use the **W3C Design Tokens Format** (reached its first stable version, 2025.10) — a vendor-neutral
  JSON format with reference tooling (Style Dictionary, Tokens Studio, Terrazzo). Standardizing on it
  means no custom glue.
- **Pipeline pattern:** tokens in Git as source of truth → (optional Tokens Studio two-way sync with
  design) → Style Dictionary in CI transforms them → Tailwind config / CSS variables / platform
  outputs. The agent reads one config; the design tool reads the same source.

Sources:
https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/ ,
https://www.designtokens.org/tr/2025.10/format/

## Practical defaults for an AI-built web product

- Wire tokens into the Tailwind config / CSS variables so `forge-build` inherits them automatically and
  every generated component references them.
- Pair with an available design-system/Tailwind capability (for example `tailwind-design-system`, if
  installed) for token/component scaffolding rather than building the pipeline from scratch.
- Keep the primitive palette small and the semantic layer expressive — most screens should touch only
  a handful of semantic tokens.

## Anti-patterns to flag

- **Generating screens before tokens exist.** Guarantees per-screen drift and is the system-level cause
  of "AI slop." (MindStudio frames "define the system first" as the antidote.)
- **Hardcoded values in components.** Any literal color/spacing in a screen is a token that should
  exist.
- **Semantic tokens pointing at other semantics, or components at primitives.** Keep the tiers clean:
  component → semantic → primitive.
- **Appearance-named semantics** (`blue-button` instead of `action`). Name for role, or a rebrand
  breaks the naming.
