"""Part 6 — Ackermann: four wheels, pose at rear axle, front steers (car-like)."""

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.ACKERMANN,
    dt=0.02,
    ackermann=amr.AckermannParams(wheelbase=0.55, track_width=0.35, max_steering_angle=0.5, max_speed=1.0),
)
s.forward(1.0, 0.5)
s.turn_left(math.radians(30), 0.6)

fig, ax = plt.subplots(figsize=(5, 5))
amr.plot_motion(s, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "class_ackermann.png"), dpi=120)
print("Done. Final pose:", s.pose)
