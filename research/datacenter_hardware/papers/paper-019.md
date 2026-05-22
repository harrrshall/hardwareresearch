# Paper 019: Coolant Distribution Units (CDUs) and Liquid Cooling Infrastructure (2025)

**Tags:** liquid-cooling, thermal-management, rack-scale
**Source:** Vertiv, JetCool, ToneCooling, CoolIT Systems, OCP White Paper
**Date:** 2025
**Relevance:** High

## CDU Architecture Overview

A Coolant Distribution Unit (CDU) is the central thermal management component connecting facility chilled water to server-level cold plates. It contains:
- Heat exchanger (facility water-to-server coolant)
- Primary and redundant pumps
- Filters and deionizers
- Temperature, flow, and pressure sensors
- Control electronics and remote monitoring
- Leak detection systems

## Deployment Configurations

### In-Rack CDU
- Mounted inside or adjacent to the compute rack
- Typical capacity: 100–300 kW
- Low latency to servers; short manifold runs
- Used for high-density single-rack deployments (GB200 NVL72)

### In-Row CDU
- One CDU serves a row of multiple racks
- Typical capacity: 300–1,350 kW (Vertiv CoolChip 1350)
- Longer manifold runs; requires more piping
- More economical for large deployments

### Central CDU (Facility Level)
- Serves multiple rows
- Capacity: 2,300 kW (Vertiv CoolChip 2300)
- Most cost-efficient per kW of cooling

## Vertiv CoolChip CDU Product Line (2025)

| Model | Capacity | Notes |
|-------|----------|-------|
| CoolChip CDU In-Rack | Up to 100 kW | Liquid-to-liquid |
| CoolChip CDU 450 | 450 kW | Row-based L2L |
| CoolChip CDU 600 | 600 kW | Row-based L2L |
| CoolChip CDU 1350 | 1,350 kW | Large row/hall L2L |
| CoolChip CDU 2300 | 2,300 kW | Facility/campus level |
| CoolChip 70 (air) | 70 kW | Liquid-to-air |

Temperature control precision: ±1.8°F (±1°C) across all models.

**Vertiv market position:** ~70% volume share of CDUs shipped with first GB200 NVL72 rack deployments.

## Supermicro 250 kW CDU (2025)

- New Supermicro 250 kW CDU: more than doubled capacity vs previous 120 kW unit
- Maintains same 4U form factor
- Introduced specifically for GB200 NVL72 and HGX B200 rack deployments
- Features vertical coolant distribution manifolds (CDM) for higher rack density

## Manifold and Quick-Disconnect Standards

- **OCP Universal Quick Disconnect (UQD):** adopted standard for spill-free coupling
- Bidirectional self-sealing; steel ball locking mechanism
- Enables hot-swap server service without fluid loss
- Rack manifold receives coolant from CDU; distributes via flexible hose assemblies to each server cold plate
- Branch flow balance: manifold must ensure equal flow rate across all servers (typically within ±5%)

## Sizing Rules

- CDU capacity = sum of all server TDPs × 1.15 (15% headroom)
- GB200 NVL72 rack: 120 kW × 1.15 = 138 kW minimum CDU capacity (typically 150–200 kW)
- Coolant flow rate: Q = P / (ρ × Cp × ΔT) — where ΔT is typically 10–15°C across cold plate

## Temperature Specifications

| Parameter | Typical Value |
|-----------|--------------|
| Facility supply water | 12–18°C |
| CDU secondary supply | 18–25°C |
| CDU secondary return | 35–45°C |
| GPU cold plate target | 25–45°C supply |
| Maximum chip junction | 85°C (B200) |

## Leak Detection

- Distributed sensors at each manifold connection
- Floor sensors below rack sump pans
- Automatic shutoff valves triggered within 1 second of leak detection
- OCP white paper: manifold requirements and qualification standards for rack cooling

## Implications

CDU supply chain is a deployment bottleneck. Lead times for large CDUs (600–1,350 kW) extended to 20–36 weeks in 2025 due to demand surge from GB200 NVL72 deployments. Operators must plan CDU procurement 6–12 months ahead of rack arrival.
