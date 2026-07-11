# Ideakit — Execution contract (do the work, don't just advise)

Read this in every `ideakit-*` skill. These skills think *with* the user — but thinking should end in
**real artifacts produced with the right tool**, not a description of what could be produced. This file
is the family-level execution guard; it's self-contained so `ideakit-*` stays standalone.

## The principle

**Produce, don't propose.** Each ideakit stage has a concrete deliverable — an edge map, a ranked idea
table, a sharpened direction, a PRD, a pitch. Once the user has steered the thinking, **make that
deliverable real with the appropriate tool** and hand it over, rather than offering to do it.

## What "executing" looks like per skill

- **ideakit-discover** → actually write the **edge map** as a file the user can carry forward (and run
  the react-to-concretes research live, fetching real examples to react to).
- **ideakit-generate** → actually **run the searches** (don't describe the scan), synthesize openings
  and opportunity theses, then produce the venture portfolio with cited observations, labeled
  inference/bets, wedges, and learning tests—as a file, not a verbal summary—and ask where it belongs.
- **ideakit-explore** → capture the session's output (options, assumptions, the front-runner, next
  experiments) as a real artifact, not just talk; draw the tree/diagram when it helps; update idea
  memory when a stored idea/location is in play.
- **ideakit-validate** → actually **do the research** (search + fetch) and **write the PRD file**
  (`outputs/<slug>-PLAN.md`) — the skill's whole point is a written, buildable plan, not a verbal one;
  update the matching idea memory with the PRD link and validation outcome when available.
- **ideakit-present** → actually **build the deck / one-pager / demo** as a file (using the document
  skills where polish matters), not an outline of one; update idea memory with the pitch artifact when
  available.

## Pick the right tool for the job

- **Web research** (search + fetch) — for generate's scan and validate's market/competitor/demand work;
  always under the grounding discipline (cite or mark as assumption; never invent market data).
- **File tools** — write the edge map, shortlist, PRD, or pitch as a real file.
- **Document skills** (docx/pptx/pdf) — when the deliverable should be a polished deck or document.
- **Code / shell** — when a quick calculation, data pull, or diagram-generation helps the analysis.
- **Connectors / MCP** — if connected, mine first-party signal (analytics, CRM, support tickets) for
  real evidence instead of public proxies.
- **Share the result** — deliver the finished file; don't bury the deliverable in chat prose.

## Keep the human-judgment gates

These skills are collaborative by design — keep the moments where the user picks the direction, chooses
the idea, approves the sharpened framing, or confirms the snapshot. Execution means: once they've
steered, *build the artifact fully* rather than re-summarizing it. Never decide the user's idea *for*
them; never fabricate evidence to make a deliverable look finished.

## The hard boundary (never cross without explicit, per-action confirmation)

Prepare, but don't autonomously perform: anything that **acts in the outside world from the user's
identity** (publishing the pitch, emailing investors/customers, posting the idea publicly), **spends
money**, or is **irreversible**. Draft and stage it; hand the user the final send/publish/pay step.

## In short

Do the research for real, write the actual deliverable file with the right tool, keep the user in
charge of direction — and stage any outward-facing or money-touching action for their approval.
