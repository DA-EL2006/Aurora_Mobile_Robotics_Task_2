# AuroraMR (AMR-lib)

**AuroraMR** is a Python library for **2D autonomous mobile robotics**: planar poses, kinematic simulation, motion scripting, matplotlib visualization, and optional **terminal “teaching” logs** during live playback. It targets courses, labs, and quick prototyping.

The package is published on PyPI as **`AuroraMR`**; import it as either `import AuroraMR as amr` or `import amr` (same public API).

---

## Features

| Area | What you get |
|------|----------------|
| **Pose** | Immutable `Pose(x, y, theta)` with heading **θ counterclockwise from north** (+y). |
| **Visualization** | `simulate()` draws a robot or pointer at a pose; customizable figure and style. |
| **Kinematics** | Two-wheel \((v,\omega)\), differential drive, Ackermann (4-wheel, rear axle pose), and mecanum (X-config). |
| **Motion** | `MotionSession` records trajectories, wheel contact traces, and supports `forward`, turns, model-specific commands, and `drive_to_pose` (where implemented). |
| **Plots** | Static `plot_motion()` with dotted tire traces; live `play_motion()` animation. |
| **Teaching logs** | Optional formatted logs during playback (`log=True`, `PlaybackLogOptions`, throttling). |

**Dependencies:** Python ≥ 3.10, NumPy, Matplotlib.

---

## Installation

### From PyPI

```bash
pip install AuroraMR
```

### From source (editable, for development)

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
# If the Git repo root is this library folder (it contains pyproject.toml), stay here.
# If AuroraMR lives inside a monorepo, cd into the AMR-lib (or equivalent) subfolder first.
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

Replace the clone URL with your real GitHub repository after you create it.

---

## Coordinate frame (read this once)

- **World:** \(x\) right, \(y\) up (north).
- **Heading θ:** radians, **counterclockwise from +y** (north).  
  Examples: θ = 0 faces north, θ = π/2 faces west, π faces south, 3π/2 (or −π/2) faces east.

This matches the integration and drawing code throughout the library.

---

## Quick start

```python
import math
import AuroraMR as amr

session = amr.MotionSession.create(
    amr.pose(0.0, 0.0, 0.0),
    amr.KinematicsModel.TWO_WHEEL,
    dt=0.02,
)
session.forward(1.0, 0.5)
session.turn_left(math.pi / 2, 1.0)

amr.plot_motion(session)  # static figure
# amr.play_motion(session, log=True, show=True)  # live animation + terminal logs
```

See `examples/minimal_drive_and_play.py` for a short path with turns, a U-turn, 2× playback, and logging.

---

## Kinematic models (`KinematicsModel`)

| Member | Role |
|--------|------|
| **`TWO_WHEEL`** | Planar two-wheel / \((v,\omega)\) model; left/right traces use `track_width`. (`UNICYCLE` is a legacy alias, same value.) |
| **`DIFFERENTIAL`** | Left/right wheel speeds; uses `DifferentialParams`. |
| **`ACKERMANN`** | Four wheels, pose at rear axle, front steering; `AckermannParams`. |
| **`BICYCLE`** | Legacy name; maps to Ackermann-style parameters via `BicycleParams` → `AckermannParams`. |
| **`MECANUM`** | X-config mecanum at center; `MecanumParams`. |

Parameter dataclasses: `TwoWheelParams` / `UnicycleParams` (same type), `DifferentialParams`, `AckermannParams`, `BicycleParams`, `MecanumParams`.

`KinematicsKind` is kept as an alias of `KinematicsModel` for older code.

---

## Main API (lazy exports)

Access these from `amr` after `import AuroraMR as amr` (or `import amr`):

- **Pose:** `Pose`, `pose`
- **Drawing a single pose:** `simulate`
- **Session & motion:** `MotionSession`
- **Plots:** `plot_motion`
- **Live animation:** `play_motion`, `play_all_kinematics_live`, `play_motion_by_kind`
- **Logging:** `PlaybackLogOptions`, `effective_interval_ms`

Playback helpers accept `interval_ms`, `playback_speed` (effective interval = base / speed), and logging flags such as `log`, `log_every_n_frames`, `log_detailed`, `log_file`.

---

## Examples

The `examples/` directory includes:

