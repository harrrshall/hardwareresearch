# Paper 015: AI Data Center Power Delivery — MW to GW Infrastructure Challenges

**Tags:** power-delivery, rack-scale, AI-cluster
**Source:** Data Center Knowledge, IEA, Brookings, Cummins, Tech Plus Trends
**Date:** 2025–2026
**Relevance:** High

## The Scale Shift

Power delivery for AI data centers has shifted from kilowatt-per-rack thinking to megawatt-per-cluster and gigawatt-per-campus thinking.

## Power Demand by Scale Level

| Level | Scale | Power |
|-------|-------|-------|
| Single GPU | NVIDIA B200 | ~1,200 W |
| Single server tray | GB200 NVL72 tray | ~10,000 W |
| Single rack | GB200 NVL72 rack | 120 kW |
| AI cluster (100 racks) | 100× GB200 NVL72 | 12 MW + 2–5 MW network |
| Hyperscale campus | Meta / Google tier | 100–500 MW |
| Gigawatt facility | Stargate, Colossus 2 | 1,000 MW |

## Power Delivery Architecture (Rack Level)

### Traditional Path
Utility → Transformer → UPS → PDU → Server PSU (48V) → VRM → Chip

### AI-Optimized Path
Utility → Transformer → UPS → Rack-level PSU shelf (ORv3 48V busbar) → Server VRM → Chip

### Emerging HVDC Path
Utility → Transformer → Rectifier (600–800V DC) → Rack-level DC/DC → Chip
- Eliminates one conversion stage
- 800V: 600 kW delivered at 750A (feasible with standard busbars)
- 48V: 600 kW delivered at 12,500A (requires liquid-cooled busbars)

## Sharp Power Spikes

- AI training/inference creates near-instantaneous power fluctuations of hundreds of MW
- NVIDIA GB200 NVL72 cluster of 1,000 racks: 120 MW nominal, spike to 140+ MW within milliseconds
- Energy storage (BESS) is mandatory for large clusters to smooth grid interface
- UPS sizing must account for spike profiles, not just nominal load

## Grid Capacity Bottleneck

- PJM capacity market: $28.92/MW (2024) → $329/MW (2026-27 delivery year) — 10× increase
- Site selection has transformed: primary criterion is now available megawatts, not network latency
- Permitting for new transmission: 2–7 year lead time in the US
- Generators (diesel/gas): cannot fully substitute — carbon intensity, air quality permitting

## HVDC Distribution Adoption

- Microsoft: trialing 800V HVDC across new builds
- Google: testing 600V HVDC in new data center pilots
- Amazon: evaluating wide-bandgap converters (SiC) for HVDC
- Industry standard expected to emerge 2026–2027 via OCP / IEEE process

## Power Infrastructure per GW Campus

Full AI campus at 1 GW:
- Requires ~8–12 dedicated 345kV transmission lines
- 2–4 on-site substations (each handling 250+ MW)
- 15–30 MW of UPS and BESS (1–2.5% of IT load)
- Natural gas or hydrogen fuel cells for backup
- Cost: $45–55 billion per GW (fully built out with land, power, connectivity, equipment)

## Implications

The power constraint is the binding constraint for AI data center expansion in 2025–2026. Grid availability now determines where the next facility can be built. Operators with locked-in power purchase agreements and existing substation connections have a structural competitive advantage.
