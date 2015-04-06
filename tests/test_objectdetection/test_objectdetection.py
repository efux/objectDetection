import unittest
import objectdetection.objectdetection
from objectdetection.objectdetection import ObjectDetection

class TestObjectDetection(unittest.TestCase):

    def test_getDistanceFromMiddle(self):
        with self.assertRaises(NotImplementedError):
            ObjectDetection().getDistanceFromMiddle(0)
