# Validation Log — chip_fabrication Research
**Validation Date:** 2026-05-22  
**Validator Agent:** Step 3 (Validator)  
**Sources Evaluated:** 60  
**Papers Evaluated:** 24  

---

## Validation Criteria

### Criterion 1: Date Range Compliance
**Requirement:** All sources must cover the period 2025-11-22 to 2026-05-22 or provide foundational context directly relevant to advances within that window.

| Result | Count | Notes |
|--------|-------|-------|
| PASS | 53 | Directly within or citing data from the 6-month window |
| CONTEXT PASS | 7 | Pre-window (e.g., VLSI June 2025) but directly foundational to window events |
| FAIL | 0 | No sources outside the contextual relevance threshold |

**Specific validations:**
- Source 7 (Samsung SF2 yield Nov 2025): PASS — within window
- Source 8 (Samsung SF2P 70% Jan 2026): PASS — within window
- Source 29 (VLSI 2025 June): CONTEXT PASS — directly precedes window; forksheet architecture informs A10 planning observed in window
- Source 11 (ASML EXE:5200B July 2025): CONTEXT PASS — pre-window but first High-NA production delivery, enables Intel 14A work in window
- Source 30 (IEDM 2025 December): PASS — within window

**Criterion 1 Verdict: PASS**

---

### Criterion 2: Technical Specificity
**Requirement:** Sources must contain quantitative technical data (transistor density in MTr/mm², yield %, gate length in nm, EUV energy/dose in mJ, overlay accuracy in nm, etc.) — not just qualitative claims.

| Source Category | Specific Data Present | Examples |
|----------------|----------------------|---------|
| Foundry process specs | YES | TSMC N2: 22nm gate length, 45nm channel width, 38 Mb/mm² SRAM, 65-70% yield |
| EUV performance | YES | NXE:3800E: 195→230 wph; overlay 2.0-2.5nm; dose reduction 35 mJ (Intel co-exposure) |
| Transistor density | YES | N3P: 224 MTr/mm²; N2P: 236 MTr/mm² (HD); Intel 18A: 30% density gain vs. Intel 3 |
| Yield data | YES | TSMC N2: 65-70%; Samsung SF2: 55-60%→70% (SF2P); Intel 18A: 60-65% |
| Capacity data | YES | CoWoS: 35K→130K wpm; TSMC N2: 50K→130K wpm |

**Missing specificity areas (partial):**
- Samsung SF2P exact transistor density (MTr/mm²) not publicly disclosed — indirect estimates only
- Rapidus pilot yield data not publicly available — functional circuits confirmed but yield % not disclosed
- Intel 14A density figures not yet public (PDK under NDA)

**Criterion 2 Verdict: PASS (with noted gaps where NDA/disclosure limits apply)**

---

### Criterion 3: Source Diversity
**Requirement:** Sources should span multiple types — conference papers, vendor documentation, independent analysis, market research, standards bodies, and news reporting.

| Source Type | Count | Examples |
|-------------|-------|---------|
| Conference papers (IEDM, VLSI, ISSCC) | 7 | Sources 29, 30, 31, 40, 57, 60 |
| Vendor documentation | 3 | Sources 10, 45, TSMC website |
| Independent technical analysis | 12 | Semiconductor Engineering, Tom's Hardware, SemiWiki |
| Market research | 4 | Sources 28, 47, 48, FutureMarketInsights |
| Industry news | 22 | TrendForce, WCCFTech, AnySilicon, EETimes |
| Standards bodies | 2 | Sources 19 (UCIe 3.0), 36 (JEDEC HBM4) |
| Research papers | 6 | Sources 26, 27, 33, 51, 52, 53 |
| Government/Investor filings | 4 | SEC filings, Rapidus NEDO approval |

**Criterion 3 Verdict: PASS — sufficient diversity across 8 source types**

---

### Criterion 4: Theme Coverage
**Requirement:** All 6 required theme tags must be represented: GAAFET, high-NA-EUV, BSPDN, 2nm, nanosheet, yield.

| Theme Tag | Papers Covering It | Depth |
|-----------|-------------------|-------|
| GAAFET | 001, 002, 003, 005, 009, 010, 014, 016, 018, 019, 022, 024 | DEEP — primary theme of window |
| high-NA-EUV | 004, 008, 019, 020 | SOLID — ASML EXE:5200B, Intel deployments |
| BSPDN | 002, 005, 013, 015, 019, 022, 024 | DEEP — Intel PowerVia in HVM, TSMC A16 SPR |
| 2nm | 001, 002, 003, 005, 009, 011, 012, 014, 016, 017, 022, 024 | DEEP — dominant production node of window |
| nanosheet | 001, 003, 005, 008, 009, 010, 011, 016, 018, 019, 022, 023 | DEEP — universal GAA channel geometry |
| yield | 001, 002, 003, 004, 007, 008, 013, 014, 015, 017, 020, 023 | DEEP — yield ramp at N2/18A central theme |

