#!/usr/bin/env python3
"""Draw the 23 Nov 2026 world-news front page, 1024x1024 PNG.
Headlines verified 2026-11-24 morning: COP31 (UN News/CNN),
Kyiv/Dymer toll (Kyiv Post/Ukrinform, 11 dead in Dymer, 15+ region),
Chapo Isidro capture + Nov 23 extradition order (Reuters/Al Jazeera),
Korea minister resignation Nov 22 (Yonhap), FIFA hosts (FIFA.com).
Other items as in news-image-brief.md (2026-11-24 00:35 scan)."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK, RED, GREY = (16, 16, 16), (178, 34, 34), (90, 90, 90)

def wrap(text, f, width):
    lines = []
    for para in text.split("\n"):
        lines += textwrap.wrap(para, width=width,
                               break_long_words=False, break_on_hyphens=False) or [""]
    return lines

def text_block(x, y, w, lines, f, fill=BLACK, leading=1.28):
    for ln in lines:
        d.text((x, y), ln, font=f, fill=fill)
        y += int(f.size * leading)
    return y

def box(x, y, w, h, kicker, head, body, head_size=34, body_size=21, head_width=26):
    d.rectangle([x, y, x + w, y + h], outline=(200, 200, 200), width=2)
    pad = 16
    yy = y + pad
    d.text((x + pad, yy), kicker, font=font(SANS_B, 17), fill=RED)
    yy += 28
    yy = text_block(x + pad, yy, w - 2 * pad,
                    wrap(head, font(SANS_B, head_size), head_width),
                    font(SANS_B, head_size), leading=1.12)
    yy += 6
    text_block(x + pad, yy, w - 2 * pad,
               wrap(body, font(SANS, body_size), (w - 2 * pad) // (body_size * 0.52)),
               font(SANS, body_size), fill=(40, 40, 40))

# Masthead
d.text((32, 22), "THE WORLD IN ONE DAY", font=font(SERIF_B, 62), fill=BLACK)
d.text((32, 96), "MONDAY, 23 NOVEMBER 2026", font=font(SANS_B, 30), fill=RED)
d.line([(32, 142), (992, 142)], fill=BLACK, width=4)
d.line([(32, 150), (992, 150)], fill=RED, width=2)

# Lead row
box(32, 168, 476, 300, "CLIMATE  •  ANTALYA",
    "COP31 collapses: no deal",
    "Antalya talks end with no climate pact — the longest COP on record. The EU and about 130 nations reject a text that never mentions fossil fuels. UN chief Guterres: “deeply disappointed.” Next: COP32 in Addis Ababa.",
    head_size=36, head_width=22)
box(516, 168, 476, 300, "WAR  •  UKRAINE",
    "Kyiv region: at least 15 killed",
    "A Russian drone flattens a five-storey block in Dymer, killing 11, including an 11-year-old girl. A 7-year-old boy and a 79-year-old woman are pulled alive from the rubble. A supermarket strike in Vyshneve kills three more.",
    head_size=36, head_width=22)

# Middle row (3 columns)
y2, h2, cw = 484, 228, 304
box(32, y2, cw, h2, "IRAN  •  WASHINGTON",
    "Trump leans to new Iran strikes",
    "President says talks failed and leans to resuming strikes after the New Year. Tehran vows to answer any US naval blockade.",
    head_size=27, head_width=17, body_size=19)
box(360, y2, cw, h2, "USA  •  MIDTERMS",
    "Democrats lock the House",
    "At least 258 seats — the party’s biggest House majority since 1992. The 2028 race is already under way.",
    head_size=27, head_width=17, body_size=19)
box(688, y2, cw, h2, "MEXICO  •  SINALOA",
    "“Chapo Isidro” captured",
    "Army special forces seize FBI most-wanted boss Fausto Isidro Meza Flores in Guasave. US extradition order confirmed on Monday.",
    head_size=27, head_width=17, body_size=19)

# Bottom row (3 columns)
y3, h3 = 728, 232
box(32, y3, cw, h3, "SUDAN  •  KHARTOUM",
    "Drone hits homes, UN building",
    "Drone attack strikes a Khartoum residential area and a United Nations building.",
    head_size=24, head_width=17, body_size=18)
box(360, y3, cw, h3, "SOUTH KOREA  •  SEOUL",
    "Minister quits over AI exam row",
    "Education chief Choi Kyo-jin resigns after last-minute anti-AI rules sow chaos at the college entrance exam.",
    head_size=24, head_width=17, body_size=18)
box(688, y3, cw, h3, "SPORT  •  ZURICH",
    "2031 Women’s World Cup",
    "FIFA appoints the USA, Mexico, Costa Rica and Jamaica for 2031 — first 48-team edition. UK gets 2035.",
    head_size=24, head_width=17, body_size=18)

d.line([(32, 972), (992, 972)], fill=BLACK, width=2)
d.text((32, 982), "Eight stories from Monday 23 November 2026  •  Climate  •  War  •  Politics  •  Crime  •  Sport",
       font=font(SANS, 17), fill=GREY)

img.save("/home/hatch/workspace/makefun/entry-news-image/entry.png", optimize=True)
print("saved", img.size)
import os
print("bytes:", os.path.getsize("/home/hatch/workspace/makefun/entry-news-image/entry.png"))
