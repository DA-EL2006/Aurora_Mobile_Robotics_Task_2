#!/usr/bin/env python3
"""Several poses on one axes or on separate subplots.

Each call to :func:`amr.simulate` sets axis limits around that pose. If you draw
more than one robot on the same ``ax``, set limits yourself so everyone stays
in view.
"""

from __future__ import annotations #This helps us use class names as type labels before the classes are fully created. It stops Python from throwing a tantrum when it reads a name that it has not finished building yet.

import math #This imports the math toolkit or library having extra math features like square roots etc

import matplotlib.pyplot as plt #This imports the matplotlib.pyplot library which acts like a visualizer for the code that is written

import AuroraMR as amr #This imports the AuroraMR library and gives us access to call functions from the library.

#This is an  array of three poses, with varying directions resulting from a tweak in their values. 
poses = [
    amr.pose(0.0, 0.0, 0.0),  # north. This proves that the angle begins to read from the North. 
    amr.pose(2.5, 1.0, math.pi / 2),  # west. This pose shows the convention to be counterclockwise
    amr.pose(-1.0, 2.0, math.pi),  # south
]

# --- Same figure, one axes, multiple robots ---

fig1, ax1 = plt.subplots(figsize=(8, 8)) #This generates the one figure for the poses

#Loops through each robot's position and draw them all on the same graph
for p in poses:
    amr.simulate(p, ax=ax1, show=False, length=0.45, width=0.28)

#Gathers all the X and Y coordinates to find the outer boundaries of the robots
xs = [p.x for p in poses]
ys = [p.y for p in poses]
pad = 1.2

#Manually sets the zoom limits of the graph so that the robots fit 
ax1.set_xlim(min(xs) - pad, max(xs) + pad)
ax1.set_ylim(min(ys) - pad, max(ys) + pad)

#Adds a title to the top of this single graph and cleaning of the spacing
ax1.set_title("Three robots on one axes (limits set manually)")
fig1.tight_layout()

# --- One subplot per pose ---
fig2, axes = plt.subplots(1, len(poses), figsize=(4 * len(poses), 4))

#matches each robot position up with its own graph.
for ax, p in zip(axes, poses):

    #Runs the simulate function in the AuroraMR Library
    amr.simulate(p, ax=ax, show=False)

    #Labels each subplot with that robot's exact coordinates and angle
    ax.set_title(f"({p.x:.1f}, {p.y:.1f}), θ={p.theta:.2f}")

#Adds the title over the row of mini graphs and cleans up spacing
fig2.suptitle("Same poses in separate subplots")
fig2.tight_layout()

plt.show() #This shows the result on a display with the picture.
