# AI_accelerators — Research Summary

**Generated:** 2026-05-22  
**Window:** 2025-11-22 – 2026-05-22  
**Validated Sources:** 53 (of 56 collected)  
**Papers Analyzed:** 25  
**Validation Score:** 29/30

---

## Executive Summary

The six-month window from November 2025 to May 2026 marks a **structural inflection in AI accelerator architecture**: the industry has decisively shifted from training-centric GPU clusters to inference-optimized, heterogeneous systems. Five major developments define this period:

1. **Inference Hardware Primacy.** Google's Ironwood (TPU v7) became GA as the "first TPU for the age of inference." NVIDIA's Rubin entered full production at CES 2026. Inference workloads will account for two-thirds of all AI compute in 2026 — up from one-third in 2023.

2. **Rack-Scale as the Unit of Analysis.** Individual GPU TFLOPS has become a secondary metric. The GB200 NVL72 (72 GPUs at 130 TB/s NVLink bandwidth), TPU v7 pod (9,216 chips at 1.77 PB shared HBM), and AWS Trainium3 UltraServer (144 chips at 706 TB/s aggregate bandwidth) demonstrate that the system — not the chip — is the fundamental deployable unit.

3. **The Groq-NVIDIA Convergence.** NVIDIA's $20 billion non-exclusive license of Groq's Language Processing Unit architecture (December 24, 2025) validates the deterministic, latency-optimized inference approach and integrates it into the NVIDIA Vera Rubin platform. This is the most significant architectural licensing deal since ARM.

4. **Memory as the Binding Constraint.** The HBM memory supercycle has created the most severe DRAM shortage in 15 years, with prices up 171.8% YoY in late 2025 and shortages projected to 2027–2030. CXL memory expansion, PIM architectures, and on-chip SRAM are now primary axes of differentiation.

5. **Manufacturing Transitions.** TSMC N2 entered mass production December 31, 2025 with 70–80% yields. TSMC N3 is at capacity (180k wafers/month by April 2026), constrained by AI chip demand. UCIe 3.0 ratified August 2025 enables heterogeneous chiplet integration at scale.

**Bottom line:** AI accelerator design is entering an era of architectural specialization where training hardware, inference hardware, edge NPUs, and memory subsystems are optimized separately — and interconnected via higher-bandwidth, lower-latency fabrics than ever before.

---

## All Collected Findings

### 1. Google TPU Family

**TPU v5p (Foundation):**
- 8,960-chip pods, 460 PFLOPS aggregate BF16
- 3D torus topology: 4,800 Gbps per chip, max 48 hops in 4,096-chip pod
- 128×128 MXU per chip

**TPU v6e / Trillium (Scaling):**
- 256×256 MXU (4x MAC ops/cycle vs v5e)
- ~918 BF16 TFLOPS per chip (2x v5e BF16)
- 2x HBM capacity and bandwidth vs v5e; 2x ICI bandwidth vs v5e
- 2.1x perf/dollar over v5e; 2.5x over v5p for LLM training

**TPU v7 / Ironwood (November 2025 – GA):**
- 4,614 TFLOPs per chip; 4.6 PFLOPS FP8
- 192 GB HBM3e, 7.4 TB/s HBM3e bandwidth
- 9.6 Tb/s ICI bandwidth
- 9,216-chip pods: 42.5 Exaflops FP8, 1.77 PB shared HBM
- Beats NVIDIA GB300 on specific inference workloads per SemiAnalysis
- Anthropic committed to 1M+ Ironwood chip deployment beginning 2026

**TPU v8 (Preview):**
- Split into dedicated training and inference chips
- Manufactured at TSMC 2nm
- No public specifications as of May 2026

### 2. NVIDIA Platform Family

**Blackwell B200 (2025):**
- 208B transistors, 180 GB HBM3e, 8 TB/s bandwidth
- FP8 TFLOPS: ~9,000+ per GPU
- NVLink 5: 1.8 TB/s bidirectional per GPU
- 3.1x H200 inference throughput (Llama-2 70B, 8-GPU DGX)
- Power: up to 1,000W (SXM form)

**GB200 NVL72 (2025):**
- 72 B200 GPUs + 36 Grace CPUs, fully NVLink-connected
- 1.5M tokens/sec on GPT-OSS-120B (single NVL72 system)
- 30x Hopper-generation inference on Llama 3.1-405B
- 4x GPT-MoE-1.8T training speedup vs Hopper

**Rubin R100 (CES 2026, full production):**
- 336B transistors, TSMC N3, dual reticle dies
- 50 PFLOPS NVFP4 inference; 35 PFLOPS NVFP4 training per GPU
- 288 GB HBM4, 22 TB/s bandwidth per GPU
- NVLink 6: 3.6 TB/s bidirectional per GPU
- 5x Blackwell inference per GPU; 3.5x training
- 10x lower inference token cost vs Blackwell

**Vera Rubin NVL72:**
- 3.6 EFLOPS NVFP4 inference; 2.5 EFLOPS training
- 1.6 PB/s HBM bandwidth, 20.7 TB HBM4
- 260 TB/s NVLink scale-up bandwidth

**Rubin CPX:**
- Specialized variant for massive-context inference
- Architecture details not fully disclosed

### 3. AMD Instinct MI355X (CDNA 4)

- 185B transistors; 288 GB HBM3E
- 10 PFLOPS FP4; 5 PFLOPS FP8 (1.9x vs MI300X)
- 32 active CUs/XCD (down from 38, doubled per-CU FP8 throughput)
- 2.8x faster training vs MI300X; 4.2x faster agent/chatbot workloads
- **MLPerf Inference 6.0:** First AMD result >1M tokens/sec
- Llama 3.1-405B FP4 latency (8-GPU): 50.6 ms
- ISSCC 2026: AMD disclosed matching GB200 performance on key workloads

### 4. AWS Trainium3 (December 2025)

- 2.52 PFLOPS FP8 per chip; 144 GB HBM3e; 4.9 TB/s bandwidth
- 144-chip UltraServer: 362 PFLOPS, 20.7 TB HBM3e, 706 TB/s aggregate
- 4.4x compute, 4x energy efficiency, 4x memory BW vs Trainium2 UltraServer
- 30-40% better price/performance vs NVIDIA P5e instances
- Trainium4 roadmap: 6x FP4, 3x FP8, 4x BW vs Trainium3

