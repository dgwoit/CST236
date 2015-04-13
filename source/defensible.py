"""
:mod:`source.Defensible` -- Defense class definitions
============================================

This module contains classes involved with defining defense logic and implementation
"""


from Positionable import *

"""
:class:'Defense'
:Purpose: Defines the interface for defense classes
"""
class Defense:
    def __init__(self):
        return

    """
    :function: activate
    :purpose: called when a game object triggers defenses. Overload in your implemenation to provide specific behavior.
    :arguments:
        :param game_object: the game_object that  is cause for defenses to become activated.
    :returns: nothing
    """
    def activate(self, game_object):
        return

"""
:class: DefensePerimeter
:Purpose: provides a definition of a defended area specified by a location and radius
"""
class DefensePerimeter(Positionable):
    """
    :function: __init__
    :purpose: class initializer
    :arguments:
        :param position: center of the defense perimeter area
        :param radius: radius of the defense area
    """
    def __init__(self, position, radius):
        super(DefensePerimeter, self).__init__(position)
        self.defenses = []
        self.radius = radius

    """
    :function: add_defense
    :purpose: adds a defense
    :arguments:
        :param defense: the particular defense mechanism to add to this defense area
    :returns: nothing
    """
    def add_defense(self, defense):
        self.defenses.append(defense)

    """
    :function: check_for_breach
    :purpose: checks to see if the specified game_object has entered the defended area
    :argument game_object: the game object
    :returns: boolean, True if the game object is in the defended area
    """
    def check_for_breach(self, game_object):
        position = self.position()
        if abs(position-game_object.position()) <= self.radius:
            for defense in self.defenses:
                defense.activate(game_object)
            return True
        return False
