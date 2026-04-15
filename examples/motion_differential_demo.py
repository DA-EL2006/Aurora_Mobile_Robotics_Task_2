#!/usr/bin/env python3
"""Differential drive: wheel-based moves and dotted left/right tire paths."""

from __future__ import annotations

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

params = amr.DifferentialParams(track_width=0.4, wheel_radius=0.08, max_wheel_speed=2.0)
session = amr.MotionSession.create(
    amr.pose(0.0, 0.0, 0.0),
    amr.KinematicsModel.DIFFERENTIAL,
    dt=0.012,
    differential=params,
)

session.forward_wheels(1.2, 1.0)
session.turn_right(math.pi / 3, 1.2)
session.differential_drive_wheels(0.3, 1.2, duration=1.5)
session.forward(0.8, 0.5)

fig, ax = plt.subplots(figsize=(8, 8))
amr.plot_motion(session, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "motion_differential_demo.png"), dpi=150)
print("Saved motion_differential_demo.png")