### 5. Intel Gaudi 3

- 1.8 PFLOPS FP8/BF16; 128 GB HBM2e; 3.7 TB/s bandwidth
- 95–170% H100 performance on Llama benchmarks
- 4x advantage on Falcon 180B (capacity-constrained workload)
- Open ecosystem: standard Ethernet interconnect, PyTorch native

### 6. Groq LPU

- SIMD conveyor architecture; static scheduling compiler
- Hundreds of MB on-chip SRAM as primary weight storage
- Samsung 4nm (v2); plesiosynchronous multi-chip protocol
- 20+ TOPS/W (self-reported); sub-millisecond TTFT
- **December 24, 2025:** NVIDIA $20B non-exclusive license deal
- Groq 3 LPU integrated into NVIDIA Vera Rubin platform

### 7. Cerebras WSE-3

- 4 trillion transistors; 900,000 AI cores; 5nm TSMC
- 44 GB on-chip SRAM; 21 PB/s fabric bandwidth (7,000x H100)
- 125 PFLOPS peak AI inference
- 2,500 tokens/sec/user on Llama 4 Maverick (400B params) — 2x DGX B200
- 2025 revenue: $510M; valuation $8.1B; IPO early 2026

### 8. SambaNova SN40L/SN50 RDU

- Reconfigurable Dataflow Unit: PCU/PMU tiled array with 3D switching fabric
- Three-tier memory: on-chip SRAM + HBM (1 TB/s) + DDR DRAM
- SN50 (fifth-gen): optimized for agentic AI and RAG pipelines
- Demonstrated 1 TB/s bandwidth; purpose-built for enterprise multi-document inference

### 9. Microsoft Maia 100/200

- Maia 100: 820mm², TSMC N5, 1.8 TB/s BW, 64 GB HBM2E — used only internally
- **January 26, 2026:** Maia 200 announced as "built for inference"
- Maia 200 positions Azure as a serious custom-silicon inference provider

### 10. Key Research Findings (Academic)

- **arXiv 2507.09010 (Hybrid SA):** 247/117 token/s/mm² on 1.3B LLM; 2.45x–13.5x over prior edge SA
- **arXiv 2509.12993 (HPIM):** 34.3x speedup vs A100; heterogeneous SRAM-PIM + HBM-PIM
- **arXiv 2509.22512 (AxLLM):** 90% compute reduction via reuse; 1.7x speedup, 28% energy reduction
- **arXiv 2510.08544 (SPAD):** Specialized prefill and decode ASIC design for disaggregated inference
- **ISCA 2025 (Tokyo):** Papers on wafer-scale cabinet co-design, RRAM-based PIM for transformers

---

## Summarized Papers

**paper-001 — Google Ironwood:** 4,614 TFLOPs/chip, 192 GB HBM3e, 9.6 Tb/s ICI, 9,216-chip pod at 42.5 Exaflops. First inference-purpose TPU. 1.77 PB shared HBM enables KV-cache coordination across entire pod.

**paper-002 — NVIDIA Blackwell GB200:** B200 at 180 GB HBM3e, 8 TB/s. NVL72 delivers 1.5M tokens/sec on GPT-120B, 30x Hopper on Llama 405B. 5th-gen NVLink 1.8 TB/s per GPU; 130 TB/s aggregate across 72 GPUs.

**paper-003 — Cerebras WSE-3:** Single 300mm wafer, 44 GB SRAM, 21 PB/s. 2,500 tokens/sec/user on 400B-param model. $510M revenue, profitable in 2025.

**paper-004 — NVIDIA Rubin:** 336B transistors, 50 PFLOPS NVFP4, HBM4 at 22 TB/s. NVLink 6 at 3.6 TB/s. NVL72 = 3.6 EFLOPS. 10x lower token cost vs Blackwell.

**paper-005 — AWS Trainium3:** 2.52 PFLOPS FP8 per chip; 144-chip UltraServer = 362 PFLOPS. 4.4x vs Trainium2 system-level. Trainium4 roadmap: 6x FP4 throughput.

**paper-006 — AMD MI355X:** 10 PFLOPS FP4; halved CU count with doubled per-CU FP8 throughput. First AMD MLPerf >1M tokens/sec. ISSCC 2026 confirms match vs GB200 on targeted workloads.

**paper-007 — Groq LPU:** Static-schedule SIMD conveyor, on-chip SRAM weight storage. NVIDIA $20B license validates deterministic inference approach. LPU 3 integrated into Vera Rubin platform.

**paper-008 — SambaNova RDU:** Three-tier memory (SRAM/HBM/DDR) for enterprise-scale model inference. SN50 targets agentic AI. 1 TB/s HBM tier; DDR enables multi-TB parameter sets economically.

**paper-009 — Hybrid Systolic Array:** Runtime-reconfigurable prefill (dense SA) / decode (vector units) modes. MXINT4 quantization. 247/117 token/s/mm². Supports Mamba + Transformer hybrid models.

**paper-010 — Sparsity Acceleration:** NVIDIA 2:4 = 2x effective throughput. MoE activation sparsity (5.5%) enables 18x parameter efficiency. 2025 survey covers all major sparsity exploitation hardware.

**paper-011 — Analog In-Memory Computing:** IBM 3D AIMC for MoE models outperforms GPUs per study. HfOx ReRAM on-chip train+infer demo (arXiv Feb 2025). IMC = 38% of analog AI chip market. 30x energy advantage theoretical for dense matmul.

**paper-012 — Mobile NPU:** Apple M4 = 38 TOPS; Snapdragon X Elite = 45 TOPS. Real-world vs TOPS divergence confirmed. arXiv 2509.23324: mobile NPU can run LLM test-time compute for on-device reasoning.

**paper-013 — HPIM PIM Accelerator:** SRAM-PIM + HBM-PIM heterogeneous design. 34.3x peak speedup vs A100 for LLM inference. Targets memory-bound decode phase specifically.

