# One founder directing an AI engineering team

Use this default model for every software or digital product opportunity. Assume one founder directs
coding agents to build and maintain software whose breadth, customization, integration load, or release
cadence may previously have implied a human engineering organization.

## Premise

Treat AI as **engineering capacity**. Do not treat it merely as a product feature, a faster code
completion tool, or an unlimited autonomous company.

Separate the production method from the product architecture:

- **AI-developed product:** AI coders plan, implement, test, integrate, document, or maintain it. The
  shipped product may be deterministic conventional software with no model or agent at runtime.
- **AI-native product:** AI inference or agents are part of the customer-facing value mechanism or
  runtime operation.

This mode requires the first and does not require the second. Do not add chat, generation, agents, or
an AI value proposition merely to justify the AI engineering team. Research the customer's actual job
and alternatives without assuming they care how the software was produced.

The founder owns product intent, consequential architecture and risk decisions, acceptance criteria,
and escalation. The agent team may plan, implement, test, inspect, document, migrate, refactor, and
maintain work when context, interfaces, permissions, and verification make that delegation credible.

Do not use conventional engineering headcount or founder coding hours as the product-scope ceiling.
Do not infer venture value from repository size or feature count. The binding constraint becomes the
founder's ability to direct and verify the system, plus external constraints that generated code cannot
remove.

## 1. Reconstruct the engineering cost curve

Before inventing products, map the work that a conventional organization would perform:

| Workstream | Conventional roles / coordination | Delegable unit | Context and interface required | Verification | Founder decision / escalation | Residual cost or risk |
|---|---|---|---|---|---|---|
| Product surface | ... | ... | ... | ... | ... | ... |
| Architecture / platform | ... | ... | ... | ... | ... | ... |
| Integrations / migrations | ... | ... | ... | ... | ... | ... |
| QA / security / reliability | ... | ... | ... | ... | ... | ... |
| Documentation / release | ... | ... | ... | ... | ... | ... |
| Maintenance / incidents | ... | ... | ... | ... | ... | ... |

Use current evidence for claims about model, agent, tool, or infrastructure capability. A benchmark,
demo, or generated code sample shows a capability signal; it does not by itself prove unattended
production operation.

Identify what actually changed:

- fixed engineering work becoming variable or repeatable;
- coordination being replaced by explicit interfaces and machine-readable acceptance criteria;
- customization becoming maintainable instead of one-off consulting debt;
- integration or migration work becoming continuously regenerable;
- testing, documentation, and release work scaling with the generated surface;
- small markets supporting broad products because engineering cost no longer requires mass-market
  economics.

If the map only says “coding is faster,” continue. Find the changed product boundary, feasible breadth,
customization model, release model, or business architecture.

Record `Product AI dependency` as `none`, `build-time only`, `optional runtime`, or `core runtime`.
Treat `none` and `build-time only` as fully valid outcomes.

## 2. Run the organizational-compression lane

Add one isolated invention lane to breakthrough mode. Give it the neutral signal pack plus the cost
curve map, but no candidate products.

Use these operators selectively:

- **Compress the engineering organization:** ask what product previously required several specialist
  roles and coordination layers, then redesign its control plane for one founder plus agents.
- **Invert customization:** replace one shared compromise product with maintained variants or generated
  modules when verification and upgrade paths can remain common.
- **Invert integration economics:** pursue jobs rejected because connectors, migrations, or per-customer
  adaptation consumed too much engineering labor.
- **Multiply the product line:** ask whether one shared platform, corpus, or evaluation harness can
  support several coherent products without multiplying founder attention at the same rate.
- **Build the whole workflow:** reconsider boundaries created by historical team or vendor constraints,
  but retain boundaries required by trust, regulation, data ownership, or failure containment.
- **Remove coordination software:** when agents can execute the work, ask whether a tool for coordinating
  humans should become an outcome-producing system instead.
- **Make maintenance part of the product:** treat continuous adaptation, migration, testing, and repair
  as a product capability rather than an after-sale labor burden.

Return seeds as:

`actor | trigger/job | product boundary newly feasible | AI engineering work | founder control surface |
verification loop | external bottleneck | payer | architecture`

Reject a seed when AI only decorates an ordinary category or shortens the build schedule without
changing what can be offered, to whom, or at what economics.

## 3. Design the founder control plane

For every serious concept, make the directed engineering organization legible:

