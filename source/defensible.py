"""
:mod:`source.Defensible` -- Defense class definitions
=====================================================

This module contains classes involved with defining defense logic and implementation
"""


from source.Positionable import *


class Defense:
    """
    Defines the interface for defense classes
    """
    def __init__(self):
        return

    def activate(self, game_object):
        """
        :function: activate

        :purpose: called when a game object triggers defenses. Overload in your implemenation to provide specific behavior.

        :param game_object: the game_object that  is cause for defenses to become activated.
        :type game_object: GameObject

        :returns: nothing
        """
        return

class DefensePerimeter(Positionable):
    """
    :class: DefensePerimeter
    :Purpose: provides a definition of a defended area specified by a location and radius

    :param position: position of the defense perimeter
    :type position: position

    :param radius: radius of the perimeter
    :type radius: int/float
    """

    def __init__(self, position, radius):
        """
        :function: __init__
        :purpose: class initializer
        :arguments:
            :param position: center of the defense perimeter area
            :type position: position

            :param radius: radius of the defense area
        """
        super(DefensePerimeter, self).__init__(position)
        self.defenses = []
        self.radius = radius

    def add_defense(self, defense):
        """
        :function: add_defense
        :purpose: adds a defense

        :param defense: the particular defense mechanism to add to this defense area

        :returns: nothing
        """
        self.defenses.append(defense)


    def check_for_breach(self, game_object):
        """
        :function: check_for_breach

        :purpose: checks to see if the specified game_object has entered the defended area

        :param game_object: the game object

        :returns: boolean, True if the game object is in the defended area
        """
        position = self.position()
        if abs(position-game_object.position()) <= self.radius:
            for defense in self.defenses:
                defense.activate(game_object)
            return True
        return False
