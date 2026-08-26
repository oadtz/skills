# Idea storage handoff

Use this after the venture portfolio exists.

## Contents

- Default destination
- Default portfolio layout
- Idea card fields
- Index row
- Evidence and decision capture
- Custom paths
- Scan and merge existing repositories

## Default destination

Do not ask where the idea set should live. Resolve the destination in this order:

1. Use the path or repository the user already named.
2. Otherwise follow a visible existing idea-storage convention in the current workspace.
3. Otherwise save the minimum portfolio artifact under `outputs/`, marked `unfiled`.

When the host can write files/artifacts, the minimum acceptable save is the generated portfolio
artifact in `outputs/`. If the host truly has no writable destination, say that no durable storage
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

## Outcome log
[empty at generation. Append a dated observable event whenever one occurs — build started or
abandoned, first paid customer or failure to find one, launch, shutdown, pivot — with what it
confirmed or disconfirmed. See `../../ideakit-memory.md`.]

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
