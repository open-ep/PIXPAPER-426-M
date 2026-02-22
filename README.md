<img src="https://github.com/user-attachments/assets/47d51a3d-a075-440f-b9df-2e13a8659e65" width="100" align="right">

# PIXPAPER-426-M
### 4.26 GrayScale Electronic Paper Display Module

<div align="center">

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Platform](https://img.shields.io/badge/platform-ARM%20%7C%20RISC--V-green.svg)
![License](https://img.shields.io/badge/license-GPLv2-orange.svg)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen.svg)

</div>

---

## 🎯 Product Overview

**Open-EP** introduces **PIXPAPER-426-M** - A professional-grade 4.26 inch gray-scale Electronic Paper Display module developed in collaboration with **Triangle Alien Studio**. This prototype showcases exceptional craftsmanship and superior hardware quality, featuring an SPI interface fully compatible with worldwide embedded devices.

<table>
<tr>
<td width="35%">
<img src="https://github.com/user-attachments/assets/7affd69a-6906-4586-a301-481bc97a6508" width="100%">
</td>
<td width="65%">

### 📊 Technical Specifications

| Specification | Details |
|:-------------|:--------|
| **Screen Size** | 4.26 inch |
| **Resolution** | 800 x 480 pixels |
| **Color Support** | Mono(Black, White), Gray-Scale(7-level) |
| **PPI** | 219 |
| **Interface** | SPI |
| **Partial Update** | YES |
| **Operating Temp** | 0 - 40°C |

</td>
</tr>
</table>

### 🔌 Pin Configuration
```
3.3V | GND | MOSI | SCK | CS# | DC# | RST# | BUSY
```
> **Note:** DC#, RST#, and BUSY are GPIO-controlled

---

## 📚 Implementation Guide

Choose your implementation approach based on your application requirements:

<div align="center">

```mermaid
graph LR
    A[PIXPAPER-426-M] --> B[User-Space Applications]
    A --> C[Linux Kernel DRM]
    A --> D[Special Applications]
    
    B --> B1[Quick Start]
    B --> B2[Flexible Control]
    
    C --> C1[Hardware Acceleration]
    C --> C2[System Integration]
    
    D --> D3[Custom Solutions]
    D --> D4[Advanced Features]
    
    style A fill:#ff6b6b
    style B fill:#4ecdc4
    style C fill:#45b7d1
    style D fill:#ffd93d
```

</div>

---

## 🚀 User-Space Applications

> **Best for:** Rapid prototyping, application-level control, and cross-platform development

User-space drivers provide direct application control without kernel modifications. Ideal for quick deployment and testing across multiple platforms.

### 🖥️ MPU Platforms (ARM64)

<table>
<tr>
<td align="center" width="50%">

<a href="https://www.nxp.com/" target="_blank">
<img src="https://github.com/TechNexion-Vision/.github/assets/28101204/67cc61c0-6bb7-44d5-889a-1ba5d4c0b9b5" height="80">
</a>

#### NXP
**Status:** ✅ Ready

</td>
<td align="center" width="50%">

<a href="https://www.telechips.com/" target="_blank">
<img src="https://github.com/user-attachments/assets/4f260b12-4d99-42e3-b9bd-6b90b2bbec16" height="80">
</a>

#### Telechips
**Status:** ✅ Ready

</td>
</tr>
</table>

#### 📖 Supported Boards & Guides

| Manufacturer | Board / SoC | Porting Guide | Status |
|:------------|:-----------|:--------------|:------:|
| **NXP** | FRDM-IMX93 (IMX93) | [📄 Guide](https://github.com/open-ep/PIXPAPER-426-M/blob/main/FRDM-IMX93_PIXPAPAER-426-M.md) | ✅ |
| **Telechips** | TOPST D3-G (Dolphin 3M) | [📄 Guide](https://github.com/open-ep/PIXPAPER-426-M/blob/main/D3-G_PIXPAPAER-426-M.md) | ✅ |

-----------------
### 🔧 MCU Platforms (ARM32)

<table>
<tr>
<td align="center" width="25%">

<a href="https://www.raspberrypi.com/" target="_blank">
<img height="100" alt="image" src="https://github.com/user-attachments/assets/f2c7c418-baf4-456f-81cd-1149b3247a4e" />


#### Raspberry Pi
**Status:** ✅ Ready

</td>
<td align="center" width="25%">

<a href="https://www.nxp.com/" target="_blank">
<img src="https://github.com/TechNexion-Vision/.github/assets/28101204/67cc61c0-6bb7-44d5-889a-1ba5d4c0b9b5" height="80">
</a>

#### NXP
**Status:** ✅ Ready

</td>
<td align="center" width="25%">

<a href="https://www.st.com/" target="_blank">
<img src="https://github.com/user-attachments/assets/512fc35f-6a9a-471c-bd2b-2d77ac4b4e0a" height="80">
</a>

#### ST
**Status:** ✅ Ready

</td>
</tr>
</table>

| Manufacturer | Board / Core | Porting Guide | Status |
|:------------|:------------|:--------------|:------:|
| **Raspberry Pi** | Raspberry Pi Pico (M0+) | [📄 Guide](https://github.com/open-ep/PIXPAPER-426-M/blob/main/RPI-PICO_PIXPAPAER-213-C.md) | ✅ |
| **NXP** | FRDM-IMX93 (M33 Core) | [📄 Guide](https://github.com/open-ep/PIXPAPER-426-M/blob/main/FRDM-IMX93-M33_PIXPAPAER-213-C.md) | ✅ |
| **ST** | STM32 | [📄 Guide](https://github.com/open-ep/PIXPAPER-426-M/blob/main/STM32_PIXPAPAER-213-C.md) | ✅ |

---

## 🐧 Linux Kernel DRM Integration

> **Best for:** System-level integration, hardware acceleration, and production deployments

DRM (Direct Rendering Manager) integration provides native Linux kernel support for optimal performance and seamless system integration.

### ✨ Advantages

<table>
<tr>
<td width="33%" align="center">

### ⚡ Performance
Hardware-accelerated rendering with zero-copy operations

</td>
<td width="33%" align="center">

### 🔄 Integration
Native support in framebuffer and display subsystems

</td>
<td width="33%" align="center">

### 🛡️ Stability
Kernel-space reliability with proper error handling

</td>
</tr>
</table>

### 📋 Platform Support Status

| Platform | Board | Architecture | DRM Driver Status | Kernel type |
|:---------|:------------|:------------|:-----------------|:----------------|
| **IMX95** | LEC-IMX95 | ARM64 | 📝 Planned | Vendor Kernel 6.12↑ |
| **IMX93** | PANZER-LITE93 | ARM64 | ✅ Ready,[📄 Guide](https://github.com/open-ep/PIXPAPER-426-M/blob/main/linux-kernel-drm/DRM-FRDM-IMX93_PIXPAPAER-426-M.md) | Vendor Kernel 6.12↑ |
| **RK3588** | CUBE-RK3588 | ARM64 | 📝 Planned | TBD |

> **Note:** DRM drivers are currently under active development. Contact us for early access programs.


---

## 🎨 Special Applications

> **Best for:** Custom solutions, research projects, and advanced use cases

Specialized implementations for unique requirements and cutting-edge applications.

### 🔬 Research & Development

<table>
<tr>
<td width="50%">

#### 🤖 Computer Vision
- [Local/Remote Real-Time Text Output System]()

</td>
<td width="50%">

#### 📡 Medical Applications
- Monitor displays

</td>
</tr>
<tr>
<td width="50%">

#### 🎓 AI Projects
- Speech To Text

</td>
<td width="50%">

#### 🏭 Industrial Applications
- Process monitoring
- Equipment status displays
- Factory automation

</td>
</tr>
</table>

### 🛠️ Custom Development Services

We offer tailored solutions for your specific needs:

- ✅ Custom driver development
- ✅ Platform porting services
- ✅ Performance optimization
- ✅ Technical consulting
- ✅ Batch customization

### 📞 Contact for Special Projects

Have a unique application in mind? We'd love to collaborate!

---

## 🤝 Community & Support

<div align="center">

### Stay Connected

[![GitHub Issues](https://img.shields.io/badge/Issues-Report%20Bug-red.svg)](https://github.com/open-ep/PIXPAPER-426-M/issues)
[![GitHub Discussions](https://img.shields.io/badge/Discussions-Join%20Community-blue.svg)](https://github.com/open-ep/PIXPAPER-426-M/discussions)
[![Documentation](https://img.shields.io/badge/Docs-Wiki-green.svg)](https://github.com/open-ep/PIXPAPER-426-M/wiki)

</div>

### 📬 Get Help

- **Technical Issues:** [Open an Issue](https://github.com/open-ep/PIXPAPER-426-M/issues)
- **Feature Requests:** [Start a Discussion](https://github.com/open-ep/PIXPAPER-426-M/discussions)
- **Commercial Inquiries:** support@open-ep.org

---

## 📄 License & Credits

**PIXPAPER-426-M** is developed by **Open-EP** in collaboration with **Triangle Alien Studio**.

<div align="center">

Made with ❤️ for the Embedded Community

**[Documentation](https://github.com/open-ep/PIXPAPER-426-M/wiki)** • **[Examples](https://github.com/open-ep/PIXPAPER-426-M/tree/main/examples)** • **[Changelog](https://github.com/open-ep/PIXPAPER-426-M/blob/main/CHANGELOG.md)**

</div>
