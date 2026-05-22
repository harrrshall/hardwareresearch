# Paper 004: NVIDIA Vera Rubin NVL144 Platform — Next-Generation Rack Architecture

**Tags:** rack-scale, liquid-cooling, AI-cluster
**Source:** Tom's Hardware, The Register, ServeTheHome, NVIDIA Newsroom
**Date:** Jan 2026 (CES announcement), delivery late 2026
**Relevance:** High

## Platform Overview

NVIDIA unveiled the Vera Rubin platform at CES 2026 (January 5–6, 2026), representing the next generation after Blackwell. The NVL144 is the rack-scale product, shipping in late 2026.

## GPU Architecture

- **Rubin GPU:** 336 billion transistors; dual-die design
- **Process node:** TSMC N3 (3nm)
- **NVLink 6.0:** ~3.6 TB/s total bidirectional per GPU (1.8 TB/s per direction)
- **NVSwitch 6.0:** ~28.8 TB/s aggregate GPU-to-GPU bandwidth in NVL144 fabric

## System Configuration

- **GPUs:** 144 Rubin GPUs (in 72 dual-GPU packages)
- **CPUs:** 36 Vera CPUs
- **HBM4 memory:** 20,736 GB (20.7 TB) — 1.5× NVL72
- **HBM4 bandwidth:** 1.6 PB/s — 2.8× NVL72
- **LPDDR5X (CPU):** 54 TB total — 2.5× NVL72

## Performance

- **FP4 inference:** 3.6 ExaFLOPS — 2.5× NVL72
- **FP8 training:** 1.2 ExaFLOPS — 1.67× NVL72
- **3.3× improvement** over Blackwell Ultra NVL144 configuration

## Power and Physical

- **Rack TDP:** approximately 120–130 kW (similar to NVL72, despite more GPUs due to process efficiency)
- **Assembly time:** Reduced from 100 minutes (Blackwell) to 6 minutes (Rubin) via improved modular design

## New Additions: Rubin CPX

- Rubin CPX is a dedicated inference GPU variant targeting 1M+ token context workloads
- Optimized for large context windows in agentic AI
- Available end 2026

## Infrastructure Implications

- Same approximate power envelope as NVL72 at 120–130 kW — existing liquid-cooled infrastructure is compatible
- NVLink 6.0 doubles per-link throughput; requires updated NVSwitch 6.0 (not backward compatible at max bandwidth)
- HBM4 vs HBM3e: higher bandwidth but similar power draw due to improved memory process efficiency

## Strategic Significance

The Vera Rubin NVL144 is the first rack that natively scales to 144 GPUs in a single NVLink domain. This eliminates the need for the 8-rack NVL576 multi-rack NVLink extension required in Blackwell for >72 GPU coherent domains.
