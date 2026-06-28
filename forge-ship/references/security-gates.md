# Security & quality gates — blocking and external

This is the governing principle applied to quality: **the gates must be blocking and external**,
because the human is overconfident and the agent grades itself generously. Use in Steps 1–2 of
forge-ship.

## The evidence you're gating against

- ~**45% of AI-generated code** contains an OWASP Top 10 vulnerability, and **newer/bigger models are
  not safer** — it's structural, not "the next model fixes it." (Veracode 2025.)
- Developers using an AI assistant wrote **less secure code and believed it was more secure** (Stanford,
  ACM CCS 2023). ~80% trust AI security; ~10% actually scan AI code (Snyk).
- AI raises duplication, churn, and instability unless work is chunked small (GitClear; DORA).

The throughline: you cannot close this with discretion. An overconfident reviewer won't *choose* to
check. So the checks run automatically and block merge.

Sources: https://www.veracode.com/blog/genai-code-security-report/ , https://arxiv.org/abs/2211.03622 ,
https://snyk.io/articles/the-highs-and-lows-of-vibe-coding/ ,
https://www.gitclear.com/ai_assistant_code_quality_2025_research ,
https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report

## Step 1 — CI quality gates (make them blocking)

- **On every PR:** `lint → type-check → test → build`. **On merge:** deploy.
- **Branch protection on main** — the single most important control for AI-built code. Every change
  (including every agent change) goes through review + passing checks. No direct pushes.
- **Preview/PR deployments** (free on Vercel/Netlify/Cloudflare) so reviewers check *behavior*, not
  just the diff.
- **CI hardening:** pin actions to a commit SHA, use OIDC over long-lived credentials, set
  least-privilege `permissions:`.

Source: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule

## Definition of Done (counteracts AI's biases)

A change is done only when:
- tests pass in CI; lint + type-check clean;
- **no new duplicated blocks** (AI skews toward copy-paste);
- the change is **small enough to review in one sitting** (chunk AI work into multiple reviewable PRs —
  small batches are what separate teams where AI helps delivery from teams where it hurts stability);
- behavior verified on a preview deploy;
- errors/logging instrumented;
- **a human reviewed the diff** (and, for test changes, reviewed the test diff — not just that it's
  green).

## Step 2 — Security & dependency gates

Three complementary tiers (all have free/low-cost options):

1. **Secret scanning.** Pre-commit (e.g. Gitleaks) + repo push protection. Confirm `.env` is
   git-ignored, no secrets in code or MCP config files (a known leak source), secrets in a
   per-environment store. AI-assisted commits leak secrets at ~2× the baseline rate.
2. **SAST.** A fast scanner on every PR (e.g. Semgrep, ~seconds, org-specific rules) + a deep dataflow
   scan scheduled / pre-release (e.g. CodeQL). LinkedIn's published pattern: Semgrep per-PR + CodeQL
   scheduled.
3. **Dependency integrity (slopsquatting gate)** ⚠️ — the signature new AI supply-chain risk. Across
   ~2.2M samples, **~19.7% of AI-recommended packages did not exist**, and **43% of the hallucinated
   names recurred on every re-run** — predictable enough for attackers to pre-register as malware. A
   hallucinated `huggingface-cli` package was downloaded 35,000+ times. Gate:
   - **never auto-install AI-suggested packages**; verify each *exists* + check publisher and
     registration date before adding;
   - enforce **lockfiles + hash pinning** (`npm ci` with `package-lock.json`; `pip --require-hashes`);
   - allowlist new deps / use a private registry with a first-seen policy;
   - enable automated updates (Dependabot) + SCA (Snyk/Socket).

Sources: https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen ,
https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks ,
https://konvu.com/compare/semgrep-vs-codeql

## The security review gate

Run an available security/code review capability (for example `security-review`, if installed) on any
change touching auth, data access, input handling, or external calls — don't hand-roll a checklist. Map
findings against:

- **OWASP Top 10:2021 + OWASP ASVS Level 1** as the MVP floor. The honest minimum is "L1 auth + access
  control + input validation" (add L2 controls if handling personal data) — not 100% of L1.
- **Input validation / output encoding first** — the single most-omitted control *and* the
  highest-frequency AI failure, so the highest-leverage fix.
- **Broken access control** (Top 10 #1) — explicitly confirm authorization is enforced. For apps with a
  client-embedded DB key (Supabase/Firebase-style), **confirm row-level security is actually on**:
  ~88% of audited vibe-coded apps had it disabled, and that's exactly the class behind real CVEs.

Note: security-review tooling may not be hardened against prompt injection — only run it on **trusted**
PRs.

Sources: https://owasp.org/Top10/2021/ , https://github.com/OWASP/ASVS ,
https://github.com/anthropics/claude-code-security-review ,
https://securityboulevard.com/2025/10/methodology-how-we-discovered-over-2k-high-impact-vulnerabilities-in-apps-built-with-vibe-coding-platforms/

## The MVP security minimum (concrete)

1. Gitleaks pre-commit + push protection (secrets).
2. Semgrep per-PR + CodeQL scheduled (SAST).
3. Dependabot + lockfiles/hash-pinning (deps & slopsquatting).
4. Security/code review capability + behavior verification on PRs touching sensitive code, mapped to
   OWASP Top 10 + ASVS L1.

All blocking. All run by the pipeline, not at the reviewer's discretion.