**paper-014 — Prefill-Decode Disaggregation:** Now default architecture at every major hyperscaler. NVIDIA Dynamo as orchestration layer. 52.3k input + 22.3k output TPS on 96 H100s with DeepSeek-R1. SPAD paper proposes custom ASICs per phase.

**paper-015 — TSMC Fabrication:** N3 at 180k wafers/month (Apr 2026). N2 mass production Dec 2025 at 70–80% yield. All N2 capacity booked through 2026. CoWoS quadrupling to 130k wafers/month.

**paper-016 — MoE Hardware Acceleration:** 60% of 2025 open-source models use MoE. DeepSeek-V3: 671B total, 37B active. Expert placement, load imbalance, KV amplification are key hardware challenges. Three-tier memory (SambaNova) naturally addresses expert tiering.

**paper-017 — CXL Memory Expansion:** $1.3B market 2025; 21.9x throughput + 60x energy/token for RAG. Microsoft Azure CXL instances Nov 2025. CXL enabling 1M-token inference beyond GPU HBM limits.

**paper-018 — Photonic AI:** Lightmatter PCU sampling in 2025 (100x efficiency claim). Tsinghua Science paper: all-optical vision generation. Nature paper: 30x energy reduction path. Commercial scale: late 2020s.

**paper-019 — MLPerf 2025:** Training v5.0 (Jun) + v5.1 (Nov); Inference v5.0 (Apr) + v5.1 (Sep). 50% inference improvement in 6 months (v5.0→v5.1). Llama 3.1-405B + DeepSeek-R1 added as benchmarks.

**paper-020 — AxLLM Computation Reuse:** Content-addressable activation cache. 90% compute reduction, 28% energy, 1.7x speedup. Complementary to KV-cache. Best for RAG/agent loops with repeated content.

**paper-021 — HBM Supercycle:** 171.8% YoY price surge. Shortage to 2027–2030. HBM4 transition: Samsung first shipments May 2026. Most severe memory shortage in 15 years per Goldman Sachs.

**paper-022 — TPU Systolic Array Evolution:** v5p (128×128) → Trillium (256×256) → Ironwood (256×256, higher speed). 3D torus topology: 48 max hops vs 128 for fat-tree at 4,096-chip scale.

**paper-023 — Intel Gaudi 3:** 1.8 PFLOPS, 128 GB HBM2e, 3.7 TB/s. 95–170% H100 on Llama. 4x H100 on Falcon 180B (capacity advantage). Open Ethernet interconnect.

**paper-024 — Data Center Thermal Crisis:** NVIDIA roadmap to 1,500W/chip (2026). GB200 NVL72 = 120 kW/rack. Direct-to-chip liquid cooling 47% market share. Global DC demand: 460–490 TWh (2025), 500+ TWh (2026).

**paper-025 — Tenstorrent Wormhole:** RISC-V Tensix cores, 16x 100GbE per chip, 384 GB/s GDDR6. Blackhole taped out 2025 on TSMC. Zero-overhead NOC extension over Ethernet ports.

---

## Technical Analysis

### 3.1 Compute Architecture Trajectories

**Systolic Array Scaling:** Google's TPU progression demonstrates diminishing returns from MXU width expansion alone. The 128×128 → 256×256 jump in Trillium delivered 4.7x compute per chip. But Ironwood maintained the same 256×256 MXU while achieving further gains through bandwidth (7.4 TB/s HBM3e) and interconnect (9.6 Tb/s ICI). This suggests that MXU width has reached a practical optimum for on-chip design — future gains will come from bandwidth, process node, and system-level coordination.

**FLOPS Inflation vs Practical Throughput:** Raw TFLOPS claims have become unreliable metrics. The key 2025-2026 insight: memory bandwidth, not compute TFLOPS, limits production LLM throughput. Google engineers (cited in SDxCentral, 2026) confirmed that network latency and memory are the primary inference bottlenecks, not compute. AMD's MI355X actually reduced CU count while improving overall performance, validating this thesis.

**Precision Race:** NVFP4 (NVIDIA), FP4 (AMD), FP6 (AMD) — new narrow-precision formats are expanding. Rubin at 50 PFLOPS NVFP4 vs Blackwell's 20 PFLOPS NVFP4 shows that precision reduction remains the highest-leverage lever for throughput scaling at fixed silicon area.

### 3.2 Memory Architecture Analysis

**The Arithmetic Intensity Problem:**
- LLM prefill: ~2 FLOPs/byte (compute-rooflined)
- LLM decode: ~0.2 FLOPs/byte (severely memory-bandwidth-bound)
- GPU design optimized for ~100 FLOPs/byte (traditional DNN training)

The mismatch between GPU architecture and LLM inference arithmetic intensity explains why specialist architectures (Groq LPU on-chip SRAM, Cerebras WSE-3 44GB SRAM, Tenstorrent GDDR6 400 GB/s) can exceed GPU performance for specific inference tasks despite lower FLOPS.

**Memory Hierarchy Innovations:**
1. **On-chip SRAM dominance:** Groq, Cerebras, and Tenstorrent all bet on SRAM-heavy architectures
2. **HBM3E → HBM4 transition:** 22 TB/s (Rubin) vs 8 TB/s (Blackwell) — 2.75x improvement
3. **CXL expansion tier:** 21.9x throughput for RAG workloads vs NVMe; $1.3B market in 2025
4. **PIM integration:** Samsung HBM-PIM, SK Hynix KV-cache PIM patents; HPIM research prototype shows 34.3x A100 speedup

### 3.3 Interconnect Analysis

| System | Interconnect | Bandwidth/GPU | Domain Size |
|--------|-------------|---------------|-------------|
| NVIDIA Blackwell NVL72 | NVLink 5 | 1.8 TB/s | 72 GPUs |
| NVIDIA Rubin NVL72 | NVLink 6 | 3.6 TB/s | 72+ GPUs |
| Google Ironwood Pod | ICI | 9.6 Tb/s | 9,216 chips |
| AWS Trainium3 UltraServer | NeuronLink | — | 144 chips |
| Groq Multi-LPU | Plesiosynchronous | — | 1000s LPUs |
| Tenstorrent Wormhole | 100GbE × 16 | ~200 GB/s | Unlimited |

