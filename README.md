# Skills

A personal collection of Claude / Cowork skills. Skills are added here over time and are **not
necessarily related** — each is independent unless it explicitly belongs to a named set.

## How this folder is organized

- **One folder per skill.** The folder name matches the skill's `name` in its `SKILL.md`.
- **Each skill has a `SKILL.md`** (YAML frontmatter + instructions), plus an optional `references/`
  folder for supporting detail. Keep `SKILL.md` focused and under ~500 lines; push depth into
  `references/`.
- **Related skills that form a workflow share a name prefix** (e.g. `ideakit-*`) and get their own
  set-level README. Unrelated standalone skills just sit here as their own entries.

## Index

### `ideakit-*` — business idea pipeline (a related set)

A 4-stage, loosely-coupled pipeline: generate → explore → validate → present. Each stage works
standalone and hands off to the next. Full details in **[ideakit-README.md](ideakit-README.md)**.

| Skill | Role |
|---|---|
| `ideakit-generate` | source new business/startup ideas from trends + real problems |
| `ideakit-explore` | brainstorm / stress-test a direction as a thinking partner |
| `ideakit-validate` | deep-validate a chosen idea → produce a PRD / PLAN.md |
| `ideakit-present` | turn a validated idea into a persuasive deck / demo / one-pager |

### `forge-*` — PRD → product pipeline (a related set)

A 4-stage, loosely-coupled pipeline that turns a validated PRD into a running, production-worthy
product: architect → design → build → ship. Full details in **[forge-README.md](forge-README.md)**.

| Skill | Role |
|---|---|
| `forge-architect` | turn a PRD into a sound technical foundation (stack, data model, ADRs, scaffold) |
| `forge-design` | build a real design system + core user flows, not generic "AI slop" |
| `forge-build` | write the product skeleton-first then slice-by-slice, with verified tests |
| `forge-ship` | harden + release: CI guardrails, security/eval gates, deploy with rollback |

### `solo-*` — solopreneur business pipeline (a related set)

A 4-stage, loosely-coupled pipeline that turns a validated idea into a one-person business that makes
money and lasts: model → fund → distribute → sustain. It's the *commercial* sibling of ideakit/forge
and runs alongside the forge build track. Full details in **[solo-README.md](solo-README.md)**.

| Skill | Role |
|---|---|
| `solo-model` | decide how a solo business makes money + set starting price |
| `solo-fund` | fund the build with minimal dilution (bootstrap → pre-sale → RBF → SEAL → grants) |
| `solo-distribute` | get the first customers via one deep channel + an audience motion |
| `solo-sustain` | run it solo long-term: automation/systems, calm-company defaults, anti-burnout guardrails |

### Other skills

_(Add new, unrelated skills here as their own entries — one row or short section each.)_

## Adding a new skill

1. Create a folder named after the skill.
2. Add a `SKILL.md` with `name` + a clear, third-person `description` of when to trigger it.
3. If it belongs to an existing set, reuse that set's prefix; otherwise give it its own name.
4. Add a line to the **Index** above so this folder stays self-documenting.
