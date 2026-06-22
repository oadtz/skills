# Architecture patterns — decide explicitly, design before code

This is the governing principle applied to structure: **decide explicitly** what the model would
otherwise pick for you, and design the contracts *before* the agent writes code. Use in Step 3 of
forge-architect.

## Default: modular monolith

For an MVP, or any team under ~10 developers, default to a **modular monolith** — a single deployable,
divided internally into modules with well-defined boundaries.

- **Why not microservices first:** "Almost all the successful microservice stories started with a
  monolith that got too big and was broken up. Almost all the cases where a system was built as a
  microservice system from scratch ended up in serious trouble." (Martin Fowler, *MonolithFirst*.)
  Microservices carry a premium — network calls, deployment, observability, distributed data
  consistency — that only pays off past ~10 developers. **You discover the correct service boundaries
  by building the monolith first.**
- **Modular, though.** A monolith is not a mud ball: enforce module boundaries internally (clear
  public interfaces per module, no reaching into another module's internals). When a boundary proves
  stable *and* you have a real scaling reason, you can extract it.
- Any deviation from modular monolith (microservices, serverless-everything, event-sourcing) needs an
  ADR justifying the premium for *this* product.

Sources: https://martinfowler.com/bliki/MonolithFirst.html ,
https://martinfowler.com/articles/dont-start-monolith.html (the counter-case: only when domain
boundaries are already proven).

## Design before code — the ordering

Each artifact below becomes machine-readable context that narrows the agent's search space in the
build. Do them in this order; each constrains the next.

### 1. Domain model + ubiquitous language
Name the core entities and define them precisely ("an order is a customer commitment created at
checkout"). A shared, precise vocabulary reduces agent misinterpretation. If the domain is rich,
identify **bounded contexts** — areas with their own consistent language — which act as natural module
boundaries. Event Storming (events → commands → aggregates) is a lightweight way to discover them.
Source: https://martinfowler.com/bliki/BoundedContext.html

### 2. Data model / schema
Design the schema as a single source of truth (e.g. one `schema.prisma` or equivalent). A type-safe
generated client constrains both humans and agents and gives AI tools accurate field/relation context
so they don't hallucinate columns. Decide the data store here — it's hard to reverse, so it gets an
ADR.

### 3. API contract (when there's a service boundary)
If the product has a client/server split or multiple services, define the **API contract first**
(e.g. OpenAPI; TypeSpec if hand-writing YAML is error-prone). Generate stubs, client types, and mocks
from it so front and back can't drift, and add a contract-diff check in CI.

- **Caveat from the source:** codegen-from-contract pays off only when the contract is *relatively
  stable*. If the spec is still in flux, you'll spend more time regenerating than you save — so for an
  early, single-surface app, a lighter contract (or none yet) is the right call. Don't impose API-first
  ceremony on a tiny app.

Source: https://devblogs.microsoft.com/ise/design-api-first-with-typespec/

## What to NOT over-build (YAGNI, with the carve-out)

- **Defer presumptive features.** Don't build for hypothetical future needs — Microsoft research found
  only ~⅓ of built features improved their target metric. Build/delay/carry/repair are all real costs.
- **"Design for 10×, expect to rewrite before 100×."** Building for 1000 tps instead of 10 costs more
  to build and operate with zero benefit until you near that scale. Premature scaling is the #1
  startup killer.
- **Premature optimization** — skip small efficiencies ~97% of the time, but *don't* pass up the
  critical 3%; optimize after measuring, not before.
- **The carve-out:** YAGNI does **not** excuse neglecting code health, and it does **not** apply to
  hard-to-reverse architectural decisions. Those still need upfront thought — and an ADR.

Sources: https://martinfowler.com/bliki/Yagni.html ,
https://startupgenome.com/insights/a-deep-dive-into-the-anatomy-of-premature-scaling

## Documenting the architecture (lean)

- **C4 model, Context + Container only** for an MVP. The System Context (who/what touches the system)
  and Container (the deployable units — apps, datastores; *not* Docker containers) levels are enough.
  Skip the Code level — it drifts the instant you write code and duplicates the source.
- **Diagrams-as-code** (e.g. Mermaid) in-repo, so the diagram versions and diffs with the code and
  renders natively in markdown.
- Heavier options (arc42, all four C4 levels, full UML) are over-engineering for a solo/MVP build —
  reach for them only when comprehensive docs are genuinely warranted.

Source: https://c4model.com/

## Anti-patterns to flag

- **Microservices / serverless-everything / event-sourcing by default.** MVP over-engineering; each
  needs an ADR justifying its premium.
- **Skipping the data/contract design and "letting the agent figure it out."** That's how the model
  silently becomes your architect.
- **Over-specifying implementation detail.** Specify boundaries and contracts; the agent fills the
  inside. Exhaustive upfront specs revive waterfall and produce unmaintainable structure.
