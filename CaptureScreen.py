import numpy as np
import cv2
import mss
import mss.tools
import PIL.Image
from io import BytesIO, StringIO


class Capture:

    def __init__(self, quality=50, width=1920, height=1080, left_pad=0, right_pad=0):
        # Quality is an integer between 0-100
        self.quality = quality
        self.width = width
        self.height = height
        self.left_padding = left_pad
        self.top_padding = right_pad

    def get_screen_image(self):
        recording_box = {'top': self.top_padding, 'left': self.left_padding, 'width': self.width, 'height': self.height}

        with mss.mss() as sct:
            # sct.compression_level = 1
            sct_img = sct.grab(recording_box)
            img = PIL.Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

            with BytesIO() as f:
                img.save(f, format='JPEG', quality=self.quality)
                return f.getvalue()

    def show_local_stream(self):
        recording_box = {'top': self.top_padding, 'left': self.left_padding, 'width': self.width, 'height': self.height}
        sct = mss.mss()

        while 1:

            sct_img = sct.grab(recording_box)
            cv2.imshow('screen', np.array(sct_img))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


if __name__ == '__main__':
    Capture().show_local_stream()
