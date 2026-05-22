# memory — Research Summary

Generated: 2026-05-22 | Window: 2025-11-22 – 2026-05-22 | Validated sources: 55

---

## Executive Summary

The six-month period from November 2025 to May 2026 marks the most consequential transition in DRAM architecture since the introduction of DDR4. Three simultaneous technology inflections converged: **HBM4 entered mass production** from all three major vendors with 2x the interface width of HBM3E; **LPDDR6 was standardized and first products were announced**; and **CXL 4.0 was released** on November 18, 2025 at SC25. Underneath these production events, a deeper structural shift is underway in 3D DRAM research, processing-in-memory standardization, and hybrid bonding manufacturing — each of which will define the memory landscape from 2027 onward.

The central finding is that memory bandwidth has become the singular binding constraint for AI infrastructure, not compute. A 70B parameter FP16 model requires loading ~140 GB of weights per token, and even the H100 SXM5's 3.35 TB/s bandwidth yields a theoretical 42ms floor per token. HBM4's 2–3.3 TB/s per stack represents a 2x improvement over HBM3E but does not eliminate the memory wall — it delays it. The industry's response is a multi-front attack: higher-bandwidth HBM (SK Hynix: 2 TB/s; Samsung: 3.3 TB/s; Micron: 2.8 TB/s), more stacks per GPU (AMD MI400: 12 stacks, 432 GB, 19.6 TB/s), memory disaggregation via CXL for capacity expansion, and processing-in-memory standardization to eliminate data movement entirely.

Five near-term production facts define 2026: (1) All three HBM4 vendors are in mass production with 2026 capacity sold out. (2) JEDEC's LPDDR6 standard was published July 2025. (3) CXL 4.0 at 128 GT/s was released November 2025. (4) TSMC's N2 2nm process with 38 Mb/mm² SRAM density is in mass production. (5) 3D NAND has crossed 400 layers. The 2027+ picture is defined by HBM4E (4 TB/s, 16 Gbps, hybrid bonding), DDR6 consumer deployment, CXL memory fabric at rack scale, and the first potential appearance of IGZO-based 3D DRAM in product roadmaps.

---

## All Collected Findings

### HBM4 Mass Production Race

