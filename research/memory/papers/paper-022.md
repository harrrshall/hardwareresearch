# Paper 022: MRAM and FeRAM — Emerging Non-Volatile Memory for AI 2025

**Source ID**: 50, 51  
**Source Title**: Progress of Emerging NVM Technologies; In-Memory Analog Computing Landscape 2026  
**URLs**:  
- https://link.springer.com/article/10.1557/s43579-024-00660-2  
- https://www.patsnap.com/resources/blog/articles/in-memory-analog-computing-landscape-2026/  
**Date**: 2024-2025  
**Tags**: MRAM, FeRAM, NVM, emerging-memory, STT-MRAM, AI-hardware

---

## One-Sentence Claim
STT-MRAM entered production with Everspin targeting 64Mb/128Mb chips for AI in 2025 and Netsol scaling from 28nm to 14nm in 2026, while as of 2025 no single non-volatile memory technology (RRAM, MRAM, FeRAM, PCM) has emerged as the definitive winner for analog in-memory computing AI accelerators.

## Methodology Summary
Review of industrial and academic developments in STT-MRAM, FeRAM (including HfO2-based FeFET variants), and RRAM (resistive RAM). Patent landscape analysis from PatSnap covering 2025 filings. Assessment of production readiness from company announcements and MRS/IEEE publications.

## Quantitative Results
- STT-MRAM: entering production; Everspin targets 64Mb, 128Mb chips in 2025
- Netsol MRAM node scaling: 28nm → 14nm by 2026
- FeRAM retention/latency: ~50-100ns operation, low power
- MRAM vs conventional DRAM: near-performance in non-volatile caching and in-memory logic
- FeRAM advantage: ultra-low-power binary neural network inference
- HfO2 FeRAM concerns: wake-up effect, fatigue mechanisms affect reliability
- Voltage-controlled magnetization switching: potential for low-energy writes (no specified quantitative improvement)

## Stated Limitations
- HfO2 FeRAM: wake-up effect and fatigue limit reliability lifetime
- FeRAM processing temperature: <650°C constraint limits integration with CMOS back-end processes
- No NVM technology has achieved analog CiM AI accelerator production readiness
- Everspin's 64Mb/128Mb targets are small vs GBs of DRAM needed for AI inference

## Inferred Limitations
- MRAM density at 14nm still lags DRAM density by ~10x, preventing MRAM from replacing DRAM at scale
- STT-MRAM write energy, while lower than Flash, is still higher than SRAM, limiting use as working memory
- The multi-vendor research fragmentation (each vendor pursuing different NVM type) delays standardization

## Architectural Significance
Despite significant research investment, NVM is not replacing DRAM in AI accelerators in the 2025-2026 timeframe. Instead, NVM occupies niche roles: MRAM for non-volatile cache (between L3 cache and DRAM), FeRAM for ultra-low-power edge inference, and PCM for storage-class memory. The "no clear winner" status reflects that each NVM type has a workload-specific advantage, preventing consolidation around a single technology.

## Cross-Paper Connections
- NVM context positions DRAM (papers 001-003) as dominant for foreseeable future
- FeRAM and MRAM compute-in-memory concepts parallel LPDDR6-PIM (paper-011)
- IGZO DRAM (paper-009) is itself an emerging memory technology competing in this space
- Data center NVM could complement CXL tiering (paper-005) as storage-class memory tier

## Theme Tags
MRAM, STT-MRAM, FeRAM, FeFET, NVM, emerging-memory, HfO2, analog-CiM, Everspin
