
import logging
from unittest import TestCase
from latlon import *

class TestLatLon(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_lat_lon_default(self):
        ll = LatLon()
        self.assertEqual(ll.Lat, 0)
        self.assertEqual(ll.Lon, 0)


    def test_lon_over_180e(self):
        ll = LatLon(0, 181)
        self.assertEqual(ll.Lon, -179)

    def test_lon_over_180w(self):
        ll = LatLon(0, -181)
        self.assertEqual(ll.Lon, 179)

    def test_lat_90n(self):
        ll = LatLon(90, 0)
        self.assertEqual(ll.Lat, 90)

    def test_lat_90s(self):
        ll = LatLon(-90, 0)
        self.assertEqual(ll.Lat, -90)

    def test_lat_over_90n(self):
        with self.assertRaises(Exception):
            LatLon(90.1, 0)

    def test_lat_over_90s(self):
        with self.assertRaises(Exception):
            LatLon(-90.1, 0)