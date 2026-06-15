# Deep Validation Playbook

Use this playbook in Phase 2 of the ideakit-validate skill. Goal: build an evidence-backed picture of
whether the idea is real, viable, and worth doing — before producing a PRD.

Run searches in **parallel batches** where the host supports it. Use multiple distinct query
phrasings per topic. Cite every claim.

## What "Deep" Means Here

This is not a 5-minute Google. Plan to run **15–30 searches** across the categories below,
synthesize the findings, and pause to report back to the user before moving on. If you find
contradictory data, surface the contradiction.

A note on AI-sourced ideas: if the idea came from ideakit-generate (or any AI generation), treat its
stated feasibility and novelty as a hypothesis, not a finding. Machine-generated ideas reliably
over-rate their own feasibility — so weight real demand evidence (complaints, spend, behavior)
above plausible narrative, and put extra rigor into investigations 5, 6, and 7 below.

## The Eight Investigations

### 1. Existing Solutions / Direct Competitors

**Goal**: Identify the top 3–7 alternatives that solve the same or adjacent problem.

**Queries to run** (adapt to the idea):
- `"[problem statement]" tools` / `best [category]` / `top [category] [current year]`
- `[idea description] alternative` / `vs [obvious competitor]`
- `open source [category]` / `free [category]`
- Reddit, Hacker News, Product Hunt searches: `[category] site:reddit.com`, `site:news.ycombinator.com [category]`
- For each competitor found: pricing page, recent reviews (G2, Capterra, Trustpilot, Reddit threads)

**Capture for each competitor:**
- Name + 1-line description
- Strengths users praise
- Gaps or complaints (this is where the opportunity lives)
- Pricing model and price range
- URL

### 2. Demand Signals

**Goal**: Quantitative or anecdotal evidence that real people want this.

**Sources & queries:**
- Reddit: `site:reddit.com "I wish there was a [thing]"` / `site:reddit.com [problem]`
- Hacker News: `site:news.ycombinator.com [problem]` (look at comment volume, upvotes)
- GitHub: search for related issues, feature requests, or "show HN" threads
- Twitter/X: `[problem] OR [pain point]` (look for engagement)
- Quora, Stack Overflow, niche forums for the audience
- Google Trends for the relevant keywords (direction of trendline matters more than absolute number)

**Quantify wherever possible.** "47 people asked for X in the last 12 months on r/foo" is more
useful than "people on Reddit want X."

### 3. Market Size & Adjacency

**Goal**: Is this a real market or a vanishingly small niche? What adjacent markets exist?

**Queries:**
- `[category] market size` / `[category] TAM`
- Industry reports (Gartner, Forrester, IDC, Statista) — usually only headline figures are free,
  but headlines are often enough
- Adjacent categories: who already serves this audience with something else?
- Trend direction: is the underlying activity growing or shrinking? (Job postings, search trends,
  funding rounds in the space)

For software: also check funding signals — Crunchbase, recent VC investments in the category.

### 4. Pricing & Business Model Patterns

**Goal**: How do similar things make money? What price points are typical?

**Capture:**
- Free tier? What's free vs. paid?
- Pricing tiers (typical: free / starter ~$10–30/mo / pro ~$50–200/mo / enterprise custom)
- Per-seat vs. per-usage vs. flat
- Self-serve vs. sales-led
- Outliers worth noting (anything radically different)

This shapes the v1 monetization assumptions in the PRD.

### 5. Feasibility

**Software mode:**
- What technology stack is typical for this kind of thing?
- Are there off-the-shelf libraries / APIs / SaaS that do most of the work?
- Build-vs-buy options (use a no-code platform? wrap an existing API?)
- Hard parts: anything that requires unusual expertise (ML training, real-time, scale, regulatory)
- Time-to-MVP estimate (range: weekend / 2–4 weeks / 1–3 months / 6+ months)

**General mode:**
- Standard playbook for this kind of initiative — does one exist?
- Required skills or roles
- Required tools, vendors, or partnerships
- Cost ranges for similar initiatives

### 6. Platform & Ecosystem Replication Risk ⚠️ CRITICAL

**This investigation was added in v0.2 after a real-world miss. Skipping it can kill an idea
6 months into the build.**

