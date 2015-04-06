import cv2
import sys

class ImageCamera(object):
    """Class for capturing an image from the webcam"""

    __counter = 0

    def __init__(self, width, height):
        print "Image used..."
        self.__img = cv2.imread('img/1.jpg')

    def capture(self):
        """Return an image from the webcam."""
        if self.__counter == 0:
            self.__counter = self.__counter + 1 
            print "Returning first image."
            return cv2.imread('img/1m.jpg')
        else:
            return self.__img
