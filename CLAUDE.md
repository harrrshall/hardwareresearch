# Hardware Research Pipeline — Operational Instructions

## Mission
Maintain a continuously-updated, peer-reviewed-grade research dataset on the AI / semiconductor hardware stack. The pipeline re-executes every 5 hours, discovers new material, and refreshes the cross-sector synthesis. An independent verification agent confirms that findings flagged "not priced into the market" are still genuinely non-consensus.

## Repository
- **Local**: `/home/cybernovas/Desktop/2026/experiments/hardware`
- **Remote**: `https://github.com/harrrshall/hardware-research-2026`
- **Master spec**: `hardware_research_orchestration.md` (sector pipeline + global synthesis spec)
- **Research outputs**: `research/`
- **Run tracker**: `research/run_history.md`

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

### Step 7.5 — OVERWRITE `research/opportunity.md` (actionable shortlist)
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