The biggest threat to a software product in the current AI platform era is not a direct competitor —
it's a major platform launching the same capability as a built-in feature, plugin, or skill. Apple, Google,
Microsoft, Meta, OpenAI, Anthropic, and large vertical SaaS vendors are all racing to absorb
features into their platforms.

**Mandatory questions to answer:**

1. **Could this product reasonably live as a plugin, skill, extension, or feature within a larger
   platform?** (Claude plugins, ChatGPT GPTs/Actions, Cursor extensions, Apple Shortcuts,
   browser extensions, Notion integrations, Slack apps, Salesforce apps, Shopify apps, etc.)
2. **What has the dominant platform shipped in the last 6 months that's adjacent to this idea?**
   Search the platform's blog, changelog, and tech press coverage explicitly.
3. **What's the dominant platform's stated roadmap for the next 12 months?** Read their public
   statements, recent investor / dev day talks, and analyst coverage.
4. **Is there an open standard / protocol** (MCP, OpenAPI, A2A, etc.) that changes the
   build-vs-buy calculus? If so, building on the protocol is often safer than building a silo.
5. **If the dominant platform launches this as a native feature tomorrow, what survives?** This
   is the survivability test — name what's left.

**Searches to run (mandatory):**

For each plausibly relevant platform, run searches like:
- `"[platform name]" plugin marketplace [year]`
- `"[platform name]" launch [adjacent feature]`
- `"[platform name]" roadmap [year]`
- `[platform name] vs [your category]`
- Check the platform's GitHub org, official plugin/skill directory, and recent announcements

**Common platforms to check by default for any AI/software product:**

- Claude (Anthropic) — Cowork, Code, plugin marketplace, Managed Agents
- ChatGPT / OpenAI — Custom GPTs, Actions, Operator, Agent Builder
- Cursor / Windsurf / Continue — IDE extensions
- Microsoft — Copilot, Copilot Studio, Office add-ins
- Google — Gemini, Workspace add-ons, Apps Script
- Notion / Slack / Linear / Asana — app marketplaces
- Apple — Shortcuts, App Intents
- Vercel / Cloudflare — platform-native features

**Output for this investigation:**

Produce a Platform Replication Risk Table:

```
| Platform     | Already shipped? | On roadmap? | Replication risk |
| ------------ | ---------------- | ----------- | ---------------- |
| Claude       | [details]        | [details]   | High/Med/Low     |
| ChatGPT      | [details]        | [details]   | High/Med/Low     |
| ...          | ...              | ...         | ...              |
```

Plus a one-paragraph survivability statement: "If [platform] launches this natively tomorrow,
this product still wins because [specific moat]."

If no compelling survivability statement exists → **strongly consider pivoting** to one of:
- Build as a plugin/skill on the dominant platform (accept lower margins, gain distribution)
- Build on an open protocol (e.g., MCP server) for cross-platform reach
- Pick a sharper vertical/niche the platform won't bother with
- Pivot the wedge entirely

**Decision rule**: If replication risk is HIGH on any platform that owns >30% of the target user
base, this should become an explicit kill criterion in the PRD.

### 7. Future Trajectory & Time Horizon (3–24 months) ⏱️ CRITICAL

**This investigation was added in v0.2 alongside Platform Replication. Static snapshots of
"today's market" miss the most important signal — where the world is heading. An idea that
looks great in today's snapshot can be obsolete in 18 months.**

**The mental model**: research isn't an answer to "is this market real today?" — it's an answer
to "will this market still want this in 18-24 months, given how the world is moving?"

**Mandatory questions:**

