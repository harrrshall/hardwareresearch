# Paper 025: Oracle OCI Zettascale10 — Hyperscale AI Cluster Architecture (Oct 2025)

**Tags:** AI-cluster, rack-scale, hyperscale, power-delivery
**Source:** Oracle press release, HPCwire, Storage Newsletter
**Date:** October 14, 2025
**Relevance:** High

## Announcement Overview

Oracle unveiled OCI Zettascale10 at Oracle AI World 2025 (October 14, 2025), positioning it as the largest AI supercomputer available in the cloud.

## Performance Claims

- Peak performance: up to **16 ZettaFLOPS** (16 × 10²¹ FLOPS)
- Scale: up to 800,000 NVIDIA GPU platforms
- Available: second half 2026 (orders accepted from announcement date)

## Architecture

### Networking
- Built on **Oracle Acceleron RoCE** networking architecture
- Low GPU-to-GPU latency across the cluster (key design objective)
- 800G RDMA over Converged Ethernet (RoCEv2) fabric

### Physical Layout
- Clusters housed in gigawatt data center campuses
- **Two-kilometer radius constraint**: all compute within 2 km for acceptable GPU-to-GPU latency
- This geographic concentration drives the need for high-density, liquid-cooled racks

### Cooling
- Liquid-cooled at rack level (GB200 NVL72 format)
- Central CDU infrastructure at campus scale

## Zettascale10 as Stargate Backbone

OCI Zettascale10 is the **fabric underpinning the flagship Stargate supercluster** in Abilene, Texas (built for OpenAI). This makes it the infrastructure layer for the most ambitious AI training cluster ever announced.

## Evolution from Zettascale (v1)

- Zettascale v1: introduced September 2024 — first cloud-based Zettascale compute offering
- Zettascale10: 10th-generation scale evolution; order-of-magnitude improvement in coordination

## AMD Partnership

Oracle also announced AMD open rack-scale AI infrastructure with MI355X GPUs:
- Up to **131,072 MI355X GPUs** in a single zettascale cluster
- Demonstrates that large-scale clusters are not exclusively NVIDIA

## Infrastructure Requirements for 800,000 GPU Scale

Estimated facility requirements for full 800,000 GPU OCI Zettascale10 deployment:
- Power: approximately 800 MW (assuming ~1 kW per GPU effective average)
- CDU infrastructure: ~800 MW cooling capacity
- Network switches: ~10,000+ Quantum-X800 switches at 144 ports × 800G
- Physical footprint: multiple adjacent GW-scale facilities within 2 km

## Implications

OCI Zettascale10 validates the trend toward 100,000+ GPU clusters as a standard cloud offering, not a research one-off. The 2 km radius constraint creates a new data center campus design requirement: density and geographic concentration within a single campus boundary, driving the need for even denser rack designs and higher-voltage power distribution (to minimize cable gauge at extreme distances within campus).
