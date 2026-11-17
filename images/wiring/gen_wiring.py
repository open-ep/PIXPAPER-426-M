#!/usr/bin/env python3
"""Generate the per-board wiring diagrams (SVG) used by the guides.

Run:  python3 gen_wiring.py      (writes *.svg next to this file)
Edit the BOARDS table below if a pin assignment changes.
"""
from pathlib import Path

# One colour per panel signal, same in every diagram.
SIG = {
    "3V3":  "#d62728", "GND":  "#222222", "MOSI": "#1f77b4", "SCK": "#ff7f0e",
    "CS#":  "#9467bd", "DC#":  "#2ca02c", "RST#": "#8c564b", "BUSY": "#e377c2",
}
PANEL = Path(__file__).resolve().parents[2].name   # repo name, e.g. PIXPAPER-213-C
PANEL_ORDER = ["3V3", "GND", "MOSI", "SCK", "CS#", "DC#", "RST#", "BUSY"]


def h2x(n):  # standard 2-row header: (1,2) (3,4) ...
    return [(2 * i - 1, 2 * i) for i in range(1, n + 1)]


def pico():  # Pico footprint: 1..20 down the left, 40..21 down the right
    return [(i, 41 - i) for i in range(1, 21)]


# pins: {header_pin: (signal, note)}
BOARDS = {
    "rpi2": ("Raspberry Pi 2 — 40-pin header", [
        ("J8", h2x(20), {1: ("3V3", "3.3 V"), 9: ("GND", ""), 19: ("MOSI", "GPIO10"),
                         23: ("SCK", "GPIO11"), 24: ("CS#", "GPIO8 / CE0"),
                         16: ("DC#", "GPIO23"), 18: ("RST#", "GPIO24"), 22: ("BUSY", "GPIO25")})]),
    "d3g": ("TOPST D3-G — 40-pin GPIO_HEADER", [
        ("JH1", h2x(20), {1: ("3V3", "3.3 V"), 9: ("GND", ""), 19: ("MOSI", "GPIO_C02 / SPI0 MOSI"),
                          23: ("SCK", "GPIO_C00 / SPI0 SCLK"), 24: ("CS#", "GPIO_C01 / SPI0 CS0"),
                          29: ("DC#", "GPIO_G01 (gpiochip4 line 1)"), 31: ("RST#", "GPIO_G02 (gpiochip4 line 2)"),
                          37: ("BUSY", "GPIO_G06 (gpiochip4 line 6)")})]),
    "frdm-imx93": ("NXP FRDM-IMX93 — 40-pin header P11", [
        ("P11", h2x(20), {1: ("3V3", "3.3 V"), 9: ("GND", ""), 19: ("MOSI", "LPSPI3 SOUT"),
                          23: ("SCK", "LPSPI3 SCK"), 24: ("CS#", "LPSPI3 PCS0"),
                          27: ("DC#", "GPIO2_IO00"), 29: ("RST#", "GPIO2_IO05"),
                          37: ("BUSY", "GPIO2_IO26")})]),
    "kakip": ("Kakip (RZ/V2H) — 40-pin header CN6", [
        ("CN6", h2x(20), {1: ("3V3", "3.3 V"), 9: ("GND", ""), 19: ("MOSI", "P9_0 RSPI0 MOSI"),
                          23: ("SCK", "P9_2 RSPI0 RSPCK"), 24: ("CS#", "P9_3 RSPI0 SSL0"),
                          29: ("DC#", "P7_4  (gpio 60)"), 31: ("RST#", "P10_7 (gpio 87)"),
                          37: ("BUSY", "P11_3 (gpio 91)")})]),
    "kakip-cm33": ("Kakip (RZ/V2H) Cortex-M33 — Zephyr, 40-pin header CN6", [
        ("CN6", h2x(20), {1: ("3V3", "3.3 V"), 9: ("GND", ""), 19: ("MOSI", "P9_0 RSPI0 MOSI"),
                          23: ("SCK", "P9_2 RSPI0 RSPCK"), 24: ("CS#", "P9_3"),
                          29: ("DC#", "P7_4"), 31: ("RST#", "P10_7"), 37: ("BUSY", "P11_3")})]),
    "rpi-pico": ("Raspberry Pi Pico / Pico 2 (top view, USB up)", [
        ("Pico", pico(), {36: ("3V3", "3V3(OUT)"), 23: ("GND", ""), 25: ("MOSI", "GP19"),
                          24: ("SCK", "GP18"), 22: ("CS#", "GP17"), 21: ("DC#", "GP16"),
                          26: ("RST#", "GP20"), 27: ("BUSY", "GP21")})]),
    "w6300-evb-pico2": ("W6300-EVB-Pico2 / Pico 2 — Zephyr (top view, USB up)", [
        ("Pico", pico(), {36: ("3V3", "3V3(OUT)"), 8: ("GND", ""), 4: ("SCK", "GP2"),
                          5: ("MOSI", "GP3"), 6: ("CS#", "GP4"), 7: ("DC#", "GP5"),
                          9: ("RST#", "GP6"), 10: ("BUSY", "GP7")})]),
    "milkv-duo256m": ("Milk-V Duo256M (top view, USB up)", [
        ("Duo256M", pico(), {36: ("3V3", "3V3(OUT)"), 3: ("GND", ""), 9: ("SCK", "GP6 / SPI2 SCK"),
                             10: ("MOSI", "GP7 / SPI2 SDO"), 12: ("CS#", "GP9 / SPI2 CS"),
                             24: ("DC#", "GP18 (gpiochip0 line 22)"), 22: ("RST#", "GP17 (line 24)"),
                             21: ("BUSY", "GP16 (line 23)")})]),
    "panzer-plus": ("PANZER-PLUS (i.MX8MP) — JP2 + JP3, after rework", [
        ("JP2 (SPI)", h2x(3), {1: ("3V3", "3.3 V wire (rework)"), 2: ("SCK", "ECSPI1 SCLK"),
                               3: ("CS#", "GPIO5_IO09"), 4: ("MOSI", "ECSPI1 MOSI"), 6: ("GND", "")}),
        ("JP3 (GPIO)", h2x(4), {4: ("BUSY", "EXT_GPIO4"), 6: ("RST#", "EXT_GPIO6"),
                                8: ("DC#", "EXT_GPIO8")})]),
}

