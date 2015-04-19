"""
Units of Measure
"""

class UnitSystem:
    Imperial = 1 #gallons, miles, slugs, pounds
    Metric = 2 #liters, kilometers, kilograms, newtons
    Parsec = 3 #shouldn't this be astronimical, there is AU: Astronomical Unit
    Nautical = 4 #

class UnitSettings:
    def __init__(self):
        self._system = UnitSystem.Metric

    def set_system(self, value):
        self._system = value

    def get_system(self):
        return self._system

    system = property(get_system, set_system)

units = UnitSettings()