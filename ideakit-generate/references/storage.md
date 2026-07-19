# Idea storage handoff

Use this after the venture portfolio exists.

## Contents

- Ask
- Default portfolio layout
- Idea card fields
- Index row
- Evidence and decision capture
- Custom paths
- Scan and merge existing repositories

## Ask

Ask one concise question, in the user's language, shaped like:

> Where should this idea set live? For example `ideas/` in this repo, another repo/vault, a path you
> name, or the minimum save in `outputs/`.

If the host supports structured choices, offer:

1. `ideas/ portfolio here` — create/update idea cards, index, evidence, and decision notes in this repo.
2. `external repo/vault` — store in another repository, Obsidian vault, notes folder, or user-specified
   path.
3. `outputs/ minimum` — keep the generated portfolio artifact as the saved record, marked unfiled.

When the host can write files/artifacts, do not offer "skip", "do not save", or "chat only". The
minimum acceptable save is the generated portfolio artifact in `outputs/`, labelled unfiled if it has
not entered a portfolio. If the host truly has no writable destination, say that no durable storage
mechanism is available instead of pretending to save.

## Default portfolio layout

When the user chooses `ideas/ portfolio`, use:

```text
ideas/
  index.md
  cards/
  evidence/
  decisions/
```

Create missing folders. Do not overwrite existing cards without reading them first; merge or append a
dated update instead.

## Idea card fields

Create one Markdown card per shortlisted idea:

```md
# [Idea name]

Stage: raw | shaped | validated | prototype | active | parked | killed
Origin: [brief / run / source artifact]
Generated: YYYY-MM-DD

## One-liner
[plain-language idea]

## Problem / Want
[who feels what pain or desire]

## Customer
[primary customer + buyer/user split if useful]

## Route to market
[consumer/DTC, B2B, grant/public, marketplace, creator, services, etc.]

## Evidence
- [signal](url) — [what it supports]

## Venture judgment
Surprise [judgment] · Inevitable in hindsight [judgment] · Enterable [judgment] ·
Value capture [judgment] · Power path [judgment]

## Core labeled lines (carry from the portfolio)
Revelation: · Why others miss it: · Solo entry: · Paid commitment: · Delivered value: · Killer risk:

## Riskiest assumption
[single riskiest assumption]

## Cheapest next test
[one concrete test]

## Notes
[optional nuance, killed/parked reason, links to related ideas]
```

Default `Stage` is `shaped` for portfolio finalists and `raw` for unselected concepts if they are
stored.

## Index row

Append or update `ideas/index.md` with one row per stored idea:

```md
| Idea | Stage | Playing field | Architecture | Portfolio role | Source | Next action |
|---|---|---|---|---|---|---|
| [Idea](cards/idea-slug.md) | shaped | [playing field] | [venture architecture] | [portfolio role] | [portfolio artifact] | [learning test] |
```

Keep the index compact. It is for retrieval and portfolio review, not full reasoning.

## Evidence and decision capture

If the run used several important sources, create or update `ideas/evidence/<brief-slug>.md` with:

- source link
- one-line signal
- which stored ideas it supports
- strength: low / medium / high

If the run had a clear recommendation or front-runner, create
`ideas/decisions/YYYY-MM-DD-<brief-slug>.md` with:

- selected / recommended idea
- why it won
- alternatives kept alive
- killed or parked ideas and why
- suggested next skill (`ideakit-explore` or `ideakit-validate`)

## Custom paths

When the user names a custom path, external repo, or vault:

- inspect existing files first and preserve the local convention when obvious
- if no convention is visible, write the same portable Markdown card/index structure
- confirm the final file paths using the host's normal link/path format

## Scan and merge existing repositories

Before writing to any non-empty destination, follow the Scan and Match protocol in
`../../ideakit-memory.md` (list files, read the index plus a small sample, preserve the local
convention, dedupe by concept, never overwrite existing notes, fall back to `inbox/` when the match
is uncertain). That contract is the single source of truth for merge behavior; this file only adds
the card and index formats above for destinations with no convention of their own.
