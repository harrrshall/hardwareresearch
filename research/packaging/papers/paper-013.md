# paper-013: Co-Packaged Optics (CPO) — Silicon Photonics Enters the Packaging Stack

**Tags:** CPO, silicon-photonics, advanced-packaging, optical-interconnect, AI
**Date Range:** 2025-Q4 – 2026-Q2
**Source IDs:** 60, 61, 66

---

## Summary

Co-packaged optics (CPO) integrates optical transceivers directly into the chip package, eliminating pluggable modules and reducing power consumption by 60–70%. The CPO market was $95M in 2025, growing at 37% CAGR to >$20B by 2036. NVIDIA, Broadcom, and Marvell are all shipping or sampling CPO-enabled silicon photonics solutions in 2025–2026.

## Technical Details

**CPO Architecture:**
- Silicon photonic integrated circuit (SiPho PIC) co-packaged with compute die
- Optical fiber connects directly to package (vs. pluggable SFP/QSFP on PCB edge)
- Eliminates electrical driver + retimer + pluggable module overhead
- Power reduction: ~60–70% vs. pluggable optics for 800G+ links

**Key Players and Products (2025–2026):**
| Company | Product | Bandwidth | Date |
|---|---|---|---|
| NVIDIA | Quantum-X | 1.6 Tbps CPO | H2 2025 |
| NVIDIA | Spectrum-X | 3.2 Tbps CPO | H2 2026 |
| Broadcom | CPO solution | Tested 1M link-hours (Meta, Oct 2025) | 2025 |
| Marvell | XPU + 3D SiPho | Custom AI accelerator CPO | 2025 |
| Lightmatter | Passage M1000 | 114 Tbps total optical bandwidth | 2025-Q4 |

**TSMC CPO Strategy:**
- COUPE-on-substrate approach for CPO integration
- Production scheduled to begin 2026
- Integrates photonic die and electronic die in same CoWoS-style package
- Uses active silicon photonic interposer for 3D CPO configurations

**UCIe Optical:**
- World's first UCIe optical interconnect chiplet: OFC 2025, 8 Tbps
- Brings optical bandwidth density into the chiplet ecosystem framework

**Market:**
- CPO market: $95M (2025) → $1.05B (2034) at 30.6% CAGR
- IDTechEx: $20B+ by 2036 at 37% CAGR
- Primary driver: hyperscale AI data center scale-out interconnect (800G → 1.6T → 3.2T)

## Key Findings

1. NVIDIA's move to integrated CPO in Quantum-X eliminates the need for pluggable transceiver modules entirely.
2. Broadcom validated 1 million link-hours of CPO operation at high temperature for Meta — de-risking reliability concerns.
3. Lightmatter Passage M1000 achieves 114 Tbps on-package optical bandwidth, targeting systems with thousands of GPUs in a single optical domain.
4. Marvell's XPU architecture bundles HBM, compute dies, and 3D SiPho engines on one substrate — the most integrated CPO + chiplet solution demonstrated.
5. TSMC treating CPO production as a 2026 milestone alongside CoWoS expansion.

## Implications

CPO ends the "bandwidth cliff" at the package edge that constrains GPU cluster interconnect. As AI clusters scale beyond 10,000 GPUs, electrical interconnect between machines becomes the bottleneck. CPO at 3.2 Tbps/port with >100 Tbps/package enables GPU-to-GPU communication at memory-like bandwidth, fundamentally changing cluster topology design.
