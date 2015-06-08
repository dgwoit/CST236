import logging
from unittest import TestCase
from waypoint import *

class TestWaypoint(TestCase):
    def test_position(self):
        wpt = Waypoint("1", "test", LatLon(1, 2))
        self.assertEqual(wpt.position.lat, 1, "%f <> %f" % (wpt.position.lat, 1))
        self.assertEqual(wpt.position.lon, 2, "%f <> %f" % (wpt.position.lon, 2))

    def test_name(self):
        wpt = Waypoint("", "test", LatLon(1, 2))
        assert wpt.name == "test", "%s <> %s" % (wpt.name, "test")

