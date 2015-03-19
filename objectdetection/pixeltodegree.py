import math
from imageparameters import ImageParameters

class PixelToDegree(object):
    """Convert pixel from image to degree"""

    fov_picamera = math.radians(53)

    @staticmethod
    def getDegree(distanceFromMiddle):
        # x = (distanceFromMiddle - ImageParameters.width/2)
        x = distanceFromMiddle
        y = (ImageParameters.width / 2) / math.tan(PixelToDegree.fov_picamera / 2)
 
        # degree = math.degrees(math.atan2(x, y))
        degree = math.degrees(math.atan2(y, x)) - 90
        degree = round(-1 * degree, 2)
        return degree
