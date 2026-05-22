# Paper 007: NVIDIA Vera Rubin NVL72 — HBM4 Memory Architecture

**Source ID**: 13  
**Source Title**: NVIDIA Vera Rubin NVL72 — Co-Designed Infrastructure for Agentic AI  
**URL**: https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/  
**Date**: 2026-01 (CES 2026 announcement; H2 2026 deployment)  
**Tags**: Vera-Rubin, HBM4, NVIDIA, AI-accelerator, NVL72

---

## One-Sentence Claim
NVIDIA's Vera Rubin NVL72 rack-scale system delivers 288 GB HBM4 per GPU and 22.2 TB/s total HBM4 bandwidth, targeting 50 PFLOPS FP4 compute per GPU from three qualified HBM4 suppliers (SK Hynix, Samsung, Micron).

## Methodology Summary
Vera Rubin uses a multi-chip GPU architecture with 8 HBM4 stacks per GPU die. The NVL72 integrates 72 GPUs in a rack-scale system. NVIDIA upgraded the HBM4 bandwidth specification mid-cycle by 10% to maintain competitive positioning against AMD MI400. Three vendors (SK Hynix, Samsung, Micron) have been qualified as HBM4 suppliers, reducing single-source risk.

## Quantitative Results
- HBM4 capacity per GPU: 288 GB
- Total NVL72 HBM4 capacity: 20.7 TB (72 GPUs × 288 GB)
- HBM4 bandwidth per GPU (updated): 22.2 TB/s
- Compute performance per GPU: 50 PFLOPS FP4
- HBM4 stacks per GPU: 8 (each at ~2-3 TB/s per stack depending on configuration)
- H2 2026: target deployment window
- NVIDIA B300 GPU (predecessor): 288 GB HBM3E, 8 TB/s bandwidth, 15 PFLOPS FP4

## Stated Limitations
- H2 2026 deployment means full production availability is at least 6 months from announcement
- NVIDIA upgraded bandwidth spec "to stay ahead of AMD" — suggests competitive pressure forcing spec changes
- Three-supplier strategy adds logistical complexity for matched-spec HBM4 across vendors

## Inferred Limitations
- 22.2 TB/s total per-GPU HBM4 bandwidth implies ~2.77 TB/s per stack — achievable by all three suppliers but at different efficiency points
- At 50 PFLOPS FP4 with 288 GB memory, the memory-to-compute ratio is lower than training-optimized clusters, suggesting inference as primary use case
- Power envelope per NVL72 rack likely exceeds 100 kW, requiring immersion or direct liquid cooling

## Architectural Significance
Vera Rubin represents the industry's first major deployment of HBM4 at scale, validating the 2,048-bit interface in production AI infrastructure. The three-vendor qualification strategy is architecturally significant as it signals NVIDIA's intent to treat HBM4 as a commodity supply component rather than a differentiating vendor lock-in. The 20.7 TB total per-rack HBM4 capacity is a landmark for large-model in-memory inference.

## Cross-Paper Connections
- Requires HBM4 from all three major suppliers (papers 001, 002, 003)
- AMD MI400 (paper-008) is the direct competitor with 432 GB HBM4 at 19.6 TB/s (more capacity, different trade-off)
- SOCAMM2 192 GB (paper-013) is used for the Vera Rubin platform's CPU-side memory (Grace CPU)
- Memory wall analysis (paper-018) makes the bandwidth case for why 22.2 TB/s is needed for LLM serving

## Theme Tags
Vera-Rubin, HBM4, NVIDIA, NVL72, rack-scale, AI-accelerator, 50PFLOPS, 288GB
