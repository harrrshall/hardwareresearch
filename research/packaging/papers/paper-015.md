# paper-015: NVIDIA Blackwell GB200 — CoWoS-L Packaging and 8 TB/s HBM3e Architecture

**Tags:** CoWoS, NVIDIA, HBM3e, 3D-stacking, interposer, AI
**Date Range:** 2025-Q4 – 2026-Q1
**Source IDs:** 65

---

## Summary

NVIDIA's Blackwell B200 GPU uses TSMC's CoWoS-L packaging with two GPC dies and eight HBM3e stacks, delivering 8 TB/s memory bandwidth per GPU. The package exceeds the reticle-size limit, requiring a Local Silicon Interconnect (LSI) bridge rather than a monolithic silicon interposer. The B200's BOM places packaging cost ($1,100) as 17% of total manufacturing cost ($6,400).

## Technical Details

**Package Architecture:**
- Two B200 GPU dies (N4P process, each ~800 mm²)
- 8× HBM3e stacks (8-Hi, 24 GB each = 192 GB total)
- Total active silicon area: ~3,200 mm² (logic) + HBM footprint
- Package substrate: CoWoS-L organic interposer with LSI bridges
- Package size: ~6,000 mm² total footprint

**Memory Specifications:**
| Parameter | H100 (HBM3) | B200 (HBM3e) |
|---|---|---|
| Memory | 80 GB | 192 GB |
| Bandwidth | 3.35 TB/s | 8.0 TB/s |
| HBM stacks | 6 | 8 |
| Interface width | 5,120-bit | 8,192-bit |
| Die stack height | 8-Hi | 8-Hi |

**CoWoS-L vs. CoWoS-S:**
- CoWoS-S: monolithic silicon interposer, limited to ~2 reticles
- CoWoS-L: organic substrate + embedded LSI silicon bridges
- LSI bridge: ~50–100 mm², handles die-to-die signal routing at critical paths
- CoWoS-L allows unrestricted package size (currently 5.5–6 reticle equivalents)

**BOM Cost Breakdown ($6,400 total):**
- HBM3e: $2,900 (45%)
- Logic dies: $1,400 (22%)
- CoWoS packaging: $1,100 (17%)
- Other: $1,000 (16%)

## Key Findings

1. CoWoS packaging at 17% of BOM is now a cost-critical component — comparable to traditional SoC substrate costs for flagship products.
2. 8 TB/s aggregate HBM3e bandwidth is 2.4x H100 — enabled by adding 2 more HBM stacks and switching to HBM3e.
3. CoWoS-L was specifically required because two full GPU dies + 8 HBM stacks exceed a single silicon interposer's reticle limit.
4. The B200 package represents the current practical limit of CoWoS packaging: further scaling requires 14-reticle format (2028 roadmap).
5. TSMC's CoWoS ramp from 35K to 130K wafers/month is almost entirely driven by B200/GB200 demand.

## Implications

The B200 package architecture will be the template for all flagship AI accelerators through 2026–2027. The packaging cost per unit (~$1,100) will drive continued investment in efficiency improvements. The transition to HBM4 (2 TB/s/stack × 8 = 16 TB/s) expected in NVIDIA Rubin (2026) will require new CoWoS variants to handle the wider interface.
