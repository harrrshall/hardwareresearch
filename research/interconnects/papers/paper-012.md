# paper-012: Ultra Ethernet Consortium (UEC) 1.0 — AI-Native Ethernet Transport

**Tags:** chip-to-chip  
**Date:** 2025-06-11  
**Source:** Ultra Ethernet Consortium  
**URL:** https://ultraethernet.org/ultra-ethernet-consortium-uec-launches-specification-1-0-transforming-ethernet-for-ai-and-hpc-at-scale/

---

## Summary

The Ultra Ethernet Consortium released its UE 1.0 specification in June 2025, delivering a 560+ page comprehensive Ethernet networking stack engineered for AI and HPC workloads. UE 1.0 addresses the fundamental weaknesses of standard Ethernet (retransmission latency, congestion under all-to-all patterns) with a new transport protocol and hardware-accelerated flow control.

## Specification Overview

| Parameter | Value |
|---|---|
| Specification pages | 560+ |
| Release date | June 11, 2025 |
| Members | 100+ companies, 1,500+ participants |
| Target scale | Millions of endpoints |
| Physical layer | QSFP-DD and OSFP optics (800G+) |
| Transport | Ultra Ethernet Transport (UET) |

## Key Technical Components

### Ultra Ethernet Transport (UET)
- Purpose-built for AI training collective operations (AllReduce, AllGather, ReduceScatter)
- Native RDMA support at the data link layer
- Intelligent multi-path flow control to prevent congestion collapse
- Low-latency path selection across equal-cost multi-path (ECMP) topologies

### Physical Layer
- Standard QSFP-DD and OSFP form factors for 800G ports
- IEEE 802.3 compliance for physical medium
- 1.6T optics roadmap integration

### Management and Observability
- Open APIs for observability and automation
- Multi-vendor NIC/switch interoperability
- Hardware timestamping for congestion telemetry

## Hardware Availability

- UE hardware began shipping: **fall 2025**
- NICs and switches from initial vendors (Intel, Cisco, others)
- Full ecosystem interoperability testing ongoing

## UEC vs Alternative Scale-Up Fabrics

| Technology | Scale | Latency | Open? | Status |
|---|---|---|---|---|
| NVLink 5 (NVIDIA) | 576 GPUs | <1 µs | No | Production |
| UALink 200G 1.0 | 1,024 accel. | ~1 µs | Yes | 2026+ |
| UEC 1.0 | Millions | 1–3 µs | Yes | 2025 |
| InfiniBand XDR | 1000s | <1 µs | No | Production |

## ESUN — Ethernet for Scale-Up Networking (OCP 2025)

At OCP Summit October 2025, the Open Compute Project announced ESUN:
- Pushes Ethernet into the scale-up domain (traditionally NVLink/InfiniBand territory)
- Backed by: **AMD, Arista, ARM, Broadcom, Cisco, HPE, Marvell, Meta, Microsoft, NVIDIA, OpenAI, Oracle**
- Targets disaggregated AI accelerator pods using open Ethernet fabric

## Meta Non-Scheduled Fabric (NSF)

Meta introduced NSF architecture at OCP 2025:
- Shallow-buffer, disaggregated Ethernet switches
- Supports AI clusters up to **18,432 XPUs**
- Based on 2-stage Clos topology with Minipack3N (51 Tbps, Spectrum-4 ASIC)

## Strategic Observations

- UEC 1.0 represents the industry's strongest attempt to extend Ethernet into AI-native territory
- The overlap between UEC (scale-out) and ESUN/UALink (scale-up) reflects the blurring boundary between the two domains
- NVIDIA's participation in ESUN is notable: it signals NVLink may not remain the sole scale-up standard even in NVIDIA-dominated infrastructure
