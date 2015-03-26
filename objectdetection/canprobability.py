from imageparameters import ImageParameters

class CanProbability(object): 
    """Class for the calculation of the probability, if a contour is a can."""

    WEIGHT_AREASIZE = 0.4
    WEIGHT_RATIO = 0.4
    WEIGHT_LENGTH = 0.2

    # This are the default values for the can (change when tested first with the picamera on the actual Tellbot)
    expectedWidth = 54
    expectedHeight = 70
    expectedAreaSize = ImageParameters.width/8 * ImageParameters.height/4

    @staticmethod
    def getProbabilityOfRect(w, h):
        """Calculates the probability of a rectangle. 1.0 == Perfect match 0.0 == No match"""
        probability = 0.0

        if h>0 and w>0: 
            probability = probability + CanProbability.getAreaProbability(w*h) * CanProbability.WEIGHT_AREASIZE
            probability = probability + CanProbability.getRatioProbability(w, h) * CanProbability.WEIGHT_RATIO
            probability = probability + CanProbability.getLengthsProbability(w, h) * CanProbability.WEIGHT_LENGTH

        return probability


    @staticmethod
    def getRatioProbability(w,h):
        """Calculates the probability of the can based on the ratio.""" 
        probability = 0.00
        probability = CanProbability.getLengthProbability(w/h, CanProbability.expectedWidth/CanProbability.expectedHeight)
        return CanProbability.normalizeProbability(probability)


    @staticmethod
    def getLengthsProbability(w, h):
        """Calculates probability based on the expectedLengths."""
        probability = 0.00

        probability = probability + CanProbability.getLengthProbability(w, CanProbability.expectedWidth) * 0.5
        probability = probability + CanProbability.getLengthProbability(h, CanProbability.expectedHeight) * 0.5

        return probability


    @staticmethod
    def getLengthProbability(length, expected):
        probability = 0.0
        if expected>0:
            probability = length / expected
        return CanProbability.normalizeProbability(probability)


    @staticmethod
    def getAreaProbability(area):
        """Calculates probability  that this area has the same size as the one of a can."""
        probability = 0.00

        probability = area / CanProbability.expectedAreaSize

        return CanProbability.normalizeProbability(probability)


    @staticmethod
    def normalizeProbability(probability):
        """The input probability can be everything. Limit on the range from 0.0 to 1.0."""
        if probability >= 0.00 and probability <= 1.00:
            probability = round(probability, 2)
            return probability
        else:
            if probability >= 0.00 and probability <= 2.0:
                probability = probability-2.0
                probability = abs(probability)
                probability = round(probability,2)
                return probability
            else:
                return 0.00


