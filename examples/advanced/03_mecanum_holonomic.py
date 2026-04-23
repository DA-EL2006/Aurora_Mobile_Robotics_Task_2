"""Advanced: Mecanum — strafe, custom ``mecanum_drive_wheels``, and a short ``drive_to_pose`` finish.

The built-in mecanum ``drive_to_pose`` is segment-limited; use a nearby goal and loose tolerances,
or build your own planner for tight goals.
"""

from __future__ import annotations

import math
import os
from pathlib import Path

import matplotlib.pyplot as plt
from amr.kinematics.integration import wrap_pi

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")
here = Path(__file__).resolve().parent


def main() -> None:
    m = amr.MecanumParams(half_length_y=0.26, half_width_x=0.2, max_wheel_speed=2.5)
    s = amr.MotionSession.create(
        amr.pose(0, 0, 0),
        amr.KinematicsModel.MECANUM,
        dt=0.012,
        mecanum=m,
    )
    s.forward(0.4, 0.55)
    s.strafe_right(-0.35, 0.5)  # negative distance → strafe left (body +x is “right”)
    s.mecanum_drive_wheels(0.5, 0.5, 0.2, 0.2, duration=0.5)
    # Finish with drive_to_pose: easy goal and tolerances (controller is intentionally simple)
    here_pose = s.pose
    goal = amr.pose(here_pose.x + 0.25, here_pose.y + 0.1, 0.25)
    s.drive_to_pose(
        goal,
        linear_speed=0.45,
        angular_speed=0.85,
        position_tol=0.12,
        angle_tol=0.15,
    )
    print("Final:", s.pose, "angle err vs goal", abs(wrap_pi(s.pose.theta - goal.theta)))

    fig, ax = plt.subplots(figsize=(6, 6))
    amr.plot_motion(s, ax=ax, show=False)
    ax.set_title("Mecanum: strafe + wheels + drive_to_pose")
    out = here / "adv_mecanum_holonomic.png"
    fig.savefig(out, dpi=150)
    print("Wrote", out)


if __name__ == "__main__":
    main()
