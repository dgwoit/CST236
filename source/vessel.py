from latlon import LatLon
from enum import Enum

class Vessel:
    class NavigationMode(Enum):
        none = 0
        dead_reckoning = 1
        gps = 2

    def __init__(self):
        self.position = LatLon()
        self.heading_true = 0
        self.speed_over_ground = 0
        self._follower = None #e.g. RouteFollower, WaypointFollower
