# https://realpython.com/face-recognition-with-python/
# https://realpython.com/traditional-face-detection-python/

import cv2 as cv
from PIL import Image


class Resolution:
    def __init__(self, image):
        self.image = image

    def resize(self, quality):
        im = Image.open(self.image)
        im.save(self.image, quality=quality)

if __name__ == '__main__':
    Resolution('images/family.jpg').resize(25)
