# Paper 021: HBM Market Share and AI Memory Supercycle 2025-2026

**Source ID**: 11, 12, 52  
**Source Title**: SK Hynix Holds 62% of HBM; HBM Technology Landscape 2026; South Korea's HBM4 Moment  
**URLs**:  
- https://www.astutegroup.com/news/general/sk-hynix-holds-62-of-hbm-micron-overtakes-samsung-2026-battle-pivots-to-hbm4/  
- https://www.patsnap.com/resources/blog/articles/hbm-technology-landscape-2026-market-and-ai-demand/  
**Date**: 2025-Q2/Q3; 2026-01  
**Tags**: HBM, market-share, SK-Hynix, Samsung, Micron, supercycle, revenue

---

## One-Sentence Claim
SK Hynix held 62% global HBM market share in Q2 2025 (dropping to 57% in Q3), while Micron surpassed Samsung for the first time to claim second place at 21%; HBM demand grew 130%+ YoY in 2025 with 70%+ additional growth forecast for 2026, and all three vendors have sold out their 2026 HBM capacity.

## Methodology Summary
Market share data aggregated from TrendForce quarterly DRAM market reports. HBM demand growth based on AI accelerator unit projections from NVIDIA, AMD, and Google ASIC shipments. Revenue figures from company earnings reports and analyst estimates.

## Quantitative Results
- SK Hynix HBM market share: 62% (Q2 2025), 57% (Q3 2025)
- Samsung HBM share: 15% (Q2 2025), 22% (Q3 2025) — jumped from 3rd to 2nd
- Micron HBM share: 21% (Q2 2025), 21% (Q3 2025) — fell to 3rd
- HBM demand growth 2025: 130%+ YoY
- HBM demand forecast 2026: 70%+ YoY
- Micron HBM annualized revenue run-rate: ~$8B projected
- Morgan Stanley Samsung memory profit projection 2026: +300%
- SK Hynix 30% CAGR projected through 2030 for HBM segment
- All three vendors: 2026 HBM capacity sold out under multi-year agreements

## Stated Limitations
- Market share figures are estimates from third-party analysts, not confirmed financials
- Samsung's HBM3E qualification issues with NVIDIA in early 2025 depressed its Q2 share
- Sell-out clauses in supply agreements do not preclude price renegotiation

## Inferred Limitations
- SK Hynix's dominant position creates HBM supply chain risk for AI accelerator makers
- Samsung's rapid recovery from 15% to 22% share indicates qualification bottlenecks, not production limits
- HBM price increases (Samsung priced at 2x by some reports) create inflation pressure on AI hardware economics

## Architectural Significance
The HBM oligopoly — three vendors with locked 2026 capacity — is architecturally shaping AI hardware design choices. System designers are now treating HBM supply as a hard constraint and designing around it: AMD's 12-stack MI400 configuration (paper-008) maximizes bandwidth per GPU to reduce total GPU count needed, and CXL memory pooling (paper-005) extends system-level memory capacity beyond what HBM alone can provide.

## Cross-Paper Connections
- Samsung HBM4 supply for NVIDIA Vera Rubin (paper-007) and Google TPU is the revenue driver
- Micron's rise to 21% share (paper-003) came from successful HBM3E ramp on 1-beta process
- SK Hynix supply dominance (paper-001) is reinforced by being first to HBM4 mass production
- Memory supercycle (paper-055 source) reflects broader AI training CAPEX expansion

## Theme Tags
HBM, market-share, SK-Hynix, Samsung, Micron, supercycle, demand, capacity, oligopoly
