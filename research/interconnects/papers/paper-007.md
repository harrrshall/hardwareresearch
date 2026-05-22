# paper-007: Switch ASIC Bandwidth Race — Tomahawk 6, Silicon One G300, and 102.4T Era

**Tags:** chip-to-chip  
**Date:** 2026-03  
**Source:** Broadcom, Cisco, The Register  
**URL:** https://www.broadcom.com/company/news/product-releases/63146

---

## Summary

2026 marks the arrival of 102.4 Tbps Ethernet switch ASICs in production volume, with Broadcom's Tomahawk 6 shipping as the first, followed by Cisco's Silicon One G300. The next generation roadmap already targets 204.8T (Tomahawk 7) and 409.6T (Tomahawk 8).

## Broadcom Tomahawk 6 (Davisson)

**Production shipping: March 12, 2026**

| Parameter | Tomahawk 5 | Tomahawk 6 |
|---|---|---|
| Switching capacity | 51.2 Tbps | 102.4 Tbps |
| Process node | TSMC 5nm | TSMC 3nm |
| SerDes rate | 100G | 100G / 200G |
| SerDes lanes | 512 × 100G | 512 × 200G or 1024 × 100G |
| Port configurations | 128 × 400G | 512 × 200G, 256 × 400G |
| CPO support | No | Yes (co-packaged optics option) |
| AI feature | Cognitive Routing 1.0 | Cognitive Routing 2.0 |

### Key Technical Advances
- **200G SerDes per lane**: double the lane rate of Tomahawk 5
- **Co-packaged optics**: eliminates external optical transceiver module for intra-cluster links
- **Cognitive Routing 2.0**: adaptive traffic management tuned for AI training collective communication patterns (AllReduce, AllGather)
- From sampling to production in under 3 quarters

## Cisco Silicon One G300

**Announced: February 2026**

- 102.4 Tbps switching capacity
- Directly targets Broadcom Tomahawk 6 and NVIDIA Spectrum-X
- Integrated with Cisco's programmable forwarding pipeline

## NVIDIA Spectrum-X Photonic (2H 2026)

- 102.4 Tbps, but with native silicon photonics co-packaging
- 3.2T ports (silicon photonics)
- 3.5x power efficiency improvement over pluggable-optics equivalent
- Targets 400 Tbps total throughput in full 512-port configuration

## Roadmap Projection

| Generation | Capacity | Target Date |
|---|---|---|
| Tomahawk 5 | 51.2 Tbps | 2024–2025 |
| Tomahawk 6 | 102.4 Tbps | 2026 |
| Tomahawk 7 | 204.8 Tbps | 2027–2028 |
| Tomahawk 8 | 409.6 Tbps | 2029–2030 |

## Market Context

- 51.2 Tbps switch shipments: 77,000 units (2024) → **1.8 million units** (2028) — 120% CAGR (650 Group)
- Ethernet switch sales in AI back-end networks more than tripled in 2025, capturing >67% of the entire data center switch market for AI clusters
- Revenue for 800G port-based switches surged 220% QoQ in H1 2025

## Marvell Teralynx 10 (51.2T, Volume Production 2025)

- 51.2 Tbps, sub-500 ns latency
- 512 × 112G SerDes
- Lowest latency in its class at 500 ns across all packet sizes
- Volume production 2025 for global AI cloud deployments

## Strategic Observations

- The doubling of switching capacity every 18–24 months tracks closely with Moore's Law for interconnects
- CPO integration into switch ASICs eliminates the transceiver power budget (~14–20W/port at 800G)
- The tri-vendor competition (Broadcom, Cisco, NVIDIA) at 102.4T will accelerate both price compression and feature differentiation