**SK Hynix** completed development of HBM4 with a 2,048-bit interface (double HBM3E's 1,024-bit) and 10 GT/s JEDEC specification, delivering actual products at 11.7 Gbps and 2 TB/s bandwidth per stack. The 16-Hi 48 GB configuration was demonstrated at CES 2026 (January). The 12-Hi 36 GB configuration entered mass production in approximately February 2026. SK Hynix uses TSMC's 12nm logic process for the base die — the external foundry dependency gives TSMC leverage but delivers higher base die performance. SK Hynix held 62% of the global HBM market in Q2 2025, slipping to 57% in Q3 2025. The company is projected to be primary HBM4 supplier to NVIDIA (~two-thirds of Vera Rubin HBM4 allocation).

**Samsung** presented its HBM4 at ISSCC 2026 (February 15–19, San Francisco). Its 12-Hi 36 GB configuration achieves 3.3 TB/s via 13 Gbps per pin — 37.5% higher bandwidth than Samsung's initial HBM4 product (which shipped at 2.4 TB/s). The upgraded chip uses Samsung's 1c (6th-gen 10nm-class) DRAM process dies and an SF4 (Samsung Foundry 4nm-class) logic base die. Power efficiency improved 40% vs HBM3E; thermal resistance improved 10%; heat dissipation improved 30%. Samsung began mass production in February 2026 and is supplying both NVIDIA (Vera Rubin) and Google (TPU v6). Samsung's HBM market share recovered from 15% (Q2 2025) to 22% (Q3 2025) as qualification issues with NVIDIA were resolved. Morgan Stanley projects Samsung's memory profits to rise >300% in 2026.

**Micron** entered high-volume production of HBM4 36GB 12H in Q1 2026 on its 1-gamma (6th-gen 10nm-class) DRAM process. Micron's HBM4 achieves >11 Gbps per pin and >2.8 TB/s bandwidth — a 2.3x improvement over Micron's HBM3E, with >20% better power efficiency. Micron shipped 48GB 16H samples (33% capacity increase per HBM placement) to customers. Micron's 2026 HBM capacity is 100% sold out under multi-year agreements. Micron projects ~$8 billion HBM annualized revenue run-rate. Micron held 21% HBM share in Q3 2025.

**HBM4 JEDEC Specification (JESD270-4)**: Published April 2025. Defines 2,048-bit interface width (doubled from 1,024-bit in HBM3E), minimum 8 GT/s per pin, maximum capacity of 64 Gb per die, 32 independent channels. HBM4 enables up to 2 TB/s bandwidth per stack at JEDEC minimum spec.

### LPDDR6 Standardization and Products

**JEDEC JESD209-6** was published July 9, 2025 — the first DDR6-era memory standard to be finalized (before DDR6 itself). The standard defines 10,667 MT/s to 14,400 MT/s data rates, dual sub-channel architecture with 12 DQ lines per sub-channel, 32-byte access granularity, device densities from 4 Gb to 64 Gb, lower VDD2 supply vs LPDDR5, DVFSL for dynamic voltage scaling, on-die ECC, CA parity, and MBIST.

**Samsung LPDDR6**: 12nm process delivering 10.7 Gbps with 21% energy efficiency improvement over LPDDR5X. Presented at CES 2026, won CES Innovation Award Honoree in Mobile Devices category. Roadmap targets 14 Gbps. LPDDR6X samples sent to Qualcomm for SoC validation.

**SK Hynix LPDDR6**: 16 Gb per die on 1c process, targeting 14.4 Gbps per I/O pin. Presented at ISSCC 2026.

**LPDDR6-PIM**: JEDEC previewed the LPDDR6 roadmap for data centers including SOCAMM2 and Processing-in-Memory integration. Samsung and SK Hynix are collaborating on LPDDR6-PIM standardization through JEDEC, targeting approval in 2026 for products.

### CXL Memory Fabric Evolution

**CXL 4.0** was released November 18, 2025 at SC25. It shifts from PCIe 6.x (64 GT/s) to PCIe 7.0 (128 GT/s), doubling link bandwidth while maintaining the 256-byte FLIT format from CXL 3.x. New bundled port capability aggregates physical ports to achieve 1.5 TB/s per logical attachment. Enhanced RAS features added for production deployment. The specification enables 100+ TB coherent memory pools. CXL 4.0 multi-rack systems are expected in late 2026 to 2027.

**CXL deployment phases**: Phase 1 (now) — memory expansion; Phase 2 (2025-2026) — memory tiering between fast local DRAM and CXL-attached; Phase 3 (2026-2027) — memory pooling via CXL switches with 100 TiB+ coherent pools. Commercial 100 TiB CXL pools became available in 2025.

**CXL for LLM inference**: At SC25 (November 2025), XConn Technologies and MemVerge demonstrated CXL memory solutions for LLM KV cache offload and prefill/decode disaggregation, achieving 3.8x speedup vs 200G RDMA and 6.5x vs 100G RDMA (vendor benchmarks). Astera Labs' Leo CXL Smart Memory Controller enabled 3x concurrent LLM instances at 3x lower latency.

**arXiv modeling (2511.04104)** shows 20-40% TCO reduction for disaggregated architectures vs. monolithic servers at data center scale (preprint, peer review pending).

### AI Accelerators: HBM4 in Production Systems

**NVIDIA Vera Rubin (NVL72)**: 288 GB HBM4 per GPU, 22.2 TB/s total HBM4 bandwidth per GPU (updated spec, ~10% increase to stay ahead of AMD), 50 PFLOPS FP4, 72 GPUs in NVL72 rack system (20.7 TB HBM4 per rack). H2 2026 deployment. Three qualified HBM4 suppliers: SK Hynix, Samsung, Micron.

**AMD Instinct MI400**: 12 HBM4 stacks per GPU, 432 GB capacity, 19.6 TB/s bandwidth, CDNA 5 on TSMC 2nm, CoWoS-L advanced packaging. Confirmed at CES 2026. Claims 1.5x memory capacity advantage over Vera Rubin. Scale-out link: 300 GB/s. Deployment: 2026.

### SRAM Scaling Recovery at 2nm

**TSMC N2** (gate-all-around nanosheet transistors) achieves approximately 38 Mb/mm² SRAM density — the highest ever reported, enabled by GAA architecture. N2 delivers 15% speed improvement or 30% power reduction vs N3, with >1.15x chip density. N2 in risk production; mass production H2 2025. N3E and N3B provided zero SRAM scaling benefit over N5. N2P (5% additional speed) targets mass production 2026. TSMC A16 (GAA + backside power delivery) targeting H2 2026.

**Intel** also reported SRAM breakthroughs at the 2nm node class (Intel 20A/18A), confirmed at industry forums.

### 3D DRAM Research

**imec 2T0C IGZO DRAM (IEDM 2025)**: Two IGZO thin-film transistors per cell, zero capacitor. Sub-100nm patterning via reactive ion etch (RIE). 5nm IGZO channels via ALD. 1.2V operation at 5-year lifetime at 95°C. Added to Yole Intelligence DRAM long-term roadmap. Not in production timeline; research stage.

**Kioxia oxide-semiconductor 3D DRAM (IEDM 2025)**: Highly stackable oxide-semiconductor channel transistor technology for high-density, low-power 3D DRAM. IEDM 2025, Session 29-1. Research stage.

Both represent the potential for DRAM-on-logic monolithic integration using the same 3D stacking techniques pioneered by 3D NAND.

### Processing-in-Memory

**SK Hynix GDDR6-AiM / AiMX**: GDDR6-AiM integrates MAC units into GDDR6 dies at 16 Gbps. AiMX PCIe card: 10x LLM inference speedup vs GPU at 1/5 power. GPT-1.3B benchmark: 347.83 tokens/s with 8x PIM bandwidth scaling, 1.6x faster than NVIDIA A100. Optimized for attention operations and KV cache utilization.

**LPDDR6-PIM**: Samsung and SK Hynix jointly standardizing through JEDEC; targets approval in 2026.

**arXiv (2412.19275) — Processing-in-DRAM**: Demonstrates functionally-complete bulk-bitwise computation in unmodified commercial DRAM chips (no custom silicon required). Theoretical foundation for software-only PIM.

### Hybrid Bonding for Advanced 3D Stacking

**Samsung HCB (Hybrid Copper Bonding)**: Adopted for HBM4 and next-gen stacking. Eliminates microbumps. Reduces thermal resistance >20% vs TCB. Licensed hybrid bonding patents from YMTC for NAND V10.

**SK Hynix hybrid bonding**: MR-MUF as primary process for HBM4; hybrid bonding as backup/HBM4E target. 321-layer 4D NAND uses hybrid bonding; 400-layer NAND target by end 2025/H1 2026.

**Pitch**: Hybrid bonding enables <10µm interconnect pitch vs ~40-50µm for microbumps, enabling higher bandwidth density and thinner stacks.

### 3D NAND 400-Layer Milestone

Samsung V10 NAND: 400+ layers, 1 Tb die, 28 Gb/mm², H1 2026. Kioxia BiCS10: 332 layers, expedited from 2027 to 2026 for AI data center demand. SK Hynix: 321-layer in mass production with hybrid bonding; 400-layer by H1 2026. All major vendors converging on 1-2 Tb die by 2026-2027 for QLC. Samsung roadmap targets 1,000 layers by 2030.

### DDR6 and GDDR7 Status

**DDR6**: JEDEC draft completed end 2024. Final standard expected Q4 2025–Q1 2026. Enterprise/server priority access 2026. Consumer DDR6 delayed to 2027. Speed range: 8,800–17,600 MT/s.

**GDDR7**: SK Hynix presented 48 Gbps 24 Gb GDDR7 at ISSCC 2026 (symmetric dual-channel, 192 GB/s per chip, 70% above 28 Gbps GDDR7). Samsung mass-producing 24 Gb GDDR7 since November 2025, sampled at 42.5 Gbps. NVIDIA RTX 50-series uses GDDR7 (Blackwell, launched January 2025).

### NVM (MRAM/FeRAM)

STT-MRAM entering production (Everspin 64Mb/128Mb for AI, 2025). Netsol scaling from 28nm to 14nm by 2026. No single NVM technology has emerged as the production winner for analog in-memory computing AI accelerators as of 2025. FeRAM retains advantages for ultra-low-power binary neural network inference. HfO2-based FeFET reliability (wake-up, fatigue) and <650°C processing constraints limit expansion.

---

## Summarized Papers

| # | Title | Key Claim | Bandwidth / Density | Status |
|---|-------|-----------|---------------------|--------|
| 001 | SK Hynix HBM4 16-Hi 48GB | 2,048-bit, 11.7 Gbps, 2 TB/s per stack | 2 TB/s | Mass Production Feb 2026 |
| 002 | Samsung HBM4 ISSCC 2026 | 36GB 12-Hi, 13 Gbps, 3.3 TB/s | 3.3 TB/s | Mass Production Feb 2026 |
| 003 | Micron HBM4 for Vera Rubin | >2.8 TB/s, 2.3x vs HBM3E, 1-gamma process | 2.8 TB/s | HVP Q1 2026 |
| 004 | JEDEC LPDDR6 JESD209-6 | 10,667–14,400 MT/s, dual sub-channel, on-die ECC | 38.4 GB/s max | Standard Jul 2025 |
| 005 | CXL 4.0 Specification | 128 GT/s PCIe 7.0, 1.5 TB/s bundled ports | 1.5 TB/s/port | Released Nov 18, 2025 |
| 006 | TSMC N2 SRAM ~38 Mb/mm² | GAA nanosheet breaks 3nm SRAM stagnation | 38 Mb/mm² | Risk prod; mass prod H2 2025 |
| 007 | NVIDIA Vera Rubin NVL72 | 288 GB HBM4, 22.2 TB/s per GPU, 50 PFLOPS | 22.2 TB/s | H2 2026 deployment |
| 008 | AMD MI400 432GB HBM4 | 12 stacks, 432 GB, 19.6 TB/s, CDNA 5 on 2nm | 19.6 TB/s | 2026 |
| 009 | imec IGZO 2T0C DRAM (IEDM 2025) | Capacitorless DRAM, sub-100nm RIE, 1.2V/5yr | Research stage | IEDM Dec 2025 |
| 010 | Kioxia 3D DRAM OS transistor (IEDM 2025) | Highly stackable oxide-semiconductor 3D DRAM | Research stage | IEDM Dec 2025 |
| 011 | PIM: AiMX + LPDDR6-PIM standardization | 10x LLM speedup at 1/5 power; JEDEC standardization underway | 16 Gbps GDDR6-AiM | Products 2026 |
| 012 | Hybrid bonding for HBM4 / 3D NAND | <10µm pitch, >20% thermal improvement vs TCB | <10µm pitch | Ramping 2026 |
| 013 | SOCAMM2 192 GB SK Hynix | 2x DDR5 RDIMM bandwidth, 55% power, 14×90mm | 2x DDR5 | Mass prod Q2 2026 |
| 014 | Hot Chips 2025: Memory dominates | "Memory: Almost the Only Thing That Matters" | — | Conference Aug 2025 |
| 015 | DDR6 JEDEC Timeline | 8,800–17,600 MT/s; consumer 2027 | 17,600 MT/s ceiling | Standard Q4 2025–Q1 2026 |
| 016 | Near-Memory Computing | 306.7 GOPS/W in 8-bit matmul; Google 3D-DRAM chiplet LLM work | 306.7 GOPS/W | Research → early deploy |
| 017 | HBM4E: 16 Gbps, 4 TB/s (Samsung GTC 2026) | 60% faster than HBM4; hybrid copper bonding | 4 TB/s | Roadmap 2027 |
| 018 | Memory Wall: LLM is BW-bound | 42ms/token lower bound for 70B FP16 on H100; FLOPS grew 80x vs BW 17x | 3.35 TB/s H100 ceiling | Analysis |
| 019 | CXL disaggregation: KV cache + TCO | 3.8x vs 200G RDMA; 20-40% TCO reduction | 3.8x speedup | SC25 + arXiv 2025 |
| 020 | 3D NAND 400-Layer: Samsung V10, Kioxia BiCS10 | 400+ layers, 1 Tb die; hybrid bonding enabling | 28 Gb/mm² | H1 2026 |
| 021 | HBM Market Share + Supercycle | SK Hynix 57-62%; 130% YoY growth; all 2026 capacity sold | — | Market analysis |
| 022 | MRAM/FeRAM NVM Status | STT-MRAM entering production; no clear CiM winner | Everspin 64-128Mb | Production (limited) |

---

## Technical Analysis

### HBM4 Interface Architecture: The 2,048-bit Revolution

The transition from HBM3E's 1,024-bit to HBM4's 2,048-bit interface width is the most significant architectural change to HBM in the standard's history. This is not a minor incremental improvement — it doubles the number of data channels from 16 to 32 and doubles the width of each channel, enabling bandwidth to scale at a rate that pin speed alone could not achieve.

**The math**: At 10 GT/s per pin × 2,048 pins / 8 bits per byte = 2,560 GB/s = 2.56 TB/s. Samsung's 3.3 TB/s product achieves this by pushing pin speed to 13 GT/s: 13 GT/s × 2,048 / 8 = 3,328 GB/s = 3.3 TB/s. SK Hynix's 11.7 Gbps × 2,048 / 8 = 2.995 TB/s ≈ 3 TB/s for the 16-Hi at full speed.

**Channel architecture impact**: 32 independent channels allow the memory controller to perform 32 simultaneous independent memory operations, dramatically increasing effective throughput for non-sequential access patterns (critical for attention mechanisms in transformers).

**Base die separation**: Both SK Hynix (TSMC 12nm) and Samsung (SF4) chose external or semi-external logic processes for their HBM4 base dies, distinct from the DRAM die process. This co-optimization approach allows the I/O circuits and row/column decoders to be designed on an optimized logic process while the memory cells use the most advanced DRAM process.

### Process Node Convergence

Three major DRAM process nodes are being commercialized in the 2025-2026 window:

1. **Samsung 1c (6th-gen 10nm-class)**: Used in Samsung HBM4 core dies and LPDDR6. Represents the leading-edge production node.
2. **Micron 1-gamma (1γ, 6th-gen 10nm-class)**: Offers 20% lower power, 15% higher performance, 30% greater bit density vs 1-beta (previous Micron node). Used in HBM4, SOCAMM2.
3. **SK Hynix 1c**: Used in LPDDR6 (14.4 Gbps) and HBM4 dies.

All three vendors are in their "6th generation 10nm-class" nodes, suggesting process convergence at a level not seen since DDR4 era. Below this, the path to smaller nodes for DRAM is increasingly non-obvious — this is precisely why 3D DRAM research (IGZO-based) is accelerating.

### Bandwidth Per System: The Stack Count Battle

The divergence between NVIDIA's 8-stack / 288GB Vera Rubin and AMD's 12-stack / 432GB MI400 reflects a fundamental design philosophy disagreement about where AI workloads are bottlenecked:

| System | Stacks | Capacity | Bandwidth | Compute |
|--------|--------|----------|-----------|---------|
| NVIDIA Vera Rubin GPU | 8 | 288 GB | 22.2 TB/s | 50 PFLOPS FP4 |
| AMD MI400 | 12 | 432 GB | 19.6 TB/s | N/A publicly |

NVIDIA's architecture maximizes bandwidth per GPU (22.2 TB/s vs 19.6 TB/s) for training and compute-heavy workloads. AMD's architecture maximizes capacity per GPU (432 GB vs 288 GB) for large-model inference where the entire model must fit in-package memory. The fact that AMD achieves lower bandwidth with 50% more stacks suggests the per-stack HBM4 bandwidth in MI400 is ~1.63 TB/s, compared to ~2.77 TB/s per stack in Vera Rubin — pointing to different HBM4 configurations or clock speeds.

---

## Architectural Observations

### Observation 1: Memory Hierarchy Stratification is Accelerating

The 2025-2026 period has produced a clearer five-tier memory hierarchy than existed two years ago:

**Tier 0 (On-chip SRAM)**: TSMC N2 at 38 Mb/mm², ~4-6 MB per mm² of chip area. Sub-nanosecond latency. Used for L1/L2 caches and compute-in-SRAM (d-Matrix approach). Bandwidth: hundreds of TB/s internally, limited by SRAM array width.

**Tier 1 (HBM4)**: 2–3.3 TB/s per stack, 36–48 GB per stack, ~100 ns latency. 8-12 stacks per GPU. Used as working memory for AI accelerator weights and activations.

**Tier 2 (SOCAMM2 / LPDDR6)**: 2x DDR5 RDIMM bandwidth, 192 GB modules, used for CPU-side memory in heterogeneous systems (Grace CPU with Vera Rubin). Lower cost per GB than HBM4.

**Tier 3 (CXL-attached DRAM)**: CXL 4.0 at 1.5 TB/s bundled port, latency ~100-200 ns above local DRAM. Used for KV cache spilling, memory capacity expansion, and tenant isolation in data centers. 100 TiB+ pool scale.

**Tier 4 (3D NAND SSD)**: 400-layer NAND at 28 Gb/mm², 16 TB+ per SSD, µs-range latency. Used for AI training dataset storage and model checkpointing. PCIe Gen 5/6 access.

### Observation 2: Base Die Architecture as a Competitive Moat

The choice of base die process node for HBM4 is emerging as a significant competitive differentiator:

- **SK Hynix → TSMC 12nm**: Leverages TSMC's mature logic process for robust I/O circuits; adds cost and supply chain complexity
- **Samsung → SF4 (Samsung Foundry 4nm)**: Keeps manufacturing in-house; requires Samsung Foundry's 4nm to be competitive with TSMC; allows tighter co-optimization

The base die contains all I/O circuits, temperature sensors, power management, and row/column address decoders. A more advanced base die process (SF4 vs 12nm) potentially enables faster I/O at lower power — which may explain Samsung's 13 Gbps vs SK Hynix's 11.7 Gbps.

### Observation 3: The Hybrid Bonding Inflection Point

Hybrid bonding's penetration into production memory in 2025-2026 is a manufacturing inflection comparable to the introduction of FinFET for logic:

- **3D NAND**: SK Hynix 321-layer and Samsung V10 400-layer using hybrid bonding NOW
- **HBM4**: Hybrid bonding being evaluated/adopted for 16-Hi stacks and confirmed for HBM4E
- **3D DRAM**: imec and Kioxia IEDM 2025 research assumes hybrid bonding as the integration mechanism

The sub-10µm interconnect pitch enabled by hybrid bonding removes the fundamental area penalty of bump-based interconnects. For HBM, eliminating microbumps means: (a) thinner stack for same layer count, (b) better thermal management, (c) lower parasitic capacitance enabling higher pin speeds, (d) higher interconnect density per area enabling wider buses.

### Observation 4: PIM Standardization Creates an Industry Inflection

The joint Samsung/SK Hynix collaboration on LPDDR6-PIM standardization through JEDEC is architecturally significant beyond its technical merits. Two competing companies cooperating on a memory standard only happens when both parties believe the standard will expand their total addressable market. The implication: both Samsung and SK Hynix expect LPDDR6-PIM to become a commodity module that device OEMs will demand, creating pull from the market rather than requiring each memory vendor to individually sell PIM hardware.

This contrasts with the current AiMX approach (SK Hynix-specific PCIe card) — standardization enables any device with an LPDDR6-PIM controller to use commodity PIM DIMMs from any vendor.

### Observation 5: CXL 4.0 Arrives at the Right Time

The November 2025 CXL 4.0 release at exactly 128 GT/s (PCIe 7.0) lands at the moment HBM4's 2 TB/s per stack is becoming the new baseline. CXL 4.0's 1.5 TB/s bundled port bandwidth is comparable to a single HBM4 stack — meaning CXL-attached memory expanders can now serve as a secondary tier with bandwidth comparable to what was "high end" HBM memory just one generation ago. This timing enables a genuine two-tier approach: fast HBM4 for hot data, CXL 4.0 for warm data, with latency differentiation but bandwidth convergence.

---

## Trend Analysis

### Trend 1: Bandwidth Doubling Cadence Accelerates

| Generation | Bandwidth/Stack | Interface Width | Year |
|-----------|-----------------|-----------------|------|
| HBM2 | 256 GB/s | 1,024-bit | 2016 |
| HBM2E | 461 GB/s | 1,024-bit | 2020 |
| HBM3 | 819 GB/s | 1,024-bit | 2022 |
| HBM3E | 1,280 GB/s | 1,024-bit | 2024 |
| HBM4 | 2,000–3,300 GB/s | 2,048-bit | 2026 |
| HBM4E (target) | 4,000 GB/s | 2,048-bit | 2027 |

The transition from HBM3E to HBM4 achieved a 1.56x–2.58x bandwidth improvement in one generation (depending on which vendor's HBM3E and HBM4 are compared). The previous HBM2→HBM2E→HBM3→HBM3E sequence each delivered roughly 1.5-1.8x improvements. HBM4 is the first generation to break through by doubling interface width rather than only increasing pin speed — this architectural change cannot be repeated for HBM5 without further doubling to 4,096 bits.

### Trend 2: AI Compute → AI Memory → AI Interconnect Bottleneck Migration

The bottleneck in AI infrastructure has migrated predictably:
- **2020-2022**: Compute-bound (FLOPS insufficient for model scale)
- **2023-2024**: Memory bandwidth-bound (HBM3E insufficient for LLM inference)
- **2025-2026**: Memory capacity and interconnect becoming co-bottlenecks
- **2026-2027**: Projected interconnect dominance (NVLink, CXL fabric, scale-out bandwidth)

AMD's MI400 with 300 GB/s scale-out links and NVIDIA's updated Vera Rubin spec (22.2 TB/s total BW) both reflect that the next bottleneck is already being designed around.

### Trend 3: The Three-Vendor HBM Race Stabilizes at Different Bandwidth Points

As of Q1 2026, the three HBM4 vendors have settled into differentiated positions:
- **SK Hynix**: Volume leader, first to market, 11.7 Gbps, 2 TB/s. Prioritizes supply volume and reliability.
- **Samsung**: Bandwidth leader at 13 Gbps, 3.3 TB/s per 12-Hi stack. Prioritizes performance metrics.
- **Micron**: Efficiency leader at >20% power efficiency improvement, 2.3x vs HBM3E. Prioritizes TCO.

This differentiation is non-trivial — AI accelerator designers now choose HBM4 suppliers based on bandwidth, capacity, or power objectives, not just availability.

### Trend 4: Advanced Packaging Becomes the Primary Scaling Vector

The 2025-2026 period confirms that advanced packaging (hybrid bonding, CoWoS-L, SOCAMM2) is now advancing faster than the underlying DRAM process node:
- HBM4's 2x bandwidth improvement comes more from interface width doubling (packaging/architecture) than from DRAM process node improvement
- SOCAMM2's 2x DDR5 bandwidth improvement comes entirely from the LPDDR module format, not process node
- 3D NAND's 400-layer milestone is a stacking (packaging) achievement, not a lithography achievement
- imec IGZO DRAM's pathway to production depends on ALD (deposition) and hybrid bonding more than EUV

Process node scaling (EUV, GAA) enables the base transistors, but packaging innovations now deliver most of the system-level performance gains.

### Trend 5: LLM Inference Workload is Reshaping Memory Architecture Priorities

Pre-2024 memory architecture prioritized training workloads: high bandwidth, large capacity, sequential access. LLM inference in 2025-2026 adds new requirements:
- **Extremely long contexts (100K-1M tokens)**: KV cache grows linearly with context length, requiring either massive HBM capacity or CXL offload
- **Low batch size decoding**: Highly bandwidth-bound, not FLOPS-bound
- **Attention memory access**: Irregular, non-sequential — benefits from many parallel channels (32 in HBM4)
- **Weight loading per token**: Every token decode reads entire model once — pure bandwidth sensitivity

The AMD MI400's 432 GB vs Vera Rubin's 288 GB per GPU reflects this exactly: AMD is targeting the long-context inference market where model + KV cache exceeds 288 GB.

---

## Manufacturing Implications

### HBM4 Manufacturing Complexity

HBM4 manufacturing involves more process steps than any previous DRAM product:

1. **DRAM die fabrication**: 1c/1γ node (6th-gen 10nm-class), extreme precision required for bitline capacitor and access transistor
2. **Base die fabrication**: TSMC 12nm (SK Hynix) or SF4/Samsung Foundry 4nm (Samsung) — separate foundry engagement
3. **Die preparation**: Thinning to ~50µm per layer for 12-16 layer stack height management
4. **TSV drilling**: Through-silicon vias connecting all dies, pitch <50µm
5. **Stacking/bonding**: TCB (current) or hybrid bonding (HBM4E); alignment to <1µm
6. **Base die attachment**: Logic die bonded to memory stack
7. **Encapsulation**: Molding compound around the entire stack

Each step compounds yield loss. A 12-die stack where each die has 98% yield has a stack yield of 0.98^12 = 78.5%. This is why HBM per-GB cost is 5-8x higher than standard DDR5 — the stacking process is inherently low-yield compared to single-die products.

### Hybrid Bonding Yield Challenges

Hybrid bonding requires:
- Sub-0.5µm alignment accuracy (wafer-to-wafer or die-to-wafer)
- Copper pad surface roughness <1nm RMS
- Oxide surface cleanliness at atomic level
- Precise temperature/pressure control during bonding anneal

Industry yield for hybrid bonding in volume production (3D NAND) is now >90% for established processes. Applying this to HBM is harder due to the requirement for KGD (Known Good Die) testing before stacking — you cannot bond a defective die that will void the entire stack. HBM4E's adoption of hybrid bonding in 2027 is conditional on achieving acceptable yield with KGD screening.

### TSMC 2nm (N2) Production Ramp

N2's 38 Mb/mm² SRAM density is not just an academic metric — it directly affects the economics of AI chips:
- A 100 mm² GPU compute tile with 40% SRAM area can now hold 15.2 Mb vs previous-generation equivalents
- Higher SRAM density reduces the frequency with which compute units stall waiting for HBM data (larger on-chip cache absorbs more of the working set)
- N2P (2026) and A16 (H2 2026) extend these gains with backside power delivery, reducing power delivery resistance overhead

### 3D NAND at 400 Layers: The Aspect Ratio Limit

Vertical holes through 400 layers of silicon oxide/nitride require etching aspect ratios of approximately 80:1 (400 layers × ~10nm per layer / ~50nm hole diameter). This is at the practical limit of plasma etching. The industry's solution: hybrid bonding separates the NAND into two ~200-layer "decks" bonded together, halving the required etch aspect ratio. This is why hybrid bonding is the enabling technology for 400-layer and beyond — not merely an optimization.

---

## Scalability Considerations

### HBM Scalability Limits

**Interface width**: HBM4 doubled to 2,048 bits. HBM5 cannot simply double again to 4,096 bits without prohibitive die area for the interface. The next scaling vector must be either: (a) higher pin speeds beyond 16 Gbps (HBM4E territory), (b) more stacks per package, or (c) architectural changes like compute-near-memory to reduce transfer frequency.

**Layer count**: 12-Hi HBM4 (36 GB, 3 Gb × 12). 16-Hi HBM4 (48 GB). HBM4E targets 48 GB at 16-Hi. Beyond 16-Hi, thermal and yield constraints become binding. Hybrid bonding enables thinner dies (potentially 20-24 layer stacks) but yield challenges scale with layer count.

**Stack count per package**: NVIDIA uses 8, AMD uses 12. Beyond 12, package substrate area becomes limiting. 2.5D CoWoS-S (standard interposer) supports up to ~8 stacks. CoWoS-L (local Si interconnect, used by AMD) enables more but increases substrate cost and complexity.

**Bandwidth per GPU asymptote**: Current trajectory suggests GPU HBM bandwidth reaches ~32 TB/s (8 HBM4E stacks at 4 TB/s) by 2027. The memory bandwidth growth rate of ~2x per HBM generation (2-year cadence) can continue through HBM4E but will face physics limits in the HBM5 generation.

### CXL Scalability

CXL 4.0 at 128 GT/s enables 1.5 TB/s bundled ports. PCIe 8.0 (256 GT/s) is in early research, suggesting CXL 5.0 could reach 3 TB/s per port in 2028-2029. The coherency protocol overhead at large pool scales (100+ TB) may become the next CXL scalability bottleneck — not the raw bandwidth but the latency of maintaining coherency across thousands of nodes.

### SRAM Scalability Beyond N2

TSMC N2 at 38 Mb/mm² is the highest reported. N2P adds ~5% more. A16 (backside power, 2026) improves power delivery but may not provide direct SRAM density increase. Below A16, 1.4nm-class nodes (A14, projected 2028) would be required for further SRAM scaling — and it is not guaranteed that GAA architecture alone can continue to shrink SRAM bit cells beyond A16 without additional innovations (potentially vertical SRAM or alternative cell structures).

### 3D DRAM Research Scalability

imec's IGZO 2T0C DRAM represents a fundamentally scalable architecture: 3D stacking of IGZO layers (similar to 3D NAND) could theoretically enable 64+ layer DRAM with high density. The scalability challenge is the OFF-current of IGZO (must be <10 fA/µm for adequate retention at elevated temperatures), which is extremely difficult to maintain as device dimensions shrink.

---

## Strategic Insights

### Insight 1: The HBM Supply Chain is a Geopolitical Asset

SK Hynix (62% share), Samsung (22% share), and Micron (21% share) represent a near-total oligopoly in HBM. All three are closely tied to US-aligned supply chains (SK Hynix and Samsung are South Korean; Micron is American). TSMC's 12nm process for SK Hynix's HBM4 base die adds another US-aligned supply chain node. Chinese vendors (CXMT, YMTC) have no viable HBM production capability as of 2026. This creates a structural dependency of global AI infrastructure on a three-company, US/Korea supply chain that is simultaneously a concentration risk and a strategic asset.

### Insight 2: Samsung's SF4 Base Die Bet is High-Risk, High-Reward

Samsung's decision to manufacture its HBM4 base die on Samsung Foundry 4nm (SF4) — rather than outsourcing to TSMC like SK Hynix — creates a vertically integrated manufacturing advantage IF Samsung Foundry's yield and performance are competitive. Samsung's HBM4 achieving 13 Gbps (vs SK Hynix's 11.7 Gbps) supports the thesis that SF4 base die outperforms TSMC 12nm for I/O performance. If this holds through HBM4E, Samsung could erode SK Hynix's performance leadership by leveraging its own foundry technology.

### Insight 3: CXL 4.0's Impact on DRAM Demand May Be Non-Linear

CXL memory pooling enables memory disaggregation — instead of each server needing X GB of locally attached DRAM, a rack of servers shares a CXL pool of N×X GB. This could simultaneously: (a) increase total DRAM units shipped (memory utilization improvement reduces waste → demand increases), OR (b) decrease total DRAM per server (pooling reduces per-server provisioning). The net effect on DRAM ASP and volume depends on the adoption pace and workload mix — a key uncertainty for DRAM vendor revenue forecasting in 2027+.

### Insight 4: The LPDDR6-PIM Standard Could Disrupt AiMX Economics

SK Hynix's AiMX is currently differentiated hardware (PCIe card with custom GDDR6-AiM chips) that commands premium pricing. If LPDDR6-PIM is standardized by JEDEC and adopted by Samsung and SK Hynix alike as a commodity module, the PIM market transitions from high-margin differentiated product to commodity — potentially accelerating adoption but compressing margins. The strategic tension for SK Hynix: maximize AiMX margins now while advocating for standard adoption.

### Insight 5: 3D DRAM (IGZO) Timeline is Being Systematically Advanced

The presence of two independent groups (imec and Kioxia) presenting 3D DRAM oxide-semiconductor results at IEDM 2025, combined with Yole Intelligence adding 2T0C IGZO DRAM to its official roadmap, signals that the technology has crossed an academic threshold. These are no longer exploratory papers — they are process development papers with production-intent metrics (aspect ratio, reliability lifetime, device uniformity). The 5-10 year timeline to production readiness is aggressive but not implausible given 3D NAND's similar development arc.

### Insight 6: GDDR7 48 Gbps Creates a New "Mid-Range Inference" Tier

SK Hynix's 48 Gbps GDDR7 (192 GB/s per chip) at ISSCC 2026 targets "mid-range inference AI" (per the paper title). With 12 GDDR7 chips on a high-end discrete GPU, system bandwidth approaches 2.3 TB/s — comparable to initial HBM4 specs but at dramatically lower cost. This creates a viable memory architecture for inference workloads that do not require HBM4's premium: edge datacenters, on-premise AI servers, and automotive inference applications where HBM4's cost is prohibitive.

---

## Open Questions

1. **Samsung SF4 HBM4 base die yield**: Can Samsung Foundry's 4nm process achieve competitive yield for HBM4 base dies at volume? Vendor-reported 13 Gbps is impressive but yield/cost data is unavailable.

2. **LPDDR6-PIM JEDEC timeline**: Will JEDEC approve LPDDR6-PIM in 2026 as expected, or will disagreements between Samsung and SK Hynix on specific circuit implementations delay the standard?

3. **HBM4E hybrid bonding yield**: At what layer count and what KGD screening cost does hybrid bonding for HBM stacking become economically viable at HBM production volumes (tens of millions of stacks per year)?

4. **CXL 4.0 latency at scale**: What is the actual latency penalty for CXL-attached memory in the context of 100+ TB coherent pools with thousands of endpoints? The 3.8x speedup vs 200G RDMA is encouraging but measured at small scale.

5. **IGZO 2T0C DRAM OFF-current at temperature**: Can IGZO DRAM maintain adequate data retention at 85-95°C junction temperature as feature sizes shrink below 50nm? The 1.2V / 5-year / 95°C result from imec is for current prototype dimensions.

6. **AMD MI400 software ecosystem**: Can AMD ROCm mature sufficiently in 2026 to attract enterprise customers away from NVIDIA's CUDA ecosystem, enabling MI400's 432 GB / 19.6 TB/s architecture to be competitive beyond capacity-constrained inference?

7. **DDR6 consumer timing**: JEDEC standard expected Q4 2025–Q1 2026, but consumer products delayed to 2027. What is causing the platform validation delay — is it Intel/AMD platform complexity, or controller/PHY design issues?

8. **HBM5 interface architecture**: If HBM4 doubled interface width to 2,048-bit and HBM4E increases pin speed to 16 Gbps, what is the HBM5 architectural path? A further doubling to 4,096-bit would be impractical. Is die stacking within the package (3D HBM) the solution?

9. **CXL vs NVLink competition**: As CXL 4.0 enables low-latency coherent interconnects, does it start to compete with proprietary GPU-to-GPU interconnects like NVLink? What is the long-term architecture of AI compute fabric — open CXL or proprietary NVLink?

10. **FeRAM reliability lifetime**: HfO2-based FeFET devices show wake-up effects and fatigue after repeated cycling. What are the practical endurance limits for FeRAM used in on-device AI inference inference scenarios (billions of inference cycles per device lifetime)?

---

## Source Index

| # | Source | Publication / Venue | Date | URL |
|---|--------|---------------------|------|-----|
| 1 | SK Hynix 48GB HBM4 at CES 2026 | Tweaktown | 2026-01 | https://www.tweaktown.com/news/109572 |
| 2 | Samsung/SK Hynix HBM4 Production Acceleration | DigiTimes | 2025-12-26 | https://www.digitimes.com/news/a20251226PD223 |
| 3 | SK Hynix HBM4 2,048-bit, 10 GT/s | Tom's Hardware | 2025-11 | https://www.tomshardware.com/pc-components/dram/sk-hynix-completes-development-of-hbm4 |
| 4 | SK Hynix 16-Hi 48GB HBM4 at CES 2026 | TechPowerUp | 2026-01 | https://www.techpowerup.com/344834 |
| 5 | Samsung HBM4 3.3 TB/s | Windows Report | 2026-02 | https://windowsreport.com/samsungs-hbm4-delivers-3-3-tb-s-bandwidth |
| 6 | Samsung HBM4 Mass Production | VideoCardz | 2026-02 | https://videocardz.com/newz/samsung-begins-hbm4-mass-production |
| 7 | ISSCC 2026 HBM4/LPDDR6/GDDR7 Preview | Tweaktown | 2025-12 | https://www.tweaktown.com/news/109057 |
| 8 | ISSCC 2026 SemiAnalysis Coverage | SemiAnalysis | 2026-02 | https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo |
| 9 | Micron HBM4 High-Volume Production | Micron IR | 2026-04 | https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin |
| 10 | Micron HBM4 2.3x BW | Tom's Hardware | 2026-04 | https://www.tomshardware.com/pc-components/dram/micron-enters-high-volume-production-of-hbm4 |
| 11 | SK Hynix HBM Market Share 62% | Astute Group | 2026-01 | https://www.astutegroup.com/news/general/sk-hynix-holds-62-of-hbm |
| 12 | HBM Landscape 2026 | PatSnap | 2026-01 | https://www.patsnap.com/resources/blog/articles/hbm-technology-landscape-2026 |
| 13 | NVIDIA Vera Rubin NVL72 | NVIDIA Official | 2026-01 | https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/ |
| 14 | AMD Instinct MI400 432GB HBM4 | VideoCardz | 2025-11 | https://videocardz.com/newz/amd-launches-instinct-mi350-series-confirms-mi400-in-2026 |
| 15 | JEDEC LPDDR6 JESD209-6 | JEDEC Official | 2025-07-09 | https://www.jedec.org/news/pressreleases/jedec-releases-new-lpddr6-standard |
| 16 | Samsung LPDDR6 10.7 Gbps 12nm | TrendForce | 2025-11-10 | https://www.trendforce.com/news/2025/11/10/news-samsung-lpddr6-memory-specs |
| 17 | SK Hynix LPDDR6 14.4 Gbps | VideoCardz | 2025-12 | https://videocardz.com/newz/sk-hynix-details-16gb-lpddr6-at-14-4gbps |
| 18 | Samsung LPDDR6 CES 2026 | VideoCardz | 2026-01 | https://videocardz.com/newz/samsung-confirms-lpddr6-memory-with-10-7-gbps-bandwidth-at-ces-2026 |
| 19 | JEDEC LPDDR6 Roadmap / Data Center | JEDEC Official | 2025 | https://www.jedec.org/news/pressreleases/jedec-previews-lpddr6-roadmap |
| 20 | CXL 4.0 Release SC25 | BusinessWire | 2025-11-18 | https://www.businesswire.com/news/home/20251118275848 |
| 21 | CXL 3.0 Memory Pooling 2026 | Colobird | 2026 | https://www.colobird.com/blogs/cxl-3-memory-pooling-dedicated-servers/ |
| 22 | SC25 XConn/MemVerge CXL LLM | Storage Newsletter | 2025-11-21 | https://www.storagenewsletter.com/2025/11/21/sc25-xconn-technologies |
| 23 | CXL 4.0 Infrastructure Guide | Introl Blog | 2025 | https://introl.com/blog/cxl-4-0-infrastructure-planning-guide-memory-pooling-2025 |
| 24 | Memory Bottleneck LLM Challenge | Winbuzzer | 2026-01-26 | https://winbuzzer.com/2026/01/26/memory-bottleneck-llm-inference-hardware-challenge |
| 25 | Processing-in-DRAM arXiv | arXiv 2412.19275 | 2024-12 | https://arxiv.org/pdf/2412.19275 |
| 26 | Samsung/SK Hynix PIM for AI | DigiTimes | 2025-12-18 | https://www.digitimes.com/news/a20251218PD206 |
| 27 | SK Hynix AiMX for Generative AI | SK Hynix Newsroom | 2025 | https://news.skhynix.com/sk-hynix-debuts-first-gddr6-aim-accelerator-card-aimx |
| 28 | GDDR6-AiM 16x Acceleration | Tom's Hardware | 2022-2025 | https://www.tomshardware.com/news/sk-hynix-next-generation-ai-accelerator |
| 29 | TSMC N2 SRAM Breakthrough | Tom's Hardware | 2025 | https://www.tomshardware.com/tech-industry/sram-scaling-isnt-dead-after-all |
| 30 | Intel, TSMC SRAM 2nm | SemiEngineering | 2025 | https://marklapedus.substack.com/p/intel-tsmc-tout-sram-breakthroughs |
| 31 | Marvell Hot Chips 2025 | ServeTheHome | 2025-08 | https://www.servethehome.com/marvell-shows-dense-sram-custom-hbm |
| 32 | Hot Chips 2025 Overview | Design News | 2025-08 | https://www.designnews.com/semiconductors-chips/hot-chips-2025 |
| 33 | IEDM 2025 Kioxia 3D DRAM | IEDM Program | 2025-12 | https://iedm25.mapyourshow.com/8_0/sessions/session-details.cfm?ScheduleID=210 |
| 34 | imec IGZO DRAM | imec Official | 2025 | https://www.imec-int.com/en/articles/disrupting-dram-roadmap-capacitor-less-igzo-dram-technology |
| 35 | IEDM 2025 Report | Vik's Newsletter | 2025-12 | https://www.viksnewsletter.com/p/2025-international-electron-devices |
| 36 | Samsung Hybrid Bonding HBM4 | Tom's Hardware | 2025-2026 | https://www.tomshardware.com/pc-components/dram/samsung-to-adopt-hybrid-bonding-for-hbm4 |
| 37 | Samsung vs SK Hynix Hybrid Bonding | Benzinga | 2026-04 | https://www.benzinga.com/markets/tech/26/04/51655835 |
| 38 | DDR6 Explained | IntuitionLabs | 2025-12 | https://intuitionlabs.ai/articles/ddr6-explained-speed-architecture |
| 39 | DDR6 Samsung/Micron/SK Hynix Plans | Guru3D | 2025 | https://www.guru3d.com/story/samsung-micron-sk-hynix-ddr6-development-plans |
| 40 | SK Hynix SOCAMM2 192GB | SK Hynix Newsroom | 2026 | https://news.skhynix.com/mass-production-socamm2-192gb/ |
| 41 | SOCAMM Memory Data Center | Network World | 2025 | https://www.networkworld.com/article/4112926/socamm-memory-gains-ground |
| 42 | Samsung HBM4E GTC 2026 | WCCFTech | 2026-03 | https://wccftech.com/samsung-hbm4e-memory-up-to-4-tbps-bandwidth |
| 43 | Rambus HBM4E Controller | WCCFTech | 2026 | https://wccftech.com/rambus-hbm4e-memory-controller-60-percent-faster-vs-hbm4 |
| 44 | SK Hynix 48 Gbps GDDR7 | TrendForce | 2025-11-27 | https://www.trendforce.com/news/2025/11/27/news-ai-memory-showdown |
| 45 | Samsung 24Gb GDDR7 Production | Samsung Newsroom | 2025 | https://news.samsung.com/global/samsung-develops-industrys-first-24gb-gddr7 |
| 46 | Samsung V10 NAND 400-Layer | TrendForce | 2024-10 | https://www.trendforce.com/news/2024/10/29/news-samsung-reportedly-plans-400-layer |
| 47 | Kioxia BiCS10 332-Layer Expedited | Tom's Hardware | 2025-2026 | https://www.tomshardware.com/pc-components/ssds/kioxias-next-gen-3d-nand |
| 48 | Micron 1-Gamma Node 2026 | HardForum | 2026 | https://hardforum.com/threads/micron-sets-1g-as-mainstream-node |
| 49 | TSMC A16 GAA + Backside Power | SemiAnalysis | 2025 | https://newsletter.semianalysis.com/p/clash-of-the-foundries |
| 50 | NVM Technology Progress | MRS Communications | 2024-2025 | https://link.springer.com/article/10.1557/s43579-024-00660-2 |
| 51 | Analog CiM Landscape 2026 | PatSnap | 2026 | https://www.patsnap.com/resources/blog/articles/in-memory-analog-computing-landscape-2026 |
| 52 | HBM4 Memory Supercycle | Introl Blog | 2026 | https://introl.com/blog/south-korea-hbm4-stargate-memory-supercycle-2026 |
| 53 | HBM Evolution HBM3→HBM4 | Introl Blog | 2025 | https://introl.com/blog/hbm-evolution-hbm3-hbm3e-hbm4-memory-ai-gpu-2025 |
| 54 | Disaggregated Architectures arXiv | arXiv 2511.04104 | 2025-11 | https://arxiv.org/html/2511.04104v1 |
| 55 | Memory Wall / Supercycle | TrendForce | 2025-2026 | https://www.trendforce.com/insights/memory-wall |
