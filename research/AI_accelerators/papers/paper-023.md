# paper-023: Intel Gaudi 3 — Open Standards AI Accelerator

**Tags:** transformer-accelerator, LLM-inference  
**Date:** 2025  
**Source:** Intel Official Docs, IEEE Spectrum, SqueezeBits Blog  
**URL:** https://cdrdv2-public.intel.com/817486/gaudi-3-ai-accelerator-white-paper.pdf

---

## Summary

Intel Gaudi 3 is Intel's third-generation AI accelerator, targeting the NVIDIA GPU market with an open-ecosystem approach. It delivers 1.8 PFLOPS FP8/BF16 compute, 128 GB HBM2e per card, and 95–170% of H100 performance on LLM benchmarks while maintaining competitive pricing.

## Core Specifications

| Metric | Gaudi 3 |
|--------|---------|
| FP8/BF16 Compute | 1.8 PFLOPS |
| HBM2e Memory | 128 GB |
| HBM Bandwidth | 3.7 TB/s |
| Memory vs Gaudi 2 | +1.5x bandwidth, +33% capacity |
| Process | TSMC N5 |
| Power | ~600W (OAM form factor) |

## Architecture

Gaudi 3 uses Intel's Matrix Multiply Engines (MMEs) with a systolic array design:
- 8 MMEs per chip
- Support for FP8, BF16, TF32 precision formats
- 128 GB HBM2e: more capacity than H100 (80 GB), competitive with H200 (141 GB)
- Ethernet-native interconnect (100 GbE/200 GbE) — no proprietary NVLink equivalent

## Performance vs H100

| Model | Gaudi 3 vs H100 (%) |
|-------|---------------------|
| Llama-2 (various sizes) | 95–170% |
| Falcon 180B | 400% (4x advantage) |
| General inference range | 95–170% |

The Falcon 180B advantage comes from Gaudi 3's larger 128 GB HBM capacity vs H100's 80 GB — enabling larger batch sizes without model sharding.

## Open Ecosystem Advantage

Gaudi 3 differentiates with openness:
- **Standard Ethernet interconnect** (not proprietary NVLink)
- **PyTorch via Intel Habana** SDK — no CUDA-exclusive code required
- **Open recipes** for Llama, Falcon, Mistral on Intel Developer Cloud
- **Price-competitive** vs NVIDIA H100/H200 in cloud pricing

## Gaudi 3 vs H200 Context (2025)

At the time of Gaudi 3 deployments, H200 dominated the market but Gaudi 3 offered:
- 128 GB HBM2e vs H200's 141 GB HBM3e (less bandwidth but larger capacity)
- Competitive on long-context inference where capacity matters more than bandwidth
- 40% lower power consumption vs H200 on specific inference workloads
- Open networking interconnect reduces cluster configuration complexity

## 2025 Deployment Landscape

Gaudi 3 is deployed across:
- Intel Developer Cloud (public access)
- HPC user forum benchmarks (published April 2025)
- Supermicro server systems (dual-card OAM configurations)
- Government HPC facilities

## Limitations vs NVIDIA Blackwell

- No FP4 support (Blackwell has NVFP4)
- Ethernet interconnect bandwidth (~100-200 GbE) far lower than NVLink (1.8 TB/s)
- Software ecosystem significantly smaller than CUDA
- No equivalent of NVL72 rack-scale system

## Significance

Gaudi 3 demonstrates that non-NVIDIA architectures can achieve production AI workload parity for specific use cases. Its success with memory-heavy models (128 GB HBM) and open interconnect standards represents a viable alternative trajectory for AI infrastructure that avoids NVIDIA vendor lock-in. The transition to Gaudi 4 (unannounced as of this research window) remains uncertain given Intel's broader financial challenges.
