"""Part 2 — Draw one robot (or pointer) at a pose.

Use show=True in a normal desktop session to open a window. show=False is safe in headless runs.
"""

import math

import AuroraMR as amr

p = amr.pose(0.0, 0.0, math.pi / 4)  # northeast-ish heading
# style="robot" is default; use style="pointer" for a simple arrow
amr.simulate(p, show=False)
print("To see the window, use: amr.simulate(p)  or  amr.simulate(p, show=True)")
