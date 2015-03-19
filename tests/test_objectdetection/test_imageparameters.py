import unittest
import objectdetection.imageparameters
from objectdetection.imageparameters import ImageParameters

class TestImageParameters(unittest.TestCase):

    def test_ImageParametersWidth(self):
        self.assertEqual(320, ImageParameters.width)

    def test_ImageParametersHeight(self):
        self.assertEqual(240, ImageParameters.height)

    def test_ImageParametersContrastCalibration(self):
        self.assertEquals(80, ImageParameters.contrastCalibration)
