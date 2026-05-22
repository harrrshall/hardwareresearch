# Paper 013: SOCAMM2 — New AI Server Memory Form Factor, 192 GB at 2x DDR5 Bandwidth

**Source ID**: 40, 41  
**Source Title**: SK Hynix Begins Mass Production of 192 GB SOCAMM2; SOCAMM Memory Gains Ground  
**URLs**:  
- https://news.skhynix.com/mass-production-socamm2-192gb/  
- https://www.networkworld.com/article/4112926/socamm-memory-gains-ground-as-ai-data-centers-proliferate.html  
**Date**: 2026  
**Tags**: SOCAMM2, LPDDR5X, form-factor, AI-server, SK-Hynix, Micron

---

## One-Sentence Claim
SK Hynix has begun mass production of 192 GB SOCAMM2 modules using 1cnm LPDDR5X, a new 14×90mm AI-server memory form factor that delivers 2x the bandwidth of DDR5 RDIMM at 55% of the power, designed specifically for NVIDIA Vera Rubin's Grace CPU.

## Methodology Summary
SOCAMM2 (Small Outline Compression Attached Memory Module) uses LPDDR5X DRAM in a compression-attach module format. SK Hynix's 192 GB variant uses its 1cnm (1-gamma equivalent) process LPDDR5X. The form factor was developed to bring data-center-class modular DRAM to AI server platforms where RDIMM power efficiency is inadequate. Micron also produces SOCAMM2, qualifying alongside SK Hynix for Vera Rubin.

## Quantitative Results
- Module capacity: 192 GB per SOCAMM2 module
- Physical dimensions: approximately 14 × 90 mm (1/3 footprint of standard RDIMM)
- Bandwidth vs DDR5 RDIMM: 2x improvement
- Power consumption vs DDR5 RDIMM: 55% (45% power reduction)
- Performance vs standard DDR5: 1.5x to 2.0x
- Process: SK Hynix 1cnm (1c-nm, 1-gamma tier) LPDDR5X
- Launch timing: Q2 2026 with NVIDIA Vera Rubin platform

## Stated Limitations
- Based on LPDDR5X; LPDDR6 transition needed for next-generation bandwidth targets
- Limited number of qualified suppliers (SK Hynix, Micron) reduces competition
- Compression-attach mechanism requires precision PCB design; not hot-swappable

## Inferred Limitations
- 192 GB capacity per module may still be insufficient for future multi-trillion parameter LLM serving without multi-module configs
- LPDDR5X has reached its bandwidth ceiling; SOCAMM2 designed for LPDDR6 upgrade path
- Form factor compatibility is platform-specific (initially Grace CPU only), limiting broad adoption

## Architectural Significance
SOCAMM2 is architecturally significant as it brings mobile LPDDR power efficiency to the data center, bridging the gap between ultra-high-bandwidth HBM (for GPU) and conventional DDR5 RDIMM (for CPU). In the Vera Rubin architecture, the Grace CPU uses SOCAMM2 while the Blackwell GPU uses HBM4 — a tiered memory architecture that maximizes both bandwidth and power efficiency at the system level.

## Cross-Paper Connections
- Pairs with HBM4 in NVIDIA Vera Rubin system (paper-007): HBM4 for GPU side, SOCAMM2 for CPU side
- Uses LPDDR5X today; roadmap aligned with LPDDR6 standard (paper-004) for next generation
- Micron's SOCAMM2 (paper-003 ecosystem) is produced alongside HBM4 for Vera Rubin
- JEDEC's LPDDR6 roadmap (paper-019) specifically previewed SOCAMM2 data center expansion

## Theme Tags
SOCAMM2, LPDDR5X, form-factor, AI-server, SK-Hynix, Micron, Vera-Rubin, Grace-CPU, power-efficiency
