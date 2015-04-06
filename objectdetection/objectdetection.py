from pixeltodegree import PixelToDegree
from camera import Camera

class ObjectDetection(object):
    """Interface for ObjectDetection, the getPosition- and init-methods have to be implemented"""
    __prob = 0.0

    def getProbability(self):
        """Probability that this detection is the can."""
        return self.__prob

    def getDistanceFromMiddle(self, image):
        """Returns the position of the can in degrees. To be implemented by subclasses."""
        raise NotImplementedError("Has to be implemented by subclasses.")
        
    def getPosition(self, image):
        return PixelToDegree.getDegree(self.getDistanceFromMiddle(image))

    def __init__(self):
        """Initializes the camera used for this camera detection."""



