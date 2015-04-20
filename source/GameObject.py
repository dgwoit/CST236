"""
:mod:`source.GameObject` -- GameObject class definitions
============================================

Provides definitions of objects that are in play
"""

from source.Positionable import *
from random import Random

class IDFactory:
    """
    IDFactory
    """
    def __init__(self):
        self.identifier = 0

    def get_id(self):
        """
        returns the next identifier

        :returns: int
        """
        self.identifier += 1
        return self.identifier

"""
global instance of the IDFactory
"""
idFactory = IDFactory()

class Alive(object):
    """
    Provides the life state of a class
    """
    def __init__(self):
        self.alive = True

    def is_alive(self):
        """
        :returns: the life state
        :rtype: bool
        """
        return self.alive

    def animate(self):
        """
        changes object to living
        """
        self.alive = True

    def terminate(self):
        """
        changes object to non-living
        """
        self.alive = False

class GameObject(Positionable, Alive):
    """
    Base class for any object in the game, Orc or otherwise

    :param position: location of the object in the game
    :type position: position
    """
    def __init__(self, position):
        super(GameObject, self).__init__(position)
        self._id = idFactory.get_id()

    def get_id(self):
        """
        :returns: the identifier for the game object
        :rtype: int
        """
        return self._id

    id = property(get_id)

class OrcType:
    """
    enumerated orc types
    """
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    violet = 6
    grey = 7
    white = 8

class OrcFactory:
    """
    OrcFactory
    """
    def __init__(self):
        self.identifier = 0
        self.orcs = {}

    def spawn_orc(self, position, velocity=0, type=OrcType.red):
        """
        Creates an Orc of the specified values adding it to the list of Orcs

        :param position: position
        :type position:

        :returns: an Orc
        :rtype Orc:
        """
        orc = Orc(position, velocity, type)
        self.orcs[orc.id] = orc
        return orc

    def remove_orc(self, id):
        """
        Removes and Orc from the list of Orcs

        :param id: identifier
        :type id: int
        """
        del self.orcs[id]

    def get_orc(self, id):
        """
        :param id: identifier of the Orc to retrieve
        :type id: int

        :returns: the orc
        :rtype: OrcFactory
        """
        return self.orcs[id]

    def terminate_orc(self, id):
        """
        terminates the specified Orc, removing it fro the list of Orcs

        :param id: identifier of the Orc
        :type id: int
        """
        orc = self.orcs[id]
        self.remove_orc(id)
        orc.terminate()

"""
OrcFactory global instance
"""
orcFactory = OrcFactory()

class OrcGenerator:
    """
    OrcGenerator
    """
    def generate_orcs_randomly(self, num):
        """
        generate_orcs_randomly

        :param num: Number of orcs to generate
        :type num: int

        :return: list of orcs
        :rtype: [Orc]
        """

        orcs = []
        for x in range(0, num):
            random = Random()
            position = random.randint(-10,10)
            orcs.append(orcFactory.spawn_orc(position))
        return orcs

class Orc(GameObject):
    """
    Ininitializes an Orc to the specified properties

    :param position: position
    :type position: position

    :param velocity: velocity
    :type velocity: velocity

    :param type: type of orc
    :type type: OrcType
    """
    def __init__(self, position, velocity=0, type=OrcType.red):
        super(Orc, self).__init__(position)
        super(Orc, self).animate()
        self._velocity = velocity
        self._type = type
        self._priority = 0

    def get_velocity(self):
        """
        :return: the velocity
        :rtype: velocity
        """
        return self._velocity

    velocity = property(get_velocity)

    def get_type(self):
        """
        :return: the type of Orc
        :rtype: OrcType
        """
        return self._type

    type = property(get_type)

    def terminate(self):
        """
        causes the Orc to become deceased
        """
        super(Orc, self).terminate()

    def set_priority(self, value):
        """
        Sets the tracking priority for the Orc

        :param value: tracking priority
        :type value: int
        """
        self._priority = value

    def get_priority(self):
        """
        :return: tracking priority
        :rtype: int
        """
        return self._priority

    priority = property(get_priority, set_priority)