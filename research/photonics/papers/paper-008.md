# Paper 008: Avicena LightBundle — MicroLED Optical Interconnect at <1 pJ/bit

**Tags:** optical-IO  
**Date:** March 2025 (announcement); December 2025 (operational results); March 2026 (eKit)  
**Source:** Avicena / BusinessWire / Semiconductor Today  
**URL:** https://avicena.tech/avicena-announces-modular-lightbundle-optical-interconnect-platform-with-1tbps-mm-i-o-density-and-1pj-bit/

## Summary

Avicena's LightBundle platform uses GaN-based microLEDs as optical transmitters to achieve record energy efficiency (<1 pJ/bit, with demonstrated 200 fJ/bit and 80 fJ/bit operation) combined with >1 Tbps/mm I/O shoreline density. This challenges traditional silicon photonic laser-based approaches with fundamentally lower device power.

## Key Technical Specifications

- **I/O density:** >1 Tbps/mm (shoreline)
- **Energy efficiency:** <1 pJ/bit (system); 200 fJ/bit (Tx demonstrated); 80 fJ/bit (LED energy without FEC)
- **Per-lane rate:** 4 Gbps (December 2025 operational results)
- **Transmitter current:** as low as 100 µA per LED
- **Maximum reach:** >10 meters (die-to-die and rack-scale)
- **Roadmap:** 10 Tbps/mm² target
- **FEC:** demonstrated operation without FEC at target BER

## Technology Architecture

Unlike laser-based silicon photonics (which require precision-controlled laser threshold current, external modulation, and thermal stabilization), LightBundle uses:
1. **GaN microLED arrays**: direct modulation at GHz rates with femtojoule energy per bit
2. **TSMC-fabricated PD arrays**: monolithic photodetector integration using TSMC process
3. **Multi-core fiber bundle**: guides light between dies
4. **Lens arrays**: precision coupling optics

## TSMC Partnership

Avicena partnered with TSMC to fabricate complementary photodetector arrays using TSMC's process, enabling wafer-level integration of PD arrays with CMOS circuits.

## March 2026 Milestone

Avicena launched the LightBundle eKit — industry's first microLED optical interconnect evaluation kit using ASIC-based transceivers with integrated LED, photodetector, and micro-lens arrays connected via multi-core fiber bundle.

## Significance

80–200 fJ/bit transmit energy is 25–60× more efficient than Intel OCI (5 pJ/bit) and Ayar Labs TeraPHY (5 pJ/bit), though at lower per-lane rates. LightBundle addresses ultra-short reach (die-to-die, chiplet-to-chiplet, and rack scale) where microLED economics and power dominate.
