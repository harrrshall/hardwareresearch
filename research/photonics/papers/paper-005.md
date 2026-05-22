# Paper 005: Intel Optical Compute Interconnect (OCI) Chiplet — Fully Integrated Optical I/O

**Tags:** optical-IO, silicon-photonics  
**Date:** 2025  
**Source:** Intel Newsroom  
**URL:** https://newsroom.intel.com/artificial-intelligence/intel-unveils-first-integrated-optical-io-chiplet

## Summary

Intel demonstrated the first fully integrated Optical I/O Chiplet (OCI), combining silicon photonics and on-chip InP lasers with an electrical interface IC. The chiplet is designed for heterogeneous integration with CPUs, GPUs, IPUs, and other system-on-chips.

## Key Technical Specifications

- **Bidirectional throughput:** 4 Tbps
- **Energy efficiency:** ~5 pJ/bit
- **On-chip laser:** Indium Phosphide (InP) integrated laser sources
- **Optical amplifiers:** On-chip optical amplifiers included
- **Integration:** Silicon photonics IC + electrical IC in a single package
- **Target hosts:** CPUs, GPUs, IPUs, and SoCs

## Architecture Notes

The OCI chiplet integrates three functional domains:
1. **Silicon photonic IC**: modulators, waveguides, grating couplers
2. **On-chip InP laser**: eliminates need for external laser
3. **Electrical IC**: control circuits, TIA, and driver electronics

On-chip laser integration is notable — most silicon photonics systems require an external laser source due to silicon's indirect bandgap. Intel's approach uses heterogeneous III-V/Si bonding to achieve monolithic integration.

## Significance

- First fully integrated OCI chiplet (laser + photonics + electronics)
- 5 pJ/bit matches Ayar Labs TeraPHY efficiency
- Eliminates external light source, reducing system complexity
- Demonstrates path to CPU/GPU-native optical I/O

## Comparison Table

| Company | Product | Bandwidth | Energy |
|---------|---------|-----------|--------|
| Intel | OCI Chiplet | 4 Tbps | ~5 pJ/bit |
| Ayar Labs | TeraPHY | 8 Tbps | 5 pJ/bit |
| Avicena | LightBundle | >1 Tbps/mm | <1 pJ/bit |

## Open Questions

- Production timeline and foundry partner not disclosed
- Per-channel specifications and wavelength plan unclear
- Coupling loss between on-chip laser and Si photonic waveguide not published
