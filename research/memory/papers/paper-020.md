# Paper 020: 3D NAND 400-Layer Race — Samsung, SK Hynix, Kioxia 2025-2026

**Source ID**: 46, 47  
**Source Title**: Samsung Plans 400-Layer V-NAND by 2026; Kioxia BiCS10 332-Layer Expedited  
**URLs**:  
- https://www.trendforce.com/news/2024/10/29/news-samsung-reportedly-plans-400-layer-vertical-nand-by-2026-targeting-1000-layer-nand-by-2030/  
- https://www.tomshardware.com/pc-components/ssds/kioxias-next-gen-3d-nand-production-gets-expedited-to-2026-report-claims  
**Date**: 2024-10 / 2025-2026  
**Tags**: 3D-NAND, Samsung, Kioxia, SK-Hynix, 400-layer, hybrid-bonding

---

## One-Sentence Claim
Samsung's V10 NAND targets 400+ layers with 1 Tb die at 28 Gb/mm² density for H1 2026, Kioxia's 332-layer BiCS10 was accelerated from 2027 to 2026 for AI data center demand, and SK Hynix's 321-layer 4D NAND uses hybrid bonding with 400-layer target by end of 2025 — collectively establishing 400-layer 3D NAND as the industry's 2026 storage milestone.

## Methodology Summary
Samsung's V10 uses its hybrid bonding technology (licensed from YMTC) to bond upper and lower NAND decks, enabling 400+ layer count. SK Hynix entered mass production of 321-layer 4D NAND and accelerated its hybrid bonding roadmap for the V9+ generation. Kioxia expedited BiCS10 from 2027 to 2026 in response to hyperscaler SSD demand for AI training datasets.

## Quantitative Results
- Samsung V10: 400+ layers, 1 Tb die, 28 Gb/mm², TLC format, H1 2026
- Samsung long-term: 1,000-layer target by 2030
- SK Hynix V9: 321 layers, 4D NAND, hybrid bonding, in mass production (2025)
- SK Hynix 400-layer: hybrid bonding, production target by end-2025 / H1 2026
- Kioxia BiCS10: 332 layers, high-capacity AI data center focus, expedited to 2026
- Industry convergence: 1 Tb and 2 Tb die capacities by 2026-2027 for QLC products
- V10Q (500-layer QLC): target H1 2027 at 4800 MT/s

## Stated Limitations
- Layer count beyond 400 requires new precision stacking — z-pitch (layer-to-layer spacing) must be reduced
- Kioxia's BiCS10 acceleration is driven by customer demand; manufacturing ramp is still a risk
- QLC (4-bits/cell) at 400+ layers faces reliability challenges (retention, endurance) vs TLC

## Inferred Limitations
- The race to 1,000 layers (Samsung 2030 target) requires process innovations not yet demonstrated
- Higher layer counts increase die stacking height, creating mechanical stress and thermal challenges
- For AI data center SSD workloads, NAND write endurance (QLC: ~100-300 P/E cycles) is a deployment limitation

## Architectural Significance
The 400-layer 3D NAND milestone enables 16TB+ SSDs at competitive cost points, directly enabling the petabyte-scale storage tiers needed for AI training datasets. The accelerated timelines (Kioxia pulling BiCS10 from 2027 to 2026) reflect hyperscaler demand driven by AI training. The hybrid bonding techniques developed for 3D NAND are now being applied to HBM4E (paper-012), showing cross-pollination of packaging technologies.

## Cross-Paper Connections
- Hybrid bonding for NAND (this paper) is the same technology being developed for HBM4E (paper-012)
- 400-layer 3D NAND at 1-2 Tb per die enables near-storage compute architectures
- YMTC's hybrid bonding patent position (paper-012) affects both NAND and DRAM stacking for Korean vendors
- Oxide-semiconductor technology for 3D DRAM (paper-009, 010) draws on 3D NAND vertical stacking expertise

## Theme Tags
3D-NAND, Samsung-V10, Kioxia-BiCS10, SK-Hynix, 400-layer, hybrid-bonding, QLC, TLC, AI-storage
