import cv2
from objectdetection import ObjectDetection
from imageparameters import ImageParameters
from canprobability import CanProbability

class ContourDetection(ObjectDetection):
    """Detect the can with the help of contours"""

    def __init__(self):
        super(ContourDetection, self).__init__()        

    def getProbability(self):
        return self.__prob

    def getDistanceFromMiddle(self, image):
        """Calculate the distance to the middle with the contour detection"""
        self.__img = image
        self.__prepareImage()
        ret, thresh = cv2.threshold(self.__img, ImageParameters.contrastCalibration, 255, cv2.THRESH_BINARY_INV)
        (cnts, _) = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key = self.__calcProbability, reverse = True)[:1]

        if len(cnts) > 0:
            for c in cnts:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(self.__img, (x, y),(x+w,y+h),(0,230,0),1)

            cv2.imwrite("detected/cont.png", self.__img)
            self.__prob = `CanProbability.getProbabilityOfRect(w,h)`

            halfX = x + w/2
            distanceFromMiddle = halfX - ImageParameters.width/2
        else:
            distanceFromMiddle = 0
            self.__prob = 0.00

        return distanceFromMiddle

    def __calcProbability(self, contour):
        """Calculate probabilty that the found contour is our can"""
        x, y, w, h = cv2.boundingRect(contour)
        return CanProbability.getProbabilityOfRect(w, h)

    def __prepareImage(self):
        """Apply grey filter."""
        self.__img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
