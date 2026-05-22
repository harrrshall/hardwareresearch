# paper-007: AMD MI300X Packaging — 3.5D Chiplet Co-Optimization with SoIC and Interposers

**Tags:** chiplet, AMD, 3D-stacking, interposer, SoIC, heterogeneous-integration
**Date Range:** 2025-Q1 – 2025-Q4
**Source IDs:** 55

---

## Summary

The AMD Instinct MI300X/MI300A represents the most complex commercially shipped 3D chiplet package as of 2025. It employs TSMC's SoIC hybrid bonding (3D vertical) combined with a silicon interposer (2.5D horizontal), combining for what AMD calls "3.5D packaging." The design stacks 5nm compute dies atop 6nm IO dies, with eight HBM3 stacks on the same interposer.

## Technical Details

**Chiplet Configuration (MI300X):**
- 8× GPU XCD (Compute Complex Die) — TSMC N5 (5nm)
- 4× IO Die (IOD) — TSMC N6 (6nm)
- 8× HBM3 stacks (2.5D on interposer)
- Total: 12 chiplets + 8 HBM stacks
- TSV pitch (SoIC): 9 μm
- XCD-on-IOD stacking: face-to-back SoIC hybrid bonding

**MI300A (CPU+GPU APU):**
- 3× CPU CCD (Zen 4, N5) + 6× GPU XCD (N5) + 4× IOD (N6)
- Total: 13 chiplets
- First commercial CPU+GPU 3D-stacked product in HPC

**Package Architecture:**
- 2.5D silicon interposer: ~850 mm² active area
- Interposer micro-bump pitch: ~55 μm (IOD-to-interposer)
- HBM3 connection through interposer TSVs
- Total package I/O: >5 TB/s peak memory bandwidth (HBM3 8-stack)

**Packaging Paper at ECTC 2025:**
- Architecture-packaging co-optimization presented: die-level power density management across heterogeneous nodes
- Thermal resistance of full stack: ~0.04°C/W per tile
- Yield improvement via known-good die (KGD) testing at each stacking step

## Key Findings

1. The 9 μm TSV pitch SoIC bonding achieved interconnect density 100x greater than comparable micro-bump options.
2. MI300X uses the 2.5D silicon interposer to route HBM3 signals — SoIC only handles vertical XCD-on-IOD stacking.
3. Known-good die (KGD) sorting at N5 and N6 steps was essential to maintain yield on 12-chiplet assemblies.
4. AMD demonstrated >5 TB/s HBM3 aggregate bandwidth, validated in production AI deployments.
5. The ECTC 2025 paper highlighted that power delivery to 5nm dies through the 6nm IOD substrate required novel IR-drop mitigation techniques.

## Implications

MI300X proved that 3.5D packaging (combined SoIC + 2.5D interposer) is viable in high-volume production. The approach enables disaggregation: logic, memory controllers, and cache are on optimally chosen process nodes, with 3D stacking providing near-monolithic interconnect density. This architecture will likely define HPC accelerator packaging for the next 3–5 years.
