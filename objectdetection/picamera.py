import picamera
import picamera.array

class PiCamera2(object):
    """Class for the pi camera"""

    def __init__(self, width, height):
        print "Camera from Raspberry Pi used..."
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.width, self.height)
        self.stream = picamera.array.PiRGBArray(self.camera)

    def capture(self):
        """Return an image from the picamera."""
        self.stream.truncate(0)
        self.camera.capture(self.stream, format='bgr', use_video_port=True)
        img = self.stream.array
        return img
