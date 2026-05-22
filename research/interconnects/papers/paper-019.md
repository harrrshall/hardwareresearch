# paper-019: 800G to 1.6T Ethernet Transition — AI Data Center Scale-Out 2025-2026

**Tags:** chip-to-chip  
**Date:** 2025-2026  
**Source:** Introl Blog, 650 Group, Keysight  
**URL:** https://introl.com/blog/800g-networking-ai-gpu-fabric-planning-2025

---

## Summary

800G Ethernet became the de facto standard for AI data center scale-out networking in 2025, with revenue surging 220% QoQ in H1 2025. The transition to 1.6T is expected to begin in H2 2026, driven by IEEE 802.3dj standardization and Tomahawk 7/Spectrum-X Photonic switch availability.

## 800G Ethernet Deployment (2025)

### Key Metrics
| Metric | Value |
|---|---|
| Ethernet switch AI share | >67% of datacenter switch market |
| Revenue growth H1 2025 | 220% QoQ |
| Dominant port speed | 800G OSFP |
| Leading vendors | Celestica + NVIDIA (50% combined) |

### 800G Technical Details
| Parameter | Value |
|---|---|
| Per-port speed | 800 Gbps |
| Lanes | 8 × 100G PAM4 |
| Module type | OSFP, QSFP-DD |
| Module power | 14–20 W per port |
| LPO power reduction | ~30% lower vs retimed optics |

### Linear Pluggable Optics (LPO)
- Removes signal regeneration (retimer) from optical module
- 800G LPO consumes ~10 W/port vs 14–20 W for retimed
- Emerging standard for within-rack AI cluster fabric
- IEEE P802.3df standardization track for 800G LPO

## 1.6T Transition Timeline

| Milestone | Date |
|---|---|
| IEEE 802.3dj 1.6T standardization completion | 2026 |
| First 1.6T switch products available | H2 2026 |
| Hyperscale deployment of 1.6T | 2027 |
| Mainstream 1.6T adoption | 2028 |

## 1.6T Technical Requirements

| Parameter | 800G | 1.6T |
|---|---|---|
| Lanes | 8 × 100G | 8 × 200G or 16 × 100G |
| Symbol rate | 112 GBaud PAM4 | 224 GBaud PAM4 |
| Module power | 14–20 W | 25–35 W (estimated) |
| CPO benefit | Optional | Critical (power budget) |

## Infrastructure Challenges

### Power Density
- 800G modules at 14–20 W/port × 512 ports = 7–10 kW just for optics in one switch
- 1.6T without CPO would push this to 13–18 kW/switch
- CPO at 1.6T reduces optical power by 60–70% (critical for deployment viability)

### Signal Integrity
- 224 GBaud PAM4 requires tighter channel control
- Strict PCB design rules for 200G/lane: shorter traces, less tolerance for FR4 dielectric variation
- Active Electrical Cables (AECs) emerging for rack-level 1.6T without optics penalty

## ESUN and Scale-Up Ethernet

OCP ESUN initiative (October 2025) specifically targets using 800G/1.6T Ethernet for **scale-up** (intra-AI-pod), not just scale-out:
- AMD, Broadcom, Cisco, Meta, Microsoft, NVIDIA all participating
- Aims to reduce the cost/complexity premium of NVLink for AI pods where latency tolerance is slightly higher
- First ESUN switch reference designs expected 2026

## Key Vendor 1.6T Roadmap

| Vendor | Product | Capacity | Timeline |
|---|---|---|---|
| Broadcom | Tomahawk 7 | 204.8 Tbps | 2027–2028 |
| NVIDIA | Spectrum-X Photonic | 102.4 Tbps @ 1.6T | H2 2026 |
| Cisco | Silicon One G400 | TBD | 2027 |
| Marvell | Teralynx 20 | ~102.4 Tbps | 2027 |

## Strategic Observations

- 800G LPO adoption is accelerating as hyperscalers prioritize power efficiency over module feature richness
- The 1.6T transition will be impossible at scale without CPO — power budgets simply don't work with pluggable optics
- Ethernet's 67% market share in AI back-end networking is a structural shift; InfiniBand will retain HPC supercomputer segment but lose share in hyperscale AI
