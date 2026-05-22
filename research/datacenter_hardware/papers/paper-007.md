# Paper 007: Meta AI Infrastructure — Data Center Design and Scale (2025–2026)

**Tags:** AI-cluster, rack-scale, hyperscale, power-delivery
**Source:** Engineering at Meta, Meta Newsroom, Data Center Dynamics, Data Center Frontier
**Date:** 2025–2026
**Relevance:** High

## Investment Scale

- Meta 2025 AI infrastructure capex: $72 billion
- Total declared multi-year investment: $600 billion (decade-scale)
- GPU procurement: 1.3+ million GPUs acquired through 2025
- Target: >1 GW of AI computing power online by 2026

## Key Facilities (2025–2026)

| Site | Investment | Status |
|------|-----------|--------|
| Montgomery, Alabama | $1.5 billion | Opening 2026 |
| Rosemount, Minnesota | $800 million | 2026 |
| Jeffersonville, Indiana | $800 million | 2026 |
| Kuna, Idaho | $800 million | Operational 2025 |

## Meta Compute Division

Meta established "Meta Compute" as a dedicated infrastructure division to build gigawatt-plus scale AI data centers. Plans include multiple GW+ facilities this decade, with hundreds of GW or more over time.

## Technical Design Philosophy

- Pivot to rack-level integration: GPU-dense, liquid-cooled racks replacing traditional server-row architecture
- Construction restart: ~12 data centers paused in late 2022 were redesigned for GPU-dense liquid-cooled workloads
- OCP ORv3-HPR V3 deployment: 300 kW/cabinet GPU server density
- OCP EMEA Summit 2025: Meta previewed ORv3-HPR V4 with ±400V (800V equivalent) HVDC, pushing cabinet to 800 kW

## Custom Silicon: MTIA v2

- MTIA (Meta Training and Inference Accelerator) v2 deployed at scale in 2025
- Based on 5nm process; 354 TOPS INT8 at 90W TDP, 421mm²
- 3.5× dense compute vs MTIA v1; 7× sparse compute
- 256 MB on-chip memory; 2.7 TB/s on-chip bandwidth
- Primarily serves ranking/recommendation (ads) workloads
- MTIA v3 roadmap announced; Broadcom partnership for multi-gigawatt ASIC deployment
- Broadcom partnership: extended to support multiple gigawatts of Meta custom silicon

## Engineering Insights (September 2025 Engineering Blog)

- Shift from "server-centric" to "cluster-centric" design: the rack and network fabric are designed as a single system
- AI training clusters are sized at 16,384+ GPU scale per job
- Optical interconnects between racks are becoming mandatory for bandwidth at this scale

## Implications

Meta's infrastructure decisions shape OCP standards. The ORv3-HPR V4 preview at 800 kW/cabinet with 800V HVDC signals the next power density milestone for the industry. Meta's MTIA program demonstrates that custom silicon can compete with NVIDIA for inference-class workloads at scale, reducing per-unit cost while increasing data center utilization efficiency.
