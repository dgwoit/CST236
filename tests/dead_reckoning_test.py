from unittest import TestCase
from vessel import Vessel
from dead_reckoner import DeadReckoner
from latlon import LatLon
from mock import patch
import threading
import time


class TestDeadReckoning(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_dead_reckoner(self):
        vessel = Vessel()
        vessel.position = LatLon(9, 10)
        vessel.speed_over_ground = 23
        vessel.heading_true = 45
        dr = DeadReckoner(vessel)
        real_sleep = time.sleep
        with patch("time.sleep") as mock:
            waiter = threading.Event()

            def sleepy(duration):
                print "sleepy called"
                waiter.set()
                real_sleep(10.0)

            mock.side_effect = sleepy
            dr.start()
            waiter.wait()
            dr.stop()
        assert vessel.heading_true == 45, "HDT changed: {1} <> {2}".format(vessel.heading_true, 45)
        assert vessel.speed_over_ground == 23, "SOG changed: {1} <> {2}".format(vessel.speed_over_ground, 23)
        assert vessel.position != LatLon(9, 10), "DR failed to navigate: ({1}, {2}) == ({2}, {3})".format(vessel.position.lat, vessel.position.lon, 9, 10)