# Paper 023: Hot Carrier Degradation in GAA Nanosheet Transistors — Reliability at 3nm/2nm

**Source ID:** 51  
**Authors:** Multiple (MDPI Micromachines)  
**Venue:** MDPI Micromachines, Vol. 16, No. 3 (2025)  
**Date:** March 2025  
**Tags:** GAAFET, nanosheet, yield  
**URL:** https://www.mdpi.com/2072-666X/16/3/311

## Abstract / Summary

This review paper systematically characterizes hot carrier injection (HCI) effects in gate-all-around nanosheet transistors at 3nm and 2nm technology nodes. Hot carriers — high-energy electrons or holes accelerated by lateral electric fields — degrade transistor characteristics over time (Vt shift, gm degradation, Ioff increase). The paper benchmarks GAA vs. FinFET reliability and identifies geometry-dependent degradation mechanisms specific to multi-sheet stacked architectures.

## Key Technical Data

- **Hot carrier mechanism:** High-energy carriers injected into gate dielectric interface traps
- **Key metric:** Vt shift after 10-year operational stress (reliability qualification standard)
- **GAA advantage vs. FinFET (HCI):** Improved short-channel control reduces lateral field, lowering HCI rate by ~15-20%
- **Nanosheet-specific concern:** Inner surface passivation quality differs from outer — asymmetric degradation
- **Critical gate length for HCI:** Below 12nm gate length, HCI rates increase significantly
- **Reliability test voltage:** 1.5-2x nominal Vdd for accelerated lifetime testing
- **Industry qualification standard:** TSMC N2 passed wafer-level reliability; Samsung SF2 qualification in progress
- **Stacking count impact:** 3-sheet stack has higher worst-case degradation than single sheet due to inner sheet inner surface exposure

## Key Findings

1. GAA nanosheet transistors have intrinsically better hot carrier immunity than FinFET at the same gate length, due to all-around gate control reducing peak lateral electric field.
2. Inner nanosheet surfaces (facing adjacent sheets) have less effective passivation than outer surfaces, creating asymmetric degradation — a manufacturing process optimization target.
3. N-type nanosheet FETs show ~70% Ion improvement (from TSMC's IEDM 2025 data) but also have proportionally higher hot carrier stress — reliability testing must account for new drive current levels.
4. 10-year reliability qualification requires careful distinction between intrinsic device degradation and extrinsic (defect-dominated) failure modes.
5. Multi-sheet 3D stacking (CFET direction) will require solved HCI management for inner sheets before commercial viability.

## Relevance to Research Window (2025-11-22 to 2026-05-22)

TSMC N2 reliability qualification (completed 2025) and Samsung SF2P qualification are both occurring at the start of and during the research window. HCI is a key qualification gate for production release.
