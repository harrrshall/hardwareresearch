# Paper 008: NVIDIA DLSS 4 and Neural Rendering Advances

**Source ID**: src-018, src-030  
**Tier**: 4 (Vendor Disclosure)  
**Date**: 2025-01-06 (DLSS 4), 2026-01-06 (DLSS 4.5)  
**URL**: https://www.nvidia.com/en-us/geforce/news/dlss4-multi-frame-generation-ai-innovations/

---

## One-Sentence Claim
DLSS 4 (January 2025) and DLSS 4.5 (January 2026) mark a paradigm shift in GPU-driven neural rendering: the first real-time transformer-based AI model for super resolution, generating up to 3 (and later 6) AI-synthesized frames per rendered frame, multiplying effective framerate by up to 8x (later more) using Blackwell tensor cores.

## Methodology Summary
NVIDIA launched DLSS 4 with RTX 50 series (Blackwell) consumer GPUs in January 2025. Performance measurements are rendered-frame comparisons in supported games vs. brute-force rendering and prior DLSS versions. The transformer model architecture change is documented in NVIDIA's DLSS technical blog. DLSS 4.5 announced CES 2026 with 6X Dynamic Multi Frame Generation and 2nd generation transformer model. Game support: 75 games at DLSS 4 launch, 125+ by Computex 2025, 250+ by CES 2026.

## Quantitative Results
- **DLSS 4 Multi Frame Generation (MFG)**: Generates up to 3 additional frames per rendered frame
- **Framerate multiplier**: Up to 8x over brute-force rendering (MFG + Ray Reconstruction + Super Resolution combined)
- **vs. DLSS Frame Generation (DLSS 3)**: Up to 1.7x boost upgrading from FG to MFG
- **4K full ray tracing**: RTX 5090 achieves 240 FPS with DLSS 4 MFG
- **Architecture change**: Transformer model replaces 6-year-old CNN architecture for Super Resolution, Ray Reconstruction, DLAA
- **DLSS 4.5**: 6X Dynamic Multi Frame Generation (twice the frames vs. DLSS 4 MFG)
- **DLSS 4.5 SR**: 2nd generation transformer model for super resolution
- **Game support**: 250+ DLSS 4 Multi Frame Generation games by CES 2026
- **MFG restriction**: Multi Frame Generation hardware-exclusive to RTX 50 series Blackwell GPUs
- **Older card support**: Super Resolution transformer model update available for RTX 20/30/40 series

## Stated Limitations
- Multi Frame Generation is RTX 50 series Blackwell exclusive (hardware requirement)
- Generated frames introduce latency; NVIDIA Reflex 2 required to compensate
- Transformer model requires more compute per frame than CNN predecessor
- 8x framerate multiplier is peak theoretical; typical games see 3-5x depending on RT content

## Inferred Limitations
- Frame generation artifacts more visible in fast-motion scenes with AI-generated frames
- 6X MFG in DLSS 4.5 requires very high base framerates to avoid perceptible lag artifacts
- Transformer model inference uses tensor core cycles that compete with game rendering if tensor cores are insufficient
- Multi-frame generation fundamentally inserts latency between input and visual response (2 vs 1 generated frame buffer)

## Architectural Significance
DLSS 4's shift from CNN to transformer architecture is the first production deployment of real-time transformer inference on consumer GPU hardware. This demonstrates that Blackwell's 5th-gen tensor cores have sufficient headroom beyond game rendering to run a full transformer inference stack in a game's frame budget. The 6X MFG in DLSS 4.5 requires GPU-side AI acceleration that was computationally impossible before Blackwell's FP8/FP4 tensor core throughput. DLSS 4's game adoption trajectory (75 → 250+ games in 12 months) demonstrates the industry now treats AI-accelerated rendering as a required feature, not an optional enhancement.

## Cross-Paper Connections
- src-005 (RDNA4) covers competing AMD FSR4 transformer-based super-resolution
- src-017 (RTX 5090) covers the Blackwell gaming GPU enabling DLSS 4 hardware features
- src-003 (Blackwell tensor cores) explains the hardware enabling real-time transformer inference

## Theme Tags
`DLSS4`, `neural-rendering`, `tensor-cores`, `transformer-model`, `consumer-GPU`, `ray-tracing`, `AI-rendering`, `Blackwell`, `multi-frame-generation`
