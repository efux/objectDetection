class Measurement(object):
    """Contains an angle and the probability"""

    def __init__(self, angle, probability):
        super(Measurement, self).__init__()
        self.angle = angle
        self.probability = probability

    def __repr__(self):
        return "Angle: " + `self.angle` + " Probability: " + `self.probability`
