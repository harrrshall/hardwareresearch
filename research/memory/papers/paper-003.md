# Paper 003: Micron HBM4 — High-Volume Production for NVIDIA Vera Rubin

**Source ID**: 9, 10  
**Source Title**: Micron in High-Volume Production of HBM4 for NVIDIA Vera Rubin; 2.3x Bandwidth Improvement  
**URLs**:  
- https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin  
- https://www.tomshardware.com/pc-components/dram/micron-enters-high-volume-production-of-hbm4-for-nvidia-vera-rubin  
**Date**: 2026-04  
**Tags**: HBM4, Micron, Vera-Rubin, 1-gamma, bandwidth, production

---

## One-Sentence Claim
Micron has entered high-volume production of HBM4 36GB 12H targeting NVIDIA Vera Rubin, achieving >2.8 TB/s bandwidth at >11 Gbps per pin — a 2.3x bandwidth improvement over HBM3E with 20% better power efficiency, on its 1-gamma DRAM process.

## Methodology Summary
Micron's HBM4 uses its 1-gamma (6th-generation 10nm-class) DRAM process for core dies. The company has demonstrated advanced packaging capability with both 12H (36 GB, volume production) and 16H (48 GB, customer samples) configurations. Micron entered high-volume production in Q1 2026 with all 2026 capacity already allocated under multi-year agreements.

## Quantitative Results
- Config in production: 36 GB 12H
- Pin speed: >11 Gbps per pin
- Bandwidth: >2.8 TB/s per stack (2.3x vs Micron HBM3E)
- Power efficiency: >20% improvement vs HBM3E
- Sample config: 48 GB 16H (33% capacity increase per HBM placement vs 36 GB 12H)
- 2026 capacity: 100% sold out under multi-year agreements
- Micron HBM annualized revenue run-rate: ~$8 billion (projected)
- DRAM process: 1-gamma (1γ, 6th-gen 10nm-class): 20% lower power, 15% higher perf, 30% better bit density vs 1-beta

## Stated Limitations
- Micron is the third HBM4 volume producer behind SK Hynix and Samsung
- 48 GB 16H is still in sample phase as of April 2026; volume production timing not confirmed
- HBM market share at 21% vs SK Hynix 57% in Q3 2025

## Inferred Limitations
- "Sold out" capacity signals Micron is supply-constrained, not demand-constrained — limiting revenue upside
- 1-gamma process transition risk: first major HBM product on this node
- Micron's packaging ecosystem maturity for 16H stacking lags SK Hynix's established processes

## Architectural Significance
Micron's HBM4 with 2.3x bandwidth improvement over HBM3E demonstrates that per-stack bandwidth improvements follow a non-linear trajectory as interface width doubles and pin speeds increase simultaneously. The 1-gamma process introduction for HBM4 positions Micron to compete on power efficiency, which becomes increasingly critical as GPU TDPs approach 1kW+ in Vera Rubin class systems.

## Cross-Paper Connections
- One of three suppliers for NVIDIA Vera Rubin HBM4 (paper-007) alongside SK Hynix and Samsung
- Micron's 1-gamma process also being used for LPDDR5 qualification (paper-004 ecosystem)
- Micron also in production of 192 GB SOCAMM2 (paper-013) for same Vera Rubin platform
- HBM market share competition (paper-011): Micron gained from 6% in 2023 to 21% in 2025

## Theme Tags
HBM4, Micron, 1-gamma, bandwidth, Vera-Rubin, production, 12H, 16H
