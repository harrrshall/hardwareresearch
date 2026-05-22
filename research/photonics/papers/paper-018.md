# Paper 018: NTT IOWN All-Photonics Network — 1 Tbps Optical Paths and PEC-2 Switch

**Tags:** optical-interconnect  
**Date:** 2025–2026  
**Source:** IEEE ComSoc Blog / NTT / Computer Weekly  
**URL:** https://techblog.comsoc.org/2026/05/09/ntts-iown-is-finally-evolving-to-an-all-photonic-network-apn-physics-based-ai-for-enterprise-ot/

## Summary

NTT's Innovative Optical and Wireless Network (IOWN) All-Photonics Network (APN) achieved commercial milestones in 2025-2026, including 1 Tbps optical path demonstrations at OFC 2025, 455 Tbps over 1000 km transmission, and PEC-2 switch development targeting 102.4 Tbps commercial release in 2026.

## Key Milestones

### OFC 2025
- Demonstrated 1 Tbps-class optical paths
- Showcased APN for Expo 2025 Osaka connectivity (pavilion interconnect)

### 2025 Transmission Record
- 455 Tbps over 1,000 km using ordinary optical fibers
- Demonstrates path to hyperscale long-haul photonic networking

### MWC Barcelona 2026
- APN-facilitated AI video analysis demonstration
- In-network computing on photonic paths
- Improved AI inference processing via APN

## PEC-2 Switch Technology

- **Aggregate capacity:** 102.4 Tbps (commercial release 2026)
- **Technology partners:** Broadcom (co-developing)
- **Architecture:** Photonic Engine Card (PEC) switching — all-optical switching without O-E-O conversion
- **Latency advantage:** Eliminates electronic conversion latency at each hop

## APN Vision

The All-Photonics Network eliminates optical-electrical-optical (OEO) conversion at network nodes:
- **Compute layer:** Photonic memory access
- **Storage layer:** Photonic interconnect
- **Transport layer:** All-optical wavelength switching
- **Energy savings:** ~100× vs equivalent electronic network (claimed)

## Technical Architecture

```
Traditional: Fiber → OE → Electronic Switch → EO → Fiber
APN:         Fiber → Optical Switch → Fiber (no conversion)
```

Key components:
- Photonic switch fabrics (silicon photonic or LiNbO3 arrays)
- Optical amplifiers (EDFA or Raman) for span loss compensation
- Coherent transceivers at endpoints only
- Software-defined optical path provisioning

## Partners

- NTT (Japan): APN development and deployment
- Broadcom: PEC-2 co-development
- Sony, Intel, Microsoft: IOWN Global Forum members
- ITU: Collaborative standardization (2026 announcement)

## Significance for AI

The APN is directly relevant to AI factory scale-across architectures where GPU-to-GPU communication spans multiple racks and buildings. By eliminating intermediate OEO conversions, APN reduces latency by removing nanoseconds of conversion at each hop and saves substantial power at network node equipment.
