# paper-010: NVIDIA Vera Rubin Platform — NVLink 6.0 at 3.6 TB/s per GPU

**Tags:** NVLink, chip-to-chip  
**Date:** 2026-01  
**Source:** NVIDIA Newsroom / ServeTheHome / Tom's Hardware  
**URL:** https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/

---

## Summary

NVIDIA announced the Vera Rubin platform at CES 2026 in January, introducing NVLink 6.0 that doubles per-GPU bandwidth to 3.6 TB/s. The Vera Rubin NVL72 rack delivers 260 TB/s of aggregate bandwidth and is planned for H2 2026 production deployment with AWS, Google Cloud, Microsoft Azure, and Oracle Cloud.

## NVLink Generation Comparison

| Generation | Per-GPU BW | System | Year |
|---|---|---|---|
| NVLink 4.0 | 900 GB/s | H100/H200 NVL8 | 2023 |
| NVLink 5.0 | 1,800 GB/s | GB200/GB300 NVL72 | 2024–2025 |
| NVLink 6.0 | 3,600 GB/s | Rubin NVL72 | 2026 |

## Vera Rubin NVL72 Specifications

| Parameter | GB200 NVL72 | Vera Rubin NVL72 |
|---|---|---|
| GPU | Blackwell (B200) | Rubin (R100) |
| CPU | Grace | Vera |
| Process | TSMC 4nm | TSMC 3nm |
| Per-GPU BW | 1,800 GB/s | 3,600 GB/s |
| NVLink gen | 5 | 6 |
| Rack aggregate BW | 130 TB/s | 260 TB/s |
| HBM type | HBM3e | HBM4 |
| HBM capacity | 192 GB/GPU | 288 GB/GPU |
| HBM BW | ~8 TB/s | 13 TB/s |

## NVLink 6.0 Physical Layer

- **400 Gbps SerDes** per sub-link (2x vs NVLink 5's 200 Gbps)
- Required thermal management: NVLink 6.0 switch chips require **liquid cooling**
- 18 NVLink links per GPU × 200 GB/s per link bidirectional = 3,600 GB/s

## Rubin NVL144 (Extended Configuration)

- 144 GPUs per rack (double NVL72)
- 3.6 ExaFLOPS dense FP4 per rack
- Targets exascale in a single rack footprint

## Deployment Timeline

| Milestone | Date |
|---|---|
| CES 2026 announcement | January 2026 |
| Full production | In progress (announced) |
| Cloud provider launch | H2 2026 (AWS, GCP, Azure, OCI) |

## Strategic Observations

- NVIDIA maintains a 2:1 bandwidth lead over AMD IF4 in scale-up (3.6 TB/s vs 1.075 TB/s)
- NVLink 6 liquid-cooled switch requirement raises rack-level infrastructure requirements
- The 260 TB/s Rubin NVL72 rack aggregate exceeds the total bandwidth of many national research networks
- Rubin's HBM4 at 13 TB/s per GPU + NVLink 6 at 3.6 TB/s creates a 16.6 TB/s total memory+fabric bandwidth per GPU
