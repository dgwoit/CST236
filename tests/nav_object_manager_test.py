from unittest import TestCase
from navigation_object_manager import NavigationObjectManager
from latlon import LatLon
from waypoint import Waypoint
from route import Route
from track import Track
import random
import json
import string
from strgen import StringGenerator

class TestNavObjMan(TestCase):

    def setUp(self):
        self.nav_obj_man = NavigationObjectManager()

    def tearDown(self):
        pass

    def test_waypoints(self):
        wpt1 = self.nav_obj_man.add_waypoint("wpt1", LatLon(-14, -15))
        self.assertIsNotNone(wpt1)
        wpt2 = self.nav_obj_man.add_waypoint("wpt2", LatLon(16, 17))
        self.assertIsNotNone(wpt2)
        wpt3 = self.nav_obj_man.add_waypoint("wpt3", LatLon(18, -19))
        self.assertIsNotNone(wpt3)
        wpt4 = self.nav_obj_man.add_waypoint("wpt4", LatLon(-20, 21))
        self.assertIsNotNone(wpt4)
        self.assertEqual(len(self.nav_obj_man.waypoints), 4, "%d <> %d" % (len(self.nav_obj_man.waypoints), 4))
        self.nav_obj_man.remove_waypoint(wpt2)
        self.assertEqual(len(self.nav_obj_man.waypoints), 3, "%d <> %d" % (len(self.nav_obj_man.waypoints), 3))
        self.assertNotIn(wpt2, self.nav_obj_man.waypoints, "waypoint not removed")



    def rand_latlon(self):
        return LatLon(random.uniform(-90.0, 90.0), random.uniform(-180.0, 180.0))

    def rand_name(self):
        length = random.randint(1, 40)
        name = StringGenerator("[ -~]{%d}"%length).render()
        return name

    def make_waypoint(self, name="waypoint"):
        return self.nav_obj_man.add_waypoint(name, self.rand_latlon())

    def make_route(self, name="route", num_waypoints=2):
        rte = self.nav_obj_man.create_route(name)
        for i in range(0, num_waypoints, 1):
            self.nav_obj_man.add_waypoint_to_route(rte, str(i), self.rand_latlon())
        self.assertNotIn(rte, self.nav_obj_man.routes, "route added to collection before commit")
        self.nav_obj_man.commit_route(rte)
        self.assertIn(rte, self.nav_obj_man.routes.values(), "route not added to collection after commit")
        return rte

    def test_routes(self):
        rte1 = self.make_route("rte1", 2)
        self.assertEqual(len(self.nav_obj_man.routes), 1, "%d <> %d" % (len(self.nav_obj_man.routes), 1))
        rte2 = self.make_route("rte2", 3)
        self.assertEqual(len(self.nav_obj_man.routes), 2, "%d <> %d" % (len(self.nav_obj_man.routes), 2))
        rte3 = self.make_route("rte3", 4)
        self.assertEqual(len(self.nav_obj_man.routes), 3, "%d <> %d" % (len(self.nav_obj_man.routes), 3))
        rte4 = self.make_route("rte4", 4)
        self.assertEqual(len(self.nav_obj_man.routes), 4, "%d <> %d" % (len(self.nav_obj_man.routes), 4))
        self.nav_obj_man.remove_route(rte3)
        self.assertNotIn(rte3, self.nav_obj_man.routes.values(), "route %s not removed" % rte3.name)
        self.nav_obj_man.remove_route(rte4)
        self.assertNotIn(rte4, self.nav_obj_man.routes.values(), "route %s not removed" % rte4.name)
        self.nav_obj_man.remove_route(rte1)
        self.assertNotIn(rte1, self.nav_obj_man.routes.values(), "route %s not removed" % rte1.name)
        self.nav_obj_man.remove_route(rte2)
        self.assertNotIn(rte2, self.nav_obj_man.routes.values(), "route %s not removed" % rte2.name)


    def make_track(self, name, num_points):
        track = self.nav_obj_man.add_track(name)
        for i in range (0, num_points):
            track.add_point(self.rand_latlon())
        return track

    def test_tracks(self):
        trk1 = self.make_track("trk1", 10)
        self.assertEqual(len(self.nav_obj_man.tracks), 1, "%d <> %d" % (len(self.nav_obj_man.tracks), 1))
        trk1 = self.make_track("trk2", 10)
        self.assertEqual(len(self.nav_obj_man.tracks), 2, "%d <> %d" % (len(self.nav_obj_man.tracks), 2))
        trk1 = self.make_track("trk3", 10)
        self.assertEqual(len(self.nav_obj_man.tracks), 3, "%d <> %d" % (len(self.nav_obj_man.tracks), 3))
        trk1 = self.make_track("trk4", 10)
        self.assertEqual(len(self.nav_obj_man.tracks), 4, "%d <> %d" % (len(self.nav_obj_man.tracks), 4))

    def test_serialize_nav_objects(self):
        for i in range(1, 4):
            self.make_waypoint(self.rand_name())
            self.make_route(self.rand_name(), 4)
            self.make_track(self.rand_name(), 10)
        with open("navdata.json", 'w') as fout:
            json.dump(self.nav_obj_man.encode(), fout)

        # load data and compare to what we serialized out
        with open("navdata.json") as fin:
            data = json.load(fin)
            decoded_objects = NavigationObjectManager()
            decoded_objects.decode(data)

            assert len(self.nav_obj_man.waypoints) == len(decoded_objects.waypoints), "number of waypoints do not match"
            for wpt_id in self.nav_obj_man.waypoints:
                wpt1 = self.nav_obj_man.waypoints[wpt_id]
                wpt2 = decoded_objects.waypoints[wpt_id]
                self.assert_waypoint_equivalent(wpt1, wpt2)

            assert len(self.nav_obj_man.routes) == len(decoded_objects.routes), "number of routes do not match"
            for rte_id in self.nav_obj_man.routes:
                rte1 = self.nav_obj_man.routes[rte_id]
                rte2 = decoded_objects.routes[rte_id]
                self.assert_route_equivalent(rte1, rte2)

            assert len(self.nav_obj_man.tracks) == len(decoded_objects.tracks), "number of tracks do not match"
            for trk_id in self.nav_obj_man.tracks:
                trk1 = self.nav_obj_man.tracks[trk_id]
                trk2 = decoded_objects.tracks[trk_id]
                self.assert_track_equivalent(trk1, trk2)

    def assert_latlon_equality(self, ll1, ll2):
        assert ll1.lat == ll2.lat
        assert ll1.lon == ll2.lon

    def assert_waypoint_equivalent(self, wpt1, wpt2):
        assert wpt1.id == wpt2.id
        assert wpt1.name == wpt2.name
        assert wpt1.position.lat == wpt2.position.lat
        assert wpt1.position.lon == wpt2.position.lon

    def assert_route_equivalent(self, route1, route2):
        assert route1.id == route2.id
        assert route1.name == route2.name
        assert len(route1.waypoints) == len(route2.waypoints), "{0} <> {1}".format(len(route1.waypoints), len(route2.waypoints))
        for i in range(0, len(route1.waypoints)):
            wpt1 = route1.waypoints[i]
            wpt2 = route2.waypoints[i]
            self.assert_waypoint_equivalent(wpt1, wpt2)

    def assert_track_equivalent(self, track1, track2):
        self.assertIsNotNone(track1)
        self.assertIsNotNone(track2)
        assert track1.id == track2.id
        assert track1.name == track2.name
        assert len(track1.points) == len(track2.points)
        for i in range(0, len(track1.points)):
            pt1 = track1.points[i]
            pt2 = track2.points[i]
            assert pt1.datetime == pt2.datetime
            self.assert_latlon_equality(pt1.position, pt2.position)