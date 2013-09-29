__author__='VUTUNG'

import math
import decimal
import unittest
from triangle import detect_triangle

class testTriangle(unittest.TestCase):
#Test Equilateral
    def testEquilateral(self):
        result = detect_triangle(2.0,2.0,2.0)
        self.assertEqual(result,'equilateral')
    def testEquilateral1(self):
        result = detect_triangle(3,3,3)
        self.assertEqual(result,'equilateral')
#Test isosceles right-angled
    def testIsosceles_rightangled(self):
        result = detect_triangle(3.0,3.0,math.sqrt(18.0))
        self.assertEqual(result,'isosceles right-angled')
    def testIsosceles_rightangled1(self):
        result = detect_triangle(5.0,math.sqrt(50),5.0)
        self.assertEqual(result,'isosceles right-angled')
    def testIsosceles_rightangled2(self):
        result = detect_triangle(math.sqrt(32.0),4.0,4.0)
        self.assertEqual(result,'isosceles right-angled')
#Test right-angled
    def testRight_angled(self):
        result = detect_triangle(3,4,5)
        self.assertEqual(result,'right-angled')
    def testRight_angled1(self):
        result = detect_triangle(3.0,4.0,5.0)
        self.assertEqual(result,'right-angled')
    def testRight_angled2(self):
        result = detect_triangle(4.0,math.sqrt(52),6.0)
        self.assertEqual(result,'right-angled')
    def testRight_angled3(self):
        result = detect_triangle(math.sqrt(61),5.0,6.0)
        self.assertEqual(result,'right-angled')
#Test Isosceles
    def testIsosceles(self):
        result = detect_triangle(2.0,2.0,3.0)
        self.assertEqual(result,'isosceles')
    def testIsosceles1(self):
        result = detect_triangle(2.0,3.0,3.0)
        self.assertEqual(result,'isosceles')
    def testIsosceles2(self):
        result = detect_triangle(3.0,5.0,3.0)
        self.assertEqual(result,'isosceles')
#Test Normal
    def testNormal(self):
        result = detect_triangle(3.0,4.0,2.0)
        self.assertEqual(result,'normal')
    def testNormal1(self):
        result = detect_triangle(3,4,6)
        self.assertEqual(result,'normal')
    def testNormal2(self):
        result = detect_triangle(2**30+1,2**30+2,2**30+3)
        self.assertEqual(result,'normal')
#Test not triangle
    def testNotTriangle(self):
        result =detect_triangle(5.0,2.0,2.0)
        self.assertEqual(result,'Not Triangle')
    def testNotTriangle1(self):
        result =detect_triangle(5.0,8.0,2.0)
        self.assertEqual(result,'Not Triangle')
    def testNotTriangle2(self):
        result =detect_triangle(5.0,6.0,12.0)
        self.assertEqual(result,'Not Triangle')
    def testNotTriangle3(self):
        result =detect_triangle(5.0,8.0,2**30)
        self.assertEqual(result,'Not Triangle')
#Test Wrong value
    def testWrongValue(self):
        result = detect_triangle('a',1.0,1.0)
        self.assertEqual(result,'Wrong value(not float)')
    def testWrongValue1(self):
        result =detect_triangle(2.0,'a',2.0)
        self.assertEqual(result,'Wrong value(not float)')
    def testWrongValue2(self):
        result =detect_triangle(2.0,3.0,2**32)
        self.assertEqual(result,'Wrong value(not float)')
    def testWrongValue3(self):
        result =detect_triangle(2.0,3.0,-2**32)
        self.assertEqual(result,'Wrong value(not float)')
#Test Null value
    def testNullValue(self):
        result = detect_triangle(2,2)
        self.assertEqual(result,'Null Value')
    def testNullValue1(self):
        result = detect_triangle()
        self.assertEqual(result,'Null Value')

if __name__ == '__main__':
    unittest.main()