"""
:mod:`source.GameObject` -- GameObject class definitions
============================================

Provides definitions of objects that are in play
"""

from source.Positionable import *

class IDFactory:
    def __init__(self):
        self.identifier = 0
    def get_id(self):
        self.identifier += 1
        return self.identifier




idFactory = IDFactory()

class Alive(object):
    def __init__(self):
        self.alive = True

    def is_alive(self):
        return self.alive

    def animate(self):
        self.alive = True

    def terminate(self):
        self.alive = False

class GameObject(Positionable, Alive):
    def __init__(self, position):
        super(GameObject, self).__init__(position)
        self._id = idFactory.get_id()

    def get_id(self):
        return self._id

    id = property(get_id)

class OrcType:
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    violet = 6
    grey = 7
    white = 8

class OrcFactory:
    def __init__(self):
        self.identifier = 0
        self.orcs = {}

    def spawn_orc(self, position, velocity=0, type=OrcType.red):
        orc = Orc(position, velocity, type)
        self.orcs[orc.id] = orc
        return orc
    def remove_orc(self, id):
        del self.orcs[id]
    def terminate_orc(self, id):
        orc = self.orcs[id]
        self.remove_orc(id)
        orc.terminate()

orcFactory = OrcFactory()

class Orc(GameObject):
    def __init__(self, position, velocity=0, type=OrcType.red):
        super(Orc, self).__init__(position)
        super(Orc, self).animate()
        self._velocity = velocity
        self._type = type
        self._priority = 0

    def get_velocity(self):
        return self._velocity

    velocity = property(get_velocity)

    def get_type(self):
        return self._type

    type = property(get_type)

    def terminate(self):
        super(Orc, self).terminate()

    def set_priority(self, value):
        self._priority = value

    def get_priority(self):
        return self._priority

    priority = property(get_priority, set_priority)