# Paper 014: NVIDIA DGX Spark — GB10 Grace Blackwell Personal AI Supercomputer

**Source ID**: src-049  
**Tier**: 4 (Vendor Disclosure)  
**Date**: 2025-10-13  
**URL**: https://nvidianews.nvidia.com/news/nvidia-puts-grace-blackwell-on-every-desk-and-at-every-ai-developers-fingertips

---

## One-Sentence Claim
The NVIDIA DGX Spark launches October 2025 at $3,000 with the GB10 superchip (TSMC 3nm, 1 PFLOP FP4, 140W), combining a MediaTek CPU tile and NVIDIA Blackwell GPU tile via NVLink C2C at 600 GB/s into 128GB unified LPDDR5X memory — marking the first personal AI workstation with datacenter-class Blackwell architecture.

## Methodology Summary
Product launched October 15, 2025. GB10 chip co-designed between NVIDIA and MediaTek (MediaTek provides CPU chiplet). Technical details from NVIDIA Hot Chips 2025 GB10 presentation. Specifications verified from product page and retail availability (BestBuy, Amazon, Newegg).

## Quantitative Results
- **Launch date**: October 15, 2025
- **Price**: Starting ~$3,000
- **Process**: TSMC 3nm for both CPU and GPU dies
- **NVLink C2C bandwidth**: 600 GB/s bidirectional (CPU-GPU)
- **CPU cores**: 20 Arm v9.2 (10x Cortex X925 + 10x Cortex A725)
- **Memory**: 128GB unified LPDDR5X
- **GPU compute**: 1 PFLOP FP4 / 31 TFLOPS FP32
- **TDP**: 140W (vs RTX 5070's 250W, despite Blackwell GPU)
- **Storage**: 4TB NVMe M.2
- **Packaging**: TSMC 2.5D advanced packaging connecting CPU and GPU dies
- **GPU die**: Full Blackwell architecture including 5th-gen tensor cores, FP4 support
- **LLM capability**: Runs models at 1 PFLOP FP4, sufficient for 70B parameter models
- **Compared to H100**: B10 GPU is a mobile/workstation-class Blackwell, not datacenter class

## Stated Limitations
- 140W TDP limits maximum sustained GPU clock vs. full-power B200 at 1000-1400W
- 1 PFLOP FP4 is ~150x less than B200's 9+ PFLOPS FP4 (per-GPU)
- No NVLink scale-out; single system unit only (no multi-DGX Spark NVLink fabric)
- LPDDR5X instead of HBM3E limits memory bandwidth to fraction of datacenter GPU levels

## Inferred Limitations
- 128GB unified memory is impressive but shared CPU-GPU bandwidth (600 GB/s) less than HBM3E's 8 TB/s
- Workstation use case limits to inference and small-scale fine-tuning; full-scale training requires datacenter GPUs
- $3,000 price is extremely high relative to consumer GPU price/performance for non-professional use
- CPU is MediaTek design (mobile-class Arm, not server-class Neoverse); limits server workload efficiency

## Architectural Significance
DGX Spark is architecturally significant as proof that the NVLink C2C CPU-GPU integration paradigm scales down to workstation power envelopes. The 600 GB/s NVLink C2C (from datacenter Grace Hopper architecture) provides CPU-GPU memory coherence bandwidth that PCIe can never match. This makes DGX Spark capable of running multi-modal AI tasks where CPU pre-processing feeds GPU inference continuously without PCIe bottleneck. The co-design with MediaTek demonstrates NVIDIA's NVLink Fusion approach in practice — MediaTek CPU + NVIDIA GPU tile in one package via NVIDIA's chiplet interface. At 140W with 1 PFLOP FP4, the energy efficiency (TFLOPS/W) of Blackwell architecture is validated at mobile-class power levels.

## Cross-Paper Connections
- src-022 (NVLink Fusion) covers the architecture enabling CPU-GPU chiplet integration
- src-012 (memory bottleneck) shows why high CPU-GPU bandwidth matters for LLM inference
- src-001 (Blackwell overview) covers the full datacenter Blackwell that GB10 is derived from
- src-005 (Hot Chips 2025) covers NVIDIA's GB10 presentation at the conference

## Theme Tags
`DGX-Spark`, `GB10`, `Grace-Blackwell`, `NVLink-C2C`, `workstation-AI`, `chiplet-GPU`, `MediaTek`, `personal-AI`, `unified-memory`, `FP4`
