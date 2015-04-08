"""
Test for source.source2
"""
from source.source2 import get_quadrilateral_type
from unittest import TestCase

class TestGetQuadrilateralType(TestCase):

    def test_get_quadrilateral_square_all_int(self):
        result = get_quadrilateral_type(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_rectangle_all_int(self):
        result = get_quadrilateral_type(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')

    def test_get_quadrilateral_equilateral_int_dict(self):
        a = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
        result = get_quadrilateral_type(a)
        self.assertEqual(result, 'square')

    def test_get_quadrilateral_rectangle_all_char(self):
        result = get_quadrilateral_type('1', '2', '1', '2')
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_rectangle_has_int_zero(self):
        result = get_quadrilateral_type(0, 1, 0, 1)
        self.assertEqual(result, 'invalid')

    def test_get_quadrilateral_invalie_all_int(self):
        result = get_quadrilateral_type(1, 2, 3, 4)
        self.assertEqual(result, 'invalid')