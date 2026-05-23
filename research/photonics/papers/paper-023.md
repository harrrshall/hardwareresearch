# paper-023 — GlobalFoundries SCALE CPO Platform

**Validation status:** VALIDATED  
**Source:** GlobalFoundries Press Release, 2026-05-04  
**URL:** https://gf.com/gf-press-release/globalfoundries-accelerates-adoption-of-co-packaged-optics-for-advanced-ai-data-centers-with-scale-optical-module-solution/  
**Tier:** 4 (primary vendor disclosure)  
**Run:** #1 (2026-05-23)

---

## One-Sentence Claim

GlobalFoundries launched SCALE (Silicon Photonics Co-packaged Advanced Light Engine), the industry's first Optical Compute Interconnect Multi-Source Agreement (OCI MSA)-compliant CPO platform targeting AI data center scale-up architectures.

## Methodology Summary

Product announcement and ecosystem demonstration. GF's 300mm silicon photonics process underlies the SCALE platform. Technical specifications disclosed for the photonic integrated circuit (PIC): CWDM and DWDM bi-directional transmission modes, 8λ and 16λ configurations, 50Gbps and 100Gbps micro-ring modulators. Ecosystem partners (SENKO, Corning, EXFO, Siluxtek) provided third-party validation of the full CPO signal path.

## Quantitative Results

- **Data rates:** 50 Gbps and 100 Gbps per lane via micro-ring modulators
- **Wavelength modes:** 8λ and 16λ DWDM bi-directional transmission
- **OCI MSA compliance:** exceeds the specification requirements for modern AI scale-up architectures
- **Fiber interface:** SENKO wafer-level detachable connector supports repeatable testing throughout PIC development
- **Siluxtek 200G/lane SiPho receiver chips** in production qualification on GF process

## Stated Limitations

- Platform is production-qualification stage, not yet volume AI deployment
- Does not disclose power figures or latency vs competing CPO platforms
- Laser source integration details not specified (whether uses EML or on-chip laser)

## Inferred Limitations

- GF's 300mm SiPho process competes directly with TSMC COUPE; market share vs TSMC is uncertain
- 200G/lane receiver (Siluxtek) is the bandwidth target but qualification timeline not stated
- OCI MSA is a relatively new standard; customer adoption depends on ecosystem breadth

## Architectural Significance

This is the first foundry-level OCI MSA CPO platform from a non-TSMC foundry at production scale. It signals that silicon photonics is no longer a TSMC/GF niche trade but a competitive multi-foundry market. By targeting the OCI MSA standard (designed for AI scale-up fabrics), GF positions its SiPho capacity directly against TSMC COUPE for AI accelerator interconnect. The DWDM approach (vs single-wavelength CWDM in earlier CPO generations) dramatically increases bandwidth density per fiber.

## Cross-Paper Connections

- Extends the foundry-war insight established by photonics sources 35–40 (Tower/imec/GF/TSMC SiPho competition)
- Directly relevant to Finding 4 in cross_sector_alpha.md (EML laser supply gates CPO) — GF SCALE's laser approach (ring modulator based) may reduce EML dependency if on-chip laser alternatives mature
- Connects to packaging/paper-023 (CoPoS panel-level integration) as GF SCALE's detachable fiber interface addresses a key CPO manufacturing challenge
- Revenue forecast (src-054) provides the financial confirmation that SiPho is now a material business line

## Theme Tags

`CPO`, `silicon-photonics`, `OCI-MSA`, `DWDM`, `micro-ring-modulator`, `foundry-competition`, `GF-SiPho`, `AI-scale-up`, `optical-interconnect`
