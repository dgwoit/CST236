import logging
from unittest import TestCase
from route import Route
from waypoint import Waypoint
from latlon import LatLon
from settings import Settings
from route_follower import RouteFollower

class TestRouteFollower(TestCase):
    waypoint_active_called = False
    destination_arrived_called = False

    def setup(self):
        waypoint_active_called = False
        destination_arrived_called = False

    def test_leg(self):
        route = Route("1234", "route")
        route.waypoints.append(Waypoint("id1", "1", LatLon(1, 2)))
        route.waypoints.append(Waypoint("id2", "2", LatLon(-3, 4)))
        route.waypoints.append(Waypoint("id3", "3", LatLon(5, -6)))
        self.waypoint_active_called = False
        self.destination_arrived_called = False
        follower = RouteFollower(route)
        follower.waypoint_active_callback = self.waypoint_active
        follower.destination_arrived_callback = self.destination_arrived
        self.assertEqual(follower.active_waypoint.name, "1")

        follower.set_position(LatLon(1.000001, 2.000001))
        self.assertTrue(self.waypoint_active_called)
        self.assertFalse(self.destination_arrived_called)
        self.assertIsNotNone(follower.active_waypoint)
        self.assertEqual(follower.active_waypoint.name, "2")
        self.waypoint_active_called = False

        follower.set_position(LatLon(-3.000001, 4.000001))
        self.assertTrue(self.waypoint_active_called)
        self.assertFalse(self.destination_arrived_called)
        self.assertIsNotNone(follower.active_waypoint)
        self.assertEqual(follower.active_waypoint.name, "3")
        self.waypoint_active_called = False

        follower.set_position(LatLon(5.000001, -6.000001))
        self.assertTrue(self.destination_arrived_called)
        self.assertIsNotNone(follower.active_waypoint)
        self.assertEqual(follower.active_waypoint.name, "3")
        self.waypoint_active_called = False


    def waypoint_active(self, waypoint):
        self.assertIsNotNone(waypoint)
        self.waypoint_active_called = True

    def destination_arrived(self):
        self.destination_arrived_called = True