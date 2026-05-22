# Paper 015: Backside Power Delivery Network — Technology Overview and Industry Adoption

**Source ID:** 13, 14  
**Authors:** Semiconductor Engineering / Tom's Hardware / FutureMarketInsights  
**Venue:** Semiconductor Engineering / Tom's Hardware / Market Reports  
**Date:** 2025  
**Tags:** BSPDN, 2nm  
**URL:** https://semiengineering.com/backside-power-delivery-creates-fab-tool-thermal-dissipation-barriers/

## Abstract / Summary

Backside Power Delivery Networks (BSPDN) represent a fundamental architectural change in chip manufacturing: relocating power distribution from the transistor front-side (traditional) to the silicon backside. This eliminates the conflict between power routing and signal routing at the most congested metal layers, enabling better logic density and reduced IR drop. Intel's PowerVia (shipping with 18A), TSMC's Super Power Rail (A16), and Samsung's BSPDN (SF2Z) represent the three primary industry implementations.

## Key Technical Data

- **BSPDN market size (2025):** USD 14.3 million
- **BSPDN market projection (2035):** USD 51.5 million (13.7% CAGR)
- **3nm chips segment (2025):** 61% of BSPDN market
- **Density improvement:** >20% circuit density increase vs. frontside PDN implementations
- **Power reduction:** Up to 30% in HPC applications
- **Traditional PDN metal layers:** 7-9 layers partially for power
- **BSPDN metal layers:** 2-3 dedicated backside layers (freeing frontside)
- **IR drop reduction (Intel PowerVia measured):** ~4% ISO-power performance improvement
- **Intel 18A standard cell utilization (PowerVia):** +5-10% vs. Intel 3 without BSPDN
- **TSMC A16 SPR production:** Q4 2026 risk; HVM 2027
- **Samsung SF2Z (with BSPDN) production:** 2027

## Key Findings

1. BSPDN is the most significant power delivery innovation since multi-layer metal routing was introduced in the 1990s.
2. All three leading foundries/IDMs (TSMC, Intel, Samsung) have BSPDN implementations in active development or production.
3. Intel is the earliest commercial deployer (18A in HVM from Oct 2025); TSMC follows with A16 in 2026-2027.
4. The fabrication challenge for BSPDN includes: wafer bonding/thinning, backside reveal/etch, and TSV formation after front-side processing.
5. Thermal dissipation is a secondary BSPDN challenge — heat must now route through the silicon substrate, potentially increasing junction temperatures.

## Relevance to Research Window (2025-11-22 to 2026-05-22)

Intel 18A with PowerVia is in HVM during the entire research window (Oct 2025 start). TSMC A16 SPR preparation is active. Samsung SF2Z planning proceeding. BSPDN is one of the defining technology themes of the window.
