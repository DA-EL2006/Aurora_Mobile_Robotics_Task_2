"""Part 6 — Ackermann: four wheels, pose at rear axle, front steers (car-like)."""

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
    amr.KinematicsModel.ACKERMANN, #kinematicsModel function specifically the ACKERMANN
    dt=0.02, #The timesteps
    ackermann=amr.AckermannParams(wheelbase=0.55, track_width=0.35, max_steering_angle=0.5, max_speed=1.0), #Collects the Ackermann Parameters by an AuroraMR function called ackermannparams
)

#This is a command in "session" to move forward by a particular distance with a particular speed 
s.forward(1.0, 0.5)
s.turn_left(math.radians(30), 0.6)
s.backward(2.6, 1)
s.turn_right(math.radians(45), 1)

#This is to plot and visualize the robot's movement graphically.
fig, ax = plt.subplots(figsize=(5, 5))
amr.plot_motion(s, ax=ax, show=False)

#This saves the image generated to the folder
fig.savefig(os.path.join(os.path.dirname(__file__), "class_ackermann.png"), dpi=120)
print("Done. Final pose:", s.pose)

#This command simulates the robot's movement and logs every frame and time of simulation.
amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
