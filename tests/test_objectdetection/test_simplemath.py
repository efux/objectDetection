import unittest
import objectdetection.simplemath
from objectdetection.simplemath import Mathematics

class TestMathematics(unittest.TestCase):

    def test_add(self):
        math = Mathematics()
        self.assertEqual(math.add(5,4), 9)
