# Paper 001: Direct-to-Chip Liquid Cooling for AI Servers — State of Play 2025

**Tags:** liquid-cooling, direct-to-chip, thermal-management
**Source:** Tom's Hardware / Schneider Electric (blog.se.com)
**Date:** Jan–Mar 2026
**Relevance:** High

## Summary

Direct-to-chip (D2C) liquid cooling has transitioned from an optional upgrade to the dominant thermal solution for AI data centers. Goldman Sachs projects that liquid-cooled AI servers will increase from 15% penetration in 2024 to 54% by end-2025, rising further to 76% in 2026. D2C commands a 47% share of all liquid cooling deployments.

## Key Technical Findings

- D2C cold plates remove heat directly from GPU/CPU die surfaces via micro-channel or pin-fin structures, achieving thermal resistance below 0.02°C/W
- CoolIT demonstrated a single-phase split-flow D2C coldplate handling ~200 W/cm² heat flux, cooling up to 4,000 W per device
- Accelsius two-phase D2C cooling achieves 300 W/cm² heat flux — critical for next-generation devices
- Single-phase D2C begins to reach practical limits at ~1,500 W TDP; emerging two-phase variants extend ceiling beyond 2,000 W
- A hybrid approach (70% liquid, 30% residual air) is typical in 2025 rack deployments

## Market Events 2025–2026

- Microsoft mandated D2C liquid cooling for all new Azure AI server deployments as of February 2025
- Microsoft began fleet deployment across Azure campuses in July 2025
- Equinix launched AI Powerhouse initiative in Ashburn VA with Vertiv partnership (April 2025)
- HPE expanded Coolit Systems alliance for Cray portfolio pre-installed D2C (March 2025)
- In 2026, D2C accounts for approximately 65–70% of the liquid cooling market

## Infrastructure Requirements

- A GB200 NVL72 rack at 120 kW requires CDU capacity of 150–200 kW (10–15% headroom)
- Coolant supply temperature maintained within 25–45°C depending on platform
- Quick-disconnect manifolds (Universal Quick Disconnect / OCP UQD standard) enable hot-swap server service
- Row-level CDU feeds multiple racks; rack-level CDU is used for isolated high-density deployments

## Implications

D2C is the baseline for new AI data center builds. Operators who do not have chilled water infrastructure face major retrofits. Certified supplier pool remains small, creating supply-chain risk during rapid adoption.
