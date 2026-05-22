# Paper 012: Hollow-Core Fiber — 0.091 dB/km Loss at 1550nm, 45% Faster Propagation

**Tags:** optical-interconnect  
**Date:** September 2025  
**Source:** Phys.org / University of Southampton / Microsoft  
**URL:** https://phys.org/news/2025-09-hollow-core-optical-fiber-transmits.html

## Summary

Researchers from the University of Southampton and Microsoft demonstrated a hollow-core photonic bandgap fiber (HCF) achieving 0.091 dB/km attenuation at 1550nm, surpassing the theoretical Rayleigh scattering floor of ~0.14 dB/km for conventional silica fiber. Light travels 45% faster than in glass because it propagates mostly through air (n≈1 vs n≈1.45 for silica).

## Key Technical Specifications

- **Attenuation:** 0.091 dB/km at 1550 nm
- **Previous silica floor:** ~0.14 dB/km (theoretical limit for conventional fiber)
- **Latency advantage:** ~30–47% lower propagation delay vs silica fiber
- **Speed factor:** ~1.45× faster than glass fiber (light in air vs glass)
- **Wavelength:** 1550 nm (telecom C-band)
- **Fiber type:** Hollow-core photonic bandgap fiber (HC-PBF)

## Physics Explanation

In conventional silica fiber, attenuation is dominated by Rayleigh scattering (~0.14 dB/km minimum). In hollow-core fiber:
- Light propagates through air (>99% of mode in air)
- Rayleigh scattering in air is negligible
- Loss limited by surface roughness of the glass microstructure walls
- The 0.091 dB/km result demonstrates surface roughness has been reduced below the previous theoretical floor

## Data Center Applications

For AI training cluster scale-across (rack-to-rack, pod-to-pod), HCF provides:
1. **Latency**: Critical for all-reduce operations in distributed training
2. **Bandwidth**: Standard 400G/800G/1.6T transceivers compatible
3. **Power**: Same passive fiber — no additional power needed for latency advantage

## Deployment Outlook (2026)

- Ciena CTO (March 2026): HCF is "the future generation of fiber technology"
- Microsoft: owns Lumenisity (HCF manufacturer, acquired 2022)
- YOFC: active commercial HCF development
- OFC 2026: Additional performance milestones demonstrated
- Commercial availability: targeted for AI hyperscale interconnects by 2026-2027

## Open Questions

- HCF splice loss with conventional fiber (insertion loss at transitions)
- Bending radius limitations vs standard SMF-28
- Long-term reliability and bend-induced polarization effects
- Cost premium vs standard single-mode fiber at volume
