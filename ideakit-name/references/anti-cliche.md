# Anti-cliché — escaping the AI naming centroid

The single biggest weakness of AI-generated names: a language model predicts the *most likely* next
token, so it gravitates to the **centroid** — the average startup name that every other AI tool also
produces. The result *feels* like a brand but is generic, forgettable, and instantly "AI." This file
exists to push generation off the centroid, toward names a thoughtful human namer would land on.

## Contents

- Why it happens
- The banned tells
- Stay globally legible
- Techniques that produce distinctive, human names
- Linguistic check
- Wire it into the workflow

## Why it happens (and the one mental move that fixes it)

The first 10–15 names a model produces for any brief are the centroid: the obvious, safe, average ones.
**They are the warm-up, not the answer — discard them on principle.** The good names live *after* you've
exhausted the obvious. The core move: **generate the obvious batch, throw it away, then deliberately
generate names that are unexpected for the category.** Distinctiveness comes from *tension* (a name
slightly "wrong" for the space — "Slack" for work software, "Stripe" for payments, "Nest" for
thermostats), not from describing the product more cleverly.

## The banned tells (auto-reject — these read as AI/generic)

If a candidate has any of these, cut it unless there's a genuinely strong reason:

- **Slop suffixes:** `-ly`, `-ify`, `-io`, `-er`, `-it`, `-able`, `-hub`, `-base`, `-flow`, `-stack`,
  `-labs`, `-ai`, `-ware`, `-sense`, `-genix`/`-genics`. (Most-overused suffixes are `-er`, `-ly`, `-it`
  — [naming trends](https://www.buycompanyname.com/startup-naming-trends/).)
- **Overused abstract/"epic" words:** Nexus, Vertex, Apex, Zenith, Quantum, Lumen, Aether, Nova, Helix,
  Catalyst, Synergy, Paradigm, Momentum, Pulse, Spark, Ignite, Forge, Beacon, Summit, Pinnacle, Elevate,
  Ascend, Flux, Prism, Echo, Halo, Orbit, Vortex.
- **Greek/Roman gods on autopilot:** Atlas, Apollo, Athena, Hermes, Mercury, Titan, Hydra, Zeus (used so
  often they're now the cliché — mythology is fine only if unobvious and tied to a real story).
- **Buzzword mash-ups:** Cloud+X, Smart+X, Data+X, Ultra/Hyper/Meta+X (Cloudbot, SmartTask, DataFlow,
  Ultranet) — [the classic generic move](https://medium.com/@jowitaemberton/how-to-name-your-startup-56a64171e38).
- **Random animal/color/element + tech noun:** Firebot, Cloudbadger, Yellowbook, RedOwl, FoxStack.
- **Prefix/affix gimmicks:** `Get[X]`, `Try[X]`, `[X]HQ`, `[X]App`, `[X]AI`, `i[X]`, `e[X]`.
- **ccTLD-as-the-name gimmick:** bending `.ly`/`.io`/`.ai` to spell the name (Parse.ly-style) — dated.
- **Dropped-vowel respellings:** Flickr/Mndfl-style — now reads as ~2010s, not fresh.

> A fast smell test: *"Would 50 other AI name generators also output this for this brief?"* If yes, it's
> the centroid — cut it.

## Stay globally legible (read this before the techniques)

Escaping cliché must **not** swing the other way into obscure, hard, "thesaurus" English. The audience is
global, and most users are second-language English speakers. So bias hard toward names that a
non-native speaker can **read, say, and spell after hearing once**:

- Favor **simple, common, concrete** words and easy syllables over rare/archaic/literary vocabulary.
- Avoid silent letters, tricky consonant clusters, and spellings whose pronunciation is ambiguous.
- "Distinctive" comes from *unexpected use of a simple word* (Stripe, Slack, Nest, Square), **not** from
  a harder word. Simple-but-surprising beats clever-but-obscure every time.

This overrides everything below: if a candidate is distinctive but hard to read/say globally, cut it.

## Techniques that produce distinctive, human names

Use these deliberately *after* discarding the obvious batch (and always inside the global-legibility
rule above):

1. **Empty-vessel / arbitrary real word** — a real, concrete word whose literal meaning doesn't describe
   the product but carries the right *feeling*, used as an unexpected metaphor (Stripe, Slack, Nest,
   Square, Patch, Oxide, Plaid, Monzo, Orange, Virgin). Pick concrete, sensory, picture-able words over
   abstract ones. ([the dominant modern pattern](https://www.entrepreneur.com/starting-a-business/making-things-up-why-fake-words-may-be-right-for-your-new/345925))
2. **Random-word trigger** — pick a word with *nothing* to do with the category, then mine its
   associations/metaphors/sounds. This is the standard trick for breaking out of the obvious set
   ([random-word technique](https://www.selfstorming.com/tools/libraries/naming-techniques/inventive-names)).
3. **Tension / category-wrongness** — deliberately choose a word that feels slightly off for the space;
   the friction is what makes it memorable.
4. **Borrow from another language** — a simple, evocative word from another language whose meaning fits
   the brand. Done well it's memorable, concise, and crosses markets: **Volvo** (Latin *volvere*, "to
   roll"), **Audi** (Latin *audi*, "listen" — a translation of founder Horch's name). Prefer words that
   are *short and easy for anyone to pronounce*, not just meaningful. **Always then run the linguistic
   check** (next section): a borrowed word can mean something odd or offensive in another major
   language. Latin/Romance/short Japanese-style sounds travel well; obscure or hard-to-say borrowings
   don't.
5. **Unexpected sources** — a place, an object, a person, or jargon from an *unrelated* field. (Archaic
   English and on-the-nose mythology mostly fight global legibility — use only if the word is still
   genuinely easy to say.)
6. **Sound symbolism / coinage with roots** — invent a word using phonetics that *feel* like the brand
   (plosives feel sharp/fast; soft sounds feel calm), or fuse meaningful roots — but avoid the
   slop-suffix coinages above, and keep it easy to say.
7. **Concrete over abstract, short over long, sayable over clever** — favor words you can picture, spell
   after hearing once, and say out loud without thinking.

## Linguistic check (cross-language) — part of the gauntlet

Professional naming includes **linguistic screening**: confirming a name is pronounceable and carries no
unintended/offensive meaning across the major languages and markets it will live in. Famous launches have
been derailed by a name that meant something embarrassing in another language. So for every shortlisted
name, check (a web search per major target language usually suffices for a solo):

- **Pronounceable** for non-native speakers in the target markets? (no tricky clusters/silent letters)
- **No bad/odd meaning** in major languages (English, Spanish, French, German, Mandarin/pinyin, Japanese
  romaji, Hindi, Arabic transliteration — weight toward the actual target markets).
- **Cultural fit** — no unfortunate associations in the regions you'll sell to.

This is *screening*, not a full professional linguistic audit — flag it, and recommend a proper check
before a global launch. (Grounding rule still applies: don't claim a name is "clean in all languages"
unless you actually checked; mark unchecked languages as not verified.)

## Wire it into the workflow

In Step 2 (Generate): produce a quick obvious batch, **explicitly discard it as the centroid**, then
generate the real set using techniques 1–6, banning every tell above. In Step 3 (SMILE/SCRATCH): treat
any surviving centroid name as an automatic **SCRATCH** ("Tame"/"Copycat") and cut it. The goal is a
shortlist where each name would make a sharp human namer nod — not one a generator spat out.

Note the trade-off (it's real): distinctive *real-word* names (Mirror, Wardrobe) collide and get
trademarked far more often — which is exactly why this skill pairs distinctiveness with the availability
gauntlet. Coined/empty-vessel/tension names tend to be *both* more distinctive *and* more clearable.
