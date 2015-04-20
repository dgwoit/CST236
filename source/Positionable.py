"""
:mod:`source.Positionable` -- mixin for positionable objects
============================================
"""


class Positionable(object):
    """
    initializes the positionable object with a position

    :param position: position
    """
    def __init__(self, position):
        self._position = position

    def position(self):
        """

        :return: the position
        """
        return self._position

    def getDistance(self, anotherPosition):
        """

        :param anotherPosition: position of something else
        :type anotherPosition: Positionable

        :return: absolute difference of the two positions
        """
        return abs(self._position - anotherPosition)