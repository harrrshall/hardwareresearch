# paper-010: Chiplet-Based RISC-V SoC with Modular AI Acceleration

**Tags:** `RISC-V-AI` `mobile-NPU`
**Venue:** arXiv preprint
**Authors:** Suhas Suresh Bharadwaj et al.
**arXiv:** https://arxiv.org/abs/2509.18355
**Date:** 2025-09

---

## Summary

Proposes a novel **chiplet-based RISC-V SoC architecture** for edge AI that addresses the fundamental limitations of monolithic SoC designs through modular, composable AI acceleration. Demonstrates substantial improvements in latency, throughput, and power efficiency compared to previous chiplet approaches.

## Motivation: Monolithic SoC Limitations

- Monolithic SoC designs at advanced nodes (360 mm²) suffer <16% manufacturing yields
- Fixed function allocation cannot adapt to diverse edge AI workloads
- Tight integration limits scalability and reuse across product lines

## Architecture: 4-Innovation Chiplet Design

Integrates 4 innovations on a **30mm × 30mm silicon interposer**:

1. **Adaptive cross-chiplet DVFS:** Dynamic voltage/frequency scaling across chiplet boundaries
2. **AI-aware UCIe protocol extensions:** Modified Universal Chiplet Interconnect Express for AI tensor traffic patterns
3. **Distributed cryptographic security:** Hardware security without centralized bottleneck
4. **Intelligent load migration:** Runtime workload redistribution across AI chiplets

## Performance Results

| Metric | Improvement vs Basic Chiplet |
|--------|------------------------------|
| Latency | **14.7% reduction** |
| Throughput | **17.3% improvement** |
| Power | **16.2% reduction** |
| Combined efficiency gain | **40.1%** |

### Absolute Performance

- Energy: **~3.5 mJ per MobileNetV2 inference**
- Throughput: **244 images/sec**
- Power at throughput: **860 mW**
- Real-time capability: **sub-5ms** across all tested workloads

## RISC-V Architecture Advantages

- Open ISA enables custom AI extensions without licensing fees
- RISC-V vector (RVV) and matrix extensions accelerate tensor operations
- Chiplet disaggregation allows CPU-chiplet, NPU-chiplet, memory-chiplet to be sourced independently

## Manufacturing Implications

- Chiplet yield advantage: small dies achieve >80% yield vs <16% for monolithic 360mm² designs
- UCIe provides standardized die-to-die interface enabling multi-vendor chiplet ecosystems
- Modularity enables field-specific configurations (e.g., vision-heavy vs audio-heavy)

## Significance

This work demonstrates that RISC-V chiplet designs can achieve competitive edge AI performance with monolithic ASICs while offering dramatically better manufacturing yields and design flexibility — critical for the diverse edge AI deployment landscape.
