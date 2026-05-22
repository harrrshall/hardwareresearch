# Paper 014: Silicon Photonics and Co-Packaged Optics for AI Data Centers (2025–2026)

**Tags:** AI-cluster, network-topology, power-delivery
**Source:** Yole Développement, NVIDIA Technical Blog, Tom's Hardware, ADTEK
**Date:** 2025–2026
**Relevance:** High

## Technology Overview

Co-Packaged Optics (CPO) integrates optical transceiver components directly with switch ASICs or GPU packages, eliminating pluggable optics modules and their associated PCB trace losses. This enables higher bandwidth at lower power per bit.

## Market Trajectory

| Year | 800G+ Transceiver Shipments | CPO Market Size |
|------|---------------------------|----------------|
| 2025 | 24 million units | $95 million |
| 2026 | ~63 million units (projected) | ~$150 million |
| 2034 | — | >$1.05 billion (CAGR 30.6%) |

Optical interconnect market (AI data centers total): $3.75 billion in 2025, projected $18.36 billion by 2033.

## NVIDIA's Co-Packaged Optics Roadmap

- NVIDIA outlined CPO plans for GPU communication "by 2026" at GTC 2025
- CPO-based systems targeting 409.6 Tb/s bandwidth with 512 ports at 800 Gb/s
- Silicon photonics integration within GPU packages for Rubin+ generation
- NVIDIA's photonic platform: "Quantum-X" photonics for switch-to-switch links

## 800G Optical Deployment (2025)

- NVIDIA Quantum-X800 InfiniBand: 800 Gb/s per port, 144 ports — ships 2025
- 200G/channel QSFP-DD becomes mainstream in 2026
- 800G transceivers: 4×200G lanes using 100G PAM4 signaling
- Leading manufacturers: AOI, Coherent, Lumentum, Inphi (Marvell)

## Power Efficiency Impact

- Pluggable 800G QSFP-DD optic: ~12–15 W per module
- CPO equivalent: projected 3–5 W per 800G port (4× improvement)
- For a 100-rack cluster with 6,400+ optical ports: CPO saves ~50–75 kW of optics power

## Large-Scale CPO Deployments

- Full hyperscale CPO: projected 2028–2030 for large-scale deployment
- 2026: NVIDIA commercial availability of CPO switch products
- Industry names committed to CPO: NVIDIA, Broadcom, Marvell, Intel, Cisco, Google, Microsoft, Amazon, Fujitsu, NTT

## Infrastructure Implications

The move from pluggable to CPO represents a significant servicing model change:
- Pluggable optics: field-replaceable in minutes
- CPO: optics integrated into switch ASIC — requires ASIC board replacement for optics failure
- This trades serviceability for power efficiency and density

## Data Rate Evolution

| Year | Dominant Per-Port Speed | Primary Technology |
|------|------------------------|-------------------|
| 2024 | 400G | NDR InfiniBand / 400G Ethernet |
| 2025 | 800G | XDR InfiniBand / 800G Ethernet |
| 2027 | 1.6T | Next-gen with CPO |
| 2029+ | 3.2T | Full silicon photonics integration |
