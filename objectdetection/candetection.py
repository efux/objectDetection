from contourdetection import ContourDetection
from hsvdetection import HSVDetection
from differencedetection import DifferenceDetection
from camera import Camera
from measurement import Measurement

class CanDetection(object):
    """Performs multiple detections for the can and the initialisation."""

    __detections = []

    def __init__(self):
        """Constructor for the CanDetection, assignes the wanted detection methods."""
        super(CanDetection, self).__init__()
        self.__detections.append(ContourDetection())
        self.__detections.append(HSVDetection())

    def initialize(self):
        """Initializes the camera and takes a first snapshot for the difference detection."""
        self.__camera = Camera()
        __firstImage = self.__camera.capture()
        self.__detections.append(DifferenceDetection(__firstImage))

    def getTurnAngleInDegree(self):
        """Calculates for all the assigned detection methods the position of the can."""
        imageWithCan = self.__camera.capture()

        probabilities = []
        for d in self.__detections:
            m = Measurement(d.getPosition(imageWithCan), d.getProbability())
            print m
            probabilities.append(m)

        finalMeasurement = sorted(probabilities, key=lambda x: x.probability, reverse=True)[0]
        return finalMeasurement
