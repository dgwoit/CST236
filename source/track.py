from navigation_object import NavigationObject
import datetime
from latlon import LatLon

class TrackPoint():
    def __init__(self, position):
        self.position = position
        self.datetime = datetime.datetime.utcnow()

    def encode(self):
        return {"position": self.position.encode(), "datetime": self.datetime.isoformat()}

    @staticmethod
    def decode(data):
        position = LatLon.decode(data["position"])
        dt = datetime.datetime.strptime(data["datetime"], "%Y-%m-%dT%H:%M:%S.%f")
        tp = TrackPoint(position)
        tp.datetime = dt
        return tp


class Track(NavigationObject):
    def __init__(self, id, name):
        super(Track, self).__init__(id)
        self.name = name
        self.points = []

    def add_point(self, position):
        point = TrackPoint(position)
        self.points.append(point)

    def encode(self):
        data = {"id": self.id, "name": self.name, "points": map(lambda x: x.encode(), self.points)}
        return data

    @staticmethod
    def decode(data):
        id = data["id"]
        name = data["name"]
        track = Track(id, name)
        track.points = map(lambda x: TrackPoint.decode(x), data["points"])
        return track




