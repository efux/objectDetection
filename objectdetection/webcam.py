import cv2

class Webcam(object):
    """Class for capturing an image from the webcam"""

    def __init__(self, width, height):
        print "Webcam used..."
        self.vid = cv2.VideoCapture(0)
        self.vid.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
        self.vid.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)

    def capture(self):
        """Return an image from the webcam."""
        return self.vid.read()

        
