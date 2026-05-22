# paper-022: Ayar Labs TeraPHY UCIe Optical Chiplet — 8 Tbps In-Package Photonics

**Tags:** optical-switching, UCIe, chip-to-chip  
**Date:** 2025-03-31  
**Source:** Ayar Labs / BusinessWire / OFC 2025  
**URL:** https://www.businesswire.com/news/home/20250331044779/en/Ayar-Labs-Unveils-Worlds-First-UCIe-Optical-Chiplet-for-AI-Scale-Up-Architectures

---

## Summary

Ayar Labs unveiled the world's first UCIe-compatible optical I/O chiplet at OFC 2025 (March 2025), delivering 8 Tbps aggregate bandwidth per chiplet with a bandwidth density of 200 Gbps per millimeter of chip edge — 1,000x the density of conventional electrical I/O. This enables memory disaggregation up to 2 km from compute while maintaining coherent bandwidth.

## TeraPHY Optical I/O Chiplet Specifications

| Parameter | Value |
|---|---|
| Bandwidth per chiplet | **8 Tbps** |
| Bandwidth density | **200 Gbps/mm** chip edge |
| Density vs electrical I/O | **1,000x** |
| Light source | SuperNova (16-wavelength) |
| Standard compliance | UCIe 2.0 Standard Package |
| Fabrication | Silicon photonics + CMOS (same manufacturing) |

## SuperNova Light Source

- 16 wavelengths per fiber channel (WDM)
- Continuous-wave (CW) laser source — power generated separately from modulation
- External laser approach reduces thermal coupling between laser and signal electronics

## Use Cases

### AI Scale-Up (Primary Use Case)
- Replace electrical NVLink/InfiniBand cables with optical UCIe chiplet connections
- Enable scale-up fabrics beyond single-rack without bandwidth degradation
- Maintain <10 ns latency at rack-to-rack distances (<2 m)

### Memory Disaggregation
- Memory modules up to **2 km from compute** package
- Latency: **< 2×5 ns + Time-of-Flight**
  - 5 ns electrical I/O each direction + optical propagation delay
  - At 100 m: total latency ≈ 10 ns + 0.5 µs (TOF) ≈ 0.51 µs
  - At 2 km: total latency ≈ 10 ns + 10 µs (TOF) ≈ 10.01 µs
- Bandwidth maintained at 8 Tbps regardless of distance (unlike electrical)

## UCIe Integration

The TeraPHY is the first optical chiplet compliant with UCIe 2.0 Standard Package:
- Protocol layer: PCIe or CXL (inherited from UCIe)
- Physical layer: replaced from electrical to optical (TeraPHY handles electrical-to-optical conversion)
- Host sees TeraPHY as a standard UCIe peer — no software changes required
- Drop-in replacement for electrical UCIe I/O

## Comparison to Conventional Electrical I/O

| Parameter | Electrical I/O | TeraPHY |
|---|---|---|
| Max distance | ~1 m (PCB/package) | 2,000 m |
| Bandwidth density | ~0.2 Gbps/mm | 200 Gbps/mm |
| Latency at 10 m | <1 ns | ~60 ns |
| Latency at 100 m | N/A (not feasible) | ~510 ns |
| Energy | ~0.5 pJ/bit | ~2–4 pJ/bit |

## Industry Significance

- First demonstration that UCIe standard can encompass optical physical layer
- Enables heterogeneous chiplet integration with compute and memory physically separated
- OFC 2025 marked the transition from concept to silicon-validated product

## Alchip + Ayar Labs CPO Collaboration (2025)

Alchip Technologies and Ayar Labs announced collaboration on co-packaged optics for AI datacenter scale-up:
- Alchip provides chip design services and advanced packaging expertise
- Ayar Labs provides TeraPHY optical engine
- Target: AI accelerator packages with integrated optical scale-up from day one

## Strategic Observations

- The 1,000x bandwidth density advantage over electrical I/O justifies the 4–8x energy premium for distance-insensitive applications
- UCIe compatibility is crucial: it means existing SoC designs can adopt optical I/O without protocol changes
- The 2 km reach transforms memory disaggregation from a per-rack to a per-building architecture
