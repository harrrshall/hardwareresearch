# GPUs — Research Summary
Generated: 2026-05-22 | Window: 2025-11-22 – 2026-05-22 | Validated sources: 15 primary, 5 context

---

## Executive Summary

The GPU sector in the November 2025 – May 2026 window is defined by five converging developments that collectively mark the most architecturally consequential period in GPU history since the introduction of CUDA:

**1. Exascale-per-rack computing becomes deployable.** NVIDIA GB200 NVL72 (1.44 EXAFLOPS FP4 in a single rack) began widespread cloud deployment in 2025. The GB300 Blackwell Ultra NVL72 reaches 1.5x more performance (shipping H2 2025). Both AWS and Google Cloud committed to deploying NVIDIA's next-generation Vera Rubin NVL72 in H2 2026, delivering 3-4x further density improvement with CG-HBM direct die-stacking.

**2. FP4 quantization becomes the dominant inference precision.** NVIDIA Blackwell 5th-generation tensor cores and AMD CDNA4 matrix cores both natively support FP4 formats (NVFP4 and MXFP4 respectively). On a single Blackwell DGX (8x B200), DeepSeek-R1 671B achieves 30,000+ tokens/second — a 36x improvement from January 2025. FP4 is not yet universal in production (calibration tooling still maturing), but it is the architecture's dominant design point.

**3. AMD reaches competitive parity on inference.** The MI350X and MI355X (CDNA4, TSMC 3nm, 9.2 PFLOPS MXFP4) delivered measurable competitive benchmarks: MI355X beats 4x DGX GB200 by 1.3x on Llama 3.1 405B inference and 8x B200 HGX by 1.2x on DeepSeek-R1 at FP4. Combined with ROCm 7's 3.5x performance jump over ROCm 6, AMD has moved from "niche alternative" to "credible second source" in datacenter AI.

**4. Interconnect topology becomes the central architectural variable.** NVLink 5.0 at 1,800 GB/s per GPU enables the NVL72 rack to behave as a single logical compute device. NVIDIA's NVLink Fusion (Computex 2025) opened NVLink to third-party chipmakers (MediaTek, Marvell, and even Intel in September 2025). UALink 1.0 (April 2025) is the open-standard response from AMD, Intel, and hyperscalers — hardware available late 2026 at earliest. NVLink 6.0 (3,600 GB/s, announced CES 2026) further extends NVLink's lead.

**5. Memory bandwidth, not compute, is the binding constraint for AI.** IBM Research and independent academic work confirmed that attention kernels in LLM inference achieve only 23.35% compute utilization and 47.10% memory bandwidth utilization — the system is fundamentally memory-bandwidth-bound. HBM4, arriving in Rubin and MI400 in H2 2026, doubles per-stack bandwidth from 1.2 TB/s to 1.5+ TB/s. AMD MI400's 19.6 TB/s total target represents a 2.45x generational jump.

**The supply constraint:** TSMC CoWoS advanced packaging remains critically oversubscribed. NVIDIA holds 60%+ of 650K annual wafers in 2025, limiting availability of competing AI accelerators. CoWoS capacity targets 730K wafers in 2026, but lead times remain 6-12 months for non-NVIDIA customers.

---

## All Collected Findings

### NVIDIA Blackwell Architecture (GB200 / GB300 / GB10)
- **GB200 NVL72**: 72 Blackwell B200 GPUs in a single rack. 1.44 EXAFLOPS FP4. 130 TB/s NVLink 5.0 system bandwidth. Requires 120kW power and mandatory liquid cooling. Ships to Microsoft, Meta, Oracle, Amazon, Google from early 2025. CoreWeave ordered $2.3B of systems.
- **B200 GPU specs**: 192GB HBM3E at 8 TB/s, 9+ PFLOPS FP4, 1,800 GB/s NVLink 5.0, 1,000W TDP.
- **GB300 Blackwell Ultra**: 288GB HBM3E (12-high stacks), 15 PFLOPS FP4, 1,400W TDP, 640 5th-gen tensor cores, 20,480 CUDA cores, PCIe Gen6. Ships H2 2025. GB300 NVL72 = 1.1 exaflops, 1.5x GB200 NVL72. 250kW+ rack power.
- **5th-generation tensor cores**: Native FP4 (NVFP4) and FP6 support via micro-tensor formats. 256 KB TMEM per SM (new). Dedicated hardware decompression engine for sparse data. Fine-grained structured sparsity: 3x throughput improvement over dense. Unified INT32/FP32 cores better than Hopper in mixed workloads.
- **Warp scheduling advance**: Blackwell eliminates Hopper's 4-warp synchronization requirement for wgmma operations. Dual-thread-block MMA enables paired SMs to cooperate on single MMA operation, sharing operands.
- **FP64 regression**: Only 2 FP64 units/SM vs. 64 in GH100 — Blackwell explicitly deprioritizes HPC in favor of AI.
- **GB10 DGX Spark**: Consumer Blackwell workstation (TSMC 3nm, 140W, 1 PFLOP FP4, 128GB unified LPDDR5X). 600 GB/s NVLink C2C CPU-GPU bandwidth. $3,000. Ships October 2025.
- **DeepSeek-R1 benchmark**: 8x B200 achieves 30,000+ tokens/second, 250+ tokens/second per user. 36x throughput improvement since January 2025.
- **NVFP4 format**: FP8 micro-scales on 16-value blocks + global FP32 scale. 88% lower quantization error than power-of-two MXFP4.

### AMD CDNA4 — Instinct MI350 Series
- **MI350X specs**: TSMC N3P (8 XCDs) + N6 (2 base dies). 185B transistors. 256 CUs, 1,024 matrix cores. 288GB HBM3E at 8 TB/s. 9.2 PFLOPS MXFP4. 1,000W TDP. Launched June 2025.
- **MI355X specs**: 288GB HBM3E, 10 PFLOPS MXFP4/MXFP6, 1,400W TDP.
- **CDNA4 matrix core advances**: Doubled throughput for low-precision types. MXFP4 and MXFP6 support. 2:4 structured sparsity for FP16/BF16/FP8/INT8/MXFP8. LDS bandwidth doubled.
- **Infinity Fabric redesign**: 5.5 TBps inter-die bandwidth (within MI350 package). 7x Gen4 links = 1,075 GBps aggregate GPU-to-GPU.
- **Scale**: 128 liquid-cooled GPUs = 2.6 exaflops FP4 + 36TB HBM3E. 64 air-cooled = enterprise rack.
- **Competitive benchmarks**: MI355X 1.3x faster than 4x DGX GB200 on Llama 3.1 405B inference; 1.2x faster than 8x B200 HGX on DeepSeek-R1 at FP4. MI355X 2.7x more tokens/s vs MI325X at FP8.
- **InferenceMAX**: 5x generational improvement from MI300X to MI355X.

