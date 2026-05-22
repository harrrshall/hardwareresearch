# paper-011: Analog In-Memory Computing for AI — IBM and Beyond

**Tags:** analog-AI, transformer-accelerator  
**Date:** 2025  
**Source:** IBM Research Blog, arXiv 2502.04524, NextBigFuture  
**URL:** https://research.ibm.com/blog/how-can-analog-in-memory-computing-power-transformer-models

---

## Summary

Analog In-Memory Computing (AIMC) has progressed from academic curiosity to feasibility demonstrations for transformer models. IBM Research leads with 3D analog architectures for MoE inference, while academic groups demonstrate full on-chip ReRAM training and inference. The IMC segment held 38% of the analog AI chip market in 2025.

## Principle of Operation

Analog in-memory computing performs matrix-vector multiplications directly within memory arrays using Ohm's Law and Kirchhoff's Current Law:
- Memory cells store weight values as conductance levels
- Input voltages applied to rows produce current-weighted column sums
- Output current represents the dot product result
- Eliminates the fetch-compute-store cycle of digital architectures

## Key Technologies

### Phase-Change Memory (PCM) Based IMC
IBM's primary research platform:
- Each PCM cell stores a multi-bit analog weight
- On-chip precision: 4–8 effective bits per weight
- Demonstrated on transformer inference tasks at edge scale

### ReRAM (Resistive RAM) Implementation
arXiv 2502.04524 (Feb 2025): "All-in-One Analog AI Hardware":
- HfOx ReRAM with conductive-metal-oxide devices
- Demonstrated both on-chip training AND inference on same hardware
- Process: standard CMOS-compatible back-end
- Challenge: device-to-device variation and precision drift

### 3D Analog Architecture (IBM, 2025)
- Stacked analog memory layers connected by vertical interconnects
- Targets MoE models: inactive experts stored at reduced resolution
- Demonstrated outperforming GPUs on multiple metrics for MoE inference

## AIMC for LLM Attention (2025 Research)

NextBigFuture covered a paper on AIMC attention mechanisms:
- Replaces digital MatMul in self-attention with analog crossbar computation
- Status: early research stage with prototypes
- Challenges: noise sensitivity, precision limits, scaling to billion-parameter models
- Demonstrated feasibility for attention in small transformers

## Energy Efficiency

IMC reduces energy by eliminating the memory wall:
- 30x lower energy consumption vs CMOS for specific workloads
- No data movement between memory and compute arrays
- Challenge: ADC/DAC conversion overhead remains significant

## Market Context (2025)

- IMC segment: 38% of analog AI chip market
- Inference acceleration: 52% of overall analog AI chip market
- Analog AI chip market: projected $2.45 billion by 2035
- IBM, SpiNNaker, and emerging startups driving commercial interest

## Current Limitations

1. **Precision:** Typically 4-8 bits effective vs 8-16 bits for digital accelerators
2. **Noise:** Analog noise accumulates across layers, limiting network depth
3. **Programming Speed:** Writing analog weights slower than digital equivalent
4. **Temperature Drift:** Conductance values shift with temperature
5. **Scaling:** Moving to billion-parameter models requires new 3D integration approaches

## Significance

AIMC represents a potential step-change in energy efficiency — particularly for edge inference where power budgets are critical. The IBM demonstrations for MoE models suggest that analog architectures may have a natural fit for sparse activation patterns, where only a small fraction of analog cells need be read per inference pass.
