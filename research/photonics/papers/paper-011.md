# Paper 011: Thin-Film Lithium Niobate Modulator — >200 GHz Bandwidth at 0.1 V·cm

**Tags:** silicon-photonics  
**Date:** 2026  
**Source:** Advanced Photonics Research (Wiley)  
**URL:** https://advanced.onlinelibrary.wiley.com/doi/10.1002/adpr.202500237

## Summary

This work demonstrates an ultra-efficient thin-film lithium niobate (TFLN) electro-optic modulator achieving >200 GHz bandwidth with a half-wave voltage-length product (Vπ·L) of only 0.1 V·cm, enabling 1V drive voltage at 1mm device length. This sets a new benchmark for TFLN efficiency.

## Key Technical Specifications

- **EO bandwidth:** >200 GHz (3dB)
- **Vπ·L product:** 0.1 V·cm (record-level efficiency)
- **Drive voltage:** 1V (Vπ at 1mm length)
- **Device length:** 1 mm
- **Platform:** Lithium niobate on insulator (LNOI) / TFLN
- **Waveguide type:** High-permittivity Bragg waveguide structure
- **Wavelength:** Telecom C-band (1550 nm range)

## Architecture Innovation

The key innovation is a high-permittivity Bragg waveguide that:
1. Concentrates the microwave RF field more efficiently in the electro-optic region
2. Reduces the required device length for a given drive voltage
3. Maintains low optical loss through careful waveguide design
4. Achieves velocity-matching between optical and RF wave without extensive electrode engineering

## Industry Context

At OFC 2026, Liobate demonstrated:
- 1.6T coherent PDMIQ modulator for long-haul
- 400G/lane device for AI data centers
- 200G/lane solution

HyperLight (OFC 2025) showed:
- Single-lane 400G TFLN PIC
- Reference LN modulator with 145 GHz bandwidth
- 448 Gbps using 224 GBaud PAM4

## Platform Comparison

| Platform | Max EO BW | Vπ·L | Integration |
|----------|-----------|-------|-------------|
| TFLN (this work) | >200 GHz | 0.1 V·cm | Difficult (no Si laser) |
| Si MRR | >110 GHz | ~0.02 V | Easy (CMOS) |
| GeSi EAM (imec) | >110 GHz | N/A | Easy (300mm CMOS) |
| InP MZM | ~50 GHz | ~1 V·cm | Moderate (native laser) |

## Manufacturing Note

Fujitsu announced 35% increase in LN modulator production capacity by Q2 2026 to address supply constraints.
