# Paper 005: AMD RDNA4 Architecture — RX 9000 Series GPU Design

**Source ID**: src-007, src-008, src-037, src-038  
**Tier**: 1/3/4 (Hot Chips 2025 + Analysis + Vendor)  
**Date**: 2025-02-28 (launch), 2025-09-13 (Hot Chips)  
**URL**: https://www.amd.com/en/newsroom/press-releases/2025-2-28-amd-unveils-next-generation-amd-rdna-4-architectu.html

---

## One-Sentence Claim
AMD RDNA4 (Navi 48, 53.9B transistors, TSMC 4nm) doubles ray tracing performance over RDNA3, delivers 8x faster AI inference via redesigned matrix accelerators, and introduces 2nd-gen AI accelerators with INT8/INT4 sparsity — all in a monolithic design with enlarged L2 cache optimized for RT and AI workloads.

## Methodology Summary
Architecture presented at AMD's launch event February 28, 2025 and at Hot Chips 2025 (Stanford). Performance comparisons use published gaming benchmarks vs. RTX 4090 and RDNA3 predecessors. TechInsights independently analyzed the Navi 48 die floorplan. Chips and Cheese (Chester Lam) provided independent architectural analysis from Hot Chips presentation.

## Quantitative Results
- **Die size (Navi 48)**: 356.5 mm² on TSMC 4nm
- **Transistors**: 53.9 billion
- **Compute Units**: 64 CUs (4 Shader Engines × 16 DCUs)
- **AI Accelerators**: 128 per GPU (2 per CU)
- **Stream Processors**: 4,096 total
- **RT Accelerators**: 64 (3rd generation)
- **Memory**: 16GB GDDR6 on RX 9070 XT
- **L2 Cache**: Enlarged vs RDNA3 for RT workload efficiency
- **RX 9070 XT MSRP**: $599 (launched March 6, 2025)
- **RX 9070 MSRP**: $549
- **RT performance vs RDNA3**: 2x improvement in competitive RT games
- **AI inference vs RDNA3**: 8x faster at INT8/INT4 precision
- **Gaming**: 27-35% faster than RTX 4090 at 4K in most titles (for RTX 5090 context; RDNA4 competitive at $599 tier)
- **Modular design**: Navi 48 designed to be halved to produce lower-tier GPU variants

## Stated Limitations
- RT performance competitive in many scenarios but still behind NVIDIA's 4th-gen RT Cores with SER 2.0 in heavy RT workloads
- Gaming focus limits AI/compute capabilities vs. CDNA4 datacenter parts
- GDDR6 memory (not HBM) limits memory bandwidth compared to datacenter AI GPUs
- Consumer-tier product not designed for datacenter inference at scale

## Inferred Limitations
- Monolithic die (not chiplet) creates yield vulnerability as transistor counts grow beyond ~60B
- GDDR6 rather than GDDR7 (unlike NVIDIA RTX 5090) limits peak bandwidth for compute workloads
- FSR 4 AI super-resolution requires matrix accelerators, competing with gaming workloads for AI hardware
- RDNA4's AI accelerators are gaming-focus (neural rendering) not datacenter-class matrix operations

## Architectural Significance
RDNA4 represents AMD's most competitive consumer GPU response to NVIDIA in several years. Key advances: (1) The 3rd-gen RT accelerators with improved BVH traversal close the RT gap with NVIDIA Blackwell consumer GPUs significantly; (2) The 2nd-gen AI accelerators with sparsity support enable FSR4 (transformer-based super resolution) competing with DLSS 4; (3) The enlarged L2 cache design decision specifically to help RT workloads shows architecture-level RT optimization. The modular design philosophy — where Navi 48 can be bisected — reduces engineering cost for product-line segmentation. Hot Chips 2025 coverage confirmed the B-frame AV1 media encoder as a quality-of-life improvement for content creators.

## Cross-Paper Connections
- src-008 (Hot Chips 2025) provides the deepest technical details
- src-038 (RT improvements analysis) validates the 2x RT claim independently
- src-037 (TechInsights floorplan) provides silicon-level die analysis
- src-018 (DLSS4) covers competing NVIDIA AI super-resolution technology
- src-007 (RDNA4 launch press release) is primary vendor source

## Theme Tags
`RDNA4`, `ray-tracing`, `AI-accelerators`, `consumer-GPU`, `Navi-48`, `sparsity`, `TSMC-4nm`, `monolithic`, `FSR4`, `Hot-Chips-2025`
