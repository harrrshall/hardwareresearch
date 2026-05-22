# Paper 019: AMD Zen 6 Architecture Confirmation — TSMC 2nm, 12 Cores/CCD, 2026 Launch

**Source ID**: src-038, src-052  
**Date**: 2025-11-01 to 2025-12-20  
**Venue**: PC Gamer, Overclock3D

---

## One-Sentence Claim
AMD has officially confirmed Zen 6 architecture for 2026 on TSMC 2nm, increasing CCD density to 12 cores (50% more than Zen 5), supporting DDR5-8000, and targeting 10–15% IPC improvement with new ISA extensions including AVX512_FP16.

## Methodology Summary
AMD official architectural disclosures at financial analyst day (November 2025) covered by PC Gamer, supplemented by leaked specification documents analyzed by Overclock3D (December 2025). AMD confirmed Zen 6 and Zen 6c core variants, 'Medusa' desktop platform, and 'Venice' EPYC server platform. Some details (IPC improvement percentage, exact CCD core count) are from credible leaks cross-referenced with AMD patents and roadmap patterns.

## Quantitative Results
- **Cores per CCD**: 12 (up from 8 in Zen 4/5 — 50% increase)
- **Max desktop cores**: 24 (2 CCDs × 12 cores)
- **Process node**: TSMC 2nm (N2) — AMD's first 2nm processor
- **IPC improvement vs Zen 5**: 10–15% (leaked; AMD confirmed "significant improvement")
- **Max memory speed**: DDR5-8000 (up from DDR5-6000 on Zen 4/5 platforms)
- **New ISA extensions**: AVX512_BMM, AVX_NE_CONVERT, AVX_IFMA, AVX_VNNI_INT8, AVX512_FP16
- **Desktop codename**: 'Medusa' (Ryzen 10000 series)
- **Server codename**: 'Venice' (EPYC 10005?)
- **APU codename**: TBD (Medusa APU with RDNA GPU)
- **TSMC N2 volume production**: Q4 2025 (providing AMD first-mover advantage)
- **Expected launch**: H2 2026 (desktop); potential slip to early 2027 for some SKUs

## Stated Limitations
IPC improvement figures are from leaked sources, not official AMD disclosure. The 10-15% range is based on AMD's historical improvement trajectory and architectural changes described — not independently benchmarked. Some desktop SKUs may slip to 2027.

## Inferred Limitations
- TSMC 2nm early production may face yield challenges analogous to N3's early 2023 period — AMD's first 2nm products may be supply-constrained
- 12 cores/CCD requires significant re-engineering of the cache hierarchy; L3 cache per CCD must scale proportionally or per-core cache shrinks
- DDR5-8000 benefits may only materialize for bandwidth-bound workloads; typical consumer gaming and productivity already saturate DDR5-6000
- AVX512_FP16 and new AI extensions require recompiled software to benefit; performance gains for existing binaries limited to IPC improvement
- With Zen 6 delayed to potentially 2027 for some SKUs, AMD faces a window where Intel Nova Lake (18A, Coyote Cove) could recapture desktop mindshare

## Architectural Significance
Zen 6's jump from 8 to 12 cores per CCD is AMD's most radical density increase since Zen 2 (which doubled cores from 4 to 8 vs Zen 1). Combined with TSMC 2nm's 15% performance / 25-30% power improvement over N3E, Zen 6 could deliver the most significant generational performance leap since Zen 3 (2020). The introduction of AVX512_FP16 is a direct response to AI/ML workload requirements — enabling consumer Ryzen CPUs to accelerate bfloat16 inference without a discrete GPU. DDR5-8000 support enables Zen 6 to saturate server memory bandwidth requirements for in-memory databases. If AMD succeeds in shipping Zen 6 in H2 2026 before Intel Nova Lake achieves volume, AMD will have maintained architectural momentum for the full decade of the 2020s.

## Cross-Paper Connections
- **paper-001 (Zen 5 architecture)**: The predecessor that Zen 6 builds upon and surpasses
- **paper-003 (EPYC Turin)**: Zen 5c server deployment; Zen 6 'Venice' will be the next server generation
- **paper-015 (Nova Lake)**: Intel's direct temporal competitor — both targeting H2 2026
- **paper-036 (TSMC N2)**: The process node technology that enables Zen 6's density and efficiency improvements

## Theme Tags
`AMD`, `Zen-6`, `TSMC-2nm`, `IPC-improvement`, `AVX512`, `DDR5-8000`, `desktop-CPU`, `server-CPU`, `roadmap`
