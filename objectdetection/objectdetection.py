from pixeltodegree import PixelToDegree
from camera import Camera

class ObjectDetection(object):
    """Interface for ObjectDetection, the getPosition- and init-methods have to be implemented"""

    def getDistanceFromMiddle(self):
        """Returns the position of the can in degrees. To be implemented by subclasses."""
        raise NotImplementedError("Has to be implemented by subclasses.")
        
    def getPosition(self):
        return PixelToDegree.getDegree(self.getDistanceFromMiddle())

    def __init__(self):
        """Initializes the camera used for this camera detection."""
        print "Initialize camera..."
        self.camera = Camera()



