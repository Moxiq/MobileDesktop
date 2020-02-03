import numpy as np
import cv2
import mss
import mss.tools

class Capture:

    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.left_padding = 500
        self.top_padding = 500

    def get_screen_image(self):
        recording_box = {'top': self.top_padding, 'left': self.left_padding, 'width': self.width, 'height': self.height}

        with mss.mss() as sct:
            sct_img = sct.grab(recording_box)
            # Return as jpg image in bytes
            return mss.tools.to_png(sct_img.rgb, sct_img.size)

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
