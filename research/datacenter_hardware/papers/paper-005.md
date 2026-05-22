# Paper 005: AI Cluster Network Topology — Fat-Tree vs Dragonfly+ vs Rail-Optimized (2025)

**Tags:** AI-cluster, network-topology
**Source:** Introl Blog, Pingdo, LuxOptx, InfiniBand documentation
**Date:** 2025
**Relevance:** High

## Overview

Network fabric has become the dominant performance constraint for large-scale AI training. Topology selection directly determines throughput, latency, congestion behavior, and cost at scale. Three topologies dominate in 2025: fat-tree, Dragonfly+, and rail-optimized.

## Fat-Tree Topology

**Architecture:** Multi-tier Clos network; typically 3-tier (edge, aggregate, spine) for large deployments.

**Key properties:**
- Non-blocking bandwidth between any pair of endpoints
- Predictable performance regardless of communication pattern
- NVIDIA DGX SuperPOD reference architecture uses 3-tier fat-tree with Quantum-2 InfiniBand at 400 Gb/s per port
- 32 DGX nodes per SuperPOD building block, expandable via spine layer

**Scale:** A 100-rack cluster requires hundreds of spine/leaf InfiniBand switches; a 100-switch fabric adds 150–350 kW to facility load.

**2025 status:** Dominant topology for GPU cluster deployments because distributed training patterns are dynamically varying — fat-tree's bisection bandwidth guarantee matters most.

## Dragonfly+ Topology

**Architecture:** Two-level direct network; fully-connected groups of switches; inter-group links via "all-to-all" pattern.

**Key properties:**
- Average path length: ~2 hops vs 4+ in fat-tree
- 50–70% fewer cables than fat-tree at equivalent scale
- Cost-effective at 256+ GPU scales

**Scale:** Scales to 100,000+ endpoints with 2-level hierarchy.

**2025 status:** Preferred for HPC (HPE Slingshot) but not yet dominant for GPU training clusters, where fat-tree's predictability wins. Best economics at very large scale (>10,000 GPUs).

## Rail-Optimized Topology

**Architecture:** InfiniBand "rail" fabric organizes GPUs so that GPU 0 across all nodes shares a top-of-rack switch, GPU 1 across all nodes shares another, etc.

**Key properties:**
- Optimized for all-reduce collective operations (AllReduce across same GPU index)
- Reduces intra-rank traffic concentration
- Common in NVIDIA Spectrum-X deployments with RoCEv2

**2025 status:** Gaining adoption for large-scale inference clusters; combined with NVIDIA Spectrum-X 800G Ethernet for cost-sensitive deployments.

## Bandwidth Comparison (2025)

| Technology | Per-Port Speed | Ports/Switch | Topology |
|-----------|----------------|--------------|----------|
| NVIDIA Quantum-2 NDR IB | 400 Gb/s | 64 | Fat-tree |
| NVIDIA Quantum-X800 XDR IB | 800 Gb/s | 144 | Fat-tree |
| NVIDIA Spectrum-X 800G | 800 Gb/s | 64 | Rail-opt |
| HPE Slingshot 200G | 200 Gb/s | 64 | Dragonfly+ |

## Cost Comparison: InfiniBand vs Ethernet (2025)

- InfiniBand NDR per-port cost: 1.5–2.5× higher than 400G Ethernet
- 512-GPU cluster: InfiniBand network overhead could fund an additional 128 GPUs
- Annual InfiniBand maintenance premium: ~$213,000 vs Ethernet on same cluster
- For hyperscale LLM training: InfiniBand remains gold standard
- For inference, R&D, mid-size training: Ethernet now viable with RoCEv2 tuning (PFC + ECN + buffer allocation)

## Implications

The 800G migration (Quantum-X800 / Spectrum-X) is underway in 2025. 102.4 Tb/s switch ASICs are the new fabric planning baseline for AI cluster builds. Network power (150–350 kW per 100-rack cluster) must be included in facility power budgets.
