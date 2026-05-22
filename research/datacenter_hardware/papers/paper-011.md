# Paper 011: OCP Open Rack V3 (ORv3) and High-Power Rack (HPR) Standards

**Tags:** rack-scale, power-delivery
**Source:** OCP Foundation, Advanced Energy, Eaton, Legrand
**Date:** 2025–2026
**Relevance:** High

## OCP ORv3 Baseline Specifications

Open Rack V3 (ORv3) is the current OCP mechanical and power standard for hyperscale AI data centers. Current revision: ORv3.1 (as of March 2026).

### Mechanical Dimensions

- Interior equipment width: 537 mm (21 inches) — wider than standard 19-inch
- Rack unit: OpenU (OU) = 48 mm (vs standard 44 mm rack unit)
- Exterior dimensions: 600 mm wide (same as standard rack)

### Power Bus

- DC busbar voltage: 48V nominal (47.5V trigger for BBU)
- Power shelf: 33 kW per 2RU shelf (6× 5.5 kW PSUs in parallel)
- Peak efficiency: approaching 98%
- Redundancy: N+1 or N+N per shelf configuration
- Input: 3-phase AC, 347/200 to 480/277 VAC

## ORv3 High Power Rack (HPR)

ORv3-HPR is the evolution targeting AI rack densities:

### HPR V3 (2025 Deployed)

- Supports 300 kW per cabinet
- Used by Meta, Google, Microsoft at hyperscale
- Centralized AC-to-DC conversion at rack level
- Legrand Open Compute Project power train implementation

### HPR V4 (Meta Preview, OCP EMEA 2025)

- ±400V (equivalent 800V) HVDC solution
- Target: 800 kW per cabinet
- Higher voltage enables lower current at same power (I = P/V)
- 800 kW at 800V = 1,000A vs 800 kW at 48V = 16,667A (air-cooled busbars become feasible)

## Power Delivery Architecture — 48V to 12V Conversion

- Traditional: AC → UPS → PDU → server PSU (48V → 12V → point-of-load)
- ORv3 approach: AC → rack-level PSU (48V DC) → server-level VRM (48V → chip voltage)
- Eliminating the 12V intermediate step reduces conversion losses by 2–3%

## HVDC Architecture (380V / 600V / 800V)

- HVDC eliminates one AC-DC conversion stage vs traditional AC distribution
- 600–800V distribution: delivers 600 kW at 750–1,000A (air-cooled feasible)
- vs 48V: 600 kW at 48V = 12,500A (requires liquid-cooled busbars)
- Microsoft, Google, Amazon all trialing HVDC with wide-bandgap semiconductors (SiC, GaN)

## BBU (Battery Backup Unit) Integration

- ORv3 BBU shelf: DC power to rack during AC transition events
- Busbar must stay above 46V during PSU-to-BBU handover
- Typical transition: sub-1ms

## Implications

ORv3-HPR V4 at 800 kW/rack (previewed by Meta) represents the next inflection point. At 800V HVDC, the entire power distribution architecture becomes simpler, lighter, and more efficient. This standard is expected to be formalized through OCP processes in 2026–2027, with first deployments in late 2027.
