# paper-025: Tenstorrent Wormhole and Blackhole — Open Dataflow Architecture

**Tags:** dataflow, transformer-accelerator, NPU  
**Date:** 2024–2025  
**Source:** SemiAnalysis, Tenstorrent Official, arXiv (Gravitational N-Body Study)  
**URL:** https://newsletter.semianalysis.com/p/tenstorrent-wormhole-analysis-a-scale

---

## Summary

Tenstorrent's Wormhole architecture (product since 2024) and the new Blackhole generation (taped out 2025) represent a RISC-V-powered open dataflow approach to AI acceleration. Founded by CPU architecture legend Jim Keller, Tenstorrent targets scale-out efficiency through Ethernet-native multi-chip design.

## Wormhole Architecture (n300s, 2024 Product)

### Core Design
- **Process:** GlobalFoundries 12nm
- **Tensix Cores:** 80 per chip (upgraded from Grayskull's 120 at 7nm)
- **Matrix Operations:** Each Tensix core has FPU matrix unit + vector unit + RISC-V control
- **SRAM per Core:** Larger than Grayskull, enabling more complex operations
- **Total Die:** 670mm²

### Memory
- **GDDR6:** 192-bit bus, 384 GB/s bandwidth (3x Grayskull)
- **On-chip SRAM:** Distributed across Tensix cores

### Networking (Key Differentiator)
- **16 ports** of 100 Gigabit Ethernet per chip
- **Total switching capacity:** 1.6 Tb/s networking
- **Scale-out approach:** Standard Ethernet for multi-chip connectivity (no proprietary NVLink equivalent)
- **Zero-overhead NOC extension:** Network-on-chip topology extends over Ethernet ports with zero software overhead

### Performance
- 2x Grayskull matrix operation performance
- 3x Grayskull memory bandwidth
- 150W TDP (same envelope as doubled performance)

## Grayskull vs Wormhole Comparison

| Feature | Grayskull | Wormhole |
|---------|-----------|----------|
| Process | GF 12nm | GF 12nm |
| Tensix Cores | 120 | 80 |
| Memory Bus | LPDDR4 8-ch | GDDR6 192-bit |
| Memory BW | 100 GB/s | 384 GB/s |
| Ethernet Ports | None | 16x 100GbE |
| TDP | 75W | 150W |

## Blackhole (2025 Tape-Out)

Details limited but key known specs:
- Taped out 2025 on TSMC process (upgrade from GlobalFoundries)
- Product availability targeted 2026
- Expanded Tensix core count
- Enhanced Ethernet connectivity
- Potential PCIe Gen 5 interface

## RISC-V Control Architecture

Each Tensix core contains embedded RISC-V processors for:
- Local data orchestration
- Conditional compute scheduling
- Kernel execution control

This allows the dataflow graph to be programmed with fine-grained control unavailable in purely static schedules.

## Scientific Computing Applications

A 2025 arXiv paper (2509.19294) demonstrated Wormhole accelerating gravitational N-body simulations — a non-AI workload. This illustrates the architecture's generality: the Ethernet-native scale-out design enables HPC workloads beyond ML inference, differentiating Tenstorrent from inference-only competitors.

## Competitive Position

- **vs NVIDIA:** Open ecosystem, standard Ethernet; disadvantage: smaller software ecosystem, lower absolute performance
- **vs Groq:** Supports training; Ethernet-native scale-out vs plesiosynchronous LPU protocol
- **vs Cerebras:** Distributed multi-chip vs monolithic wafer; more flexible deployment

## Significance

Tenstorrent represents the "open architecture" bet in AI acceleration. Standard Ethernet connectivity makes multi-chip clusters buildable without proprietary switch infrastructure. The RISC-V control cores provide a pathway for community-driven kernel development — analogous to how x86 and Arm created software ecosystems. If Blackhole can match performance efficiency of TSMC-fab competitors, the open ecosystem advantage may compound significantly post-2026.
