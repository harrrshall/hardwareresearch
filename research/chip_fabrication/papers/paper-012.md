# Paper 012: HBM4 JEDEC Standard and 3D Stacking Architecture for AI Memory

**Source ID:** 36, 37  
**Authors:** JEDEC / SK Hynix / Samsung Memory  
**Venue:** JEDEC Standard JESD270-4 / SC25 Supercomputing Conference 2025  
**Date:** April 2025 / December 2025  
**Tags:** 2nm, nanosheet (logic base die on advanced nodes)  
**URL:** https://www.oscoo.com/news/hbm4-the-memory-revolution-in-the-age-of-ai-computing/

## Abstract / Summary

JEDEC released the HBM4 standard (JESD270-4) in April 2025, defining the sixth generation of High Bandwidth Memory. HBM4 introduces a "logic base die" architecture where the bottom layer of the memory stack is fabricated on an advanced logic process node (e.g., TSMC N3 or N2), enabling customization and integration of logic functions directly within the memory stack. SK Hynix and Samsung both demonstrated 12-Hi HBM4 pilot runs by late 2025.

## Key Technical Data

- **Standard:** JEDEC JESD270-4, released April 2025
- **Stack height:** 12-Hi (pilot, 2025); 16-Hi (target, mid-2026)
- **Bandwidth per stack:** >2.0 TB/s; up to 3.3 TB/s in advanced configurations
- **Capacity per stack:** Up to 64 GB via 16-Hi with 32 Gb layers
- **I/O speed:** ~11.7 Gbps per pin
- **Logic base die:** Bottom layer on advanced logic process (N3-class); enables custom DRAM controller, PHY, power management
- **Interconnect:** Through-Silicon Via (TSV) density 1000+ per mm² for 16-Hi stacks
- **Bonding technology:** Advanced MR-MUF (Mass Reflow Molded Underfill) for 16-Hi
- **Thermal challenge:** 16-Hi stack dissipates >15W/stack requiring active cooling management

## Key Findings

1. HBM4's logic base die fundamentally changes the memory-logic boundary: foundry-made logic cells (at N3/N2-class) are embedded in the memory package.
2. 16-Hi stacking requires novel bonding technologies (MR-MUF) to maintain yield across 16 die-to-die bonds.
3. Samsung and SK Hynix both achieved 12-Hi pilot runs by late 2025, suggesting competitive parallel development.
4. HBM4 bandwidth (3.3 TB/s) combined with TSMC CoWoS-L packaging enables >100 TB/s aggregate bandwidth in next-gen GPU packages.
5. The logic base die creates a new foundry revenue stream — TSMC and Samsung foundry both benefit from memory customers' logic base dies.

## Relevance to Research Window (2025-11-22 to 2026-05-22)

SK Hynix presented HBM4 at Supercomputing 2025 (SC25, November 2025). Both SK Hynix and Samsung are actively ramping 12-Hi HBM4 production during the research window for 2026 AI platform integration.
