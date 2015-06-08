import logging
from unittest import TestCase
from route import Route
from waypoint import Waypoint
from latlon import LatLon

class TestRoute(TestCase):
    def test_name(self):
        route = Route("1", "name")
        self.assertEqual(route.name, "name", "%s <> %s" % (route.name, "name"))

    def test_add_waypoint(self):
        route = Route("1", "route")
        route.waypoints.append(Waypoint("3", "wpt1", LatLon(1, 2)))
        route.waypoints.append(Waypoint("4", "wpt2", LatLon(1, 2)))
        self.assertEqual(len(route.waypoints), 2, "{0} <> {1}".format(len(route.waypoints), 2))

    def test_remove_waypoint(self):
        route = Route("1", "route")
        wpt1 = Waypoint("2", "wpt1", LatLon(1, 2))
        wpt2 = Waypoint("3", "wpt2", LatLon(3, 4))
        route.waypoints.append(wpt1)
        route.waypoints.append(wpt2)
        self.assertEqual(len(route.waypoints), 2, "{0} <> {1}".format(len(route.waypoints), 2))
        route.waypoints.remove(wpt1)
        self.assertEqual(len(route.waypoints), 1, "{0} <> {1}".format(len(route.waypoints), 1))
        route.waypoints.remove(wpt2)
        self.assertEqual(len(route.waypoints), 0, "{0} <> {1}".format(len(route.waypoints), 0))

