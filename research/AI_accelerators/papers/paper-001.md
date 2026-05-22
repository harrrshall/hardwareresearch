# paper-001: Google Ironwood (TPU v7) — The First Inference-First TPU

**Tags:** transformer-accelerator, LLM-inference, systolic-array  
**Date:** April 2025 (GA release)  
**Source:** Google Cloud Blog + TPU v7 Documentation  
**URL:** https://docs.cloud.google.com/tpu/docs/tpu7x

---

## Summary

Google's seventh-generation Tensor Processing Unit, named **Ironwood**, became generally available at Google Cloud Next 2025 in Las Vegas. It is the first TPU explicitly designed and marketed for the "age of inference" rather than training.

## Architecture Details

- **Matrix Multiply Unit (MXU):** 256×256 tiles, yielding 65,536 multiply-accumulate operations per cycle (up from 128×128 in Trillium)
- **Per-Chip Performance:** 4,614 TFLOPs (FP8: 4.6 PFLOPS per chip)
- **HBM3e Memory:** 192 GB per chip, 7.4 TB/s total HBM3e bandwidth
- **Inter-Chip Interconnect (ICI):** 9.6 Tb/s, enabling seamless 9,216-chip pod communication
- **Pod Aggregate:** 42.5 Exaflops FP8 compute, 1.77 Petabytes shared HBM

## Performance Characteristics

- Designed for MoE (Mixture of Experts) and long-context inference
- Pod-level shared memory pool reduces model distribution overhead
- 256×256 MXU optimized for dense linear algebra in transformer inference layers
- ICI bandwidth allows KV-cache synchronization across chips without HBM pressure

## Competitive Context

- Tom's Hardware reports Ironwood training and inferencing pods beat NVIDIA GB300 on specific workloads
- Anthropic committed to deploy over 1 million Ironwood chips starting 2026
- Eighth-generation TPU already previewed: split into dedicated training and inference chips at TSMC 2nm

## Key Numbers

| Metric | Value |
|--------|-------|
| FP8 TFLOPS/chip | 4,614 |
| HBM3e per chip | 192 GB |
| HBM3e bandwidth | 7.4 TB/s |
| ICI bandwidth | 9.6 Tb/s |
| Pod size | 9,216 chips |
| Pod aggregate FP8 | 42.5 Exaflops |
| Shared HBM (pod) | 1.77 PB |

## Significance

Ironwood signals Google's strategic pivot from general-purpose training accelerators toward specialized inference infrastructure. The 192 GB per-chip HBM capacity — larger than the H100's 80 GB — directly targets the KV-cache bottleneck in long-context LLM serving.
