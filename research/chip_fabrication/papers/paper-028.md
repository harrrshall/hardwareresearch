# paper-028 — Apple Explores Intel and Samsung as TSMC Foundry Alternatives

**Status: VALIDATED**
**Source ID:** 64
**Venue:** Bloomberg (May 5, 2026) / 9to5Mac (May 4, 2026) / Tom's Hardware (May 5, 2026)
**Date:** 2026-05-05
**URL:** https://9to5mac.com/2026/05/04/report-apple-considers-intel-and-samsung-to-diversify-chip-manufacturing-away-from-tsmc/
**Tier:** 3 (Bloomberg as primary; corroborated by 9to5Mac, Tom's Hardware, AppleInsider, Dataconomy — minimum 5 independent sources)

---

## One-sentence claim
Apple held early-stage discussions with Intel about using its 18A/14A foundry and sent executives to visit Samsung's Texas facility as it explored diversifying chip manufacturing away from TSMC — a strategic shift that, if realized in 2027-2028, could free significant TSMC N2 capacity for AI chip customers while validating Intel Foundry Services as a credible Tier-1 foundry.

## Methodology summary
Bloomberg (primary, May 5, 2026) — one of the most reliable sources for Apple supply-chain intelligence. Corroborated by 9to5Mac (citing Bloomberg), Tom's Hardware, AppleInsider, Dataconomy, MWM, and Winbuzzer. Digitimes (May 12, 2026) added context on implications for Samsung Foundry. No source denies the exploration; the uncertainty is scope and timeline.

## Quantitative results
- Apple accounts for >50% of TSMC's initial N2 (2nm) capacity in 2026 (chip_fabrication paper-009, TSMC 2025 annual report)
- Intel 18A: reportedly approaching ~62-65% yield as of early 2026 (chip_fabrication paper-015)
- Samsung Texas (Taylor, TX) facility: advanced node plant expected to produce chips using SF4X/SF2 class processes
- Analyst estimate: Intel could begin Apple processor production for lower-end devices as early as 2027-2028
- No contracts signed; no orders placed as of May 5, 2026

## Stated limitations
- "Early-stage discussions" — no commitment
- Scope: lower-end chips (M-series for non-Pro devices, iPad, lower iPhone tiers) — not flagship A-series
- TSMC expected to "continue as Apple's main chip manufacturer for its most advanced processors"
- Timeline: earliest feasible Intel production for Apple is 2027-2028

## Inferred limitations
- Intel 18A yield at ~62-65% may be insufficient for Apple's quality standards on flagship SoCs — lower-end focus is consistent with risk tolerance
- Samsung Texas facility timeline and yield readiness are uncertain for Apple-class designs
- Even a partial Apple-Intel deal would represent Intel's largest and most credible IFS win to date — transforming Intel Foundry's business case
- Risk: Apple designs may stress Intel's RibbonFET/PowerDirect integration in ways TSMC's process has been tuned for

## Architectural significance

**1. TSMC N2 capacity liberation for AI.** Apple consuming >50% of TSMC N2 capacity is a well-documented fact. If Apple shifts even 15-20% of its silicon volume to Intel 18A or Samsung SF2/SF2X, TSMC's N2 allocation opens for AMD, NVIDIA, and hyperscaler ASIC customers. This changes the "TSMC N2 100% booked, Apple >50%" chokepoint described in cross_sector_alpha.md pair 25 (FAB × ACC).

**2. Intel Foundry Services credibility validation.** No external design win has matched the credibility an Apple tape-out would provide Intel IFS. The discussions validate that 18A is at least *under consideration* by the world's most demanding chip customer. Combined with Intel's High-NA EUV first-mover advantage (paper-026), an Apple design win would transform Intel from a "make-or-break yield story" into a credible second-source foundry.

**3. TSMC single-source risk in the spotlight.** Apple's motivation is explicitly supply-chain risk from Taiwan-concentration and TSMC-exclusivity. This is the first high-profile disclosed instance of a major customer actively pursuing foundry diversification *for strategic reasons* (not just cost). It sets a precedent that AMD, Qualcomm, and hyperscaler ASIC teams may cite internally.

**4. Samsung Texas facility viability signal.** Apple executives visiting Samsung's Taylor, TX plant signals Samsung's US facility is progressing sufficiently to attract evaluation from the world's most demanding customer. This is positive for Samsung Foundry's global expansion and its High-NA EUV first-mover thesis.

## Cross-paper connections
- **paper-026 (ASML High-NA EUV):** Intel's High-NA first-mover advantage would be more valuable with Apple as a customer. Apple's evaluation may have been triggered partly by Intel's High-NA differentiation.
- **paper-027 (TSMC Symposium):** TSMC's A16 slip to 2027 and absence of High-NA EUV through 2029 make the Intel 18A/14A option more competitive for Apple's 2027-2028 timeline.
- **chip_fabrication paper-009 (N2 allocation):** The >50% Apple N2 allocation is the single largest foundry concentration; any partial diversification has outsized effects on capacity availability for AI.
- **CPU research.md:** CPU sector documents Intel 18A as the make-or-break yield story; an Apple design win would resolve that story decisively.

## Theme tags
`foundry-diversification`, `Apple-silicon`, `Intel-IFS`, `Samsung-Texas`, `TSMC-concentration-risk`, `supply-chain-geopolitics`, `N2-capacity-liberation`
