# news-image-20261124 — poster for Tuesday 24 November 2026.
# Draws one 1024x1024 PNG with PIL only: no network, no clock, no
# randomness, so two runs write byte-identical files. Six stories that
# were first reported in the 24 November 2026 news cycle, each checked
# against its source on 24 Nov 2026 (AP, Meduza/Mediazona, US BIS,
# European Commission, Indonesian officials via AP/Xinhua).
#
# Run:  python3 draw.py        (writes entry.png next to this file)

import hashlib
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT = HERE / "entry.png"

W, H = 1024, 1024
BG = (13, 22, 38)          # deep navy
PANEL = (24, 36, 58)       # card navy
PANEL_EDGE = (58, 82, 122)
INK = (240, 244, 250)      # near-white text
MUTED = (168, 184, 205)    # grey-blue secondary text
GOLD = (232, 184, 84)      # masthead rule + date
RED = (224, 82, 82)
TEAL = (64, 190, 178)
BLUE = (96, 150, 235)
GREEN = (110, 196, 110)
ORANGE = (235, 150, 64)
VIOLET = (168, 130, 220)

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")


def font(name, size):
    return ImageFont.truetype(str(FONT_DIR / name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 58)
F_DATE = font("DejaVuSans-Bold.ttf", 27)
F_TAG = font("DejaVuSans-Bold.ttf", 21)
F_HEAD = font("DejaVuSans-Bold.ttf", 27)
F_BODY = font("DejaVuSans.ttf", 21)
F_FOOT = font("DejaVuSans.ttf", 19)

# (tag, tag colour, headline, body, source line)
STORIES = [
    (
        "INDONESIA",
        RED,
        "Factory fire toll: 24 dead, ~30 missing",
        "Rescuers search the ruins of the Cikande candy factory.",
        "Officials via AP / Xinhua",
    ),
    (
        "UKRAINE · LIBYA",
        TEAL,
        "Kyiv sinks Russian warship off Libya",
        "Sea drones sank the corvette Merkury at Benghazi naval base, "
        "Zelenskyy says.",
        "AP",
    ),
    (
        "TECH",
        BLUE,
        "Nvidia brings back Jensen Huang",
        "The board unanimously reinstates its co-founder as CEO, "
        "11 days after he resigned.",
        "Nvidia / Morningstar",
    ),
    (
        "RUSSIA",
        ORANGE,
        "Russian war dead near 700,000",
        "Leaked Rosstat records analysed by Meduza and Mediazona put "
        "the toll far higher.",
        "Meduza / Mediazona",
    ),
    (
        "EUROPE",
        GREEN,
        "EU proposes 22nd Russia sanctions package",
        "New measures target banks, crypto platforms and Russian teams "
        "at EU events.",
        "European Commission",
    ),
    (
        "USA · CHINA",
        VIOLET,
        "US blacklists firm in Nvidia spy case",
        "Singapore-based Megaspeed and six more firms join the Entity "
        "List.",
        "US Bureau of Industry and Security",
    ),
]


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap measured in pixels; returns list of lines."""
    lines = []
    for para in text.split("\n"):
        words = para.split()
        cur = ""
        for word in words:
            trial = f"{cur} {word}".strip()
            if draw.textlength(trial, font=fnt) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
    return lines


def draw_card(draw, x, y, w, h, story):
    tag, colour, head, body, src = story
    draw.rounded_rectangle([x, y, x + w, y + h], radius=18,
                           fill=PANEL, outline=PANEL_EDGE, width=2)
    # coloured tag chip
    chip = tag
    cw = draw.textlength(chip, font=F_TAG) + 24
    draw.rounded_rectangle([x + 22, y + 20, x + 22 + cw, y + 52],
                           radius=9, fill=colour)
    draw.text((x + 34, y + 26), chip, font=F_TAG, fill=(12, 18, 30))
    # headline, up to two lines
    head_lines = wrap(draw, head, F_HEAD, w - 44)[:2]
    hy = y + 68
    for line in head_lines:
        draw.text((x + 22, hy), line, font=F_HEAD, fill=INK)
        hy += 33
    # body, up to two lines
    body_lines = wrap(draw, body, F_BODY, w - 44)[:2]
    by = hy + 8
    for line in body_lines:
        draw.text((x + 22, by), line, font=F_BODY, fill=MUTED)
        by += 27
    # source, pinned to the card bottom
    draw.text((x + 22, y + h - 34), "Source: " + src,
              font=F_FOOT, fill=(130, 148, 172))


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # --- masthead ---
    draw.text((48, 34), "THE WORLD IN ONE DAY", font=F_TITLE, fill=INK)
    draw.text((48, 108), "TUESDAY  \u00b7  24 NOVEMBER 2026",
              font=F_DATE, fill=GOLD)
    draw.line([(48, 152), (W - 48, 152)], fill=GOLD, width=4)
    draw.text((48, 164),
              "Six stories that defined the day \u2014 from Jakarta to Benghazi, "
              "Brussels to Silicon Valley.",
              font=F_FOOT, fill=MUTED)

    # --- six cards: two columns, three rows ---
    margin = 48
    gap = 20
    cw = (W - 2 * margin - gap) // 2
    ch = 236
    top = 208
    for i, story in enumerate(STORIES):
        col = i % 2
        row = i // 2
        x = margin + col * (cw + gap)
        y = top + row * (ch + gap)
        draw_card(draw, x, y, cw, ch, story)

    # --- footer ---
    fy = top + 3 * ch + 2 * gap + 22
    draw.line([(48, fy), (W - 48, fy)], fill=PANEL_EDGE, width=2)
    draw.text((48, fy + 14),
              "Checked 24 Nov 2026  \u00b7  AP \u00b7 Meduza / Mediazona \u00b7 "
              "US BIS \u00b7 European Commission",
              font=F_FOOT, fill=MUTED)
    draw.text((48, fy + 42), "make.fun  \u00b7  news-image-20261124",
              font=F_FOOT, fill=(130, 148, 172))

    img.save(OUT, format="PNG", optimize=True)
    data = OUT.read_bytes()
    print(f"wrote {OUT} {len(data)} bytes "
          f"sha256={hashlib.sha256(data).hexdigest()}")


if __name__ == "__main__":
    main()
