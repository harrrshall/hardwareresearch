# paper-008: InfiniBand XDR (800G) — AI Cluster Scale-Up Fabric

**Tags:** chip-to-chip  
**Date:** 2025  
**Source:** IBTA, NADDOD, InfiniBand Trade Association  
**URL:** https://www.infinibandta.org/infiniband-roadmap-charting-speeds-for-future-needs/

---

## Summary

InfiniBand XDR at 800 Gbps per port became the dominant AI cluster interconnect in 2025, deployed in the world's largest AI supercomputers including Stargate and Oracle's planned zetta-scale cluster. The next generation — GDR at 1.6 Tbps — is appearing in vendor roadmaps for 2026–2027.

## InfiniBand Generation Roadmap

| Generation | Speed | Status |
|---|---|---|
| HDR | 200 Gbps | Deployed |
| NDR | 400 Gbps | Deployed |
| XDR | 800 Gbps | Current (2025) |
| GDR | 1.6 Tbps | Roadmap 2026–2027 |
| LDR | 3.2 Tbps | Roadmap 2029+ |

## NVIDIA Quantum-X800 Switch Specifications

| Parameter | Value |
|---|---|
| Ports | 144 × 800 Gbps XDR |
| Total bandwidth | 115.2 Tbps |
| In-network compute | 14.4 TFLOPS |
| SHARP support | Yes (9x vs NDR) |
| Protocol | InfiniBand XDR |

## Major 2025 Deployments

### Stargate AI Supercomputer
- Installation began March 2025
- **64,000 GB200 systems** interconnected
- 800 Gbps InfiniBand XDR for multi-exaflop AI services
- Scale-out fabric uses Quantum-X800 switches

### Oracle Zetta-Scale Cluster (Planned)
- **131,000 GB200 GPUs** planned
- Connected through Quantum InfiniBand XDR fabric
- Will exceed 1 ExaFLOP/s sustained training throughput

### Azure GB300 Cluster (October 2025)
- First supercomputer-scale NVL72 deployment
- **4,608 GB300 GPUs** with NVLink 5 scale-up + InfiniBand XDR scale-out
- Demonstrates hybrid NVLink + InfiniBand topology

## Scale-Up vs Scale-Out Architecture

In GB200/GB300 systems:
- **Scale-up** (within NVLink domain): NVLink 5 at 1.8 TB/s per GPU, all-to-all within 72-GPU rack
- **Scale-out** (between racks): InfiniBand XDR 800G or Ethernet 800G via ConnectX-8 NICs

## InfiniBand vs Ethernet Convergence

2025 marks a key inflection:
- InfiniBand retains advantage in latency (<1 µs vs 1–3 µs for Ethernet) and congestion management for training
- Ethernet 800G with Ultra Ethernet (UEC 1.0) closing the gap for inference and less latency-sensitive workloads
- ESUN initiative at OCP 2025 pushes Ethernet into scale-up territory

## Market Size

- InfiniBand market: **$25.74B (2025)** → **$126.99B (2030)** at 37.6% CAGR

## Strategic Observations

- The XDR 800G transition has been remarkably rapid: NDR deployments peaked in 2024, XDR became the standard in under 18 months
- 1.6T GDR optics beginning to appear in roadmaps suggests the next transition will be faster
- SHARP in-network compute (reducing collective communication overhead) has become a decisive competitive differentiator vs Ethernet
