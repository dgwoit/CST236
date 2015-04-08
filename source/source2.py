"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set of 4 sides of a quadrilateral is a rectangle, or a square
"""

def get_quadrilateral_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given quadrilateral is equilateral, scalene or Isosceles

    :param a: line a
    :type a: float or int

    :param b: line b
    :type b: float or int

    :param c: line c
    :type c: float or int

    :return: "square", "rectangle", or "invalid"
    :rtype: str
    """

    if isinstance(a, dict) and len(a.keys()) == 4:
        values = []
        for value in a.values():
            values.append(value)
        a = values

    if isinstance(a, (tuple, list)) and len(a) == 4:
        d = a[3]
        c = a[2]
        b = a[1]
        a = a[0]

    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)) and isinstance(d, (int, float))):
        return "invalid"

    if a <= 0 or b <= 0 or c <= 0 or d <= 0:
        return "invalid"

    if a == c and b == d:
        if a != b:
            return "rectangle"
        else:
            return "square"

    return "invalid"
