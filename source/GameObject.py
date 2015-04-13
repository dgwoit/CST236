"""
:mod:`source.GameObject` -- GameObject class definitions
============================================

Provides definitions of objects that are in play
"""

from source.Positionable import *


class GameObject(Positionable):
    def __init__(self, position):
        super(Positionable, self).__init__(position)

"""
Note: probably should create some sort of character/non-playing character type
"""
class Orc(GameObject):
    def __init__(self, position):
        super(GameObject, self).__init__(position)