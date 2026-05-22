# Multi-Agent Hardware Research Orchestration System

## Mission

Conduct a comprehensive  retrospective on advancements across the semiconductor and AI hardware stack. Produce validated, peer-reviewed-grade research outputs per sector, followed by a synthesized cross-sector strategic analysis.

## Time Window

Last 6 months from execution date. Older material may only be cited as essential context, not as primary findings.

---

## 1. System Architecture

### 1.1 Orchestrator (root agent)

Responsibilities:
- Initialize the full directory structure
- Spawn 10 sector research teams **in parallel**
- Enforce a hard synchronization barrier — global synthesis cannot begin until every sector is complete
- Spawn the Global Synthesis Agent after the barrier clears
- Maintain run state in `run_log.md`
- Retry failed teams in isolation without unblocking the global stage

### 1.2 Per-Sector Research Team

Each of the 10 sectors gets its own team. Inside a team, four specialized sub-agents run **sequentially**:

1. **Collector Agent** — gathers candidate papers and primary sources
2. **Deep Analyzer Agent** — reads, extracts, and writes per-paper analyses
3. **Validator Agent** — cross-references claims, flags weak evidence, separates signal from noise
4. **Writer Agent** — synthesizes validated material into the final `research.md`

### 1.3 Global Synthesis Agent

Activated only after all 10 sector teams complete. Reads every `research.md` and `sources.json`, performs cross-sector correlation, and produces three top-level files.

---

## 2. Sectors (10 total)

Create one folder per sector, using these exact names:

1. `GPUs`
2. `CPUs`
3. `memory`
4. `chip_fabrication`
5. `AI_accelerators`
6. `packaging`
7. `photonics`
8. `interconnects`
9. `datacenter_hardware`
10. `edge_AI_hardware`

---

## 3. Directory Layout

```
research/
├── GPUs/
│   ├── research.md           ← primary sector deliverable
│   ├── papers/               ← one .md per paper analyzed
│   │   ├── paper-001.md
│   │   ├── paper-002.md
│   │   └── ...
│   ├── sources.json          ← all candidate sources + metadata
│   └── validation_log.md     ← evidence-quality decisions
├── CPUs/                     (same structure)
├── memory/
├── chip_fabrication/
├── AI_accelerators/
├── packaging/
├── photonics/
├── interconnects/
├── datacenter_hardware/
├── edge_AI_hardware/
├── conclusion.md             ← global synthesis output
├── market_opportunities.md   ← global synthesis output
├── future_trends.md          ← global synthesis output
└── run_log.md                ← orchestrator transition log
```

---

## 4. Source Priority Tiers

All agents weight evidence by tier. Higher tier overrides lower tier on conflict.

### Tier 1 — Peer-reviewed (highest credibility)
- ACM Digital Library, IEEE Xplore
- ISCA, MICRO, HPCA, ASPLOS proceedings
- ISSCC, VLSI Symposium, IEDM
- Hot Chips (industry-presented but vetted)
- SC (Supercomputing) proceedings
- Nature Electronics, IEEE Journal of Solid-State Circuits

### Tier 2 — Preprints (leading indicator, not ground truth)
- arXiv: `cs.AR`, `cs.AI`, `cs.PF`, `cs.DC`
- Semantic Scholar for citation context
- Must be cross-referenced before being elevated to "validated"

### Tier 3 — Industry analysis
- SemiAnalysis
- Chips and Cheese
- The Next Platform
- IEEE Spectrum
- AnandTech archives, Tom's Hardware (for benchmark numbers)

### Tier 4 — Primary vendor disclosure
- NVIDIA, AMD, Intel, Apple, Qualcomm, TSMC, Samsung, SK Hynix, Micron, ASML whitepapers
- Earnings call transcripts
- SEC filings, investor day presentations

---

## 5. Validation Criteria

A finding is retained only if **all** of these hold:

1. **Recency** — Published or disclosed within the last 6 months
2. **Cross-reference** — Tier 2 claims confirmed by ≥1 independent source
3. **Methodology disclosure** — Performance claims include baseline, workload, and measurement method
4. **Benchmark fairness** — Comparisons aren't against strawman baselines
5. **No rebuttal** — Search confirms no public rebuttal or failed replication
6. **Traceable attribution** — Original source link captured

Items failing validation are **moved to `validation_log.md` with reason**, not silently dropped. This preserves an audit trail.

---

## 6. Per-Sector Workflow (parallel across sectors, sequential within team)

