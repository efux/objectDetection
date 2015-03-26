import cv2
from objectdetection import ObjectDetection
from imageparameters import ImageParameters
from canprobability import CanProbability

class ContourDetection(ObjectDetection):
    """Detect the can with the help of contours"""

    __expectedRatio = 0.75

    def __init__(self):
        super(ContourDetection, self).__init__()        

    def getDistanceFromMiddle(self):
        """Calculate the distance to the middle with the contour detection"""
        self.__prepareImage()
        ret, thresh = cv2.threshold(self.__img, ImageParameters.contrastCalibration, 255, cv2.THRESH_BINARY_INV)
        (cnts, _) = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        c = sorted(cnts, key = self.__calcProbability, reverse = True)[0]
        x, y, w, h = cv2.boundingRect(c)
        halfX = x + w/2
        distanceFromMiddle = halfX - ImageParameters.width/2

        return distanceFromMiddle

    def __calcProbability(self, contour):
        """Calculate probabilty that the found contour is our can"""
        x, y, w, h = cv2.boundingRect(contour)
        return CanProbability.getProbabilityOfRect(w, h)

    def __prepareImage(self):
        """Capture image from camera and apply grey filter."""
        self.__img = self.camera.capture()
        self.__img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
