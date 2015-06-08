from waypoint import Waypoint
from navigation_obect import NavigationObject

class Route(NavigationObject):
    def __init__(self, id, name):
        super(Route, self).__init__(id)
        self.name = name
        self.waypoints = []

    def encode(self):
        data = {}
        data["id"] = self.id
        data["name"] = self.name
        data["waypoints"] = self.encode_waypoints()
        return data

    def encode_waypoints(self):
        data = []
        for waypoint in self.waypoints:
            data.append(waypoint.encode())

        return data

    @staticmethod
    def decode(data):
        id = data["id"]
        name = data["name"]
        route = Route(id, name)
        for waypoint_datum in data["waypoints"]:
            route.waypoints.append(Waypoint.decode(waypoint_datum))

        return route


