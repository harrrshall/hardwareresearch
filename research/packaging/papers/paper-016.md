# paper-016: Power Delivery Innovation — Package-Integrated Voltage Regulators (PIVR) and Vertical Power Delivery

**Tags:** power-delivery, IVR, advanced-packaging, vertical-power, AI
**Date Range:** 2025-Q2 – 2026-Q1
**Source IDs:** 50

---

## Summary

Power delivery in advanced packages is evolving from traditional PCB-mounted VRMs toward package-integrated voltage regulators (PIVR) and vertical power delivery (VPD) architectures. Marvell's PIVR (June 2025) claims 2x current density and 85% reduction in transmission losses. Infineon and Delta Electronics are jointly developing vertical power modules for AI data center chips.

## Technical Details

**Traditional vs. Advanced Power Delivery:**
| Architecture | VRM Location | Distance to Load | Transmission Loss |
|---|---|---|---|
| Traditional VRM | PCB, external | 30–60 mm | High (~5–15%) |
| Near-package VR | PCB, near package | 5–15 mm | Moderate |
| Package-integrated (PIVR) | Inside package | < 2 mm | Low (<2%) |
| Embedded die | In substrate | < 0.5 mm | Very low |

**Marvell PIVR (June 2025):**
- Up to 2x higher current density vs. discrete VRM
- 85% reduction in final voltage conversion transmission losses
- Integrates voltage regulator IC within the package stack
- Targets AI accelerator and XPU markets

**Vertical Power Delivery (VPD):**
- Regulator chips mounted on backside of processor die
- Reduces power delivery path from 30+ mm to < 5 mm
- Infineon + Delta Electronics collaboration: OptiMOS 90A integrated power stage
- Empower Semiconductor raised $140M to develop VR ICs for AI chips (2025)

**Embedded Passive Integration:**
- Decoupling capacitors embedded in substrate beneath processor die
- Reduces Ldi/dt transient voltage noise by 40–60%
- Required for sub-1V core voltages at >1A/μm² current density

## Key Findings

1. AI chips now operate at sub-0.7V core voltages with >100A total current — traditional PCB power delivery fails at these specifications.
2. PIVR reduces die-to-regulator inductance from ~500 pH to < 50 pH, enabling 10x faster transient response.
3. Vertical power delivery combined with embedded decoupling capacitors is now considered a standard advanced packaging feature for flagship AI accelerators.
4. The emergence of dedicated power delivery semiconductor companies (Empower Semiconductor at $140M raised) signals this is a major standalone market.
5. Package-level power integrity will be a co-design requirement alongside thermal management and signal integrity.

## Implications

The shift to PIVR and VPD is not optional for next-generation AI chips at 500W+ TDP. The power delivery network must be integrated into the package design from the outset. This creates new IP requirements and changes OSAT capabilities — OSATs must now offer embedded power delivery solutions alongside traditional wire bonding and flip-chip.
