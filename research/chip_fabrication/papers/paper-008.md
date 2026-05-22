# Paper 008: EUV Stochastic Patterning Defects — Photoresist CDU and LWR at Sub-3nm

**Source ID:** 26, 50, 59  
**Authors:** Multiple (Nature Scientific Reports, AIP Advances, Semiconductor Engineering)  
**Venue:** Scientific Reports / AIP Advances / Semiconductor Engineering  
**Date:** 2025  
**Tags:** high-NA-EUV, yield  
**URL:** https://www.nature.com/articles/s41598-025-29021-2

## Abstract / Summary

Stochastic effects in EUV lithography — arising from photon shot noise and chemical variations in photoresist — are a primary yield limiter at sub-3nm nodes. This body of 2025 research characterizes the relative contributions of material vs. optical stochastic effects on line width roughness (LWR), and provides a quantitative model for predicting "defectivity cliffs" — critical dose thresholds below which stochastic failures become unacceptably frequent.

## Key Technical Data

- **Overlay accuracy (production):** 2.0–2.5 nm on-product overlay at leading-edge 5nm and below
- **LWR target for 2nm nodes:** <1.5 nm 3-sigma
- **CDU impact:** Small CD variations amplify stochastic failures nonlinearly (exponential near defectivity cliffs)
- **Dominant mechanism:** Vertical PAG (photoacid generator) and base distribution non-uniformity causes bottom residue
- **Dose reduction approaches (2025):**
  - Intel UV+EUV co-exposure: reduces required EUV dose by ~35 mJ
  - ASM IP: dose-reducing underlayer structures
  - Lam Research: pre-exposure UV curing
- **Resolution capability (standard 0.33NA EUV):** ~13nm half-pitch
- **Resolution capability (0.55NA High-NA EUV):** ~8nm half-pitch

## Key Findings

1. Material stochastic effects dominate over optical stochastic effects at the pattern breakage regime — resist formulation is the critical knob.
2. Controlling vertical PAG distribution through resist chemistry (quencher design, post-exposure bake optimization) is the primary path to reducing CDU at 2nm and below.
3. Three independent research teams converged on dose-reduction strategies in 2025, signaling industry-wide recognition that stochastic budget is a fundamental constraint.
4. At <8nm half-pitch (High-NA EUV territory), photon shot noise becomes limiting even with optimized resists.
5. Machine learning models are being applied to predict defectivity cliffs from in-line metrology data.

## Relevance to Research Window (2025-11-22 to 2026-05-22)

Research published in 2025 with direct application to N2 and A16 patterning. EUV dose optimization is actively being implemented at TSMC and Intel fabs during the research window.
