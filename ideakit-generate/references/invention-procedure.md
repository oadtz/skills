# The invention procedure (single path)

This is the only generation procedure. It exists to produce ideas that are surprising, defensible,
and enterable — not a celebrity persona and not a license for random weirdness.

## 1. Freeze a neutral invention packet

Give every invention lane the same compact packet: the actor/domain or force brief and the desired
decision; Observed signals, causal openings, counter-signals, and uncertainty; founder-specific
access, credibility, lived evidence, and no-go work.

Withhold candidate products, the previous portfolio, obvious categories, and other lanes' output.
Keep the packet's wording **neutral**: a causal opening states what changed and what it costs, not
which mechanism should exploit it — interpretive framing in the packet is the main cause of every
lane returning the same seed. Include source URLs with the signals so lanes inherit evidence quality,
not just claims. Record founder time, cash, and support capacity separately for the later solo
translation; do not let feasibility filters collapse divergent search before a mechanism exists.

The packet is a **shared floor, not the whole evidence base** — see the retrieval mandate in step 2.
Isolating contexts while feeding them one identical evidence set produces correlated output no matter
how well the contexts are separated, because the lanes are reasoning over the same facts.

**Carry forward what this user has already been shown.** If idea memory or a prior portfolio exists
for this person, list the venture families already proposed to them as an **exclusion set** in the
packet — named as neighborhoods to avoid, never as examples to riff on. Individually sound runs
converge across sessions when nothing remembers the last one; the exclusion set is what stops the
same user receiving the same neighborhood under new wording.

## 2. Run independent invention lanes

**With subagents / fresh contexts:** run 3–5 lanes in parallel. A lane sees only the neutral packet
and its operator, returns terse anonymous seeds — not polished pitches. No lane is entitled to a
finalist.

**No-subagent fallback (mandatory when isolation is unavailable):** run 2–3 lanes *sequentially* as
strictly separated scratch passes. Before each lane, restate only the neutral packet and that lane's
operator; do not look back at, revise, or reuse the previous lane's seeds until synthesis. Write each
lane's seeds immediately and move on. Fewer, honestly isolated lanes beat five contaminated ones —
never skip isolation and brainstorm once in an open context.

**Give each lane its own retrieval mandate.** Before it invents, a lane spends a small, bounded
search budget on questions its *operator* asks — under the same evidence discipline as the main scan,
and reported with the seeds so the evidence is auditable. A deletion lane asks what an input costs
today and who supplies it; an expired-premise lane asks what incumbents publicly still assume; an
analogy lane searches the remote domain it is transferring from, not the brief's domain at all. What
each lane brings back stays inside that lane until synthesis.

This is the intervention that separates lanes in *knowledge* rather than only in prompt. Planned,
iterative retrieval interleaved with generation produced several times more distinct usable ideas
than single-shot generation over a fixed corpus in the published comparison (arXiv:2410.14255;
measured on research ideation, so treat the size of the effect as indicative, not transferred). When
no live research is available, say so and expect narrower divergence — do not pretend a shared frozen
pack delivers the same spread.

Lane operators (pick for the brief):

- **Bedrock / deletion / new bottleneck** — decompose the outcome into physical or economic inputs;
  ask what stays expensive when the headline capability gets 10× cheaper, which inherited step can
  disappear, and where value pools next.
- **Expired premise** — find a premise customers or incumbents still optimize around although the
  world changed; trace second-order behavior, shifted budgets, and the rational incentive that keeps
  incumbents from serving the opening.
- **Structured distant analogy** — represent the opening abstractly (actors, constraint, trigger,
  feedback loop); transfer a causal mechanism, ownership rule, or value-capture pattern from a remote
  domain with the same structure. Reject surface metaphors.
- **Non-consumption / desire / inversion** — start with actors excluded by cost, trust, expertise, or
  workflow, or with identity, status, ritual, and belonging; invert who uses, pays, owns, approves.
- **Organizational compression** (software scope) — run the lane in
  `ai-engineering-team.md`.

Within each lane, use the two interventions that are measured to work — and skip the ones that are
measured not to:

- **Sample ordinary people, not geniuses.** Before generating, draw 3-5 *specific ordinary people*
  from the brief's world — "a 24-year-old admin of a 3,000-member fanbase", "the owner of a
  40-person extrusion shop in Samut Prakan" — and generate from each. Controlled comparison finds
  everyday-persona sampling closes the human-LLM idea-diversity gap while "act as a visionary
  founder" personas barely move it and can degrade factual accuracy
  (arXiv:2602.20408; Wharton GAIL, *Playing Pretend*).
