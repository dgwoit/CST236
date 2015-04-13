Source Example
==============

Defensible provides functions for describing defenses.

Implementing a defense
^^^^^^^^^^^^^^^^^^^^^^

class MyDefense(Defense):
    activate(game_object)
        print 'MyDefense is activated due to game_object'

defendedArea = DefensePerimeter(0, 5) #at 0, radius of 5
defendedArea.add_defense(MyDefense())
orc = Orc(3)
defendedArea.check_for_breach(orc)

Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.Defensible
    :members:
