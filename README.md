# What I Learned: Simulating Mobile Robots with AuroraMR

A set of Python scripts I built to work through the fundamentals of mobile robot motion and visualization — starting from a raw pose, up through full differential-drive and Ackermann-steering simulations using the **AuroraMR (`amr`)** library.

---

## Setup

```bash
pip install AuroraMR matplotlib
```

**Gotcha:** on Ubuntu/Debian you may hit an `externally-managed-environment` error (PEP 668). Either work inside a virtual environment, or force it with:

```bash
pip install AuroraMR matplotlib --break-system-packages
```

---

## Concepts Learned

### 1. Pose Representation & Angle Conventions
*(`pose_basics.py`)*

A robot's state boils down to three numbers: `x`, `y`, `theta`. The part that actually took checking, not assuming, was the angle convention — this library treats **0 radians as North**, with rotation **counterclockwise** from there. That's different from the standard math convention (0 = East, CCW from the positive x-axis). The lesson: always confirm a library's "zero direction" by printing a known pose before writing any motion logic on top of it — assuming the wrong convention produces headings that are wrong in a way that's easy to miss until something drives the wrong way.

| Direction | Angle (rad) | Faces |
| :--- | :--- | :--- |
| North | 0 | Up |
| West | π/2 | Left |
| South | π | Down |
| East | 3π/2 (or −π/2) | Right |

```python
from __future__ import annotations
import math
import AuroraMR as amr

p = amr.pose(1.5, -0.5, math.pi / 6)
print("pose() ->", p)
print("  x =", p.x, "  y =", p.y, "  theta (rad) =", p.theta)

north = amr.pose(0, 0, 0)
west = amr.pose(0, 0, math.pi / 2)
```

### 2. Visualizing Multiple Robots at Once
*(`simulate_multiple_poses.py`)*

Two layout strategies for comparing several poses: overlay them on one shared `axes`, or give each its own subplot. The actual matplotlib lesson here is passing an *existing* `ax` into a plotting function instead of letting it create its own figure — that's the difference between several robots sharing one canvas versus a flood of separate windows.

```python
import math
import matplotlib.pyplot as plt
import AuroraMR as amr

poses = [
    amr.pose(0.0, 0.0, 0.0),
    amr.pose(2.5, 1.0, math.pi / 2),
    amr.pose(-1.0, 2.0, math.pi),
]

# Approach A: all robots on one shared map
fig1, ax1 = plt.subplots(figsize=(8, 8))
for p in poses:
    amr.simulate(p, ax=ax1, show=False, length=0.45, width=0.28)

# Approach B: one mini-subplot per robot
fig2, axes = plt.subplots(1, len(poses), figsize=(4 * len(poses), 4))
for ax, p in zip(axes, poses):
    amr.simulate(p, ax=ax, show=False)
    ax.set_title(f"({p.x:.1f}, {p.y:.1f}), θ={p.theta:.2f}")

plt.show()
```

### 3. Differential Drive Kinematics
*(`differential.py`)*

A two-wheel robot's motion is fully determined by independent left/right wheel speeds — turning comes from the *difference* between the two speeds, not from a steering mechanism. `track_width` (distance between wheels) and `max_wheel_speed` directly set how sharply it can turn: wider track or a bigger speed split tightens the turning radius. This is the model behind most warehouse and research robots, TurtleBot3 included.

```python
import math, os
import matplotlib.pyplot as plt
import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.DIFFERENTIAL,
    dt=0.02,
    differential=amr.DifferentialParams(track_width=0.4, max_wheel_speed=2.0),
)

s.forward_wheels(1.0, 1.0)
s.turn_left(math.pi / 4, 1.0)
s.forward_wheels(2.0, 0.8)

amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
```

### 4. Ackermann (Car-Like) Steering Kinematics
*(`Ackermann.py`)*

The other foundational mobile-robot model, and the one that actually matters for AV work: steering happens through a front axle, not wheel-speed differences, so the parameters shift to `wheelbase` (front-to-rear axle distance) and `max_steering_angle`. This is the direct geometric analog to how real cars steer — the natural stepping stone toward bicycle-model controllers later. Also picked up the habit of saving a static snapshot of a path (`fig.savefig(...)`) separately from the live animation, which is the difference between something you can drop into a report and something you can only watch once.

```python
import math, os
import matplotlib.pyplot as plt
import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")

s = amr.MotionSession.create(
    amr.pose(0, 0, 0),
    amr.KinematicsModel.ACKERMANN,
    dt=0.02,
    ackermann=amr.AckermannParams(wheelbase=0.55, track_width=0.35, max_steering_angle=0.5, max_speed=1.0),
)

s.forward(1.0, 0.5)
s.turn_left(math.radians(30), 0.6)
s.backward(2.6, 1)

fig, ax = plt.subplots(figsize=(5, 5))
amr.plot_motion(s, ax=ax, show=False)
fig.savefig(os.path.join(os.path.dirname(__file__), "class_ackermann.png"), dpi=120)

amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
```

### 5. Scripted Motion Sequences
*(`try.py`)*

Chaining `forward()`/`turn_left()` calls into a repeated pattern — the simplest possible "scripted behavior," with zero feedback or sensing involved yet. 
```python
import math
import AuroraMR as amr

s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)

s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)
s.forward(0.8, 0.5)
s.turn_left(math.pi / 3, 0.9)
s.forward(0.4, 0.5)

amr.play_motion(s, interval_ms=30, log=True, log_every_n_frames=10, show=True)
```

---
