# Paper 002: AMD MI350X/MI355X — CDNA4 Architecture and Performance

**Source ID**: src-002, src-004, src-015  
**Tier**: 4 (Vendor Disclosure)  
**Date**: 2025-06-12  
**URL**: https://www.amd.com/en/products/accelerators/instinct/mi350/mi350x.html

---

## One-Sentence Claim
The AMD Instinct MI350X/MI355X, based on CDNA4 architecture on TSMC 3nm, delivers up to 9.2 PFLOPS MXFP4 performance with 288GB HBM3E at 8TB/s, achieving 4x generational compute gains and 35x inference improvement over MI300X.

## Methodology Summary
AMD presented MI350 series at launch events and Hot Chips 2025. Performance claims include MLPerf submissions comparing MI355X to MI325X. The CDNA4 architecture whitepaper details the micro-architectural changes. Benchmarks run on Llama 2 70B server and offline scenarios at FP8 precision.

## Quantitative Results
- **Peak MXFP4**: 9.2 PFLOPs per MI350X
- **Peak MXFP6**: 9.2 PFLOPs
- **Peak MXFP8**: 4.6 PFLOPs
- **Peak FP16**: 2.3 PFLOPs
- **Memory**: 288GB HBM3E at 8TB/s bandwidth
- **Matrix Cores**: 1,024 per GPU (256 Compute Units)
- **Transistors**: 185 billion
- **Process**: TSMC N3P (3nm) XCDs + TSMC N6 (6nm) base dies
- **XCDs**: 8 Accelerator Complex Dies + 2 base dies
- **MI355X vs MI325X**: 2.7x more tokens/s on Llama 2 70B server at FP8
- **Gen-over-gen**: 4x AI compute improvement vs MI300X
- **Inference**: 35x faster than MI300X
- **InferenceMAX**: 5x generational improvement from MI300X to MI355X
- **8x MI355X vs 4x DGX GB200**: 1.3x faster on Llama 3.1 405B inference
- **8x MI355X vs 8x B200 HGX**: 1.2x faster on DeepSeek-R1 at FP4
- **TDP**: MI350X 1000W, MI355X 1400W
- **Infinity Fabric**: 5.5 TBps inter-die bandwidth
- **Scale**: 128 liquid-cooled GPUs = 2.6 exaflops FP4, 36TB HBM3E

## Stated Limitations
- 4x and 35x figures compare to MI300X using latest CDNA4 software optimizations
- FP4 comparisons require MXFP4 calibration, still maturing in deployment
- 1400W TDP for MI355X requires advanced thermal management
- Limited to AMD's ROCm software stack; CUDA compatibility requires HIP translation overhead

## Inferred Limitations
- 185B transistor chiplet requires sophisticated die stacking and yield management
- Infinity Fabric inter-die bandwidth of 5.5 TBps creates potential intra-GPU communication bottleneck for certain workloads
- Ecosystem gap: CUDA-native frameworks run natively on NVIDIA; ROCm requires porting
- H100/B200 still outperform on training-focused workloads requiring FP64 or TF32

## Architectural Significance
CDNA4 represents AMD's most aggressive generational leap in compute density. The 3D chiplet approach (8 compute dies + 2 base dies) is AMD's response to TSMC reticle limits. Doubling matrix core throughput for all low-precision formats simultaneously with adding MXFP4/MXFP6 support mirrors NVIDIA's FP4 introduction in Blackwell. 2:4 structured sparsity hardware matching NVIDIA's sparse tensor core approach. The MI355X matching or exceeding B200 on select inference benchmarks represents AMD's strongest competitive showing in datacenter AI.

## Cross-Paper Connections
- src-005 (Hot Chips 2025) provides deeper architectural detail on MI350
- src-019 (ROCm 7) covers software stack enabling 3.5x inference improvement
- src-041 (FP8 matrix characterization) provides independent validation methodology
- src-042 (matrix core programming) covers CDNA4 programming model
- src-026 (MI400 roadmap) shows trajectory toward CDNA5 with HBM4
- src-032 (InferenceMAX benchmarks) provides third-party competitive analysis

## Theme Tags
`CDNA4`, `MI350X`, `MI355X`, `HBM3e`, `MXFP4`, `matrix-cores`, `sparsity`, `chiplet-GPU`, `AMD-Instinct`, `inference`, `ROCm`