1. **Tech maturity trajectory** — Is the underlying technology getting dramatically cheaper,
   faster, or more capable in the next 18 months? (LLM cost has dropped 95% in 3 years; what
   does that mean for your unit economics — and your competitors'?)
2. **Standards/protocol momentum** — Is an open protocol (MCP, OpenAPI, A2A, OpenID, etc.) being
   adopted that changes the build calculus? Adoption velocity matters — MCP went from 2M to 97M
   monthly downloads in 16 months. This level of momentum changes everything.
3. **Funding & M&A signals** — Where is VC money flowing in this category in the last 12 months?
   What recent acquisitions suggest about where incumbents see threats/opportunities?
4. **Adjacent disruption** — What emerging tech could obsolete this in 18-24 months? (Quantum,
   ambient computing, AR/VR, on-device LLMs, brain interfaces — each has its own timeline.)
5. **Regulatory & policy horizon** — What rules are being drafted that could enable or kill this?
   (EU AI Act, US AI executive orders, GDPR-equivalent in new markets, content provenance laws.)
6. **Demographic / cultural shifts** — Generational changes in who has the pain, who has spending
   power, who hangs out where. (Boomers retiring, Gen Z entering workforce, AI-native generation.)
7. **Best / middle / worst case scenarios at 18 months** — Write three short scenarios. If the
   worst case is "this product is obsolete," you have a structural problem.

**Searches to run:**

- `"[category]" funding rounds [current year] venture capital`
- `"[category]" Gartner OR Forrester OR Bain OR Deloitte [current year] prediction`
- `"[category]" roadmap OR future [current year + 1] [current year + 2]`
- `"[adjacent tech]" timeline maturity [category] disruption`
- `"a16z" OR "Bessemer" OR "Sequoia" "state of [category]" [current year]`
- `[regulatory body] [category] regulation draft [current year] [current year + 1]`
- Check job postings for "Head of [emerging role]" — leading indicator of what big companies bet on

**Output: Future Trajectory Table**

```
| Force                        | Direction (18mo)        | Effect on idea       |
| ---------------------------- | ----------------------- | -------------------- |
| LLM cost                     | ↓ 50% expected          | ✅ better margins     |
| MCP adoption                 | ↑ becoming default      | ⚠️ build on protocol  |
| [Adjacent tech]              | ↑ rising / ↓ fading     | ✅ ⚠️ ❌                |
| [Regulation]                 | [draft / passing / ?]   | ✅ ⚠️ ❌                |
| [Demographic shift]          | [direction]             | ✅ ⚠️ ❌                |
```

**Plus three scenario statements:**
- **Best case (18mo)**: [what success looks like with tailwinds]
- **Middle case (18mo)**: [most likely state of the world]
- **Worst case (18mo)**: [biggest threat materializes]

**Decision rule**: If the worst case includes "the underlying problem disappears" or "the
technology that makes this worth paying for becomes free as a default feature," this is a
structural issue — fold it into kill criteria as a time-bound condition (e.g., "abandon if
[trigger] happens before [date]").

**Common time-horizon mistakes to flag:**

- Assuming today's LLM costs / context limits are permanent
- Assuming today's competitive landscape is stable (it isn't — every 6 months in AI is a generation)
- Assuming users will care about the same things 2 years from now
- Building for a regulatory environment that's about to change
- Missing a protocol/standard that's about to make your custom solution irrelevant

### 8. Risks & Assumptions

Synthesize from the above:
- **Market risks** — Is the market too small? Too crowded? Wrong direction?
- **Execution risks** — Required skills missing? Timeline unrealistic? Dependencies fragile?
- **User risks** — Will users actually adopt? Is the problem painful enough?
- **Business model risks** — Can it sustain itself? Will users pay?
- **Platform risks** — Carry over from investigation #6; surface as explicit kill criteria.
- **Time horizon risks** — Carry over from investigation #7; include time-bound kill criteria.
- **Regulatory / structural risks** — Compliance, platform dependency, etc.

## Connected Capabilities — Use Them If Present

Before relying solely on web search, check what's connected:

- **Enterprise or workplace search** — search across user's connected sources for prior internal work,
  customer feedback, related discussions. Use this if the idea touches their company or industry.
- **Slack, Notion, Confluence, Drive** connectors — same as above.
- **Common Room, Apollo** — for ICP-style validation when the idea targets a specific market segment.
- **Connector/plugin registry** — if the idea names a specific platform, check whether the host can
  discover connectors that would surface relevant data.

If you discover relevant connectors that aren't installed, surface them to the user — don't try
to work around them silently.

## Output Format

Produce the **research brief** as specified in SKILL.md Phase 2. Cite sources inline using
markdown links. Group findings by the eight investigation areas. Pause for user reaction before
moving to synthesis.

## What Counts as Insufficient Research

- Fewer than 3 named competitors when competitors exist
- Pricing claims without a specific source
- "There's high demand" without a quantified data point
- "It's feasible" without naming specific technologies/tools
- **No platform replication risk assessment** (investigation #6 missing or shallow)
- **No survivability statement** for the dominant platform's likely native launch
- No risks identified

If you hit any of these, do another round of searches before proceeding.
