# paper-020: ISSCC 2026 Electro-Optical Router — In-Package Dynamic Optical Routing

**Tags:** optical-switching, chip-to-chip  
**Date:** 2026-02  
**Source:** CEA-List / CEA-Leti / Electronics Weekly  
**URL:** https://www.electronicsweekly.com/news/business/isscc-2026-02/

---

## Summary

Researchers from CEA-List and CEA-Leti presented the first electro-optical router with dynamic, frame-level routing integrated with CMOS control logic at ISSCC 2026. Implemented in 28nm CMOS on a photonic interposer, this device establishes optical paths in 18 ns and achieves 3.19 pJ/bit — a landmark for practical optical networking inside chiplet-based packages.

## Device Specifications

| Parameter | Value |
|---|---|
| CMOS process | 28nm |
| Platform | Photonic interposer (silicon photonics) |
| Optical path establishment time | **18 ns** |
| Energy efficiency | **3.19 pJ/bit** |
| Active area per link | **0.007 mm²** |
| Wavelengths per link | Up to 6 (dynamic selection) |
| Routing type | Dynamic, frame-level |

## Architecture

The electro-optical router consists of:
1. **Optical switching elements**: Silicon photonic microring resonators driven by analog drivers
2. **CMOS control logic**: Standard-cell digital circuitry for wavelength selection and path setup
3. **Analog drivers**: Co-integrated with SerDes for dense endpoint packing
4. **Photonic interposer**: Silicon platform hosting both optical and electrical components

### Dynamic Routing
- Traditional optical switches are static (circuit-switched) — paths are set for entire sessions
- This router switches paths at **frame granularity** (~18 ns per reconfiguration)
- Enables packet-switching-like behavior in optical domain: different frames can take different optical paths
- Critical for AI training collective communications (AllReduce) where traffic patterns change rapidly

### Wavelength Division Multiplexing
- 6 wavelengths per link, dynamically selected
- Up to 6x bandwidth multiplexing within a single optical waveguide
- Wavelength selection adds minimal latency (<1 ns) within the 18 ns total setup time

## Energy Efficiency Context

| Technology | Energy/bit |
|---|---|
| Pluggable optical (400G) | 24 pJ/bit |
| CPO on MCM | 6.75 pJ/bit |
| CPO on interposer | 3.5 pJ/bit |
| **CEA electro-optical router (ISSCC 2026)** | **3.19 pJ/bit** |
| CEI-224G XSR electrical (target) | <0.5 pJ/bit |

The CEA device achieves parity with CPO-on-interposer at 3.19 pJ/bit, but with **dynamic routing capability** that CPO devices lack.

## Implications for Chiplet Interconnects

The combination of:
- **18 ns reconfiguration** (fast enough for sub-microsecond network scheduling)
- **3.19 pJ/bit** (competitive with state-of-art CPO)
- **0.007 mm² per link** (extremely dense, fits within chiplet edge area)

...makes this architecture a candidate for:
1. In-package all-to-all interconnect between chiplets (replacing 3D torus wired topologies)
2. Memory fabric switching between compute chiplets and disaggregated HBM
3. Multi-rack coherent interconnects at lower latency than current solutions

## Path to Production

Challenges remaining:
- Temperature sensitivity of silicon photonic microring resonators (requires active thermal stabilization)
- Fabrication yield on photonic interposer platforms still maturing
- Integration with leading-edge CMOS (28nm demonstrated; 7nm/5nm integration TBD)

## Strategic Observations

- The 3.19 pJ/bit landmark validates optical routing as competitive with best-in-class CPO at the energy level
- Dynamic frame-level routing in optical domain could eliminate the static circuit-switched limitation of current optical fabrics
- CEA's photonic interposer approach is complementary to Celestial AI's in-die photonic approach — different positions on the package integration spectrum
