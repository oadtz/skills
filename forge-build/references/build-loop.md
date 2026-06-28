# The build loop — thin slice first, verify externally

This is the governing principle applied to execution: build the **thinnest end-to-end path first**,
then vertical slices, each **test-first with a gate the building agent can't edit.** Use across Steps
1–4 of forge-build.

## Walking skeleton (Step 2 — do this before any feature)

The walking skeleton is "the thinnest possible slice of real functionality that we can automatically
**build, deploy, and test end-to-end**" (Cockburn; Freeman & Pryce). One trivial request flowing
through every architectural layer, plus a real (even if empty) deployment and CI run.

- **Why first:** it "forces us to face the difficult infrastructural problem first, while we still have
  time and the code base is almost empty." Integration and deployment are the expensive, surprising
  parts — pay them down before complexity accumulates, not after.
- **Done when:** the skeleton builds, its one test passes, and it deploys green through CI. Every later
  slice now has a proven path to plug into.

Source: https://www.mattblodgett.com/2020/09/start-with-walking-skeleton.html

## Vertical slices (Step 1 — how to decompose)

After the skeleton, add **vertical slices**, never horizontal layers. A slice spans UI → logic → data
for **one user-facing capability**. Rule: *minimize coupling between slices, maximize coupling within a
slice* (Jimmy Bogard).

- **Why slices, for agents specifically — locality of reference:** a slice lets the agent ingest a
  feature's complete context in one pass, "without needing to hallucinate dependencies." Horizontal
  layers scatter a feature across the codebase and force the agent to guess.
- **Each slice must be:** independently demoable/verifiable, small (≈≤2–3 days), and dependency-ordered
  so finishing it *unblocks* the next without needing other features first.
- **Tag each slice HITL or AFK:** HITL (human-in-the-loop) slices touch auth, data access, money,
  irreversible actions, or anything subtle — a human reviews the diff before merge. AFK ("away from
  keyboard") slices are low-risk enough for the agent to complete and the gate to verify unattended.

Sources: https://www.jimmybogard.com/vertical-slice-architecture/ ,
https://explainx.ai/skills/mattpocock/skills/prd-to-issues

## Testable acceptance criteria (EARS)

Each slice gets acceptance criteria in **EARS** form before any code:

> **WHEN** [trigger/condition] **THE SYSTEM SHALL** [observable behavior].

EARS bans vague words ("fast", "user-friendly") so every line is concrete enough to write a test
against. Vague criteria are the #1 cause of agent drift. Example: "WHEN a user submits the form with an
empty email field, THE SYSTEM SHALL display an inline 'email required' error and not submit."

Source: https://kiro.dev/docs/specs/feature-specs/

## The slice loop (Step 3 — test-first)

For each slice, in dependency order:

1. **Write the tests first** from the acceptance criteria — no implementation yet.
2. **Run them; confirm they fail (red).** A test that passes before implementation tests nothing.
3. **Commit the failing tests as a checkpoint.** This is the anti-reward-hacking move: any later edit
   to the tests now shows up in the diff.
4. **Implement until green — without modifying the tests to pass.** Agents will sometimes weaken
   assertions, special-case test inputs, or delete failing tests. That's reward hacking (METR observed
   >50% on impossible tasks). The committed checkpoint + the external gate below catch it.
5. **Refactor while green.** AI code arrives duplicated and under-refactored — pay the copy-paste tax
   here, per slice, not "later."

Why TDD fits agents: "everything that makes TDD a slog for humans makes it the perfect workflow for an
AI agent" — a binary pass/fail test is the clearest goal you can give one.

Sources: https://www.anthropic.com/engineering/claude-code-best-practices ,
https://www.builder.io/blog/test-driven-development-ai , https://metr.org/blog/2025-06-05-recent-reward-hacking/

## External verification (Step 4 — the loop-closer)

"Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal" —
so give it an external check, and **make sure the agent that wrote the code is not the one grading it.**

Escalating rigor (use what the host supports):
1. Run the gate inline — tests + type-check + lint + build — and read the **actual output**, not the
   agent's summary.
2. A standing goal/condition the agent re-checks each turn.
3. A **stop hook** that deterministically blocks "done" until the gate passes (the agent can't end the
   turn red).
4. A **separate verifier subagent** with fresh context, prompted to *refute* the result — so the grade
   isn't self-issued. For HITL slices, a human reviews the **test diffs**, not just the green check.

**Verify behavior, not claims:** for UI/feature slices, require observable evidence — a screenshot, a
real request/response, a running process. Use an available app-verification capability (for example
`verify` / `run`, if installed) to drive the real app.

**Triage rule:** is the expected value derivable from code the agent can read, or from a spec it never
saw? Tests grounded only in the agent's own code can pass while the product is wrong. Anchor critical
assertions to the spec/PRD, not to the implementation.

## Done means

A slice is done when: the external gate is green (tests + type + lint + build), behavior is verified
with observable evidence, the change is small and reviewable, and — for HITL — a human has reviewed the
diff (including test changes). Then merge small, update `progress.md`, and move to the next slice.
