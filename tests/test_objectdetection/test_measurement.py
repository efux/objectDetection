import unittest
import objectdetection.measurement
from objectdetection.measurement import Measurement

class TestMeasurement(unittest.TestCase):

    def test_measurementRepr(self):
        measurement = Measurement(15.51, 13.95)
        self.assertEqual("Angle: 15.51 Probability: 13.95", str(measurement))