- **Differentiate explicitly, in two passes.** Write short seed *titles* first, then revise the list
  specifically to make each maximally unlike the others, and only then expand the survivors. Chain-
  of-thought differentiation reduces fixation; raising temperature does not (temperature 2.0 tested
  and rejected as garbled).
- **Do not "generate more" as the fix.** In the largest published run, 4,000 seed ideas per topic
  yielded roughly 200 non-duplicates and the duplicate rate rose with volume (arXiv:2409.04109).
  Breadth comes from distinct sampling anchors, not sample count.

Write each seed as `actor | trigger/job | causal thesis | scarce asset | mechanism | proof/feedback
loop | payer | architecture`; replace any pair sharing actor + job + thesis + mechanism; expand only
the strongest one or two into a falsifiable thesis, wedge, value capture, and why-now.

## 3. Synthesize without averaging

Collect lane outputs only after divergence ends. Canonicalize, cluster duplicates, keep the strongest
representative; recombine two candidates only when their mechanisms reinforce each other — never a
feature bundle or compromise concept.

If lanes converged on the same seeds, suspect the inputs before celebrating signal gravity, in this
order: (1) did the lanes actually retrieve different material, or did they all reason over the frozen
pack alone? (2) is there packet-steering — interpretive framing in the packet pushing them to one
seed? Fix whichever holds and rerun one lane. Convergence between lanes that read the same facts is
arithmetic, not evidence.

Assign a **venture-family ID** before selection: if one company would serve the candidates as modules
using the same buyer relationship, input corpus, operating workflow, and compounding asset, they are
one family even when trigger or pitch differs. Matching any three of the four fields means one
family; a new name, trigger, or asserted thesis cannot override it. Keep at most one finalist per
family.

## 4. Evaluator-only collision pass

Use a fresh evaluator context when possible; in the no-subagent fallback, run this as its own
separated pass after writing the candidates down, and generate the **obvious baseline** only now —
the inventor must never see it beforehand. When a third context is available, have it canonicalize
the candidates so the orchestrator's summarization cannot leak emphasis.

Run **two different comparisons**. Confusing them is the single most damaging error this procedure
can make, and it silently destroys good candidates.

**A. Against the other candidates and the obvious baseline — deduplicate.** Compare canonical
signatures: actor, trigger/job, causal thesis, scarce asset, mechanism, payer, architecture. A
different actor, payer, vertical, or channel is insufficient when the causal thesis and core
mechanism are the same. Merge or drop duplicates; keep one representative per venture family.

**B. Against the outside world — this is NOT a kill pass.** Search current offerings, failed
attempts, and adjacent prior art by mechanism as well as category. Then apply the correct rule:

> **An existing operator is demand evidence, not a wall.** It is the cheapest proof money can buy
> that someone pays for this outcome. An empty landscape is the *worse* signal — it usually means
> you will pay to prove demand yourself, and for a solo founder with no audience that is the most
> expensive thing you can buy.

So do not ask "does this exist?" Ask, and answer with evidence:

1. **Who does the incumbent structurally fail to serve** — which segment, at which price tier, in
   which language, geography, channel, or moment?
2. **Why can they not fix it** without cannibalising their own revenue, breaking their channel,
   taking on liability, or contradicting their cost floor? Name the mechanism. "They are slow" is
   not an answer.
3. **Can we take those customers**, and on which single dimension are we 10× better?
4. **What did the failures actually die of?** A dead company usually proves a *business shape* was
   wrong (burn rate, CAC, licensing), not that the demand was absent. Say which.

Kill a candidate here only when the answer to (1) or (3) is genuinely nothing — not merely because a
name came back in a search. Also kill it when the incumbent is free (see the substitute test in
`substitutes-and-incumbents.md`) and the added value cannot clear that price.

A clean search reveals no collision; it never proves global novelty — and it never proves an
opportunity either.

## 5. Compare in pairs, then evolve the survivors

