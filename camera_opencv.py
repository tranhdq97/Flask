import os
import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):

    def frames(self):
        camera = cv2.VideoCapture(self.video_source_set)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
