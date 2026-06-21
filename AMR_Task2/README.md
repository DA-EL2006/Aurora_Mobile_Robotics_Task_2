# AuroraMR Simulation Scripts

This repository contains Python scripts for simulating and visualizing Autonomous Mobile Robots (AMRs) using the **AuroraMR (`amr`)** library. It covers basic coordinate systems, managing multiple robot figures, and controlling both **Differential Drive** and **Ackermann** steering setups.

---

## Requirements

```bash
pip install AuroraMR matplotlib
```

---

## 🧭 System Rules & Coordinate Setup

* **0 Radians (0)**: Points straight **North** (+y).
* **Positive Rotation**: Turning is **Counterclockwise** (turning left increases the angle).

| Direction | Angle in Radians | Direction Vector |
| :--- | :--- | :--- |
| **North** | 0 | Facing Upwards |
| **West** | π/2 | Facing Left |
| **South** | π | Facing Downwards |
| **East** | 3π/2 (or −π/2) | Facing Right |

---

## 💻 Script Reference

### 1. Basic Positions (`pose_basics.py`)
This script introduces how to create points on a map using x, y, and an angle (theta).

```python
from __future__ import annotations # Stops Python from panicking if a class name is used early
import math # Unlocks math tools like pi
import AuroraMR as amr # Unlocks the robot toolset

# Create a position: X=1.5, Y=-0.5, Angle=pi/6
p = amr.pose(1.5, -0.5, math.pi / 6)
print("pose() ->", p)
print("  x =", p.x, "  y =", p.y, "  theta (rad) =", p.theta)

# Define standard directions
north = amr.pose(0, 0, 0)
west = amr.pose(0, 0, math.pi / 2)
```

### 2. Plotting Fleet Poses (`simulate_multiple_poses.py`)

This script takes an array of robots and shows how to draw them together on a single map, or separate them into mini-plots side-by-side.

```python
import math
import matplotlib.pyplot as plt # Unlocks the map drawing visualizer
import AuroraMR as amr

poses = [
    amr.pose(0.0, 0.0, 0.0),          # Facing North
    amr.pose(2.5, 1.0, math.pi / 2),  # Facing West
    amr.pose(-1.0, 2.0, math.pi),     # Facing South
]

# --- Approach A: All robots on ONE shared map ---
fig1, ax1 = plt.subplots(figsize=(8, 8))
for p in poses:
    amr.simulate(p, ax=ax1, show=False, length=0.45, width=0.28) # Draws them together

# --- Approach B: One mini-graph subplot per robot ---
fig2, axes = plt.subplots(1, len(poses), figsize=(4 * len(poses), 4))
for ax, p in zip(axes, poses):
    amr.simulate(p, ax=ax, show=False) # Draws them on separate mini-maps
    ax.set_title(f"({p.x:.1f}, {p.y:.1f}), θ={p.theta:.2f}")

plt.show() # Pops open the actual image window on your desktop
```

### 3. Differential Drive Simulation (`differential.py`)

Simulates a classic two-wheel robot setup controlled by manipulating left and right wheel speeds.

```python
import math
import os # Unlocks tools to talk directly to your computer system
import matplotlib.pyplot as plt
import AuroraMR as amr

# Force graphs to draw invisibly in the background (good for cloud/servers)
os.environ.setdefault("MPLBACKEND", "Agg")

s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.DIFFERENTIAL, # Selects two-wheel logic
    dt=0.02, # Time interval between calculations
    differential=amr.DifferentialParams(track_width=0.4, max_wheel_speed=2.0),
)

# Command actions
s.forward_wheels(1.0, 1.0) # Move forward 1 meter
s.turn_left(math.pi / 4, 1.0)
s.forward_wheels(2.0, 0.8)

# Run animation and print statistics to terminal
amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
```

### 4. Ackermann Steering Simulation (`Ackermann.py`)

Simulates a car-like steering vehicle layout (four wheels, front steering axle, rear driving axle).

```python
import math
import os
import matplotlib.pyplot as plt
import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.ACKERMANN, # Selects car-steering logic
    dt=0.02,
    ackermann=amr.AckermannParams(wheelbase=0.55, track_width=0.35, max_steering_angle=0.5, max_speed=1.0),
)

# Drive actions
s.forward(1.0, 0.5)
s.turn_left(math.radians(30), 0.6) # Turns left 30 degrees
s.backward(2.6, 1)

# Generate and save map layout image directly to a folder
fig, ax = plt.subplots(figsize=(5, 5))
amr.plot_motion(s, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "class_ackermann.png"), dpi=120)

amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
```

### 5. Simple Action Pattern Loop (`try.py`)

Runs a quick repetitive pattern sequence using standard motion controls to test paths.

```python
import math
import AuroraMR as amr

s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)

# Runs a repeated pattern sequence of driving forward and pivoting left
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)

# Visualizes the run session path
amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
```