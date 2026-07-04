# Idea storage handoff

Use this at Step 6 of `ideakit-generate`, after the ranked shortlist artifact exists.

## Contents

- Ask
- Default portfolio layout
- Idea card fields
- Index row
- Evidence and decision capture
- Custom paths
- Scan and merge existing repositories

## Ask

Ask one concise question:

> อยากให้เก็บชุดไอเดียนี้ไว้ที่ไหนต่อ? เลือกได้ เช่น `ideas/` ใน repo นี้, repo/vault อื่น,
> path ที่คุณระบุ, หรือเก็บขั้นต่ำไว้ที่ `outputs/`

If the host supports structured choices, offer:

1. `ideas/ portfolio here` — create/update idea cards, index, evidence, and decision notes in this repo.
2. `external repo/vault` — store in another repository, Obsidian vault, notes folder, or user-specified
   path.
3. `outputs/ minimum` — keep the generated shortlist as the saved record, marked unfiled.

When the host can write files/artifacts, do not offer "skip", "do not save", or "chat only". The
minimum acceptable save is the generated shortlist artifact in `outputs/`, labelled unfiled if it has
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

## Score
[total]/30 — Pull [x], Market [x], Secret [x], Job [x], Survivability [x], Feasibility [x]

## Riskiest assumption
[single riskiest assumption]

## Cheapest next test
[one concrete test]

## Notes
[optional nuance, killed/parked reason, links to related ideas]
```

Default `Stage` is `shaped` for shortlisted ideas and `raw` for unranked/raw-pool ideas if they are
stored.

## Index row

Append or update `ideas/index.md` with one row per stored idea:

```md
| Idea | Stage | Domain | Route | Score | Source run | Next action |
|---|---|---|---|---:|---|---|
| [Idea](cards/idea-slug.md) | shaped | climate/city | consumer/media/data | 26 | [run](../outputs/run.md) | publish ranking test |
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

Before writing to any non-empty destination, scan it enough to infer its storage convention:

- list top-level files and likely idea folders with `rg --files` or the host's fastest file search
- look for `ideas/`, `notes/`, `inbox/`, `cards/`, `evidence/`, `decisions/`, `index.md`, `README.md`,
  frontmatter, tags, backlinks, or Dataview-style fields
- read the smallest representative set: the index, 2-3 existing idea cards/notes, and any README or
  template that explains the convention
- if it is a git repo, check status before editing; do not stage, commit, or push unless the user
  explicitly asks

Merge behavior:

- preserve the destination's naming, frontmatter, tag, backlink, and folder conventions when they are
  clear
- dedupe by normalized idea name, aliases, and concept overlap; if an existing note is the same idea,
  append a dated "Generated update" or merge missing fields instead of creating a duplicate
- if an existing note is adjacent but not the same, add `Related` links both ways when the convention
  supports links
- update existing index/table rows in place when possible; append only when there is no matching row
- never overwrite or delete existing notes to make room for the new structure
- if confidence is low after scanning, write to an `inbox/` or `ideas/inbox/` area and say the merge is
  conservative
