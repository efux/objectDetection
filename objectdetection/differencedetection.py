import cv2
from objectdetection import ObjectDetection
from imageparameters import ImageParameters
from canprobability import CanProbability
import numpy as np

class DifferenceDetection(ObjectDetection):
    """Detect the can with the help of a reference image."""

    def __init__(self, reference):
        super(DifferenceDetection, self).__init__()        
        self.__cropReferenceImage = reference[ImageParameters.box_y:(ImageParameters.box_y+ImageParameters.box_height), ImageParameters.box_x:(ImageParameters.box_x+ImageParameters.box_width)]
        self.__cropReferenceImage = cv2.cvtColor(self.__cropReferenceImage, cv2.COLOR_BGR2GRAY)

    def getProbability(self):
        return self.__prob

    def getDistanceFromMiddle(self, image):
        """Calculate the distance to the middle with a reference image."""
        self.__img = image
        self.__prepareImage()

        self.__cropImage = self.__img[ImageParameters.box_y:(ImageParameters.box_y+ImageParameters.box_height), ImageParameters.box_x:(ImageParameters.box_x+ImageParameters.box_width)]

        diff = cv2.absdiff(self.__cropReferenceImage, self.__cropImage)
        ret, thresh = cv2.threshold(diff, 20, 256, cv2.THRESH_BINARY_INV)
        cv2.imwrite("detected/diffm.png", thresh)

        (cnts, _) = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        c = sorted(cnts, key = self.__calcProbability, reverse = True)[0]

        x, y, w, h = cv2.boundingRect(c)
        x = x + ImageParameters.box_x
        y = y + ImageParameters.box_y
        self.__prob = `CanProbability.getProbabilityOfRect(w,h)`
        
        cv2.rectangle(self.__img, (x, y),(x+w,y+h),(0,230,0),1)
        cv2.imwrite("detected/diff.png", self.__img)

        halfX = x + w/2
        distanceFromMiddle = halfX - ImageParameters.width/2

        return distanceFromMiddle

    def __calcProbability(self, contour):
        """Calculate probabilty that the found contour is our can."""
        x, y, w, h = cv2.boundingRect(contour)
        return CanProbability.getProbabilityOfRect(w, h)

    def __prepareImage(self):
        """Apply filters."""
        self.__img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
