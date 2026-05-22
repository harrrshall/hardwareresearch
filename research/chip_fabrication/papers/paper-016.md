# Paper 016: Nanosheet Transistor Scaling Challenges Into Sub-2nm Nodes

**Source ID:** 52  
**Authors:** Multiple authors (ResearchGate / IEEE)  
**Venue:** ResearchGate Preprint / IEEE  
**Date:** 2025  
**Tags:** GAAFET, nanosheet, 2nm  
**URL:** https://www.researchgate.net/publication/381529300_Scaling_Challenges_of_Nanosheet_Field-Effect_Transistors_Into_Sub-2nm_Nodes

## Abstract / Summary

This paper provides a systematic 3D simulation study of nanosheet FET scaling from 12nm gate length down to the "ultimate" ~10nm gate length for sub-2nm nodes. It identifies the primary scaling challenges: drive current degradation with narrow sheets, increased source-drain tunneling at <10nm gate lengths, and variability from sheet thickness fluctuations. The paper proposes architectural modifications including variable-width sheets and optimized inner spacer geometries.

## Key Technical Data

- **Gate length range studied:** 12 nm → 10 nm (ultimate for sub-2nm)
- **Nanosheet width range (narrow):** 10-25 nm (low-power optimized)
- **Nanosheet width range (wide):** 60-120 nm (high-performance optimized)
- **Sheet thickness (typical):** 5-8 nm
- **Key challenge at <12nm gate length:** Source-drain direct tunneling becomes non-negligible
- **Drive current (Idsat) challenge:** Narrow nanosheets have lower current vs. wide — multi-sheet stacking compensates
- **Sheet thickness variability:** ±0.5 nm causes ~10% Vt variation in 6nm-thick sheets
- **Inner spacer thickness:** 3-5 nm typical; <3 nm increases parasitic gate-to-S/D capacitance
- **Stacking count (typical):** 3 nanosheets per GAA stack at N2; future nodes may push to 4-5 sheets

## Key Findings

1. Gate length scaling below 12nm requires innovative source-drain doping profiles to suppress direct source-drain tunneling.
2. Nanosheet width is a tunable parameter — narrow sheets for Vt control, wide sheets for maximum drive current — enabling co-design flexibility not available in FinFET.
3. Multi-stack (3→4→5 sheets) is the primary scaling lever for drive current as gate length and sheet thickness approach physical limits.
4. Inner spacer thickness uniformity is the hardest manufacturing challenge: <3nm spacers require sub-atomic-layer precision ALD.
5. At the 10nm gate length limit, electrostatic control becomes excellent (near-ideal subthreshold slope) but variability from atomic-scale effects dominates.

## Relevance to Research Window (2025-11-22 to 2026-05-22)

Directly applicable to N2 (22nm gate length, not yet at the scaling limit) and forward-looking to N2P/A16 which push nanosheet optimization further. These simulation results inform TSMC and Samsung process development during the window.
