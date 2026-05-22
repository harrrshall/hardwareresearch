# paper-022: Google TPU v5p and Trillium (v6e) — Systolic Array Evolution

**Tags:** systolic-array, transformer-accelerator, LLM-inference  
**Date:** 2024–2025  
**Source:** Google Cloud Documentation, Google Blog  
**URL:** https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus

---

## Summary

Google's TPU v5p and TPU v6 (Trillium/v6e) represent back-to-back generations of systolic array evolution. The v5p established the architecture for large-scale training pods, while Trillium quadrupled the MXU array size to achieve 4.7x the compute of v5e. Together they establish the baseline against which Ironwood (v7) is measured.

## TPU v5p Architecture

### Systolic Array Topology
- **3D Torus Interconnect:** Each chip connects to 6 neighbors in X, Y, Z dimensions
- **Pod Size:** 8,960 chips
- **ICI Bandwidth:** 4,800 Gbps per chip (six 3D torus links combined)
- **Pod Aggregate:** 460 petaFLOPS
- **Topology Advantage:** For 4,096-chip pod, maximum hops: 48 (vs 128 for H100 fat-tree at same scale)

### Training Optimization
The 3D torus topology minimizes all-reduce communication latency in distributed training:
- Model parallel: each chip holds a shard; 3D torus enables low-latency ring-allreduce
- Pipeline parallel: depth of torus enables deep pipeline staging
- Data parallel: multiple pods can coordinate efficiently

## TPU v6e (Trillium) Architecture

### MXU Scale-Up
- **Previous (v5e):** 128×128 matrix multiply unit
- **Trillium:** 256×256 matrix multiply unit
- **Scale factor:** 4x the multiply-accumulate operations per cycle
- **Result:** 4.7x peak compute performance vs v5e

### Other Improvements
- **HBM:** Doubled capacity and bandwidth vs v5e
- **ICI:** Doubled interchip interconnect bandwidth vs v5e
- **Performance/Cost:** 2.1x improvement per dollar over v5e for LLM training

### BF16 TFLOPS
- TPU v5p: ~459 BF16 TFLOPS per chip
- TPU v6e (Trillium): ~918 BF16 TFLOPS per chip (2x per chip vs v5p for BF16)

## Trillium Performance on LLMs

For training dense LLMs (Llama2-70B, Llama3.1-405B):
- **vs TPU v5e:** 2.1x performance per dollar
- **vs TPU v5p:** 2.5x performance per dollar

## Systolic Array Design Philosophy

Google's systolic arrays are specifically designed for:
1. **Dense Matrix Multiply:** The core operation of transformer FFN layers
2. **No Cache:** Unlike GPUs, no L1/L2 cache hierarchy — all data flows through the systolic array
3. **Deterministic Performance:** Software can predict exactly when data arrives
4. **TPU Compiler (XLA):** Tightly coupled compiler controls data flow and memory staging

## Architectural Comparison

| Generation | MXU Size | BF16 TFLOPS | HBM BW | ICI BW |
|-----------|----------|-------------|--------|--------|
| TPU v5e | 128×128 | ~459 | baseline | baseline |
| TPU v5p | 128×128 | ~459 | higher | 4,800 Gbps/chip |
| TPU v6e (Trillium) | 256×256 | ~918 | 2x v5e | 2x v5e |
| TPU v7 (Ironwood) | 256×256 | 4,614 TF FP8 | 7.4 TB/s | 9.6 Tb/s |

## Significance

The progression from v5p → Trillium → Ironwood shows Google consistently doubling systolic array capabilities every generation. The jump to 256×256 in Trillium and maintaining it in Ironwood (while dramatically increasing clock rate and bandwidth) demonstrates that MXU width has reached a practical optimum for single-chip design — future gains come from bandwidth, density, and multi-chip coordination rather than wider arrays.