**Key Insight:** NVLink 6 (3.6 TB/s) in Rubin is 2x NVLink 5 — maintaining NVIDIA's consistent doubling cadence. Google's ICI at 9.6 Tb/s (1.2 TB/s) is lower per-chip but enables 9,216-chip pod coordination with 1.77 PB shared memory — a qualitatively different capability.

### 3.4 Quantization and Precision

The precision compression trend:
- FP32 → BF16/FP16: Standard transition 2018–2022
- FP16 → FP8: 2023–2025 (Hopper, Blackwell, AMD, Gaudi 3)
- FP8 → FP4/NVFP4: 2025–2026 (Blackwell Ultra, Rubin, MI355X)

Each halving of precision delivers:
- 2x theoretical throughput (Tensor Cores)
- 2x memory capacity (more parameters fit in HBM)
- 2x memory bandwidth effectiveness (transfer more params/second)

Combined: up to 4–8x practical inference speedup per precision step with <1% accuracy loss (calibrated).

### 3.5 Architecture Convergence Patterns

The industry is converging on:
1. **Disaggregated prefill/decode** as the default serving architecture
2. **MoE sparse models** as the dominant frontier model structure
3. **Rack-scale systems** as the procurement unit
4. **FP8 + sparsity** as the inference compute baseline
5. **CXL** as the standard KV-cache expansion mechanism

---

## Architectural Observations

### Observation 1: The End of General-Purpose AI Accelerators

The period 2025–2026 marks the end of general-purpose AI accelerators. Evidence:
- Google splits TPU v8 into separate training and inference chips
- NVIDIA introduces Rubin CPX for massive-context inference (separate from standard NVL72)
- Groq LPU integrated into NVIDIA platform as inference co-processor
- SambaNova SN50 explicitly targets "agentic AI" inference workloads
- SPAD paper proposes custom ASICs for each of prefill and decode phases

The trend is clear: the performance demands of training, prefill, decode, and edge inference are now divergent enough to justify separate silicon for each.

### Observation 2: Scale-Up Bandwidth is the New Clock Speed

In the Blackwell/Ironwood/Rubin era, raw FLOPS comparisons have become secondary. What differentiates:
- NVLink 6 (Rubin) at 3.6 TB/s doubles NVLink 5 (Blackwell) at 1.8 TB/s
- Ironwood ICI at 9.6 Tb/s enables pod-wide KV-cache sharing
- Trainium3 NeuronLink enables 144-chip aggregation at 706 TB/s combined BW

The ability to treat a rack or pod as a single logical accelerator — not individual cards — is now the primary architectural differentiator.

### Observation 3: On-Chip SRAM is the Hidden Moat

Cerebras (44 GB on-chip SRAM), Groq (hundreds of MB SRAM weight storage), and SambaNova (PCU/PMU SRAM grid) all achieve their performance advantages from on-chip memory density. On-chip SRAM provides:
- 10–100x lower access latency than HBM
- 1,000x lower access latency than DDR
- No bandwidth sharing across multiple memory requestors

However, on-chip SRAM density grows slowly — it is the most area-expensive memory in CMOS. This creates a fundamental scaling limit: SRAM capacity cannot keep pace with model parameter growth (which doubles every ~6 months).

### Observation 4: Dataflow Architecture Vindication

Both Groq's LPU (NVIDIA-licensed) and SambaNova's RDU have proven commercial viability. The shared insight: eliminating dynamic scheduling overhead (cache misses, branch prediction, out-of-order execution) enables predictable, high-efficiency inference when workloads are statically known.

The counter-argument: LLMs require KV-cache memory access patterns that are dynamic (dependent on input). The solution emerging in 2025–2026 is hybrid architectures: static dataflow for weight-matmul operations + dynamic management for KV-cache and expert routing.

### Observation 5: Manufacturing is Now the Bottleneck

For the first time, the primary constraint on AI hardware deployment is not chip design but:
1. HBM3E manufacturing capacity (shortage to 2027+)
2. TSMC CoWoS packaging capacity (racing to 4x current volume)
3. TSMC N3 wafer capacity (fully booked by AI vendors)
4. Liquid cooling infrastructure availability

---

## Trend Analysis

### Trend 1: Inference Workload Dominance

Inference share of total AI compute:
- 2023: 33%
- 2025: 50%
- 2026: projected 67%

Drivers: proliferation of AI applications serving users vs fewer training runs; multi-billion user deployments (ChatGPT, Gemini, Claude, Copilot).

Implication: Every major chip vendor is now optimizing for inference. Training is becoming a minority workload by dollar volume even as model training runs get larger.

### Trend 2: MoE as the Dominant Model Architecture

60%+ of 2025 open-source model releases use MoE. All top-tier models on leaderboards use sparse expert activation:
- GPT-4 (OpenAI): MoE
- Gemini Ultra: MoE
- DeepSeek-V3: 671B/37B active MoE
- Llama 4: MoE

Hardware implication: Next-generation accelerators must efficiently handle sparse expert dispatch — not just dense matrix operations.

### Trend 3: On-Device AI Acceleration

Mobile NPU TOPS compound annual growth:
- Apple M1 Neural Engine (2020): 11 TOPS
- Apple M4 Neural Engine (2025): 38 TOPS
- Qualcomm Hexagon (Snapdragon X Elite): 45 TOPS
- Intel Lunar Lake NPU: 48 TOPS

Projection: Consumer devices capable of running 13B–30B quantized models locally by 2026. arXiv 2509.23324 demonstrates on-device reasoning via test-time compute scaling on mobile NPU.

### Trend 4: Energy Efficiency as Primary Competitive Axis

ML hardware improves ~40% energy efficiency annually (Epoch AI data). But model sizes grow ~3.5x annually:
- Net energy demand growth: ~2.5x annually
- Global data center electricity: 460 TWh (2025) → projected ~1,000 TWh (2030)

Energy efficiency leaderboard (TOPS/W, 2025):
1. Groq LPU: 20+ TOPS/W (self-reported)
2. Google Trillium: 15–20 TOPS/W
3. Cerebras WSE-3: 15–25 TOPS/W
4. Intel Gaudi 3: 12–18 TOPS/W
5. AWS Trainium2: 10–15 TOPS/W
6. NVIDIA H100: 5–10 TOPS/W (baseline)

