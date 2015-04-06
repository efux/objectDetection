import cv2

class Webcam(object):
    """Class for capturing an image from the webcam"""

    def __init__(self, width, height):
        print "Webcam used..."
        self.width = width
        self.height = height
        self.initialize()

    def initialize(self):
        self.vid = cv2.VideoCapture(0)
        self.vid.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, self.width)
        self.vid.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, self.height)

    def capture(self):
        """Return an image from the webcam."""
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        self.vid.grab()
        ret, img = self.vid.read()
        cv2.imwrite("/tmp/test.png", img)
        return img

        
