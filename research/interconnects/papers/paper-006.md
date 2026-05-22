# paper-006: UALink 200G 1.0 — Open GPU Scale-Up Interconnect Standard

**Tags:** chip-to-chip  
**Date:** 2025-04  
**Source:** UALink Consortium  
**URL:** https://ualinkconsortium.org/wp-content/uploads/2025/04/UALink-1.0-White_Paper_FINAL.pdf

---

## Summary

The Ultra Accelerator Link (UALink) Consortium released the UALink 200G 1.0 specification in April 2025, establishing an open standard for scale-up interconnect between AI accelerators. UALink is positioned as a vendor-neutral alternative to NVIDIA's proprietary NVLink/NVSwitch ecosystem.

## Key Technical Specifications

| Parameter | Value |
|---|---|
| Maximum data rate | 200 GT/s per lane |
| Bandwidth (x4 config) | 800 Gbps |
| Pod scale | Up to 1,024 accelerators |
| Routing | 10-bit unique identifiers |
| Operations supported | Load/store across full pod |
| Topology | Switch-based fabric |

## Consortium Members

The UALink 1.0 specification was developed by 75 member companies with a board including:
**Alibaba, AMD, Apple, Astera Labs, AWS, Cisco, Google, HPE, Intel, Meta, Microsoft, Oracle, Synopsys**

This cross-industry coalition represents a direct challenge to NVIDIA's dominant NVLink ecosystem.

## Architecture

### Pod Model
- A UALink "Pod" contains up to **1,024 accelerators** interconnected through a fabric of UALink switches
- Each switch assigns one port per accelerator
- 10-bit unique identifiers enable precise routing across the full pod

### Software Model
- Simple load/store programming model — all accelerators in a pod share a unified address space
- No explicit message-passing required; hardware handles remote memory access with cache coherency

### Physical Layer
- Based on 200G PAM4 SerDes technology
- Leverages OIF CEI-224G electrical interface standards
- Designed for short-reach (XSR/USR) die-to-package and board-level connections

## Comparison to NVLink 5.0

| Parameter | NVLink 5.0 | UALink 1.0 |
|---|---|---|
| Per-GPU bandwidth | 1,800 GB/s | ~800 Gbps (x4) |
| Scale | 576 GPUs (NVSwitch) | 1,024 accelerators |
| Vendor support | NVIDIA only | AMD, Intel, Google, others |
| Availability | 2024–2025 | Late 2026 (Upscale AI) |
| Cost model | Proprietary | Open/royalty-free |

## Deployment Timeline

- Specification released April 2025
- First UALink silicon: **late 2026** (Upscale AI targeting Q4 2026 for scale-up switch)
- Meaningful production deployments: **2027**

## Strategic Observations

- UALink addresses the lock-in concern: enterprises running AMD, Intel, or custom accelerators want an open fabric
- The 1,024-accelerator pod scale exceeds NVSwitch's 576-GPU non-blocking domain
- At 200 GT/s per lane, UALink is behind NVLink 5.0 (effectively 200 GT/s per NVLink sub-link) but addresses different price/performance points
- The late 2026 silicon availability means NVLink 5.0 and the emerging NVLink 6.0 will have a 1–2 year head start in production
