"""Part 5 — Differential drive: left/right wheel speeds, same (v, omega) world motion idea."""

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.DIFFERENTIAL,
    dt=0.02,
    differential=amr.DifferentialParams(track_width=0.4, max_wheel_speed=2.0),
)
s.forward_wheels(1.0, 1.0)  # 1 m forward (both wheels same speed)
s.turn_left(math.pi / 4, 1.0)

amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)

"""fig, ax = plt.subplots(figsize=(5, 5))
amr.plot_motion(s, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "class_differential.png"), dpi=120)
print("Done. Final pose:", s.pose)
"""