# Context engineering — one thing per loop, state on disk

This is the governing principle applied to memory and attention: **one thing per loop, state on disk.**
Drift over a long build is mostly a context-hygiene failure, not a model failure. Use throughout
forge-build.

## Why context rots

An LLM's attention scales roughly with the square of the tokens it must relate; as context grows, that
attention spreads thin and accuracy declines. This is architectural, not a quirk. The four named
failure modes (Willison / dbreunig): **poisoning** (a wrong fact lodges and recurs), **distraction**
(volume drowns the goal), **confusion** (irrelevant material misleads), **clash** (contradictory
context). Long marathon sessions hit all four.

Sources: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ,
https://simonwillison.net/2025/Jun/29/how-to-fix-your-context/

## Curate context per slice

- **Tight rules file.** `CLAUDE.md` / `AGENTS.md` at ~80–120 lines (hard ceiling well under 200) —
  build/test/lint commands, conventions, "always/never" rules, and a *link* to `docs/adr/`. Files over
  ~200 lines measurably *reduce* adherence; bloated auto-generated rules files even *raise* cost and
  *lower* success. Reference canonical example files; don't paste code (it goes stale).
- **Repo map for orientation.** A token-budgeted map of the most-referenced classes/functions and
  their signatures (e.g. Aider's tree-sitter + PageRank map) teaches the agent the existing
  abstractions so it respects them instead of re-implementing them.
- **ADRs linked, not inlined.** The "why" loads on demand (see `forge-architect/references/adr-guide.md`).
- **Tool discipline.** More than ~20 available tools starts to confuse models — keep the loadout per
  slice minimal.

Sources: https://code.claude.com/docs/en/memory , https://cursor.com/blog/agent-best-practices ,
https://aider.chat/docs/repomap.html

## One thing per loop; fresh context

- **Build one slice per loop.** The "Ralph" pattern (Geoffrey Huntley): re-feed a stable prompt into a
  *fresh-context* agent each iteration, with the rule "only one thing per loop." Fresh context each
  loop sidesteps rot; tests + type-checks provide the "backpressure" after each change.
- **Clear context or start a new session on task switches** (e.g. `/clear` in Claude Code). Don't
  carry a finished slice's detailed context into the next one.
- **Isolate sub-tasks.** Run research, planning, and building as separate sessions/subagents; only a
  condensed summary returns to the orchestrator, so detailed search context never pollutes higher-level
  reasoning. This is the single most effective structural defense against drift.

Caveat on the Ralph loop: it's for **greenfield** builds ("there's no way I'd use Ralph in an existing
code base"), and known failure modes include placeholder/stub implementations and duplicate
implementations — so instruct the agent to **search before assuming something isn't implemented yet.**

Sources: https://ghuntley.com/ralph/ , https://code.claude.com/docs/en/sub-agents

## State on disk — the durable memory

The context window is the only short-term memory; durable workspace files survive `/clear`,
compaction, and restarts. Maintain:

- **`plan.md`** — the dependency-ordered slice list, with acceptance criteria. The index of the build.
- **`progress.md`** — what's done, what's in flight, what's next. Updated after every slice; this is
  how the next loop knows where it is.
- **`decisions.md`** — deviations from the plan and *why* (promote anything irreversible to an ADR).
- **A per-slice todo list** with item status, which continuously re-injects the current goal and
  counters distraction.

Persisting state + running one thing per loop is what lets the build survive context resets without
losing the thread. Fresh context each iteration beats a rotting marathon session.

Source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
