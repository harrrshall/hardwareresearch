# paper-017: TSMC CoWoS Advanced Packaging — Chiplet Substrate for AI Interconnect

**Tags:** chip-to-chip, UCIe  
**Date:** 2025-2026  
**Source:** SemiWiki, TSMC, CNBC  
**URL:** https://semiwiki.com/forum/threads/cowos-capacity-set-to-skyrocket-by-2026-massive-growth-in-advanced-packaging.21773/

---

## Summary

TSMC's CoWoS (Chip-on-Wafer-on-Substrate) is the dominant advanced packaging platform for AI accelerator chips in 2025–2026. NVIDIA holds >70% of capacity, constraining competitors. TSMC is doubling capacity at 80% CAGR to meet demand, while transitioning from CoWoS-S (silicon interposer) to CoWoS-L (LSI bridge) for multi-chiplet configurations.

## CoWoS Variant Comparison

| Variant | Description | Interconnect Density | Application |
|---|---|---|---|
| CoWoS-S | Silicon interposer | Highest (microbump) | Single GPU + HBM (H100/H200) |
| CoWoS-L | LSI Bridge (chiplet stitching) | High | Multi-chiplet (Blackwell, Rubin) |
| CoWoS-R | Redistribution layer (RDL) | Medium | Lower-cost option |
| CoWoS + SoIC-X | 3D hybrid bond stack | Highest | Future compute stacking |

## CoWoS-L for Blackwell/Rubin

As AI chip complexity exceeds single-reticle dimensions (~858 mm² maximum):
- NVIDIA GB200 uses **CoWoS-L**: bridges multiple chiplets via Local Silicon Interconnect (LSI) pads
- Interconnect between compute die and HBM stacks routes through the LSI bridge
- Die-to-HBM bump pitch: ~40–55 µm on CoWoS-L substrate
- HBM3e to CoWoS-L bandwidth: ~2 TB/s per stack, 8 stacks = ~16 TB/s total substrate capability

## Rubin Platform Packaging

NVIDIA Rubin (H2 2026) combines:
- **CoWoS-L** for horizontal die stitching (multiple Rubin GPU chiplets + HBM4)
- **SoIC** (System on Integrated Chips) for 3D vertical stacking
- This combination enables shorter vertical interconnects with SRAM or other dies stacked on compute

## Capacity and Supply

| Year | CoWoS Capacity (est.) | Growth |
|---|---|---|
| 2023 | Baseline | — |
| 2024 | 1.5x baseline | +50% |
| 2025 | 2.5x baseline | +67% |
| 2026 | 4–5x baseline | +60–100% |

- 80% CAGR but demand still outpaces supply
- NVIDIA secured >70% of 2025 CoWoS allocation
- AMD MI350, Trainium3, Google Ironwood all compete for remaining capacity

## TSMC COUPE — Co-packaged Optics Integration

At OFC 2025 / IFTLE 642 (October 2025), TSMC demonstrated:
- **COUPE** (Co-packaged optics for ultra-high-performance compute): integrates optical engines within CoWoS substrate
- Combines silicon photonics PIC (Photonic Integrated Circuit) with compute/switch ASIC on single CoWoS-L substrate
- Target: >10 Tbps/mm optical bandwidth density at package edge

## UCIe on CoWoS

CoWoS-L enables UCIe Advanced Package connections:
- UCIe-A at 64 GT/s (UCIe 3.0) requires advanced package bump pitch <55 µm
- CoWoS-L with 40 µm bumps supports full UCIe-A bandwidth
- Enables multi-vendor chiplet assembly (AMD chiplets + Intel I/O + TSMC memory) on a single substrate

## Strategic Observations

- CoWoS is the single most supply-constrained element in the AI accelerator supply chain (2025)
- TSMC's COUPE demonstrates that CPO will integrate into packaging substrates, not just switch ASICs
- Intel's EMIB-T competes directly with CoWoS for HBM4 integration contracts from non-TSMC customers
- As packaging becomes strategic, TSMC has a second revenue moat beyond leading-edge lithography
