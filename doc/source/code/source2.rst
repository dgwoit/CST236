Source Example
==============

Source2 provides functions for describing a quadrilateral.

Determining Quadrilateral Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source2.get_quadrilateral_type` provides users with a way to provide a set of four sides
of a quadrilaterals and returns the type of quadrilateral ("rectangle", "square", or "invalid")

Rectangle Example
^^^^^^^^^^^^^^^^^

>>> from source.source2 import get_quadrilateral_type
>>> get_quadrilateral_type(1, 2, 1, 2)
'rectangle'



Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source2
    :members:

Simple Doctest
^^^^^^^^^^^^^^
>>> x = 1
>>> y = 2
>>> print x + y
3

Complex Doctest
^^^^^^^^^^^^^^^
.. testsetup:: *

    x = 1
    y = 2

.. testcode:: addition

    print x + y

.. testoutput:: addition

    3
