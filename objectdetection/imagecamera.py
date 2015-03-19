import cv2
import sys

class ImageCamera(object):
    """Class for capturing an image from the webcam"""

    def __init__(self, width, height):
        print "Image used..."
        self.__img = cv2.imread('/media/win/Users/efux/Documents/dev/ipcv/Bilder/rechts.jpg')

    def capture(self):
        """Return an image from the webcam."""
        return self.__img
