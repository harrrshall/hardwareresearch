# paper-005: Optical Chip-to-Chip Interconnects — Silicon Photonics and Co-Packaged Optics in 2025-2026

**Tags:** optical-switching, chip-to-chip  
**Date:** 2025-2026  
**Source:** Multiple (NAND Research, OFC, EDN, Siemens, Ayar Labs)

---

## Summary

2025-2026 marks the inflection point for optical interconnects in AI data centers. Co-packaged optics (CPO) transitions from demonstration to early production deployment, with major announcements at OFC 2025 establishing 400 Gbps/lane as the next milestone. Energy efficiency — measured in pJ/bit — becomes the dominant KPI over raw bandwidth.

## Technology Landscape

### Pluggable Optics (Baseline)
- Current generation: 400G/800G QSFP-DD and OSFP modules
- Energy: 14–18 pJ/bit (800G generation)
- Range: up to 2 km (active optical cable) or 10–80 km (coherent)

### Near-Package Optics (NPO)
- Optical engine sits near (not on) package
- Reduces electrical reach, cuts ~40% vs pluggable
- Bridge between pluggable and full CPO

### Co-Packaged Optics (CPO)
- Optical engine co-packaged with switch/compute ASIC
- Energy: 3.5–6.75 pJ/bit (vs 15 pJ/bit pluggable)
- Key examples:
  - **Broadcom Tomahawk 6 (Davisson)**: 102.4 Tbps + CPO option, ~5.5 W per 800 Gbps port (~6–7 pJ/bit)
  - **NVIDIA Quantum-X (2H 2025)**: 1.6T per port CPO for InfiniBand scale-up
  - **NVIDIA Spectrum-X (2H 2026)**: 3.2T silicon photonics, 3.5x power efficiency, 400 Tbps total

### In-Die Optical I/O
- **Celestial AI Photonic Fabric Module**: World's first SoC with in-die optical I/O (Hot Chips 2025)
  - TSMC 5nm ASIC + photonic interposer + 2× HBM3e stacks
  - 7.2 Tbps optical connectivity per module
  - 16 Tbps optical chiplet (first generation)
  - 25x bandwidth, 10x lower latency vs CPO alternatives
  - **Marvell acquired Celestial AI for $3.25B** (announced November 2025)

## Bandwidth Race: Lane Rate Evolution

| Year | Per-Lane Rate | Interface |
|---|---|---|
| 2023 | 100 Gbps | 112G PAM4 |
| 2024 | 200 Gbps | 224G PAM4 |
| 2025 | 400 Gbps | 224 GBaud PAM4 (target) |
| 2026+ | 800 Gbps+ | TBD |

At OFC 2025, Accelink and others demonstrated 224 GBaud PAM4 achieving 400 Gbps/lane — a critical milestone for next-generation AI cluster interconnects.

## Ayar Labs UCIe Optical Chiplet (March 2025)

The world's first UCIe-compatible optical I/O chiplet:
- **TeraPHY**: 8 Tbps aggregate bandwidth
- **200 Gbps per mm** of chip edge (1000x electrical density)
- SuperNova 16-wavelength light source
- Memory disaggregation use case: up to **2 km** from compute with <2×5ns + TOF latency
- Compatible with UCIe 2.0 standard package

## Energy Efficiency Benchmarks

| Architecture | Total pJ/bit |
|---|---|
| Pluggable 400G | 24 |
| Near-Package Optics | 15 |
| CPO on MCM | 6.75 |
| CPO on Interposer | 3.5 |
| CEA-Leti electro-optical router (ISSCC 2026) | 3.19 |

## Market Forecast

- CPO market: **$95M (2025) → $1.05B (2034)** at 30.6% CAGR
- Early hyperscale deployment window: 2026–2027
- "All AI data center interconnects will be optical within 5 years" — Semiconductor Engineering consensus

## Strategic Observations

- The Marvell/Celestial AI acquisition consolidates in-die optical I/O IP with Teralynx switch and CXL memory portfolios
- Wafer-level CPO with aggressive WDM targets 2–4 Tbps/mm fiber-coupled optical links near-term; 10 Tbps/mm by end of decade
- pJ/bit has replaced Gbps as the primary KPI in hyperscale optical procurement
