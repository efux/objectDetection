from imageparameters import ImageParameters

class CanProbability(object): 
    """Class for the calculation of the probability, if a contour is a can."""

    WEIGHT_AREASIZE = 1.0

    @staticmethod
    def getProbabilityOfRect(w, h):
        """Calculates the probability of a rectangle. 1.0 == Perfect match 0.0 == No match"""
        probability = 0.0

        probability = probability + CanProbability.getAreaProbability(w*h) * CanProbability.WEIGHT_AREASIZE

        return probability


    @staticmethod
    def getAreaProbability(area):
        """Calculates probability  that this area has the same size as the one of a can."""
        probability = 0.00

        expectedAreaSize = ImageParameters.width/8 * ImageParameters.height/4
        probability = area / expectedAreaSize

        return CanProbability.normalizeProbability(probability)


    @staticmethod
    def normalizeProbability(probability):
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


