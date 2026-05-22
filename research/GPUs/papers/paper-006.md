# Paper 006: NVIDIA Rubin GPU Architecture and NVLink 6.0

**Source ID**: src-009, src-010, src-028, src-046  
**Tier**: 3/4 (Industry Analysis + Vendor)  
**Date**: 2026-01-06 (CES 2026), 2026-03-18 (GTC 2026)  
**URL**: https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/

---

## One-Sentence Claim
NVIDIA Rubin GPU (336B transistors, TSMC 3nm, HBM4 memory, NVLink 6.0 at 3,600 GB/s) targets H2 2026 enterprise deployment in the Vera Rubin NVL72 platform, delivering 260 TB/s rack bandwidth and 3-4x compute density improvement over Blackwell using a novel CG-HBM (chip-on-GPU HBM) stacking approach.

## Methodology Summary
Rubin announced at multiple NVIDIA events: initial roadmap disclosure at Hot Chips / AI Infra Summit 2025, detailed specifications at CES 2026, and deployment timeline at GTC 2026. Micron confirmed HBM4 production for Rubin. Google Cloud and AWS commitments announced at GTC 2026. Architecture details from NVIDIA product announcements and industry analyst coverage.

## Quantitative Results
- **Transistors**: 336 billion (Rubin GPU die)
- **Process**: TSMC 3nm-class
- **Memory type**: HBM4 (first NVIDIA product)
- **NVLink version**: NVLink 6.0
- **NVLink 6.0 bandwidth**: 3,600 GB/s per GPU (2x over NVLink 5.0's 1,800 GB/s)
- **Vera Rubin NVL72 rack bandwidth**: 260 TB/s (2x over GB200 NVL72's 130 TB/s)
- **Compute density**: 3-4x improvement over Blackwell
- **CG-HBM**: Memory stacked directly on GPU die (novel approach)
- **HBM4 bandwidth (per stack)**: ~1.5+ TB/s (via 2,048-bit interface, 2x HBM3E's 1,024-bit)
- **Micron HBM4**: 36GB modules, 2.3x bandwidth improvement over previous gen
- **Process efficiency gain (3nm)**: 10-15% performance at same power, or 20-30% power reduction
- **Target deployment**: H2 2026 (enterprise); consumer cards late 2026 or early 2027
- **Vera CPU**: 88 custom Olympus Arm v9.2-A cores, 1.5 TB/s LPDDR5X bandwidth
- **Vera Rubin NVL72**: 72 Rubin GPUs + 36 Vera CPUs

## Stated Limitations
- Rubin Ultra reportedly scaled back from 4-die to 2-die design vs. earlier roadmap
- Production volume constrained by HBM4 supply (Micron confirmation of high-volume production still in progress)
- Consumer Rubin not yet officially announced as of May 2026
- TSMC 3nm capacity for Rubin competes with Apple, AMD, and others

## Inferred Limitations
- CG-HBM approach (memory stacked on GPU) is novel and untested at volume; thermal and yield risks
- 3,600 GB/s NVLink 6.0 requires upgraded NVLink switch silicon (new product required)
- 260 TB/s rack bandwidth at GB300 NVL72 power levels implies 300kW+ racks
- HBM4 supply concentrated at SK Hynix and Samsung; tight supply could limit Rubin ramp speed

## Architectural Significance
Rubin represents NVIDIA's second consecutive architecture on sub-5nm TSMC processes. The CG-HBM (on-die HBM stacking) is architecturally analogous to what AMD has done with CDNA chiplets but applied differently — stacking memory dies directly on the processor die eliminates the interposer layer, reducing access latency and potentially improving bandwidth-per-watt. NVLink 6.0 doubling to 3.6 TB/s maintains the pattern of interconnect doubling per generation. The Vera CPU with custom Olympus cores (rather than licensed Arm designs) signals NVIDIA's move to compete directly with AMD Epyc and AWS Graviton in datacenter CPUs.

## Cross-Paper Connections
- src-006 (NVLink 5.0) establishes baseline that NVLink 6.0 doubles
- src-044 (HBM4 design guide) covers the memory technology Rubin first deploys
- src-027 (Vera CPU) covers the CPU paired with Rubin in the superchip
- src-009 (Rubin roadmap analysis) provides broader roadmap context including Feynman
- src-047 (performance/watt trends) contextualizes NVIDIA's efficiency claims

## Theme Tags
`Rubin`, `NVLink-6.0`, `HBM4`, `CG-HBM`, `TSMC-3nm`, `Vera-CPU`, `NVL72`, `superchip`, `roadmap`, `2026`