### ROCm 7 Software Platform
- **Performance**: 3.5x inference improvement and 3x training throughput vs ROCm 6 on MI300X.
- **New features**: FP4 (MXFP4) and FP6 (MXFP6) support. DeepEP inference engine with compute-communication overlap. Native vLLM integration. Windows support for Radeon 7000/9000.
- **Framework support**: PyTorch, TensorFlow, ONNX, JAX/XLA all day-zero supported.

### AMD RDNA4 — Radeon RX 9000 Series (Context)
- **Navi 48**: 53.9B transistors, 356.5 mm², TSMC 4nm. 64 CUs, 128 AI matrix accelerators. 3rd-gen RT accelerators. 8x faster AI inference vs RDNA3 at INT8/INT4.
- **Products**: RX 9070 XT ($599), RX 9070 ($549). March 2025 availability.
- **RT performance**: 2x improvement over RDNA3; competitive in most RT games with NVIDIA Blackwell consumer GPUs.
- **Hot Chips 2025**: Navi 48 designed to be halved for lower-tier products. B-frame AV1 encoder added.

### DLSS 4 and Neural Rendering (Context + Window)
- **DLSS 4** (January 2025): First real-time transformer model for super resolution. Multi Frame Generation generates up to 3 AI frames per rendered frame. Up to 8x framerate multiplier. MFG exclusive to RTX 50 Blackwell.
- **DLSS 4.5** (CES 2026, in window): 6X Dynamic Multi Frame Generation. 2nd-generation transformer SR model. 250+ games supported.

