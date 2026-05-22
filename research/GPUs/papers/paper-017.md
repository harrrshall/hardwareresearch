# Paper 017: FP4/FP8 Precision Formats and Quantization in GPU Hardware

**Source ID**: src-033 (NVIDIA NVFP4), relevant sections from src-001, src-002, src-003  
**Tier**: 4 (Vendor Technical Blog)  
**Date**: 2025-02-01  
**URL**: https://developer.nvidia.com/blog/nvidia-blackwell-delivers-world-record-deepseek-r1-inference-performance/

---

## One-Sentence Claim
NVIDIA's NVFP4 format (FP8 micro-scales on 16-value blocks with FP32 global scale) achieves 88% lower quantization error than power-of-two MXFP4 alternatives and enables 30,000+ tokens/second on DeepSeek-R1 671B using 8 Blackwell GPUs — with 36x throughput improvement over January 2025 in ~6 months.

## Methodology Summary
NVIDIA published DeepSeek-R1 inference benchmarks on Blackwell B200 GPUs using NVFP4 quantization. 36x improvement figure is from January 2025 (when DeepSeek-R1 launched) to the benchmark date. NVFP4 format uses a two-level quantization scheme: FP8 micro-scales at 16-value block granularity plus a global FP32 tensor scale. AMD's MXFP4 comparison uses the OCP standard Microscaling formats. Both NVIDIA and AMD hardware support MXFP4 via Blackwell and CDNA4 respectively.

## Quantitative Results
- **DeepSeek-R1 throughput on 8x B200**: 30,000+ tokens/second
- **User concurrency**: 250+ tokens/second per user sustained
- **vs January 2025**: 36x throughput improvement (software+hardware optimizations combined)
- **NVFP4 quantization error**: 88% lower than power-of-two MXFP4 alternatives
- **NVFP4 format**: FP8 micro-scales per 16-value block + global FP32 scale
- **Blackwell FP4 tensor core throughput**: 2x vs FP8, 4x vs FP16 at same power
- **AMD CDNA4 MXFP4**: 9.2 PFLOPs peak (per MI350X); matches OCP standard
- **FP8 production deployment**: Standard for H100/H200/B200 deployment, 2x throughput vs FP16
- **FP4 production maturity**: Maturing through 2026; widespread deployment expected H2 2026

## Stated Limitations
- 36x improvement is cumulative from January 2025 (hardware + software); hardware alone is ~30x
- FP4 calibration tooling still maturing; some model architectures degrade more at FP4 than others
- NVFP4 vs MXFP4 comparison uses NVIDIA's preferred comparison methodology
- DeepSeek-R1 is MoE (mixture of experts) — FP4 gains may differ for dense transformer architectures

## Inferred Limitations
- FP4 is sensitive to outlier activations in transformers; calibration dataset quality affects deployment accuracy
- 88% lower quantization error claim for NVFP4 is on NVIDIA's chosen test distribution; adversarial distributions may differ
- FP4 on non-transformer architectures (diffusion models, GNNs) is less mature
- AMD's MXFP4 vs NVIDIA's NVFP4 creates a fragmented quantization ecosystem

## Architectural Significance
FP4 represents the frontier of reduced-precision computation. While FP8 became a production standard in 2024-2025, FP4 is the dominant precision for 2025-2026 scaling. The NVFP4 vs MXFP4 design choice is architecturally significant: NVFP4 uses FP8 micro-scales (higher precision scaling factors), while OCP MXFP4 uses power-of-two scales. The 88% lower quantization error comes from finer-grained dynamic range representation. For tensor core design, FP4 support requires hardware precision converters not present in Hopper (A100/H100) generation — Blackwell's 5th-gen tensor cores and CDNA4's matrix cores both add native FP4 paths. This enables the "quantize-at-inference" deployment model where models are stored in FP16/BF16 and quantized on-the-fly to FP4 for each layer's computation.

## Cross-Paper Connections
- src-003 (Blackwell microbenchmarks) characterizes the FP4 tensor core hardware implementation
- src-002 (CDNA4 MI350X) covers AMD's equivalent MXFP4 hardware path
- src-011 (MLPerf) shows FP8 as dominant benchmark precision with FP4 emerging
- src-012 (memory bottleneck) explains why FP4 helps: halved memory bandwidth per activation

## Theme Tags
`FP4`, `FP8`, `NVFP4`, `MXFP4`, `quantization`, `DeepSeek-R1`, `tensor-cores`, `LLM-inference`, `precision`, `Blackwell`
