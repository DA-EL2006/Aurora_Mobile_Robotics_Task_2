"""Advanced: one figure, four ``KinematicsModel``s — compare paths and contact traces.

Each subplot is a short scripted session; axis limits are independent. Useful for teaching
how geometry differs (two wheels vs four vs mecanum).
"""

from __future__ import annotations

import math
import os
from pathlib import Path

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")
here = Path(__file__).resolve().parent


def two_wheel() -> amr.MotionSession:
    s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)
    s.forward(0.7, 0.5)
    s.turn_left(math.pi / 3, 0.85)
    s.forward(0.4, 0.5)
    return s


def differential() -> amr.MotionSession:
    s = amr.MotionSession.create(
        amr.pose(0, 0, 0),
        amr.KinematicsModel.DIFFERENTIAL,
        dt=0.015,
        differential=amr.DifferentialParams(),
    )
    s.forward_wheels(0.7, 0.9)
    s.turn_right(math.pi / 4, 0.9)
    return s


def ackermann() -> amr.MotionSession:
    s = amr.MotionSession.create(
        amr.pose(0, 0, 0),
        amr.KinematicsModel.ACKERMANN,
        dt=0.02,
        ackermann=amr.AckermannParams(),
    )
    s.forward(0.8, 0.45)
    s.turn_left(math.radians(35), 0.65)
    s.forward(0.45, 0.4)
    return s


def mecanum() -> amr.MotionSession:
    s = amr.MotionSession.create(
        amr.pose(0, 0, 0),
        amr.KinematicsModel.MECANUM,
        dt=0.015,
        mecanum=amr.MecanumParams(),
    )
    s.forward(0.35, 0.5)
    s.strafe_right(0.25, 0.45)
    s.turn_left(math.pi / 5, 0.85)
    return s


def main() -> None:
    sessions: list[tuple[str, amr.MotionSession]] = [
        ("TWO_WHEEL (v, ω)", two_wheel()),
        ("DIFFERENTIAL", differential()),
        ("ACKERMANN", ackermann()),
        ("MECANUM", mecanum()),
    ]
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    for ax, (title, session) in zip(axes.flat, sessions):
        amr.plot_motion(session, ax=ax, show=False)
        ax.set_title(title, fontsize=10)
    fig.suptitle("Short paths — four kinematic models (same start pose)", y=0.98)
    fig.tight_layout()
    out = here / "adv_four_kinematics.png"
    fig.savefig(out, dpi=150)
    print("Wrote", out)


if __name__ == "__main__":
    main()
