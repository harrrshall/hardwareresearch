# Paper 003: Microbenchmarking NVIDIA Blackwell Architecture

**Source ID**: src-020, src-021  
**Tier**: 2 (arXiv Preprint)  
**Date**: 2025-12-03 / 2025-07-14  
**URLs**:  
- https://arxiv.org/abs/2512.02189  
- https://arxiv.org/abs/2507.10789

---

## One-Sentence Claim
Independent microbenchmarks of NVIDIA Blackwell reveal that unified INT32/FP32 cores, per-SM 256KB TMEM, warp-level MMA scheduling (eliminating Hopper's 4-warp sync requirement), and 3x sparsity throughput represent fundamental architectural advances — while FP64 performance regressed to 2 units/SM (vs 64 in GH100).

## Methodology Summary
Researchers used CUDA microbenchmark programs to probe the Blackwell microarchitecture systematically: latency/throughput tests for each instruction type, pointer-chasing for memory hierarchy mapping, warp scheduling pressure experiments, and MMA instruction timing. Tested on B200/B100 hardware using CUDA 12.6+. Cross-validated with NVIDIA's published architectural documentation.

## Quantitative Results
- **FP4/FP6 tensor core throughput**: Natively supported via micro-tensor formats with dynamic range scaling
- **Sparse computation**: 3x throughput improvement over dense when fine-grained structured sparsity enabled
- **TMEM**: 256 KB per SM (new to Blackwell, absent in Hopper)
- **Warp MMA sync**: Eliminated Hopper requirement for 4 warps to synchronize per wgmma operation
- **FP64 units**: 2 per SM vs. 64 per SM in GH100 — Blackwell ~32x worse at FP64
- **Mixed INT32/FP32**: Blackwell outperforms Hopper (GH100) on mixed instruction sequences
- **Dual-TB MMA**: Paired SMs can cooperate on single MMA, sharing operands, reducing memory traffic
- **Decompression engine**: Dedicated hardware for on-the-fly decompression of compressed sparse data from HBM
- **TMEM usage**: Compressed sparse rows stored in HBM, decompressed rows streamed into TMEM for reduction
- **Block-level MMA granularity**: Finer than Hopper, enabling more flexible SM utilization

## Stated Limitations
- Microbenchmarks run on pre-production/early engineering samples in some cases
- Not all Blackwell features were fully exposed in CUDA 12.6 at time of writing
- Vendor documentation sometimes unavailable, requiring inference from behavior
- FP64 regression well-documented but no official NVIDIA statement explaining the architectural trade-off

## Inferred Limitations
- Dual-thread-block MMA benefit limited to workloads that can restructure for paired SM cooperation
- TMEM as shared operand buffer introduces new synchronization concern between TB pairs
- 256KB TMEM is only beneficial when tensor operations can exploit it; irregular workloads see no gain
- The sparsity engine requires 2:4 structured sparsity; unstructured sparsity sees no hardware benefit

## Architectural Significance
This independent analysis is the most detailed publicly available microarchitectural characterization of Blackwell. Key findings: (1) Blackwell explicitly deprioritizes HPC/scientific (FP64) in favor of AI (FP4/FP8/FP16) — a strategic architectural divergence from Hopper; (2) The TMEM + decompression engine forms a dedicated sparsity execution subsystem, not just a software technique; (3) Eliminating warp group MMA synchronization requirements reduces scheduling overhead for transformer-heavy kernels; (4) FP4/FP6 micro-tensor format is a novel quantization paradigm. The dual-thread-block MMA innovation is architecturally novel with no prior published description.

## Cross-Paper Connections
- src-001 (Blackwell performance) provides the application-level context this work explains mechanistically
- src-031 (Acc-SpMM) shows how sparse tensor cores are exploited in practice
- src-033 (DeepSeek-R1 Blackwell) demonstrates NVFP4 inference enabled by these hardware features
- src-034 (memory bottleneck paper) contextualizes the TMEM's role in reducing HBM traffic

## Theme Tags
`blackwell`, `tensor-cores`, `sparsity`, `TMEM`, `warp-scheduling`, `FP4`, `FP64-regression`, `microbenchmark`, `MMA`, `arXiv`
