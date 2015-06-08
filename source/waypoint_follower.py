import waypoint
import settings

class WaypointFollower:
    def __init__(self, waypoint):
        self.waypoint = waypoint
        self.arrived = False

    def set_position(self, position):
        if self.arrived == True:
            return True

        distance = self.waypoint.position.distance(position)
        if distance <= settings.settings.arrival_radius:
            self.arrived = True

        return self.arrived