from waypoint import Waypoint
from route import Route
from track import Track
import random
import uuid

class NavigationObjectManager:
    def __init__(self):
        self.waypoints = {}
        self.routes = {}
        self.tracks = {}

    def next_id(self):
        return str(uuid.uuid4())

    def add_waypoint(self, name, position):
        waypoint = self.new_waypoint(name, position)
        self.waypoints[waypoint.id] = waypoint
        return waypoint

    def new_waypoint(self, name, position):
        waypoint = Waypoint(self.next_id(), name, position)
        return waypoint

    def remove_waypoint(self, waypoint):
        del self.waypoints[waypoint.id]

    def create_route(self, name):
        route = Route(self.next_id(), name)
        return route

    def add_waypoint_to_route(self, route, name, position):
        waypoint = self.new_waypoint(name, position)
        route.waypoints.append(waypoint)
        return waypoint

    def commit_route(self, route):
        self.routes[route.id] = route

    def remove_route(self, route):
        del self.routes[route.id]

    def add_track(self, name):
        track = Track(self.next_id(), name)
        self.tracks[track.id] = track
        return track

    def remove_track(self, track):
        del self.tracks[track.id]

    def encode(self):
        data = {}
        data["NavObjData"] = {"waypoints": self.encode_waypoints(), "routes": self.encode_routes(),\
                              "tracks" : self.encode_tracks()}
        return data

    def encode_waypoints(self):
        return map(lambda x: x.encode(), self.waypoints.values())

    def encode_routes(self):
        return map(lambda x: x.encode(), self.routes.values())

    def encode_tracks(self):
        return map(lambda x: x.encode(), self.tracks.values())

    def decode(self, data):
        nav_obj_data = data["NavObjData"]

        self.waypoints = {}
        for wpt_datum in nav_obj_data["waypoints"]:
            waypoint = Waypoint.decode(wpt_datum)
            self.waypoints[waypoint.id] = waypoint

        self.routes = {}
        for route_datum in nav_obj_data["routes"]:
            route = Route.decode(route_datum)
            self.routes[route.id] = route

        self.tracks = {}
        for track_datum in nav_obj_data["tracks"]:
            track = Track.decode(track_datum)
            self.tracks[track.id] = track
