# Paper 001: AMD Zen 5 Architecture — Hot Chips 2024 Deep Dive

**Source ID**: src-041  
**Date**: 2024-08-25  
**Venue**: Hot Chips 2024 (Peer-Reviewed Symposium)

---

## One-Sentence Claim
AMD Zen 5 is the first microarchitecture to fully implement two-ahead branch prediction and delivers a ~16% IPC uplift over Zen 4 through a combination of wider front-end, 8-wide execution, 6 ALUs, and doubled data bandwidth.

## Methodology Summary
AMD internal architectural simulation and silicon measurement at fixed-frequency conditions comparing Zen 5 (TSMC N4P) vs. Zen 4 (TSMC N5). IPC measured across industry-standard benchmark suites including SPEC CPU2017, AI/ML kernels, and internal microarchitectural stress tests. Presented at Hot Chips 2024, a peer-reviewed academic symposium.

## Quantitative Results
- **Average IPC uplift**: +16% over Zen 4 (geomean across workloads)
- **Execution/retire width**: 8-wide (up from 6-wide in Zen 4) — contributes 34% of total IPC gain
- **ALU count**: 6 (up from 4) 
- **Front-end instruction bandwidth**: 2x improvement — contributes 27% of IPC gain
- **Data bandwidth (L2→L1 and L1→FP)**: 2x improvement — contributes 27% of IPC gain
- **Branch prediction improvement**: contributes 12% of IPC gain
- **Two-ahead prediction**: first microarchitecture to predict up to 2 branches per clock cycle
- **BTB**: 24K entries (large decoupled predictor)
- **L1i**: 32 KB with 6K-entry op cache
- **AVX-512 throughput**: 2x improvement
- **AI throughput**: 2x improvement

## Stated Limitations
- Fixed-frequency IPC measurements may not reflect realistic workload performance with dynamic DVFS
- Gaming workloads show lower-than-average IPC gains due to clustered decoder behavior in low-IPC code

## Inferred Limitations
- The clustered decoder architecture, while beneficial for high-IPC workloads, creates uneven gains across workload types — games and integer-heavy code benefit less than expected
- N4P process node (not yet N3) limits achievable clock speeds compared to TSMC N3
- Two-ahead branch prediction adds circuit complexity and latency; benefits depend heavily on code structure

## Architectural Significance
The Zen 5 two-ahead branch prediction is a landmark innovation: no prior production microarchitecture had achieved this. Combined with 8-wide execution (the widest in AMD's history), Zen 5 represents a fundamental increase in the instruction-level parallelism budget AMD is willing to budget silicon for. The 6-ALU configuration challenges Intel's own ALU counts in Lion Cove. This is the largest single-generation IPC jump AMD has delivered since Zen 2.

## Cross-Paper Connections
- **paper-002 (Chips and Cheese Zen 5)**: Independent third-party confirmation of 6K op cache, 24K BTB, and clustered decoder behavior
- **paper-007 (EPYC Turin)**: Zen 5 architecture deployed at server scale with 192 Zen 5c cores
- **paper-003 (Zen 5 gaming analysis)**: Explains why gaming IPC gains are below average due to clustered decoder
- **paper-023 (AMD Threadripper PRO 9000)**: Same architecture extended to workstation with 96 cores

## Theme Tags
`zen-5`, `out-of-order`, `branch-prediction`, `two-ahead-prediction`, `IPC-improvement`, `ALU-width`, `front-end`, `AVX-512`, `heterogeneous-cores`, `AMD`
