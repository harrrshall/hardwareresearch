# Paper 012: xAI Colossus — The First Gigawatt AI Data Center (2025–2026)

**Tags:** AI-cluster, power-delivery, rack-scale, hyperscale
**Source:** SemiAnalysis, Wikipedia, DCD, Bloomberg
**Date:** 2025–2026
**Relevance:** High

## Overview

Colossus, built by Elon Musk's xAI, is the world's largest AI supercomputer by GPU count and (as of mid-2025) by power consumption. Located in Memphis, Tennessee (and Southaven, Mississippi adjacent site), it represents the fastest build of any AI supercomputer in history.

## Phase 1 Scale (Memphis, operational July 2024)

- Initial deployment: 100,000 NVIDIA H100 GPUs
- Site: repurposed former Electrolux factory (~1M sq ft)
- Location advantage: proximity to wastewater treatment facility for cooling water supply

## Phase 2 Scale (as of June 2025)

| Component | Count |
|-----------|-------|
| H100 GPUs | 150,000 |
| H200 GPUs | 50,000 |
| GB200 GPUs | 30,000 |
| **Total GPUs** | **230,000** |

- Maximum power consumption: increased from 150 MW to 250 MW
- Colossus expanded to adjacent Southaven, Mississippi site

## Colossus 2 (expansion announced March 2025)

- xAI acquired 1 million sq ft warehouse + 100 adjacent acres in Memphis (March 7, 2025)
- By August 22, 2025: 119 air-cooled chillers on site = ~200 MW of cooling capacity for new building
- Colossus 2 becoming "fastest growing AI data center in the world"
- Bloomberg (Dec 2025): additional buildings acquired for further expansion

## Infrastructure Design

- Mix of air-cooled and liquid-cooled racks
- H100/H200: primarily air-cooled rows (standard 10–15 kW rack density for air-cooled GPU servers)
- GB200 NVL72: liquid-cooled at 120 kW/rack
- 230,000 GPUs across multiple rack types represents an extraordinarily diverse infrastructure stack
- Cooling: industrial-scale water chiller plant, not standard data center CRAC units

## Power Supply

- 250 MW of power: requires dedicated substation(s) and grid connections
- MLGW (Memphis Light Gas and Water) is the primary utility provider
- Natural gas generators on-site for backup (controversial: community health complaints logged in Memphis)

## Purpose

- Primary: training Grok LLM (xAI's large language model)
- Secondary: compute support for X (Twitter) platform and SpaceX infrastructure

## Significance

Colossus represents the "speed-first" approach to AI infrastructure: compress construction timeline to under 12 months for 150 MW+ deployment. This demonstrated that hyperscale AI data centers can be built faster than traditional data center schedules (typically 2–4 years), using repurposed industrial buildings and industrial-grade water cooling.
