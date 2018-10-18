import os
from PIL import Image, ImageFont, ImageDraw


class CharPainting:
    def __init__(self, string: str, width: int, height: int):
        """
        """
        self.string = string
        self.w = width
        self.h = height

    def print_painting_char(self):
        #
        im = Image.new("RGB", (self.w, self.h), (255, 255, 255))
        dr = ImageDraw.Draw(im)
        font = ImageFont.truetype(os.path.join("fonts", "DejaVuSans.ttf"), 40)

        dr.text((10, 5), self.string, font=font, fill="#000000")
        im.show()
        return True


if __name__ == "__main__":
    #
    text = "this is a test"
    cp = CharPainting(text, 300, 50)
    status = cp.print_painting_char()
