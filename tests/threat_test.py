__author__ = 'drock'

from source.GameObject import *
from source.Positionable import *
from unittest import TestCase

class TestThreat(TestCase):
    def test_threat_distance(self):
        orc = Orc(5, 1)
        my_position = -2
        distance = orc.getDistance(my_position)
        self.assertEqual(distance, 7)

    def test_thread_velocity(self):
        orc = Orc(0, 2)
        velocity = orc.velocity
        self.assertEqual(velocity, 2)

    def test_orc_type(self):
        orc = Orc(0, 1, OrcType.violet)
        self.assertEqual(orc.type, OrcType.violet)

    def test_thread_id(self):
        orc1 = Orc(1, 2)
        orc2 = Orc(3, 4)
        id1 = orc1.id
        id2 = orc2.id
        self.assertNotEqual(id1, id2)

    def test_threat_is_alive(self):
        orc = Orc(5,6)
        self.assertTrue(orc.is_alive())

    def test_terminate_threat(self):
        orc = orcFactory.spawn_orc(0)
        orcFactory.terminate_orc(orc.id)
        self.assertFalse(orc.is_alive())

    def test_priority(self):
        orc = orcFactory.spawn_orc(1)
        orc.priority = 13
        self.assertEqual(orc.priority, 13)

    def test_get_by_id(self):
        orc1 = orcFactory.spawn_orc(2)
        id = orc1.id
        orc2 = orcFactory.get_orc(id)
        self.assertNotEqual(orc2, None)

    def test_random_orcs(self):
        generator = OrcGenerator()
        orcs = generator.generate_orcs_randomly(10)
        self.assertEqual(len(orcs), 10)