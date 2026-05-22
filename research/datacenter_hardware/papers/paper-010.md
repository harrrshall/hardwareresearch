# Paper 010: OpenAI Stargate Project — Infrastructure Architecture and Scale

**Tags:** AI-cluster, power-delivery, hyperscale, rack-scale
**Source:** OpenAI announcements, Data Center Dynamics, Data Center Knowledge
**Date:** Jan 2025 announcement; ongoing through 2026
**Relevance:** High

## Project Overview

Stargate was announced January 21, 2025, with a stated goal of $500 billion in AI infrastructure investment over 4 years. Initial equity investors: SoftBank, OpenAI, Oracle, MGX. Technology partners: NVIDIA, Oracle, Microsoft, Arm.

## Scale and Capacity (as of May 2026)

- Total planned capacity: nearly 7 GW across announced sites
- Total investment committed: >$400 billion over 3 years
- Oracle partnership: 4.5 GW of infrastructure capacity commitment
- UAE Stargate: expected to open 2026

## Active Sites (as of 2026)

| Location | Status | Notes |
|----------|--------|-------|
| Abilene, Texas | Active flagship | ~1 GW by mid-2026; $3–4B |
| Shackelford County, TX | Building | Announced Sep 2025 |
| Doña Ana County, NM | Building | Announced Sep 2025 |
| Lordstown, Ohio | Building | Announced Sep 2025 |
| Milam County, TX | Building | Announced Sep 2025 |
| Midwest US | Planning | Announced Sep 2025 |
| Argentina (Patagonia) | Planning | Up to $25B, 500 MW |
| UAE | Opening 2026 | International expansion |

## Technical Infrastructure (OCI Zettascale10)

Oracle's contribution to Stargate is built on the OCI Zettascale10 platform:
- Connects hundreds of thousands of NVIDIA GPUs across multiple data centers
- Peak performance: up to 16 ZettaFLOPS
- Scale: up to 800,000 NVIDIA GPU platforms
- Built on Oracle Acceleron RoCE networking architecture
- Clusters housed within 2 km radius for low GPU-to-GPU latency
- Delivery: second half 2026 for full Zettascale10 buildout

## Custom Silicon: OpenAI "Titan" Chip

- Mass production targeted for H2 2026
- Designed for inference at scale
- Reduces Stargate's dependence on NVIDIA supply

## Power Infrastructure

- Abilene, TX: sourced from ERCOT grid + co-located generation
- Each GW-scale campus requires dedicated substation infrastructure
- Partnership model: Oracle builds and operates facilities; OpenAI is the primary tenant

## Microsoft Pullback

- April 2026: OpenAI pulled back from Stargate Norway deal; Microsoft took over the Norway project
- Reflects shifting financial responsibilities within the consortium

## Significance

Stargate is the largest single AI infrastructure commitment in history. The 7 GW of capacity (when fully built) would represent approximately 10% of US total data center power capacity, concentrated within a 3-year build window. NVIDIA has effectively locked in GPU supply for the program.
