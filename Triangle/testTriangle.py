__author__='VUTUNG'

import math
import unittest
from Triangle import Triangle
class testTriangle(unittest.TestCase):

    def testEquilateral(self):
        result = Triangle(2.0,2.0,2.0)
        self.assertEqual(result,'equilateral')
    def testIsosceles_rightangled(self):
        result = Triangle(3.0,3.0,math.sqrt(18.0))
        self.assertEqual(result,'isosceles right-angled')
    def testIsosceles(self):
        result = Triangle(3.0,4.0,5.0)
        self.assertEqual(result,'isosceles')
    def testRight_angled(self):
        result = Triangle(2.0,2.0,3.0)
        self.assertEqual(result,'right-angled')
    def testNormal(self):
        result = Triangle(3.0,4.0,2.0)
        self.assertEqual(result,'normal')
    def testNotTriangle(self):
        result = Triangle(5.0,2.0,2.0)
        self.assertEqual(result,'Not Triangle')
    def testWrongValue(self):
        result = Triangle('a',2.0,2.0)
        self.assertEqual(result,'Wrong value(not interger)')
    def testNullValue(self):
        result = Triangle(2,2)
        self.assertEqual(result,'Null Value')
if __name__ == '__main__':
    unittest.main()