### 6.1 Collector Agent

Inputs: sector name, time window, source tier list.

Process:
- Query Tier 1 venues' recent proceedings
- Walk arXiv listings month-by-month for `cs.AR` and adjacent categories
- Query Google Scholar with "since 2025" filter using sector-specific keyword sets
- Use Semantic Scholar to expand citation graphs around 3–5 seed papers
- Sweep Tier 3 sources for industry context
- Capture Tier 4 disclosures relevant to the sector

Output: `sources.json` with 40–80 candidate items. Each entry contains:
```json
{
  "id": "src-001",
  "title": "...",
  "authors": ["..."],
  "venue": "...",
  "date": "YYYY-MM-DD",
  "url": "...",
  "tier": 1,
  "abstract": "..."
}
```

### 6.2 Deep Analyzer Agent

Input: `sources.json`.

For each candidate, write `papers/paper-NNN.md` containing:
- **One-sentence claim** — the core contribution in plain language
- **Methodology summary** — how the work was done
- **Quantitative results** — actual numbers, with units and baselines
- **Stated limitations** — what the authors acknowledge
- **Inferred limitations** — what the Analyzer suspects but the authors didn't say
- **Architectural significance** — why this matters for the sector
- **Cross-paper connections** — other items in this sector that this work builds on, contradicts, or extends
- **Theme tags** — e.g., `3D-stacking`, `compute-in-memory`, `chiplet`, `RISC-V-vector`

### 6.3 Validator Agent

Input: all `papers/paper-NNN.md`, original `sources.json`.

Process:
- Walk every paper file
- Apply the six validation criteria
- Assign each item one of: `VALIDATED`, `CONTEXT-ONLY`, `REJECTED`
- For suspicious claims, run additional searches to confirm or refute
- Write all decisions and reasoning to `validation_log.md`
- Tag each `paper-NNN.md` header with its validation state
- Remove `REJECTED` items from the dataset that feeds the Writer

### 6.4 Writer Agent

Input: validated `papers/*.md`, `sources.json`, `validation_log.md`.

Output: `research.md` with **these exact sections, in this order**:

```markdown
# [Sector Name] — Research Summary
Generated: [date] | Window: [start] – [end] | Validated sources: [N]

## Executive Summary
3–5 sentences capturing the most important shifts in this sector over the window.

## All Collected Findings
Master bulleted list of every validated finding, each with source link.

## Summarized Papers
Per-paper synopses grouped by sub-theme. Each entry includes the claim,
the evidence, and a one-line significance note.

## Technical Analysis
Deep technical commentary — what's genuinely novel vs incremental,
what fundamental constraints are being addressed, what tradeoffs are being made.

## Architectural Observations
Design patterns across the sector — what's converging, what's diverging,
which approaches are being abandoned, which are gaining adherents.

## Trend Analysis
Directional movement: what was state-of-the-art 6 months ago vs now.
Rate of change. Inflection points.

## Manufacturing Implications
Process node, yield, packaging complexity, supply chain consequences.
Which fabs/foundries are positioned for which directions.

## Scalability Considerations
Power, thermal, bandwidth, area, and cost scaling envelopes.
Where the walls are.

## Strategic Insights
What this sector implies for system builders, buyers, and investors.
Asymmetric bets visible from this sector alone.

## Open Questions
What the current evidence does not yet resolve. Where more data is needed.

## Source Index
All cited sources grouped by tier, with links and dates.
```

---

## 7. Synchronization Barrier

The orchestrator does **not** spawn the Global Synthesis Agent until every sector folder contains:

- `research.md` — non-empty, all 11 required sections present
- `sources.json` — ≥30 entries
- `validation_log.md` — non-empty
- `papers/` — populated with validated paper analyses

If any sector team fails or stalls, the orchestrator retries that team only. Other completed teams hold their state. The global stage stays blocked until full completion.

---

## 8. Global Synthesis Agent

Activates only after the barrier clears. Reads all 10 `research.md` files and all `sources.json` files. Produces three deliverables at the root level.

### 8.1 `conclusion.md`

- Executive overview across all 10 sectors
- Cross-sector findings correlation — claims or trends that appear in ≥2 sectors
- Cross-industry patterns
- Emerging technological shifts (a shift counts if ≥3 sectors show the same direction)
- Identified bottlenecks — places where multiple sectors hit the same physical, economic, or architectural wall
- Confidence rating attached to each conclusion (high / medium / speculative)
- Every conclusion cites the sector(s) and source(s) supporting it

