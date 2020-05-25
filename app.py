#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
from camera_index import Cam_index

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_opencv import Camera


app = Flask(__name__)


# @app.route('/')
# def index():
#     """Video streaming home page."""
#     return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed/<string:id>')
def video_feed(id):
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera(Cam_index.get(id))),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='192.168.4.120', threaded=True, debug=False)
    # app.run(host='192.168.4.2', threaded=True, debug=False)
