# Open-EP Text Sender — User Guide

`epaper_text_sender.html` is a browser-based tool for sending text to a **PixPaper EPD** (e-paper display) over a serial connection. It builds the correct `text_renderer` command for you, previews how the text will look on the screen, and can send the command straight to the board using the **Web Serial API** — no terminal required.

---

## 1. Requirements

| Item | Requirement |
|------|-------------|
| **Browser** | Desktop **Chrome** or **Edge** (Web Serial API support). Firefox and Safari are *not* supported for direct sending. |
| **Board** | A target board running the `text_renderer` binary (e.g. NXP i.MX93 FRDM, Renesas RZ/V2H "Kakip") connected to a PixPaper e-paper panel. |
| **Connection** | A USB-to-serial (UART) link between your computer and the board. |
| **Font file** | `NotoSansCJK-Bold.ttc` (or another font) present on the board next to `text_renderer`. |
| **Internet** | Only needed once, so the page can load its web fonts. The tool itself runs fully in the browser. |

> If your browser does not support Web Serial, the tool still works as a **command generator** — you can copy the command and paste it into your own serial terminal manually.

---

## 2. Open the tool

1. Make sure the `text_renderer` binary and your font file already exist on the board.
2. Double-click `epaper_text_sender.html`, or open it in Chrome/Edge via **File → Open**.
3. If you see a red banner saying *"Your browser does not support the Web Serial API"*, switch to desktop Chrome or Edge, or use the **Copy Command** workflow (Section 7).

---

## 3. Enter your text

- Type or paste your message into the large **Display Text** box on the left.
- Press **Enter** to create new lines.
- CJK and multilingual text (Chinese / Japanese / Korean) is fully supported.
- The **E-Paper Preview** on the right updates live so you can see roughly how it will appear on the 800 × 480 panel.

You can also click one of the **Quick Examples** buttons to load a ready-made demo:

- 📋 iMX93 FRDM — Multilingual Demo
- 📋 Kernel Evolution (Japanese)
- 📋 Kernel Development (Korean)
- 📋 Open-EP Intro (Chinese)

---

## 4. Set the renderer parameters

Under **text_renderer Parameters**, adjust the values to match your panel and font:

| Field | Flag | Default | Meaning |
|-------|------|---------|---------|
| **Width**  | `-w` | `800` | Screen width in pixels |
| **Height** | `-h` | `480` | Screen height in pixels |
| **Font Size** | `-s` | `30` | Text size in pixels |
| **Format** | `--format` | `rgba` | Pixel format: `rgba`, `rgb`, or `gray` |
| **Font** | `-f` | `./NotoSansCJK-Bold.ttc` | Path to the font file **on the board** |
| **Output** | `-o` | `/dev/fb0` | Framebuffer device **on the board** |

> The **Font** and **Output** paths refer to locations on the target board, not on your computer.

As you change these, the **Generated Command** box shows the exact command that will be run, for example:

```
$ ./text_renderer -t "Hello World" -f ./NotoSansCJK-Bold.ttc -w 800 -h 480 -s 30 --format rgba -o /dev/fb0
```

---

## 5. Configure the serial connection

Under **Serial Connection**:

- **Baud Rate** — must match the board's serial console (default **115200**).
- **Line Ending** — the character sent after the command:
  - `LF (\n)` — default, works for most Linux shells
  - `CRLF (\r\n)`
  - `CR (\r)`

---

## 6. Connect and send (Web Serial workflow)

1. Click **⎈ Connect Serial**.
2. In the browser pop-up, choose the serial port for your board and confirm.
3. When connected, the status badge in the top-right turns to **Connected** with a green dot, and the log shows `Serial connected`.
4. Click **▶ Send to Board** (or press **Ctrl+Enter**).
5. The command is transmitted over serial; the board runs `text_renderer` and the text appears on the e-paper display.
6. Any output the board sends back appears in the **Communication Log** at the bottom (prefixed with `←`).
7. When finished, click **⏻ Disconnect** to release the serial port.

> **Note:** The board must already be at a shell prompt where it can execute `text_renderer`. The tool sends the command line as typed text into that shell.

---

## 7. Copy Command workflow (no Web Serial)

If you prefer your own terminal, or your browser lacks Web Serial:

1. Build your text and parameters as above.
2. Click **⧉ Copy Command** (or press **Ctrl+Shift+C**).
3. Paste the command into your own serial terminal (e.g. `minicom`, `picocom`, `screen`, PuTTY) that is connected to the board.
4. Press Enter to run it.

---

## 8. Buttons & shortcuts

| Control | Action |
|---------|--------|
| **⎈ Connect Serial / ⏻ Disconnect** | Open or close the serial port |
| **▶ Send to Board** | Send the generated command over serial |
| **⧉ Copy Command** | Copy the generated command to the clipboard |
| **✕ Clear** | Clear the text box |
| **Ctrl+Enter** | Send command |
| **Ctrl+Shift+C** | Copy command |

---

## 9. Troubleshooting

| Symptom | Cause / Fix |
|---------|-------------|
| Red "Web Serial not supported" banner | Use desktop Chrome or Edge, or use the Copy Command workflow. |
| No serial port appears in the pop-up | Check the USB cable and drivers; make sure no other program (terminal, IDE monitor) is holding the port. |
| `Send failed` in the log | The port may have been disconnected. Click Disconnect, then Connect again. |
| Command sent but nothing on screen | Verify the board is at a shell prompt, the `text_renderer` binary and font path exist, and the `-o` framebuffer device (`/dev/fb0`) is correct. |
| Garbled characters on the panel | Confirm the **Font** file supports your language and the **Baud Rate** matches the board. |
| Text is clipped on the display | Reduce the **Font Size** (`-s`) or shorten the text so it fits the **Width × Height**. |

---

## 10. Quick start (TL;DR)

1. Open `epaper_text_sender.html` in **Chrome/Edge**.
2. Type your text.
3. Check Width / Height / Font Size / Font / Output match your board.
4. Set **Baud Rate** to **115200**.
5. Click **Connect Serial** → pick the port.
6. Click **Send to Board** (or **Ctrl+Enter**).
7. Watch the text appear on the PixPaper e-paper display. ✅
