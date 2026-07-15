# AI engineering foundation — default operating model

Read this from every `ideakit-*`, `solo-*`, and `forge-*` skill. Apply it by default whenever software
or a digital product is in scope. A local skill may specialize the model, but must not silently restore
a product-scope ceiling based only on one human's coding hours or the absence of human employees.

## Contents

- Default premise
- Replace the old constraint model
- Apply the premise across Ideakit, Solo, and Forge
- Decision rules
- Handoff fields for software work

## Default premise

Assume **one founder can direct an AI engineering team**.

Treat AI coders as engineering capacity that can plan, implement, test, inspect, document, migrate,
refactor, and maintain software under explicit context, interfaces, permissions, acceptance criteria,
and escalation. Treat the founder as the source of product direction, consequential judgment, risk
ownership, and final acceptance—not as the person who must type every line.

Separate the production method from the product:

- **AI-developed product:** AI coders help build or maintain it. The shipped product may be ordinary,
  deterministic software with no model or agent at runtime.
- **AI-native product:** AI inference or agents are part of the customer-facing value or runtime.

Default to the first. Require the second only when it is the right product mechanism. Do not add a
chatbot, agent, generated output, AI positioning, or runtime model merely because AI coders built the
software. Customers usually buy the outcome, not the production method.

Do not force a non-software opportunity to become software. This foundation changes feasible software
production; it does not make software the answer to every business problem.

## Replace the old constraint model

Do not reason from:

`founder coding hours → feasible product scope`

Reason from:

`founder direction + AI engineering capacity + verification + operational control → feasible product scope`

Conventional engineering headcount, repository size, feature count, or what one human could implement
after work are not default rejection criteria. A broad product, maintained variants, many integrations,
or a multi-module system may be valid when the directed system remains controllable.

Keep the real constraints visible:

- **Directability:** Can the founder express intent, non-goals, boundaries, and acceptance criteria?
- **Decomposability:** Can work split across stable components and interfaces?
- **Verifiability:** Can tests, evals, reviews, and observable outcomes distinguish correct work from
  plausible-looking work?
- **Integrability:** Can parallel changes merge without unbounded regression and review burden?
- **Operational control:** Are deployment, permissions, observability, rollback, maintenance, and
  incident response explicit?
- **Failure containment:** Is blast radius proportionate to the reliability of the delegated work?
- **Founder attention:** Do recurring decisions, reviews, exceptions, and escalations stay bounded as
  product breadth grows?
- **Engineering economics:** Do model, tool, compute, storage, review, and failure costs work?
- **External bottlenecks:** Demand, distribution, trust, data rights, permissions, liability, capital,
  physical operations, and customer change do not disappear because code is cheap.

Do not assume unlimited autonomy. Expand scope where delegation and control make it feasible; narrow or
sequence work when a control-plane or external bottleneck remains unresolved.

## Apply the premise across the skillset

### Ideakit

- Reconstruct engineering work and coordination whose economics changed before filtering software
  opportunities by founder capacity.
- Generate the complete product or company architecture; do not default to micro-SaaS, a single
  feature, or permanent manual service because the founder lacks a human team.
- Test the riskiest external dependency or control loop first. A small proof earns the right to build;
  it does not redefine the long-term ambition.
- Preserve `Product AI dependency` as `none`, `build-time only`, `optional runtime`, or `core runtime`.

### Solo

- Treat AI engineering capacity as capacity the founder already controls when it is directable and
  verifiable. Do not choose the revenue model by minimizing implementation scope alone.
- Optimize for value capture, time to evidence or cash, and sustainable **founder attention**. Keep
  customer support, sales, trust, fulfillment, legal, and exception load honest.
- Distinguish build labor from operating labor. AI coders may remove the former without removing the
  latter; automate or design the operating system instead of pretending the burden is gone.
- Do not market the product as AI-built unless that fact changes customer value, trust, or risk.

### Forge

- Architect for directed parallel execution: explicit module boundaries, contracts, source-of-truth
  context, agent-readable decisions, and dependency order.
- Build through bounded work packets with external verification. Let multiple AI coders expand
  throughput without letting them silently redefine architecture or acceptance.
- Make the control plane durable: tests, evals where behavior is probabilistic, CI gates, permissions,
  work traces, observability, rollback, and escalation.
- Apply AI-runtime evals only when the product actually contains runtime AI. Apply ordinary software
  quality and security gates to AI-developed conventional software.

## Decision rules

1. Do not reject or shrink a product solely because one founder could not code it manually.
2. Do not require customer-facing or runtime AI merely because AI coders are the engineering team.
3. Do not equate generated scope with value; retain demand, distribution, and value-capture evidence.
4. Do not equate many agents with a team unless work has interfaces, acceptance, integration, and
   escalation.
5. Budget founder **attention and consequential decisions**, not personal implementation throughput.
6. Preserve ambition while sequencing proof around the most dangerous external or control-plane risk.
7. If a local instruction conflicts only by reintroducing human implementation labor as the ceiling,
   this foundation wins. Safety, truthfulness, external authorization, affordable loss, and actual
   operating risk still win over ambition.

## Handoff fields for software work

Carry these when they affect the next stage; do not force them into unrelated prose:

- `Product AI dependency:` none | build-time only | optional runtime | core runtime
- `Founder control surface:` consequential decisions and boundaries retained
- `AI engineering work absorbed:` delegated engineering work and coordination
- `Verification loop:` tests, evals, review, observability, rollback
- `Human attention budget:` recurring decisions, exceptions, and escalation
- `External bottleneck:` constraint more generated code cannot remove
- `Failure containment:` permissions, stop conditions, blast-radius limits, recovery
- `Scope made feasible:` product boundary newly credible under AI engineering economics
