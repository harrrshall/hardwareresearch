# Paper 001: NVIDIA Blackwell GB200/GB300 Training and Inference Performance

**Source ID**: src-001, src-012, src-013  
**Tier**: 4 (Vendor Disclosure)  
**Date**: 2025-03-18  
**URL**: https://developer.nvidia.com/blog/nvidia-blackwell-enables-3x-faster-training-and-nearly-2x-training-performance-per-dollar-than-previous-gen-architecture/

---

## One-Sentence Claim
NVIDIA Blackwell GB200 and GB300 architectures deliver up to 3.2x faster LLM training and 30x inference throughput improvement over H100, enabled by FP4 tensor computation, NVLink 5.0, and the dual-die GB chip design.

## Methodology Summary
NVIDIA published MLPerf-style training benchmarks on Llama 3.1 405B using FP8 precision. Inference measurements compare equal GPU counts on LLM workloads. Performance-per-dollar claims use TCO modeling including power and system cost. GB200 NVL72 is a 72-GPU rack-scale system; GB300 NVL72 (Blackwell Ultra) is the successor.

## Quantitative Results
- **GB200 NVL72 training**: 3.2x faster than Hopper FP8 on Llama 3.1 405B pretraining
- **GB200 inference**: 30x faster throughput vs. same count of H100s for LLM inference
- **GB200 performance/dollar**: ~2x vs. H100 system
- **GB200 NVL72 rack compute**: 1.44 EXAFLOPS FP4 (1,440 PFLOPS)
- **GB300 (Blackwell Ultra)**: 1.1 EXAFLOPS per NVL72 rack in FP4, 1.5x over GB200 NVL72
- **GB300 memory**: 288GB HBM3E at 8 TB/s per GPU, up from GB200's 192GB
- **GB300 TDP**: 1,400W per GPU
- **NVLink 5.0**: 1,800 GB/s bidirectional per GPU (18 links x 100 GB/s)
- **NVLink system aggregate**: 130 TB/s per GB200 NVL72 rack

## Stated Limitations
- 30x inference speedup is for LLM inference; does not apply to all workloads
- FP4 precision requires calibration; production deployment still maturing
- GB300 NVL72 racks drive power demands to 250kW+, requiring specialized facilities
- Results are vendor-reported, not third-party audited

## Inferred Limitations
- FP64 performance regressed significantly vs. GH100 (only 2 FP64 units/SM in Blackwell vs. 64 in GH100), limiting HPC applicability
- 30x inference claim likely assumes H100 SXM reference without tensor parallelism optimization
- GB300 rack at 250kW+ limits deployment to purpose-built liquid-cooled facilities
- Sustained throughput depends heavily on memory capacity and model size

## Architectural Significance
The GB200/GB300 transition marks the shift to exascale-in-a-rack computing. The dual-die design (two reticle-limited dies connected via 10 TB/s NV-HBI interface) overcomes lithography reticle limits. FP4 tensor cores represent a 2-precision-level advance beyond FP8 for transformer inference. NVLink 5.0 at 1.8 TB/s/GPU makes the 72-GPU rack behave as a single logical device. The Blackwell Ultra GB300 shows NVIDIA's annual cadence architecture evolution pattern.

## Cross-Paper Connections
- src-020 (microbenchmarking paper) independently validates Blackwell tensor core capabilities
- src-014 (MLPerf v5.1) provides third-party validation of training performance claims
- src-025 (TSMC CoWoS) explains supply constraints limiting GB300 availability
- src-006 (NVLink 5.0) provides detailed NVLink specification context
- src-029 (deployment guide) covers facility requirements for NVL72 racks

## Theme Tags
`blackwell`, `FP4`, `tensor-cores`, `NVLink`, `exascale`, `HBM3e`, `LLM-inference`, `training-performance`, `GB200`, `GB300`
