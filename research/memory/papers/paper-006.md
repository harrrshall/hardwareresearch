# Paper 006: TSMC N2 SRAM Breakthrough — 38 Mb/mm² at 2nm GAA

**Source ID**: 29, 30  
**Source Title**: TSMC 2nm Process Claims Major SRAM Improvements; Intel, TSMC Tout SRAM Breakthroughs at 2nm  
**URLs**:  
- https://www.tomshardware.com/tech-industry/sram-scaling-isnt-dead-after-all-tsmcs-2nm-process-tech-claims-major-improvements  
- https://marklapedus.substack.com/p/intel-tsmc-tout-sram-breakthroughs  
**Date**: 2025  
**Tags**: SRAM, TSMC, N2, 2nm, GAA, scaling

---

## One-Sentence Claim
TSMC's N2 (2nm) process with gate-all-around nanosheet transistors achieves approximately 38 Mb/mm² SRAM density — the densest ever reported — reversing the SRAM scaling stagnation that plagued the 3nm generation and enabling >1.15x chip density improvement over N3.

## Methodology Summary
TSMC's N2 uses gate-all-around (GAA) nanosheet transistors, replacing the FinFET architecture used from 16nm through 3nm. The GAA geometry enables smaller HD (high-density) SRAM bit cell sizes that were not achievable with FinFET at 3nm. N2 is in risk production and scheduled for mass production in 2H 2025, with N2P (5% speed-enhanced) targeting qualification in 2025 and mass production in 2026.

## Quantitative Results
- SRAM density: ~38 Mb/mm² (densest macro ever reported at time of publication)
- Speed improvement vs N3: 15% (at same power) OR 30% power reduction (at same speed)
- Chip density improvement vs N3: >1.15x
- N3E (previous gen): Zero SRAM scaling advantage vs N5 — HD SRAM bit cell size unchanged
- N2P: Additional 5% speed improvement over N2; mass production 2026
- A16: First GAA + backside power delivery node; target 2H 2026
- Transistor gate pitch reduction: GAA enables smaller gate pitch than FinFET equivalent

## Stated Limitations
- N3B and N3E showed zero SRAM bit cell area reduction vs N5 — only N2 breaks this pattern
- N2P improvements are incremental (5% speed) over N2
- Risk production timing suggests N2 yield ramping is still in progress

## Inferred Limitations
- 38 Mb/mm² SRAM density is for HD macros; L1/L2 cache macros in production designs may not achieve theoretical maximum
- GAA manufacturing complexity introduces new process control challenges (nanosheet thickness uniformity)
- SRAM scaling recovery at N2 does not guarantee proportional DRAM scaling improvements (different physics)

## Architectural Significance
The SRAM scaling recovery at N2 is architecturally significant because SRAM dominates chip area in modern CPUs and GPU compute tiles. SRAM stagnation at 3nm forced larger L1/L2 caches or lower cache capacities than desired. N2's ~38 Mb/mm² enables chip designers to either increase cache capacity (beneficial for memory-bound LLM workloads) or reduce chip area for equivalent cache sizes. This directly affects the economics of AI accelerator design.

## Cross-Paper Connections
- Dense SRAM at N2 enables larger on-chip buffers, partially mitigating HBM bandwidth requirements (papers 001-003)
- TSMC A16 (2H 2026) with backside power delivery extends the N2 gains further
- d-Matrix's compute-in-SRAM approach (paper-016) relies on dense SRAM macros at advanced nodes
- Marvell at Hot Chips 2025 (paper-014) cited SRAM density as critical for custom HBM integration

## Theme Tags
SRAM, TSMC, N2, 2nm, GAA, nanosheet, density, scaling, FinFET-successor
