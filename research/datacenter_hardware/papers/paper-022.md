# Paper 022: NVLink 5 and NVSwitch Architecture — Blackwell GPU Interconnect (2025)

**Tags:** AI-cluster, rack-scale
**Source:** NVIDIA official documentation, Introl Blog, Nebius, AMAX
**Date:** 2025
**Relevance:** High

## NVLink 5 Technical Specifications

Fifth-generation NVLink (NVLink 5) ships with NVIDIA Blackwell GPUs in the GB200 NVL72 platform.

| Parameter | NVLink 5 (Blackwell) | NVLink 4 (Hopper) |
|-----------|---------------------|-------------------|
| Links per GPU | 18 | 18 |
| Per-link bandwidth | 100 GB/s | 50 GB/s |
| Per-GPU bandwidth | 1.8 TB/s bidirectional | 900 GB/s bidirectional |
| Generation improvement | 2× | — |
| PCIe Gen5 comparison | 14× higher bandwidth | — |

## NVSwitch 3.0 (Blackwell)

Each GB200 NVL72 rack contains 9 NVLink Switch trays (3 NVSwitches per tray = 9 total NVSwitch chips).

| Parameter | NVSwitch 3.0 |
|-----------|-------------|
| NVLink ports per switch | 144 |
| Non-blocking switching bandwidth | 14.4 TB/s |
| Total 72-GPU fabric bandwidth | 130 TB/s |

## NVLink Domain Scaling

| Scale | Configuration | Bandwidth |
|-------|--------------|-----------|
| Single rack (NVL72) | 72 GPUs, 9 NVSwitches | 130 TB/s aggregate |
| Multi-rack (NVL576) | 576 GPUs, 8 racks + NVLink trunk | ~1 PB/s total |

## NVLink 6.0 (Vera Rubin, 2026)

| Parameter | NVLink 6.0 | NVLink 5 |
|-----------|-----------|---------|
| Per-link bandwidth | 200 GB/s | 100 GB/s |
| Per-GPU bandwidth | ~3.6 TB/s | 1.8 TB/s |
| NVLink domain in NVL144 | 144 GPUs | 72 GPUs |
| Total fabric bandwidth | ~28.8 TB/s per rack | 130 TB/s per rack |

Wait — the 28.8 TB/s in NVL144 (144 GPUs) with NVLink 6 vs 130 TB/s in NVL72 (72 GPUs) with NVLink 5 reflects architectural choices: the NVL144 uses fewer NVSwitch chips per GPU with higher per-link bandwidth, trading some all-reduce efficiency for simpler rack construction (6-minute assembly vs 100 minutes in Blackwell).

## Two-Die GB200 Chip Architecture

- GB200 superchip: 2 Blackwell dies + 1 Grace CPU die
- Die-to-die chip interconnect: ~10 TB/s throughput
- Enables the 2 B200 GPU dies to appear as a single GPU to software

## Programming Model

- NVLink enables Unified Virtual Memory (UVM) across all 72 GPUs in the NVL72 domain
- Applications can address all 13.4 TB of GPU memory as a flat address space
- CUDA peer access uses NVLink, not PCIe, for intra-domain transfers
- NCCL (NVIDIA Collective Communications Library) is optimized for NVLink topology

## Competitive Context

| System | GPU-GPU BW | Scope |
|--------|-----------|-------|
| GB200 NVL72 NVLink 5 | 130 TB/s | 72 GPUs |
| Rubin NVL144 NVLink 6 | ~28.8 TB/s | 144 GPUs |
| Google TPU v7 ICI | 9.6 Tb/s per chip × 9,216 | 9,216 chips |
| AWS NeuronLink | Not publicly specified | 64 chips per UltraServer |

Note: TPU v7 ICI and NVLink are not directly comparable — ICI is a die-to-die optical mesh across thousands of chips; NVLink is a Cu electrical interconnect optimized for dense small-domain all-to-all bandwidth.
