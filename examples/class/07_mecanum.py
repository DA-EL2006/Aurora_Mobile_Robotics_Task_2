"""Part 7 — Mecanum: omni platform; can strafe and rotate. Four corner wheel traces."""

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.MECANUM,
    dt=0.02,
    mecanum=amr.MecanumParams(half_length_y=0.25, half_width_x=0.2, max_wheel_speed=2.5),
)

s.strafe_right(4, 0.5)  # slide sideways (body +x in world for this call pattern)

amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