ROW, PIN_R, W = 26, 8, 860
FONT = 'font-family="Helvetica,Arial,sans-serif"'


def svg_board(title, headers):
    out, y = [], 24
    out.append(f'<text x="{W/2}" y="{y}" text-anchor="middle" font-size="20" font-weight="bold" {FONT}>{title}</text>')
    # panel connector strip
    y += 22
    out.append(f'<text x="{W/2}" y="{y+4}" text-anchor="middle" font-size="13" fill="#555" {FONT}>'
               f'{PANEL} connector (as printed on the label, left → right)</text>')
    y += 12
    bw = 84
    x0 = (W - bw * 8) / 2
    for i, s in enumerate(PANEL_ORDER):
        out.append(f'<rect x="{x0+i*bw+2}" y="{y}" width="{bw-4}" height="28" rx="4" fill="{SIG[s]}"/>'
                   f'<text x="{x0+i*bw+bw/2}" y="{y+19}" text-anchor="middle" font-size="14" font-weight="bold" fill="#fff" {FONT}>{s}</text>')
    y += 60
    for name, rows, pins in headers:
        # Pico-style module: pads on the two long edges of the board, USB on top
        edge = rows == pico()
        cx_l, cx_r = (W / 2 - 80, W / 2 + 80) if edge else (W / 2 - 18, W / 2 + 18)
        out.append(f'<text x="{W/2}" y="{y}" text-anchor="middle" font-size="16" font-weight="bold" {FONT}>{name}</text>')
        y += 14
        if edge:
            out.append(f'<rect x="{W/2-34}" y="{y}" width="68" height="30" rx="5" fill="#c9c9c9" stroke="#777"/>'
                       f'<text x="{W/2}" y="{y+20}" text-anchor="middle" font-size="13" font-weight="bold" fill="#333" {FONT}>USB</text>')
            y += 22
        top = y
        if edge:
            out.append(f'<rect x="{cx_l-14}" y="{top}" width="{cx_r-cx_l+28}" height="{len(rows)*ROW+8}" rx="10" fill="#e3efe3" stroke="#6a9a6a" stroke-width="2"/>')
        else:
            out.append(f'<rect x="{cx_l-16}" y="{top}" width="{cx_r-cx_l+32}" height="{len(rows)*ROW+8}" rx="6" fill="#f2f2f2" stroke="#999"/>')
        for r, (lp, rp) in enumerate(rows):
            cy = top + 4 + ROW / 2 + r * ROW
            for p, cx, side in ((lp, cx_l, -1), (rp, cx_r, 1)):
                used = pins.get(p)
                fill = SIG[used[0]] if used else "#fff"
                if p == 1:
                    out.append(f'<rect x="{cx-PIN_R}" y="{cy-PIN_R}" width="{2*PIN_R}" height="{2*PIN_R}" fill="{fill}" stroke="#333"/>')
                else:
                    out.append(f'<circle cx="{cx}" cy="{cy}" r="{PIN_R}" fill="{fill}" stroke="#333"/>')
                nx = cx - side * 16 if edge else cx + side * 30   # edge boards: number inside the board
                anchor = "end" if side < 0 else "start"
                if used:
                    sig, note = used
                    lx = cx + side * (30 if edge else 62)
                    lw = 250
                    rx = lx - lw if side < 0 else lx
                    out.append(f'<line x1="{cx+side*PIN_R}" y1="{cy}" x2="{lx}" y2="{cy}" stroke="{SIG[sig]}" stroke-width="3"/>')
                    out.append(f'<rect x="{rx}" y="{cy-11}" width="{lw}" height="22" rx="4" fill="{SIG[sig]}"/>')
                    label = f'{sig}' + (f'  ·  {note}' if note else '')
                    tx = rx + (lw - 8 if side < 0 else 8)
                    out.append(f'<text x="{tx}" y="{cy+5}" text-anchor="{anchor}" font-size="13" font-weight="bold" fill="#fff" {FONT}>{label}</text>')
                # pin number on a white chip so the wire doesn't cross it
                bx = nx - 22 if side < 0 else nx - 2
                if used and not edge:
                    out.append(f'<rect x="{bx}" y="{cy-9}" width="24" height="18" fill="#fff"/>')
                weight, colr = ("bold", "#000") if used else ("normal", "#888")
                nanchor = ("start" if side < 0 else "end") if edge else anchor
                out.append(f'<text x="{nx}" y="{cy+5}" text-anchor="{nanchor}" font-size="13" font-weight="{weight}" fill="{colr}" {FONT}>{p}</text>')
        y = top + len(rows) * ROW + 44
    out.append(f'<text x="{W/2}" y="{y-14}" text-anchor="middle" font-size="12" fill="#555" {FONT}>'
               '■ = pin 1.  Only the coloured pins are used. Panel is 3.3 V only — never connect it to 5 V.</text>')
    h = y
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}">'
            f'<rect width="{W}" height="{h}" fill="#fff"/>' + "".join(out) + "</svg>\n")


if __name__ == "__main__":
    import sys
    here = Path(__file__).parent
    only = sys.argv[1:] or ['d3g', 'frdm-imx93', 'kakip-cm33']   # boards used by this repo's guides
    for key, (title, headers) in BOARDS.items():
        if only and key not in only:
            continue
        (here / f"{key}.svg").write_text(svg_board(title, headers))
        print("wrote", key + ".svg")
