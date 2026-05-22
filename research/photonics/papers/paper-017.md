# Paper 017: AI Optical Transceiver Market — $26B by 2026, EML Supply Crisis

**Tags:** optical-interconnect  
**Date:** April 20, 2026  
**Source:** TrendForce / Cignal AI / Electronics Weekly  
**URL:** https://www.trendforce.com/presscenter/news/20260420-13017.html

## Summary

The global AI optical transceiver market expanded from $16.5B in 2025 to $26B in 2026 (57% YoY), driven by 800G mass deployment and 1.6T ramp. The primary constraint is a component shortage in 200G/lane EML (electro-absorption modulated laser) production, with Lumentum the only volume supplier, creating a critical bottleneck.

## Market Data

- **2025 market:** $16.5B
- **2026 market:** $26B (57% YoY growth)
- **800G units shipped (2025):** 24M+
- **800G units projected (2026):** 63M (2.6× increase)
- **1.6T units (2025):** <1M (pilot scale)
- **1.6T units (2026):** 5M+ (Cignal AI forecast)
- **1.6T module price:** $1,300-1,500 per module

## Enabling Technology: 200G/Lane EML

The transition from 800G to 1.6T is fundamentally gated by 200G/lane EML laser availability:
- 800G: uses 100G/lane EML (8 lanes × 100G = 800G)
- 1.6T: requires 200G/lane EML (8 lanes × 200G = 1.6T)
- 200G EML requires 100 GBaud modulation — complex III-V epitaxy
- **Only volume supplier:** Lumentum (as of early 2026)
- McKinsey forecast: 800G shortfall 40-60% through 2027; 1.6T shortfall 30-40% through 2029

## Strategic Response

**NVIDIA $4B Investment (March 2026):**
- Invested $2B in Lumentum
- Invested $2B in Coherent (alternative EML supplier)
- Explicit goal: secure priority access to scarce 200G EML capacity

## Technology Breakdown

### 800G Module Types (2025 mix)
- QSFP-DD800 and OSFP form factors dominant
- 800G DR8: 8×100G O-band, SR8: 8×100G multi-mode
- 800G FR4: 4×200G C-band (limited availability, higher power)

### 1.6T Module Types (2026 ramp)
- 1.6T DR8: 8×200G O-band (primary form factor)
- 1.6T FR4: 4×400G C-band (requires 400G/lane DSP)
- OSFP-XD dominant form factor (92% of hyperscale contracts in 2025)

## Silicon Photonics Share

- Si photonics share in 800G transceivers: ~40-45%
- Si photonics share in 1.6T modules: ~60% (higher due to integrated modulator advantage)

## LPO Market Disruption

LPO (Linear Pluggable Optics) threatens to disrupt DSP-based market:
- 800G LPO: <8.5W vs >16W for DSP module
- 50% power reduction enables lower TCO
- Arista, Cisco ToR switches deploying LPO 2025-2026
