# paper-021: Through-Silicon Vias (TSVs) — Scaling and Inspection Technology Advances (2025)

**Tags:** TSV, through-silicon-via, advanced-packaging, 3D-stacking, manufacturing
**Date Range:** 2025-Q1 – 2025-Q4
**Source IDs:** 22

---

## Summary

TSVs remain the fundamental vertical interconnect in all 3D packaging — from HBM stacking (55 μm pitch) to SoIC bumpless bonding (9 μm pitch in production, sub-5 μm in development). ASME's 2025 review of TSV inspection and metrology identified Cu fill uniformity, void detection, and dimensional control as the critical manufacturing challenges at sub-10 μm TSV dimensions.

## Technical Details

**TSV Technology Specifications (2025):**
| Application | Diameter | Pitch | Depth | AR |
|---|---|---|---|---|
| HBM memory (via middle) | 5–8 μm | 40–55 μm | 50–70 μm | 10:1 |
| 3D logic (SoIC) | 2–5 μm | 9 μm | 50–100 μm | 20:1 |
| CMOS image sensor | 3–6 μm | 20–40 μm | 30–50 μm | 8:1 |
| Deep TSV (silicon interposer) | 10–20 μm | 40–80 μm | 100–250 μm | 12:1 |

**Manufacturing Process:**
1. Bosch deep reactive ion etching (DRIE): etch high-aspect-ratio via
2. SiO₂ liner deposition (ALD for conformality)
3. TaN/Ta barrier + Cu seed PVD
4. Bottom-up Cu electroplating (fills void-free)
5. CMP to remove overburden Cu
6. Wafer thinning (backgrind) to expose TSV tips

**Key Challenges (ASME 2025 Review):**
- Cu void formation at high aspect ratios (>15:1): requires advanced electroplating chemistry
- TSV-induced stress on surrounding silicon: affects transistor performance within 5–10 μm of TSV
- Inspection: X-ray CT and optical coherence tomography (OCT) required for sub-5 μm TSV; conventional optical insufficient
- Thermal cycling reliability: CTE mismatch between Cu and Si generates fatigue at TSV tips

**Inspection Advances:**
- ALD (atomic layer deposition) for liner: improved conformality vs. CVD at aspect ratios > 15:1
- HDP-CVD: improved gap fill for oxide liner
- Spin-on dielectrics: filling capability for complex TSV shapes

## Key Findings

1. AMD MI300X uses 9 μm pitch SoIC TSVs — at the production frontier for high-volume applications.
2. JEDEC's decision to increase HBM4 package thickness to 775 μm accommodates the TSV depth required for 12-Hi stacking.
3. TSV-induced stress ("keep-out zone") at 10+ μm from via edges limits transistor placement density around TSVs.
4. ACM Research is developing electrolytic TSV fill processes targeting < 5 μm pitch with >99.5% void-free yield.
5. TSV market projected to grow in alignment with 2.5D/3D packaging at compound rates of 15–20% through 2030.

## Implications

TSV pitch scaling from 55 μm (HBM) to 9 μm (SoIC) to future < 5 μm represents a ~10x density increase. As pitch shrinks below 5 μm, conventional electrochemical deposition approaches will require fundamental chemistry changes. Inspection and metrology cost grows super-linearly with pitch reduction, becoming a meaningful packaging cost contributor at sub-5 μm.
