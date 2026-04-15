#!/usr/bin/env python3
"""Legacy alias: use :class:`AckermannParams` and :attr:`KinematicsModel.ACKERMANN` instead."""

from __future__ import annotations

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

params = amr.BicycleParams(
    wheelbase=0.55,
    rear_track_width=0.36,
    max_steering_angle=0.5,
    max_speed=1.0,
)
session = amr.MotionSession.create(
    amr.pose(0.0, 0.0, 0.0),
    amr.KinematicsModel.BICYCLE,
    dt=0.02,
    bicycle=params,
)

session.forward(2.0, 0.6)
session.turn_left(math.radians(40), 0.8)
session.forward(1.5, 0.5)

fig, ax = plt.subplots(figsize=(8, 8))
amr.plot_motion(session, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_bicycle_demo.png"), dpi=150)
print("Saved motion_bicycle_demo.png (BicycleParams → Ackermann four-wheel)")
