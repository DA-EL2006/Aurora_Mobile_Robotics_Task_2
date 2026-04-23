"""Advanced: use the stored ``poses`` (and time) as plain data — export CSV for another tool / plotting.

A ``MotionSession`` is not black box: ``session.poses`` is a list of ``Pose``; ``dt`` is fixed.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import AuroraMR as amr

here = Path(__file__).resolve().parent
out_csv = here / "adv_trajectory.csv"


def main() -> None:
    s = amr.MotionSession.create(amr.pose(0, 0, 0), amr.KinematicsModel.TWO_WHEEL, dt=0.02)
    s.forward(1.0, 0.5)
    s.turn_left(math.pi / 2, 0.9)
    s.forward(0.3, 0.45)

    with open(out_csv, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["t_sim", "x", "y", "theta_rad", "theta_deg"])
        for i, p in enumerate(s.poses):
            t = i * s.dt
            w.writerow([f"{t:.5f}", f"{p.x:.6f}", f"{p.y:.6f}", f"{p.theta:.6f}", f"{math.degrees(p.theta):.3f}"])

    print(f"Wrote {len(s.poses)} rows to {out_csv}")


if __name__ == "__main__":
    main()
