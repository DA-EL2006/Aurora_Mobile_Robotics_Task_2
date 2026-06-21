"""Part 5 — Differential drive: left/right wheel speeds, same (v, omega) world motion idea."""

import math #This imports the math toolkit or library having extra math features like square roots etc

import os #This tells Python to load a built-in toolkit that allows the script to talk directly to te computer's operating system

import matplotlib.pyplot as plt #This imports the matplotlib.pyplot library which acts like a visualizer for the code that is written

import AuroraMR as amr #This imports the AuroraMR library and gives us access to call functions from the library.

#os.environ opens the computer's hidden background settings panel
# MPLBACKEND is te shortform for Matplotlib Backend which decides how graphs are shown
# Agg is the specific mode that tells python to save graphs to memory or a file but does not open an  actual window on the desktop 
os.environ.setdefault("MPLBACKEND", "Agg")

#This is a function that accepts other sub functions
s = amr.MotionSession.create(
    amr.pose(0, 0, 0), #pose function, defines the position (x, y) and the angle (theta)
    amr.KinematicsModel.DIFFERENTIAL, #kinematicsModel function specifically the DIFFERENTIAL
    dt=0.02, #The timesteps
    differential=amr.DifferentialParams(track_width=0.4, max_wheel_speed=2.0), #Collects the Differential Drive Parameters by a function called differentialparams
)

#This is a command in "session" to move forward by a particular distance with a particular speed 
#s.forward_wheels(distance, speed)
s.forward_wheels(1.0, 1.0)  # 1 m forward (both wheels same speed)

s.turn_left(math.pi / 4, 1.0)

s.turn_right(math.pi / 3, 1.0)

s.forward_wheels(2.0, 0.8)

s.backward(1.2, 0.4)

#This calls a function to simulate the robot's movement
amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)

"""fig, ax = plt.subplots(figsize=(5, 5))
amr.plot_motion(s, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "class_differential.png"), dpi=120)
print("Done. Final pose:", s.pose)
"""