# Paper 020: AMD Threadripper PRO 9000 WX-Series — Zen 5 Workstation Benchmark Analysis

**Source ID**: src-025  
**Date**: 2025-07-23  
**Venue**: AMD Corporate Blog, Phoronix, BOXX Technologies

---

## One-Sentence Claim
AMD Threadripper PRO 9000 WX-Series with up to 96 Zen 5 cores delivers 16% IPC uplift and beats Intel Xeon W9-3595X by 28–145% across professional workloads, with 25% improvement in the SPECworkstation 4.0 AI/ML benchmark.

## Methodology Summary
AMD internal benchmarking against Threadripper PRO 7995WX (Zen 4) and Intel Xeon W9-3595X (60-core Intel Sapphire Rapids-based). Third-party validation by Phoronix on AMD-provided hardware. Professional workload benchmarks include SPECworkstation 4.0, V-Ray, KeyShot, Adobe After Effects, Blender, and DeepSeek R1 inference. Available from Dell, HP, Lenovo, and Supermicro.

## Quantitative Results
- **Max cores**: 96 Zen 5 cores (9995WX)
- **IPC uplift vs Threadripper PRO 7000 (Zen 4)**: 16% (fixed frequency)
- **AI/ML improvement (SPECworkstation 4.0)**: 25% over Threadripper PRO 7000
- **vs 96-core Threadripper PRO 7995WX (gen-over-gen)**:
  - Workstation benchmarks: 13–26% faster
  - DeepSeek R1 inference: 22–23% faster
- **vs Intel Xeon W9-3595X (60-core)**:
  - Professional workloads: 28–145% faster depending on task
  - V-Ray render: 2.4x faster
  - KeyShot: 2.2x faster
  - Adobe After Effects: +78%
- **Memory**: 8-channel DDR5-6400
- **PCIe**: PCIe 5.0
- **Launch date**: July 23, 2025
- **OEM availability**: Dell Technologies, HP, Lenovo, Supermicro

## Stated Limitations
AMD's 28–145% advantage range vs. Intel Xeon W9-3595X partly reflects AMD's 96-core vs. Intel's 60-core count advantage, not purely IPC improvement. Per-core comparisons narrow the gap significantly. The 145% ceiling applies to highly parallel workloads (V-Ray, Blender) that scale efficiently with core count.

## Inferred Limitations
- 96 Zen 5 cores at full load are thermally and power-constrained; sustained workstation use may not maintain peak clock speeds across all 96 cores simultaneously
- 8-channel DDR5-6400 memory is adequate but narrower than EPYC server configurations with 12-channel DDR5; memory bandwidth may limit performance in memory-bound workloads
- Intel's Xeon W9-3595X comparison uses Intel's workstation Sapphire Rapids platform which is already somewhat dated; future Xeon W products (presumably on newer nodes) may narrow the gap
- DeepSeek R1 inference improvements (22-23%) are relevant but modest — dedicated AI accelerators (GPU, NPU) vastly outperform CPU inference for large model deployments

## Architectural Significance
Threadripper PRO 9000 demonstrates AMD's ability to scale Zen 5 from consumer (9950X, 16 cores) to HEDT (9995WX, 96 cores) on a common architecture platform. The 25% AI/ML improvement in SPECworkstation 4.0 is significant for the growing AI workstation market — a Threadripper PRO workstation can accelerate local AI inference competitively with a discrete GPU for smaller models. The 8-channel DDR5-6400 memory configuration is meaningfully faster than prior-gen Threadripper PRO 7000's DDR5-5200, providing important bandwidth for content creation and scientific workloads. The product's availability from Dell, HP, Lenovo, and Supermicro (all simultaneously at launch) indicates AMD's mature supply chain and strong OEM relationships at the premium workstation tier.

## Cross-Paper Connections
- **paper-001 (Zen 5 architecture)**: Same core architecture deployed in workstation format
- **paper-003 (EPYC Turin)**: Server counterpart showing how the same Zen 5 architecture scales across market segments
- **paper-018 (Ryzen 9 9950X3D)**: Consumer flagship at the other end of the AMD desktop range

## Theme Tags
`AMD`, `Threadripper-PRO`, `Zen-5`, `workstation-CPU`, `high-core-count`, `IPC-improvement`, `DDR5`, `PCIe-5`, `professional-workloads`
