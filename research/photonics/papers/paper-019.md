# Paper 019: 262 TOPS Photonic AI Accelerator Using Si3N4 Frequency Comb

**Tags:** photonic-compute  
**Date:** March 2025  
**Source:** arXiv  
**URL:** https://arxiv.org/pdf/2503.03263

## Summary

This paper demonstrates a 262 TOPS (tera-operations per second) hyperdimensional photonic AI accelerator leveraging a silicon nitride (Si3N4) microresonator frequency comb as a multi-wavelength light source. The frequency comb provides many coherent optical channels for simultaneous parallel computation in a hyperdimensional computing (HDC) paradigm.

## Key Technical Specifications

- **Compute throughput:** 262 TOPS
- **Light source:** Si3N4 microcomb (frequency comb)
- **Computing paradigm:** Hyperdimensional computing (HDC)
- **Architecture:** Wavelength-multiplexed photonic matrix operations
- **Platform:** Silicon nitride photonic integrated circuit

## Technology Components

### Si3N4 Microresonator Frequency Comb
- Generates dozens of coherent optical channels from a single pump laser
- Each comb line independently carries information (WDM)
- Ultra-stable frequency spacing enables interference-based computation
- Low propagation loss in Si3N4 (<0.1 dB/cm) enables high-Q resonators

### Hyperdimensional Computing (HDC)
- HDC uses high-dimensional vector representations (~10,000 dimensions)
- Naturally suited to photonic hardware because:
  - High dimensionality → many WDM channels
  - Binding and bundling → interference operations
  - Classification → dot product threshold
- Energy per operation estimated at sub-picojoule regime

## Performance Context

| System | TOPS | Power | Architecture |
|--------|------|-------|-------------|
| This work (photonic HDC) | 262 | N/A (reported) | Si3N4 comb + HDC |
| Lightmatter Envise | 65.5 | 78W | Photonic MVM |
| NVIDIA H100 | 2,000+ | 700W | Electronic |
| Google TPUv4 | 275 | 170W | Electronic |

## Limitations

- HDC accuracy for general neural network tasks not yet demonstrated at commercial quality
- Comb stabilization requires pump laser + temperature control
- Analog precision limits effective bits of computation
- System integration (photonic chip + driver electronics) not yet reported

## Significance

262 TOPS from a photonic chip using frequency comb demonstrates that silicon nitride photonics can serve as a practical AI compute substrate beyond just optical interconnect. The frequency comb approach is scalable — more comb lines = more compute channels.
