"""Part 8 — Live animation + terminal 'teaching' logs (run where a GUI is available)."""

import math

import AuroraMR as amr

# Build a path (see 03_session_two_wheel.py)
s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)

# Set MPLBACKEND if you have no display, or use show=False to skip the window
# and still get logs printed to the terminal
amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
