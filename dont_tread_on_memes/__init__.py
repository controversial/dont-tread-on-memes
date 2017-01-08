#!python3

import os

from PIL import Image, ImageDraw, ImageFont

localdir = os.path.dirname(__file__)
BLANK_FLAG = Image.open(os.path.join(localdir, "dont-tread-on-blank.png"))
LORA_FONT = ImageFont.truetype(
    os.path.join(localdir, "../fonts/Lora-Regular.ttf"), 120
)


def tread_on(caption, color="black"):
    """Caption the "Don't Tread on Me" snake with `caption`"""
    flag = BLANK_FLAG.copy()
    draw = ImageDraw.Draw(flag)

    text = caption.upper()

    font_pos = (flag.width / 2 - LORA_FONT.getsize(text)[0] / 2, 1088)

    draw.text(font_pos, text, font=LORA_FONT, fill=color)

    return flag


def dont_me(phrase, *args, **kwargs):
    """Caption the "Don't tread on me" flag with "Don't [phrase] me" """
    return tread_on("don't {} me".format(phrase), *args, **kwargs)