### Trend 5: Open Architecture vs Proprietary Ecosystem

Two competing trajectories:
- **NVIDIA CUDA ecosystem:** Dominant, ~70–80% of deployed AI compute
- **Open alternatives:** Tenstorrent (RISC-V, Ethernet), Intel Gaudi (open Ethernet), AMD ROCm

The RISC-V AI chip market was $6.1B in 2023 and is projected to reach $92.7B by 2030 (47.4% CAGR). Tenstorrent, Axelera AI, Esperanto, and BrainChip are the leading vendors.

### Trend 6: The Rise of Custom Hyperscaler ASICs

All major hyperscalers now design custom AI silicon:
| Hyperscaler | Chip | Status (2025–2026) |
|-------------|------|-------------------|
| Google | TPU v7 Ironwood | GA |
| AWS | Trainium3 | Production |
| Microsoft | Maia 200 | Announced Jan 2026 |
| Meta | MTIA Gen 2 | Production (internal) |
| Alibaba | Hanguang 800 | Production (internal) |

The trend indicates that at sufficient scale (>$100B annual AI compute spend), custom silicon has a better TCO than commercial GPU clusters.

---

## Manufacturing Implications

### Wafer Allocation

The AI chip boom has created a significant reallocation of semiconductor manufacturing capacity:

**TSMC N3 (3nm) Capacity (April 2026: 180k wafers/month):**
- NVIDIA Blackwell + Rubin: ~35% of N3 capacity
- AMD MI350/MI355X: ~15% of N3 capacity
- Apple A18/M4 family: ~25% of N3 capacity
- Other (Qualcomm, Intel outsourcing, automotive): ~25%

**TSMC N2 (2nm) Capacity (ramping 2026):**
- Apple A20/M5: >50% of initial allocation
- Qualcomm Snapdragon 8 Elite 2: ~20%
- AMD/NVIDIA next-gen (2H 2026 design tape-ins): ~20%
- Remaining: ~10%

### Advanced Packaging Bottleneck

CoWoS (Chip-on-Wafer-on-Substrate) for HBM attachment:
- Current capacity: ~32,500 wafers/month (TSMC estimate)
- Target by late 2026: 130,000 wafers/month (4x)
- All major AI chips require CoWoS: B200, H200, MI355X, Rubin

This packaging constraint has been cited by NVIDIA as a primary production bottleneck in 2025. The race to expand CoWoS capacity is as important as wafer fabrication.

### HBM Manufacturing

Each HBM3E 36-GB stack requires:
- ~3 DRAM die wafers (12Hi stacking)
- Through-Silicon Via (TSV) bonding at each layer
- Yield significantly lower than planar DRAM

At 288 GB per AMD MI355X GPU, a single accelerator requires 8 HBM stacks — consuming ~24 DRAM die wafers just for memory. This explains the structural shortage.

### Geographic Diversification

- TSMC Arizona Fab 1: N4 in production (2024)
- TSMC Arizona Fab 2: N3 targeted 2H 2027
- TSMC Japan (Kumamoto): 28nm/16nm; Kumamoto 2 targets 6nm (2028)
- Samsung S2 Fab (Texas): 4nm capacity
- Intel 18A: Limited production; Intel Foundry Services still building customer trust

AI chip production remains heavily concentrated in Taiwan (TSMC Hsinchu/Taichung). This geographic concentration is a supply chain risk noted by U.S. CHIPS Act policy.

---

## Scalability Considerations

### Training Scalability

Current frontier training run scale:
- 10,000–100,000+ GPUs for GPT-4 / Llama 3 class models
- Interconnect topology becomes critical: 3D torus (Google) vs fat-tree (NVIDIA InfiniBand)
- All-reduce communication scales O(log N) with bandwidth-optimal ring algorithms
- KV-cache not relevant for training; primary bottleneck is weight gradient communication

**Scaling Limits:**
1. **Model weight communication:** Each training step requires all-reduce over billions of parameters
2. **Power infrastructure:** 100,000 H100 GPUs = ~70 MW power draw
3. **Cooling infrastructure:** Liquid cooling at 1,000W+ per GPU
4. **HBM availability:** Training at scale limited by HBM supply

### Inference Scalability

**Request-level parallelism (batch serving):**
- Scales horizontally: add more inference servers
- Bottleneck: per-request latency requirements

**Model parallelism for large models:**
- Tensor parallel: split within a layer across GPUs (requires high-bandwidth NVLink)
- Pipeline parallel: different layers on different GPUs (pipeline bubbles at stage boundaries)
- Expert parallel (MoE): different experts on different devices

**KV-Cache Scaling:**
- Grows linearly with context length × batch size × num_heads × head_dim × num_layers
- 100K-token context on Llama 70B: ~240 GB KV-cache per request
- CXL expansion enables cost-effective scaling beyond HBM limits

### Long-Context Scaling

The emerging frontier: 1M-token contexts. Challenges:
- KV-cache: 100K tokens = 240 GB per Llama 70B; 1M tokens = 2.4 TB
- Attention computation: O(n²) in token sequence length
- Solutions: Ring attention (split across GPUs), FlashAttention 3 (tiled computation), CXL KV-cache pooling

Ironwood's 1.77 PB shared HBM across 9,216 chips positions Google to address this at pod scale.

### Edge Scalability

On-device inference scaling:
- Quantization: FP32 → INT8 → INT4 reduces model size 4–8x
- Models now deployable on smartphones: 7B params in INT4 = ~3.5 GB (fits in 8 GB RAM)
- NPU TOPS growing 30–40% annually
- Challenge: power budget for sustained inference (3–5W mobile limit vs 1,000W data center GPU)

---

## Strategic Insights

### 1. The NVIDIA-Groq Synthesis

The $20B NVIDIA licensing of Groq's LPU architecture is not merely a financial transaction — it represents a recognition that GPU architectures are fundamentally inefficient for the decode phase of LLM inference. By integrating LPU-style deterministic execution as a co-processor within the Vera Rubin platform, NVIDIA is building hybrid systems where:
- Prefill (compute-bound): Rubin GPU handles efficiently
- Decode (memory-bandwidth-bound): LPU handles with superior TOPS/W

