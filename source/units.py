"""
:mod:`source.units` -- Units of Measure
=======================================
Code for system-wide units of measurement, plus conversion, parsing, and formatting of values
"""


class UnitSystem:
    """
    Defines the types of UnitSystem: Imperial, Metric, Parsec, Nautical
    """
    Imperial = 1 #gallons, miles, slugs, pounds
    Metric = 2 #liters, kilometers, kilograms, newtons
    Parsec = 3 #shouldn't this be astronomical, there is AU: Astronomical Unit
    Nautical = 4 #

class UnitSettings:
    """
    Defines the unit settings
    """
    def __init__(self):
        self._system = UnitSystem.Metric

    def set_system(self, value):
        """
        Sets the unit system to use

        :param value: unit system to use
        """
        self._system = value

    def get_system(self):
        """
        :return: UnitSystem type
        """
        return self._system

    system = property(get_system, set_system)

units = UnitSettings()
"""
global instances of UnitSettings
"""