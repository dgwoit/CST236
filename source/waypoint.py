from latlon import LatLon
from navigation_object import NavigationObject

class Waypoint(NavigationObject):
    def __init__(self, id, name, position):
        super(Waypoint, self).__init__(id)
        self._position = None
        self._name = None
        self.setPosition(position)
        self.setName(name)

    def getPosition(self):
        return self._position

    def setPosition(self, value):
        assert isinstance(value, LatLon), "{0} <> {1}".format(value, LatLon)
        self._position = value

    def getName(self):
        return self._name

    def setName(self, value):
        self._name = value

    position = property(getPosition, setPosition)
    name = property(getName, setName)

    def encode(self):
        data = {}
        data["id"] = self.id
        data["name"] = self._name
        data["position"] = self._position.encode()
        return data

    @staticmethod
    def decode(data):
        position = LatLon.decode(data["position"])
        name = data["name"]
        id = data["id"]
        waypoint = Waypoint(id, name, position)
        return waypoint