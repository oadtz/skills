# The anti-slop brief — constrain before you generate

This is the governing principle applied to generation: **constrain before you generate.** Generic "AI
slop" is a constraint problem, not a capability problem. Use this in Step 1 of forge-design, and carry
the brief into every UI generation throughout the build.

## Why AI UI looks the same

LLMs interpolate the **median of their training data**. Ask for "a landing page" with no constraints
and you get the median of every Tailwind tutorial scraped 2019–2024 — which is why the signature look
(centered hero card, `bg-indigo-500` purple gradient on white, three-icon feature grid, Inter
everywhere) recurs. Tools like v0 are narrowly trained on shadcn/ui + Tailwind, so their output is
competent but homogeneous. None of this is a capability ceiling — it's an *unconstrained prompt*.

Source: https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website

## The brief — four parts

Write this once per product and reuse it in every UI generation prompt.

### 1. Negative constraints (the highest-leverage, nearly-free lever)
State explicitly what to **avoid**. Transformers perform negation at inference — naming a pattern
actively lowers its probability weight. Most people only say what they want; saying what to avoid is
what kills the default.

Starter list (tune per product):
- No Inter / Roboto / Arial as the primary typeface.
- No purple/indigo gradient on a white background.
- No centered hero card as the landing pattern.
- No three-icon-box feature grid.
- No timid, evenly-weighted color palette.

### 2. Described references (transfer taste, don't ask for it)
Gather **3–5 references** (Dribbble, Mobbin, real products) and describe *why each works* — the layout
logic, the type pairing, the color relationships, the spacing/density. Feed the *descriptions* plus the
functional requirements. "Make it beautiful" asks the model for taste it doesn't have; "dense
information layout like Linear, a type scale with strong contrast like Stripe, a warm accent on a near-
black surface" transfers concrete decisions.

### 3. Persona priming
Prime the role: "You are a senior frontend engineer with a print-design background." This shifts the
sampling distribution away from the tutorial median toward more deliberate craft.

### 4. Explore, don't converge
Ask for **3 directions, not 1.** One request converges on the first (often generic) local maximum;
three forces exploration of the solution space. Then iterate **one dimension at a time** ("same layout,
bolder headers") rather than regenerating wholesale.

## A reusable aesthetics frame

The Anthropic Cookbook aesthetics approach externalizes taste into four named, repeatable dimensions —
use them as headings in the brief:

- **Typography** — distinctive over generic; a real type scale with contrast.
- **Color** — a dominant color + sharp accents beats a timid, even palette.
- **Motion** — one orchestrated page-load reveal beats scattered micro-interactions.
- **Backgrounds** — layered gradients/geometry for depth, not flat fills.

The **`frontend-design`** skill (if installed in your environment) encodes the same anti-slop approach
— invoke it for the visual direction rather than re-deriving it here.

Sources: referenced via prg.sh above;
https://moelkholy1995.medium.com/beyond-make-it-beautiful-the-anti-slop-framework-for-ai-frontend-craftsmanship-c99bbee6c994 ,
https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it

## Caution

- **AI is a draft engine, not a finisher.** Output that "still looks AI-generated" means the brief was
  too thin — name what's generic and tighten the constraints, don't accept it.
- **One-command "anti-slop" tools** mostly repackage this same brief-and-constraints method. Understand
  the method; don't treat the tool as magic.
- The durable principle: **AI provides speed and execution; the human provides taste and the
  constraints.**
