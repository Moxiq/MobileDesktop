#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from CaptureScreen import Capture

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def mjpeg_generator(boundary, source):
    """
    For mjpeg
    """

    hdr = '--%s\r\nContent-Type: image/jpeg\r\n' % boundary

    prefix = ''
    while True:
        frame = source.get_screen_image()
        msg = prefix + hdr + 'Content-Length: %d\r\n\r\n' % len(frame)
        yield msg.encode('utf-8') + frame
        prefix = '\r\n'


def gen(capture):
    """Video streaming generator function."""
    while True:
        frame = capture.get_screen_image()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(mjpeg_generator('frame', Capture(40, 2560, 1440, 0, 0)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='192.168.0.34', port=5000)