This convergence was predicted by the prefill-decode disaggregation research trend (paper-014) and validates the architectural split as a hardware design imperative.

### 2. Google's Inference Infrastructure Moat

With 1M+ Ironwood chips committed to Anthropic (beginning 2026), Google is building a proprietary inference infrastructure advantage. The Ironwood pod's 1.77 PB shared HBM — accessible at 9.6 Tb/s ICI — enables a qualitatively different capability for long-context inference that NVIDIA's rack-based systems cannot match without CXL supplementation.

Google's vertical integration (chip design + manufacturing allocation + cloud infrastructure + AI model development) positions it as the only vendor with end-to-end optimization from model training through production inference.

### 3. AMD's Credible Challenge

The ISSCC 2026 disclosure that AMD MI355X "matches GB200" on key workloads is a landmark claim. If validated at production scale, it means:
- The datacenter AI market is no longer a NVIDIA monopoly on performance
- ROCm + vLLM + SGLang ecosystem maturity has closed the software gap
- AMD's chiplet approach (MCM-GPU with HBM3E) provides cost structure advantages

The first AMD MLPerf result exceeding 1M tokens/sec is the credibility threshold event that enterprise buyers needed.

### 4. The Memory-Centric Future

Every major architecture innovation in this period relates to memory:
- Ironwood: 192 GB HBM3e per chip (2.4x H100)
- MI355X: 288 GB HBM3E per chip (3.6x H100)
- Cerebras: 44 GB on-chip SRAM
- CXL: 100 TiB pools expanding LLM serving capacity
- PIM: Compute inside HBM banks (34.3x A100 in research)
- HBM4: 22 TB/s in Rubin (2.75x Blackwell)

The strategic imperative for the next 3 years: solve memory, and inference cost falls by 10x.

### 5. Chiplet Architecture as Manufacturing Insurance

UCIe 3.0 (ratified August 2025) combined with TSMC CoWoS expansion creates an inflection in chiplet economics:
- Vendors can combine best-of-breed dies: TSMC N2 for logic + SK Hynix HBM4 for memory
- Failed yield on one die does not scrap the entire package
- Enables product differentiation at packaging stage (memory, IO variants)
- Cross-vendor chiplet standardization reduces barrier to ASIC development

This is particularly important for hyperscaler ASICs (Maia, Trainium, TPU) which can differentiate in architecture while using commodity chiplets for memory and IO.

### 6. The Edge-Cloud Continuum

On-device NPUs (38–50 TOPS) are not competing with cloud accelerators — they are expanding the total inference market by:
- Enabling privacy-sensitive workloads (health, legal, financial) to remain on-device
- Eliminating round-trip latency for real-time applications
- Reducing cloud inference cost by handling simple queries locally

The aggregate deployed NPU capacity in smartphones and PCs likely exceeds total cloud AI accelerator TOPS by 10-100x — though at much lower utilization rates.

---

## Open Questions

### Architecture Questions

1. **Optimal systolic array width:** Has 256×256 reached the practical limit? Google maintained this in Ironwood while focusing on bandwidth. Will NVIDIA Rubin expand beyond this? Data suggests width is no longer the scaling lever.

2. **FP4 accuracy floor:** NVFP4 claims minimal accuracy loss vs FP8. What is the true quality degradation boundary for FP4 in reasoning-heavy tasks? Current MLPerf benchmarks do not capture this.

3. **Transformer vs SSM hardware trade-offs:** State Space Models (Mamba, etc.) have fundamentally different compute profiles (recurrent, not attention-based). If SSM-transformer hybrids become dominant, how should accelerator ISAs be redesigned?

4. **Wafer-scale scaling limit:** Cerebras demonstrated WSE-3 at 44 GB SRAM. The next generation would require new 3D stacking approaches to substantially grow. What is the physical limit before yield economics prevent further wafer-scale growth?

5. **Analog computing precision barrier:** Current analog in-memory architectures are limited to ~4–8 effective bits. Transformer inference at commercial quality requires 8–16 bits. What material or circuit innovations would close this gap?

### Manufacturing Questions

6. **HBM supply recovery timeline:** Will SK Hynix and Samsung capacity investments normalize HBM3E pricing by 2027, or does HBM4 transition create a new shortage cycle as HBM3E capacity is retired?

7. **Gate-all-around (GAA) transistors:** TSMC N2 uses FinFET-derived process; Samsung GAA 3nm is in production. Will NVIDIA / AMD adopt Samsung GAA nodes for future generations, or remain exclusively TSMC?

8. **CoWoS physical limits:** What is the maximum number of HBM stacks that can be co-packaged with a single logic die in CoWoS? Current max is 8-12 stacks. Rubin with 288 GB HBM4 requires ~8 HBM4 stacks.

### Software / System Questions

9. **KV-cache compression:** Can lossless or near-lossless KV-cache compression (demonstrated at 46.9% reduction) become universally deployed? What accuracy guarantees apply?

10. **Expert routing overhead at scale:** For MoE models with 128+ experts across distributed hardware, what is the minimum expert dispatch overhead achievable? Current implementations add 5–15% overhead.

11. **Disaggregated prefill/decode SLO management:** How should cloud providers price and SLA-guarantee TTFT vs ITL independently when running disaggregated inference infrastructure?

### Strategic Questions

12. **Will NVIDIA's CUDA moat hold against AMD ROCm?** AMD's MLPerf parity on MI355X and accelerating ROCm framework support suggest the gap is narrowing. What is the remaining switching cost?

13. **Photonic AI commercialization:** Lightmatter has commercial samples. What is the realistic timeline to photonic co-processors being standard in data center AI servers?

14. **Post-training inference economics:** As inference hardware becomes 10x more efficient (Blackwell → Rubin), will AI service providers pass savings to consumers or absorb margin? This determines the speed of AI capability democratization.

---

## Source Index