- **Basics:** `pose_basics.py`, `simulate_robot_default.py`, `simulate_custom_figure.py`, `simulate_headless_default_figure.py`
- **Motion / kinematics:** `motion_two_wheel_demo.py`, `motion_differential_demo.py`, `motion_ackermann_demo.py`, `motion_mecanum_demo.py`, `motion_bicycle_demo.py`, `minimal_drive_and_play.py`
- **Live demos:** `live_kinematics_demo.py` (CLI: mode, speed, logs, optional save), `live_ackermann_quick.py`, `live_ackermann_session.py`
- **Scratch:** `examples/simple/test.py` — small script for local experiments
- **Teaching / class:** `examples/class/` — numbered short scripts (`01_pose.py` … `08_playback_log.py`); see `examples/class/README.md`
- **Advanced:** `examples/advanced/` — logging tee, `drive_to_pose`, mecanum/differential patterns, 4-model subplot, CSV export, `plot_motion` styling; see `examples/advanced/README.md`

Run from the repo root with `PYTHONPATH=.` or after `pip install -e .` so `AuroraMR` resolves.

**Headless environments:** set `MPLBACKEND=Agg` if you do not have a display (saving figures only). Interactive `play_motion(..., show=True)` needs a GUI backend.

### Example gallery (static PNGs)

These images are produced by the matching scripts (same base name, `.py` → `.png`). They use the **world frame** (\(x\) right, \(y\) up), **θ** counterclockwise from north, the robot outline, and (for motion demos) **dotted tire-contact traces** along the path.

#### `simulate_headless_default_figure.py` → `headless_default_figure.png`

![Default simulate output (headless)](examples/headless_default_figure.png)

Single pose, default **robot** polygon from `simulate()` when Matplotlib creates the figure for you. Use this pattern with `MPLBACKEND=Agg` for CI or saved figures without a GUI.

#### `simulate_custom_figure.py` → `custom_figure_example.png`

![Custom figure and axes](examples/custom_figure_example.png)

You supply your own `fig` and `ax`; `simulate(..., ax=ax, show=False)` draws into your layout—handy for dashboards or multi-panel figures.

#### `motion_two_wheel_demo.py` → `motion_two_wheel_demo.png`

![Two-wheel kinematics session](examples/motion_two_wheel_demo.png)

**`KinematicsModel.TWO_WHEEL`**: \((v,\omega)\) motion with left/right wheel traces—forward, turn, backward, and `drive_to_pose`.

#### `motion_differential_demo.py` → `motion_differential_demo.png`

![Differential drive session](examples/motion_differential_demo.png)

**`DIFFERENTIAL`**: wheel-speed commands, straight segments and turns; two drive contact traces.

#### `motion_ackermann_demo.py` → `motion_ackermann_demo.png`

![Ackermann four-wheel session](examples/motion_ackermann_demo.png)

**`ACKERMANN`**: pose at the rear axle, four wheels, Ackermann-style front steering and arcs.

#### `motion_bicycle_demo.py` → `motion_bicycle_demo.png`

![Legacy bicycle params → Ackermann geometry](examples/motion_bicycle_demo.png)

**`BICYCLE`** with `BicycleParams`: legacy API that maps to the same four-wheel Ackermann visualization as above.

#### `motion_mecanum_demo.py` → `motion_mecanum_demo.png`

![Mecanum omnidirectional session](examples/motion_mecanum_demo.png)

**`MECANUM`**: X-config wheels at the robot center; path includes strafe and rotation; four corner traces.

---

**Regenerate all gallery PNGs** (from the `AMR-lib` folder that contains `pyproject.toml`):

```bash
export MPLBACKEND=Agg PYTHONPATH=.
python examples/simulate_headless_default_figure.py
python examples/simulate_custom_figure.py
python examples/motion_two_wheel_demo.py
python examples/motion_differential_demo.py
python examples/motion_ackermann_demo.py
python examples/motion_bicycle_demo.py
python examples/motion_mecanum_demo.py
```

Live animations and saved **videos** (`*.mp4` / `*.gif` from `live_kinematics_demo.py --save …`) are not shown here; generate them locally if you need clips for talks or docs.

---

## Development & tests

```bash
pip install -e ".[dev]"
# If pytest picks up unrelated plugins (e.g. ROS), disable autoload:
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest
```

Or use the helper script:

```bash
./scripts/run_tests.sh -q
```

---

## Project layout

```
AMR-lib/
├── pyproject.toml      # package AuroraMR, wheels include amr + AuroraMR
├── amr/                # main package (kinematics, motion, plot, live, playback_log, simulate)
├── AuroraMR/           # thin shim, same API as amr
├── tests/
├── examples/
└── scripts/run_tests.sh
```

---

## Contributing & GitHub

1. Add a **LICENSE** file in the repository root if you have not already (choose MIT, Apache-2.0, etc., and match `pyproject.toml` if you add SPDX metadata later).
2. Push this folder (or the monorepo path you use) to GitHub; point the README clone URL to the real repo.
3. Pull requests: run tests as above; keep examples runnable with documented assumptions (GUI vs headless).

---

## Version

Current version is defined in `pyproject.toml` (`[project].version`).
