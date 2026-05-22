# Paper 022: TSMC N2P and N2X — Performance-Enhanced 2nm Variants with BSPDN

**Source ID:** 49  
**Authors:** TSMC Technology Team / Tom's Hardware  
**Venue:** Tom's Hardware / TSMC Technology Disclosures  
**Date:** 2025-2026  
**Tags:** GAAFET, 2nm, BSPDN, nanosheet  
**URL:** https://www.tomshardware.com/news/tsmc-readies-n2p-and-n2x-2nm-with-enhanced-performance

## Abstract / Summary

TSMC's N2 node family includes three variants beyond the baseline: N2P (performance + backside power, H2 2026), N2X (maximum performance for HPC, 2027), and N2U (power-efficient ultralow-leakage mobile variant, timing TBD). N2P introduces backside power delivery as a step toward A16, while maintaining the N2 nanosheet transistor architecture. N2X will target AI training accelerators and HPC CPUs requiring maximum clock frequency.

## Key Technical Data

**N2P Specifications:**
- **Transistor density (HD library):** 236 MTr/mm²
- **Performance vs. baseline N2:** +18% speed at iso-power/area
- **Power vs. baseline N2:** -36% at same clock speed
- **BSPDN:** Yes — full backside power delivery (precursor architecture to A16 SPR)
- **Volume production:** H2 2026
- **Primary customers:** AI accelerators, next-gen server chips

**N2X Specifications:**
- **Architecture:** Same nanosheet as N2, but optimized for high-voltage/high-frequency operation
- **Target:** Maximum clock frequency — HPC and AI training
- **Production:** ~2027
- **Key feature:** Supports higher supply voltages (Vdd) for maximum drive current

**N2 Baseline Reference:**
- Density: ~192-216 MTr/mm² (HP/HD library range)
- Gate length: 22 nm
- Channel width: 45 nm

## Key Findings

1. N2P represents an 18% performance jump even within the same 2nm process generation — primarily enabled by backside power routing freeing signal metal layers.
2. N2P's 236 MTr/mm² density (HD) surpasses N3E's 216 MTr/mm² — making N2P a strong migration target for 3nm customers.
3. The 36% power reduction of N2P is transformative for AI training efficiency: NVIDIA's next-generation GPU on N2P could halve training energy per token.
4. N2X's higher voltage operation enables overclocking scenarios critical for HPC customers — targeting 5+ GHz chip designs.
5. The N2 family (N2, N2P, N2X, N2U) is expected to be in active production simultaneously by 2028, catering to mobile, AI, and HPC markets separately.

## Relevance to Research Window (2025-11-22 to 2026-05-22)

N2P is in process development and early customer tape-out during the research window, targeting H2 2026 production. Design kits and customer sampling are active during the window.