### NVLink 5.0 and 6.0 Interconnect
- **NVLink 5.0**: 1,800 GB/s per GPU bidirectional (2x over NVLink 4.0's 900 GB/s). 18 links × 100 GB/s. GB200 NVL72 aggregate: 130 TB/s. Max domain: 576 GPUs.
- **NVLink Fusion** (Computex 2025): Chiplet-based NVLink 5 integration for third-party CPUs (MediaTek, Marvell, Qualcomm, Fujitsu, Intel).
- **Intel deal** (September 2025): NVIDIA invests $5B in Intel; Intel builds NVL72-style racks with x86 CPUs.
- **NVLink 6.0** (CES 2026): 3,600 GB/s per GPU. Vera Rubin NVL72: 260 TB/s rack bandwidth.

### UALink 1.0 Open Standard
- Released April 8, 2025. Consortium: AMD, Intel, Google, Microsoft, Meta, Broadcom, Cisco, HPE, AWS.
- 800 Gbps per Station (4 lanes). Up to 1,024 accelerators per domain.
- Hardware availability: Late 2026 at earliest. Meaningful production: 2027.

### NVIDIA Rubin GPU Architecture
- **Transistors**: 336B. **Process**: TSMC 3nm-class.
- **Memory**: HBM4 (first NVIDIA product with HBM4). CG-HBM: memory stacked directly on GPU die.
- **NVLink**: NVLink 6.0 at 3,600 GB/s per GPU.
- **Vera Rubin NVL72**: 72 Rubin GPUs + 36 Vera CPUs. 260 TB/s rack bandwidth. 3-4x compute density over Blackwell.
- **Vera CPU**: 88 custom Olympus Arm v9.2-A cores. 10-wide instruction decoder. 1.5x IPC over Grace. 1.5 TB LPDDR5X at 1.2 TB/s.
- **Timeline**: Enterprise H2 2026. Consumer late 2026 / early 2027.

### AMD MI400 CDNA5 (Roadmap)
- **Launch**: H2 2026. **Architecture**: CDNA5.
- **Compute**: 40 PFLOPs FP4, 20 PFLOPs FP8. **Memory**: 432GB HBM4 at 19.6 TB/s.
- **Scale-out**: 300 GB/s new scale-out link. **Packaging**: CoWoS-L.
- **Variants**: MI455X (training/cloud) and MI430X (HPC/government with native FP64).

### HBM Memory Evolution
- **HBM3E** (current): up to 1.2 TB/s per stack, 1,024-bit I/O. Deployed in H200, B200, MI350X.
- **HBM4** (JEDEC spec April 2025): 2,048-bit I/O (doubled). 1.5+ TB/s per stack. Up to 64GB per stack. First deployments: Rubin R100 and MI400, H2 2026.
- **HBM4E** (future): 10+ Gb/s per pin. 2027-2028.

### TSMC CoWoS Packaging Bottleneck
- 2025 capacity: 650K wafers. NVIDIA: 370K (57%). Monthly: 75-80K wafers. Target 2026: 730K+ wafers, 120-130K/month.
- Outsourced to Amkor (~180-190K) and SPIL (~60-80K) per year.
- Oversubscribed through at least 2026. Lead times: 6-12 months for non-NVIDIA customers.

### LLM Inference Memory Bottleneck Research
- Attention kernels: 23.35% compute utilization, 47.10% memory bandwidth utilization.
- Arithmetic intensity of attention stays near-constant as batch size grows → DRAM saturation at large batches.
- Multiple bottleneck sources: CPU preprocessing, PCIe transfer, memory bandwidth, KV cache growth.
- Flash Attention 3 on H100: 1.5-2x speedup vs FA2. FP8: 2x throughput over FP16. vLLM 0.6+: 3-5x throughput via continuous batching.

### Production LLM Serving (vLLM/DeepSeek)
- Production H200 clusters: 2,200 tokens/second per H200 GPU at scale using Wide-EP.
- SGLang: 52,300 input + 22,300 output tokens/second at large scale.
- Speculative decoding: 2-3x speedup; EAGLE achieves ~80% acceptance rate.
- NVIDIA Blackwell vs H200: Up to 4x higher throughput at similar latency (InferenceMAX).

### Thermal Management Crisis
- GB200 NVL72: 120kW. GB300 NVL72: 250kW+. Liquid cooling now mandatory for all AI GPU racks.
- CoolIT: ~200 W/cm² heat flux coldplate demo (single-phase) handling 4,000W.
- TSMC + HP: Developing direct-to-silicon microfluidic cooling for next-gen GPUs.
- Liquid cooling market: $4.9B (2024) → $21.3B (2030) at 27.6% CAGR.

### China Domestic GPU Sector
- IPO wave: Moore Threads (Dec 2025, $1.1B, +400% debut), MetaX (Dec 2025), Biren (HK, Jan 2026), Enflame (HK, Jan 2026).
- Combined market cap: >$186B. Moore Threads revenue: $60M with $700M cumulative losses.
- Moore Threads Huagang: 5th-gen architecture, 50% compute density increase, H100-class claim for 2026 (unverified).
- Advancing to 6nm/7nm processes. Cluster stability challenges reported (DigiTimes April 2026).

---

## Summarized Papers

**paper-001 (Blackwell GB200/GB300 Performance)**: Establishes the performance envelope of NVIDIA's current flagship system. GB200 NVL72 delivers 3.2x training speedup vs Hopper and 30x inference speedup vs H100 count-equal comparison. GB300 adds 50% more performance in H2 2025.

**paper-002 (AMD MI350X CDNA4)**: Demonstrates AMD's competitive return to datacenter AI. CDNA4 at TSMC 3nm achieves 9.2 PFLOPS MXFP4 with 8TB/s HBM3E. MI355X beats B200 on select inference benchmarks. InferenceMAX shows 5x generational improvement.

**paper-003 (Blackwell Microbenchmarks)**: Independent academic characterization of Blackwell's microarchitecture. Confirms TMEM (256KB/SM), warp-level MMA scheduling, 3x sparsity throughput, and the deliberate FP64 regression to 2 units/SM. Most detailed public analysis of Blackwell's internals.

**paper-004 (NVLink 5.0 and Fusion)**: Documents the interconnect architecture enabling rack-scale GPU coherency. NVLink 5.0 at 1,800 GB/s per GPU doubles Hopper's bandwidth. NVLink Fusion creates ecosystem lock-in through chiplet licensing. NVLink 6.0 at 3,600 GB/s already announced.

**paper-005 (AMD RDNA4, Context)**: AMD's consumer GPU architectural response. Doubled RT performance, 8x faster AI inference vs RDNA3, enlarged L2 cache for RT workloads. Hot Chips 2025 confirmed modular design and B-frame AV1 encoding.

**paper-006 (NVIDIA Rubin Architecture)**: Next GPU generation specifications. 336B transistors, HBM4, NVLink 6.0, CG-HBM stacking. Vera CPU with custom Olympus Arm cores. Enterprise H2 2026 deployment. GTC 2026 commitments from AWS (1M GPUs) and Google Cloud.

**paper-007 (HBM3E to HBM4)**: Memory technology evolution that will double inference throughput for memory-bound workloads. JEDEC HBM4 spec (April 2025) doubled I/O to 2,048 bits. First deployments in H2 2026 with Rubin and MI400.

**paper-008 (DLSS 4, Context/Validated)**: Neural rendering advances using Blackwell tensor cores. First real-time transformer model for consumer GPU. DLSS 4.5 (CES 2026) extends to 6X frame generation. 250+ games supported.

**paper-009 (ROCm 7, Context)**: AMD's software platform closing CUDA gap. 3.5x inference improvement on MI300X. FP4/FP6 support. DeepEP inference engine. Native vLLM support.

**paper-010 (TSMC CoWoS Constraints)**: Supply bottleneck analysis. NVIDIA secures 57% of all CoWoS capacity. Oversubscribed through 2026. Constrains AMD MI400 and all alternative AI accelerator availability.

**paper-011 (MLPerf v5.1)**: Third-party validation of GPU inference performance. H200 8-GPU cluster achieves 31,391 tokens/s on Llama 3.1-70B. AMD MI355X competitive. First DeepSeek-R1 standardized benchmark.

**paper-012 (GPU Memory Bottleneck)**: Academic foundation for why bandwidth (not FLOPS) is the design constraint. 23.35% compute utilization, 47.10% memory bandwidth utilization in attention kernels. Motivates HBM4 and TMEM advances.

**paper-013 (UALink 1.0)**: Open interconnect standard specification. 800 Gbps per Station, 1,024-GPU domain. No hardware until late 2026. Strategic counterweight to NVLink ecosystem dominance.

**paper-014 (DGX Spark, Context)**: NVLink C2C at workstation scale. 600 GB/s CPU-GPU bandwidth. 140W Blackwell GPU. Validates NVLink Fusion chiplet approach in production hardware.

**paper-015 (AMD MI400 Roadmap)**: AMD's H2 2026 competitive response to Rubin. 432GB HBM4, 19.6 TB/s, 40 PFLOPs FP4, 300 GB/s scale-out link. 2.45x bandwidth improvement over MI350X.

**paper-016 (Acc-SpMM, Context)**: 2.52x average SpMM speedup over cuSPARSE on RTX 4090 by aligning sparse matrices to tensor core requirements. Shows production GPU sparse libraries under-exploit hardware.

**paper-017 (FP4/FP8 Quantization)**: NVFP4 format delivers 88% lower error than power-of-two MXFP4. Enables 30,000 tok/s on DeepSeek-R1. FP4 production deployment maturing through 2026.

**paper-018 (China GPU Sector)**: IPO wave validates China's domestic GPU investment thesis. Moore Threads, Biren, MetaX all public. Financial reality: $60M revenue vs $700M losses. Performance claims (H100-class Huagang) unverified.

**paper-019 (Thermal Management)**: 250kW+ racks force fundamental data center redesign. CoolIT demonstrates 4,000W coldplate at ~200 W/cm². TSMC developing direct-to-silicon microfluidic cooling. Market growing 27.6% CAGR.

**paper-020 (vLLM DeepSeek Production Serving)**: Production measurement: 2,200 tok/s per H200 GPU at scale. Algorithmic MoE optimizations (Wide-EP) responsible for significant fraction of throughput. Blackwell achieves 4x over H200 in InferenceMAX.

---

## Technical Analysis

### Tensor Core Precision Architecture (FP4 → FP8 → FP16 stack)

Both NVIDIA Blackwell and AMD CDNA4 have independently arrived at strikingly similar precision format hierarchies in 2025-2026: FP4 for peak inference throughput, FP8 for production-validated inference, FP16/BF16 for training, and TF32 for legacy compatibility. This convergence is not coincidental — it is driven by the same application pressure (trillion-parameter LLM inference) and the same physical constraint (HBM bandwidth per parameter per token).

NVIDIA's NVFP4 and AMD's MXFP4 (OCP standard) diverge at the micro-scaling implementation. NVIDIA's NVFP4 uses FP8 micro-scales at 16-value block granularity; AMD's MXFP4 uses power-of-two scales per the OCP standard. NVIDIA claims 88% lower quantization error for NVFP4. The architectural consequence is that models quantized for NVFP4 are not directly portable to MXFP4 hardware without re-calibration — creating a hidden ecosystem compatibility gap.

For the 2:4 structured sparsity hardware, both architectures implement identical patterns: 2 non-zero values per 4-element group, with hardware that skips zero-valued elements. This doubles effective throughput for eligible layers. The Blackwell addition is the dedicated hardware decompression engine (per src-021): compressed sparse representations in HBM are decompressed on-the-fly before entering TMEM, hiding the decompression cost.

### Memory Bandwidth as the Governing Variable

The IBM Research finding (23.35% compute, 47.10% memory bandwidth utilization in attention) quantitatively confirms what practitioners have observed: LLM inference is not compute-bound. The implication is that FP4's 4x compute density advantage over FP16 translates to throughput improvements only for the compute-bound (linear layer) portions of transformer inference — the attention portion remains bandwidth-bound regardless of tensor core precision.

This creates a structural architectural opportunity that HBM4 directly addresses. Moving from 8 TB/s (HBM3E, MI350X / B200) to 19.6 TB/s (HBM4, MI400) would improve attention throughput by ~2.45x on a single GPU — more impactful than any tensor core precision improvement for attention-heavy workloads.

The Blackwell TMEM (256 KB per SM) partially addresses this by keeping intermediate MMA results on-chip rather than round-tripping through HBM. For transformer FFN layers (which are the compute-intensive portion), TMEM reduces HBM reads for reused operands. The dual-thread-block MMA feature allows adjacent SMs to share operands, cutting HBM reads in half for those operations.

### Warp Scheduling and Execution Pipeline Changes

The elimination of the 4-warp synchronization requirement for wgmma in Blackwell (confirmed by microbenchmarks, src-003) is a meaningful scheduling improvement. In Hopper, scheduling a warp group matrix multiply-accumulate requires all 4 participating warps to be ready simultaneously, creating pipeline stalls when even one warp is delayed. Blackwell's warp-level MMA scheduling allows individual warps to issue MMA instructions, improving SM utilization under memory latency variability.

For the RDNA4 architecture (AMD consumer GPU), the redesigned compute units with dual-issue capability and out-of-order memory operations represent parallel improvements. The enlarged L2 cache specifically targeting RT workload efficiency shows AMD's recognition that BVH traversal (ray tracing tree structures) creates irregular memory access patterns that benefit more from cache capacity than throughput.

---

## Architectural Observations

### The Dual-Die and Chiplet Convergence

Every major GPU platform announced in this period uses multi-die (chiplet) construction:

- **NVIDIA Blackwell B200**: Two reticle-limited dies connected via 10 TB/s NV-HBI
- **AMD MI350X**: 8 compute dies (XCDs) + 2 base dies, TSMC 3nm + 6nm
- **NVIDIA GB10**: CPU tile (MediaTek) + GPU tile (NVIDIA) via NVLink C2C on TSMC 3nm
- **NVIDIA Rubin**: CG-HBM direct die-stacking on GPU (memory-on-logic)

The pattern shows GPU architecture has permanently departed from monolithic die design at the high end. The engineering trade-off is clear: monolithic dies face yield penalties (one defect kills the whole die), reticle limits (maximum die size ~800 mm²), and power delivery challenges. Chiplet designs allow heterogeneous process nodes (AMD's 3nm compute + 6nm I/O base) and modular yield management.

NVIDIA's CG-HBM in Rubin is the most architecturally novel development: stacking HBM memory dies directly on top of the GPU logic die eliminates the silicon interposer layer entirely. This reduces access latency, improves bandwidth-per-mm², and enables higher sustained memory throughput — directly addressing the bandwidth bottleneck identified in paper-012.

### The NVLink Ecosystem Lock-in Architecture

NVIDIA's interconnect strategy in 2025-2026 reveals a deliberate ecosystem architecture: NVLink 5.0 creates the high-performance GPU-to-GPU fabric, NVLink C2C creates the CPU-GPU coherent interface, and NVLink Fusion creates the third-party chiplet integration pathway. Together they form a three-tier ecosystem lock:

1. **Intra-rack GPU fabric** (NVLink Switch, 576-GPU domains): Creates the "single logical GPU" illusion for AI training at scale
2. **CPU-GPU superchip integration** (NVLink C2C, 600 GB/s): Enables Grace-Blackwell, GB10, and now Vera Rubin superchips
3. **Third-party chiplet interface** (NVLink Fusion, chiplet licensing): Allows MediaTek, Marvell, Intel to build NVLink-capable chips without full IP licensing

This architecture means customers who build NVLink-native software stacks (using multi-GPU communication primitives optimized for NVLink topology) face switching costs to move to UALink or other fabrics — even if UALink hardware delivers equal or better bandwidth per dollar.

### FP64 Architectural Divorce

The finding that Blackwell has only 2 FP64 units per SM (vs 64 in GH100) is architecturally significant. NVIDIA has explicitly decoupled AI GPU design from HPC/scientific computing GPU design. The GH100 (H100) was the last NVIDIA architecture where FP64 was a primary design objective. Blackwell is the first architecture where FP64 is vestigial — maintained for instruction set compatibility but not performance-critical.

This represents an architectural fork: the H100/H200 family (Hopper) remains NVIDIA's HPC/scientific computing recommended platform, while Blackwell and Rubin are AI-first architectures. For GPU architecture research, this means future AI-GPU performance analysis should not evaluate FP64 performance as a meaningful metric.

### AMD Chiplet vs NVIDIA Die-Pair Approach

AMD's 8-die XCD approach (8 compute chiplets + 2 base dies) and NVIDIA's 2-die approach represent different chiplet philosophies:

- **AMD**: Many smaller dies = better yield per die, more granular compute scaling, but higher inter-die communication overhead (5.5 TBps Infinity Fabric within package)
- **NVIDIA**: Two large reticle-sized dies = fewer inter-die links, simpler memory topology, but larger per-die area and yield risk

NVIDIA's approach with CG-HBM in Rubin may represent a third model: eliminate the interposer entirely and stack memory directly on the compute die, using 3D TSVs for electrical connections. This is architecturally closest to mobile SoC memory-on-package integration, scaled to datacenter power levels.

---

## Trend Analysis

### Trend 1: Inference Dominates GPU Architecture Decisions

GTC 2026's major strategic announcement was NVIDIA's explicit pivot from training to inference as the primary growth and revenue driver. This reflects a market reality: LLM training is primarily done by hyperscalers on massive clusters (relatively fewer systems), while inference is required for every production deployment (vastly more systems). Architecturally, this means:

- FP4 and FP8 (inference-first precisions) are primary design objectives
- Low-latency decode optimization (TMEM, KV cache compression) is a first-class requirement
- MIG (Multi-Instance GPU) partitioning for efficient multi-tenant inference is increasingly important
- Memory capacity per GPU (288GB for MI350X, coming 432GB for MI400) prioritized for large model deployment without parameter offloading

### Trend 2: Annual GPU Cadence Becomes Norm

Both NVIDIA and AMD have established (or aspire to establish) annual GPU architecture refresh cycles for datacenter AI:

- **NVIDIA**: H100 (2022) → H200 (2023/24) → B200 GB200 (2025) → GB300 Blackwell Ultra (H2 2025) → Rubin (H2 2026) → Rubin Ultra (2027) → Feynman (~2028)
- **AMD**: MI300X (2023) → MI325X (2024) → MI350X/MI355X (June 2025) → MI400 (H2 2026) → MI500 (2027)

This annual cadence has no precedent in GPU history. It places enormous pressure on CoWoS packaging supply (src-025), software ecosystem maturity, and customer datacenter infrastructure (which cannot refresh annually at $30,000-60,000 per GPU). The cadence is financially driven: each generation commands a premium pricing window before the next generation resets the market.

### Trend 3: Software Value Exceeds Hardware Value for Near-Term Performance

The 36x DeepSeek-R1 throughput improvement from January to December 2025 (src-033) is instructive: the hardware (Blackwell) was constant; the software improvements (vLLM, TensorRT-LLM, NVFP4 calibration, continuous batching, expert parallelism) drove the majority of gains. Similarly, H200 improved 12.3% from MLPerf v5.0 to v5.1 (same hardware, better software).

This trend has a ceiling: hardware compute and bandwidth limits constrain how much software can improve. But in the 0-24 month window after new hardware launches, software optimization typically extracts 3-10x more performance than the initial deployment achieves. Companies with better software teams extract disproportionately more value from the same hardware investment.

### Trend 4: Interconnect Standards War Plays Long Game

NVLink vs UALink is a multi-year industry contest. The 2025-2026 period establishes the factions clearly:

- **NVLink camp**: NVIDIA, MediaTek, Marvell, Qualcomm, Fujitsu, (Intel as ally)
- **UALink camp**: AMD, Intel, Google, Microsoft, Meta, Broadcom, Cisco, HPE, AWS

The hyperscalers are in both camps simultaneously — they use NVLink-based Blackwell/Rubin systems (no choice, best performance) while funding UALink as a future hedge. The critical date is late 2026 / early 2027 when UALink hardware materializes. If UALink switches deliver competitive bandwidth at lower cost than NVLink switches, hyperscalers will shift new cluster builds to UALink-based systems. If UALink hardware underperforms or is delayed, NVLink maintains market control through the next GPU generation.

### Trend 5: GPU Performance Gains Are Increasingly Driven by Packaging, Not Process

The move from Hopper (TSMC 4nm) to Blackwell (TSMC 4NP) to Rubin (TSMC 3nm) represents incremental node improvements. But the performance gains from Hopper to Blackwell (~30x for inference) far exceed what the node transition could deliver alone. The performance comes from:

1. **FP4 tensor cores**: 4x compute throughput per tensor core vs FP16 at same node
2. **HBM3E capacity increase**: 141GB (H200) → 192GB (B200) → 288GB (GB300) — enables larger batch sizes
3. **NVLink 5.0 bandwidth**: 2x over NVLink 4.0 — enables tensor parallelism at scale
4. **CoWoS advanced packaging**: Enables multiple HBM3E stacks (B200 uses 5 stacks vs H100's 5)
5. **Architecture changes**: TMEM, decompression engine, dual-TB MMA

This packaging-driven performance improvement means TSMC's CoWoS capacity (src-025) is a more critical constraint than TSMC's logic process capacity. Companies that secure CoWoS wafers secure GPU supply; the logic process (3nm, 4nm) is comparatively less constrained.

---

## Manufacturing Implications

### CoWoS: The Invisible Bottleneck

TSMC's CoWoS (Chip-on-Wafer-on-Substrate) advanced packaging is currently the single most constrained element in the AI GPU supply chain. The pattern is:

- TSMC logic wafers (3nm, 4nm): Growing capacity; not the bottleneck
- HBM memory stacks: Concentrated at SK Hynix, Samsung, Micron; HBM4 transitioning
- CoWoS packaging: NVIDIA secures 57% of 650K annual wafers (2025), oversubscribed through 2026

The implication: even if AMD fabricates MI400 chiplets flawlessly at TSMC 3nm, packaging them with 432GB HBM4 via CoWoS-L requires packaging capacity that NVIDIA's multi-year booking dominates. This creates a structural advantage for NVIDIA beyond pure chip design excellence.

TSMC's strategy response: outsource 240-270K wafers/year to Amkor and SPIL while building TSMC CoPoS (new packaging technology, equipment arriving mid-2026). CoPoS may partially relieve the bottleneck by 2027.

### Die Area Economics

The Blackwell B200 GPU die pair (two reticle-limited dies) maximizes silicon area per GPU. At TSMC 4NP, reticle limit is approximately 800 mm²; the B200 uses two ~400mm² dies. By comparison, RDNA4's Navi 48 at 356.5 mm² is still well within single-die territory. As transistor counts scale toward 200B and beyond (Rubin's 336B), the multi-die approach becomes mandatory for both yield and reticle reasons.

The yield economics of chiplets improve non-linearly with die area: defect density is approximately constant, so smaller dies have exponentially better yield. AMD's 8-die approach for MI350X (each XCD smaller than RDNA4's Navi 48) reflects aggressive yield optimization — any single XCD defect disables only 1/8 of compute, not the whole GPU.

### HBM4 Supply Transition

The transition from HBM3E to HBM4 in H2 2026 creates a temporary supply gap risk. Both NVIDIA Rubin and AMD MI400 are HBM4 customers simultaneously, competing for early production allocation from SK Hynix (primary supplier), Samsung, and Micron. Micron confirmed high-volume HBM4 production for Rubin (36GB modules), giving NVIDIA a confirmed supply arrangement. AMD's HBM4 supply arrangements for MI400 are less publicly confirmed.

The 2,048-bit interface of HBM4 (doubled from HBM3E's 1,024-bit) requires larger CoWoS interposers (or direct stacking in Rubin's CG-HBM approach). This further increases CoWoS area per GPU, compounding the packaging bottleneck.

### China GPU Manufacturing Constraints

Moore Threads and Biren face a compound manufacturing disadvantage:

1. **Logic process**: Limited to TSMC 7nm/6nm (export controls prevent advanced node access); NVIDIA at TSMC 4NP/3nm has 1-2 generation advantage
2. **HBM access**: HBM suppliers (SK Hynix, Samsung) face US export pressure; Chinese GPU companies may have limited HBM access
3. **CoWoS access**: TSMC CoWoS is similarly constrained by export control concerns; advanced CoWoS (for HBM3E/HBM4) may not be available
4. **SMIC limitations**: China's domestic SMIC foundry is at 7nm/14nm equivalent; not capable of competitive AI GPU process nodes

This manufacturing constraint gap explains why Moore Threads' H100-class claim for 2026 is unlikely on the published timeline despite the capital raised in IPOs. The cluster stability challenges reported in April 2026 (DigiTimes) are consistent with early-generation, pre-volume-production hardware.

---

## Scalability Considerations

### Single-Rack to Multi-Rack Scaling Architecture

The GB200/GB300 NVL72 rack-scale architecture creates a two-tier scaling hierarchy:

- **Within-rack** (NVLink 5.0, 130-260 TB/s): All-to-all communication fully supported; model parallelism across 72 GPUs is efficient
- **Between-rack** (InfiniBand HDR/NDR, 3.2-4.8 TB/s per link): 30-80x lower bandwidth than intra-rack NVLink

This bandwidth asymmetry fundamentally shapes parallelism strategy: tensor parallelism (requires near-zero communication latency) is best confined within a single NVL72 rack, while data parallelism and pipeline parallelism (which tolerate higher communication latency) can span racks. For a 100B-parameter dense model, fitting it within one GB300 NVL72 rack (288GB × 72 = ~20 TB total HBM) is achievable with FP4 quantization (100B × 0.5 bytes/param = 50GB) — enabling fully intra-rack inference.

For trillion-parameter MoE models like DeepSeek-R1 (671B active but larger total), expert parallelism spans multiple racks. The Wide-EP technique (paper-020) optimizes this by spreading experts across more GPUs than the model's natural parallelism, trading communication volume for load balancing. The 2,200 tok/s/H200 production figure represents state-of-the-art optimization of this multi-rack MoE deployment.

### MIG and Workload Multiplexing

Blackwell and Hopper MIG allows each GPU to be partitioned into up to 7 isolated instances. For inference workloads, this means a single B200 (192GB, 9+ PFLOPS) can serve seven independent tenants at 27GB HBM each — appropriate for 7B-13B model inference. AWS Bottlerocket's March 2025 MIG support for Kubernetes enables cloud-native MIG-based GPU sharing at scale.

The architectural scalability implication: MIG extends the useful utilization range of high-end GPUs from "dedicated to one large model" to "shared across many small models." This is important as inference workloads diversify: a cloud provider operating GB200s for mixed workloads (some 70B model inference, some 7B model inference, some fine-tuning) can use MIG to time-multiplex efficiently.

### UALink's 1,024-GPU Domain vs NVLink's 576-GPU Domain

UALink 1.0's 1,024-accelerator domain specification exceeds NVLink 5.0's 576-GPU limit. For today's model scales (up to ~1T parameters for dense, ~7T for large MoE), 576 GPUs is sufficient. But as models scale further (multi-trillion parameter frontier models expected 2027-2028), 576-GPU coherent domains may become limiting. The 1,024-GPU UALink domain gives AMD and Intel a future architectural headroom claim that NVIDIA's 576-GPU limit cannot match until NVLink 7.0 or beyond.

### Energy Efficiency at Scale

At GB300 NVL72 rack power of 250kW and a data center PUE of 1.3, a 100-rack AI cluster draws 32.5 MW of power. At $0.07/kWh (enterprise rate), annual energy cost is $19.9M — exceeding GPU depreciation cost for a 3-year amortization at $40,000/GPU. This energy economics driver is pushing GPU architecture toward the Vera Rubin's claimed 40% better energy efficiency per watt vs Blackwell. If validated, 40% efficiency improvement at similar performance would reduce 100-rack cluster energy cost by $8M/year — a strong economic justification for annual GPU refreshes.

---

## Strategic Insights

### NVIDIA's Structural Competitive Position

NVIDIA's competitive position in 2025-2026 is not primarily based on superior chip design (though Blackwell is excellent). It is based on three structural advantages that compound:

1. **Software ecosystem depth**: CUDA libraries (cuDNN, cuBLAS, NCCL, TensorRT) have 15+ years of optimization. ROCm 7 matches CUDA on paper for major frameworks but lacks the long-tail of CUDA-optimized kernels from thousands of researchers.

2. **Supply chain security**: 57% of TSMC CoWoS capacity is effectively a supply chain moat. Competitors cannot double their capacity by writing checks — they need TSMC allocation.

3. **Interconnect ecosystem lock**: NVLink Fusion with MediaTek, Marvell, Qualcomm, and now Intel creates a validated silicon ecosystem. Software optimized for NVLink topology (NCCL collectives, tensor parallelism patterns) requires re-tuning for UALink.

AMD's path to meaningful market share requires winning on all three simultaneously: software parity (ROCm 7 is promising but not complete), supply diversification (MI400 with CoWoS-L), and interconnect alternatives (UALink 2026+). Progress on any one without the others is insufficient.

### The Inference Economics Inflection

As inference becomes the dominant GPU workload (per GTC 2026 strategic pivot), the economics shift from "training clusters are rare and shared" to "inference capacity must match user concurrency at all times." This changes what "good GPU value" means:

- **Training metric**: PFLOPS/dollar (compute throughput efficiency)
- **Inference metric**: Tokens/second/dollar at target latency (throughput efficiency at SLA)

At the tokens/second/dollar metric, AMD MI355X is competitive with NVIDIA B200 for several models — a significant change from the training-dominated market where NVIDIA held larger advantages. If inference remains dominant, AMD's competitive position strengthens, particularly as ROCm 7 matures.

### China GPU Sector: Geopolitically-Motivated Investment

The China domestic GPU sector IPOs represent a government-backed bet that domestic AI chip capability is a strategic necessity, not just a commercial opportunity. The $186B combined market capitalization for companies with $60-100M annual revenues each implies a market bet that China will achieve competitive domestic GPU supply at some point — even if 2026 hardware cannot match NVIDIA's H100-class performance.

The strategic implication for NVIDIA: export controls that limit H100 sales to China simultaneously protect Blackwell-class technology and incentivize China's domestic GPU R&D investment. Every quarter that Chinese GPU companies advance reduces the TAM available to NVIDIA in the China datacenter market — currently estimated at 20-25% of global AI GPU spending.

### The Cooling Infrastructure Bet

250kW+ racks are not deployable in standard data centers. The $250M+ investment that hyperscalers are making in liquid-cooled AI data center infrastructure is a bet on continued GPU TDP scaling. If future GPU generations flatten TDP growth (e.g., through CG-HBM efficiency gains or 2nm process improvements), some of this infrastructure investment becomes over-specified. Conversely, if next-generation GPUs require 400kW+ racks, current liquid cooling infrastructure becomes inadequate.

TSMC's direct-to-silicon microfluidic cooling development suggests the silicon supply chain itself is investing in solving the thermal problem at the chip level — which could enable higher sustained clock speeds for the same package-level thermal budget.

---

## Open Questions

### 1. Will CG-HBM (Memory-on-GPU Die) Achieve Manufacturing Yield at Scale?
Rubin's CG-HBM approach — stacking HBM directly on the GPU logic die — is architecturally superior (lower latency, higher bandwidth density, smaller package footprint). But it is an unproven manufacturing approach at datacenter GPU scale. The key question is whether TSV (Through-Silicon Via) density required to route HBM4's 2,048-bit bus through a GPU die can be achieved with acceptable yield in 2026 production volumes. No public data on CG-HBM yield exists as of May 2026.

### 2. Can UALink Hardware Deliver Competitive Bandwidth vs NVLink 6.0 by Late 2026?
UALink 1.0 specifies 800 Gbps per Station — less than NVLink 6.0's 3,600 GB/s per GPU. For UALink to challenge NVLink, UALink 2.0 hardware at significantly higher bandwidth is required. The UALink consortium has not published a 2.0 specification timeline. Without competitive bandwidth, UALink becomes a cost-reduction play for lower-bandwidth workloads, not a NVLink replacement for high-performance training.

### 3. When Will FP4 Quantization Become Default in Production?
FP4 deployment is currently limited by calibration tooling maturity. NVFP4 achieves 88% lower quantization error, but requires careful calibration and may degrade certain model architectures. The question is whether automated FP4 calibration pipelines (analogous to LLM.int8() for FP8) will mature by H2 2026 to make FP4 the default inference precision. If yes, FP4's throughput advantages (2x over FP8) will be widely accessible. If calibration remains manual-expert work, FP4 stays niche.

### 4. Can AMD's ROCm Ecosystem Sustain Parity With CUDA Beyond Flagship Benchmarks?
ROCm 7 achieves flagship framework parity with CUDA. The open question is the long-tail: research frameworks, custom CUDA kernels in production ML stacks, domain-specific libraries (genomics, climate modeling, scientific computing). Each of these requires porting and optimization on ROCm. AMD's consumer GPU ROCm support (Radeon 7000/9000) broadens the developer base, but the kernel-level optimization gap remains. Can AMD sustain the investment required to maintain parity at scale?

### 5. What is the True Performance Ceiling of Chinese Domestic GPUs?
Moore Threads' Huagang "H100-class performance in 2026" claim on TSMC 6nm (vs NVIDIA's TSMC 4NP for H100) is technically suspicious. No independent benchmark exists. The cluster stability challenges reported by DigiTimes suggest hardware maturity issues beyond raw compute performance. Understanding the actual performance gap of Chinese domestic GPUs vs. global leaders is a critical intelligence question for the industry.

