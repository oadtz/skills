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

### Other skills

_(Add new, unrelated skills here as their own entries — one row or short section each.)_

## Adding a new skill

1. Create a folder named after the skill.
2. Add a `SKILL.md` with `name` + a clear, third-person `description` of when to trigger it.
3. If it belongs to an existing set, reuse that set's prefix; otherwise give it its own name.
4. Add a line to the **Index** above so this folder stays self-documenting.