1. **Intent:** product thesis, user outcome, non-goals, and irreversible decisions.
2. **Decomposition:** repositories, components, interfaces, work queues, ownership, and dependency
   order.
3. **Context:** specifications, architecture decisions, domain rules, examples, and source-of-truth
   data available to each agent.
4. **Acceptance:** deterministic tests, behavioral evals, security checks, performance budgets, and
   human review gates.
5. **Permissions:** least-privilege access to code, infrastructure, data, deployment, and third-party
   systems.
6. **Integration:** merge policy, contract tests, migration strategy, release sequencing, and rollback.
7. **Observability:** product outcomes, system health, agent work traces, exceptions, and cost.
8. **Escalation:** conditions that stop automation and require a founder decision or domain expert.
9. **Maintenance:** dependency updates, incident response, model/tool change, regression detection, and
   recovery.

The control plane may itself be part of the product advantage, but do not claim a moat merely because
agents are used.

## 4. Apply the new feasibility gates

Judge these independently:

- **Directable:** Can the founder state outcomes, boundaries, and acceptance criteria precisely enough
  for work to proceed without continuous implementation-level rescue?
- **Decomposable:** Can work be partitioned with stable interfaces, or will hidden coupling force the
  founder to reconstruct the whole system for every change?
- **Verifiable:** Can tests and evals catch plausible but wrong output before it reaches customers?
- **Integrable:** Can independently produced work merge without an unbounded review and regression
  burden?
- **Operable:** Are deployment, observability, support, maintenance, and incident paths explicit?
- **Containable:** Are permissions, blast radius, rollback, and escalation proportionate to failure
  cost?
- **Attention-bounded:** Does product breadth grow faster than recurring founder decisions and
  exceptions?
- **Economically sound:** Do model, tool, compute, storage, review, and failure costs preserve viable
  unit economics?
- **Externally enterable:** Can the founder obtain demand evidence, distribution, data rights, trust,
  permissions, and capital that generated engineering cannot substitute for?

Do not fail a concept because the founder could not implement it manually or because a conventional
company would assign many engineers. Fail or reframe it when direction, verification, integration,
operation, containment, attention, economics, or an external dependency is not credible.

## 5. Separate ambition from the first external proof

Keep the complete product or company thesis visible. Choose the first move to resolve the most dangerous
external or control-plane uncertainty—not to minimize lines of code.

A landing page, design-partner agreement, data-access commitment, integration sandbox, architecture
spike, adversarial eval, or paid pilot may be the correct first proof. None requires redefining the
destination as a micro-SaaS or manual service.

State both:

- **Full architecture:** what the founder-directed AI engineering organization ultimately makes
  feasible;
- **Right-to-build test:** the smallest credible proof that earns the next tranche of engineering,
  infrastructure, data, or risk.

## Output contract

For each finalist, include:

- `AI engineering work absorbed:` engineering work and coordination absorbed;
- `Product AI dependency:` none, build-time only, optional runtime, or core runtime;
- `Previously required organization:` conventional roles or team shape compressed;
- `Founder control surface:` decisions and boundaries retained by the founder;
- `Delegation architecture:` agent work partition and component/repository boundaries;
- `Verification loop:` tests, evals, reviews, observability, and rollback;
- `Human attention budget:` recurring reviews, decisions, exceptions, and escalation;
- `External bottleneck:` demand, distribution, data, trust, permission, capital, or liability;
- `Failure containment:` permissions, blast-radius limits, stop conditions, and recovery;
- `Scope made feasible:` product scope or business architecture that human engineering economics had
  blocked.

## Anti-patterns

- adding “AI-powered” to an ordinary SaaS while retaining the same product boundary and economics;
- requiring customer-facing AI, an AI runtime, or AI branding merely because AI coders built the
  product;
- assuming generated code equals an integrated, secure, maintainable production system;
- shrinking the thesis because the founder lacks human engineering hours or employees;
- counting agents or parallel tasks without specifying interfaces, acceptance, and integration;
- building a large opaque monolith that the founder cannot inspect through tests, evals, or telemetry;
- using a tiny manual service as the permanent architecture when AI execution enables a larger one;
- ignoring customer access, data rights, trust, permissions, liability, or distribution because the
  software can be generated;
- treating model autonomy as constant instead of designing for tool changes, regression, and
  escalation.