### 6. Will the 250kW+ Rack Standard Consolidate the Data Center Industry?
Only hyperscalers and specialized AI data center operators can deploy 250kW liquid-cooled racks at scale. Traditional enterprise data centers top out at 30-50kW per rack (air-cooled). Does this mean AI GPU compute permanently concentrates in hyperscaler facilities? Or do new cooling technologies (two-phase cooling, direct-to-silicon microfluidic) enable high-density AI GPU deployment in standard facilities?

### 7. How Will the NVIDIA-Intel Partnership Reshape the Ecosystem?
NVIDIA's $5B investment in Intel (September 2025) and Intel's NVLink commitment creates an unexpected alliance. Intel Xeon + NVIDIA Rubin NVL72-style systems combine Intel's enterprise CPU market presence with NVIDIA's GPU ecosystem. Does this displace AMD EPYC from AI server designs? Does it create a path for Intel to recover data center relevance? The competitive implications for AMD's integrated CPU+GPU strategy (MI430X with hybrid CPU+GPU support) are significant.

### 8. What Does HBM4 Actually Deliver in Production vs Specification?
HBM4 JEDEC specification (2,048-bit, 1.5+ TB/s per stack) represents peak theoretical bandwidth. Production HBM4 in real GPU packages, with thermal constraints, TSV IR drop, and routing limitations, typically achieves 85-92% of theoretical peak. For AMD MI400's 19.6 TB/s target, actual production bandwidth of 16-18 TB/s is more realistic. At what point does achievable HBM4 bandwidth vs. theoretical diverge, and how does this affect inference throughput projections?

