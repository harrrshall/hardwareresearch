# Paper 006: Data Center PUE and Power Efficiency Trends — AI Hyperscale 2025–2026

**Tags:** power-delivery, PUE, thermal-management
**Source:** Data Center Dynamics, IEA, dev/sustainability, Brookings
**Date:** 2025–2026
**Relevance:** High

## PUE Benchmarks (2025–2026)

Power Usage Effectiveness (PUE) = Total Facility Energy / IT Equipment Energy. Ideal value = 1.0.

| Operator | Reported PUE | Notes |
|----------|-------------|-------|
| Google | 1.09 (fleet average) | 2025 annual report |
| Microsoft | 1.12 | Azure fleet average |
| Hyperscale range | 1.04–1.20 | Best-in-class facilities |
| Immersion cooling | ~1.03 | Theoretical near-limit |
| D2C liquid cooling | 1.10–1.15 | Typical deployed |
| Legacy air-cooled | 1.40–2.0 | Older facilities |

## Energy Consumption Trends

- Global data center electricity consumption 2022: ~460 TWh/year
- Projected global consumption 2026: 650–1,050 TWh/year (IEA)
- AI data centers alone: projected to consume >90 TWh annually by 2026
- IEA report (2025): Data centre electricity use surged in 2025 even with bottlenecks

## AI Workload Power Impact

- Traditional server rack: 5–15 kW
- AI/GPU rack (pre-2024): 40–60 kW
- NVIDIA GB200 NVL72: 120 kW per rack
- Emerging designs: 200–300 kW per rack
- NVIDIA Vera Rubin (2026): approximately 120–130 kW per rack (same power, 2.5× compute)

## Power Efficiency Technologies

- Liquid cooling reduces total cooling energy by 20–40% vs air
- Immersion cooling achieves PUE approaching 1.03
- D2C with free cooling (waterside economizers): PUE 1.10–1.15
- HVDC distribution (600–800V) reduces conversion losses by 4–6% vs traditional 48V
- Silicon carbide (SiC) power supplies: Eaton 9PX Gen2 (June 2025) uses SiC for superior efficiency

## Water Usage Effectiveness (WUE)

- Traditional evaporative cooling: up to 1.5 million liters/day per hyperscale facility
- Microsoft zero-water cooling program: 80% WUE improvement vs earlier designs
- New Microsoft facilities in Phoenix AZ and Mt. Pleasant WI piloting zero-water-evaporation in 2026
- Texas AI data centers projected to use 49 billion gallons of water in 2025; 399 billion gallons by 2030 (HARC/UH study)

## Grid Stress

- PJM capacity market clearing price: jumped from $28.92/MW to $329/MW for 2026–27 delivery year
- AI data center expansion is now primarily constrained by grid availability, not compute efficiency
- Grid fluctuations from AI clusters: hundreds of MW within seconds — requires energy storage buffers
- Microsoft + Iberdrola: 150 MW dedicated wind PPA for AI infrastructure in Spain (late 2025)

## Implications

PUE is no longer the primary efficiency concern at the facility level — gross power consumption is. A 1.09 PUE facility consuming 1 GW of IT load uses more total energy than a 1.5 PUE facility consuming 100 MW. Operators are maximizing compute per watt of IT load, making liquid cooling + chip efficiency the priority.