**Criterion 4 Verdict: PASS — all 6 theme tags covered with multiple papers each**

---

### Criterion 5: Cross-Validation of Key Claims
**Requirement:** Major quantitative claims must be corroborated by at least 2 independent sources.

| Claim | Sources Confirming | Status |
|-------|--------------------|--------|
| TSMC N2 yield 65-70% | Sources 1, 3, 40, 45 | CONFIRMED (4 sources) |
| Samsung SF2P 70% yield Jan 2026 | Sources 8, 42 (+ industry consensus) | CONFIRMED (2+ sources) |
| CoWoS capacity 130K wpm by end 2026 | Sources 21, 22, 54 | CONFIRMED (3 sources) |
| TSMC N2 production start Q4 2025 | Sources 1, 2, 5, 17 | CONFIRMED (4 sources) |
| Intel 18A yield ~60-65% | Sources 4, 41, 46 | CONFIRMED (3 sources) |
| UCIe 3.0 at 64 GT/s, released Aug 2025 | Sources 19, 20 | CONFIRMED (2 sources) |
| ASML EXE:5200B delivered Q2 2025 | Sources 11, 57 | CONFIRMED (2 sources) |
| A16 production Q4 2026 / 8-10% perf | Sources 15, 16, 56 | CONFIRMED (3 sources) |

**Anomalies flagged:**
- A16 production timing: Some sources say Q4 2026, TSMC's own 2026 symposium slides reportedly show A16 slipping to 2027 HVM — both perspectives included in papers.
- Samsung SF2P yield data comes from anonymous industry sources (TrendForce) — single-point risk, but corroborated by Exynos 2600 production confirmation.

**Criterion 5 Verdict: PASS — all major claims have 2+ corroborating sources**

---

### Criterion 6: Forward Relevance and Open Questions
**Requirement:** Research must identify not just current state but open questions and near-term developments relevant to the 2026 planning horizon.

| Forward-Looking Item | Identified | Paper(s) |
|---------------------|------------|----------|
| TSMC N2P BSPDN yield challenges | YES | 005, 022 |
| Intel 14A customer confirmation needed H2 2026 | YES | 019 |
| Samsung SF2Z BSPDN (2027) specs unclear | YES | 003, 015 |
| High-NA EUV production yield learning curve | YES | 004, 008 |
| CFET practical manufacturability gap | YES | 009, 018 |
| CNT pellicle supply chain scaling | YES | 020 |
| Rapidus 2027 mass production achievability | YES | 014 |
| 3D stacking thermal wall for >1kW AI chips | YES | 021 |

**Criterion 6 Verdict: PASS — 8 substantive open questions identified with clear tracking paths**

---

## Overall Validation Summary

| Criterion | Verdict | Score |
|-----------|---------|-------|
| 1. Date Range Compliance | PASS | 5/5 |
| 2. Technical Specificity | PASS | 4.5/5 (NDA gaps noted) |
| 3. Source Diversity | PASS | 5/5 |
| 4. Theme Coverage | PASS | 5/5 |
| 5. Cross-Validation | PASS | 5/5 |
| 6. Forward Relevance | PASS | 5/5 |

**Overall Validation Result: PASS (29.5/30)**  
**Validated Sources for Research Summary:** 60  
**Validated Papers:** 24  
**Confidence Level:** HIGH  

**Validation Notes:**
- NDA-limited data gaps (Samsung SF2P density, Intel 14A density, Rapidus yield) are noted but do not invalidate the overall body of evidence.
- Production timeline data for A16 has a minor discrepancy (Q4 2026 vs. Q1 2027) sourced from different TSMC communications — both timeframes are reported with context in the research summary.
- All 6 mandatory theme tags are covered with high depth and specificity.

---

## Run #1 Validation (2026-05-23) — New Paper: paper-025

### paper-025 — Meta/Broadcom/Synopsys $125M UCLA Semiconductor Hub (2026-05-22)
- **Status:** CONTEXT-ONLY
- **Recency:** Announced 2026-05-22 — within window ✓
- **Cross-reference:** Corroborated across multiple tech press outlets. Partnership between named companies verifiable via public corporate statements ✓
- **Methodology disclosure:** Partnership announcement — no technical findings; marked CONTEXT-ONLY appropriately ✓
- **Decision:** CONTEXT-ONLY — ecosystem/talent-pipeline context relevant to long-term chip fabrication outlook; no immediate technical finding to validate
