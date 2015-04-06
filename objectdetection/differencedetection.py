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
        self.__cropReferenceImage = cv2.cvtColor(self.__cropReferenceImage, cv2.COLOR_BGR2RGB)

    def getProbability(self):
        return self.__prob

    def getDistanceFromMiddle(self, image):
        """Calculate the distance to the middle with a reference image."""
        self.__img = image
        self.__prepareImage()

        self.__cropImage = self.__img[ImageParameters.box_y:(ImageParameters.box_y+ImageParameters.box_height), ImageParameters.box_x:(ImageParameters.box_x+ImageParameters.box_width)]

        tresh = self.__compareImages()

        (cnts, _) = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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

    def __compareImages(self):
        """This method compares the reference image with the new image."""
        
        dx = 4
        y = 0
        for y in range(0, ImageParameters.box_height-1):
            for x in range(0, ImageParameters.box_width, dx):
                xstart = x
                xend = x + dx

                if x+dx > ImageParameters.box_width:
                    xend = ImageParameters.box_width

                refHist = cv2.calcHist(self.__cropImage[y:y+1, xstart:xend], [0], None, [256], [0, 256])
                refHist = cv2.normalize(refHist).flatten()

                imgHist = cv2.calcHist(self.__cropReferenceImage[y:y+1, xstart:xend], [0], None, [256], [0, 256])
                imgHist = cv2.normalize(imgHist).flatten()

                res = cv2.compareHist(refHist, imgHist, cv2.cv.CV_COMP_CORREL );
                newValue = np.array([0,0,0])
                if res < 0.1:
                    newValue = np.array([255,255,255])
                for xpos in range(xstart, xend):
                    self.__cropReferenceImage[y, xpos] = newValue

        cv2.imwrite("test.png", self.__cropReferenceImage)
        self.__cropReferenceImage = cv2.cvtColor(self.__cropReferenceImage, cv2.COLOR_BGR2GRAY)
        ret, tresh = cv2.threshold(self.__cropReferenceImage, ImageParameters.contrastCalibration, 255, cv2.THRESH_BINARY_INV)
        return tresh

    def __calcProbability(self, contour):
        """Calculate probabilty that the found contour is our can."""
        x, y, w, h = cv2.boundingRect(contour)
        return CanProbability.getProbabilityOfRect(w, h)

    def __prepareImage(self):
        """Apply filters."""
        self.__img = cv2.cvtColor(self.__img, cv2.COLOR_BGR2RGB)
