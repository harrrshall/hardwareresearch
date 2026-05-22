# Paper 008: Google TPU v7 Ironwood — Cluster Architecture and Infrastructure (2025–2026)

**Tags:** AI-cluster, rack-scale, thermal-management
**Source:** Google Cloud Blog, SemiAnalysis, Google documentation
**Date:** April 2025 announcement; 2026 deployment
**Relevance:** High

## TPU v7 (Ironwood) System Architecture

Google unveiled TPU v7 Ironwood in April 2025. It represents a fundamental shift from training-optimized to inference-optimized design.

## Chip Specifications

| Parameter | Value |
|-----------|-------|
| TensorCores per chip | 2 |
| SparseCores per chip | 4 |
| MXU Array Size | 256×256 |
| Peak BF16 TFLOPS | ~2,300 (est.) |
| Peak FP8 PFLOPS | 4.6 |
| HBM3e memory | 192 GB per chip |
| HBM3e bandwidth | 7.37 TB/s per chip |
| Power per chip | 157 W |

## Inter-Chip Interconnect (ICI)

- ICI bandwidth: 9.6 Tb/s per chip
- Enables thousands of chips to act as a single compute surface
- Single Ironwood Superpod: 9,216 chips connected via ICI
- Pod memory: 1.77 PB shared HBM3e
- Pod peak: 4,614 TFLOPS FP8 per chip × 9,216 = ~42 ExaFLOPS per pod
- Pod power: approximately 10 MW

## Extreme Scaling

- TPU v7 + Virgo Network: connect 134,000 TPUs into a single fabric within one data center
- Cross-datacenter: >1 million TPUs interconnected as a single training cluster
- Compared to NVIDIA: 134,000 TPUs vs NVIDIA's rack-level NVLink (72–144 GPUs per domain)

## TPU Variants

- **TPU 8t:** High-throughput AI training; ~3× higher compute than prior generation
- **TPU 8i:** Inference and reinforcement learning; ultra-low latency for agentic/MoE models
- **TPU v7:** Primary inferencing chip; 157 W vs ~700 W for B200 — 4.5× more power efficient per chip

## Cooling

- 9,216-chip Superpod is liquid-cooled
- Spans approximately 10 MW total power at pod scale
- Custom data center construction required; not deployable in standard air-cooled facilities

## Customer Commitments

- Anthropic: committed to deploying >1 million Ironwood TPU chips beginning 2026
- Google Cloud: GA availability Q4 2025 (limited preview); broader rollout 2026

## Strategic Implications

At 157 W per chip vs ~700 W for B200, TPU v7 represents a different design philosophy: high parallelism at lower per-chip power rather than high single-chip compute. This enables Google to build massive, power-efficient inference clusters. The 134,000-chip single-fabric capability exceeds any announced NVIDIA fabric size by approximately 100× in chip count within one datacenter.
