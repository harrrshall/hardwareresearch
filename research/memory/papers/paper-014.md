# Paper 014: Hot Chips 2025 — Memory as the Defining Constraint

**Source ID**: 31, 32  
**Source Title**: Marvell Shows Dense SRAM, Custom HBM, and CXL at Hot Chips 2025; Hot Chips 2025 Overview  
**URLs**:  
- https://www.servethehome.com/marvell-shows-dense-sram-custom-hbm-and-cxl-with-arm-compute-at-hot-chips-2025/  
- https://www.designnews.com/semiconductors-chips/hot-chips-2025-next-gen-processors-ai-chips-take-center-stage-at-stanford  
**Date**: 2025-08 (Hot Chips 2025, Stanford)  
**Tags**: Hot-Chips-2025, SRAM, HBM, CXL, Marvell, d-Matrix, memory-compute

---

## One-Sentence Claim
Hot Chips 2025 (August 2025, Stanford) established memory as the singular dominant design constraint for data center AI chips, with Marvell's session "Memory: (Almost) the Only Thing That Matters" and d-Matrix's compute-in-SRAM demonstration representing the conference's defining themes.

## Methodology Summary
Hot Chips 2025 featured presentations from IBM (Power11), NVIDIA (GB10 SoC), Marvell (custom HBM, CXL), and d-Matrix (compute-in-SRAM). The event surveyed the full AI chip ecosystem at Stanford. Marvell presented its approach to custom HBM integration with dense SRAM and CXL memory fabric solutions.

## Quantitative Results
- IBM Power11: 32 DDR ports of DDR5, 38.4 Gbps fabric, OMI D-DIMM custom form factor
- NVIDIA GB10 SoC: 256-bit L5X-9400 interface, ~301 GB/s memory bandwidth, 24 MB L2 cache
- d-Matrix: custom SRAM cells with compute woven inside, ultra-tight compute-SRAM integration
- Marvell: session title "Memory: (Almost) the Only Thing That Matters"

## Stated Limitations
- Conference presentations represent research and product previews, not shipping specifications
- Most bandwidth numbers are theoretical or peak; sustained efficiency in workloads is lower

## Inferred Limitations
- The theme convergence at Hot Chips 2025 reflects current industry consensus, but actual memory solutions are fragmented across HBM, DDR5, LPDDR6, CXL, and PIM — no single approach dominates
- "Compute-in-SRAM" (d-Matrix) competes with "Processing-in-DRAM" (SK Hynix/Samsung) for the same workload segment

## Architectural Significance
Hot Chips 2025 served as a snapshot of the industry's collective recognition that memory architecture — not compute throughput — is the binding constraint for AI systems. The presence of compute-in-SRAM (d-Matrix), custom HBM integration (Marvell), and CXL memory fabric all at the same conference signals a fragmented race to solve the memory wall through multiple parallel architectural approaches.

## Cross-Paper Connections
- NVIDIA GB10 at 301 GB/s contrasts with Vera Rubin's 22.2 TB/s (paper-007) — edge vs datacenter spectrum
- Marvell custom HBM work feeds into the HBM4 ecosystem (papers 001-003)
- d-Matrix compute-in-SRAM directly parallels the PIM work at Samsung/SK Hynix (paper-011)
- IBM Power11 DDR5 approach contrasts with the LPDDR6/SOCAMM2 direction (papers-004, 013)

## Theme Tags
Hot-Chips-2025, SRAM, HBM, CXL, Marvell, d-Matrix, IBM-Power11, NVIDIA-GB10, compute-in-memory
