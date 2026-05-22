# Paper 003: AMD EPYC Turin 9005 Series — 192-Core Zen 5 Server Benchmark Review

**Source ID**: src-007, src-008, src-037  
**Date**: 2024-10-10 (launch) through 2025-03-15  
**Venue**: Tom's Hardware, Phoronix, AMD Corporate

---

## One-Sentence Claim
AMD EPYC Turin 9005 with up to 192 Zen 5/5c cores on TSMC 3nm delivers a generational server performance leap: ~17% IPC uplift, 2.7x speedup over Intel's flagship Xeon, and 1.8x performance per watt advantage over Intel Xeon 8592+.

## Methodology Summary
Third-party independent benchmarking by Tom's Hardware and Phoronix using standard HPC/enterprise suites (SPECrate2017_int, SPECrate2017_fp, STREAM, LINPACK, video transcoding, ML inference). AMD internal benchmarking using 24 HPC/ML workloads (1.369x geomean IPC uplift claim). Phoronix comparison against AmpereOne 192-core ARM server processor. Real server configurations with 2-socket setups.

## Quantitative Results
- **IPC uplift vs EPYC 9004 (Genoa/Zen 4)**: ~17% (enterprise workloads), 1.369x geomean on AMD's 24-workload ML/HPC suite
- **Max cores**: 192 Zen 5c per socket (EPYC 9965), 128 Zen 5 per socket (EPYC 9754)
- **Process node**: TSMC N3 (3nm) for Zen 5c; TSMC N4 for Zen 5 CCDs
- **Max TDP**: 500W (EPYC 9965)
- **Average power (real workloads)**: ~275W average, 461W peak on 9965
- **Power efficiency vs Genoa**: +55% performance at +32% power = significant perf/watt gain
- **vs Intel Xeon Platinum 8952+**: 2.7x faster (AMD claim), 40% faster per independent benchmarks
- **vs Intel Xeon 8592+**: 1.8x more integer performance per CPU watt (2P EPYC 9965 = 5.740 SPECrate2017_int_base/CPU W)
- **AES-XTS encryption (single-core)**: +35% vs Zen 4
- **ML single-core**: +32% vs Zen 4
- **Video transcoding**: 4x faster vs Intel flagship (AMD claim)
- **HPC applications**: 3.9x faster vs Intel flagship (AMD claim)
- **Virtualization perf/core**: 1.6x vs Intel flagship
- **L3 cache**: 384 MB total (Zen 5c EPYC 9965)
- **Memory**: DDR5, multi-channel SP5 socket

## Stated Limitations
- AMD performance claims vs Intel use best-case configurations and may not reflect all workloads
- 500W TDP creates cooling and power delivery challenges in existing data center deployments
- Zen 5c (dense core) achieves lower single-thread performance than full Zen 5 — workloads requiring high single-thread IPC benefit less from 192-core configs

## Inferred Limitations
- Performance advantage vs Intel Xeon partially reflects Intel Xeon's architectural stagnation; Diamond Rapids is expected to partially close the gap
- 3nm process (TSMC) used for Zen 5c means AMD is tapping TSMC's most advanced node while Intel struggles with 18A yields — unsustainable advantage if Intel ramps 18A successfully
- Thermal and power envelope limits practical deployment in certain existing data center configurations

## Architectural Significance
EPYC Turin reestablishes AMD's server CPU dominance established with EPYC Rome (7nm, 2019). The combination of 192 Zen 5c cores (using a smaller, denser variant of Zen 5 without sacrificing too much single-thread performance) on TSMC 3nm represents the most powerful x86 server CPU configuration ever shipped. The 17% IPC gain is significant for a mature architecture. Google Cloud deploying Turin as N4 instances confirms hyperscaler confidence. The Zen 5c dense core design is itself architecturally important: it shows AMD can deliver both high-single-thread (full Zen 5) and high-density (Zen 5c) from a common ISA, similar in philosophy to ARM's big.LITTLE but within the x86 ISA.

## Cross-Paper Connections
- **paper-001 (Zen 5 Hot Chips)**: EPYC Turin is the server deployment of the same Zen 5 architecture analyzed there
- **paper-021 (Intel Clearwater Forest)**: Intel's direct competitive response: 288 E-cores on 18A targeting the same scale-out server market
- **paper-023 (Threadripper PRO 9000)**: Same Zen 5 architecture in HEDT workstation form factor
- **paper-017 (Intel Diamond Rapids)**: Intel's future P-core server response to Turin's dominance

## Theme Tags
`zen-5`, `zen-5c`, `EPYC`, `server-CPU`, `chiplet-CPU`, `IPC-improvement`, `performance-per-watt`, `TSMC-3nm`, `data-center`, `AMD`
