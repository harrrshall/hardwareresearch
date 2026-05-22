# Paper 003: Ayar Labs TeraPHY UCIe Optical Chiplet — World's First UCIe Optical Interconnect

**Tags:** optical-IO, silicon-photonics  
**Date:** March 31, 2025 (announced); OFC 2025 demonstration  
**Source:** Ayar Labs / BusinessWire / Optical Connections News  
**URL:** https://ayarlabs.com/news/ayar-labs-unveils-worlds-first-ucie-optical-chiplet-for-ai-scale-up-architectures/

## Summary

Ayar Labs unveiled the world's first Universal Chiplet Interconnect Express (UCIe) optical chiplet, enabling protocol-agnostic optical interconnect between AI accelerator chiplets. The TeraPHY chiplet is powered by the SuperNova multi-wavelength light source.

## Key Technical Specifications

- **Bandwidth per port:** 8 Tbps bidirectional
- **Wavelength count:** 16 wavelengths per port (DWDM)
- **Energy consumption:** as low as 5 pJ/bit
- **Interface:** UCIe electrical standard (enables multi-vendor interoperability)
- **Protocol support:** CXL, NVLink, UALink, Ethernet, any UCIe streaming mode traffic
- **Light source:** SuperNova (separate multi-wavelength chip, 16 wavelengths)
- **Production timeline:** Prototypes complete; production samples expected 2026

## Architecture Notes

TeraPHY embeds a silicon photonics transmit/receive engine with a UCIe electrical interface. The chiplet can be placed in multi-chip packages alongside GPU, AI, CPU, or networking dies via UCIe die-to-die bonding. The SuperNova light source delivers 16 independent wavelengths (C-band WDM), each modulated independently to achieve 8 Tbps total throughput.

## GUC Partnership

In November 2024, Ayar Labs integrated TeraPHY into GUC's advanced packaging and ASIC workflow, a critical step toward commercial CPO deployment at foundry scale.

## Hot Chips 2025

At Hot Chips 2025, Ayar Labs presented the UCIe Optical I/O Retimer variant with detailed system integration measurements.

## Funding and Ecosystem

- Raised $500M in 2026 funding round
- Investors/customers: NVIDIA, Intel, AWS (Trainium platform)
- U.S. Department of Defense deployment programs underway

## Significance

First UCIe-compliant optical chiplet standardizes optical I/O integration methodology. Protocol-agnostic design enables a single optical chiplet to serve multiple AI interconnect standards simultaneously.