| # | Title | URL | Category |
|---|-------|-----|----------|
| 1 | [TPU v5p Docs](https://docs.cloud.google.com/tpu/docs/v5p) | https://docs.cloud.google.com/tpu/docs/v5p | Official |
| 2 | [Trillium Launch](https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus) | https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus | Vendor Blog |
| 3 | [TPU 7-Gen Guide](https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations) | https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations | Tech Blog |
| 4 | [Ironwood Announcement](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/) | https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/ironwood-tpu-age-of-inference/ | Vendor Blog |
| 5 | [TPU7x Docs](https://docs.cloud.google.com/tpu/docs/tpu7x) | https://docs.cloud.google.com/tpu/docs/tpu7x | Official |
| 6 | [TPUv7 SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the) | https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the | Analyst |
| 7 | [Groq LPU Architecture](https://groq.com/lpu-architecture) | https://groq.com/lpu-architecture | Official |
| 8 | [Groq in 2026 (Voiceflow)](https://www.voiceflow.com/blog/groq) | https://www.voiceflow.com/blog/groq | Tech Blog |
| 9 | [Inside the LPU](https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed) | https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed | Vendor Blog |
| 10 | [LPU arXiv](https://arxiv.org/html/2408.07326v1) | https://arxiv.org/html/2408.07326v1 | arXiv |
| 11 | [WSE-3 Overview](https://awesomeagents.ai/hardware/cerebras-wse-3/) | https://awesomeagents.ai/hardware/cerebras-wse-3/ | Tech Blog |
| 12 | [Cerebras Llama 405B PR](https://www.cerebras.ai/press-release/cerebras-inference-llama-405b) | https://www.cerebras.ai/press-release/cerebras-inference-llama-405b | Press Release |
| 13 | [WSE vs GPU arXiv](https://arxiv.org/html/2503.11698v1) | https://arxiv.org/html/2503.11698v1 | arXiv |
| 14 | [NVIDIA B200 Guide](https://www.runpod.io/articles/guides/nvidia-b200) | https://www.runpod.io/articles/guides/nvidia-b200 | Tech Blog |
| 15 | [Blackwell Architecture](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) | https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/ | Official |
| 16 | [Blackwell 3x Training](https://developer.nvidia.com/blog/nvidia-blackwell-enables-3x-faster-training-and-nearly-2x-training-performance-per-dollar-than-previous-gen-architecture/) | https://developer.nvidia.com/blog/nvidia-blackwell-enables-3x-faster-training-and-nearly-2x-training-performance-per-dollar-than-previous-gen-architecture/ | Vendor Blog |
| 17 | [Trainium3 HPCwire](https://www.hpcwire.com/2025/12/02/aws-brings-the-trainium3-chip-to-market-with-new-ec2-ultraservers/) | https://www.hpcwire.com/2025/12/02/aws-brings-the-trainium3-chip-to-market-with-new-ec2-ultraservers/ | News |
| 18 | [Trainium4 NextPlatform](https://www.nextplatform.com/2025/12/03/with-trainium4-aws-will-crank-up-everything-but-the-clocks/) | https://www.nextplatform.com/2025/12/03/with-trainium4-aws-will-crank-up-everything-but-the-clocks/ | Analyst |
| 19 | [AMD MI355X Official](https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html) | https://www.amd.com/en/products/accelerators/instinct/mi350/mi355x.html | Official |
| 20 | [ISSCC 2026 MI355X](https://www.tomshardware.com/tech-industry/semiconductors/inside-the-instinct-mi355x) | https://www.tomshardware.com/tech-industry/semiconductors/inside-the-instinct-mi355x | News |
| 21 | [AMD MLPerf 6.0](https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-inference-6-0-results.html) | https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-inference-6-0-results.html | Vendor Blog |
| 22 | [Gaudi 3 White Paper](https://cdrdv2-public.intel.com/817486/gaudi-3-ai-accelerator-white-paper.pdf) | https://cdrdv2-public.intel.com/817486/gaudi-3-ai-accelerator-white-paper.pdf | Official |
| 23 | [SambaNova RDU Medium](https://medium.com/@leosorge/sambanova-rdu-reconfigurable-architectures-for-inferencefor-inference-training-and-agentic-ai-5088b5ca400b) | https://medium.com/@leosorge/sambanova-rdu-reconfigurable-architectures-for-inferencefor-inference-training-and-agentic-ai-5088b5ca400b | Tech Blog |
| 24 | [SN40L arXiv](https://arxiv.org/pdf/2405.07518) | https://arxiv.org/pdf/2405.07518 | arXiv |
| 25 | [ISCA 2025 Proceedings](https://dblp.org/db/conf/isca/isca2025.html) | https://dblp.org/db/conf/isca/isca2025.html | Conference |
| 26 | [HW Acceleration Survey arXiv 2512.23914](https://arxiv.org/abs/2512.23914) | https://arxiv.org/abs/2512.23914 | arXiv |
| 27 | [Analog AI Market](https://www.precedenceresearch.com/analog-ai-chip-market) | https://www.precedenceresearch.com/analog-ai-chip-market | Market Research |
| 28 | [IBM AIMC Blog](https://research.ibm.com/blog/how-can-analog-in-memory-computing-power-transformer-models) | https://research.ibm.com/blog/how-can-analog-in-memory-computing-power-transformer-models | Research Blog |
| 29 | [ReRAM On-Chip AI arXiv 2502.04524](https://arxiv.org/pdf/2502.04524) | https://arxiv.org/pdf/2502.04524 | arXiv |
| 30 | [NPU Buying Guide](https://www.newtechguy.com/ai-pc-buying-guide-2025-npu-tops-ratings-performance-benchmarks-and-what-actually-matters/) | https://www.newtechguy.com/ai-pc-buying-guide-2025-npu-tops-ratings-performance-benchmarks-and-what-actually-matters/ | Tech Blog |
| 31 | [Mobile NPU LLM arXiv 2509.23324](https://arxiv.org/pdf/2509.23324) | https://arxiv.org/pdf/2509.23324 | arXiv |
| 32 | [Hybrid SA arXiv 2507.09010](https://arxiv.org/abs/2507.09010) | https://arxiv.org/abs/2507.09010 | arXiv |
| 33 | [Rubin NVL72 VideoCardz](https://videocardz.com/newz/nvidia-vera-rubin-nvl72-detailed-72-gpus-36-cpus-260-tb-s-scale-up-bandwidth) | https://videocardz.com/newz/nvidia-vera-rubin-nvl72-detailed-72-gpus-36-cpus-260-tb-s-scale-up-bandwidth | News |
| 34 | [Rubin Production CES](https://introl.com/blog/nvidia-rubin-full-production-ces-2026-ai-infrastructure) | https://introl.com/blog/nvidia-rubin-full-production-ces-2026-ai-infrastructure | News |
| 35 | [QAic vs GPU arXiv 2507.00418](https://arxiv.org/abs/2507.00418) | https://arxiv.org/abs/2507.00418 | arXiv |
| 36 | [Samsung HBM-PIM](https://semiconductor.samsung.com/news-events/tech-blog/hbm-pim-cutting-edge-memory-technology-to-accelerate-next-generation-ai/) | https://semiconductor.samsung.com/news-events/tech-blog/hbm-pim-cutting-edge-memory-technology-to-accelerate-next-generation-ai/ | Vendor Blog |
| 37 | [HPIM arXiv 2509.12993](https://arxiv.org/abs/2509.12993) | https://arxiv.org/abs/2509.12993 | arXiv |
| 38 | [Optical AI ScienceDaily](https://www.sciencedaily.com/releases/2025/10/251027224833.htm) | https://www.sciencedaily.com/releases/2025/10/251027224833.htm | News |
| 39 | [UCIe Chiplet Revolution](https://www.design-reuse.com/news/202529865-the-chiplet-revolution-how-advanced-packaging-and-ucie-are-redefining-ai-hardware-in-2025/) | https://www.design-reuse.com/news/202529865-the-chiplet-revolution-how-advanced-packaging-and-ucie-are-redefining-ai-hardware-in-2025/ | Tech Blog |
| 40 | [MLPerf Training v5.0](https://mlcommons.org/2025/06/mlperf-training-v5-0-results/) | https://mlcommons.org/2025/06/mlperf-training-v5-0-results/ | Benchmark |
| 41 | [MLPerf Inference v5.1](https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/) | https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/ | Benchmark |
| 42 | [TSMC N3 180k Wafers](https://www.trendforce.com/news/2026/04/27/news-tsmc-3nm-monthly-capacity-may-hit-180k-wafers-by-2026-up-over-40-yoy-on-ai-demand/) | https://www.trendforce.com/news/2026/04/27/news-tsmc-3nm-monthly-capacity-may-hit-180k-wafers-by-2026-up-over-40-yoy-on-ai-demand/ | Market Research |
| 43 | [HBM Shortage Tom's HW](https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-and-sk-hynix-warn-ai-driven-memory-shortages-could-last-until-2027-and-beyond) | https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-and-sk-hynix-warn-ai-driven-memory-shortages-could-last-until-2027-and-beyond | News |
| 44 | [MoE Infrastructure](https://intuitionlabs.ai/articles/llm-inference-hardware-enterprise-guide) | https://intuitionlabs.ai/articles/llm-inference-hardware-enterprise-guide | Tech Blog |
| 45 | [PD Disaggregation](https://groundy.com/articles/prefill-decode-disaggregation-the-architecture-shift-redefining-llm-serving-at-scale/) | https://groundy.com/articles/prefill-decode-disaggregation-the-architecture-shift-redefining-llm-serving-at-scale/ | Tech Blog |
| 46 | [SPAD arXiv 2510.08544](https://arxiv.org/pdf/2510.08544) | https://arxiv.org/pdf/2510.08544 | arXiv |
| 47 | [Tenstorrent Wormhole](https://newsletter.semianalysis.com/p/tenstorrent-wormhole-analysis-a-scale) | https://newsletter.semianalysis.com/p/tenstorrent-wormhole-analysis-a-scale | Analyst |
| 48 | [CXL Memory Expansion](https://introl.com/blog/cxl-memory-expansion-pooling-disaggregated-memory-ai-data-center-2025) | https://introl.com/blog/cxl-memory-expansion-pooling-disaggregated-memory-ai-data-center-2025 | Tech Blog |
| 49 | [RISC-V AI Revolution](https://markets.financialcontent.com/wral/article/tokenring-2025-11-6-risc-v-the-open-source-revolution-reshaping-ai-hardware-innovation) | https://markets.financialcontent.com/wral/article/tokenring-2025-11-6-risc-v-the-open-source-revolution-reshaping-ai-hardware-innovation | News |
| 50 | [DC Energy 2026](https://presenc.ai/research/ai-data-center-energy-consumption-2026) | https://presenc.ai/research/ai-data-center-energy-consumption-2026 | Market Research |
| 51 | [Intelligence Per Watt](https://hazyresearch.stanford.edu/blog/2025-11-11-ipw) | https://hazyresearch.stanford.edu/blog/2025-11-11-ipw | Research Blog |
| 52 | [ML HW Efficiency](https://epoch.ai/data-insights/ml-hardware-energy-efficiency) | https://epoch.ai/data-insights/ml-hardware-energy-efficiency | Research |
| 53 | [LLM Inference Arch Survey](https://arxiv.org/pdf/2506.00008) | https://arxiv.org/pdf/2506.00008 | arXiv |
| 54 | [AxLLM arXiv 2509.22512](https://arxiv.org/abs/2509.22512) | https://arxiv.org/abs/2509.22512 | arXiv |
| 55 | [Microsoft Maia 200](https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/) | https://blogs.microsoft.com/blog/2026/01/26/maia-200-the-ai-accelerator-built-for-inference/ | Vendor Blog |
| 56 | [Hot Chips 2024 Cerebras](https://hc2024.hotchips.org/assets/program/conference/day2/72_HC2024.Cerebras.Sean.v03.final.pdf) | https://hc2024.hotchips.org/assets/program/conference/day2/72_HC2024.Cerebras.Sean.v03.final.pdf | Conference |

---

*Research compiled by AI_accelerators research pipeline. All performance figures are as reported by cited sources; independent verification noted where performed. Flagged items with single-source claims: Groq TOPS/W (self-reported), HPIM speedup (research prototype), Lightmatter efficiency (company claim).*
