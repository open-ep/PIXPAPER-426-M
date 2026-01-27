[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

## Linux Kernel DRM Driver User-Guide

## Hardware Preparison

Because [FRDM-IMX93 - Single Board Computer](https://youtu.be/ZpD9j6_nsNI?si=w4PjBL8ydYqj8hmg) has a 40-PIN pin header and compatible with Raspberry PI, so it has one SPI interface can be used.

Firstly, connecting the PIXPAPER-426-M's connector to the programming cable we've provided. Connect the other end of the cable to the corresponding pins, matching the colors as defined.

![image](https://github.com/user-attachments/assets/af657fcd-c5c5-4a54-b7a7-40c95f902b9c)
![image](https://github.com/user-attachments/assets/6ae059a1-9711-4d93-b800-46bffb24d128)



Then, connect to the FRDM-IMX93 specific PINs of 40-PIN header as follows:

<img src="https://github.com/user-attachments/assets/a26cf67e-9e79-4f71-a7aa-e6b0914e2319" width="600"> <br>
<img src="https://github.com/user-attachments/assets/313f981a-8fe0-4196-a6a6-c9624f8eecf3" width="600">


## Driver Installation instructions

|Kernel|Tested|
|---|---|
| 6.12 |&#10004;|

This guide will walk you through the process of building and installing the DRM driver for PIXPAPER-426M on FRDM-IMX93 using NXP vendor kernel 6.12.

### Prerequisites

- FRDM-IMX93 development board
- NXP vendor kernel 6.12 source code
- Cross-compilation toolchain for ARM64 (if building on x86_64 host)
- Git

### Step 1. Obtain NXP Vendor Kernel 6.12

Clone the NXP vendor kernel repository and checkout the 6.12 branch:

```bash
git clone https://github.com/nxp-imx/linux-imx.git
cd linux-imx
git checkout lf-6.12.y
```

### Step 2. Apply Driver Patches

Navigate to your kernel source directory and apply the patches in order:

```bash
cd linux-imx

# Apply the main driver patch
git am /path/to/frdm-imx93-kernel-6.12/0001-drm-tiny-add-support-for-Pixpaper-426M-e-ink-panel.patch

# Apply ARGB8888 format support patch
git am /path/to/frdm-imx93-kernel-6.12/0001-drm-tiny-pixpaper-426m-add-ARGB8888-format-support.patch

# Apply mirror issue fix patch
git am /path/to/frdm-imx93-kernel-6.12/0001-drm-tiny-pixpaper-426m-fix-mirror-issue.patch
```

**Note**: Replace `/path/to/` with the actual path to the `frdm-imx93-kernel-6.12` directory.

### Step 3. Modify Device Tree

Add the PIXPAPER-426M device node to your board's device tree file. For FRDM-IMX93, edit the device tree source file (e.g., `arch/arm64/boot/dts/freescale/imx93-lite93-evb.dts` or your custom board DTS).

**Step 3.1: Add pinctrl configuration in the &iomuxc section**

Add the SPI pin configuration in the `&iomuxc` section:

```dts
&iomuxc {
    pinctrl_lpspi3: lpspi3grp {
        fsl,pins = <
            MX93_PAD_GPIO_IO08__GPIO2_IO08      0x3fe  /* CS */
            MX93_PAD_GPIO_IO09__LPSPI3_SIN      0x3fe  /* MISO */
            MX93_PAD_GPIO_IO10__LPSPI3_SOUT     0x3fe  /* MOSI */
            MX93_PAD_GPIO_IO11__LPSPI3_SCK      0x3fe  /* SCK */
        >;
    };
};
```

**Step 3.2: Configure the SPI bus and add PIXPAPER device node**

Add or modify the `&lpspi3` section to include the PIXPAPER-426M device. This example shows a complete working configuration:

```dts
&lpspi3 {
    fsl,spi-num-chipselects = <1>;
    pinctrl-names = "default", "sleep";
    pinctrl-0 = <&pinctrl_lpspi3>;
    pinctrl-1 = <&pinctrl_lpspi3>;
    cs-gpios = <&gpio2 8 GPIO_ACTIVE_LOW>;
    status = "okay";

    display@0 {
        compatible = "mayqueen,pixpaper";
        reg = <0>;
        spi-max-frequency = <1000000>;
        reset-gpios = <&gpio2 5 GPIO_ACTIVE_HIGH>;
        dc-gpios = <&gpio2 0 GPIO_ACTIVE_HIGH>;
        busy-gpios = <&gpio2 26 GPIO_ACTIVE_HIGH>;
    };
};
```

**Important Notes about Compatible String**:

The driver supports both `"mayqueen,pixpaper"` and `"mayqueen,pixpaper-426m"` as compatible strings. You can use either one:
- `"mayqueen,pixpaper"` - Generic name (shown in example above)
- `"mayqueen,pixpaper-426m"` - Specific model name

**Important GPIO Pin Mapping**:

According to the hardware connection diagram in the "Hardware Preparation" section:
- **DC# PIN** (Data/Command) - Connected to Pin 11 → GPIO2_IO00 (`<&gpio2 0 GPIO_ACTIVE_HIGH>`)
- **RST# PIN** (Reset) - Connected to Pin 29 → GPIO2_IO05 (`<&gpio2 5 GPIO_ACTIVE_HIGH>`)
- **BUSY PIN** - Connected to Pin 37 → GPIO2_IO26 (`<&gpio2 26 GPIO_ACTIVE_HIGH>`)
- **MOSI** - Connected to Pin 19 → LPSPI3_SOUT (GPIO_IO10)
- **MISO** - Connected to Pin 21 → LPSPI3_SIN (GPIO_IO09)
- **SCK** - Connected to Pin 23 → LPSPI3_SCK (GPIO_IO11)
- **CS** - Connected to Pin 24 → GPIO2_IO08 (software controlled)
- **GND** - Connected to Pin 39
- **3.3V** - Connected to Pin 17

**Note**: The above example uses LPSPI3 which is available on the 40-pin header. If your hardware uses different GPIO pins or a different SPI bus, adjust the configuration accordingly. You can verify the pin mapping by checking the FRDM-IMX93 board schematic and the i.MX93 reference manual.

### Step 4. Update Kernel Configuration (defconfig)

Enable the PIXPAPER-426M driver in your kernel configuration. You can either:

**Option A: Manual configuration**
```bash
make menuconfig
```
Then navigate to:
```
Device Drivers --->
  Graphics support --->
    <M> DRM support for PIXPAPER426M display panels
```

**Option B: Modify defconfig directly**

Edit your board's defconfig file (e.g., `arch/arm64/configs/imx_v8_defconfig`) and add:

```
CONFIG_TINYDRM_PIXPAPER426M=m
```

Or build as built-in (y instead of m):
```
CONFIG_TINYDRM_PIXPAPER426M=y
```

Save the configuration:
```bash
make savedefconfig
cp defconfig arch/arm64/configs/imx_v8_defconfig
```

### Step 5. Build the Kernel

Compile the kernel with your updated configuration:

```bash
# For cross-compilation (on x86_64 host):
export ARCH=arm64
export CROSS_COMPILE=aarch64-linux-gnu-

make imx_v8_defconfig
make -j$(nproc) Image dtbs modules

# For native compilation (on ARM64 board):
make imx_v8_defconfig
make -j$(nproc) Image dtbs modules
```

### Step 6. Install Kernel and Modules

**If building on host machine**, copy the compiled files to your FRDM-IMX93:

```bash
# Copy kernel image
sudo cp arch/arm64/boot/Image /path/to/boot/partition/

# Copy device tree blob
sudo cp arch/arm64/boot/dts/freescale/imx93-11x11-evk.dtb /path/to/boot/partition/

# Install modules
sudo make INSTALL_MOD_PATH=/path/to/rootfs modules_install
```

**If building natively on the board**:

```bash
sudo make modules_install
sudo cp arch/arm64/boot/Image /boot/
sudo cp arch/arm64/boot/dts/freescale/imx93-11x11-evk.dtb /boot/
```

### Step 7. Reboot and Verify

Reboot your FRDM-IMX93 board:

```bash
sudo reboot
```

After reboot, verify the driver is loaded:

```bash
# Check if the driver module is loaded
lsmod | grep pixpaper

# Check DRM device
ls -l /dev/dri/

# Check kernel messages
dmesg | grep pixpaper
```

You should see the DRM device (e.g., `/dev/dri/card0` or `/dev/dri/card1`) and kernel messages indicating successful driver initialization.

### Step 8. Test the Display

You can test the display using standard DRM/KMS tools:

```bash
# Install modetest utility (if not already installed)
sudo apt install libdrm-tests

# List available connectors and modes
modetest -M pixpaper

# Display a test pattern
modetest -M pixpaper -s <connector_id>:800x480
```

Expection results: <br>

https://github.com/user-attachments/assets/a5192a41-dba7-4fbe-bb49-bd246300b544






## Contributors

Thanks goes to these wonderful people from open source community:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
        <td align="center" valign="top" width="14.28%"><a href="https://github.com/wigcheng"><img src="https://avatars.githubusercontent.com/u/7148592?v=4" width="100px;" alt="Wig Cheng"/><br /><sub><b>Wig Cheng</b></sub></a><br /><a href="https://github.com/wigcheng/open-epd/commits?author=wigcheng" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

---
