#!python3

import os

from PIL import Image, ImageDraw, ImageFont

BLANK_FLAG = Image.open(
    os.path.join(os.path.dirname(__file__), "dont-tread-on-blank.png")
)


def tread_on(phrase):
    """Caption the "Don't Tread on Me" snake with `phrase`"""
    flag = BLANK_FLAG.copy()
    draw = ImageDraw.Draw(flag)
    font = ImageFont.truetype("Times New Roman", 120)

    text = "don't {} me".format(phrase).upper()

    font_pos = (flag.width / 2 - font.getsize(text)[0] / 2, 1088)

    draw.text(font_pos, text, font=font, fill="black")

    return flag
