# Class examples: AuroraMR in small steps

This folder holds **eight very short scripts**, each aimed at one idea. They are meant for lectures or labs: open the file, read the top comment, run it, then tweak numbers.

**Library:** [AuroraMR](https://pypi.org/project/AuroraMR/) (`import AuroraMR as amr` or `import amr`).

---

## How to run

From the project root (the directory that contains `pyproject.toml`):

```bash
cd /path/to/AMR-lib
python -m venv .venv && source .venv/bin/activate   # optional
pip install -e .                                    # or: pip install AuroraMR
PYTHONPATH=. python examples/class/01_pose.py
```

If the package is already installed, you can run from anywhere:

```bash
python /path/to/AMR-lib/examples/class/01_pose.py
```

Use the file names in order: **01 → 08** matches how the API layers build up (pose → draw → session → static plot → more kinematics → live playback).

---

## One coordinate rule (all scripts)

- World: **x** to the right, **y** up (north).
- **θ** (theta): heading in **radians**, **counterclockwise from +y** (north).  
  So θ = 0 faces north, θ = π/2 faces west, π faces south, 3π/2 (or −π/2) faces east.

---

## Script guide

### `01_pose.py` — Poses only

- **You learn:** `amr.pose(x, y, theta)` and the optional `amr.Pose(...)` type.
- **No matplotlib.** Everything prints in the terminal.
- **Try:** change `1.0, 2.0, 0.0` and the second pose’s `math.pi / 2` to see how θ maps to “which way the nose points.”

---

### `02_simulate.py` — One picture: robot at one pose

- **You learn:** `amr.simulate(pose, …)` to draw a body (default **robot** polygon) or a **pointer** (`style="pointer"`).
- **Window:** the script uses `show=False` so it also runs in headless environments. In class, use `amr.simulate(p)` or `show=True` to open a real window and show the same drawing.

---

### `03_session_two_wheel.py` — Record a path (no plot yet)

- **You learn:** `MotionSession.create(...)`, `KinematicsModel.TWO_WHEEL`, and simple commands: `forward`, `turn_left`.
- **`TWO_WHEEL`** is the planar *two-wheel* / \((v, \omega)\) model. The session stores a list of poses and wheel contact traces.
- **Try:** change distances, speeds, or add `s.turn_right(...)`.

---

### `04_plot_static.py` — Static trajectory plot

- **You learn:** `amr.plot_motion(session, ax=..., show=False)` after you have a `MotionSession`.
- **File:** writes **`class_plot.png`** next to this script (uses `MPLBACKEND=Agg` so no window is required).
- **You see:** path, robot shape at the end, dotted **tire** traces.

---

### `05_differential.py` — Differential drive

- **You learn:** `KinematicsModel.DIFFERENTIAL` with `DifferentialParams` (track width, max wheel speed, etc.) and `forward_wheels`, `turn_left` as appropriate for that model.
- **File:** saves **`class_differential.png`**.

---

### `06_ackermann.py` — Car-like (Ackermann) steering

- **You learn:** `KinematicsModel.ACKERMANN` with `AckermannParams` (wheelbase, track, max steer angle). Pose is at the **rear axle**; four wheels and front steering are drawn in plots.
- **File:** saves **`class_ackermann.png`**.

---

### `07_mecanum.py` — Mecanum (holonomic) platform

- **You learn:** `KinematicsModel.MECANUM` with `MecanumParams` and moving **forward** and **strafe** (`strafe_right`).  
- This model uses four corner wheel traces; the robot can do sideways motion, unlike the two-wheel or Ackermann car paths alone.
- **File:** saves **`class_mecanum.png`**.

---

### `08_playback_log.py` — Live animation + teach-in logs

- **You learn:** `amr.play_motion(session, log=True, …)` to replay the stored session as an **animation** and print **formatted notes** in the terminal (frame summaries, parameters, throttled with `log_every_n_frames`).
- **GUI:** `show=True` opens a matplotlib window. On a **headless** server, set `show=False` to skip the window; you may still get log text depending on the backend. For a full in-class demo, run on a laptop with a display.
- **Try:** change `interval_ms` or add `playback_speed=2.0` for a faster replay.

---

## Output files (scripts 04–07)

| Script   | Default PNG (next to the `.py` file) |
|----------|--------------------------------------|
| 04 | `class_plot.png`         |
| 05 | `class_differential.png` |
| 06 | `class_ackermann.png`   |
| 07 | `class_mecanum.png`     |

Re-running the script overwrites the PNG. Add these filenames to **`.gitignore`** if you do not want them in version control, or keep them for student hand-ins.

---

## If something errors

- **`ModuleNotFoundError: AuroraMR`:** install the package (`pip install -e .` from the repo root) or set `PYTHONPATH` to the repo root.
- **No window / “cannot show”:** scripts 04–07 force a non-interactive backend where needed; 02 and 08 are meant to use a real display when you want animation or `simulate` with `show=True`.
- **More examples:** the parent `examples/` directory has longer demos (live kinematics, Ackermann sessions, etc.).

For the full project overview, see the main **[README.md](../../README.md)** in the repository root.
