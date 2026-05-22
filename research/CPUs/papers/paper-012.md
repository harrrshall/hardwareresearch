# Paper 012: IBM Power11 — Enterprise Processor Architecture and Hot Chips 2025 Presentation

**Source ID**: src-019, src-020  
**Date**: 2025-07-08 (launch) / 2025-08-28 (Hot Chips 2025)  
**Venue**: IBM Newsroom, ServeTheHome (Hot Chips 2025 analysis)

---

## One-Sentence Claim
IBM Power11 achieves 3x per-core performance over Power9 and 4x AI matrix operation throughput using Samsung 7nm with a stacked silicon interposer, custom DDIMM memory, and Spyre AI accelerator integration, targeting enterprise RAS with 99.9999% uptime.

## Methodology Summary
IBM official announcement (July 8, 2025) and Hot Chips 2025 presentation. ServeTheHome analysis of Power11 architecture details disclosed at the symposium. Performance comparisons against Power9 and Power10 using IBM's internal enterprise workloads. Independent analysis from SemiEngineering.

## Quantitative Results
- **Per-core performance vs Power9**: 3x
- **Per-thread performance vs Power10**: 2x
- **SIMD throughput vs Power10**: 2x per processor
- **AI matrix operation throughput vs Power10**: 4x
- **AI performance with Spyre integration**: up to 10x vs. prior generation
- **Cores per chip vs Power10**: up to 25% more per processor die
- **Process node**: Samsung 7nm (updated iteration) with silicon interposer stack
- **Memory architecture**: DDIMM (custom IBM) with OMI interface; up to 32 DDR5 ports supported
- **Reliability target**: 99.9999% uptime (~31.5 seconds downtime/year)
- **Availability**: GA July 25, 2025
- **Clock**: Higher than Power10 (specific GHz not disclosed in sources)

## Stated Limitations
IBM acknowledges staying on Samsung 7nm (not advancing to a newer node) was a deliberate client-driven decision — enterprise customers prioritize reliability and stability over process node novelty. This constrains raw performance vs. TSMC 3nm/4nm alternatives.

## Inferred Limitations
- Samsung 7nm competitive disadvantage: TSMC N3/N4 offers significantly better power efficiency and performance density; IBM's choice of Samsung 7nm limits theoretical peak performance vs. TSMC-fabbed competitors
- DDIMM memory is IBM proprietary — limits commodity memory compatibility and increases costs
- POWER ISA market share is declining; Power11 primarily serves IBM's existing mainframe/enterprise customer base rather than attracting new workloads
- The silicon interposer stacking adds manufacturing complexity and potentially limits scalability beyond Power11's configuration
- 10x AI gains with Spyre integration are dependent on Spyre accelerator availability and software stack maturity

## Architectural Significance
Power11 is significant as a demonstration that purpose-built enterprise architectures can achieve capabilities that commodity x86 cannot easily match. The 4x AI matrix throughput improvement (without a process node change) reflects microarchitectural investment in matrix math units — a design choice Intel AMD and ARM are also making (AMX, VNNI, SME). The OMI memory architecture supporting 32 DDR5 ports represents extraordinary memory bandwidth for database and analytics workloads. At 99.9999% uptime, Power11 targets mission-critical workloads where x86 servers with commodity ECC memory cannot compete. The Spyre AI accelerator integration shows IBM pursuing a CPU+accelerator integrated strategy rather than discrete GPU approaches. Presented at Hot Chips 2025 alongside Condor Cuzco (RISC-V) and Intel Clearwater Forest (x86), Power11 demonstrates that non-x86 architectures still innovate meaningfully in the enterprise tier.

## Cross-Paper Connections
- **paper-018 (Hot Chips 2025)**: Same venue; Power11 presented in the same CPU session alongside Condor Cuzco
- **paper-003 (EPYC Turin)**: x86 server competitor — contrasting approaches to enterprise workloads
- **paper-011 (Clearwater Forest)**: Intel server competitor with different core philosophy
- **paper-008 (Ventana Veyron V2)**: RISC-V server alternative in the same HPC/enterprise space

## Theme Tags
`IBM`, `Power11`, `POWER-ISA`, `enterprise-CPU`, `server-CPU`, `AI-matrix`, `reliability`, `Hot-Chips-2025`, `custom-memory`, `silicon-interposer`
