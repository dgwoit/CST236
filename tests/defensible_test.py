"""
Test for source.defensible
"""
from source.Defensible import *
from source.GameObject import *
from unittest import TestCase

class TestDefensible(TestCase, Defense):
    """
    TestDefensible
    """
    def test_defense_orc_in_range(self):
        defense_perimeter = DefensePerimeter(0, 2)
        defense_perimeter.add_defense(self)
        orc = Orc(1)
        self.defense_activated = False;
        defense_perimeter.check_for_breach(orc)
        self.assertEqual(self.defense_activated, True)
        return

    def test_defense_orc_not_in_range(self):
        defense_perimeter = DefensePerimeter(0, 2)
        defense_perimeter.add_defense(self)
        orc = Orc(3)
        self.defense_activated = False;
        defense_perimeter.check_for_breach(orc)
        self.assertEqual(self.defense_activated, False);
        return
    
    def activate(self, game_object):
        self.defense_activated = True