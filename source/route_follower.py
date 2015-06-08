from waypoint_follower import WaypointFollower


class RouteFollower:
    def __init__(self, route):
        self.route = route
        self.waypoint_active_callback = None
        self.destination_arrived_callback = None
        self.destination_arrived = False
        self.waypoint_follower = None
        self.active_waypoint = None

        self.active_waypoint = self.route.waypoints[0]
        self.fire_waypoint_active(self.active_waypoint)
        self.waypoint_follower = WaypointFollower(self.active_waypoint)


    def set_position(self, position):
        #nothing to be done if we hav arrived at the destination
        if self.destination_arrived == True:
            return True

        #if we haven't started tracking a waypoint find the first logical waypoint
        if self.waypoint_follower == None:
            self.active_waypoint = self.route.waypoints[0]
            self.fire_waypoint_active(self.active_waypoint)
            self.waypoint_follower = WaypointFollower(self.active_waypoint)
        else:
            if self.waypoint_follower.set_position(position):
                index = self.route.waypoints.index(self.waypoint_follower.waypoint)
                if index + 1 < len(self.route.waypoints):
                    self.active_waypoint = self.route.waypoints[index+1]
                    self.fire_waypoint_active(self.active_waypoint)
                    self.waypoint_follower = WaypointFollower(self.active_waypoint)
                elif self.destination_arrived == False:
                    self.fire_destination_arrived()

    def fire_waypoint_active(self, waypoint):
        if None != self.waypoint_active_callback:
            self.waypoint_active_callback(waypoint)

    def fire_destination_arrived(self):
        if None != self.destination_arrived_callback:
            self.destination_arrived_callback()
