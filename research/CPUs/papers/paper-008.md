# Paper 008: Ventana Veyron V2 and Qualcomm Acquisition — RISC-V Enters Server Market

**Source ID**: src-014, src-015, src-051  
**Date**: 2025-03-15 (Veyron V2 announcement) / 2025-12-10 (Qualcomm acquisition)  
**Venue**: RISC-V International, The Register, The Chip Letter

---

## One-Sentence Claim
Ventana's Veyron V2 RISC-V processor achieves 3.85 GHz with RVA23 compliance and a modular UCIe chiplet architecture targeting 192-core server configurations competitive with AMD EPYC Bergamo, and Qualcomm's $2.4B acquisition signals RISC-V's entry into the mainstream server market.

## Methodology Summary
Ventana engineering disclosure at RISC-V International. Independent analysis by The Chip Letter of architectural implications. Performance projections on SpecInt2017 comparing 192-core V2-based server vs. AMD EPYC Bergamo and Intel Xeon Sapphire Rapids. The Qualcomm acquisition was covered by The Register and multiple industry outlets on December 10, 2025.

## Quantitative Results
- **Clock speed**: up to 3.85 GHz per core
- **Cores per chiplet**: up to 32
- **L2 cache per core**: 1.5 MB
- **Shared L3**: 128 MB per chiplet
- **Vector unit**: 512-bit RVV 1.0 per core
- **AI/ML throughput**: 0.5 TOPS per GHz per core (INT8)
- **Matrix accelerator**: Custom unit for ML workloads
- **Max cores per system**: 192 (6 chiplets) using UCIe interconnect
- **SpecInt2017 projection**: Expected to outperform EPYC Bergamo and Xeon Sapphire Rapids in 192-core server config
- **Acquisition price**: $2.4 billion (Qualcomm acquires Ventana, Dec 2025)
- **V3 roadmap**: >4.2 GHz clock, FP8 support, expected late 2026/early 2027

## Stated Limitations
Ventana's SpecInt2017 projection for 192-core configuration is a projected claim, not yet validated by independent third-party benchmarking of actual silicon in a 192-core configuration.

## Inferred Limitations
- RVA23 software stack (Linux distributions, compilers, middleware) less mature than x86 or ARM for enterprise workloads
- Qualcomm acquisition creates integration uncertainty — Ventana's independent roadmap may be subsumed into Qualcomm's server strategy priorities
- UCIe chiplet scaling to 192 cores requires robust inter-chiplet communication latency management; memory access patterns in server workloads can expose UCIe latency penalties
- The matrix math accelerator's 0.5 TOPS/GHz/core is lower than dedicated AI accelerators; competitive for inference-at-scale but not for training

## Architectural Significance
The Veyron V2 demonstrates that RISC-V has crossed the threshold from embedded/IoT applications to serious server contention. Three features drive this: (1) 512-bit RISC-V V-extension vector units, (2) UCIe-based chiplet scaling to 192+ cores, and (3) RVA23 profile compliance enabling standard Linux workloads without ISA-specific recompilation. Qualcomm's $2.4 billion acquisition is the strongest industry signal yet that RISC-V server IP is valued on par with ARM server IP. By integrating Ventana's expertise into its Oryon CPU lineage, Qualcomm acquires the ability to build future server CPUs without ARM licensing fees — a fundamental strategic shift. The Veyron V3 roadmap (>4.2 GHz, FP8) suggests RISC-V server performance will continue improving into 2027.

## Cross-Paper Connections
- **paper-006 (Cuzco)**: Smaller-team RISC-V design targeting similar datacenter use case
- **paper-007 (SiFive P570)**: Lower-tier RISC-V IP showing the breadth of the RISC-V ecosystem
- **paper-016 (RISC-V market)**: Market context for Ventana/Qualcomm deal significance
- **paper-013 (UCIe 3.0)**: The chiplet interconnect standard that enables Ventana's scalable architecture
- **paper-019 (Snapdragon X2)**: Qualcomm's existing CPU franchise that Ventana RISC-V may eventually integrate with

## Theme Tags
`RISC-V`, `Ventana`, `Veyron-V2`, `chiplet-CPU`, `UCIe`, `server-CPU`, `vector-ISA`, `RVA23`, `Qualcomm`, `acquisition`
