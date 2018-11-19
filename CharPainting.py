import os
import cv2
import numpy as np
from osgeo import gdalnumeric
from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt


class CharPainting:
    def __init__(self, string: str, width: int, height: int):
        """
        """
        self.string = string
        self.w = width
        self.h = height

    def set_chars(self, charlist: list):
        self.charlist = charlist

    def image_to_array_byte(self, i: Image) -> np.ndarray:
        """
        Converts a Python Imaging Library array to a
        gdalnumeric image.
        """
        a = np.array(i)
        # a = np.array(i.im.size[0], i.im.size[1])
        # for h in i.im.size[0]:
        #     for w in i.im.size[1]:
        #         a[h,w] = i.im.

        # a = gdalnumeric.fromstring(i.tobytes(), dtype=np.int8)
        # a.shape = i.im.size[1], i.im.size[0], 3
        return a

    def print_painting_char(self):
        #
        im = Image.new("RGB", (self.w, self.h), (255, 255, 255))
        dr = ImageDraw.Draw(im)
        font = ImageFont.truetype(os.path.join("fonts", "DejaVuSans.ttf"), 45)

        dr.text((0, 0), self.string, font=font, fill="#000000")
        im.show()

        imarr = self.image_to_array_byte(im)
        w, h, b = imarr.shape
        imarr = imarr[:, :, 0].reshape(w, h)

        # setting kernel
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        # imarr = cv2.erode(imarr, kernel)

        plt.figure(num="test", figsize=(8, 8))  # image show part
        plt.imshow(imarr)
        plt.show()  # image show part end

        return True


if __name__ == "__main__":
    #
    text = "ABCD"
    text = text.upper()
    nchars = len(text)
    cp = CharPainting(text, nchars * 33, 50)
    cp.set_chars([".", "@"])
    status = cp.print_painting_char()
