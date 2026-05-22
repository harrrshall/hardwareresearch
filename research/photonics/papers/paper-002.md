# Paper 002: Broadcom Tomahawk 6 Davisson — First 102.4 Tbps CPO Ethernet Switch

**Tags:** co-packaged-optics, silicon-photonics  
**Date:** October 8, 2025  
**Source:** Broadcom Investor Relations / GlobeNewswire  
**URL:** https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-tomahawkr-6-davisson-industrys-first-1024

## Summary

Broadcom announced the Tomahawk 6 "Davisson" (TH6), the industry's first 102.4 Tbps Ethernet switch with co-packaged optics. TH6 represents the third generation of Broadcom's CPO Ethernet switch platform and doubles bandwidth vs previous generation.

## Key Technical Specifications

- **Switch capacity:** 102.4 Tbps (bidirectional)
- **CPO technology:** TSMC Compact Universal Photonic Engine (COUPE™)
- **Packaging:** Advanced substrate-level multi-chip packaging (SoIC-X stacking)
- **Power reduction:** 70% vs traditional pluggable solutions
- **Bandwidth progression:** 25.6T → 51.2T (TH5 CPO) → 102.4T (TH6)
- **Optical engine:** Electrical IC stacked on photonic die via SoIC-X
- **Roadmap:** Supports future 800G, 1.6T, beyond upgrades

## Architecture Notes

TH6-Davisson uses TSMC COUPE to integrate the switch ASIC with optical engines on a common substrate. Electrical-to-optical conversion occurs within millimeters of the ASIC, eliminating the need for high-power SerDes over PCB traces. The SoIC-X bonding gives lowest impedance at die-to-die interface.

## Manufacturing

Manufactured using TSMC COUPE packaging. Broadcom began mass shipments in October 2025.

## Market Impact

- First 100+ Tbps CPO product commercially shipping
- Sets CPO performance benchmark for hyperscaler AI fabric designs
- NVIDIA $4B investment in optical component suppliers (Lumentum, Coherent) followed this product launch

## Comparison to Previous Generation

| Platform | Capacity | Power Savings |
|----------|---------|---------------|
| TH5 CPO (Jericho) | 51.2 Tbps | ~40% |
| TH6 Davisson | 102.4 Tbps | 70% |
