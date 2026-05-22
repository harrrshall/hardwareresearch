# paper-005: Intel EMIB and Foveros Direct 3D — Advanced Packaging as a Foundry Business

**Tags:** EMIB, Foveros, Intel, chiplet, 3D-stacking, hybrid-bonding
**Date Range:** 2025-Q4 – 2026-Q2
**Source IDs:** 29, 30, 31, 32, 33

---

## Summary

Intel is aggressively pivoting its advanced packaging technologies (EMIB and Foveros Direct) from internal products to external foundry services. Following demand overflow from the CoWoS shortage, Apple and Qualcomm are both reportedly evaluating EMIB. Intel's newest 18A-PT process node adds Foveros Direct 3D capability (bump-less copper-to-copper bonding) for external customers.

## Technical Details

**EMIB (Embedded Multi-Die Interconnect Bridge):**
- 2.5D silicon bridge (~55 mm²) embedded in organic package substrate
- Interconnects adjacent dies at bridge-crossing region
- Bridge bump pitch: ~55 μm (bridge-to-die) / ~45 μm fine-pitch variant
- Die-to-die bandwidth via EMIB: up to 896 GB/s per bridge
- EMIB-T: Next-generation variant with tighter pitch and greater bandwidth
- First outsourced to Amkor's Songdo K5 facility (South Korea)
- Ramp target: H2 2026 (confirmed by Intel CVP John Pitzer)

**Foveros Direct 3D:**
- True vertical die stacking with bumpless Cu-to-Cu hybrid bonding
- Sub-10 μm bonding pitch (< 10 μm interconnect density)
- Copper-to-copper diffusion bonding through TSVs
- Enabled by Intel 18A-PT node (variant of 18A-P performance process)
- Clearwater Forest (server chip) to ship with Foveros Direct 3D

**Combined System (18A + 14A Foveros + EMIB-T):**
- Up to 12x reticle-equivalent silicon integration
- Up to 16 compute dies (14A or 18A) per package
- Up to 24 HBM5 stacks per package
- Fab 9 and Fab 11x in Rio Rancho, NM: first Intel sites to mass-produce 3D advanced packaging

## Key Findings

1. Apple and Qualcomm are actively recruiting talent with Intel EMIB experience, signaling intent to qualify the process.
2. Google-MediaTek TPU reportedly in development using Intel EMIB packaging.
3. EMIB competes directly with TSMC's CoWoS-S and Samsung's H-Cube for 2.5D packaging.
4. Foveros Direct sub-10 μm pitch puts Intel in direct competition with TSMC's SoIC-X in the 3D stacking market.
5. Intel Technology Roadmap: Intel 14A on Intel 18A-PT connected via Foveros Direct + EMIB-T is the flagship heterogeneous integration offering.

## Implications

Intel's decision to open advanced packaging to external customers is strategically significant. If EMIB ramps successfully at Amkor Songdo by H2 2026, it provides customers a second-source alternative to TSMC's CoWoS at similar technical capability. Foveros Direct at sub-10 μm competes with TSMC SoIC-X at 6 μm — the pitch gap will narrow by 2027.
