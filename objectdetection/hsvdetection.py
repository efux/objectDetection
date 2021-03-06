import cv2
from objectdetection import ObjectDetection
from imageparameters import ImageParameters
from canprobability import CanProbability
import numpy as np

class HSVDetection(ObjectDetection):
    """Detect the can with the help of colors"""

    hue_min = 49
    hue_max = 186
    sat_min = 4
    sat_max = 157
    val_min = 3
    val_max = 190

    def __init__(self):
        super(HSVDetection, self).__init__()        

    def getProbability(self):
        return self.__prob

    def getDistanceFromMiddle(self, image):
        """Calculate the distance to the middle with the color detection"""
        self.__img = image
        self.__prepareImage()

        cropImage = self.__img[ImageParameters.box_y:(ImageParameters.box_y+ImageParameters.box_height), ImageParameters.box_x:ImageParameters.box_x+ImageParameters.box_width]

        MIN = np.array([self.hue_min, self.sat_min, self.val_min], np.uint8)
        MAX = np.array([self.hue_max, self.sat_max, self.val_max], np.uint8)
        mask = cv2.inRange(cropImage, MIN, MAX)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((3,3), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_ERODE, np.ones((2,2), np.uint8))

        ret, tresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
        (cnts, _) = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        c = sorted(cnts, key = self.__calcProbability, reverse = True)[0]

        x, y, w, h = cv2.boundingRect(c)
        x = x + ImageParameters.box_x
        y = y + ImageParameters.box_y
        self.__prob = `CanProbability.getProbabilityOfRect(w,h)`
        
        cv2.rectangle(self.__img, (x, y),(x+w,y+h),(0,230,0),1)
        cv2.imwrite("detected/hsv.png", self.__img)
        cv2.imwrite("detected/hsvc.png", mask)

        halfX = x + w/2
        distanceFromMiddle = halfX - ImageParameters.width/2

        return distanceFromMiddle

    def __calcProbability(self, contour):
        """Calculate probabilty that the found contour is our can"""
        x, y, w, h = cv2.boundingRect(contour)
        return CanProbability.getProbabilityOfRect(w, h)

    def __prepareImage(self):
        """Apply HSV filter."""
        self.__img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2HSV)
