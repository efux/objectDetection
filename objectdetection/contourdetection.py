import cv2
from objectdetection import ObjectDetection
from imageparameters import ImageParameters

class ContourDetection(ObjectDetection):
    """Detect the can with the help of contours"""

    __expectedContourSize = ImageParameters.width * ImageParameters.height / 16
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

        # probability of size matching
        probSizeWeight = 0.6 
        probSize = cv2.contourArea(contour) / self.__expectedContourSize
        if probSize > 1.0:
            probSize = 1.0 / probSize
        probSize = pow(probSize, 2)
        # exit now if size probability limit not reached
        if probSize < 0.2:          
            return 0.0 
        # probability of ratio matching
        probRatioWeight = 1.0 - probSizeWeight
        x, y, w, h = cv2.boundingRect(contour)
        ratio = float(w)/float(h)
        probRatio = ratio / self.__expectedRatio
        if probRatio > 1.0:
            probRatio = 1.0 / probRatio
        probRatio = pow(probRatio, 2)
        # exit now if ratio probability limit not reached
        if probRatio < 0.4:
            return 0.0 
        # add probabilities
        totalProb = probSize * probSizeWeight + probRatio * probRatioWeight
        return totalProb

    def __prepareImage(self):
        """Capture image from camera and apply grey filter."""
        self.__img = self.camera.capture()
        self.__img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
