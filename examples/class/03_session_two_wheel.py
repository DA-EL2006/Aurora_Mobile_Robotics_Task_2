"""Part 3 — MotionSession with TWO_WHEEL: (v, omega) model, two tire traces."""

import math

import AuroraMR as amr

s = amr.MotionSession.create(amr.pose(0, 0, 0), 
                             amr.KinematicsModel.TWO_WHEEL, 
                             dt=0.02)
s.forward(1.0, 0.5)  # 1 m forward at 0.5 m/s
s.turn_left(math.pi / 2, 0.8)  # 90° left
print("After motion:", s.pose)
print("Number of stored poses:", len(s.poses))
