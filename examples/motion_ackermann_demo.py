#!/usr/bin/env python3
"""Four-wheel Ackermann: rear axle pose, front wheels steer; four dotted tire traces."""

from __future__ import annotations

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

params = amr.AckermannParams(
    wheelbase=0.55,
    track_width=0.36,
    max_steering_angle=0.5,
    max_speed=1.0,
)
session = amr.MotionSession.create(
    amr.pose(0.0, 0.0, 0.0),
    amr.KinematicsModel.ACKERMANN,
    dt=0.02,
    ackermann=params,
)

session.forward(2.0, 0.6)
session.turn_left(math.radians(35), 0.8)
session.forward(1.5, 0.5)

fig, ax = plt.subplots(figsize=(8, 8))
amr.plot_motion(session, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_ackermann_demo.png"), dpi=150)
print("Saved motion_ackermann_demo.png")
