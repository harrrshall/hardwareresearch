# Paper 013: Rear-Door Heat Exchangers (RDHx) — High-Density Cooling Technology

**Tags:** thermal-management, rack-scale, liquid-cooling
**Source:** Vertiv, Supermicro, Motivair, Insightace Analytics
**Date:** 2025–2026
**Relevance:** Medium-High

## Technology Overview

A Rear-Door Heat Exchanger (RDHx) mounts directly on the rear door of a server cabinet. Chilled water circulates through the heat exchanger coils; warm air exhausting from servers passes through the coil and is cooled before reaching the data center aisle.

## Technology Variants

### Passive RDHx
- No fans; relies entirely on server fans for airflow
- Heat removal: proportional to coolant-to-air temperature difference
- Typical capacity: 20–30 kW per rack
- No additional power consumption
- Lower maintenance; suitable for moderate densities

### Active RDHx
- Integrated fans supplement airflow
- Higher heat removal capacity: up to 75 kW per rack (Motivair ChilledDoor)
- Some active units claim 100% heat removal (server generates 0 heat to room)
- Adds ~300–500 W of fan power per unit
- Motivair ChilledDoor: removes densities up to 75 kW per rack

## Market Position (2025)

- Racks <10 kW: 47% of installed capacity in 2024 → dropped to 38% in 2025
- Racks 10–20 kW: 27% → 30%
- Racks 20–30 kW: 24% → 28%
- RDHx is well-suited for the 20–75 kW range — exactly where legacy air-cooled facilities are being upgraded

## Use Case Analysis

| Rack Density | Preferred Cooling |
|-------------|------------------|
| <20 kW | Air cooling (CRAC/CRAH) |
| 20–75 kW | RDHx (active) |
| 75–120 kW | Direct-to-chip (D2C) |
| 120–300+ kW | Full immersion or D2C mandatory |

## Installation Advantage

RDHx is the preferred solution for retrofitting existing air-cooled data centers because:
1. No rack infrastructure changes required
2. Does not require draining or redesigning cooling loops
3. Works with existing chilled water infrastructure
4. Operators can upgrade row by row

## Market Forecast

- Data Center RDHx Market 2026: valued at USD X billion; growing at ~18% CAGR through 2035
- Driven by: legacy data centers upgrading for GPU workloads without full rebuild

## Limitations

- Maximum cooling capacity (~75–100 kW/rack for active) is below GB200 NVL72 requirement (120 kW)
- Not suitable for pure AI training workloads at current rack densities (2025)
- Best positioned as a transitional technology and for inference/mixed workloads

## Implications

RDHx fills the gap between legacy air cooling and full liquid cooling for the large installed base of data centers with 20–75 kW rack requirements. As average rack density increases toward 100 kW+, the RDHx market shifts toward an upgrade path technology rather than an end-state solution.