### 8.2 `market_opportunities.md`

- Opportunities not yet priced into the market
- Underexplored hardware directions
- Asymmetric bets — high payoff, low current attention
- For each opportunity:
  - **Thesis** — the core bet
  - **Supporting evidence** — citations to sector research.md files
  - **Risk factors** — what would invalidate the thesis
  - **Time horizon** — short / medium / long
  - **Confidence level**

### 8.3 `future_trends.md`

-  what hardens into reality next
- 12–24-month projection: what becomes mainstream
- 3–5-year inference: directional bets
- Scenario branching where evidence supports multiple futures
- For each trend:
  - **Confidence level**
  - **Key signals to watch**
  - **Falsifiers** — what would prove the trend wrong

---

## 9. Quality Self-Check (post-synthesis)

After the three global files are written, the orchestrator runs a final pass:

- No claim in `conclusion.md` is unsupported by a sector `research.md`
- No sector is underrepresented in cross-sector analysis (every sector cited ≥2 times in global files)
- All three global files cross-link to specific sector sources
- No claim violates the recency window
- No Tier 2 claim was elevated without Tier 1 or Tier 3 corroboration

Failures here trigger targeted re-runs, not full reruns.

---

## 10. Execution Notes

- **Parallelism**: All 10 sector teams run concurrently. Do not serialize.
- **Sequentiality within team**: Collector → Analyzer → Validator → Writer, strict order.
- **Sync barrier is hard**: No previewing the global stage with partial sector data.
- **All outputs are markdown** (plus one JSON per sector for source metadata). No PDF, no DOCX in this pipeline.
- **Logging**: Single `run_log.md` at root with timestamps for every stage transition, agent spawn, and validation decision summary.
- **Idempotency**: Re-running the orchestrator should detect existing complete sectors and skip them unless explicitly forced.
- **Failure mode**: A failed sector blocks the global stage but not other sectors. Retry isolated.

---

## 11. Keyword Seeds (per sector, for Collector Agents)

To save the Collector Agents discovery time, here are starting keyword sets. They should expand these via citation graphs, not treat them as exhaustive.

- **GPUs**: tensor cores, sparsity, ray tracing units, GPU memory hierarchy, warp scheduling, MIG, NVLink
- **CPUs**: out-of-order width, branch prediction, vector ISA, chiplet CPU, P/E core scheduling, RISC-V high-performance
- **memory**: HBM4, LPDDR6, CXL 3.0, compute-in-memory, near-memory compute, 3D DRAM, NVM, processing-in-memory
- **chip_fabrication**: 2nm, GAAFET, high-NA EUV, backside power delivery, yield enhancement, advanced lithography
- **AI_accelerators**: transformer accelerator, sparsity hardware, analog AI, dataflow architecture, NPU, systolic array
- **packaging**: CoWoS, SoIC, hybrid bonding, fan-out, 2.5D, 3D stacking, interposer, glass substrate
- **photonics**: silicon photonics, co-packaged optics, optical interconnect, photonic compute, optical I/O
- **interconnects**: UCIe, NVLink, PCIe 6.0/7.0, CXL fabric, optical switching, chip-to-chip
- **datacenter_hardware**: liquid cooling, immersion cooling, rack-scale design, AI cluster topology, power delivery
- **edge_AI_hardware**: on-device LLM, mobile NPU, microcontroller AI, energy-per-inference, sparse edge inference

---

## 12. Invocation Pattern (pseudocode)

```
orchestrator.init()
orchestrator.create_dirs(SECTORS)

teams = [spawn_team(sector) for sector in SECTORS]
parallel_run(teams)
barrier.wait_until_all_complete(teams)

global_agent = spawn_global_synthesis()
global_agent.run(read_all_sector_outputs())

orchestrator.quality_self_check()
orchestrator.finalize()
```

Each `spawn_team(sector)` runs:
```
team.collector.run() → sources.json
team.analyzer.run(sources.json) → papers/*.md
team.validator.run(papers/*.md) → validation_log.md
team.writer.run(validated_papers) → research.md
```

---

## 13. Done Criteria

The full run is considered complete when:

- All 10 sector folders contain a valid `research.md` and supporting files
- `conclusion.md`, `market_opportunities.md`, and `future_trends.md` exist at root
- Quality self-check passes
- `run_log.md` shows a clean finalization timestamp

Anything short of all four conditions is a partial run and must be flagged.
