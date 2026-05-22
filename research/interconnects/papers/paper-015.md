# paper-015: Intel EMIB-T and Foveros Direct 3D — Advanced Packaging for Chiplet Interconnect

**Tags:** chip-to-chip, UCIe  
**Date:** 2025  
**Source:** Intel / Institution of Electronics / TrendForce  
**URL:** https://institutionofelectronics.ac.uk/intel-ups-the-advanced-packaging-ante-with-emib-t/

---

## Summary

Intel advanced its chiplet interconnect packaging in 2025 with EMIB-T (adding Through-Silicon Vias to EMIB for HBM4 support) and Foveros Direct 3D (hybrid bonding at <5 µm pitch), competing directly with TSMC's SoIC-X at 9 µm pitch. These technologies enable chiplet-to-chiplet bandwidth densities impractical with standard organic substrate.

## Intel Advanced Packaging Technologies

### EMIB (Embedded Multi-die Interconnect Bridge) — 2D
- Silicon bridge embedded in organic substrate
- Connects dies at 55 µm bump pitch
- Avoids full silicon interposer cost
- Apple and Qualcomm exploring EMIB licensing (TrendForce, November 2025)

### EMIB-T — 2.5D with Through-Silicon Vias
- Adds TSVs to standard EMIB
- Supports **HBM4** routing density (requires TSVs for vertical signal routing)
- Compatible with UCIe standard package + advanced package connections
- Announced at Intel Foundry Direct Connect 2025

### Foveros 2.5D
- Stacks processor and chiplets vertically on Si interposer
- Standard pitch for face-to-face die bonding

### Foveros Direct 3D — Hybrid Bonding
- **Sub-5 µm bump pitch** (copper-to-copper direct bond)
- First Intel node to support Foveros Direct 3D: **18A-PT**
- Directly competing with TSMC SoIC-X (9 µm pitch)
- Intel achieves 2x tighter pitch than TSMC's equivalent

### EMIB 3.5D — Hybrid Solution
- Combines EMIB 2.5D + Foveros Direct 3D
- Optimizes package size, compute performance, power, and cost
- Addresses thermal warping, reticle size limits, and interconnect density simultaneously

## Technology Comparison

| Technology | Pitch | Type | Primary Use |
|---|---|---|---|
| Standard substrate | >100 µm | 2D | Consumer SoC |
| EMIB | 55 µm | 2.5D | HBM, multi-die SoC |
| TSMC CoWoS-S | ~45 µm | 2.5D | GPU + HBM |
| TSMC SoIC-X | 9 µm | 3D hybrid bond | Chiplet stacking |
| Intel Foveros Direct 3D | <5 µm | 3D hybrid bond | Chiplet stacking |

## ISSCC 2025 Highlight

At ISSCC 2025, Intel demonstrated:
- Configurable heterogeneous 2.5D interfaces across **20 chiplets from 2 foundries**
- Bandwidth-scalable interface between chiplets
- Standard chiplet interface compatible across chiplet types
- Proof of multi-foundry heterogeneous integration in production-ready form factor

## Implications for Bandwidth Density

At Foveros Direct 3D pitch (<5 µm):
- Die-to-die bandwidth densities can reach **Tbps/mm²** range
- Short vertical bond wire (~10 µm) dramatically reduces signal energy vs lateral routing
- Enables SRAM caches stacked directly on compute die for L3/L4 memory bandwidth

## Strategic Observations

- Intel's <5 µm pitch advantage over TSMC's 9 µm SoIC-X is significant but not yet reflected in production volume
- Apple and Qualcomm exploring EMIB suggests Intel Foundry services are gaining traction for packaging even without leading-edge logic wins
- The combination of EMIB-T (HBM4) + Foveros Direct (compute stacking) in EMIB 3.5D is Intel's response to TSMC's CoWoS-R and SoIC-X combined approach
