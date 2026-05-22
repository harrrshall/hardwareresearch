# Paper 001: NVIDIA Spectrum-X Photonics & Quantum-X Photonics CPO Switches

**Tags:** co-packaged-optics, silicon-photonics, optical-interconnect  
**Date:** March 2025 (GTC 2025)  
**Source:** NVIDIA Newsroom / Developer Blog  
**URL:** https://nvidianews.nvidia.com/news/nvidia-spectrum-x-co-packaged-optics-networking-switches-ai-factories

## Summary

NVIDIA announced two co-packaged optics (CPO) networking switch families at GTC 2025: Spectrum-X Photonics (Ethernet) and Quantum-X Photonics (InfiniBand). These represent the first major commercial GPU-fabric CPO deployments.

## Key Technical Specifications

- **Aggregate bandwidth:** 400 Tb/s per switch
- **Per-port speed:** 1.6 Tb/s (Spectrum-X); 800 Gb/s × 144 ports (Quantum-X InfiniBand)
- **SerDes:** 200 Gb/s per lane
- **Laser count reduction:** 4× fewer lasers vs pluggable solutions
- **Power efficiency gain:** 3.5× improvement over traditional pluggable optics
- **Signal integrity improvement:** 63× compared to conventional copper-pluggable approaches
- **Network resilience:** 10× better at scale
- **Deployment speed:** 1.3× faster than traditional methods

## Architecture Notes

CPO places silicon photonics modulators, lasers, and photodetectors directly on or adjacent to the switch ASIC package, eliminating the need for high-power electrical SerDes drivers over long PCB traces. TSMC's manufacturing capability is central to the packaging.

## Availability

- Quantum-X Photonics InfiniBand: available late 2025
- Spectrum-X Photonics Ethernet: available 2026

## Significance

This announcement marks the first time a tier-1 GPU manufacturer has deployed CPO at product scale, representing a commercial inflection point for the technology. NVIDIA's adoption validates TSMC COUPE packaging and sets a performance/power benchmark for the industry.

## Open Questions

- Exact energy per bit (pJ/bit) for full system path not yet publicly disclosed
- Insertion loss budget details for on-package photonic routing not published
- Fiber attach methodology (MT/MPO vs lensed fiber) not fully described
