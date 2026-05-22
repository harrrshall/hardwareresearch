# paper-016: OIF CEI-224G and XSR/USR — Next-Generation Electrical Die-to-Die Standards

**Tags:** chip-to-chip  
**Date:** 2025  
**Source:** OIF Forum / Semiconductor Engineering / SemiAnalysis  
**URL:** https://www.oiforum.com/technical-work/hot-topics/common-electrical-i-o-cei-224g/

---

## Summary

The OIF's Common Electrical Interface (CEI) program is defining 224 Gbps electrical standards across four reach categories — XSR (on-package), VSR (chip-to-module), MR (board-level), and LR (backplane). An interoperability demonstration at OFC 2025 showed 224G, 448G, and 112G CEI variants functioning together, marking a key milestone toward multi-vendor ecosystem validation.

## CEI Reach Categories at 224G

| Variant | Reach | Use Case | Physical Medium |
|---|---|---|---|
| CEI-224G-XSR | <50 mm (on-package) | Die-to-die within MCM | Silicon substrate / organic |
| CEI-224G-VSR | <300 mm | Chip-to-optical-module | PCB trace |
| CEI-224G-MR | <500 mm | Board-to-board (backplane) | FR4 PCB |
| CEI-224G-LR | >500 mm | Backplane, copper cable | Specialized substrates |

## Key Technical Parameters

| Parameter | CEI-112G | CEI-224G |
|---|---|---|
| Line rate | 112 Gbps | 224 Gbps |
| Modulation | PAM4 | PAM4 |
| Symbol rate | 56 GBaud | 112 GBaud |
| FEC | Optional | Mandatory (XSR, VSR) |
| Energy target (XSR) | ~1 pJ/bit | <0.5 pJ/bit (target) |

## USR vs XSR Distinction

Within the CEI framework:
- **USR (Ultra-Short Reach)**: Die-to-die within same package, <20 mm, extremely low power budget
- **XSR (Extra-Short Reach)**: Die-to-die or chip-to-optical-engine in same MCM, 20–50 mm

Synopsys DesignWare USR/XSR PHY IP complies with OIF CEI-112G and CEI-56G USR/XSR, with 224G PHY IP under active development.

## OFC 2025 Interoperability Demo

At OFC 2025 (March 2025), OIF members demonstrated:
- Live interoperability between **112G, 224G, and 448G** CEI implementations
- Multi-vendor plugfest across NIC, switch, and optical module vendors
- First public validation of CEI-224G physical layer at scale

## 224G Application in AI Interconnects

- **UALink 200G 1.0**: Explicitly based on 200 GT/s which leverages CEI-224G VSR electrical interface
- **NVLink 6**: 400 Gbps SerDes per sub-link (targets 448G-class electrical)
- **Broadcom Tomahawk 6**: 200G SerDes lanes use CEI-224G-MR class electrical

## Energy vs Bandwidth Trajectory

| Interface | BW/lane | pJ/bit |
|---|---|---|
| CEI-112G XSR | 112 Gbps | ~1.0 |
| CEI-224G XSR (target) | 224 Gbps | ~0.5 |
| Optical (CPO) | 400 Gbps | 3.5–6.75 |
| Optical (pluggable) | 200 Gbps | 14–24 |

CEI-224G XSR at <0.5 pJ/bit significantly undercuts optical for on-package die-to-die connections, maintaining electrical as the preferred medium for distances <50 mm.

## IEDM 2025 Findings

At IEDM 2025, CEA demonstrated an electro-optical router on photonic interposer (ISSCC 2026 publication):
- 28nm CMOS, 3.19 pJ/bit — approaching the parity point between advanced electrical and optical
- Dynamic wavelength selection (6 wavelengths/link) in 18 ns

## Strategic Observations

- The 224G ecosystem is still maturing; full production silicon expected 2026–2027
- CEI-224G XSR will be critical for UALink switch chip die-to-die connections when UALink silicon ships in late 2026
- The pJ/bit crossover between CEI-224G electrical and CPO optical creates a design boundary: electrical wins at <50 mm, optical wins beyond package boundary