Everything before this point generates once and then selects. That is the largest structural gap a
one-shot procedure has: the best candidate available is rarely the best candidate reachable. This
step is a short improvement loop, taken from the multi-agent discovery system whose generate–debate–
evolve architecture was validated in peer review, where ranking quality rose as more compute went
into the loop rather than into the first generation
([Co-Scientist, Nature 2026](https://www.nature.com/articles/s41586-026-10644-y)).

**Compare in pairs, never score candidates alone.** Put two survivors side by side and ask one named
question at a time, then record which won and *why in one line*. Pairwise comparison is more stable
than assigning each candidate a score, for the same reason it is the standard in judge evaluation:
an isolated score drifts, a direct comparison has to name a reason.

Ask the comparison on **checkable ground only** — whose substitute is harder to beat, whose incumbent
argument is better evidenced, whose wedge needs fewer independent parties to say yes, whose causal
chain has fewer unsupported links. Never run the loop on "which is more exciting": that is the metric
that inverted after execution in the one study that measured both, and an optimization loop pointed
at it will reliably produce a more exciting and less real portfolio. The forecasting judgment stays
with the user (`scoring.md`); this loop only sharpens what is already checkable.

Keep it bounded. Compare each survivor against two or three others, not a full round robin — the aim
is to expose each candidate's specific weakness, not to produce a precise ranking. A ranking produced
here is the model's, and it is an input to the user's decision, never a substitute for it.

**Then evolve.** For each candidate that lost on a specific point, produce one improved version using
a named move, and say which move was used:

- **repair** — fix the exact weakness the comparison exposed, changing nothing else;
- **graft** — take the specific mechanism that beat it and rebuild around that, keeping the thesis;
- **shrink** — cut to the smallest version that still carries the causal thesis intact;
- **raise** — push to the version that would matter if the bet is right, to see what the cautious
  version was giving away.

Re-enter each evolved version against the version it came from. **An evolved candidate that does not
beat its parent is discarded and the parent is carried forward** — otherwise the loop drifts toward
whatever is easiest to argue for. Do not evolve a candidate that failed the substitute test; a free
and tolerable substitute is not a weakness that revision fixes.

**Meta-review before the next round.** Write down the *recurring* critique patterns — not the
individual verdicts — and carry them into the next round as things to avoid. This is the only point
in the procedure where a criticism improves later output instead of merely killing one candidate. If
the same critique appears against most candidates, it is usually a fault in the packet or the
openings, not in the candidates; go back rather than evolving around it.

**Stop after one or two rounds**, or earlier when no evolved version beats its parent. More rounds
raise quality against the comparison question, which is exactly why they also raise the risk of
optimizing for what the judge likes. Record how many rounds ran, so a portfolio produced in one pass
is not mistaken for one that survived several.

In the no-subagent fallback, run the comparisons as their own separated pass with only the two
candidates and the question in view, and write the verdict down before looking at the next pair.

## 6. Translate to a solo-founder entry

Reintroduce the operating envelope only now. For each survivor: smallest paid proof and exact first
buying occasion; how the founder reaches the first 10 without a hypothetical audience; cash, hours,
support, liability, trust, and dependency burden; every independent commitment required before value
can be demonstrated (pre-commit essential non-paying parties too); capacity economics with explicit
room for selling, administration, learning, and delivery variance — all founder hours are not
billable. `Paid commitment` before work and `Delivered value` after delivery are separate
checkpoints; both must pass.

Do not shrink the long-term thesis to make it buildable — separate the large architecture from the
founder-scale entry; park a concept with no credible translation. For software scope, the envelope is
a founder attention and control budget per `ai-engineering-team.md`; do not force a manual service
when the larger system is directable, verifiable, operable, and containable.

## 7. Finish line — pursuable wow

Judge separately, never totaled: **Surprise** (escapes the obvious category through thesis or
mechanism), **Inevitable in hindsight** (the causal chain makes the reveal click), **Enterable**
(a bounded first move earns the right to learn), **Value capture** (named payer, buying occasion,
viable capacity economics or leverage path). A finalist cannot compensate for failing one with
strength on another. All four are forecasts, so they are the user's to rank — see the split in
`scoring.md`. Express each finalist's core through the labeled lines in the SKILL's Step 6. Return
fewer finalists rather than admitting a near-duplicate or broken solo economics.

## Anti-patterns

- impersonating a famous founder, or treating biography as a method;
- exposing the obvious baseline before invention, or letting lanes see each other;
- running every lane over one identical evidence set and reading the convergence as signal gravity;
- interpretive framing inside the "neutral" packet steering every lane to one seed;
- pruning divergence with founder time/budget instead of translating the survivor;
- unverified global novelty claims (“first”, “only”, “nobody”) to manufacture surprise;
- presenting “Why others miss it” as observed universal behavior rather than labeled inference;
- running the improvement loop on appeal ("which is more exciting") instead of checkable ground;
- keeping an evolved version that never beat the version it came from;
- evolving around a free and tolerable substitute instead of accepting that it kills the concept;
- reporting a model-produced ranking from the comparison round as the portfolio's verdict;
- one venture family kept as several finalists because it has several buying occasions;
- a low pilot price treated as enterability when sustainable capacity economics do not work;
- a familiar category called novel because its feature list or vertical changed.
