# Paper 016: Optical Circuit Switching for AI Data Centers — MEMS-Based OCS Architectures

**Tags:** optical-interconnect  
**Date:** 2025–2026  
**Source:** Lumentum Blog / Cignal AI / TSPASemiconductor / PMC  
**URL:** https://www.lumentum.com/en/blog/optical-circuit-switches-in-ai-hyperscale-data-centers

## Summary

Optical circuit switching (OCS) is emerging as a transformative complement to packet-switched networks in AI hyperscale data centers. MEMS-based OCS provides dedicated optical paths between GPU clusters for large training jobs, eliminating intermediate electronic hops and reducing both latency and power.

## Market Data

- **OCS market size (2025):** $3.8 billion
- **Projected (2034):** $9.7 billion
- **AI data center traffic growth (2025):** ~120% YoY
- **Hyperscaler commitments:** Acknowledged OCS as structurally necessary for GPU-dense AI training (2025-2026 infrastructure disclosures)

## Technical Architecture

MEMS-based OCS:
1. **Switch fabric:** Micro-electromechanical mirror arrays redirect optical beams
2. **Provisioning time:** Sub-microsecond circuit setup
3. **Overlay model:** OCS layer provisions large optical circuits between GPU pods; packet switching handles burst/small flows
4. **Integration:** Works with existing 800G/1.6T pluggable transceivers — no transceiver replacement needed

## Key Advantages for AI Training

- **Large all-reduce operations:** Dedicated 800G-1.6T optical paths vs multi-hop packet routing
- **Congestion elimination:** No queuing delay at intermediate switches during gradient sync
- **Power savings:** Removing 4-6 intermediate electronic switch hops saves ~15-25W/port at scale
- **Topology flexibility:** Reconfigurable fat-tree, rail-optimized, or all-to-all for different job sizes

## PMC Research (2025): Si Photonics Switches on 300mm CMOS

Large-scale silicon photonic OCS fabricated on 300mm CMOS (O-band):
- O-band operation matches computing network standard (850nm-1310nm)
- Wafer-scale integration vs bulk MEMS
- CMOS-compatible for integration with network ASICs
- Lower cost than discrete MEMS at high volume

## OFC 2026 Consensus

All major presentations at OFC 2026 used "AI fabric" language for OCS. Emerging consensus: future GPU clusters with >10,000 GPUs require OCS overlay to prevent network bottleneck. MEMS OCS from Lumentum, Polatis (Huawei), and Agiltron all showed AI-specific products.

## Deployment Timeline

- 2025: Pilot OCS deployments in largest GPU clusters
- 2026: Standard network architecture for 10,000+ GPU pods
- 2027: OCS as default for new AI factory builds
- 2028: Broad commercial adoption including mid-tier cloud

## Open Questions

- OCS provisioning control plane software for dynamic AI workloads
- Integration with RDMA network stacks (ROCEv2, InfiniBand)
- Crosstalk and polarization-dependent loss in MEMS at 800G/1.6T
