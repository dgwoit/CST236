"""
Test for source.source1
"""
from source.source1 import get_triangle_type
from unittest import TestCase

class TestGetTriangleType(TestCase):

    def test_get_triangle_equilateral_all_int(self):
        result = get_triangle_type(1, 1, 1)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_scalene_all_int(self):
        result = get_triangle_type(1, 2, 3)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_equilateral_list(self):
        a = [1, 1, 1]
        b = [2, 2, 2]
        result = get_triangle_type(a, b)
        self.assertEqual(result, 'isosceles')

    def test_get_triangle_equilateral_dict(self):
        a = {'a': 1, 'b': 2, 'c': 3}
        result = get_triangle_type(a)
        self.assertEqual(result, 'scalene')

    def test_get_triangle_equilateral_all_char(self):
        result = get_triangle_type('1', '1', '1')
        self.assertEqual(result, 'invalid')

    def test_get_triangle_equilateral_has_zero(self):
        result = get_triangle_type(1, 1, 0)
        self.assertEqual(result, 'invalid')

