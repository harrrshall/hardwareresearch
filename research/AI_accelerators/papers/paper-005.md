# paper-005: AWS Trainium3 — Custom AI Training Accelerator at Scale

**Tags:** transformer-accelerator, LLM-inference  
**Date:** December 2025  
**Source:** HPCwire, NextPlatform, AWS Official  
**URL:** https://www.hpcwire.com/2025/12/02/aws-brings-the-trainium3-chip-to-market-with-new-ec2-ultraservers/

---

## Summary

AWS launched **Trainium3** in December 2025 alongside EC2 UltraServers, delivering 2x Trainium2's compute per chip and introducing a 144-chip UltraServer that aggregates to 362 FP8 PFLOPS — a significant leap from Trainium2.

## Trainium3 Chip Specifications

- **FP8 Compute:** 2.52 PFLOPS per chip (2x vs Trainium2)
- **HBM3e Memory:** 144 GB per chip (1.5x vs Trainium2)
- **Memory Bandwidth:** 4.9 TB/s per chip (1.7x vs Trainium2)
- **Process:** Advanced node (not publicly disclosed; likely TSMC N3 or Samsung 4nm)

## Trainium3 UltraServer

- **Chip Count:** 144 Trainium3 chips per UltraServer
- **Aggregate FP8:** 362 PFLOPS
- **Aggregate HBM3e:** 20.7 TB
- **Aggregate BW:** 706 TB/s
- **Generation-on-generation vs Trainium2 UltraServer:**
  - 4.4x more compute
  - 4x greater energy efficiency
  - 4x more memory bandwidth

## Trainium2 Comparison

| Metric | Trainium2 | Trainium3 | Improvement |
|--------|-----------|-----------|-------------|
| FP8 TFLOPS/chip | ~1.26 PFLOPS | 2.52 PFLOPS | 2x |
| HBM per chip | ~96 GB | 144 GB | 1.5x |
| Memory BW | ~2.9 TB/s | 4.9 TB/s | 1.7x |
| Price/perf vs GPU | 30-40% better than P5e | — | — |

## Trainium4 Roadmap

Already in development as of December 2025:
- 6x FP4 throughput vs Trainium3
- 3x FP8 performance vs Trainium3
- 4x memory bandwidth vs Trainium3

## AWS Custom Silicon Strategy

Trainium and Inferentia form AWS's vertical integration play. Trainium3 targets training workloads where AWS's customer captivity (internal use + Bedrock customers) provides a market without direct retail comparison. Priced at 30-40% better price/performance than equivalent NVIDIA P5e/P5en instances.

## Key Architectural Features

- NeuronLink high-bandwidth chip-to-chip interconnect for UltraServer aggregation
- NeuronCore-v3 compute units with native FP8 support
- Compiler-driven static parallelism (similar philosophy to Groq LPU) for predictable performance
- PyTorch/JAX compatibility via AWS Neuron SDK

## Significance

Trainium3 demonstrates AWS's accelerating custom silicon cadence. The UltraServer concept — aggregating 144 chips into a single compute unit — mirrors the rack-scale approach of NVIDIA NVL72 and Google's TPU pods, validating that large-scale disaggregated training is now the architectural norm for hyperscalers.
