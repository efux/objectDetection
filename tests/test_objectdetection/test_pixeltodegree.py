import unittest
import objectdetection.pixeltodegree
import objectdetection.imageparameters
from objectdetection.pixeltodegree import PixelToDegree
from objectdetection.imageparameters import ImageParameters

class TestPixelToDegree(unittest.TestCase):

    def setUp(self):
        self.oldWidth = ImageParameters.width
        ImageParameters.width = 320

    def tearDown(self):
        ImageParameters.width = self.oldWidth

    def test_getDegreeZero(self):
        self.assertEqual(0, PixelToDegree.getDegree(0))

    def test_getDegreeBorder(self):
        self.assertEqual(15.36, PixelToDegree.getDegree(88.18))

    def test_getDegreeBorderLeft(self):
        self.assertEqual(-15.36, PixelToDegree.getDegree(-88.18))

    def test_getDegreeRounding(self):
        self.assertEqual(15.36, PixelToDegree.getDegree(88.13))
