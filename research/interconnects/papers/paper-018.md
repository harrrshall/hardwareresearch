# paper-018: Celestial AI Photonic Fabric — In-Die Optical Interconnect and Marvell Acquisition

**Tags:** optical-switching, chip-to-chip  
**Date:** 2025  
**Source:** ServeTheHome Hot Chips 2025 / Optics.org / Monthly Pulse  
**URL:** https://www.servethehome.com/celestial-ai-photonic-fabric-module-at-hot-chips-2025/

---

## Summary

Celestial AI presented the world's first SoC with in-die optical I/O at Hot Chips 2025, delivering the Photonic Fabric Module (PFM) with 7.2 Tbps optical connectivity. Marvell Technologies announced the acquisition of Celestial AI for $3.25B in November 2025, consolidating the most advanced in-die optical I/O technology with Marvell's switch and CXL portfolio.

## Photonic Fabric Module (PFM) Specifications

| Parameter | Value |
|---|---|
| ASIC process | TSMC 5nm |
| Package type | 2.5D |
| Package contents | TSMC 5nm ASIC + photonic interposer + 2× HBM3e stacks + Fiber Array Unit |
| Optical connectivity | **7.2 Tbps** per module |
| Optical chiplet generation | 1st-gen (16 Tbps peak for standalone chiplet) |
| Bandwidth vs CPO | 25x greater |
| Latency vs CPO | 10x lower |

## First-Gen Optical Chiplet

Celestial AI's first generation photonic chiplet:
- **16 Tbps bandwidth** — highest announced optical chiplet as of 2025
- Integrates electrical and optical components in a compact form factor
- Photonic elements placed **below the main AI-compute ASIC** (novel topology enabling tighter integration than co-packaged approaches)

## Comparison to Co-Packaged Optics (CPO)

| Metric | CPO (2025 state) | Celestial AI PFM |
|---|---|---|
| Bandwidth (off-package) | ~18 Tbps | 7.2 Tbps (module) / 16 Tbps (chiplet) |
| Latency | Baseline | 10x lower |
| Bandwidth density | Baseline | 25x higher |
| 2026 target | 400 Tbps | 400 Tbps (different architecture) |

## In-Die Optical I/O Architecture

Traditional CPO: optical engine co-packaged adjacent to ASIC  
Celestial AI approach: optical elements placed **beneath the compute ASIC** using photonic interposer
- Shorter optical paths → lower latency
- No electrical routing from compute die to optical engine → higher bandwidth density
- Photonic interposer acts as the substrate layer

## Applications Enabled

1. **Memory disaggregation**: Separating HBM stacks from compute die, connected via photonic fabric
2. **Scale-up AI fabrics**: Replacing NVLink cables with optical chiplet connections
3. **Multi-rack coherent memory**: CXL 4.0 over photonic fabric for <2 km coherent memory pooling

## Marvell Acquisition ($3.25B)

Timeline:
- Marvell announced intent to acquire Celestial AI: November 2025
- Deal structure: cash + stock, valued at $3.25B
- Strategic rationale: Combine Celestial AI's in-die optical I/O with:
  - Marvell Teralynx switch ASIC (51.2T)
  - Marvell Structera CXL switch (260-lane)
  - Marvell silicon photonics DSP expertise

Post-acquisition, Marvell will be the only vendor offering a complete stack: switch ASIC + CXL memory fabric + in-die optical I/O.

## Strategic Observations

- The $3.25B acquisition price reflects hyperscaler demand urgency for optical disaggregation solutions
- In-die optical I/O may displace CPO in the next generation (post-2026) of AI accelerator packages
- The combination of CXL 4.0 + Celestial AI optical fabric enables memory pooling with bandwidth/latency competitive with on-package HBM
