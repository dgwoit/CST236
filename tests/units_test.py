"""
Test of units
"""

from unittest import TestCase
from Units import *

class UnitsTest(TestCase):
    def test_set_unit_system(self):
        units.system = UnitSystem.Nautical
        self.assertEqual(units.system, UnitSystem.Nautical)