import unittest
import objectdetection.canprobability
import objectdetection.imageparameters
from objectdetection.canprobability import CanProbability
from objectdetection.imageparameters import ImageParameters

class TestCanProbability(unittest.TestCase):

    def setUp(self):
        self.oldWidth = ImageParameters.width
        self.oldHeight = ImageParameters.height
        ImageParameters.width = 320
        ImageParameters.height = 240

    def tearDown(self):
        ImageParameters.width = self.oldWidth
        ImageParameters.height = self.oldHeight

#   def test_getProbabilityOfRectNoMatch(self):
#       self.assertEqual(0.00, CanProbability.getProbabilityOfRect(0,0))

#   def test_getProbabilityOfRectPerfectMatch(self):
#       self.assertGreaterEqual(CanProbability.getProbabilityOfRect(40, 60), 0.6)

    def test_getAreaProbability(self):
        self.assertEqual(0.00, CanProbability.getAreaProbability(0))

    def test_getAreaProbabilityPerfect(self):
        self.assertEqual(1.00, CanProbability.getAreaProbability(40*60))

    def test_normalizeProbabilityNegative(self):
        self.assertEqual(0.00, CanProbability.normalizeProbability(-0.5))

    def test_normalizeProbabilityNormal(self):
        self.assertEqual(0.5, CanProbability.normalizeProbability(0.5))

    def test_normalizeProbabilityZero(self):
        self.assertEqual(0.0, CanProbability.normalizeProbability(0.0))

    def test_normalizeProbabilityOne(self):
        self.assertEqual(1.0, CanProbability.normalizeProbability(1.0))

    def test_normalizeProbabilityTwo(self):
        self.assertEqual(0.0, CanProbability.normalizeProbability(2.0))

    def test_normalizeProbabilityMax(self):
        self.assertEqual(0.1, CanProbability.normalizeProbability(1.9))

    def test_normalizeProbabilityTooMuch(self):
        self.assertEqual(0.0, CanProbability.normalizeProbability(2.1))

    def test_normalizeProbabilityInRange(self):
        self.assertEqual(0.7, CanProbability.normalizeProbability(0.7))

    def test_getLengthProbability(self):
        self.assertEqual(1.0, CanProbability.getLengthProbability(5,5))

    def test_getLengthProbabilityZero(self):
        self.assertEqual(0.0, CanProbability.getLengthProbability(0,5))
