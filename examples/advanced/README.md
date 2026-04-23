# Advanced examples

These scripts go **beyond** [`examples/class/`](../class/): logging plumbing, holonomic planning hooks, multi-subplot comparisons, data export, and styling APIs.

**Prerequisite:** work through the numbered class scripts or the [main README](../../README.md) so **pose conventions** and **`MotionSession`** are already familiar.

---

## How to run

From the repository root (folder with `pyproject.toml`):

```bash
pip install -e .    # or: pip install AuroraMR
PYTHONPATH=. python examples/advanced/01_playback_logoptions_and_file.py
```

Most scripts set `MPLBACKEND=Agg` and write outputs next to the script (see below). For `play_motion` with a **visible** window, drop `Agg` and use `show=True` (not all advanced scripts expose that; copy the pattern into your own file).

---

## Scripts

| File | Topic |
|------|--------|
| **`01_playback_logoptions_and_file.py`** | **`PlaybackLogOptions`**: `detailed_block`, `include_tire_sample`, custom `every_n_frames`. Tee’s log text to **stdout and** `adv_playback.log` via a small `Tee` class. Uses `play_motion(..., log_options=opts, show=False)`. |
| **`02_drive_to_pose_tolerances.py`** | **`drive_to_pose`** on **TWO_WHEEL**: `position_tol`, `angle_tol`, prints errors vs goal, saves `adv_drive_to_pose.png` with goal marker. |
| **`03_mecanum_holonomic.py`** | **Mecanum**: `strafe_right` (negative → strafe left), **`mecanum_drive_wheels`**, then a short **`drive_to_pose`** with a nearby goal (controller is simple—see comments). |
| **`04_differential_wheels_timebased.py`** | **`differential_drive_wheels(v_left, v_right, duration)`** for timed arcs, plus `forward_wheels` / `turn_left`. |
| **`05_four_kinematics_subplots.py`** | One **2×2** figure: **TWO_WHEEL**, **DIFFERENTIAL**, **ACKERMANN**, **MECANUM** short paths side by side (`adv_four_kinematics.png`). |
| **`06_export_trajectory_csv.py`** | Treat the session as data: iterate **`session.poses`**, write **`adv_trajectory.csv`** (time, x, y, θ). |
| **`07_plot_motion_custom_style.py`** | **`plot_motion`** kwargs: `tire_linestyle`, `tire_linewidth`, per-corner colors, `draw_robot=False` (traces only). |

---

## Generated files (local, gitignored)

Outputs use the `adv_*` prefix and are listed in the **root `.gitignore`** so they are not committed by default:

- `adv_playback.log`, `adv_drive_to_pose.png`, `adv_mecanum_holonomic.png`, `adv_differential_wheels.png`, `adv_four_kinematics.png`, `adv_trajectory.csv`, `adv_plot_style.png`

Remove the `examples/advanced/adv_*` rule from `.gitignore` if you want to track them in git (e.g. for documentation figures).

---

## Ideas for your own code

- Swap **`log_options.file`** for a socket or queue if you stream logs outside the terminal.
- Combine **`06_export_trajectory_csv.py`** with pandas or another simulator for cross-checks.
- Use **`05_four_kinematics_subplots.py`** as a template for **paper figures** (tighten axes, `rcParams`, font sizes).
- Ackermann has **no** `drive_to_pose` in the library; plan arcs yourself or use `forward` / `turn_left` / `turn_right` as in **`live_ackermann_session.py`**.

For API reference, read the docstrings in `amr/motion.py`, `amr/plot_motion.py`, `amr/playback_log.py`, and `amr/live_motion.py`.
