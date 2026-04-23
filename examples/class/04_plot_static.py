"""Part 4 — Static path plot: full trajectory and dotted tire contacts (no animation)."""

import math
import os

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")  # no window; comment out to use your screen

s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)
s.forward(1.2, 0.5)
s.turn_left(math.pi / 2, 1.0)
s.forward(0.8, 0.5)

fig, ax = plt.subplots(figsize=(5, 5))
amr.plot_motion(s, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "class_plot.png"), dpi=120)
print("Wrote", os.path.join(os.path.dirname(__file__), "class_plot.png"))
