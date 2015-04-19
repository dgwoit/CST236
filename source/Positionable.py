"""

"""

class Positionable(object):
    def __init__(self, position):
        self._position = position

    def position(self):
        return self._position

    def getDistance(self, anotherPosition):
        return abs(self._position - anotherPosition)