---

## Source Index

| ID | Title | Tier | Date | Status |
|----|-------|------|------|--------|
| src-001 | NVIDIA Blackwell Enables 3x Faster Training | 4 | 2025-03-18 | VALIDATED |
| src-002 | AMD Instinct MI350X Architecture Specs | 4 | 2025-06-12 | VALIDATED |
| src-003 | AMD MI350 and CDNA4 Launched with ROCm 7 | 3 | 2025-06-12 | VALIDATED |
| src-004 | AMD CDNA4 Architecture Whitepaper | 4 | 2025-06-12 | VALIDATED |
| src-005 | AMD CDNA4 Deep Dive at Hot Chips 2025 | 1 | 2025-08-27 | VALIDATED |
| src-006 | Fifth-Generation NVIDIA NVLink 1,800 GB/s | 3 | 2025-02-01 | VALIDATED |
| src-007 | AMD RDNA4 Architecture Launch | 4 | 2025-02-28 | CONTEXT-ONLY |
| src-008 | AMD RDNA4 at Hot Chips 2025 | 1 | 2025-09-13 | CONTEXT-ONLY |
| src-009 | NVIDIA Rubin GPU 336B Transistors Roadmap | 3 | 2026-03-01 | VALIDATED |
| src-010 | NVLink 6.0 at CES 2026 Vera Rubin | 4 | 2026-01-06 | VALIDATED |
| src-011 | HBM3e vs HBM4 vs HBM4e LLM Inference Guide | 3 | 2026-02-01 | VALIDATED |
| src-012 | Blackwell Ultra AI Factory Platform | 4 | 2025-03-18 | VALIDATED |
| src-013 | Inside Blackwell Ultra Technical Blog | 4 | 2025-08-27 | VALIDATED |
| src-014 | MLPerf Inference v5.1 Results | 1 | 2025-09-10 | VALIDATED |
| src-015 | AMD MI350X/MI355X Launch Coverage | 3 | 2025-06-12 | VALIDATED |
| src-016 | NVIDIA Blackwell MLPerf Training Results | 1 | 2025-11-15 | VALIDATED |
| src-017 | NVIDIA RTX 5090 Blackwell Gaming GPU | 4 | 2025-01-26 | CONTEXT-ONLY |
| src-018 | NVIDIA DLSS 4 Multi Frame Generation | 4 | 2025-01-06 | CONTEXT-ONLY |
| src-019 | AMD ROCm 7.0 Software | 4 | 2025-06-12 | CONTEXT-ONLY |
| src-020 | Microbenchmarking NVIDIA Blackwell arXiv | 2 | 2025-12-03 | VALIDATED |
| src-021 | Dissecting Blackwell Architecture arXiv | 2 | 2025-07-14 | VALIDATED |
| src-022 | NVIDIA NVLink Fusion Announcement | 3 | 2025-05-19 | VALIDATED |
| src-023 | Nvidia extends NVLink to custom CPUs | 3 | 2025-05-19 | VALIDATED |
| src-024 | UALink 1.0 Specification Released | 3 | 2025-04-08 | VALIDATED |
| src-025 | TSMC CoWoS Capacity NVIDIA Dominance | 3 | 2025-12-10 | VALIDATED |
| src-026 | AMD MI400 CDNA5 Architecture Roadmap | 3 | 2025-12-01 | VALIDATED |
| src-027 | NVIDIA Vera CPU Architecture Detail | 3 | 2026-03-18 | VALIDATED |
| src-028 | NVIDIA GTC 2026 Vera Rubin Announcements | 4 | 2026-03-18 | VALIDATED |
| src-029 | GB200 NVL72 Deployment Guide | 3 | 2025-03-01 | VALIDATED |
| src-030 | NVIDIA DLSS 4.5 Six-Frame Generation | 4 | 2026-01-06 | VALIDATED |
| src-031 | Acc-SpMM GPU Tensor Core SpMM | 2 | 2025-01-16 | CONTEXT-ONLY |
| src-032 | SemiAnalysis InferenceMAX vLLM Blackwell | 3 | 2025-10-09 | VALIDATED |
| src-033 | NVIDIA Blackwell DeepSeek-R1 World Record | 4 | 2025-02-01 | VALIDATED |
| src-034 | Mind the Memory Gap IBM Research arXiv | 1 | 2025-03-11 | VALIDATED |
| src-035 | vLLM Large Scale DeepSeek 2.2k tok/s | 2 | 2025-12-17 | VALIDATED |
| src-036 | Moore Threads Huagang 5th Gen GPU | 3 | 2025-12-05 | VALIDATED |
| src-037 | AMD RDNA4 Navi 48 TechInsights Floorplan | 3 | 2025-03-10 | CONTEXT-ONLY |
| src-038 | RDNA4 Raytracing Improvements Analysis | 3 | 2025-03-15 | CONTEXT-ONLY |
| src-039 | Two-Phase Liquid Cooling Future of GPUs | 3 | 2025-10-15 | VALIDATED |
| src-040 | AMD MI350 to MI500 Roadmap 2027 | 3 | 2025-06-20 | VALIDATED |
| src-041 | FP8 Matrix Cores Sparsity MI300A arXiv | 2 | 2026-02-13 | VALIDATED |
| src-042 | Matrix Core Programming CDNA3 CDNA4 | 4 | 2025-07-01 | CONTEXT-ONLY |
| src-043 | Intel NVIDIA $5B Investment NVLink | 3 | 2025-09-18 | VALIDATED |
| src-044 | HBM3e and HBM4 IC Design Guide Siemens | 3 | 2026-04-24 | VALIDATED |
| src-045 | China GPU IPO Wave Moore Threads Biren | 3 | 2025-12-17 | VALIDATED |
| src-046 | NVIDIA GTC 2026 AWS Google Deployments | 3 | 2026-03-20 | VALIDATED |
| src-047 | Performance Per Watt GPUs 10-Year Overview | 3 | 2025-11-10 | VALIDATED |
| src-048 | Multipath Memory Access LLM Serving arXiv | 2 | 2025-12-19 | VALIDATED |
| src-049 | NVIDIA DGX Spark GB10 Personal AI PC | 4 | 2025-10-13 | CONTEXT-ONLY |
| src-050 | Blink CPU-Free LLM Inference arXiv | 2 | 2026-04-10 | VALIDATED |
| src-051 | AMD MLPerf Inference 6.0 Results | 1 | 2026-02-15 | VALIDATED |
| src-052 | ISSCC 2026 NVIDIA Broadcom CPO Coverage | 1 | 2026-02-17 | VALIDATED |

**Tier Distribution**: Tier 1 (peer-reviewed/benchmark): 8 | Tier 2 (arXiv): 8 | Tier 3 (industry analysis): 22 | Tier 4 (vendor): 14  
**Total sources**: 52 | **Validated**: 38 | **Context-only**: 14 | **Rejected**: 0
