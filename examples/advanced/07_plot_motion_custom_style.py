"""Advanced: ``plot_motion`` visual tuning — tire linestyle, line width, and per-corner colors.

Set ``draw_robot=False`` if you only want the path and tire polylines.
"""

from __future__ import annotations

import math
import os
from pathlib import Path

import matplotlib.pyplot as plt

import AuroraMR as amr

os.environ.setdefault("MPLBACKEND", "Agg")
here = Path(__file__).resolve().parent


def main() -> None:
    s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.ACKERMANN, dt=0.02)
    s.forward(1.0, 0.4)
    s.turn_left(math.radians(50), 0.55)
    s.forward(0.5, 0.35)

    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    amr.plot_motion(
        s,
        ax=ax,
        show=False,
        draw_robot=False,
        tire_linestyle="--",
        tire_linewidth=1.6,
        rear_left_color="#1a237e",
        rear_right_color="#b71c1c",
        front_left_color="#1b5e20",
        front_right_color="#f57f17",
        center_color="#000000",
    )
    ax.set_title("Custom tire colors and linestyle (Ackermann)")
    out = here / "adv_plot_style.png"
    fig.savefig(out, dpi=150)
    print("Wrote", out)


if __name__ == "__main__":
    main()
