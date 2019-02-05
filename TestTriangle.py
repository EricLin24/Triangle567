# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle
from math import sqrt
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testIsTriangle(self):
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle', '1,1,2 should not be a triangle') #invalid

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle') #invalid

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(6,7,8), 'Scalene', '6,7,8 should be scalene')

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', '-1, 1, 1 should be isosceles')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle('a', 'b', 'c'), 'InvalidInput', 'a, b, c are not valid inputs')

    def testOverlap1(self):
        self.assertEqual(classifyTriangle(2, 2, sqrt(8)), 'Right and Isosceles', '2, 2, sqrt(8) should be right and isosceles') #invalid

    def testOverlap2(self):
        self.assertEqual(classifyTriangle(2, 5, sqrt(29)), 'Right and Scalene', '2, 5, sqrt(29) should be right and scalene')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

