# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from math import sqrt
from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def test_is_triangle(self):
        # invalid
        self.assertEqual(classify_triangle(1, 1, 2),
                         'NotATriangle', '1,1,2 should not be a triangle')

    def test_right_triangle_a(self):
        # invalid
        self.assertEqual(classify_triangle(3, 4, 5),
                         'Right and Scalene', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        self.assertEqual(classify_triangle(5, 3, 4),
                         'Right and Scalene', '5,3,4 is a Right triangle')

    def test_equilateral_triangles(self):
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(6, 7, 8),
                         'Scalene', '6,7,8 should be scalene')

    def test_boundary(self):
        self.assertEqual(classify_triangle(-1, 1, 1),
                         'InvalidInput', '-1, 1, 1 should be isosceles')
        self.assertEqual(classify_triangle(200, 201, 199), 'InvalidInput', 'sides should more than 0 and les or equal '
                                                                           'than 200')

    def test_invalid_input(self):
        self.assertEqual(classify_triangle('a', 'b', 'c'), 'InvalidInput',
                         'a, b, c are not valid inputs')

    def test_overlap1(self):
        # invalid
        self.assertEqual(classify_triangle(2, 2, sqrt(8)), 'Right and Isosceles',
                         '2, 2, sqrt(8) should be right and isosceles')

    def test_overlap2(self):
        self.assertEqual(classify_triangle(2, 5, sqrt(29)), 'Right and Scalene',
                         '2, 5, sqrt(29) should be right and scalene')

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 2), 'Isosceles',
                         '5, 5, 2 should be isosceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
