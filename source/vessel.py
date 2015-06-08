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


    def set_navigator(self, navigator):
        self.navigator = navigator

    def set_follower(self, follower):
        self._follower = follower
        self._follower = waypoint_activated
        self._follower.destination_arrived = self.destination_arrived

    def waypoint_activated(self, waypoint):
        if self.navigator is not None:
            self.navigator.set_target_position(waypoint.position)

    def destination_arrived(self):
        self._follower = None
