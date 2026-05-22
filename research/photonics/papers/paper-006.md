# Paper 006: TSMC COUPE — Compact Universal Photonic Engine for CPO

**Tags:** co-packaged-optics, silicon-photonics  
**Date:** 2025–2026  
**Source:** TrendForce / TSMC / Tweaktown / IDTechEx  
**URL:** https://www.trendforce.com/news/2026/04/01/news-silicon-photonics-race-intensifies-as-tsmc-targets-2026-coupe-production-samsung-eyes-2029-cpo-turnkey/

## Summary

TSMC's Compact Universal Photonic Engine (COUPE) is the central packaging technology enabling CPO deployments for NVIDIA, Broadcom, and Marvell. COUPE uses SoIC-X chip stacking to bond an electrical ASIC die on top of a silicon photonic die, creating a unified package with the lowest electrical-optical interface impedance.

## Key Technical Specifications

- **Technology:** SoIC-X (3D chip stacking)
- **Interface:** Electrical die directly bonded to photonic die
- **Power improvement:** 5–10× vs conventional pluggable approaches
- **Latency reduction:** 10–20× lower than pluggable optics
- **Volume production target:** 2026 (in production for small form factor pluggables in 2025)
- **CPO integration:** CoWoS packaging for switch ASICs entering production 2026

## Architecture Notes

COUPE stacks electrical IC over silicon photonic IC using SoIC-X die bonding with sub-10µm pitch. This approach:
1. Minimizes electrical trace length between SerDes and optical modulator
2. Achieves lowest impedance at die-to-die boundary
3. Supports future photonic die upgrades without changing ASIC
4. Integrates with CoWoS interposer for full switch package

## Ecosystem Partners

- **NVIDIA:** Spectrum-X Photonics, Quantum-X Photonics switches
- **Broadcom:** Tomahawk 6 Davisson (102.4 Tbps)
- **Marvell / Celestial AI:** Custom XPU + CPO integration

## Competitive Landscape

| Foundry | Platform | CPO Volume Timeline |
|---------|----------|-------------------|
| TSMC | COUPE + CoWoS | 2026 |
| Samsung | CPO Turnkey | 2029 |
| GlobalFoundries | AMF-enhanced SiPho | 2026-2027 |

## Significance

TSMC's COUPE essentially defines the packaging standard for first-generation commercial CPO. Because both NVIDIA and Broadcom use TSMC, COUPE creates a single converged platform that simplifies supply chain for early CPO adopters.
