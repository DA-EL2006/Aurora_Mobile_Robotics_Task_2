"""Part 1 — Planar pose: (x, y) and heading theta (radians, CCW from north / +y)."""

import math

import AuroraMR as amr

#Pose (5, 1, 270)
p = amr.pose(5, 1,  270* math.pi / 180)  # facing north

amr.simulate(p, show=True)