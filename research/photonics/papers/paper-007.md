# Paper 007: Silicon Microring Modulator at 400 Gbps per Wavelength

**Tags:** silicon-photonics  
**Date:** 2025  
**Source:** Laser & Photonics Reviews (Wiley)  
**URL:** https://onlinelibrary.wiley.com/doi/10.1002/lpor.202502840

## Summary

This paper reports a wafer-scale silicon microring modulator achieving 400 Gbps per wavelength operation with an electro-optic bandwidth exceeding 110 GHz, fabricated on a 300 mm CMOS silicon photonics platform. Also demonstrated: a 4×400G WDM transmitter in O-band and C-band.

## Key Technical Specifications

- **Data rate:** 400 Gbps/λ (per wavelength)
- **EO bandwidth:** >110 GHz
- **Modulation format:** PAM4 (presumably, for 400G at 200 GBaud)
- **Platform:** 300 mm CMOS silicon photonics
- **WDM configuration:** 4×400G = 1.6 Tbps aggregate per chip
- **Spectral bands:** O-band and C-band demonstrated
- **Resonator type:** PN-junction microring resonator (MRR)
- **Wavelength selectivity:** Inherent WDM channel selectivity via resonance

## Technical Challenges Addressed

- Resonance wavelength sensitivity to fabrication variation
- Thermal drift compensation (conventional heater approach analyzed)
- Novel phase-change material tuning demonstrated for athermal operation
- Post-fabrication trimming with photochromic materials explored in companion work

## Data-Rate Density

With 4×400G on-chip, the data-rate density achieves 1.6 Tb/s per chip footprint, making this one of the highest demonstrated spectral efficiencies for silicon photonics at the time.

## Comparison with Other Platforms

| Platform | Max Rate/λ | EO BW | Platform |
|----------|-----------|-------|---------|
| Si MRR (this work) | 400 Gbps | >110 GHz | 300mm CMOS SiPho |
| TFLN MZM (HyperLight) | 400+ Gbps | 145 GHz | TFLN |
| GeSi EAM (imec) | 400 Gbps | >110 GHz | 300mm CMOS |

## Significance

400 Gbps/λ in silicon microring enables 1.6 Tbps from a 4-channel chip using standard CMOS fabrication, without exotic materials. This is the enabling device for next-generation CPO and pluggable 1.6T modules.
