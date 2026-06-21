#!/usr/bin/env python3
"""Create poses and read ``x``, ``y``, ``theta``.

Heading convention: ``theta`` is in radians; ``0`` faces north (+y); increasing
counterclockwise (west = π/2, east = 3π/2 or −π/2).

Using ``import AuroraMR as amr`` does not load matplotlib until you call
``amr.simulate``. You can also use ``import amr`` or ``from amr.pose import Pose, pose``.
"""

from __future__ import annotations #This helps us use class names as type labels before the classes are fully created. It stops Python from throwing a tantrum when it reads a name that it has not finished building yet.

import math #This imports the math toolkit or library having extra math features like square roots etc

import AuroraMR as amr #This imports the AuroraMR library and gives us access to call functions from the library.

# Preferred: factory function
p = amr.pose(1.5, -0.5, math.pi / 6) # The pose function from the AuroraMR takes in three values, x, y and theta which are assigned to a variable p

#The following functions print the pose x, y and theta
print("pose() ->", p)

print("  x =", p.x, "  y =", p.y, "  theta (rad) =", p.theta)

# Instantiate ``Pose`` directly if you already have values
q = amr.Pose(x=0.0, y=0.0, theta=0.0)
print("Pose(...) ->", q)

# Common headings
north = amr.pose(0, 0, 0)
west = amr.pose(0, 0, math.pi / 2)
south = amr.pose(0, 0, math.pi)
east = amr.pose(0, 0, 3 * math.pi / 2)
print("north theta=0:", north.theta, " west theta=π/2:", west.theta)
