# Hardware Research Pipeline — Operational Instructions

## Mission
Maintain a continuously-updated, peer-reviewed-grade research dataset on the AI / semiconductor hardware stack. The pipeline re-executes every 5 hours, discovers new material, and refreshes the cross-sector synthesis. An independent verification agent confirms that findings flagged "not priced into the market" are still genuinely non-consensus.

## Repository
- **Local**: `/home/cybernovas/Desktop/2026/experiments/hardware`
- **Remote**: `https://github.com/harrrshall/hardwareresearch`
- **Live site**: `https://harrrshall.github.io/hardwareresearch/` (GitHub Pages, mobile-first viewer)
- **Master spec**: `hardware_research_orchestration.md` (sector pipeline + global synthesis spec)
- **Research outputs**: `research/`
- **Run tracker**: `research/run_history.md`

## Website (auto-updates)
A static single-page viewer lives at `index.html` in the repo root, served via GitHub Pages from the `main` branch. It loads markdown files at runtime (`fetch` + `marked.js`), so **no rebuild step is required** — every `git push` to `main` automatically updates the live site within ~30–60 seconds.

The recurring 5-hour cycle agent must:
- NEVER delete `index.html` or `.nojekyll`
- After each cycle's final commit + push, the site refreshes automatically. Nothing extra to do.
- If new top-level markdown files are added at the research root, optionally add nav entries to `index.html` (otherwise they're still accessible by direct URL).
- If `gh-pages` or `index.html` build issues appear, the agent should report this in `run_history.md` for the run — do not silently fail.

---

## Recurring Cycle — every 5 hours (cron `0 */5 * * *`)

Each cycle runs the FULL pipeline end-to-end. Every step is idempotent against the prior cycle's state.

### Step 0 — Read state
- Read `research/run_history.md`. The next run number is `(latest entry's N) + 1`.
- Read each sector's existing `sources.json` to know what's already been seen.

### Step 1 — Identify NEW papers per sector
For each of the 10 sectors, re-run the Collector looking for papers, disclosures, or news that did NOT appear in the prior run's `sources.json`. Use spec §11 keyword seeds + citation graph expansion. APPEND new entries to `sources.json` (never remove existing ones).

### Step 2 — Analyze NEW papers only
For each newly added source, write `papers/paper-NNN.md` (continue numbering from existing files). Skip already-analyzed sources.

### Step 3 — Re-validate NEW papers only
Apply the six validation criteria from spec §5 to NEW papers. Append decisions to `validation_log.md`. Existing decisions stand.

### Step 4 — Update sector `research.md` only if changed
If a sector has new VALIDATED findings, refresh that sector's `research.md` to reflect the full corpus. If no new findings, leave it untouched.

### Step 5 — FULLY REWRITE these 3 global files every cycle (NOT incremental)
- `research/cross_sector_alpha.md` — fresh 45-cell pairwise matrix, fresh ranked deep dives. The file's intro must state which finds are unchanged-from-previous vs new this run.
- `research/future_trends.md` — full rewrite, fresh signals/falsifiers.
- `research/market_opportunities.md` — full rewrite.

Even if findings repeat verbatim, REWRITE. This is mandatory.

### Step 6 — `conclusion.md` is ADDITIVE
If a new conclusion is found that doesn't appear in a sector's main file, append it to `conclusion.md` with the marker: `**[Run #N — new conclusion]**: …`. Do not silently merge new conclusions into existing text. Past conclusions remain.

### Step 7 — Independent Verification Agent (MANDATORY every run)
After the synthesis is written, spawn a SEPARATE agent — the **Market Pricing Verification Agent**. Its only job:

1. Read `cross_sector_alpha.md` and `market_opportunities.md` (this run's versions).
2. For each "not priced in" / "non-consensus" finding, perform fresh web searches (analyst notes, vendor guidance, financial press, equity research summaries, Seeking Alpha, SemiAnalysis, Bloomberg, etc.) as of the current execution date.
3. Independently verify whether market consensus has shifted. A finding is REALLY not priced in only if no major analyst, vendor, or financial outlet currently reflects it.
4. Write `research/verification_log.md`. For each finding from the synthesis files:
   - Verdict: `VERIFIED-NOT-PRICED-IN` / `PARTIALLY-PRICED-IN` / `ALREADY-PRICED-IN`
   - Evidence: at least one URL + dated quote
   - Note any consensus shift since prior cycles
5. Be skeptical. If a Seeking Alpha article or Goldman note already says what the synthesis calls "non-consensus", downgrade the claim immediately.

The verification agent runs AFTER the synthesis writer, in the SAME cycle, but in a SEPARATE agent context so it cannot anchor on the synthesis author's prior reasoning.

### Step 7.5 — POST-VERIFICATION PURGE (mandatory, CLEAN DELETION ONLY)
After the Verification Agent writes its verdicts, scrub all `ALREADY-PRICED-IN` items out of these files so they contain signal only:

1. **`research/cross_sector_alpha.md`** — DELETE any ranked deep-dive section whose verification verdict is `ALREADY-PRICED-IN`. For matrix cells, do NOT leave a "Priced — see verification_log" note; normalize the verdict cell to a plain `Yes` so the row reads like any other already-priced pair. DELETE any triple-combination row whose chain was downgraded.
2. **`research/market_opportunities.md`** — DELETE any opportunity entry whose verification verdict is `ALREADY-PRICED-IN`. RENUMBER the surviving entries (both section headers and summary table) so the document reads sequentially with no gaps.
3. **`research/opportunity.md`** — already signal-only by design (Step 7.6 below regenerates it).

**CRITICAL — no marks, no breadcrumbs, no strikethrough.** Do NOT leave behind:
- Strikethrough headers like `~~Finding 4~~ — REMOVED`
- Breadcrumb quotes like *"removed post-verification: ALREADY-PRICED-IN as of YYYY-MM-DD"*
- Verdict cells like `Priced — see verification_log.md Claim N`
- Inline notes like `⚠️ PARTIALLY-PRICED-IN` or `✅ VERIFIED-NOT-PRICED-IN` in the synthesis files
- Explanatory paragraphs about what was removed

These create confusion when reading the document. The synthesis files must read cleanly, as if the removed items never existed in this version. The complete audit trail — what was removed, why, with dated URLs — lives in `research/verification_log.md`. That file alone is the canonical record. Readers who want the history go there.

Why: the synthesis-author agent does not have the verification data in scope when it writes; only the verification agent has independently checked the market. So the synthesis files are always optimistic about non-consensus until the verification agent has scrubbed them. The verification verdict is final. Clean deletion (not flagged deletion) keeps the surviving content readable.

Do NOT delete from `conclusion.md` or `future_trends.md`. Conclusions can be priced-in and still factually correct; future trends are about direction, not pricing. The purge applies only to the three files above.

### Step 7.6 — OVERWRITE `research/opportunity.md` (actionable shortlist)
After the Verification Agent finishes, fully OVERWRITE `research/opportunity.md` (do not append — this is the user's live action list, regenerated every cycle).

Include ONLY findings whose verification verdict is `VERIFIED-NOT-PRICED-IN` or `PARTIALLY-PRICED-IN`. Exclude `ALREADY-PRICED-IN` entirely — those are dead leads for the user.

Group into two tiers:
- **Tier 1 — Verified non-consensus** (verdict: VERIFIED-NOT-PRICED-IN). Highest action priority.
- **Tier 2 — Partially priced** (verdict: PARTIALLY-PRICED-IN). Secondary action — the consensus is moving, so window is closing.

For each opportunity, write a concise action-oriented entry:
- **Opportunity** — one-line label
- **The bet** — what to act on, concretely (company / position / experiment / supplier conversation)
- **Why still mispriced** — what the market is missing right now (cite the verification verdict)
- **Catalyst** — concrete event + rough date that forces repricing
- **Action window** — short / medium / long
- **Falsifier** — observable signal that closes the opportunity
- **Cross-reference** — sector(s) and source(s) from the synthesis

End the file with a "What changed from previous run" note: which opportunities are new this cycle, which dropped off (verified became priced), which downgraded.

This file is what the user opens between runs. Keep it tight, actionable, and ruthlessly free of any item the verification agent flagged as `ALREADY-PRICED-IN`.

**Empty `opportunity.md` is acceptable.** If a cycle finds zero `VERIFIED-NOT-PRICED-IN` and zero `PARTIALLY-PRICED-IN` items, write a short opportunity.md that says exactly that — "Run #N produced no actionable non-consensus opportunities. All synthesis candidates were already-priced-in per `verification_log.md`." Not every cycle must produce action items. An honest empty list is more useful than fabricated opportunities.

### Step 8 — Write run verdict to `run_history.md`
Append a new section:
```markdown
## Run #N — YYYY-MM-DD HH:MM UTC
- Sectors with new sources: [list, or "none"]
- New cross-sector alpha finds: [list, or "no new finds — current set unchanged"]
- Verification verdict on findings: X verified-not-priced-in / Y partially-priced / Z already-priced
- New conclusions added to conclusion.md: [list, or "none"]
- Overall: GENUINELY NEW FINDINGS | MINOR REFRESH | NO MATERIAL CHANGE
```

If nothing new was found, **say so explicitly**. Not every run must produce novelty.

### Step 8.5 — Keep `index.html` in sync with the latest run
The live site at `https://harrrshall.github.io/hardwareresearch/` is a single static HTML file (`index.html` at repo root) that fetches markdown at runtime. The markdown fetcher means most updates need no HTML change. BUT the abstract block on the frontmatter contains hard-coded text that summarizes the current verification verdict — that text must be refreshed each cycle.

Specifically, locate the `<ul class="abstract-list">` inside `<section id="frontmatter">` in `index.html`. Update its `<li>` items so they reflect:
- The current count of validated sources (e.g. "Approximately N primary sources…")
- The list of `VERIFIED-NOT-PRICED-IN` finds for the *current* run (the second-to-last bullet typically — "Two findings cleanly survived as genuinely non-consensus in Run #N: …"); if the count of verified non-consensus changes, rewrite the bullet
- The verification tally (e.g. "X further claims are partially priced; Y were retired…")

Do NOT add per-run stamps, bylines, last-update strings, or footer text — the user explicitly removed those. Keep the file minimal: title, hero illustration, abstract bullets, Contents, rendered-report area.

Do NOT touch `index.html`'s JavaScript, fonts, SVG illustrations, layout, or any element other than the abstract bullet text — those are visual identity decisions, not per-run content.

### Step 8.6 — Source Index titles must be Markdown links
In every sector's `research.md`, the `## Source Index` section must list each source with its title rendered as a clickable Markdown link: `[Title](URL)`. The URL is taken from the same row's URL column when available, otherwise from `sources.json` for that sector by id or title match. Tables that already have linked titles are left alone.

Plain-text titles in the Source Index are not acceptable — they leave the user without a path to the underlying source.

This rule applies to:
- Each sector's `research.md` Source Index table(s)
- Any new table the writer agent creates that lists sources with titles

The Writer Agent should emit linked titles directly; if it forgets, the orchestrator runs `/tmp/linkify_v2.py` (or an equivalent one-off pass) before commit to fix it.

### Step 9 — Commit and push
```bash
git add research/
git commit -m "Run #N — [one-line verdict summary]"
git push origin main
```

---

## Run counter — canonical source
`research/run_history.md` is the source of truth for run numbering. Read it at the start of each cycle. Run #N appears in:
- The top of `cross_sector_alpha.md`, `future_trends.md`, `market_opportunities.md`
- Any new entry in `conclusion.md`
- The `run_history.md` entry itself

---

## Recency window
The research window slides forward with each run: always "last 6 months from the cycle's execution date." Material older than that may be cited as context only.

---

## Do-not rules
- Never delete past sector `research.md` or `papers/`.
- Never silently overwrite a previous run's findings without noting it.
- Never claim a finding is "not priced in" without the Verification Agent checking it in the same run.
- Never skip the Verification Agent — it is mandatory in every cycle.
- Never put `ALREADY-PRICED-IN` items into `opportunity.md` — that file is the user's live action list, signal-only.
- Never co-author commits with Claude/Anthropic (user's standing rule).
