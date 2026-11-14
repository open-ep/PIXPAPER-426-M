[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

# PIXPAPER-426-M on TOPST D3-G — Linux

| Item | Value |
|---|---|
| Board | [TOPST D3-G](https://topst.ai/product/g/d3) (Telechips Dolphin 3M) |
| Tested | kernel 5.10 |
| Interface | `/dev/spidev0.0` + 3 GPIOs on `gpiochip4` |
| Demo source | [pixpaper-426-m-test-topst-d3-g.c](https://github.com/open-ep/linux-user-space-examples/blob/master/4.26/mono/spi/pixpaper-426-m-test-topst-d3-g.c) |

## 1. Wiring

Power the board off before wiring. The panel is **3.3 V only** — never use a 5 V pin.

<img src="images/wiring/d3g.svg" width="640" alt="TOPST D3-G wiring">

| Panel | JH1 pin | SoC signal |
|---|---|---|
| 3V3 | 1 | 3.3 V |
| GND | 9 (any GND) | GND |
| MOSI | 19 | GPIO_C02 / SPI0 MOSI |
| SCK | 23 | GPIO_C00 / SPI0 SCLK |
| CS# | 24 | GPIO_C01 / SPI0 CS0 |
| DC# | 29 | GPIO_G01 (gpiochip4 line 1) |
| RST# | 31 | GPIO_G02 (gpiochip4 line 2) |
| BUSY | 37 | GPIO_G06 (gpiochip4 line 6) |

<details><summary>Photo of a finished setup</summary>

<img width="640" alt="photo" src="https://github.com/user-attachments/assets/e91b0785-4cf3-4493-a628-4615d0fd2921" />
</details>

## 2. Enable SPI

Nothing to do — the stock image already provides the SPI device.

**Check:** `ls /dev/spidev0.0` prints `/dev/spidev0.0`.

## 3. Build and run the demo

> Needs **libgpiod 1.x** — check with `gpioinfo --version` (must say `v1.x`).

> Yocto image: add `IMAGE_INSTALL:append = " libgpiod libgpiod-dev libgpiod-tools packagegroup-core-buildessential"` to `conf/local.conf`, rebuild, then run the commands below on the board (skip the `apt` line).

```bash
sudo apt install -y gcc wget gpiod libgpiod-dev
mkdir -p ~/pixpaper-426m && cd ~/pixpaper-426m
BASE=https://raw.githubusercontent.com/open-ep/linux-user-space-examples/master/4.26/mono/spi
wget $BASE/pixpaper-426-m-test-topst-d3-g.c $BASE/image_output.h
gcc -o epd_test pixpaper-426-m-test-topst-d3-g.c -lgpiod
sudo ./epd_test
```

## 4. Expected result

The panel does a full refresh (it flashes) and shows the sample picture, then redraws it every 20 s until you press **Ctrl+C**.

https://github.com/user-attachments/assets/363a832f-cdcd-42d9-8cab-356c27faebf7

## 5. Show your own picture

```bash
sudo apt install -y python3-opencv
wget $BASE/png2bit_426.py
python3 png2bit_426.py your_image.png --mode mono     # → image_output.h
gcc -o epd_test pixpaper-426-m-test-topst-d3-g.c -lgpiod && sudo ./epd_test
```

This demo is **mono only**. `png2bit_426.py` resizes any PNG to 800 × 480 (landscape) and always writes `image_output.h` (`-o` is ignored).

## Troubleshooting

| Symptom | Fix |
|---|---|
| `/dev/spidev0.0` missing | SPI is not enabled → redo step 2 and reboot. |
| Compile error `implicit declaration of function 'gpiod_chip_open_by_name'` | Your OS has libgpiod 2.x; this demo needs 1.x (`gpioinfo --version`). |
| `Failed to request GPIO` / line busy | Another driver owns gpiochip4 lines 1/2/6. `gpioinfo gpiochip4` shows the user. If you rewire, edit `EPD_DC_PIN` / `EPD_RST_PIN` / `EPD_BUSY_PIN` in the `.c`. |
| Runs, but the screen never changes | Check 3V3 and GND first, then that MOSI and SCK are not swapped. |
| Hangs at 100 % CPU, no flashing | BUSY or RST# wire is loose. |

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

